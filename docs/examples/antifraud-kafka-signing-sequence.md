---
title: Sequence — Kafka, Fraud Decision & Signing
sidebar_position: 21
---

# Transaction Analysis Flow: Kafka → Antifraud → Signature Service

**STORAGE source:** `SEQUENCE_EXAMPLES.docx`, Example #3, titled **Transaction Analysis Flow**. The source includes a repeated PlantUML sequence with four participants: Integration Platform, Kafka, Antifraud and a named signing provider. The public edition retains the flow but replaces the named signing vendor with **Signature Service**.

## Main source flow

1. Integration platform puts a transaction-analysis request on Kafka.
2. Antifraud consumes the request.
3. On a technical processing failure, the message is routed to a DLQ.
4. On success, antifraud evaluates risk/rules and publishes a decision, score and triggered-rule details.
5. The integration platform consumes the response.
6. If the platform cannot process the response, it publishes a DLQ record.
7. The platform prepares the downstream customer/partner result.
8. It requests signing from an external signature service.
9. The signature service returns a signed result or file reference.

**Source-quality clarification:** The original step 1 says “creates a topic for transaction analysis”. This appears to describe **publishing a message to a pre-existing Kafka topic**, not provisioning a fresh topic for each payment. The public sequence uses the latter interpretation explicitly as a correction, not a claim about the historical source.

## Participants and message ownership

| Component | Ownership |
|---|---|
| Integration Platform | Create correlated request, consume result, invoke signer |
| Kafka | Transport analysis request/response across consumer groups |
| Antifraud | Risk evaluation and decision result |
| Signature Service | Sign normalized response under a valid contract |
| Operations / DLQ | Control poison-message review and safe redrive |

## Example event envelope (fictional)

- `eventId`: unique delivery identity
- `transactionReference`: opaque correlation to payment/analysis attempt
- `analysisResult`: `APPROVE`, `REVIEW` or `REJECT`
- `riskScore`: numeric outcome if allowed by contract
- `rulesTriggered`: non-sensitive rule references

**Do not** expose confidential fraud rules, raw PAN, authentication material or user identifiers in public Kafka event samples.

## Failure and security review (new)

- Require **durable consume-before-offset-commit** behavior with consumer inbox dedupe.
- Distinguish transient technical errors from final business fraud decisions.
- Route DLQ only after durable quarantine handoff, with correlation and operations ownership.
- Do not silently generate a client success response if antifraud or signing status is unknown.
- Verify signing provider authorization, response format, nonrepudiation requirements and timeout handling.

## Editable sequence

[Download Kafka fraud analysis and signing (.puml)](https://github.com/SergeiBudnik/architecture-analysis-hub/blob/main/diagrams/storage-kafka-antifraud-signing.puml).

**Related:** [Event-driven Processing](../payments/event-driven-processing.md) · [Kafka Offset Recovery](../payments/kafka-offset-recovery.md) · [CC BY 4.0](../license.md).
