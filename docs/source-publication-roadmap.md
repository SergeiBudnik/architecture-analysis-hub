---
title: Source Library Publication Roadmap
sidebar_position: 7
---

# Source Library Review: STORAGE Archive

**Author:** Sergei Budnik · **Audit started:** 17 October 2026.

The author's original STORAGE archive includes **44 files**, but the full archive is not publicly distributed. The public library contains newly formatted educational documentation, sanitized case-study adaptations and editable examples released separately under [CC BY 4.0](license.md).

## Newly available expanded editable public editions

Two original HLD examples now have **expanded, anonymized DOCX and RTF documents** preserving component catalogues and numbered external/internal interactions, with newly prepared Draw.io source diagrams. The two original Visio BPMN examples have **editable Draw.io reconstructions**; the food-delivery BPMN has a separate simplified public BPMN 2.0 edition. See [Editable Source Downloads](editable-source-diagrams.md).

These are edited public versions, not identical copies of source DOCX/VSDX/DRAWIO binaries. They do not imply that all original embedded images, document comments and precise original graph geometry are releasable. The original 44 files remain in private review and are not bulk uploaded.

## New releases: SRS, Use Case, Sequence, API and requirements

**Release A:** [Six detailed public Word (DOCX) examples](examples/source-examples-downloads.md) for food/travel SRS, 3-D Secure frontend configuration, SMS registration, report sequence and employee bulk update, plus two original educational editable PlantUML sequences. **Release B:** public Markdown editions of user stories, a support console FR/NFR exercise and three sets of business requirement examples.

All new versions are sanitized adaptations; the original 2025 binaries and unreviewed embedded assets remain private.

**Release C:** Two further sanitized banking process examples: the 61-step installment card application use case grouped by stages, and card blocking with legacy/new client flow. Editable neutral PlantUML sequences have been released; bank-specific original Word binaries are not public.

For the complete source-by-source matrix, see the [44-file Publication Inventory](source-inventory.md).

## Source inventory

| Original format | Number of files | Status |
|---|---:|---|
| Word .docx | 37 | Individual review in progress |
| Draw.io .drawio | 2 | Diagram content/metadata review required |
| Visio .vsdx | 2 | Diagram content/metadata review required |
| Excel .xlsx | 1 | Content, formulas and metadata review required |
| BPMN .bpmn | 1 | Content and identifiers review required |
| Text .txt | 1 | Inventory only |
| **Total** | **44** | **No raw archive upload** |

The source archive contains **22 items whose filenames include EXAMPLE or EXAMPLES**. Some are teaching cases, some may overlap, and some can contain embedded technical diagrams or organization-specific identifiers. Not all are suitable for direct publication.

## Already published as source-based web adaptations

| Original source | Published adaptation | Original binary downloadable? |
|---|---|---|
| `BRD_EXAMPLE.docx` | [Travel Booking BRD](examples/travel-platform-brd.md) | No |
| `API_EXAMPLE.docx` | [Employee XLSX Export API](examples/employee-export-api.md) | No |
| `BACK_SRS_EXAMPLE_1.docx` | [Travel Plan Backend Specification](examples/travel-plan-delete-backend.md) | No |
| `HIGH _LEVEL_ARCITECTURE_EXAMPLE_2.docx` | [Service Booking HLD](examples/service-booking-hld.md) | No |
| `DATABASE_DESIGN_EXAMPLE.docx` | [Food Ordering Data Model](examples/restaurant-database-design.md) | No |
| `MQ_SRS_EXAMPLE.docx` | [Notification MQ Consumer](examples/email-notification-consumer.md) | No |

Additionally, [12 template/guide pages](templates/catalogue.md) and [eight editable RTF downloads](downloads.md) have been published as public materials.

## Why original files need review

- Many source documents contain an **older subscriber-use notice** reading `Personal use by subscriber; no redistribution`. The author can relicense works they own, but third-party rights and embedded materials must be checked separately.
- Some HLD and integration documents contain **specific internal service/component names**, deployment topology, identifiers and linked integrations.
- Some examples include **embedded images/diagrams** and may have Office author metadata or document comments.
- The original database sample includes fields for **card number and CVV**. The web edition explicitly removes that unsafe pattern instead of presenting it as a recommendation.
- Tutorial material and diagrams may refer to third-party resources or images that must not be automatically relicensed.

## Publication gate for each original file

1. **Rights:** Is the author entitled to publish the complete text, images and editable diagram objects under CC BY 4.0?
2. **Privacy:** Are client identifiers, contacts, credentials, bank/card information, internal URLs, ticket IDs, and hidden metadata removed?
3. **Architecture:** Does the document present safe, correct and clearly qualified guidance?
4. **Usability:** Are document styles, image visibility and downloadable editing supported?
5. **Traceability:** Is the public copy clearly labeled as an adapted version, with the source version and modification note?

Only after those checks should a **new, sanitized editable .docx/.xlsx/.drawio/.bpmn version** be published. Avoid uploading an archive of unreviewed originals.

## External impact

Publishing documents is not evidence that an external community has adopted them. Real usage, independently verifiable reviews, issue discussions and references must be established separately.

See [Contributions](contribute.md), [License](license.md) and [Release Notes](release-notes.md).
