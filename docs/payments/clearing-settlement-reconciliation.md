---
title: Clearing, Settlement & Reconciliation
sidebar_position: 10
---

# Card Payments: Authorization → Capture → Clearing → Settlement → Reconciliation

**Author:** Sergei Budnik · **Release:** October 2026  
**Type:** Provider-neutral, synthetic architecture reference. All merchants, amounts, identifiers, reports and contracts are fictional. The article explains typical card acquiring concepts, not any particular card scheme's certified implementation, client documentation or actual business outcome.

## 1. Problem statement

A payment system must distinguish **permission to pay** from the **financial movement and accounting** that follows. Online approval does not mean the merchant has been funded. A resilient architecture must correlate the commercial order, authorization, capture, clearing records, settlement positions, merchant payout and reconciliation exceptions without conflating their status.

### The five key ideas

1. **Authorization:** An issuer or network returns an authorization decision. Approval may place a hold or reduce available balance, but no merchant funding is established solely by approval.
2. **Capture:** A merchant or platform finalizes an approved amount for financial submission under the acquirer/provider contract. Capture is not automatically interbank settlement.
3. **Presentment and clearing:** The acquirer submits financial records (often batched); the network exchanges/validates financial information and computes participant obligations according to the scheme's rules.
4. **Settlement:** Financial obligations are discharged between the relevant institutions using the rail or scheme settlement arrangement. **Merchant payout/funding** is a separate acquirer–merchant relationship and can occur on a different timetable.
5. **Reconciliation:** Independent records are matched and exceptions investigated across capture, presentment, scheme/acquirer reports, financial postings and bank payout data.

**Important distinctions:** Issuer cardholder posting is not the same as merchant funding. Clearing records are not a bank settlement confirmation. One issuer authorization may precede delayed capture, partial capture, void/reversal, or expiry; actual supported flows are contract-dependent.

## 2. Participants and responsibilities

| Participant / component | Responsible for | Key inputs and outputs |
|---|---|---|
| Cardholder / Shopper | Initiates purchase | Merchant checkout |
| Merchant / Order Service | Commercial order, goods fulfillment and capture policy | Order ID, capture request, payout reporting |
| Payment Gateway & Orchestrator | Routing, intent/attempt state, idempotency, technical correlation | Authorization and capture API |
| Acquirer / Processing Switch | Merchant acquiring interface, routing and records | Auth response, capture acceptance, presentment record, reports |
| Card Network | Routing, scheme clearing and settlement calculations | Scheme-defined authorization/clearing/position messages |
| Issuer | Authorization decision, cardholder account lifecycle | Approval/decline, cardholder posting, network positions |
| Capture / Presentment Service | Validate eligible captures, create durable financial submissions | Capture ID, capture amount, acquirer reference |
| Clearing Import / Export | Submit and import provider-specific financial records | Clearing batch IDs, item outcomes |
| Settlement Position Import | Consume position and funding reports | Currency, net position, cut-off / value date |
| Merchant Funding Service | Calculate and pay merchant per contract | Fee schedule, net payout, payout ID |
| Financial Ledger | Append-only double-entry or equivalent financial records | Posting IDs, balanced journals and audit |
| Reconciliation Engine | Match source-of-truth records, route exceptions | Match status, break reason and remediation |
| Payout Bank | Executes bank payout to merchant | Bank transaction ID, statement value date |

Exact settlement institutions and account arrangements differ by network, region and acquirer.

## 3. Lifecycle as one worked reference

**Scenario:** Fictional online store, single approved card payment, **manual capture**, one presentment and one merchant payout.

