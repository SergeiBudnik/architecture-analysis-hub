---
title: Backend SRS — Card Blocking
sidebar_position: 18
---

# Backend SRS: Card Blocking and Legacy Client Compatibility

**Source:** \`BACK_SRS_EXAMPLE_2.docx\`, STORAGE library v1.0.0 (September 2025). The original specifies \`POST card/block\`, legacy/new mobile-client behavior, a mandatory card identifier, card-reason values, card-network routing, card-state persistence and success/error mapping. This is a new **bank-neutral educational edition**: production endpoint paths, support contacts, exact internal database names, numeric status dictionaries and sample credentials are deliberately omitted.

## 1. Purpose and business behavior

Allow an authenticated customer to block a card for reasons such as temporary customer block, **lost** or **stolen**. The sample supports two client-contract generations with different input parameters.

## 2. Compatibility model from the source

| Caller | Incoming information | Back-end behavior |
|---|---|---|
| Legacy client | Card identifier and SMS confirmation, no explicit \`cardStatus\` | Verify an OTP/SMS challenge; infer the default customer-block reason |
| New client | Card identifier and explicit \`cardStatus\` reason | Process the reason and apply the new client verification contract |
| Invalid caller / card | Unauthenticated, unauthorized, unknown or ineligible card | Reject without changing card status |

**Important:** Skipping SMS in the newer branch is part of the original example's flow; it is **not** a recommendation to remove authentication or step-up verification. A production implementation must define permitted actions and security policy for each client version.

## 3. Public conceptual request

\`\`\`http
POST /v1/cards/{cardId}/block
Authorization: Bearer <access_token>
Content-Type: application/json
Idempotency-Key: <uuid>
\`\`\`

\`\`\`json
{
  "cardStatus": "LOST",
  "reason": "Card cannot be located"
}
\`\`\`

The endpoint, \`reason\` and idempotency header are **public illustrative additions**, not an exact replica of the source interface.

## 4. Processing steps

1. Validate caller and ownership of the card.
2. Resolve client-contract version and required verification mechanism.
3. Validate card identifier and eligible lifecycle transition.
4. Map normalized block reason to provider/processor-specific status.
5. Select the supported card-processing destination.
6. Invoke processor card-status operation with protected correlation.
7. **Only after a confirmed positive result**, update local card state and emit an auditable event.
8. When a provider outcome is ambiguous, inquire/reconcile before assuming failure or reissuing the command.

The original names Visa/UnionPay route selection. Its precise processor-specific mapping values and card-table enumeration are excluded from this public contract.

## 5. Business status mapping

| Incoming intent | Canonical public status |
|---|---|
| Temporary customer block | \`BLOCKED_BY_CARDHOLDER\` |
| Lost card | \`LOST\` |
| Stolen card | \`STOLEN\` |

A real processor may require entirely different numeric/textual reason codes; the adapter owns that translation.

## 6. Error and recovery scenarios

| Failure | Required behavior |
|---|---|
| Card cannot be found | No status update; controlled customer-facing not-found error |
| User lacks card ownership | Reject before external call |
| Verification invalid or expired | Request re-verification |
| Processor returns explicit rejection | Preserve original local status |
| Network timeout after dispatch | Store pending/unknown command, attempt provider status resolution |
| Duplicate card-block command | Idempotency and status guards prevent uncontrolled repeated side effects |
| Provider success but local update fails | Repair local projection from authoritative provider status, with audit |

The original error table includes exact issuer-specific numeric codes and support contacts. Those are not valid generic backend error codes.

## 7. Editable sequence

[Download card-block processing sequence (PlantUML)](https://github.com/SergeiBudnik/architecture-analysis-hub/blob/main/diagrams/storage-card-block-backend-sequence.puml).

[Blank Backend SRS](../templates/backend-srs-template.md) · [Idempotency and state patterns](../payments/state-machine.md) · [CC BY 4.0](../license.md).
