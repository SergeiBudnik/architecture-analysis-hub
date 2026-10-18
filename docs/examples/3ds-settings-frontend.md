---
title: Frontend SRS Example — 3-D Secure Settings
sidebar_position: 9
---

# Frontend SRS: Manage 3-D Secure Email Settings

**Based on:** STORAGE \`FRONT_SRS_EXAMPLE.docx\` (2025-09-04). This public edition **generalizes the bank/card references, API paths and error codes**. It documents the application's configuration screen, **not** the full 3-D Secure protocol or ACS transaction authentication flow.

## 1. Original scenario and preconditions

The source describes switching a card-related 3-D Secure email notification/confirmation service on and off, including setting or changing the email address.

Preconditions in the source: user authenticated in a banking mobile app, selected an eligible Visa card and opened **Card Settings**. Specific issuer functionality and card-scheme eligibility depend on a real issuing-bank contract.

## 2. UI state and initialization

The source reads a card-list interface and uses its \`emailEnabled\` flag to display toggle status. The original path \`GET /card/visa/list\` has been generalized here to a synthetic example.

| Input | Initial UI state | Behavior |
|---|---|---|
| \`emailEnabled = false\` | Toggle off | Offer activation flow |
| \`emailEnabled = true\` | Toggle on | Offer deactivation / change-email flow |
| Card data unavailable | Loading or error | Do not guess service state |
| Missing permissions / wrong card | Unavailable control | Explain why changes are not permitted |

Illustrative public API: \`GET /v1/cards/{cardId}/security-settings\`.

## 3. Activation sequence

1. Customer switches the toggle to on.
2. UI asks for an email address, validates format, and shows a masked email confirmation.
3. The source requires a **five-digit code sent by email** for the flow.
4. The customer enters the code; UI validates required input.
5. The backend verifies the code; on confirmed success the screen refreshes the enabled state.
6. If verification times out or fails, the UI shows a localised error and retains the previous confirmed state.

A real issuer must determine the allowed authenticator and scheme/regulatory policy. A five-digit email code is part of this **source example**, not a claim about current certified 3DS/SCA best practice.

## 4. Deactivation and change of email

The source includes toggling off and updating the configured email. Separate the actions to prevent incorrect confirmation of a change before the issuer backend accepts it.

| Action | Input | Authoritative result | UI outcome |
|---|---|---|---|
| Enable notifications | Address + valid code | Provider confirms enabled | Toggle on |
| Disable notifications | Authenticated action | Provider confirms disabled | Toggle off |
| Change email | New address + proof per contract | Provider confirms new address | Show masked new address |
| Unknown operation outcome | Request correlation | Query status | Preserve prior confirmed UI state |

## 5. Errors from the original example (anonymized codes)

| Source error meaning | User-facing message proposal |
|---|---|
| Email code delivery failed | “We could not send your code. Please try again.” |
| Verification code expired | “The code expired. Request a new one.” |
| Verification code incorrect | “The code is incorrect.” |
| Enable/disable failed | “Your settings could not be updated.” |
| Email change failed | “The email address could not be changed.” |

The source contains issuer-specific integer codes **16009–16013** and sample timestamps; these are deliberately **not reproduced as a public bank API contract**.

## 6. Sequence diagram

\`\`\`mermaid
sequenceDiagram
    actor Cardholder
    participant UI as Mobile Card Settings
    participant Backend as Issuer Backend
    participant Mail as Email Service
    Cardholder->>UI: Toggle security email setting
    UI->>Backend: Request verification for new email
    Backend->>Mail: Send code
    Mail-->>Cardholder: Verification code
    Cardholder->>UI: Enter code
    UI->>Backend: Confirm code / setting change
    alt Valid and accepted
       Backend-->>UI: Confirmed settings
       UI-->>Cardholder: Show updated toggle
    else Expired / invalid / unavailable
       Backend-->>UI: Validation or processing error
       UI-->>Cardholder: Localized error; prior state retained
    end
\`\`\`

**Related:** [Frontend SRS template](../templates/frontend-srs-template.md) and [Card Acquiring architecture](../payments/acquiring-processing.md).

**License:** [CC BY 4.0](../license.md). All identifiers are synthetic; this is not a bank production specification.
