---
title: PlantUML & Architecture Diagrams
sidebar_position: 5
---
# Editable architecture diagrams (PlantUML)

These are **synthetic and provider-neutral** diagrams, published as source text in GitHub. They are not copies of customer architecture diagrams.

## Download / reuse

- [HLD component diagram (PlantUML)](https://github.com/SergeiBudnik/architecture-analysis-hub/blob/main/diagrams/payment-reference-hld.puml)
- [End-to-end payment sequence (PlantUML)](https://github.com/SergeiBudnik/architecture-analysis-hub/blob/main/diagrams/payment-reference-sequence.puml)
- [Payment state lifecycle (PlantUML)](https://github.com/SergeiBudnik/architecture-analysis-hub/blob/main/diagrams/payment-reference-state.puml)

To edit, copy the plain-text `.puml` files and render them locally in a PlantUML-compatible editor. The conceptual [Mermaid sequence](end-to-end.md) and [Mermaid state model](state-machine.md) are rendered inline on the site.

## Diagram design review

- Label who owns each business state.
- Differentiate synchronous commands from asynchronous event delivery.
- Explain where the provider is authoritative and where the platform maintains local projections.
- Separate recovery from financial instruction replay.
- Avoid internal hostnames, production URLs, credentials and identifiable client-system labels.

**Source distinction:** The authored RoPay diagrams informed the choice of topics and domain boundaries, but these public diagrams use generalized components and do not assert any RoPay-specific implementation semantics.