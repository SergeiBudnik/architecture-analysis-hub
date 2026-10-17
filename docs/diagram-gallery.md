---
title: Architecture Diagram Gallery
sidebar_position: 5
---

# Architecture Diagram Gallery

Four visual summaries are provided below. These compact diagrams are for **orientation**, not literal rendered copies of the comprehensive PlantUML source. Every architecture example is fictional and provider-neutral.

## A2A / QR / Deep Link

<img src="/architecture-analysis-hub/img/a2a-overview.svg" alt="A2A QR and deep link orchestration" />

[Full case study](payments/a2a-qr-deeplink.md) · [Editable PlantUML HLD](https://github.com/SergeiBudnik/architecture-analysis-hub/blob/main/diagrams/a2a-qr-deeplink-hld.puml)

## Card Acquiring & Processing

<img src="/architecture-analysis-hub/img/acquiring-overview.svg" alt="Card acquiring network authorization participants" />

[Full case study](payments/acquiring-processing.md) · [Editable authorization sequence](https://github.com/SergeiBudnik/architecture-analysis-hub/blob/main/diagrams/acquiring-authorization-sequence.puml)

## Clearing, Settlement & Merchant Funding

<img src="/architecture-analysis-hub/img/clearing-overview.svg" alt="Payment clearing settlement and merchant funding" />

[Financial lifecycle case study](payments/clearing-settlement-reconciliation.md) · [Worked reconciliation example](payments/reconciliation-worked-example.md) · [Editable HLD](https://github.com/SergeiBudnik/architecture-analysis-hub/blob/main/diagrams/clearing-settlement-hld.puml)

## Kafka and Event-Driven Payment Processing

<img src="/architecture-analysis-hub/img/kafka-overview.svg" alt="Kafka outbox relay topics inbox and notification" />

[Kafka architecture](payments/event-driven-processing.md) · [Offset recovery walkthrough](payments/kafka-offset-recovery.md) · [Editable event-driven HLD](https://github.com/SergeiBudnik/architecture-analysis-hub/blob/main/diagrams/event-driven-payment-hld.puml)

## Editing PlantUML sources

The `.puml` links lead to editable plain-text diagrams. Open them in a PlantUML-compatible editor, adjust system boundaries and message flows, then render them. The simplified SVG overviews on this page are separate illustrations.

Always check the accompanying component tables, error paths and provider-specific constraints before applying any architecture to a real system.
