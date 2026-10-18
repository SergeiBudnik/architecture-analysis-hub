---
title: User Story Examples — Food Ordering
sidebar_position: 13
---

# User Stories: Food Delivery Application

**Source:** `USER_STORY_EXAMPLE.docx` from Sergei Budnik's STORAGE collection (v1.0.0, September 2025). The original file contains **four user stories** in a table, reproduced below in their original business framing as a new educational public edition.

| No. | Actor | User story |
|---|---|---|
| US-01 | Customer | As a user, I want to browse the menu of a specific restaurant so that I can select dishes I like |
| US-02 | Customer | As a user, I want to add and remove dishes from my order so that I can assemble the desired order |
| US-03 | Customer | As a user, I want to pay for the order by card so that I can complete ordering and payment |
| US-04 | Courier | As a courier, I want to accept an order so that I can begin delivery |

## Example acceptance criteria (added for instructional use)

**US-02 — Basket editing**

- Given a customer has opened a restaurant menu, when they add an available dish to the basket, then the basket contains that dish and its selected quantity.
- Given the basket has a dish, when the customer removes it, then that dish is absent and the order total is recalculated.

**US-03 — Card payment**

- Given a valid pending order, when the customer authorizes payment and the provider confirms success, then the order payment state becomes confirmed.
- Given the payment provider times out after receiving the request, then the platform keeps the outcome **pending/unknown** instead of reporting a decline without evidence.

**US-04 — Courier acceptance**

- Given a courier is offered a currently available order, when they accept it, then only one courier is assigned by the authoritative dispatch service.
- Given another courier already accepted the order, then the second acceptance is rejected or offered an updated assignment state.

The original contained only the **story table**. The acceptance criteria, states and business ownership rules are **new teaching additions**. They are not claims about a deployed delivery platform.

## Traceability

| Story | Related use case / specification |
|---|---|
| US-01 | [Food Delivery SRS, FR-03/FR-05](food-delivery-srs.md) |
| US-02 | [Food Delivery SRS, FR-04/FR-06–FR-09](food-delivery-srs.md) |
| US-03 | [Food Delivery SRS, FR-10](food-delivery-srs.md) |
| US-04 | [Food Delivery BPMN process](../editable-source-diagrams.md) |

[User Story Template](../templates/user-story-template.md) · [CC BY 4.0](../license.md).
