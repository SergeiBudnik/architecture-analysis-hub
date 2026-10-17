---
title: A2A — HLD Decisions & Traceability
sidebar_position: 7
---

# A2A Payment Integration: HLD and Decision Log

**Educational design companion** to [A2A QR and Deep Link Architecture](a2a-qr-deeplink.md).

## Architecture decision records

| ID | Decision | Alternative | Rationale |
|---|---|---|---|
| ADR-01 | Distinguish intent, attempt and merchant order | One mutable payment object | Allows retriable checkout without hiding external submissions |
| ADR-02 | Persist provider correlation before transitioning state | Stateless callback updates | Enables recovery of unknown outcomes |
| ADR-03 | Use verified provider callbacks and status inquiry | Success based on browser/app return | Return URL can be spoofed or abandoned |
| ADR-04 | Payment result outbox separate from financial processing | Deliver webhook inline, before acknowledging result | Merchant availability must not control payment outcome |
| ADR-05 | Store provider event IDs with dedupe key | Every callback causes downstream side effects | Providers can deliver more than once |
| ADR-06 | Unknown outcome is a first-class state | Treat HTTP timeout as failure | Prevents duplicate financial instructions |
| ADR-07 | Reconcile external and internal records | Trust only online callback path | Covers lost callback, late settlement or provider-side correction |

## Traceability matrix

| Requirement | Component | Test / evidence |
|---|---|---|
| A2A-FR-01 | Gateway, State Store | Concurrent duplicate creation test |
| A2A-FR-02 | Initiation Adapter, Checkout | Verify QR / app link carries opaque reference |
| A2A-FR-03 | Orchestrator | Browser return does not mark success |
| A2A-FR-04 | Callback Inbox, State Store | Duplicate/out-of-order callback tests |
| A2A-FR-05 | Recovery Worker | Lost response followed by status enquiry |
| A2A-FR-06 | Webhook Outbox | Merchant endpoint unavailable then delivered exactly once at application level, using consumer dedupe |

*Delivery may be at least once; exactly-once financial business effects require explicit idempotency and transaction design. The test is therefore for a single resulting business effect rather than exactly one HTTP delivery.*

## Failure-mode test pack

1. **Double-click payment:** repeated initiation with same key returns same intent.
2. **Provider timeout:** first submission persists UNKNOWN; no financial replay by default.
3. **Callback arrives before browser return:** merchant shows confirmed result after server status check.
4. **Two callbacks racing:** one guarded state transition and one downstream business outcome.
5. **Old callback after terminal success:** preserve terminal state, log conflict for review.
6. **Lost merchant webhook:** successful payment retained; outbox retries notification.
7. **QR expiry:** QR refresh/new attempt policy governed by provider rules, not blindly resubmitted.
8. **Cross-device change:** checkout status remains tied to intent, independent of device session.
9. **Provider inquiry unresolved:** bounded backoff and operational escalation.
10. **Reconciliation conflict:** explicit investigation case and auditable correction path.

## Synthetic fields for a lower-level design

| Entity | Fields |
|---|---|
| Intent | intent_id, merchant_id, merchant_order_id, amount_minor, currency, status, version |
| Attempt | attempt_id, intent_id, external_reference, channel, created_at, provider_status |
| Callback Inbox | provider_id, event_id, received_at, verified_at, payload_hash |
| Merchant Outbox | event_id, intent_id, destination, delivery_status, retry_at |
| Recovery Job | attempt_id, next_check_at, last_provider_status, retry_count |

This is a reference model, not a finished production database schema. Define retention, sensitive-data protection, uniqueness, referential integrity and transactional boundaries before implementation.