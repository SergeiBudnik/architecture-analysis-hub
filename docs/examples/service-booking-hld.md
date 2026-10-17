---
title: HLD Example — Service Booking Platform
sidebar_position: 4
---

# High-Level Architecture Example: Service Booking Platform

**Public adaptation of:** `HIGH _LEVEL_ARCITECTURE_EXAMPLE_2.docx` from Sergei Budnik's STORAGE library (2025).  
**Source-based elements:** Separate customer/administration/CRM interfaces; API gateway; user, order, session, authorization and notification services; message broker; external acquiring/payment service; and integration tables.  
**Publication changes:** Internal names, exact host configuration, deployment IDs and organization-specific operational flows are **not reproduced**. This is a newly generalized and fictional educational solution. The recovery controls below are review recommendations, not assertions about the original implementation.

## 1. Business context

A fictional service-booking platform supports customers booking advisory or training sessions, an operations team coordinating availability, and a commercial team processing orders and customer details.

### Main capabilities

- Register or identify a user and control access by role.
- View available sessions, make a booking, update or cancel within business rules.
- Create and track a service order and a payment attempt.
- Send email notifications asynchronously.
- Integrate with an external payment provider and a conferencing/scheduling tool.

## 2. Component responsibilities

| Logical component | Responsibility | Interface |
|---|---|---|
| Customer Portal | Customer-facing session selection and order view | HTTPS to gateway |
| Operations Portal | Session and booking administration | HTTPS to gateway |
| CRM Portal | Sales/assistance workflows | HTTPS to gateway |
| API Gateway | Authentication context, routing and request controls | REST |
| User Service | User profiles and ownership | Internal API |
| Order Service | Service-purchase orders and commercial status | Internal API |
| Session Service | Booking slots, reservation and expiry rules | Internal API |
| Authorization Service | Role-based permissions | Internal API |
| Notification Service | Asynchronous emails and operational messaging | Queue and email provider |
| Broker | Durable decoupling of notification tasks | Message queue |
| External Payment Provider | Payment initiation and provider status | HTTPS, webhook/status enquiry |

This table generalizes the original HLD's **component description, external interactions, internal interactions and technology-stack sections**.

## 3. High-level interactions

| Flow | Initiator | Receiver | Mode | Typical failure consideration |
|---|---|---|---|---|
| Book session | Customer Portal | Session Service via gateway | Synchronous | Concurrent slot reservation |
| Create order | Customer Portal | Order Service | Synchronous | Duplicate submission |
| Pay order | Order Service | Payment Adapter / Provider | Asynchronous outcome | Ambiguous payment result |
| Notify customer | Order Service | Notification Service via broker | Asynchronous | Retry and DLQ |
| Check access | Gateway / services | Authorization Service | Synchronous | Deny access if permission cannot be verified |
| Start session | Session Service | External conferencing provider | Provider-specific | Link expiry and provider outage |

## 4. Editing the architecture

- [Editable PlantUML HLD](https://github.com/SergeiBudnik/architecture-analysis-hub/blob/main/diagrams/storage-adapted-service-booking-hld.puml).
- [HLD reusable template](../templates/high-level-architecture-guide.md).
- [Event-driven reliability reference](../payments/event-driven-processing.md).

## 5. Architecture decisions to validate

- One service must own the authoritative reservation for a time slot.
- Order status is separate from payment attempt state.
- Client redirect is not proof of payment success; verified provider evidence is required.
- Notification delivery may retry without creating a new order/payment.
- Durable events, correlation IDs and unique operation keys support recovery.

**Educational warning:** The original HLD contains concrete component identifiers, third-party integration references and deployment specifics. Those elements were intentionally omitted; this is not an exact client architecture reproduction.

**License:** [CC BY 4.0](../license.md) for this public authored adaptation.