---
title: Full-Stack SRS — Extended Template
sidebar_position: 17
---

# Extended SRS: From Business Process to API and Data Model

**Source basis:** `SRS_TEMPLATE_1.docx` (STORAGE, v1.0.0, September 2025), a structured end-to-end SRS illustrated with a food delivery service. This is a **new public teaching adaptation**. Original embedded images, internal test URLs and old subscriber notices are not reproduced.

Unlike the [standard SRS template](srs-template.md), this source includes business analysis, UI specification, microservice architecture, database design and integration contracts in one delivery package.

## 1. Governance and requirements context

| Original source section | Information to capture |
|---|---|
| Glossary | Domain entities and technical terms |
| History of changes | Version, date, owner and change description |
| Stakeholders | RACI responsibilities for analyst, developer, product owner and tester |
| Problem | Business pain points, target audience and current process |
| Development goal | Value, expected capabilities and business constraints |
| Product description | Actors, functions, external dependencies |
| Business processes | Process steps and business decisions |
| CJM | User journey stages and friction |
| BPMN | As-is/to-be flows, actors, gateways and exception paths |
| AS-IS / TO-BE | How responsibilities and outcomes change |

**Source example:** The food-delivery application aims to improve customer ordering convenience, restaurant reach and order coordination.

## 2. Requirements specification

The original separates **user stories**, **use cases**, **functional requirements** and **non-functional requirements**.

| Field | Use |
|---|---|
| `Story ID` | Trace to epic and acceptance criteria |
| `Use Case ID` | Trigger, preconditions, success and alternative flow |
| `FR ID` | Observable system behavior |
| `NFR ID` | Measurable cross-cutting constraint |
| `Test ID` | Verification and test ownership |

An adapted worksheet should record ID, actor, desired behavior, validation rule, error state and acceptance evidence. The related [Food Delivery SRS example](../examples/food-delivery-srs.md) includes source-grounded sample functions.

## 3. Frontend implementation

The original source explicitly includes **entry points, design, screen transitions, UI description, user interactions and caching**.

| Screen / interaction | Data & action | Exception / verification |
|---|---|---|
| Restaurant listing | Search and filter list; select restaurant | Empty/loading/error; search pagination |
| Restaurant page | View menu and open dish details | Dish unavailable or changed |
| Basket | Quantity changes and recalculated total | Price changed / duplicate tap |
| Checkout | Start payment with selected method | UNKNOWN outcome and status recovery |

The last column is **additional design-review guidance**, not a direct copy of source text.

## 4. Backend implementation

Original headings include **Architecture (C4)**, **Microservices**, **DB**, **ER diagram**, **Description of tables and fields**, **Database and API mapping**, **Sequence diagram**, **API** and **Message queue**.

The source includes a conceptual `delivery` microservice responsible for order, restaurant and support workflows. The public edition makes ownership boundaries explicit; it does not claim they were independently deployed.

### Component specification table

| Component | Owns | Interfaces |
|---|---|---|
| Merchant Catalog | Restaurant and dish read model | REST / database |
| Order Service | Commercial order, status changes | REST / outbox |
| Payment Adapter | Processor interaction and status enquiry | Provider API |
| Courier Dispatch | Delivery assignment and courier state | Event / REST |
| Notification Consumer | Customer status messages | Queue / provider |
| Reconciliation | External payment status/financial alignment | File/event |

**Source basis:** UI and backend section categories, order/courier roles, data-to-API mapping and queue concepts. **New additions:** distinct payment/reconciliation ownership and resilient integration controls.

## 5. Status & role models

The source's example includes role permissions for **Client, Courier and Technical Support Employee**. The status model must reject unsupported direct jumps (for example, **New → Delivered**).

A new implementation should explicitly define permitted transitions, reason codes, transactional state ownership and role checks.

- [Editable payment/outcome state reference](../payments/state-machine.md)
- [Source-based Food Delivery SRS](../examples/food-delivery-srs.md)
- [Food Delivery BPMN](../editable-source-diagrams.md)

## 6. Template 1 vs Template 2

| SRS Template 1 | SRS Template 2 |
|---|---|
| Full-stack BA → HLD → UI → backend implementation | Formal specification organized by quality categories |
| CJM, BPMN, AS-IS/TO-BE, C4, ER, API and MQ | Functional, usability, reliability, performance, supportability |
| Practical integrated delivery dossier | Formal cross-functional requirements baseline |

**Related:** [Download templates](../downloads.md) · [License](../license.md). This page is an authored synthesis of the source structure with additions clearly identified.
