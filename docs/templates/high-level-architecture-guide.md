---
title: High-Level Architecture (HLA) Guide
sidebar_position: 2
---

# High-Level Architecture — practical guide and template

**Source:** Sergei Budnik's authored `HLA_FAQ.docx` (v1.0.0, 2025-09-04), adapted for web publication.

## What is HLA?
High-Level Architecture describes the system at a top level: its key components, external integrations, responsibilities, and interactions. It gives business stakeholders, analysts, architects and developers a shared picture before low-level design.

## 1. System context
- **Business capability:** [What problem does the system solve?]
- **System boundary:** [What is inside and outside scope?]
- **Actors and external systems:** [Users, service providers, banks, platforms]

## 2. Components and responsibilities
| Component | Responsibility | Inbound interface | Outbound dependency |
|---|---|---|---|
| [Client] | [User interaction / initiation] | [Channel] | [API Gateway] |
| [API / integration layer] | [Routing, validation, orchestration] | [REST] | [Domain service] |
| [Domain service] | [Business operations] | [Internal API] | [Database / events] |

## 3. Interfaces and information flow
For each system interaction, describe:
1. Source and target
2. Data or business event exchanged
3. Synchronous or asynchronous operation
4. Protocol / integration style
5. Expected failure behavior and responsibility

| From | To | Flow | Type / protocol | Exception consideration |
|---|---|---|---|---|
| [Source] | [Target] | [Operation] | [REST / MQ / event] | [Timeout, retry, fallback] |

## 4. Diagram standards
The original HLA guide suggests:
- C4 Context or Container diagrams for clear levels of abstraction
- UML Deployment or simple component diagrams where appropriate
- Legends for arrows, boundaries and notations
- Companion tables explaining the responsibilities of each component

## 5. Review checklist
- [ ] All key components and external dependencies are shown
- [ ] Responsibilities and ownership are unambiguous
- [ ] Data-flow arrows are labelled
- [ ] Sync and async interfaces are distinguishable
- [ ] Important security and availability constraints are captured
- [ ] Diagram is readable without the author explaining every arrow
- [ ] Detailed implementation concerns are delegated to LLD / specifications

**Design rule:** HLA should be detailed enough to support decisions, but not so detailed that it becomes a code-level implementation diagram.
