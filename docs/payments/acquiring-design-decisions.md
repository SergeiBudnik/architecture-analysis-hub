---
title: Acquiring — Design Decisions, Tests & NFRs
sidebar_position: 9
---
# Acquiring & Processing: Architecture Decisions and Verification

**Author:** Sergei Budnik · **Status:** synthetic educational engineering supplement.

## Architecture decision records

| ADR | Decision | Trade-off / rationale |
|---|---|---|
| CARD-ADR-01 | Separate merchant order, payment intent, attempt, authorization and capture | More objects but truthful lifecycle and simpler recovery |
| CARD-ADR-02 | Maintain tokenization / PCI boundary | Reduces sensitive-data handling beyond necessary scope |
| CARD-ADR-03 | Processor adapter maps an explicit canonical contract to scheme-specific formats | Reduces core coupling; requires adapter conformance testing |
| CARD-ADR-04 | Record route and transaction correlation | Supports disputes, recovery and acquirer reconciliation |
| CARD-ADR-05 | UNKNOWN is not equivalent to decline | Prevents duplicate routing of uncertain financial commands |
| CARD-ADR-06 | Conditional reversal on supported contract, not blanket timeout reversal | Reversal requirements differ by network and stage |
| CARD-ADR-07 | Deliver merchant updates via durable outbox | Merchant downtime does not affect network processing |
| CARD-ADR-08 | Capture is a separately authorized operation | Makes delayed capture, amount limits and settlement lifecycle explicit |

## Functional requirements and tests

| ID | Requirement | Expected proof |
|---|---|---|
| CARD-FR-01 | Idempotent initiation | Same request + key maps to one intent/attempt |
| CARD-FR-02 | Record route/correlation | Switch and gateway logs agree on identifiers |
| CARD-FR-03 | Preserve issuer response meaning | Approval/decline/error codes mapped under actual interface profile |
| CARD-FR-04 | Handle unknown result | Lost-response simulation produces UNKNOWN and recovery work |
| CARD-FR-05 | Prevent duplicate capture | Same capture key produces one financial effect |
| CARD-FR-06 | Independently retry webhook | Merchant unavailable → durable retry without new authorization |
| CARD-FR-07 | Reconcile settlement | Matched internal, processor and external references |

## Failure test suite

1. **Concurrent duplicate authorization:** two identical merchant calls yield one downstream attempt.
2. **Conflicting idempotency key:** same key, different amount is rejected.
3. **Issuer decline:** negative network outcome appears as a decline, not a platform failure.
4. **Processor timeout after dispatch:** attempt marked UNKNOWN; no blind replay.
5. **Lost approval response:** inquiry/reconciliation can resolve a late success.
6. **Reversal requested:** operation uses contract-defined references and validates permitted state.
7. **Late reversal response:** stored without overriding unrelated capture/settlement events.
8. **Provider callback twice:** one guarded business transition.
9. **Partial capture (where supported):** amount and remaining authorization limits validated.
10. **Merchant outage:** authorization outcome remains durable; webhook retries later.

## NFR template

| Dimension | Define for real deployment |
|---|---|
| Processing availability | SLO per ingress, gateway and processor adapter |
| Latency | p95/p99 authorization, with issuer/provider budgets |
| Throughput | Peak TPS and load profile |
| Recovery | Maximum tolerated UNKNOWN age and inquiry window |
| Security | Tokenization, encryption, least privilege, PCI controls |
| Auditing | Traceability of routing, state change, capture and reversal |
| Data retention | Policy for identifiers, events and sensitive data |
| Failover | Provider fallback **only when duplicating the financial request is demonstrably safe** |

## Traceability

| Requirement | Component | Verification |
|---|---|---|
| CARD-FR-01 | Gateway, Intent Store | Concurrency/idempotency test |
| CARD-FR-02 | Processor Adapter | Route correlation audit |
| CARD-FR-03 | Adapter, State Engine | Scheme-profile mapping test |
| CARD-FR-04 | Recovery Worker | Timeout fault injection |
| CARD-FR-05 | Capture Service | Duplicate capture test |
| CARD-FR-06 | Webhook Outbox | Delivery resilience test |
| CARD-FR-07 | Reconciliation | Synthetic external report comparison |

**Note:** This is a generic template. Certified acquiring implementation requires actual scheme and acquirer specifications, security review, and operations approval.

[Back to Acquiring Architecture](acquiring-processing.md).