| Step | Sample state / amount | What it *means* |
|---|---|---|
| Merchant creates order | Order `O-101`, GBP 100.00 | Commercial obligation only |
| Issuer approves authorization | Auth `AUTH-201`, GBP 100.00 | Approved; **not yet captured or settled** |
| Merchant requests capture | Capture `CAP-301`, GBP 100.00 | Request for financial submission |
| Acquirer accepts capture | Processor ref `ACQ-401` | May be accepted for later clearing, not proof of bank settlement |
| Record is presented / cleared | Presentment `CLR-501`, GBP 100.00 | Scheme/acquirer financial record processed under applicable rules |
| Interbank settlement position closes | Position `SET-601` | Settlement is typically **aggregated/netted**, not one-to-one with this merchant transaction |
| Acquirer determines merchant payout | Gross GBP 100.00 – illustrative fees GBP 2.20 | Merchant contractual net = **GBP 97.80**, given this simplified fee model |
| Bank payout confirmed | `PAY-701`, GBP 97.80 | Merchant account funding under processor/acquirer payout rules |
| Reconciliation matches records | No exception | All expected financial items and identifiers accounted for |

The **GBP 2.20 fee is invented for arithmetic illustration**, not a real interchange or acquiring price. Interbank settlement positions cannot be inferred from this payout calculation.

## 4. Architecture boundaries and data ownership

Separate **payment authorization**, **capture**, **financial submission**, **settlement position**, and **merchant payout** as independent aggregates with explicit references.

| Aggregate | Example identifier | Authoritative evidence |
|---|---|---|
| Order | `O-101` | Merchant order database |
| Payment intent / attempt | `PI-101`, `PA-101` | Gateway/orchestrator |
| Authorization | `AUTH-201` | Mapped issuer/acquirer authorization result |
| Capture | `CAP-301` | Acquirer/processor capture confirmation and local command journal |
| Presentment / clearing item | `CLR-501` | Acquirer/scheme financial reports |
| Scheme/acquirer settlement | `SET-601` | Authoritative settlement reports/positions |
| Merchant payout | `PAY-701` | Acquirer funding report and bank confirmation |
| Reconciliation exception | `REC-801` | Reconciliation engine and investigation audit |

Use explicit `sourceSystem`, `externalReference`, `eventTime`, `processingTime`, `currency`, `amountMinor` and `recordVersion` fields where relevant. **Do not identify transactions by STAN alone.**

## 5. Synchronous vs asynchronous responsibilities

**Synchronous/API path:** merchant authorizes payment, receives issuer response, then submits capture subject to supported capture policy.

**Asynchronous/batch path:** clearing jobs submit/acquire records; reports are imported; settlement positions are posted; merchant funding is calculated; reconciliation identifies missing or conflicting entries. These paths frequently cross business-day, cut-off and time-zone boundaries.

### Conceptual API (not a scheme contract)

```http
POST /v1/payment-intents/PI-101/captures
Authorization: Bearer <merchant_access_token>
Idempotency-Key: 18ee2308-15df-4379-b334-480ea183ba31
Content-Type: application/json
```

```json
{
  "captureReference": "merchant-cap-101",
  "amountMinor": 10000,
  "currency": "GBP"
}
```

```json
{
  "captureId": "CAP-301",
  "status": "ACCEPTED_FOR_PROCESSING",
  "amountMinor": 10000,
  "currency": "GBP"
}
```

**Acceptance is not settlement.** A real API must define `400/401/403/409/422/5xx` conditions, capture eligibility, total capturable balance, partial/multiple capture support, refund/void rules, and recovery of ambiguous results.

### Example internal event (fictional)

```json
{
  "eventId": "evt-capture-301",
  "eventType": "CaptureAccepted",
  "captureId": "CAP-301",
  "authorizationId": "AUTH-201",
  "merchantId": "merchant-demo",
  "amountMinor": 10000,
  "currency": "GBP",
  "occurredAt": "2026-10-17T14:00:00Z"
}
```

Events should be emitted via a transactional outbox or equivalent durability guarantee; consumers use unique event IDs / business keys for deduplication. The example event name is an **internal design choice**, not a statement about network event formats.

## 6. What exactly gets reconciled?

