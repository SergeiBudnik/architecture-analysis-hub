---
title: Release Notes
sidebar_position: 6
---

# Release Notes

## 2026-10-18 — Stage 5: source coverage and API design expansion

- Expanded the previously short `API_PARAMETERIZATION.docx` adaptation into **all ten source problem categories**, with explicit source alternatives, pros/cons, API validation checklist and newly authored OpenAPI 3.1 reference example.
- Added source-structured [Versioning Policy](library-versioning.md) and [How to Use](library-how-to-use.md).
- Added an independently rewritten [BPMN FAQ](architecture/bpmn-practical-faq.md); the original Visual Paradigm material is **not republished or covered by CC BY**.
- Updated the 44-source inventory to distinguish complete concept coverage from public reproductions.

## 2026-10-18 — Release D linked and downloadable

- Added a source-based download index for extended SRS, Database Design FAQ, complete Food Delivery FR/NFR and both additional sequences.
- Added five editable Word-compatible RTF public editions and two PlantUML sources.
- Published the ten-column User Stories template in **both native editable XLSX and CSV**. The original sample's full acceptance criteria are preserved in the public workbook.
- Refreshed source inventory and diagrams catalogue, distinguishing original source facts from independent additions.

## 2026-10-18 — STORAGE batch D: SRS, database, FR/NFR, sequences and spreadsheet

- Added [Extended Full-Stack SRS](templates/full-stack-srs-outline.md) based on SRS Template 1, plus editable RTF.
- Added complete [Food Delivery FR/NFR (Example 2)](examples/food-delivery-functional-nonfunctional.md), retaining original requirement groups and sample targets.
- Added generalized [Apple Pay Provisioning](examples/apple-pay-provisioning-sequence.md) and [Kafka Fraud + Signing](examples/antifraud-kafka-signing-sequence.md) sequences, with editable PlantUML files.
- Added [Database Design FAQ](architecture/database-design-faq.md) as independently authored explanatory material; vendor-authored source marketing copy was not relicensed.
- Added [User Stories Excel-compatible CSV](templates/user-story-excel-download.md), adapted from the original ten-column spreadsheet. Styled native XLSX is published alongside the CSV.
- Added five Word-compatible RTF guides for reuse.

## 2026-10-18 — STORAGE banking examples, batch C

- Published anonymized [Installment Card Application Use Case](examples/installment-card-application-use-case.md) from the original multi-step banking process, with source-step mapping and new PlantUML sequence.
- Published anonymized [Card Blocking Backend SRS](examples/card-block-backend-srs.md), preserving the original two client-contract generations, block reason handling and confirmation semantics.
- Omitted all bank-specific endpoint/processor dictionaries, private business identifiers and sensitive sample data.

## 2026-10-18 — STORAGE examples released in two batches

- [Batch A](examples/source-examples-downloads.md): Six source-grounded educational case studies (two SRS, 3DS frontend, SMS use case, report sequence, employee bulk-update API), all with native editable DOCX versions.
- Published two editable PlantUML sequence diagrams for SMS registration and long-running report generation.
- [Batch B](examples/source-examples-downloads.md): Three additional source-grounded Markdown examples covering food delivery user stories, support console FR/NFR and product-catalogue business requirements.
- Updated the template catalogue and download index. Original private source DOCX files were not bulk uploaded; extra guidance is explicitly distinguished from original example content.

## 2026-10-17 — Editable source-derived architecture library

- Published expanded, editable DOCX and Word-compatible RTF HLD documents adapted from `HIGH _LEVEL_ARCITECTURE_EXAMPLE_1.docx` and `HIGH _LEVEL_ARCITECTURE_EXAMPLE_2.docx`, preserving the original architecture document structure, component tables and numbered integration groups.
- Released Draw.io public editions with **4 pages** for request management and **3 pages** for service booking, based on the original architectural themes and HLD tables.
- Recreated two Visio BPMN examples as editable Draw.io processes (bank statement, card authorization/cancellation/clearing).
- Released a simplified, editable food-delivery BPMN 2.0 model derived from the source process.
- Added one [source-based editable download index](editable-source-diagrams.md) with clear provenance, anonymization and CC BY 4.0 terms.
- New public editions are **not binary-identical to old private source files**, and do not contain confidential customer details.

