---
title: A2A Payments — QR and Deep Link Architecture
sidebar_position: 6
---

# A2A Payments: QR Code, Deep Link and Payment Orchestration

**Author:** Sergei Budnik  
**Type:** Synthetic, provider-neutral architectural case study (October 2026). This is a newly authored educational reference based on general payment architecture experience. It is **not** a reproduction of any customer, bank, or RoPay implementation.

## 1. Problem and scope

A merchant needs a bank-account-based (A2A) checkout that works in a browser, on a smartphone and at a physical point of sale. The checkout platform must provide a payment initiation journey by **QR code** (cross-device or POS) and **deep link / app link** (same-device), and it must reliably resolve the final payment outcome even when the bank app or a callback is delayed.

This example models payment initiation and outcome orchestration. It does **not** assume a particular country's rail, scheme, settlement model, app-link format or legal framework. Authentication, authorization and finality are provider-specific.

### Functional requirements

| ID | Requirement | Acceptance criterion |
|---|---|---|
| A2A-FR-01 | Merchant creates a payment intent | Same idempotency key and identical payload cannot create two intents |
| A2A-FR-02 | Platform presents a QR or approved mobile app link | Channel-specific link/QR includes only an opaque or provider-authorized reference |
| A2A-FR-03 | Platform tracks pending outcome | User return or link open does not imply success |
| A2A-FR-04 | Validated asynchronous callback updates the attempt | Duplicate and out-of-order events do not duplicate transition or posting |
| A2A-FR-05 | Unresolved outcome triggers status enquiry | Timeout leads to UNKNOWN/PENDING, not an assumed decline |
| A2A-FR-06 | Merchant receives durable outcome event | Webhook retry does not repeat the underlying transfer |

### Non-functional decision register

| Dimension | Architectural decision to establish |
|---|---|
| Security | AuthN/AuthZ for merchant requests; verify callback authenticity; use short-lived opaque references |
| Reliability | Durable intent/attempt store, transition guards, event inbox and webhook outbox |
| Observability | Correlation across order, intent, attempt and provider reference |
| Scalability | Separate synchronous initiation from callback and background recovery |
| Privacy | Avoid full account details, tokens or personal data in URLs, QR and logs |
| Resilience | Provider-specific timeout budgets and bounded retry/backoff |
| Integrity | Monetary amounts expressed in minor units with currency; do not trust redirect parameters as proof of payment |

## 2. Logical component architecture

| Component | Responsibility | Key API / event |
|---|---|---|
| Merchant Backend | Own cart/order and commercial fulfillment | Create intent; consume webhook |
| Checkout UI / POS | Display QR or launch link; poll merchant-facing status | Display initiation payload |
| Merchant API Gateway | Authenticate merchant and validate request | HTTPS |
| Payment Orchestrator | Own intent/attempt, choose provider/channel, coordinate outcome | Internal commands |
| Initiation Adapter | Create provider payment; map checkout instructions | Provider HTTPS |
| External Payment Provider | Issue initiation reference / instructions and authoritative payment status | Provider-specific |
| Payer Banking App | Payer authentication and consent | Scheme-dependent |
| Payment State Store | Durable intent and attempt state, versioned transitions | Transactional persistence |
| Callback Inbox | Authenticate, dedupe and consume provider notifications | Signed webhook / event |
| Recovery Worker | Query unknown attempts; escalate unresolved cases | Provider status API |
| Merchant Webhook Outbox | Publish outcome reliably and independently | Asynchronous HTTPS |
| Reconciliation | Match authoritative external reports with internal payment records | Scheduled/batch/event |

**Trust boundaries:** Merchant↔Platform; Platform↔Provider; Provider↔Bank; external callback↔Platform. The app's return URL is only a UX signal, not a settlement or success confirmation.

## 3. Two initiation journeys

### A. QR (POS or cross-device)

1. Merchant creates payment intent and receives a channel-independent intent ID.
2. Orchestrator creates an attempt with provider reference and receives a **provider-approved checkout URI or opaque token**.
3. Checkout displays QR encoding that URI/token; the QR is **not** generated from sensitive bank credentials.
4. Payer scans the QR, opens the banking/approved payment app and confirms the payment.
5. Provider sends a verifiable outcome callback or exposes status via inquiry.
6. Orchestrator applies a guarded state transition, then merchant webhook is sent asynchronously.

