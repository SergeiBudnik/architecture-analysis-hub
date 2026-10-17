---
title: Architecture Deliverables & Review Checklist
sidebar_position: 3
---
# Architecture deliverables: HLD, integrations and detailed specifications

**Source basis:** the author's `HLA_FAQ.docx`, `HIGH _LEVEL_ARCITECTURE_EXAMPLE_1.docx`, and `HIGH _LEVEL_ARCITECTURE_EXAMPLE_2.docx`. These documents organize architecture around use cases, context, components, containers, component descriptions, integration scenarios, and external/internal interactions.

## Recommended HLD package

| Artifact | Purpose |
|---|---|
| Business context / use cases | Explain what the solution enables |
| Context diagram | Show external actors, systems and trust boundaries |
| Container / component diagram | Separate deployable units and main responsibilities |
| Component description | State ownership, APIs, persistence and scaling assumptions |
| Integration scenario | Show cross-system message and data flow |
| Sequence diagram | Explain temporal ordering, callbacks and exceptions |
| NFR and trade-off register | Record resilience, latency, security and risks |
| Architecture decision record | Preserve alternatives and decision rationale |

## HLD worksheet

### 1. Context

**Business objective:** [Target outcome]  
**Stakeholders:** [Owners, delivery teams, operational teams]  
**System scope:** [In scope / out of scope]

### 2. Components

| ID | Component | Ownership | Inbound interface | Outbound dependency | Data owned |
|---|---|---|---|---|---|
| C-01 | [Name] | [Team] | [API/event] | [System] | [Entity] |

### 3. Integration interaction

| Step | Source | Destination | Request or event | Sync / async | Failure path |
|---|---|---|---|---|---|
| 1 | [A] | [B] | [Operation] | [Type] | [Expected behavior] |

### 4. Quality attributes

- **Availability:** [SLO and dependency assumptions]
- **Latency:** [p95/p99 target per critical flow]
- **Security:** [AuthN/AuthZ, secrets, encryption and audit]
- **Reliability:** [Retry, dedupe, reconciliation]
- **Observability:** [Metrics, traces and correlation IDs]
- **Operability:** [Backfill, replay and incident response]

### 5. Review questions

- Are boundaries and system responsibilities consistent with the use cases?
- Do the diagrams distinguish online requests from asynchronous follow-ups?
- Does each component have an accountable team or service owner?
- Are state owners, data owners and the source of truth explicit?
- Is the architecture testable for failure, partial success and recovery?

See also [Payment Architecture Reference](../payments/overview.md) and [editable PlantUML diagrams](../payments/diagrams.md).