## 2026-10-17 — Three more sanitized examples from STORAGE

- Added [Service Booking HLD](examples/service-booking-hld.md), adapted from the second HLD example with internal component identifiers removed.
- Added [Food Ordering Database Design](examples/restaurant-database-design.md), adapting the source's seven core entities and explicitly removing unsafe payment-card storage fields.
- Added [Email Notification MQ Listener](examples/email-notification-consumer.md), with an anonymized integration, bounded retry and DLQ discussion.
- Added three matching editable PlantUML diagrams.
- Updated the source-library publication inventory. Original DOCX, XLSX, BPMN, Visio and draw.io files remain under review.

## 2026-10-17 — CC BY 4.0 public content license

- Published [License & Attribution](license.md) and a scoped repository [CC BY 4.0 license notice](https://github.com/SergeiBudnik/architecture-analysis-hub/blob/main/LICENSE.md).
- Licensed the released author-owned educational content, new RTF downloads and original reference diagrams with attribution and change-notice requirements.
- Kept the unreviewed original STORAGE archive and third-party/client-owned material outside the license and outside the repository.

## 2026-10-17 — Reusable resources and site navigation

- Published eight sanitized, editable **Word-compatible RTF templates** for requirements, HLD, API, backend/frontend, database and event-driven integration.
- Added a dedicated [Downloads page](downloads.md), author page and feedback guidelines.
- Added topic/title-based resource search and improved top navigation.
- Published a [Diagram Gallery](diagram-gallery.md) with four simplified SVG architecture flows linked to editable PlantUML sources.
- Enabled Mermaid diagram rendering in Docusaurus for explanatory sequence/state figures.
- Retained the original authored source archive privately rather than uploading unreviewed binary files.

## 2026-10-17 — Event-driven payments and Kafka recovery

- Published [Event-Driven Payment Processing](payments/event-driven-processing.md), covering Kafka topology, topic keys, outbox/inbox, merchant notifications and processor recovery.
- Added [Kafka Offset Recovery Worked Example](payments/kafka-offset-recovery.md) with partition 7 / offset 184, DB commit versus offset commit and consumer rebalances.
- Added [Event Contracts & SQL](payments/event-driven-contracts.md), [ADRs and fault-injection tests](payments/event-driven-design-decisions.md).
- Added four editable PlantUML files for HLD, outbox/inbox, offset crash recovery and DLQ/manual re-drive.
- Reference models and synthetic records are educational; no scheme-specific or client-secret information is included.

## 2026-10-17 — Card financial lifecycle reference

- Published [Clearing, Settlement & Reconciliation](payments/clearing-settlement-reconciliation.md): roles, lifecycle and operational/financial boundaries.
- Added a [worked example](payments/reconciliation-worked-example.md): capture GBP 100, illustrative merchant net GBP 97.80 and a GBP 0.50 payout mismatch.
- Added [architecture decision records](payments/clearing-design-decisions.md), control tables, batch/row idempotency and verification tests.
- Added four editable PlantUML diagrams: financial HLD, lifecycle milestones, presentment/settlement sequence, reconciliation-break sequence.
- All identities and data are fictitious and independent of any customer/scheme specifications.

## 2026-10-17 — Payment architecture and diagrams

- Published provider-neutral end-to-end payment-processing architecture and sequence.
- Added intent state machine, idempotency guidance, timeout/retry and recovery patterns.
- Added three editable PlantUML source diagrams (HLD, payment sequence and payment state).
- Expanded architecture resources with API design patterns and an HLD deliverable checklist.
- Reference examples are synthetic; no real bank/customer system diagrams or production credentials are included.

## 2026-10-17 — Practical worked examples

- Added a fictional online travel booking BRD adapted from the authored BRD example.
- Added an employee XLSX export API specification and explanatory sequence diagram.
- Added a travel-plan hotel-removal backend specification and sequence diagram.
- Linked the worked examples from the public Template Catalogue.
- These examples are illustrative learning resources, **not deployed customer projects**.

## 2026-10-17 — Initial preview

- Established the open documentation portal structure.
- Added introductory guides for requirements, architecture and engineering specifications.
- Added a public catalogue showing which original templates remain under review.

Original source documents have not yet been publicly released. Future releases will document concrete changes, examples and independently verified feedback.