### B. Deep link (same-device)

1. Merchant's mobile checkout requests an initiation action.
2. Provider supplies the permitted app link / universal link.
3. Client opens the link. A missing app requires an explicit supported fallback (e.g. QR or website).
4. App returns to merchant via return URL **only to resume UX**.
5. Merchant checks platform status; fulfillment occurs only after confirmed authoritative success.

## 4. Conceptual contracts — educational only

```http
POST /v1/payment-intents
Authorization: Bearer <merchant_access_token>
Idempotency-Key: <uuid>
Content-Type: application/json
```

```json
{
  "merchantOrderId": "order-demo-1042",
  "amountMinor": 2599,
  "currency": "EUR",
  "preferredMethod": "A2A",
  "channel": "MOBILE_WEB"
}
```

Successful initiation example:

```json
{
  "intentId": "pi_demo_1042",
  "attemptId": "pa_demo_0001",
  "status": "AWAITING_CUSTOMER",
  "checkout": {
    "type": "APP_LINK",
    "uri": "https://pay.example.invalid/checkout/opaque-demo-token",
    "expiresAt": "2026-10-17T19:30:00Z"
  }
}
```

For QR, the checkout type can be `QR_URI`; the merchant renders the **provider-approved URI** as a QR code. `example.invalid` is a reserved, non-working placeholder, not a real provider.

Status enquiry:

```http
GET /v1/payment-intents/pi_demo_1042
Authorization: Bearer <merchant_access_token>
```

```json
{
  "intentId": "pi_demo_1042",
  "status": "PROCESSING",
  "attemptId": "pa_demo_0001",
  "lastUpdatedAt": "2026-10-17T19:20:00Z"
}
```

**Design choices to validate in a real project:** amount/currency agreement between merchant and provider; expiration clock; method availability; SCA, refund model, cancellation semantics, dispute handling and provider-defined state mapping.

## 5. Error paths and resolution

| Situation | Local state | Correct response |
|---|---|---|
| Provider rejected request before execution | FAILED only if authoritative | Return error; record reason |
| Create call times out after dispatch | UNKNOWN / PENDING | Status enquiry using correlation/provider reference |
| Customer closes banking app | AWAITING_CUSTOMER / PROCESSING | Do not infer failure from app closure |
| User returns via deep link | No automatic financial state change | Query backend status |
| Duplicate or stale callback | Preserve current guarded state | Dedupe, acknowledge safely |
| Merchant webhook unavailable | Confirmed status retained | Retry webhook delivery from outbox |
| Local expiry but provider later reports success | Exception investigation | Resolve by authoritative rules and reconciliation |
| Confirmed debit but internal platform lacks confirmation | UNKNOWN → recover | Query provider and compare records; do not resubmit |

## 6. Diagram sources

- [Component HLD (PlantUML)](https://github.com/SergeiBudnik/architecture-analysis-hub/blob/main/diagrams/a2a-qr-deeplink-hld.puml)
- [QR payment sequence (PlantUML)](https://github.com/SergeiBudnik/architecture-analysis-hub/blob/main/diagrams/a2a-qr-sequence.puml)
- [Deep-link + timeout recovery (PlantUML)](https://github.com/SergeiBudnik/architecture-analysis-hub/blob/main/diagrams/a2a-deeplink-recovery-sequence.puml)

See [Integration review checklist](../templates/integration-specification.md), [Transaction state machine](state-machine.md) and [Timeout and recovery patterns](reliability.md).

## 7. Architecture review checklist

- [ ] Bank/provider integration contract identified and reviewed
- [ ] QR and deep link contain no sensitive credentials
- [ ] Same-device and cross-device behavior covered
- [ ] Return URL treated only as a UX signal
- [ ] All financial state changes sourced from verified provider evidence
- [ ] Idempotency scope and retention documented
- [ ] Concurrency between status polling and callbacks controlled
- [ ] Merchant notification handled by a durable outbox
- [ ] Reconciliation/reporting and late-status resolution owned by a team
- [ ] Logs and error payloads do not expose secrets or personal data

## About this reference

This document is intended for **education and design review**. It contains fictional identifiers and intentionally generic providers. No claims are made about a particular client architecture, scheme certification or production implementation.