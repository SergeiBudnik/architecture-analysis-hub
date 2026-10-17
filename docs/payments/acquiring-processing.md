---
title: Card Acquiring & Processing Architecture
sidebar_position: 8
---
# Card Acquiring and Processing — end-to-end reference architecture

**Author:** Sergei Budnik · **Release:** October 2026  
**Status:** original, fictional educational design using generic card-acquiring concepts. It is **not** a representation of a bank, a card scheme's proprietary message guide, or a customer implementation. No client configurations or secrets are included.

## 1. Architecture problem

A merchant needs to accept online card payments. A platform must securely receive payment initiation, route authorization to the acquiring side, communicate with network/issuer participants, and reliably report the outcome. It must also handle **unknown outcomes**, **duplicate submissions**, **void/reversal** and downstream **clearing and settlement** without assuming they all occur during authorization.

### Scope

**Included:** e-commerce card authorization, gateway, tokenization boundary, acquiring processor, switch/router, network/issuer, async notification, reversals, recovery and traceability.

**Not fully specified:** 3-D Secure protocol details, PCI DSS assessment, scheme-certified ISO 8583 profiles, regional interchange, network-specific presentment files, chargebacks, detailed capture and settlement calculations. These require scheme/acquirer-specific contracts.

## 2. HLD and ownership

| Component | Responsibility | Notable boundary |
|---|---|---|
| Shopper and merchant checkout | Purchase and payment experience, order state | Never treat browser return as proof of financial success |
| Merchant backend | Order identity, commercial fulfillment, webhooks | Owns order, **not** network authorization state |
| Payment gateway | Merchant API, validation, merchant authorization, risk routing | Prevent unauthorized/duplicate merchant requests |
| Tokenization / card vault | Tokenize sensitive card data in a controlled PCI scope | Minimize propagation of PAN/CVV |
| Payment orchestrator | Payment intent and attempt state; decision/route | Track authoritative upstream result |
| Acquirer / processing switch | Message mapping, connection management, routing to network | Own switch/processor references |
| Card network | Interoperability and routing between acquirer and issuer | Scheme-specific messaging and rules |
| Issuer | Cardholder account checks, authorization decision | Source of issuer authorization response |
| Recovery & reversal worker | Inquire/reconcile unknown attempts; apply scheme rules | Do not blindly repeat unknown money movement |
| Capture / clearing subsystem | Convert approved payments to presentment/financial claims | Separate authorization from financial completion |
| Reconciliation and ledger | Match internal and external reports/positions | Auditable amounts, statuses, corrections |

## 3. High-level authorization flow

1. Shopper initiates checkout; merchant establishes a unique `merchantOrderId`.
2. Merchant sends a request with an **idempotency key** to the payment gateway.
3. Sensitive card entry is **tokenized** through a compliant flow; backend exchanges references rather than card secrets.
4. Gateway validates merchant permissions, order and amount; orchestrator records an intent and one processing attempt.
5. Router/switch selects an acquiring route based on configured rules (capability, BIN/token metadata, availability and contracts).
6. Acquiring processor sends authorization to network; network routes to issuer.
7. Issuer returns approval or decline; response propagates back to gateway and merchant.
8. Orchestrator stores final/unknown state using guarded transitions. It returns an outcome to merchant and can publish a durable webhook.
9. Capture/presentment and settlement happen separately according to merchant/processor/scheme contracts.

**Important:** A processor's `accepted` or HTTP `200` may only acknowledge receipt, not an issuer approval. Define response mapping explicitly.

## 4. Conceptual API contracts

This API is illustrative and **not** a scheme interface.

```http
POST /v1/card-payment-intents
Authorization: Bearer <merchant-token>
Idempotency-Key: 819cbecf-138b-4ba4-9b28-90474525cc53
Content-Type: application/json
```

```json
{
  "merchantOrderId": "order-demo-2026-1017",
  "amountMinor": 1299,
  "currency": "GBP",
  "paymentMethodToken": "tok_demo_001",
  "captureMode": "MANUAL"
}
```

Illustrative response:

```json
{
  "intentId": "pi_card_1042",
  "attemptId": "pa_card_1042_1",
  "authorizationStatus": "APPROVED",
  "authorizationReference": "auth_demo_8591",
  "capturableAmountMinor": 1299
}
```

For ambiguous network outcomes return a state such as `UNKNOWN` / `PENDING_RECONCILIATION`, **not** an invented decline. Keep transport, gateway and network outcomes distinct.

## 5. ISO 8583 in an acquiring switch

ISO 8583 is a financial transaction messaging standard; field sets, message type indicators, processing codes and reversals vary by network and processor specifications. The following is **conceptual**, not an implementation-ready certified map.

