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

## Event-driven Kafka and payment integration

- [Kafka and payments HLD](https://github.com/SergeiBudnik/architecture-analysis-hub/blob/main/diagrams/event-driven-payment-hld.puml)
- [Transactional outbox and inbox sequence](https://github.com/SergeiBudnik/architecture-analysis-hub/blob/main/diagrams/event-driven-outbox-inbox-sequence.puml)
- [Consumer offset crash recovery](https://github.com/SergeiBudnik/architecture-analysis-hub/blob/main/diagrams/event-driven-offset-recovery-sequence.puml)
- [Retries, DLQ and operator-governed redrive](https://github.com/SergeiBudnik/architecture-analysis-hub/blob/main/diagrams/event-driven-dlq-recovery-sequence.puml)

See the [detailed architecture case study](event-driven-processing.md) and [worked offset example](kafka-offset-recovery.md).

## More source-based sequence examples

- [Wallet card provisioning — issuer-assisted, generalized](https://github.com/SergeiBudnik/architecture-analysis-hub/blob/main/diagrams/storage-wallet-card-provisioning.puml)
- [Kafka antifraud + signature service](https://github.com/SergeiBudnik/architecture-analysis-hub/blob/main/diagrams/storage-kafka-antifraud-signing.puml)

Both are explicitly educational adaptations, not real customer or certified provider contract sequences.

## Diagram design review

- Label who owns each business state.
- Differentiate synchronous commands from asynchronous event delivery.
- Explain where the provider is authoritative and where the platform maintains local projections.
- Separate recovery from financial instruction replay.
- Avoid internal hostnames, production URLs, credentials and identifiable client-system labels.

**Source distinction:** The authored RoPay diagrams informed the choice of topics and domain boundaries, but these public diagrams use generalized components and do not assert any RoPay-specific implementation semantics.