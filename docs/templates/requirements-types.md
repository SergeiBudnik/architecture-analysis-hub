---
title: Business, Functional and Non-Functional Requirements
---

# Business, Functional and Non-Functional Requirements

*Adapted from Sergei Budnik's authored source library, `REQUIREMENTS_DOCUMENTATION_FAQ.docx` (v1.0.0, September 2025). This is a public Markdown adaptation; placeholder fields and technical example values are illustrative.*

## Core distinctions from the source library

**Business Requirement (BR)** states the business outcome or value to achieve.  
**Business Requirements Document (BRD)** is the document collecting business requirements and scope.

**Functional Requirement (FR)** defines observable system behavior.  
**Software Requirements Specification (SRS)** is the complete specification artifact that may include FRs, interfaces, constraints and other requirements.

**Non-Functional Requirement (NFR)** defines qualities or constraints, such as performance, availability or supportability.

> **FR ≠ SRS. BR ≠ BRD.** A requirement is not the same thing as the document containing requirements.

## Traceability example
| Business objective | Functional requirement | Non-functional requirement | Acceptance evidence |
|---|---|---|---|
| BR-01: Improve self-service access | FR-01: Users can retrieve their order status | NFR-01: Define measurable response time | User test and load test |

## Review checklist
- [ ] BR states the business outcome rather than implementation detail.
- [ ] FR describes behavior that can be verified.
- [ ] NFR has a measurable target.
- [ ] Requirements have unique identifiers.
- [ ] SRS references business context and acceptance criteria.
