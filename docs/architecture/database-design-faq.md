---
title: Database Schema Design — FAQ & Checklist
sidebar_position: 16
---

# Database Schema Design: FAQ, Modeling Choices and Review Checklist

**Publication note:** The source file `DATABASE_DESIGN_FAQ.docx` discusses schema types, logical/physical models, normalisation, naming and security. It also contains a section promoting **Integrate.io**, indicating third-party editorial material. The source prose is **not republished or relicensed here**. The explanations below are independently rewritten as an original educational guide.

## What is a database schema?

A database schema specifies the structure and constraints of stored data. In a relational system it commonly defines tables, attributes, keys, types, indexes, constraints and relations between entities.

## Logical versus physical schema

| Model | Describes | Review example |
|---|---|---|
| Logical | Entities, relationships, cardinality, required information | Order is owned by a Customer; an Order has one or more Items |
| Physical | Tables, data types, indexes, partitions and performance/retention mechanisms | `food_order` PK UUID; `order_item.order_id` FK; index on creation timestamp |

A conceptual data model is useful before choosing a specific SQL engine. A physical design should also consider traffic, query plans, migration strategy and operational recovery.

## What database schema styles are commonly discussed?

| Style | Typical usage | Limitations |
|---|---|---|
| Flat | Small, simple tabular datasets | Limited entity separation |
| Hierarchical | Tree-structured ownership | Difficult for cross-branch relationships |
| Network | Explicit many-to-many record relationships | More complex traversal/maintenance |
| Relational | Transactional applications, integrity | Schema migrations and cross-table joins |
| Star | Analytical fact + dimensions | Denormalisation/ETL governance |
| Snowflake | Normalised dimension tables in analytics | Extra joins and transformation complexity |

These six categories are discussed in the original FAQ, but selection guidance is independently authored for this public edition.

## How should keys and relationships be chosen?

- Identify stable **primary keys** and referenced **foreign keys**.
- Record relationship cardinality and optionality before writing schema.
- Define uniqueness for business identity in a clear scope (for example `merchant_id + external_reference`).
- Do not confuse a human-visible reference with a globally unique technical ID.
- Enforce concurrency and state-transition invariants transactionally.

## When is database normalization useful?

Normalization is a way to reduce duplicated or contradictory data by representing independently changing facts separately. For transactional systems it often simplifies updates. Denormalization may still be justified for read performance or analytic workloads **if update and reconciliation ownership is explicit**.

## Example schema — order and payment attempt

| Entity | Primary key | Key fields | Relation |
|---|---|---|---|
| Customer | `customer_id` | profile reference | One to many Orders |
| FoodOrder | `order_id` | merchant, amountMinor, currency, status | Many to one Customer |
| OrderItem | `item_id` | orderId, dishId, quantity, unitPriceMinor | Many to one FoodOrder |
| PaymentAttempt | `attempt_id` | orderId, processorRef, status, version | Many to one FoodOrder |
| ReconciliationCase | `case_id` | attemptId, breakReason, owner | Linked operational exceptions |

All identifiers are synthetic. For card payments, **do not store CVV**, and avoid raw PAN by using a provider-controlled token reference and proper PCI scope review.

[Open editable food-order ER diagram](https://github.com/SergeiBudnik/architecture-analysis-hub/blob/main/diagrams/storage-adapted-food-order-erd.puml).

## Naming and governance checklist

- [ ] Use meaningful table and field names; avoid reserved words.
- [ ] Define NULLability, uniqueness, defaults and allowed business values.
- [ ] Specify decimal/minor-unit handling for financial values.
- [ ] Identify PII, encryption, access rights and masking.
- [ ] Add audit, correction, deletion and retention rules.
- [ ] Document high-volume query access paths and indexes.
- [ ] Review backups, recovery, migration and rollback strategy.
- [ ] Trace schema entities back to business requirements/API contracts.

## About source rights

The original FAQ contains recognizable vendor-authored marketing material. It is **not covered by this site's CC BY declaration** merely by being stored in the author's source library. Only this independently written public guide is offered under [CC BY 4.0](../license.md).

**Related:** [Database Design Template](../templates/database-design-template.md) · [Food Ordering Database Example](../examples/restaurant-database-design.md).
