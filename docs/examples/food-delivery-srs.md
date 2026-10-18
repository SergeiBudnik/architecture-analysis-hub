---
title: Complete SRS Example — Food Delivery
sidebar_position: 8
---

# Software Requirements Specification: Food Delivery App

**Source:** `SRS_EXAMPLE_1.docx` from the author's STORAGE collection (v1.0.0, 2025-09-04). **Public edition:** a sanitized educational adaptation; it is not evidence of a live food-delivery business.

## 1. Context and business objectives

The original SRS identifies four problems: customer convenience, restaurant reach/revenue, coordination of orders, and visibility of delivery/service quality.

The source's goals are revenue growth, a stronger consumer-facing brand, diversification, analytics to improve marketing/operations, and better customer retention.

## 2. Product and users

| Actor | Goals |
|---|---|
| Customer | Find restaurants, inspect dishes, manage basket, pay, track courier |
| Courier | Accept delivery assignment and update progress |
| Restaurant/operator | Maintain availability and respond to fulfilment tasks |
| Support specialist | Resolve questions via built-in chat |

The first two roles and the customer-facing requirements are source-grounded; the restaurant/operator and specialist responsibility descriptions are added as architecture-review interpretations.

## 3. Thirteen functional requirements from the example

| ID | Functional requirement |
|---|---|
| FR-01 | List restaurants with name, delivery time, highlighted dishes, rating and promotion |
| FR-02 | Search restaurants by name |
| FR-03 | Show the selected restaurant's menu with prices, dish weight and calories |
| FR-04 | Add a dish to basket from restaurant menu |
| FR-05 | Open a dish detail with name, description, nutritional value and price |
| FR-06 | Choose quantity and add dish to basket |
| FR-07 | Show basket contents, unit prices, weight, quantities, delivery cost/time and order total |
| FR-08 | Change quantity for each basket item |
| FR-09 | Remove dish from basket |
| FR-10 | Pay for an order from basket |
| FR-11 | Contact support by embedded chat |
| FR-12 | Track courier position on a map |
| FR-13 | Receive order-status notifications |

Requirements are numbered for public traceability; the original lists them sequentially as “Requirement 1–13”.

## 4. Five non-functional statements in the source

| ID | Source meaning | Review needed before delivery |
|---|---|---|
| NFR-01 | Work on iOS, Android and desktop/mobile web | Supported OS/browser versions |
| NFR-02 | Russian and English localisation | Locale coverage and translation QA |
| NFR-03 | Protect payment data in transit with HTTPS/TLS | PCI scope, tokenization and end-to-end data protection |
| NFR-04 | Support “1 million concurrent users per day” without performance loss | **Ambiguous unit**: concurrent users vs daily active users; define TPS and load model |
| NFR-05 | Separate User and Courier roles and interfaces | Back-end access-control tests |

**Important:** The phrase “one million concurrent users per day” is reproduced as an example's wording; it is not a coherent measurable capacity specification until clarified.

## 5. User stories in the source

The original includes examples for menu browsing, adding/removing dishes, card payment, courier order acceptance, and delivery tracking. See [User Story Examples](user-story-examples.md) for a separate adapted document.

## 6. User registration use case

The source gives an SMS-code registration scenario with input validation, resend, expiration and unsuccessful attempts. A full separate adaptation is available at [User Registration Use Case](sms-registration-use-case.md).

## 7. Frontend requirements

**Entry points:** launched app, push notification or SMS link.

**Home:** search input triggers keyboard; submit searches restaurants; restaurant card opens the restaurant page.

**Restaurant:** selecting a dish opens detail; the add button puts a dish in the basket; pull-to-refresh updates the menu list.

**Design review additions:** Show loading/empty/error states, duplicate-submit protection, pricing currency and source of truth, and permission controls for support chat. These additions are not asserted as literal source requirements.

## 8. Data model from the source

The SRS contains tabular entities for **Delivery, User, Order, Ordered Dishes, Restaurant, Payment and Dishes**. A separate source-based [database design example](restaurant-database-design.md) expands the relationships and corrects unsafe storage patterns.

**Safety correction:** Do **not** publish payment-card number, expiration date or CVV as recommended storage fields. Use appropriate PCI-compliant tokenization and avoid storing sensitive authentication data such as CVV.

## 9. Acceptance scenarios

| Test | Example expected behavior |
|---|---|
| Restaurant search | Customer searches and receives matching restaurants |
| Basket quantity | Totals recalculate when quantities change |
| Card payment callback lost | Payment remains pending/unknown until verified |
| Courier location unavailable | UI shows last known status rather than invented movement |
| SMS registration duplicate | Retry does not create duplicate accounts |
| Role separation | Customer cannot perform courier-only actions |

Tests in this section are new educational suggestions derived from the requirements, not verbatim source text.

**Related:** [Food delivery BPMN download](../editable-source-diagrams.md), [database schema example](restaurant-database-design.md), [blank SRS template](../templates/srs-template.md). **Licence:** [CC BY 4.0](../license.md).