| Match stage | Match keys | Typical exceptions |
|---|---|---|
| Auth → capture | Auth ref, attempt, currency, amount rules | Capture for wrong/expired auth, over-capture |
| Capture → presentment | Capture ref, acquirer/merchant ref, amount, transaction date | Missing or duplicate presentment, partial batch |
| Presentment → scheme/acquirer clearing | Clearing ID/batch, file sequence, network ref, amount | Rejected item, currency mismatch |
| Clearing → settlement position | Currency, value date, net position, report totals | Scheme charges, timing, FX, unsettled items |
| Acquirer settlement → merchant funding | Merchant ID, payout ID, fee breakdown, reserve, net amount | Missing fee, reserve, negative adjustment |
| Merchant funding → bank statement | Payout/bank reference, value date, bank account, net amount | Missing/late bank transfer, bank charges |

**Matching must reflect granularity:** scheme settlement is typically aggregate; don't attempt to match each authorization directly to one interbank settlement transfer.

## 7. Exceptional processing

| Exception | Action | Do not do |
|---|---|---|
| Authorization approved but not captured | Respect capture expiry/cancellation policy | Assume merchant was funded |
| Capture accepted but absent from clearing file | Query accepted batch/processor record and resubmit only if contractually safe | Duplicate financial presentment |
| Clearing file rejected | Identify rejection and retry corrected item under exact replay rules | Treat rejection as issuer decline |
| Partial capture | Track captured and remaining permitted amount | Automatically capture all remaining amount |
| Duplicate clearing row | Detect using financial identity and batch semantics | Book/pay same item twice |
| Settlement report missing | Keep expected position unconfirmed; escalate | Fabricate scheme settlement completion |
| Scheme settled but merchant payout delayed | Compare acquirer funding contract, holds/reserves and bank records | Equate scheme settlement with merchant funding |
| Refund or chargeback | Model independent financial adjustment linked to original transaction | Rewrite original authorized/captured history |
| FX conversion / rounding | Reconcile source amounts and converted positions with defined rates/rounding | Compare different currencies as same number |

## 8. Diagrams

- [Component HLD — acquiring to reconciliation (PlantUML)](https://github.com/SergeiBudnik/architecture-analysis-hub/blob/main/diagrams/clearing-settlement-hld.puml)
- [Authorization to merchant payout sequence (PlantUML)](https://github.com/SergeiBudnik/architecture-analysis-hub/blob/main/diagrams/clearing-settlement-sequence.puml)
- [Reconciliation and exception handling sequence (PlantUML)](https://github.com/SergeiBudnik/architecture-analysis-hub/blob/main/diagrams/clearing-reconciliation-sequence.puml)
- [Payment financial lifecycle state map (PlantUML)](https://github.com/SergeiBudnik/architecture-analysis-hub/blob/main/diagrams/clearing-lifecycle-state.puml)

For detailed arithmetic and matching rules see the [worked reconciliation example](reconciliation-worked-example.md); for controls and ADRs see [Architecture Decisions](clearing-design-decisions.md).

## 9. Design review checklist

- [ ] Auth, capture, clearing, scheme settlement, merchant payout and issuer posting have **separate lifecycle markers**
- [ ] Every financial command is idempotent in its business scope
- [ ] Technical acceptance is not mapped to funding confirmation
- [ ] Authoritative files/events and report cut-off times are identified
- [ ] Each clearing file has unique batch ID, checksum, sequence, item-level acknowledgement and replay policy
- [ ] Recon matches scheme/processor aggregate positions **at compatible granularity**
- [ ] Gross, fee, adjustment, reserve and net amounts reconcile with currency and value date
- [ ] Ledger entries are auditable and balanced; corrections are additive rather than destructive
- [ ] Missing bank credit is tracked independently of settlement position confirmation
- [ ] Chargebacks, refunds and negative settlement adjustments are handled as distinct financial flows

## Intended use

This is a reusable **training and design-review reference**, not bank-specific documentation. Actual scheme timeframes, permissible partial captures, settlement calendars, files, fees, account postings and financial rules must be confirmed from live provider contracts and schemes.
