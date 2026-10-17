---
title: MQ Example — Email Notification Consumer
sidebar_position: 6
---

# Worked Example: Queue-Driven Email Notification Service

**Public adaptation of:** `MQ_SRS_EXAMPLE.docx` from the STORAGE library (2025).  
**Source-based features:** Inbound JSON notification message; request correlation; email-provider mapping; retry with growing delay; business response handling; failure logging; and a dead-letter queue (DLQ).

Names of internal services, task references and error-code lists have been replaced with fictional equivalents. Illustrative payloads below are **not** quoted from the original system.

## 1. Component and trigger

| Field | Value |
|---|---|
| Consumer | `email-notification-consumer` |
| Input queue | `notification.email.requested` |
| Event | New email-delivery request |
| External dependency | Generic Email Provider API |
| Failure queue | `notification.email.dead-letter` |

The consumer sends notifications independently of an order, login or payment request.

## 2. Synthetic incoming message

```json
{
  "eventId": "evt-email-demo-0007",
  "type": "CUSTOMER_NOTIFICATION",
  "recipient": {"email": "reader@example.invalid"},
  "data": {"template": "order-updated", "reference": "O-101"},
  "createdAt": "2026-10-17T12:00:00Z"
}
```

`example.invalid` is a deliberately non-deliverable documentation domain.

## 3. Message mapping

| Input field | Provider field | Rule |
|---|---|---|
| `eventId` | `externalEventId` | Preserve stable ID for dedupe and correlation |
| `type` | `templateCode` | Map through approved template registry |
| `recipient.email` | `to` | Validate address and minimize logging |
| `data` | `templateData` | Allow-list fields; do not log secrets |

## 4. Processing algorithm

1. Consume message and validate schema, recipient and template.
2. Atomically claim a dedupe key for the event in the notification store.
3. Submit the message to the email provider under supported idempotency semantics.
4. On explicit success, persist delivery result and acknowledge the message.
5. On a transient provider failure, schedule a bounded retry with backoff.
6. On a permanent rejection or exhausted retry budget, persist an incident and move to a durable DLQ.
7. Acknowledge the source message only after the delivery result or retry/quarantine is durably recorded.

If the provider response is **ambiguous**, investigate its delivery status before replaying unless its contract guarantees safe deduplication. Email notifications should not be confused with financial payment instructions.

## 5. Failure matrix

| Condition | Action |
|---|---|
| Missing required field | Reject to quarantine with reason |
| HTTP 429 or transient 5xx | Retry under rate limit with exponential backoff and jitter |
| Permanent 4xx | Record failure; DLQ/manual review as appropriate |
| Worker crashes after provider response | Dedupe/status recovery to limit duplicate sends |
| DLQ re-drive | Operator-approved, idempotent and auditable |

The source's exact retry range and processor-specific error codes are deliberately **not reproduced as universal defaults**.

## 6. Design references

- [Editable PlantUML sequence](https://github.com/SergeiBudnik/architecture-analysis-hub/blob/main/diagrams/storage-adapted-email-consumer-sequence.puml)
- [MQ specification template](../templates/message-broker-spec-template.md)
- [Event-driven reference architecture](../payments/event-driven-processing.md)

**License:** [CC BY 4.0](../license.md) for this public authored adaptation.