| Concept | Illustrative ISO 8583 element | Engineering purpose |
|---|---|---|
| Authorization request / response | MTI such as `0100` / `0110` in common profiles | Distinguish request from issuer decision |
| Processing code | DE3 | Transaction type / account processing |
| Amount | DE4 | Transaction amount (format/currency context defined by profile) |
| System trace number | DE11 (STAN) | Correlate processing exchanges within defined scope |
| Retrieval reference | DE37 (RRN) | Cross-participant transaction correlation, where used |
| Approval code | DE38 | Issuer authorization identifier, where supplied |
| Response code | DE39 | Interpret issuer/network outcome using applicable profile |
| Terminal / merchant data | DE41 / DE42 | Identify accepting environment under profile rules |
| Currency | DE49 | Transaction currency |
| Reversal advice/request family | e.g. `0400` / `0420` profiles | Reverse or notify about an earlier authorization, per rules |

Do **not** implement ISO 8583 merely from these examples; MTIs and data element definitions are scheme-specific. The example makes no claim that every network uses the same messages.

### Correlation contract

Record `merchantOrderId`, `intentId`, `attemptId`, `gatewayRequestId`, switch transaction reference and applicable STAN/RRN pair with time, merchant, acquiring route and network context. **STAN alone is not globally unique.** Store normalized references securely.

## 6. Authorization, reversal and capture

| Event | What it means | Does it settle funds? |
|---|---|---|
| Authorization approved | Issuer permits the transaction under applicable rules | No |
| Authorization declined | Issuer/network has rejected the request | No |
| Timeout after dispatch | Final authorization result unknown locally | Unknown; do not infer decline |
| Authorization reversal / void | Request to release/reverse an existing authorization, when supported | Typically separate from financial settlement |
| Capture / presentment | Merchant/acquirer submits a transaction for financial processing | Not itself final interbank settlement |
| Clearing and settlement | Exchange of financial obligations and movement of funds | Settlement occurs under network/bank arrangements |

A **reversal is not a refund**: refund generally addresses an already financialized/settled charge, while reversal/void often cancels an authorization or submission subject to network rules.

## 7. Error and exceptional processing

| Scenario | Required platform behavior |
|---|---|
| Merchant repeats same request/key | Return same intent/outcome; reject key reuse with different payload |
| Switch rejects malformed request | Return mapped validation/processing rejection; do not claim issuer decline |
| Network or issuer declines | Persist mapped final decline with controlled reason |
| Switch/issuer timeout | Record UNKNOWN and initiate reconciliation/status inquiry |
| Lost issuer approval response | Seek authoritative processing records, possible reversal **only under specified contract/rules** |
| Duplicate/out-of-order callbacks | Inbox dedupe; optimistic locking / guarded state transitions |
| Merchant webhook offline | Outbox retry without resubmitting authorization |
| Capture duplicates | Enforce capture idempotency, amount controls and state constraints |
| Partial approval | Handle only when explicitly supported by channel and merchant contract |

### Recovery rules

1. Distinguish **transport-level timeout** from **final processor response**.
2. Persist attempt and correlation information before routing, when possible.
3. Query processing outcome through supported inquiry/reconciliation interface.
4. Initiate reversal/void only when business requirement and network contract authorize it.
5. Maintain reconciliation for late approvals, reversals and mismatched amounts.

## 8. Diagram package

- [Component HLD (editable PlantUML)](https://github.com/SergeiBudnik/architecture-analysis-hub/blob/main/diagrams/acquiring-hld.puml)
- [E-commerce authorization sequence](https://github.com/SergeiBudnik/architecture-analysis-hub/blob/main/diagrams/acquiring-authorization-sequence.puml)
- [Unknown outcome / reversal decision sequence](https://github.com/SergeiBudnik/architecture-analysis-hub/blob/main/diagrams/acquiring-timeout-reversal-sequence.puml)
- [ADR, acceptance scenarios and traceability](acquiring-design-decisions.md)

## 9. Architecture quality checklist

- [ ] Merchant order, intent, attempt, authorization and capture have distinct identifiers/states
- [ ] Scheme-certified interface/profile is the source of truth for MTIs, fields and reversals
- [ ] PCI scope, card tokenization and sensitive-data handling are reviewed
- [ ] Each network/issuer decline is distinguished from a connectivity failure
- [ ] Unknown outcomes survive restarts and are investigated
- [ ] Duplicate processing cannot create duplicate financial effects
- [ ] Capture and presentment do not run implicitly merely because authorization was approved
- [ ] Reconciliation links order → authorization → capture → clearing → settlement
- [ ] Merchant notifications are decoupled and auditable
- [ ] Routing/fallback and retry constraints are contractual and documented

**Use:** educational, provider-neutral architecture reference for technical review and training.

## Next step: financial lifecycle

Authorization alone does not settle a card payment. Continue to the [Clearing, Settlement & Reconciliation Architecture](clearing-settlement-reconciliation.md), including capture, financial presentment, interbank settlement, merchant funding and exception resolution.
