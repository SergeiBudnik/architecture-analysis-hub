---
title: Business Requirement Examples — Product Catalogue
sidebar_position: 15
---

# Business Requirements: Catalogue, Order Messaging and Store Discovery

**Source:** \`BR_EXAMPLE.docx\` from the author's original STORAGE collection (v1.0.0, 2025-09-04). The source juxtaposes three business-requirement examples and a small PIM requirement table. This edition retains the business intent but removes a named retailer and system-specific identifiers.

## Source guidance: what a business requirement is

The original says a business requirement should:

1. Correspond to a **specific business goal** served by the system.
2. Avoid prescribing low-level implementation.
3. Stay within the agreed project scope.

## Example A — Product Information Management

The original includes these requirement IDs:

| ID | Business need stated in source |
|---|---|
| PIM21 | Provide an internal product catalogue |
| PIM22 | Support finding products by attributes such as season and article number |
| PIM23 | Support a hierarchy such as product → model-color → model, with inherited configuration and level-specific descriptions |

**Review addition:** Verify which catalogue hierarchy is owned by the business and how overrides/inheritance should behave before assigning technical schemas.

## Example B — Order notifications for fulfillment staff

The source proposes a dedicated channel notifying warehouse/order-assembly staff about **orders with the “Auto” receipt type**. The original names a specific retailer's system, omitted here.

- **Business goal:** Ensure assembly staff receive relevant orders without having to search multiple systems.
- **In scope:** Event selection, delivery of order data, visibility of failed delivery.
- **Acceptance consideration (added):** Every eligible order is forwarded no more than once at business-effect level, and rejected notifications are observable.

## Example C — Store data and location discovery

The source includes two customer-value statements: correctly formalized store information on the website, reducing checkout blockers; and map location centered on the customer's city/town to reduce navigation steps.

| Objective | Suggested measurable acceptance (new) |
|---|---|
| Reliable store data | Test required store information fields and checkout mapping |
| City-first map discovery | Measure steps from opening location finder to selecting a store |

## Translating to architecture

The examples distinguish outcome-focused business requirements from follow-on functional and integration specifications. A real solution might later need a product catalogue service, event-driven fulfillment integration or geolocation/branch API; those are **design possibilities**, not requirements mandated by the original source.

**Related:** [BRD template](../templates/brd-template.md) · [HLD checklist](../architecture/architecture-document-checklist.md) · [CC BY 4.0](../license.md).
