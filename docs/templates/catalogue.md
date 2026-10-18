---
title: Template Catalogue
sidebar_position: 5
---

# Template Catalogue & Practical Guides

**Want an editable Word-compatible file?** Start with [eight downloadable RTF templates](../downloads.md). These open in Word or LibreOffice and can be saved as DOCX.

These are **public, editable Markdown templates and guides**, adapted from Sergei Budnik's authored STORAGE library (2025). Click a title to open it; use **Edit this page** only if available, or copy the template text into your own document.

## Requirements & Analysis

| Resource | Format |
|---|---|
| [Business Requirements Document (BRD)](brd-template.md) | Template |
| [Software Requirements Specification (SRS)](srs-template.md) | Template |
| [Extended Full-Stack SRS Template 1](full-stack-srs-outline.md) | Adapted comprehensive SRS guide + editable RTF |
| [User Stories spreadsheet (Excel-compatible CSV)](user-story-excel-download.md) | Downloadable spreadsheet |
| [Business vs Functional vs Non-Functional Requirements](requirements-types.md) | Guide |
| [Use Case](use-case-template.md) | Template |
| [User Story & Acceptance Criteria](user-story-template.md) | Template |

## Additional editable architecture sources

[Download HLD public editions, Draw.io architecture diagrams, Visio-based process conversions and BPMN 2.0](../editable-source-diagrams.md).

## Architecture & Data

| Resource | Format |
|---|---|
| [High-Level Architecture (HLA)](high-level-architecture-guide.md) | Guide & template |
| [Database Design](database-design-template.md) | Template |
| [Sequence Diagram](sequence-diagram-guide.md) | Guide & diagram example |

## Engineering & Integration

| Resource | Format |
|---|---|
| [Backend Service Specification](backend-srs-template.md) | Template |
| [Frontend Screen Specification](frontend-srs-template.md) | Template |
| [Message Broker Listener Specification](message-broker-spec-template.md) | Template |
| [Integration Specification](integration-specification.md) | Checklist & template |

## Publication status

**12 public materials** are available in web-readable form. Original Word, Excel, BPMN, draw.io and Visio downloads remain under individual review; they are **not yet published**. Selected worked examples are available below.

Markdown sources and new RTF templates can be downloaded via the linked repository. The full, original source archive is not published. Public release does not imply independent use or recognition by others.

## Architecture case studies

| Case | Resource |
|---|---|
| [A2A / QR / Deep Link](../payments/a2a-qr-deeplink.md) | HLD, API, decision log and PlantUML sequences |
| [Card Acquiring & Processing](../payments/acquiring-processing.md) | HLD, ISO 8583 overview, authorization and reversal |
| [Clearing, Settlement & Reconciliation](../payments/clearing-settlement-reconciliation.md) | Financial lifecycle, reconciliation example and four PlantUML diagrams |
| [Event-Driven Payment Processing](../payments/event-driven-processing.md) | Kafka, transactional outbox/inbox, offsets, retry/DLQ and four PlantUML diagrams |

## Extended source-derived learning materials

- [Full-Stack SRS Template 1](full-stack-srs-outline.md) — BA, frontend, backend, API and DB design in one dossier.
- [Database Design FAQ](../architecture/database-design-faq.md) — independent technical guidance based on the original topic list, without third-party promotional prose.
- [Full Food Delivery FR/NFR](../examples/food-delivery-functional-nonfunctional.md) — complete second requirements example.
- [User Stories editable spreadsheet (CSV)](user-story-excel-download.md) — follows the ten source columns and sample catalog-sorting story.
- [Apple Pay card provisioning](../examples/apple-pay-provisioning-sequence.md) and [Kafka antifraud + signing](../examples/antifraud-kafka-signing-sequence.md) — additional original-source sequence exercises.

## Worked examples

**New:** [Download source-based examples as DOCX](../examples/source-examples-downloads.md). The six new Word documents cover SRS, frontend, API, use case and sequence scenarios. Other adaptations are available as Markdown.

Six source-based educational examples are now public. Their original Word files have **not** been uploaded; links below lead to carefully adapted web editions.

| Example | Source artifact |
|---|---|
| [Travel Booking Platform — filled BRD](../examples/travel-platform-brd.md) | `BRD_EXAMPLE.docx` |
| [Employee XLSX Export — API specification and sequence](../examples/employee-export-api.md) | `API_EXAMPLE.docx` |
| [Travel Plan — hotel removal backend flow](../examples/travel-plan-delete-backend.md) | `BACK_SRS_EXAMPLE_1.docx` |
| [Travel Booking Platform — detailed SRS](../examples/travel-platform-srs.md) | `SRS_EXAMPLE_2.docx` (public DOCX) |
| [Food Delivery Platform — detailed SRS](../examples/food-delivery-srs.md) | `SRS_EXAMPLE_1.docx` (public DOCX) |
| [3-D Secure Email Settings — Frontend SRS](../examples/3ds-settings-frontend.md) | `FRONT_SRS_EXAMPLE.docx` (public DOCX) |
| [SMS Registration — Use Case](../examples/sms-registration-use-case.md) | `USE_CASE_EXAMPLE_1.docx` (public DOCX) |
| [Asynchronous Report — Sequence](../examples/async-accounting-report-sequence.md) | `SEQUENCE_EXAMPLES.docx` (Example 1; public DOCX) |
| [Employee Bulk Update — API](../examples/employee-bulk-update-api.md) | `API_EXAMPLE.docx` (second operation; public DOCX) |
| [Full Food Delivery FR/NFR — Example 2](../examples/food-delivery-functional-nonfunctional.md) | `FT_NFT_EXAMPLE.docx` (second example) |
| [Apple Pay Card Provisioning — Sequence](../examples/apple-pay-provisioning-sequence.md) | `SEQUENCE_EXAMPLES.docx` (Example 2) |
| [Kafka Antifraud & Signing — Sequence](../examples/antifraud-kafka-signing-sequence.md) | `SEQUENCE_EXAMPLES.docx` (Example 3) |
| [Food Delivery — User Stories](../examples/user-story-examples.md) | `USER_STORY_EXAMPLE.docx` |
| [Support Console — Functional / Non-functional](../examples/support-console-fr-nfr.md) | `FT_NFT_EXAMPLE.docx` (Example 1) |
| [Product Catalogue — Business Requirements](../examples/product-catalog-business-requirements.md) | `BR_EXAMPLE.docx` |
| [Installment Card Application — Use Case](../examples/installment-card-application-use-case.md) | `USE_CASE_EXAMPLE_2.docx` (anonymized) |
| [Card Blocking — Backend SRS](../examples/card-block-backend-srs.md) | `BACK_SRS_EXAMPLE_2.docx` (anonymized) |
| [Service Booking Platform — HLD and component model](../examples/service-booking-hld.md) | `HIGH _LEVEL_ARCITECTURE_EXAMPLE_2.docx` (anonymized) |
| [Food Ordering — database model and ERD](../examples/restaurant-database-design.md) | `DATABASE_DESIGN_EXAMPLE.docx` (security-corrected) |
| [Email Notification — MQ listener and retry/DLQ](../examples/email-notification-consumer.md) | `MQ_SRS_EXAMPLE.docx` (anonymized) |

**Reuse:** Public, author-owned educational adaptations and downloads are available under [CC BY 4.0](../license.md). The original STORAGE archive is not included.

The examples are educational and should not be presented as delivered client systems. Their source material was authored by Sergei Budnik; additional explanatory diagrams and checks are labelled as adaptations.
