---
title: FR/NFR Example — Support Operations Console
sidebar_position: 14
---

# Functional and Non-Functional Requirements — Support Desk

**Source:** `FT_NFT_EXAMPLE.docx`, Example 1, STORAGE v1.0.0 (2025). This public edition retains the original example's **A–E sections**, selected requirement IDs, numerical objectives and role definitions. Some explanatory review guidance is new and labelled accordingly.

## Business scenario

A company's ten-person support team handles customer-reported errors and product suggestions. The department asks for a filterable console and the ability to export feedback as **ODT** documents. This is an educational scenario, not an active support desk deployment.

## A. Specialist Console — Authentication and Roles

| ID | Source requirement |
|---|---|
| FR-SPC-AUTH-01 | Admin can provision a specialist via secured backoffice; optional bulk CSV import and role assignment |
| FR-SPC-AUTH-02 | Email/password with optional SSO (SAML/OIDC); alternative secure authentication for on-call workflows |
| FR-SPC-AUTH-03 | At minimum: Specialist, Senior/Reviewer and Admin RBAC roles |
| FR-SPC-AUTH-04 | Data access restricted by assignment; sensitive customer-field edits require elevated privilege |
| FR-SPC-AUTH-05 | Four-eyes approval for incidents marked “requires review” |
| FR-SPC-AUTH-06 | Idle session timeout, device session controls and login audit |
| NFR-SPC-AUTH-01 | Approved password hashing, token/session security, rate limits and authentication monitoring |

## B. Support Chat — Operations and UX

The source requires stored conversations, attachment upload with antivirus checks, inactivity-based close/reopen, FAQ chatbot with human escalation, post-chat 1–5 CSAT, multi-channel notifications and visitor/SSO entry paths.

| ID | Source non-functional example target |
|---|---|
| NFR-SUP-CAP-02 | ≥ 400 messages/hour, ≥ 150,000 messages/day |
| NFR-SUP-CAP-03 | Peak ×8 of hourly average: ≥ 3,200 messages/hour for ≥ 2 h |
| NFR-SUP-CAP-04 | ≥ 1,000 concurrent active chats; ≥ 200 RPS (burst ≥ 400); p95 delivery ≤ 250 ms |
| NFR-SUP-CAP-05 | p95 agent wait ≤ 60 seconds; offline email SLA ≤ 4 h |
| NFR-SUP-AVAIL-01 | 99.9% monthly chat availability |
| NFR-SUP-RET-01 | 12-month online retention and 24-month archive; deletion request window in example ≤ 30 days |
| NFR-SUP-FILE-01 | ≤ 25 MB per file; ≤ 100 MB per conversation |
| NFR-SUP-LOG-01 | Audit actions with masked personal data |

**Source-quality note:** The message volumes in the example are not naturally consistent as an average hourly/day calculation. Do not silently treat them as an internally validated capacity plan; resolve expected DAU, RPS and volume distribution first.

## C. Filter and Search Panel

| ID | Source requirement |
|---|---|
| FR-FLT-01 | Filters for status, priority, dates, assignee, tags, channel, customer, language, region, SLA and CSAT |
| FR-FLT-02 | Sorting by last activity, priority, SLA risk, CSAT |
| FR-FLT-03 | Configurable filter visibility and saved team presets |
| FR-FLT-04 | Controlled bulk actions on result rows |
| NFR-FLT-01 | Typical indexed-search p95 ≤ 300 ms, pagination/lazy loading |
| NFR-FLT-02 | Audit query parameters and duration with PII masking |

## D. Feedback Reports and ODT Export

| ID | Source requirement |
|---|---|
| FR-RPT-01 | Download feedback/incident data as **.odt**; PDF/CSV optional |
| FR-RPT-02 | Incident ID, timestamps, channel, category, priority, assignee, lifecycle, resolution, CSAT and attachments list |
| FR-RPT-03 | On-demand, daily, weekly or monthly reporting |
| FR-RPT-04 | Store reports in an immutable or controlled archive; optional distribution email |
| NFR-RPT-01 | Example p95 ≤ 5 seconds to generate 10k-row report |

## E. Shared Platform NFRs

The original describes **WCAG 2.2 AA**, HTTPS/TLS 1.2+, RBAC, core API availability of 99.9%/month, p95 common read targets around 200–300 ms, and high-capacity plans.

These are proposed requirement **targets from the source**, not security certifications, measured benchmarks or legal conclusions.

## Architecture review additions

- Identify authoritative access-control checks for search, export and document download.
- Separate report generation from UI request when data volumes exceed synchronous time limits.
- Encrypt stored exports, enforce expiry and audit access.
- Replace the sample's assumed SLAs with measured baselines and agreed acceptance plans.

**Related:** [SRS template](../templates/srs-template.md) · [Requirements classifications](../templates/requirements-types.md) · [CC BY 4.0](../license.md).
