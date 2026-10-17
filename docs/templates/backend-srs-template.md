---
title: Backend Service Specification Template
---

# Backend Service Specification Template

*Adapted from Sergei Budnik's authored source library, `BACK_SRS_TEMPLATE.docx` (v1.0.0, September 2025). This is a public Markdown adaptation; placeholder fields and technical example values are illustrative.*

## 1. Description
**Operation:** [Method / service / objective]  
**Owning component:** [Service]  
**Trigger:** [Caller / event]

## 2. Request
**Method and route:** `POST /resource/action`

| Parameter | Location | Type | Required | Description |
|---|---|---|---|---|
| requestId | header | string | Yes | Correlation identifier |
| resourceId | body | string | Yes | Resource to process |

## 3. Response
| Field | Type | Mandatory | Description |
|---|---|---|---|
| result | string | Yes | Outcome |
| errorCode | integer | On error | Machine-readable failure code |
| errorCause | string | On error | Diagnostics, if appropriate |

## 4. Examples
**Request:**
```json
{"resourceId":"example-123"}
```

**Response:**
```json
{"result":"accepted"}
```

## 5. Processing flow
1. Validate the caller and request.
2. Call [internal system] and map parameters (see section 7).
3. Call [external system], if applicable (see section 8).
4. Save results using the persistence rules (section 9).
5. Map the final response (section 10); apply failure handling (section 11).

## 6–8. Dependencies and mappings
| Source field | Target field | Rule | Mandatory |
|---|---|---|---|
| [source] | [target] | [Transformation] | [Y/N] |

## 9. Data persistence
[Tables, insert/update policy, uniqueness, transaction boundaries.]

## 10. Response formation
[Statuses, return fields, decision mapping.]

## 11. Error processing
[Validation error, timeout, dependency failure, duplicate request and recovery.]
