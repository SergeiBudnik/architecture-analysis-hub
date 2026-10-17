---
title: Event Contracts, Outbox/Inbox SQL & Consumer Pseudocode
sidebar_position: 15
---

# Event-Driven Payment Integration — Reference Contracts

**Author:** Sergei Budnik · **Original synthetic teaching artifacts** (October 2026). Names and payloads are invented. Adapt field types, transactional boundaries and cryptographic controls to your own platform and provider.

## 1. Domain event envelope

The producer owns versioning; a consumer rejects unsupported payloads to controlled quarantine rather than guessing unknown financial meanings.

```json
{
  "eventId": "evt_demo_7001",
  "eventType": "PaymentOutcomeConfirmed",
  "schemaVersion": 1,
  "aggregateType": "PaymentIntent",
  "aggregateId": "pi_demo_1001",
  "aggregateVersion": 4,
  "occurredAt": "2026-10-17T17:00:00Z",
  "correlationId": "corr_demo_123",
  "causationId": "evt_demo_6999",
  "sourceService": "payment-state-service",
  "payload": {
    "intentId": "pi_demo_1001",
    "attemptId": "pa_demo_0101",
    "status": "SUCCEEDED",
    "amountMinor": 2599,
    "currency": "EUR",
    "providerReference": "ext_demo_821"
  }
}
```

Do not embed full card numbers, bank credentials, auth tokens, identity documents or other sensitive customer information. Prefer opaque references and restrict access, retention and log exposure.

### Envelope contract

| Field | Requirement |
|---|---|
| `eventId` | Unique business event ID; stable across delivery retries |
| `schemaVersion` | Explicit version; backward/forward compatibility policy |
| `aggregateId` | Business key appropriate for partitioning and state ownership |
| `aggregateVersion` | Used with transition/version guard to reject obsolete updates |
| `occurredAt` | Source time; not necessarily arrival order |
| `correlationId` | Trace one payment across services |
| `causationId` | Event or command that caused this event |
| `payload.status` | Canonical status backed by verified provider evidence |

## 2. Transactional storage sketch (PostgreSQL-style SQL)

```sql
CREATE TABLE payment_attempt (
  attempt_id VARCHAR(64) PRIMARY KEY,
  intent_id VARCHAR(64) NOT NULL,
  provider_reference VARCHAR(128),
  status VARCHAR(32) NOT NULL,
  version BIGINT NOT NULL DEFAULT 0
);

CREATE TABLE event_inbox (
  source_system VARCHAR(64) NOT NULL,
  event_id VARCHAR(128) NOT NULL,
  handled_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  PRIMARY KEY (source_system, event_id)
);

CREATE TABLE event_outbox (
  event_id VARCHAR(128) PRIMARY KEY,
  aggregate_id VARCHAR(64) NOT NULL,
  event_type VARCHAR(80) NOT NULL,
  payload JSONB NOT NULL,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  published_at TIMESTAMPTZ
);

CREATE INDEX idx_outbox_unpublished
  ON event_outbox (created_at)
  WHERE published_at IS NULL;
```

This SQL is **not production-ready**: add FK constraints, retention/partitioning, security, provider-specific uniqueness, worker claiming/leases and full audit controls. Some production outbox relays use CDC instead of a `published_at` flag.

## 3. DB-atomic event consumption

```text
consume(message):
  validate_schema(message)
  verify_source_and_correlation(message)

  BEGIN_DB_TRANSACTION
    inbox_inserted = insert_inbox_if_absent(
      source_system=message.sourceService,
      event_id=message.eventId
    )

    if inbox_inserted:
      attempt = select_attempt_for_update(message.attemptId)
      decision = validate_authoritative_transition(attempt, message)

      if decision == APPLY:
        update_attempt_status_and_version(attempt, message.status)
        insert_outbox_once(
          new_event_id=stable_business_transition_event_id(...),
          type="PaymentOutcomeConfirmed"
        )
      else:
        persist_investigation_if_needed(decision)
  COMMIT_DB_TRANSACTION

  commit_kafka_offset_only_after_db_commit()
```

**If the DB transaction fails, do not commit the offset.** After DB commit and before offset commit, replay is safe because the inbox record and state are already durable.

## 4. Outbox relay

```text
publish_outbox():
  records = claim_unpublished_rows_with_leases()

  for row in records:
    kafka_produce(
      topic = route_by_event_type(row.event_type),
      key = row.aggregate_id,
      value = row.payload,
      event_id = row.event_id
    )
    await_broker_ack()
    mark_outbox_published(row.event_id)
```

If the relay crashes **after broker acknowledgement but before `mark_outbox_published`**, it can publish twice. The downstream inbox must dedupe. Atomic DB-to-Kafka effects do not follow merely from `acks=all`, an idempotent producer or Kafka transactions.

## 5. Consumer offset settings (example only)

```properties
enable.auto.commit=false
auto.offset.reset=none
isolation.level=read_committed
```

- `auto.offset.reset=none` is a **strict provisioning choice** that fails if no valid offset exists; use explicit bootstrap/replay policy rather than copying it blindly.
- `isolation.level=read_committed` is relevant when consuming Kafka transactional writes; it does not make your external database transactional with Kafka.
- Producer reliability settings such as `enable.idempotence=true`, `acks=all` and appropriate retries strengthen **Kafka publication**, not issuer/processor financial replay safety.

## 6. Message compatibility and failure handling

| Change | Compatibility guidance |
|---|---|
| Add optional field | Often backward-compatible if consumers ignore unknown fields |
| Rename or change financial meaning | Breaking change; version contract and test every consumer |
| Change amount units/currency semantics | Treat as high-risk breaking change |
| Add event type | Consumers must have explicit unsupported-event behavior |
| Repartition or change key | Evaluate state ordering and offset migration |
| Extend retention | Security, privacy, storage and replay implications |

Schema Registry, Avro, JSON Schema and Protobuf are **options**, not requirements for every Kafka deployment. Define actual supported schema versioning and consumer compatibility rules.

## 7. Review references

[Event-driven HLD](event-driven-processing.md), [Offset recovery walkthrough](kafka-offset-recovery.md) and [Architecture Decisions](event-driven-design-decisions.md).
