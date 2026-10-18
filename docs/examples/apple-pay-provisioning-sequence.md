---
title: Sequence — Apple Pay Card Provisioning
sidebar_position: 20
---

# Apple Pay Provisioning: Tokenization and Issuer Verification

**STORAGE source:** `SEQUENCE_EXAMPLES.docx`, Example #2, titled **Apple Pay Tokenization (Visa) — Wallet-Initiated (Issuer-Assisted)**. The original diagram has 24 numbered interactions among cardholder, Wallet/PassKit, provisioning APIs, Visa Token Service, issuer tokenization service and secure device storage.

This publication is a **generalized learning model**, **not a verified or certified Apple/Visa API contract**. The source includes provider-internal messages and cryptographic/key-material descriptions. The public diagram removes those implementation-specific payloads rather than asserting that they are publicly available APIs.

## Source participants and responsibilities

| Source actor | Public logical role |
|---|---|
| Cardholder | Requests to add an existing card to a device |
| Apple Wallet / PassKit | Customer-facing card provisioning UI |
| Apple provisioning services | Manages platform-side provisioning session |
| Network tokenization service (VTS in source) | Processes token request and token lifecycle |
| Issuer token service | Makes eligibility/risk and step-up decisions |
| Device secure storage | Holds authorized device payment credential |

## Lifecycle preserved from the source

1. **Enrollment start:** cardholder selects Add Card; device capabilities and session context are checked.
2. **Card submission:** Wallet sends protected provisioning information to relevant platform/network services.
3. **Issuer decision:** issuer checks eligibility/risk and determines whether additional verification is required.
4. **Step-up path:** SMS/call/email one-time code or redirect to issuer banking application, subject to supported methods.
5. **No-step-up path:** issuer/network confirm eligibility according to applicable risk decisions.
6. **Provisioning:** tokenization platform and Wallet complete secure credential activation.
7. **Completion:** user sees that the card has been added; provisioning status is synchronized.

The original depicts tokenized PAN and wrapped key material. Their exact contract is **outside this public reference**. Do not treat either as plaintext business data that integrators should store.

## Architecture review and recovery

| Risk | Design review consideration |
|---|---|
| Wallet UI reports success but token activation unfinished | Query authoritative token status rather than assuming active |
| OTP challenge expired or failed | Rate limit and use issuer-approved retry/step-up procedures |
| Token created but provisioning callback lost | Correlate stable token/session reference; reconcile |
| Device changed or removed | Token lifecycle suspension/deletion policies |
| Duplicate provisioning attempts | Provider-controlled enrollment correlation and dedupe |

These are **new review questions**, not claims of actual Visa/Apple backend behavior.

## Editable sequence

[Download generic Apple Pay provisioning sequence (.puml)](https://github.com/SergeiBudnik/architecture-analysis-hub/blob/main/diagrams/storage-wallet-card-provisioning.puml).

**Source limitation:** The actual issuer provisioning interfaces, message contracts and scheme requirements must be sourced from approved provider documentation. [CC BY 4.0 for this public adaptation](../license.md).
