---
title: Use Case Template
---

# Use Case Template

*Adapted from Sergei Budnik's authored source library, `USE_CASE_TEMPLATE.docx` (v1.0.0, September 2025). This is a public Markdown adaptation; placeholder fields and technical example values are illustrative.*

## Use case identity
| Field | Value |
|---|---|
| Title | [Action name] |
| Identifier | UC-001 |
| Brief description | [User goal] |
| Primary actor | [Actor] |
| Goal | [Outcome] |
| Preconditions | [Conditions that must be true] |
| Postconditions | [System state on success] |

## Main scenario
| Step | Actor action | System response | Notes |
|---|---|---|---|
| 1 | [User initiates] | [System presents] | [Rules / reference] |
| 2 | [User provides data] | [System validates] | [Constraint] |
| 3 | [User confirms] | [System completes action] | [Expected result] |

## Extensions and alternative flows
| Branch | Trigger | Alternative behavior | Outcome |
|---|---|---|---|
| 2a | [Validation fails] | [Show error and allow correction] | [Return to step 2] |
| 3a | [Downstream unavailable] | [Report unavailability] | [Stop or retry as designed] |

## Acceptance criteria
- Given [initial condition], when [action], then [expected behavior].
- [Error and boundary conditions are addressed].
