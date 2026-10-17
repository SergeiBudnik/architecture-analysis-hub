---
title: Frontend Screen Specification Template
---

# Frontend Screen Specification Template

*Adapted from Sergei Budnik's authored `FRONT_SRS_TEMPLATE.docx` (2025).* 

## General information
**Screen name:** [Name]

**Business process reference:** [Link]

**UI design:** [Approved mockup link]

## Initial loading
List methods invoked before the screen is rendered and define error handling for each operation.

| API method | Purpose | Loading state | Failure state |
|---|---|---|---|
| [Method] | [Data to obtain] | [Placeholder] | [User-facing error] |

## UI element mapping
| UI element | Type | Display rule | Data source | Validation |
|---|---|---|---|---|
| [Element] | [Text / input / button] | [Condition] | [Field] | [Constraint] |

## Active actions
| Action | Trigger | Request | Result |
|---|---|---|---|
| [Action] | [User interaction] | [API call] | [Success / failure] |

## Presentation behavior
Describe pagination, scrolling, responsive layout, empty state, and platform-specific differences.

## Revision history
| Version | Date | Changes |
|---|---|---|
| 0.1 | [Date] | Initial draft |
