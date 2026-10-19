---
title: Editable HLD, BPMN & Diagram Sources
sidebar_position: 8
---

# Download Editable Architecture and BPMN Sources

These are **new public, anonymized editions** of the author's STORAGE examples. Download them for free, open in the corresponding editor and modify for your own requirements. They are released as original author-owned educational adaptations under [CC BY 4.0](license.md).

**Publication distinction:** The HLDs retain the documented component responsibilities and the original categories of external/internal integrations. Internal naming, infrastructure details and proprietary-looking identifiers have been generalized. The Draw.io, BPMN and RTF files below are **not identical binary copies** of the private source archive.

## High-Level Architecture examples

| Source document in STORAGE | Public editable document | Editable diagram |
|---|---|---|
| `HIGH _LEVEL_ARCITECTURE_EXAMPLE_1.docx` — request-management platform | [Download HLD (DOCX)](https://sergeibudnik.github.io/architecture-analysis-hub/editable/HLD_Request_Management_Public.docx) · [RTF](https://sergeibudnik.github.io/architecture-analysis-hub/editable/HLD_Request_Management_Public.docx) | [Download 4-page Draw.io](https://github.com/SergeiBudnik/architecture-analysis-hub/raw/refs/heads/main/static/editable/requests-architecture.drawio) |
| `HIGH _LEVEL_ARCITECTURE_EXAMPLE_2.docx` — service booking / onboarding | [Download HLD (DOCX)](https://sergeibudnik.github.io/architecture-analysis-hub/editable/HLD_Service_Booking_Public.docx) · [RTF](https://sergeibudnik.github.io/architecture-analysis-hub/editable/HLD_Service_Booking_Public.docx) | [Download 3-page Draw.io](https://github.com/SergeiBudnik/architecture-analysis-hub/raw/refs/heads/main/static/editable/onboarding-architecture.drawio) |

The **DOCX documents are native editable Word files**; RTF is offered as an alternative. Both public editions include context, role/use-case responsibilities, component catalogues, source-style numbered external and internal flow tables, technology stack and architecture review questions. They preserve the key source organization, but omit the proprietary-looking service identifiers and embedded original images. The diagrams are editable in diagrams.net.

## BPMN and process diagrams

| STORAGE origin | Public editable edition | Description |
|---|---|---|
| `BPMN_EXAMPLE_1.vsdx` | [Download account-statement process (.drawio)](https://github.com/SergeiBudnik/architecture-analysis-hub/raw/refs/heads/main/static/editable/bank-statement-process.drawio) | Account statement via banking channel, core banking and card processing |
| `BPMN_EXAMPLE_2.vsdx` | [Download card-payment process (.drawio)](https://github.com/SergeiBudnik/architecture-analysis-hub/raw/refs/heads/main/static/editable/card-authorization-process.drawio) | Card authorization, cancellation/reversal, presentment and clearing |
| `BPMN_EXAMPLE_3.bpmn` | [Download food-delivery BPMN 2.0 (.bpmn)](https://github.com/SergeiBudnik/architecture-analysis-hub/raw/refs/heads/main/static/editable/food-delivery-process.bpmn) | Card/cash decision, order preparation, courier assignment, delivery and complaint handling |

The Visio examples have been **converted into newly drawn editable diagrams**, rather than retaining Visio page geometry. The food-delivery BPMN is a sanitized simplified recreation and should be validated for syntax and visual flow in your target BPMN editor before implementation.

## Why these editions are safer for publication

- Removed old subscriber-only notices from the new public editions.
- Replaced source-specific service/system names with generic component responsibilities.
- Excluded internal URLs, identifiers, credentials and production network configuration.
- Kept the meaningful participants, process stages, architecture layers and integration decisions.
- Marked design recommendations separately from claims supported by the original examples.

## How to use

1. Click the download link (or open it in GitHub and use the **Download raw file** button).
2. Open `.drawio` with [diagrams.net](https://app.diagrams.net/), `.bpmn` with a BPMN 2.0 editor such as Camunda Modeler, and `.rtf` with Microsoft Word.
3. Replace illustrative architecture with your actual requirements and verify the target bank/process contract.
4. When sharing or adapting the released material, credit Sergei Budnik and link to [CC BY 4.0](license.md).

The remaining source documents are covered in the [Source Publication Roadmap](source-publication-roadmap.md). Publishing documents alone is not proof of independent adoption or recognition.
