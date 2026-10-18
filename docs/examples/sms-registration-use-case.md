---
title: Use Case Example — SMS Registration
sidebar_position: 10
---

# Use Case: User Registration by Phone and SMS Code

**Source:** STORAGE `USE_CASE_EXAMPLE_1.docx` (v1.0.0, September 2025). The main and alternative paths below retain the source's intent; IDs, rate limiting and recovery clarifications are new editorial additions.

| Field | Description |
|---|---|
| Use case ID | UC-REG-001 (public edition) |
| Goal | Register and authenticate a new mobile user |
| Primary actor | Mobile app user |
| Supporting actor | SMS delivery service |
| Preconditions | App open; user has a phone number that can receive SMS |
| Success postcondition | Exactly one new account exists; user is authenticated |
| Alternative | Existing account follows login path |

## 1. Main flow

| Step | User | System |
|---|---|---|
| 1 | Opens app and chooses Register | Displays phone entry |
| 2 | Enters phone number | Validates format |
| 3 | Requests confirmation | Calls SMS provider for one-time code |
| 4 | Receives a 4–6 digit code | Displays code-entry screen |
| 5 | Enters code | Verifies value and expiration |
| 6 | — | On successful verification, creates account and starts session |
| 7 | — | Navigates to home screen; optional profile details later |

## 2. Extensions (source scenario)

| Branch | Trigger | Result |
|---|---|---|
| 2a | Number format invalid | Explain error; request correction |
| 3a | SMS provider delivery failed | Show retry option |
| 4a | User did not receive code | Resend and return to confirmation |
| 5a | Code invalid | Allow correction |
| 5b | Too many failed attempts | Temporarily block verification |
| 6a | Account already exists | Offer login rather than duplicate registration |

The source uses a **three-attempt** example for temporary blocking; this is an illustrative parameter, not a recommended universal rate limit.

## 3. Editable PlantUML sequence

[Download SMS registration sequence (.puml)](https://github.com/SergeiBudnik/architecture-analysis-hub/blob/main/diagrams/storage-sms-registration.puml).

## 4. Design review additions (not literal source)

- Define expiry and resend throttling according to abuse risk.
- Store only hashed/derived tokens, not plaintext SMS codes in logs.
- Create user transactionally with a unique normalized phone identifier.
- Prevent simultaneous successful verification creating two accounts.
- Do not disclose account existence when threat model requires anti-enumeration measures.

**Template:** [Blank Use Case](../templates/use-case-template.md). **Licence:** [CC BY 4.0](../license.md).
