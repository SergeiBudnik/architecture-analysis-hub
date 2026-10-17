---
title: Event-Driven Payment Processing — ADR & Test Plan
sidebar_position: 16
---

# Event-Driven Payments: Architecture Decisions and Verification

**Author:** Sergei Budnik · **Scope:** synthetic fintech integration design (October 2026).

## 1. Architecture Decision Records

| ADR | Choice | Why / trade-off |
|---|---|---|
| EVT-ADR-01 | Commit payment state + outbox in one DB transaction | Prevent business update without recoverable event; adds relay complexity |
| EVT-ADR-02 | Consume into inbox with unique scoped event ID | At-least-once delivery requires duplicate suppression |
| EVT-ADR-03 | Commit offsets **after** durable business handling | Survives crash, but replays require dedupe |
| EVT-ADR-04 | Partition by stable business entity ID | Preserves per-partition order, not cross-topic/global order |
| EVT-ADR-05 | Use canonical versioned payment-domain events | Reduces downstream coupling; requires schema governance |
| EVT-ADR-06 | Keep processor inquiry separate from Kafka retry | Avoid duplicating financial instructions after unknown outcomes |
| EVT-ADR-07 | Retry transient failures, quarantine permanent errors | Limits poison-message stalls; requires operational ownership |
| EVT-ADR-08 | Isolate merchant webhook delivery from payment execution | Merchant outage cannot replay authorization |
| EVT-ADR-09 | Treat reconciliation as an independent authoritative check | Missing callback or broker event cannot imply settlement success |
| EVT-ADR-10 | Do not claim end-to-end “exactly-once” from Kafka alone | DB, HTTP, bank provider and merchant systems require separate controls |

## 2. Failure injection tests

| Test ID | Injected fault | Expected result |
|---|---|---|
| EVT-T01 | Crash just before DB commit | Event replayed; no partial state |
| EVT-T02 | Crash after DB commit before offset commit | Duplicate inbox no-op; no second business event |
| EVT-T03 | Outbox relay publishes then crashes | Kafka duplicate consumed once at business level |
| EVT-T04 | Two callback deliveries with same event ID | One guarded payment transition |
| EVT-T05 | Success followed by older pending status | Terminal success not overwritten |
| EVT-T06 | Broker unavailable when outbox relay publishes | Durable outbox backlog; eventual retry after recovery |
| EVT-T07 | Consumer-group rebalance in-flight | Unique DB state change, safe offset ownership |
| EVT-T08 | Invalid event schema | Durable quarantine and operational alert, no financial update |
| EVT-T09 | Retry topic reorders statuses | Version/transition guard prevents regression |
| EVT-T10 | Provider submission timed out | UNKNOWN + status enquiry, not blind re-submit |
| EVT-T11 | Merchant webhook unavailable for one hour | Merchant delivery retries; payment remains final |
| EVT-T12 | Recovery inquiry also unavailable | Bounded backoff, alert, audit; pending until authoritative evidence |
| EVT-T13 | 10,000 duplicate events | Unique business side effect; monitor suppression and lag |
| EVT-T14 | Outbox transaction committed but no relay | Dashboard alerts on unpublished age |
| EVT-T15 | Late reversal/refund after success | Separate financial lifecycle event, preserve original history |

## 3. Suggested SLO categories (fill before production)

| Dimension | Specify with real measurements |
|---|---|
| Event propagation | p95/p99 from DB commit to broker and consumer persistence |
| Consumer lag | Warning/critical thresholds per topic and partition |
| Unknown status age | Recovery initiation time and operational escalation deadline |
| Outbox age | Maximum tolerable unpublished event duration |
| DLQ backlog | Owner, triage time and safe replay controls |
| Webhook delivery | Retry duration, rate limits, signature rotation |
| Ledger correctness | Duplicate posting prevention and ledger balance checks |
| Data retention | Required report period and privacy constraints |

**No universal numeric SLO is asserted**; per-project business needs and provider contracts must determine thresholds.

## 4. Definition of Done for a production integration

- [ ] Provider-origin callback verified before business transition
- [ ] DB state, inbox and outbox committed atomically
- [ ] Duplicate events and concurrent consumers tested
- [ ] Consumer offset/rebalance/replay behavior tested after kill/restart
- [ ] Schema compatibility and topic-key strategy documented
- [ ] Broker outage and outbox backlog monitoring available
- [ ] DLQ replay approved, observable and idempotent
- [ ] Merchant webhook retries do not trigger new payment instructions
- [ ] Processor timeout always represented as unknown until resolved
- [ ] Reconciliation handles external status and financial mismatches
- [ ] Authorization, capture, clearing, merchant funding remain distinct
- [ ] PAN, secrets and sensitive personal data excluded from broker payloads/logs

See [PlantUML diagrams](event-driven-processing.md#7-editable-plantuml) and [reference SQL/event contracts](event-driven-contracts.md).