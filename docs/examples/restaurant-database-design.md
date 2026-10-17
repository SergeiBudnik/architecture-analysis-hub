---
title: Database Example — Food Delivery Platform
sidebar_position: 5
---

# Database Design Example: Food Ordering & Delivery

**Public adaptation of:** `DATABASE_DESIGN_EXAMPLE.docx` from the STORAGE library (2025).  
**Source-based entities:** Delivery, Order, Restaurant, User, Payment, Menu and Dishes, with entity relationships and attribute tables.  
**Security and modeling changes are intentional and explicitly noted below.** This is a fictional reference schema, **not a verbatim copy** of the original document or its embedded ERD.

## 1. Business scenario

A user selects dishes from a restaurant menu, creates an order, pays through an external payment processor and receives a delivery-status update.

## 2. Reference entities

| Entity | Key fields (synthetic) | Purpose and relationship |
|---|---|---|
| Customer | `customer_id` (PK), `display_name` | Customer who places orders |
| Restaurant | `restaurant_id` (PK), `name` | Restaurant that offers menus |
| Menu | `menu_id` (PK), `restaurant_id` (FK) | Menu owned by a restaurant |
| Dish | `dish_id` (PK), `menu_id` (FK), `name` | Dish offered on a menu |
| FoodOrder | `order_id` (PK), `customer_id` (FK), `restaurant_id` (FK), `amount_minor`, `currency` | Commercial order |
| OrderItem | `order_item_id` (PK), `order_id` (FK), `dish_id` (FK), `quantity`, `unit_price_minor` | Ordered dishes and price snapshot |
| Delivery | `delivery_id` (PK), `order_id` (FK), `status` | Delivery lifecycle |
| PaymentAttempt | `attempt_id` (PK), `order_id` (FK), `provider_reference`, `status`, `payment_token_reference` | Processing attempt linked to order |

**Additions vs source:** `OrderItem`, minor-unit monetary fields, payment attempt/state separation, and token reference are design improvements for this generalized edition. They are **not presented as fields from the original**.

## 3. Relationships

- One Customer can have many FoodOrders.
- One Restaurant can own many Menus and receive many FoodOrders.
- Each Menu can contain many Dishes in this simplified model.
- One FoodOrder has many OrderItems and may have multiple PaymentAttempts.
- A FoodOrder can have an associated Delivery.

The actual multiplicities and invariants should be agreed before database implementation. For example, some products require a menu-to-dish many-to-many link instead.

## 4. Critical security correction

The original `Payment` table includes **Card number**, **Expiration date** and **CVV** columns. **Do not copy this into a production schema.** In particular, sensitive authentication data such as CVV must not be stored after authorization, even if encrypted, under PCI DSS rules.

In this public example, payment details are represented instead by a **tokenized/opaque provider reference** and non-sensitive transaction identifiers. PCI scope, tokenization design and actual retention require specialist review.

Another source inconsistency: the original User table repeats a `Surname` field. This edition uses a single display name for simplicity.

## 5. Suggested constraints and indices

| Constraint | Rationale |
|---|---|
| `FoodOrder.customer_id` FK | Prevent orphan commercial orders |
| `OrderItem(order_id, dish_id)` business key where valid | Avoid unintended duplicate rows if business rules require uniqueness |
| Unique `PaymentAttempt.provider_reference` within provider scope | Correlate processor outcomes |
| Unique idempotency key in merchant/operation scope | Stop duplicate charges |
| Separate status-transition audit | Explain delivery/payment changes over time |

## 6. Diagram and review

- [Editable ER-style PlantUML](https://github.com/SergeiBudnik/architecture-analysis-hub/blob/main/diagrams/storage-adapted-food-order-erd.puml)
- [Database design template](../templates/database-design-template.md)
- [Payment state and idempotency](../payments/state-machine.md)

**Publication status:** Cleaned and expanded educational example only. Original embedded ER diagrams and Word file remain unreviewed and are not distributed.

**License:** [CC BY 4.0](../license.md) for this public adaptation.