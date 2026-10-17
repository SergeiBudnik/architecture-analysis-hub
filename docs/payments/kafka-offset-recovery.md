---
title: Kafka Consumer Offsets & Recovery — Worked Example
sidebar_position: 14
---

# Kafka Consumer Offsets: What Happens When a Payment Event Is Lost or Replayed?

**Author:** Sergei Budnik · **Fictional scenario**, October 2026.

## 1. The example

Assume `payments.attempt.status.v1` has partition **7**, and consumer group `payment-state-service` receives record at offset **184**:

| Field | Sample value |
|---|---|
| Topic | `payments.attempt.status.v1` |
| Partition | `7` |
| Record offset | `184` |
| Committed group offset before processing | `184` (next record to fetch) |
| Kafka key | `pa_demo_0101` |
| Event ID | `evt_provider_9021` |
| Attempt ID | `pa_demo_0101` |
| Reported status | `SUCCEEDED` |
| DB before event | `PROCESSING` |

**Offset semantics:** The committed offset tracks the *next* record to consume for the partition. After durably processing offset 184, the consumer commits **185**. It is a progress marker, **not** an acknowledgement to the upstream bank and not proof of payment settlement.

The consumer should run with **automatic offset commits disabled** for this illustrative pattern. Real frameworks may implement acknowledgements through their own transactional abstractions; the invariant is the same.

## 2. Safe handler order

1. Poll record and validate required fields/schema.
2. Verify event provenance and correlate an existing payment attempt.
3. Begin a database transaction.
4. Insert unique inbox key (`sourceSystem + eventId`); on duplicate, avoid repeated effects.
5. If first receipt: lock/version-check attempt, validate allowed state transition, update attempt.
6. In that **same transaction**, append an outbox `PaymentOutcomeConfirmed` event when a new business outcome was applied.
7. Commit the database transaction.
8. Only after successful DB commit, commit the Kafka consumer offset to **185**.
9. Outbox relay independently delivers downstream events; Kafka may redeliver and downstream consumers must deduplicate.

An inbox unique key by itself is not enough: state update, inbox record and outbox insert must form **one atomic unit** or otherwise have an equivalent recovery design.

## 3. Four failure timings

| When failure occurs | DB state | Offset | What happens on restart? |
|---|---|---|---|
| Before DB transaction commit | No durable state update | Still 184 | Event 184 replayed and processed |
| After DB commit but before offset commit | Updated to SUCCEEDED, inbox committed | Still 184 | Event 184 replayed; inbox identifies duplicate; consumer commits 185 |
| After offset commit | Durable state update | 185 | Consumer resumes at next record |
| Kafka broker unavailable when committing offset | DB committed | Still 184 until retry/rebalance | Replay possible; inbox prevents second financial effect |

**Crucial:** If offset 185 is committed before state/outbox are durable and the service crashes, Kafka can skip the needed update on restart. The library explicitly recommends **DB-first, offset-second**, plus replay-safe inbox.

## 4. Consumer-group rebalance and ordering

A partition can be assigned to another consumer instance during rebalances. Two workers may briefly have overlapping in-flight processing unless handlers respond correctly to revocation and stale workers are fenced.

- Keep work bounded; stop accepting new tasks for revoked partitions.
- Commit only offsets belonging to currently assigned partitions under the consumer framework's protocol.
- Use a transactional database state version/unique constraint to protect against duplicate effects even if a stale worker finishes.
- Process records in partition order or track **contiguous completed offsets** before committing; do not commit past an unfinished lower offset.
- Partition key does not guarantee event-time ordering across independent topics or external provider callbacks.
- Late or out-of-order provider statuses need guarded state transitions independent of broker offsets.

## 5. A specific out-of-order payment example

Events arrive as follows:

| Delivery | Event | Source status | Current local status | Decision |
|---|---|---|---|---|
| 1 | `evt-9` | SUCCEEDED | PROCESSING | Apply success |
| 2 | `evt-8` (late) | PROCESSING | SUCCEEDED | Do not regress terminal state; record as stale |
| 3 | `evt-9` (duplicate) | SUCCEEDED | SUCCEEDED | Inbox dedupe; no duplicate ledger entry |

A financial correction or reversal after settlement is not modeled by rewriting `SUCCEEDED` to `FAILED`. Use a linked reversal/refund/adjustment lifecycle governed by the provider's actual rules.

## 6. Retry topics, pause-and-retry and DLQ

| Failure type | Strategy |
|---|---|
| Database temporarily unavailable | Pause partition or use bounded retry without committing unprocessed record |
| Schema incompatible / permanent invalid payload | Quarantine with original metadata, error class and audit; commit source offset only after durable quarantine handoff |
| Provider inquiry unavailable | Schedule bounded recovery based on authoritative reference; **never automatically create a new payment** |
| Duplicate valid delivery | Finish as successful no-op after validation, commit offset |
| Merchant webhook unavailable | Delivery queue and webhook backoff, not Kafka payment replay |
| Unknown consumer exception | Alert and preserve replayability; respect per-key ordering requirements |

Retry topics can allow later records to proceed while an earlier record waits; this may **break ordering** for one key. Either preserve ordering through partition pause, or design events/transition guards to tolerate the reorder. DLQ is an operational control, not an automatic financial-error resolution.

## 7. Offset recovery PlantUML

See [Kafka offset crash recovery sequence](https://github.com/SergeiBudnik/architecture-analysis-hub/blob/main/diagrams/event-driven-offset-recovery-sequence.puml).

## 8. Operational dashboards

Track lag by topic-partition and consumer group; age of the oldest unprocessed event; outbox rows awaiting publish; poison/DLQ counts; status UNKNOWN age; provider status-inquiry rate; duplicate suppression rate; and reconciliation breaks. Metrics must exclude PAN, credentials and sensitive customer data.

**Review criterion:** For every crash point, be able to prove no lost business outcome and no duplicate financial/ledger effect, not merely that “Kafka retried”.
