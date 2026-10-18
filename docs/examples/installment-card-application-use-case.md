---
title: Use Case — Installment Card Application
sidebar_position: 17
---

# Use Case: Applying for an Installment Card

**Source:** `USE_CASE_EXAMPLE_2.docx`, authored STORAGE documentation (v1.0.0, September 2025). The original contains a **61-step banking application process** covering digital origination, customer/lead data, compliance checks, scoring and a branch-assisted alternative. The public version consolidates steps by business phase. **No private bank, core-system, endpoint, identity-document values or production reference numbers are reproduced.**

## 1. Goal, scope and actors

**Goal:** Allow an authenticated banking customer to apply for an installment card, choose credit terms and requested servicing branch, complete customer-data checks, and submit the application to credit-scoring/case management.

| Actor or system | Responsibility |
|---|---|
| Customer / online banking | Initiates, reviews terms, selects limit and branch, supplies required information |
| Application API / orchestration | Ensures eligibility and controls application state |
| CRM and customer master | Customer data, lead and application correlation |
| Identity/eligibility service | Document validity, residence, age and required customer attributes |
| Branch/case management | Assisted/offline application creation |
| Scoring workflow | Initiates underwriting/approval process; returns status |
| Card repayment service | Stores selected eligible repayment instruments |

The source references a specific low-code engine and card processor. The public architecture uses functional names only.

## 2. Digitally initiated application: original source phases

| Source step(s) | Business flow | Important decision |
|---|---|---|
| 1–5 | Find recent or active application | Source checks prior activity over a **30-day window** |
| 6–7 | Show credit-card issuance terms and allowed limit | Customer selects limit, reads and accepts terms |
| 8–14 | Find and normalize customer profile, initialise application | Missing data can trigger alternate customer data lookup; store `NON_COMPLETE` |
| 15–23 | Select branch and check address, residency, age and mandatory fields | Mismatch may require supplying current address |
| 24–34 | Create/update CRM lead and register customer in master system | Prevent duplicate cases; preserve lead reference |
| 35–40 | Add work and repayment-card information | Apply eligibility rules to selected cards |
| 41–45 | Initiate credit scoring/case processing | On successful request move to `PENDING`; failure handled separately |

**Status names `NON_COMPLETE` and `PENDING` are preserved from the source** and are shown here as example workflow states, not a standardized card-network state machine.

## 3. Assisted/branch application: original steps 46–61

The original contains a second journey where a bank employee searches or creates customer data, checks CRM leads, fills credit/security/additional information, and creates a new lead through the case-management process.

| Phase | Agent action |
|---|---|
| Customer search | Identify customer type and search using required verified data |
| Customer creation | Only when existing records are not found; avoid duplicate identities |
| Lead search | Reuse eligible existing context or start new application |
| Credit information | Enter offer and risk-relevant data |
| Security/additional data | Complete required fields under approved process |
| Lead creation | Submit the new case and record reference |

## 4. Exceptions to model explicitly

- Customer has an active/recent incompatible application.
- Customer fails age, residency, region or document-validity rules.
- Identity data or CRM record missing or inconsistent.
- A lead/case already exists, or concurrent submissions race.
- Eligible repayment cards are unavailable.
- Scoring fails, times out or returns an unknown result.
- Customer stops during the process; unfinished draft needs an expiry rule.

**Design review additions:** Authenticated caller context, GDPR/data minimisation, application idempotency, asynchronous scoring recovery and immutable decision audit should be addressed in any new bank implementation. These details are review guidance, not confirmed controls from the original use case.

## 5. Editable architecture diagram

[Download generic installment-card application sequence (PlantUML)](https://github.com/SergeiBudnik/architecture-analysis-hub/blob/main/diagrams/storage-installment-application-sequence.puml).

This source is a business/technical use case, **not a credit eligibility recommendation or actual underwriting policy**. For implemented systems, follow applicable consumer credit laws, KYC procedures and internal approvals.

**License:** [CC BY 4.0](../license.md) for this new sanitized public edition.
