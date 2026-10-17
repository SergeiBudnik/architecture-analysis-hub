---
title: Message Broker Listener Specification
---

# Message Broker Listener Specification

*Adapted from Sergei Budnik's authored source library, `MQ_SRS_TEMPLATE.docx` (v1.0.0, September 2025). This is a public Markdown adaptation; placeholder fields and technical example values are illustrative.*

## 1. Description
**Listener:** [Name]  
**Queue / topic:** [Name]  
**Trigger:** New message  
**Consumer:** [Service]

## 2. Incoming message
**Format:** JSON

| Field | Location | Type | Required | Meaning |
|---|---|---|---|---|
| requestId | header | UUID | Yes | Event identification |
| type | header | string | Yes | Event type |
| payload | body | object | Yes | Business data |

## 3. Message example
```json
{"requestId":"00000000-0000-4000-8000-000000000001","type":"example.event","payload":{"entityId":"123"}}
```

## 4. Processing sequence
1. Consumer receives a message and begins its processing transaction.
2. Validate content and map it to the downstream request.
3. Call [downstream service].
4. On success, acknowledge / commit.
5. On transient failure, apply the defined retry/redelivery policy.
6. On permanent failure, record the exception and route to dead-letter queue when configured.

## 5. Integration mapping
| Incoming field | Downstream field | Transformation |
|---|---|---|
| requestId | event_id | Preserve |
| type | event_code | Preserve / map |

## 6. Failure handling
| Failure | Detection | Handling |
|---|---|---|
| Unavailable dependency | Timeout or connection error | Retry according to configuration |
| Business rejection | Explicit rejection response | Handle without infinite retry |
| Poison message | Repeated or invalid payload | Dead-letter queue / manual investigation |

> The original sample describes increasing retry delays, with a dead-letter queue for selected failures. Exact delays and acknowledgement semantics must be chosen for the actual broker and application.
