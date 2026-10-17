---
title: Release Notes
sidebar_position: 6
---

# Release Notes

## 2026-10-17 — Event-driven payments and Kafka recovery

- Published [Event-Driven Payment Processing](payments/event-driven-processing.md), covering Kafka topology, topic keys, outbox/inbox, merchant notifications and processor recovery.
- Added [Kafka Offset Recovery Worked Example](payments/kafka-offset-recovery.md) with partition 7 / offset 184, DB commit versus offset commit and consumer rebalances.
- Added [Event Contracts & SQL](payments/event-driven-contracts.md), [ADRs and fault-injection tests](payments/event-driven-design-decisions.md).
- Added four editable PlantUML files for HLD, outbox/inbox, offset crash recovery and DLQ/manual re-drive.
- Reference models and synthetic records are educational; no scheme-specific or client-secret information is included.

## 2026-10-17 — Card financial lifecycle reference

- Published [Clearing, Settlement & Reconciliation](payments/clearing-settlement-reconciliation.md): roles, lifecycle and operational/financial boundaries.
- Added a [worked example](payments/reconciliation-worked-example.md): capture GBP 100, illustrative merchant net GBP 97.80 and a GBP 0.50 payout mismatch.
- Added [architecture decision records](payments/clearing-design-decisions.md), control tables, batch/row idempotency and verification tests.
- Added four editable PlantUML diagrams: financial HLD, lifecycle milestones, presentment/settlement sequence, reconciliation-break sequence.
- All identities and data are fictitious and independent of any customer/scheme specifications.

## 2026-10-17 — Payment architecture and diagrams

- Published provider-neutral end-to-end payment-processing architecture and sequence.
- Added intent state machine, idempotency guidance, timeout/retry and recovery patterns.
- Added three editable PlantUML source diagrams (HLD, payment sequence and payment state).
- Expanded architecture resources with API design patterns and an HLD deliverable checklist.
- Reference examples are synthetic; no real bank/customer system diagrams or production credentials are included.

## 2026-10-17 — Practical worked examples

- Added a fictional online travel booking BRD adapted from the authored BRD example.
- Added an employee XLSX export API specification and explanatory sequence diagram.
- Added a travel-plan hotel-removal backend specification and sequence diagram.
- Linked the worked examples from the public Template Catalogue.
- These examples are illustrative learning resources, **not deployed customer projects**.

## 2026-10-17 — Initial preview

- Established the open documentation portal structure.
- Added introductory guides for requirements, architecture and engineering specifications.
- Added a public catalogue showing which original templates remain under review.

Original source documents have not yet been publicly released. Future releases will document concrete changes, examples and independently verified feedback.
