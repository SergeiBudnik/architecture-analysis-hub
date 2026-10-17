---
title: Worked Example — Travel Booking BRD
sidebar_position: 1
---
# Worked example: online travel booking platform

**Author:** Sergei Budnik  
**Source:** Authored `BRD_EXAMPLE.docx` (2025-09-04).  
**Status:** Fictional educational example; these targets are not actual business results.

## Introduction

An online travel booking platform consolidates flight, hotel and car rental bookings previously performed across different services.

## Business goals

| ID | Objective |
|---|---|
| BO-01 | Increase revenue by 20% in the first year |
| BO-02 | Improve retention through loyalty |
| BO-03 | Reduce support workload by 30% using automation |

## Scope

- Search and booking for flights, hotels and car rentals
- Payments via Visa, Mastercard, PayPal and Apple Pay
- Loyalty programme
- English, Spanish, German and French interfaces
- Web and mobile channels

## Stakeholders

| Role | Responsibility |
|---|---|
| Executive Sponsor | Return on investment |
| Product Owner | Product scope and priorities |
| Compliance Officer | Regulatory requirements |

## Example business requirements

| ID | Requirement | Measurement |
|---|---|---|
| BR-01 | Search and compare flight, hotel and rental options | At least 80% of users complete searches without errors |
| BR-02 | Support online payment | Define measurable payment success criteria |

The original example reuses some BR numbers for objectives and requirements. This web edition uses distinct `BO` and `BR` prefixes for clarity.

## Constraints and assumptions

| Item | Example |
|---|---|
| Budget | GBP 1.5 million |
| MVP schedule | 9 months |
| Technologies | AWS, React and Node.js |
| Regulatory review | GDPR and PSD2 where applicable |

Partner API reliability is a source assumption requiring validation.

## Target success metrics

- 10,000 registered users within three months
- At least 90% successful bookings
- Average satisfaction at least 4.5 / 5
- 30% fewer support calls

## Risks

| Risk | Mitigation |
|---|---|
| External booking provider unavailable | Evaluate backup integration |
| Payment certification delay | Contact payment provider early |

## Review and sign-off

Business sponsor, product owner and compliance stakeholder should review this document before implementation.

**Related:** [Blank BRD template](../templates/brd-template.md).
