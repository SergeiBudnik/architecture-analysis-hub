---
title: REST API Design — Ten Problems, Trade-offs & Contracts
sidebar_position: 2
---

# REST API Design: Ten Recurring Design Problems

**Source basis:** Sergei Budnik, `API_PARAMETERIZATION.docx`, STORAGE v1.0.0, 4 September 2025. The private source contains **10 numbered problems** with alternative solutions, pros, cons and final implementation recommendations. This expanded public edition preserves **that same problem order and trade-off framing**. New security, payment-recovery and concrete OpenAPI illustrations are explicitly identified as additions. No historical production interface is claimed.

## 1. Chaotic structure and endpoint naming

**Source problem:** Paths such as `/getUsers`, `/addNewPost` and `/user/12-3/updateEmail` mix verbs, singular/plural naming and business actions, making an API harder to predict.

| Source alternative | What it solves | Trade-off |
|---|---|---|
| A — Resource-oriented | `GET /users/{id}`, `POST /users`; nouns and standard HTTP methods | Complex commands may not fit ordinary CRUD |
| B — Verb/RPC-oriented | `POST /users/{id}/activate` exposes a named action | Uncontrolled growth of unique methods |
| Hybrid | Default to resources, allow carefully agreed command routes | Requires consistent team guidelines |

**Recommendation derived from source:** Prefer stable resource names, with narrowly scoped command endpoints where a real domain operation is not naturally CRUD.

## 2. Too much or too little response data

**Source problem:** Returning every field over-fetches; forcing one request per related resource causes N+1 HTTP calls.

| Source option | Example | Benefit | Cost |
|---|---|---|---|
| Sparse field selection | `GET /users?fields=id,name` | Smaller payload | Complex projection rules and query risk |
| Embedding related resources | `GET /posts?embed=author,comments` | Fewer requests | Larger responses and expensive joins |
| Predefined views | `GET /users?view=summary` | Server-optimized representation | Less client flexibility |

**New implementation controls:** Enforce an allow-list of selectable fields, response size budget, maximum embedding depth and authorization on embedded data. Field selection must not bypass row or field-level access checks.

## 3. Large collections and pagination

**Source options:** `limit/offset` for simplicity/random access versus **keyset (cursor) pagination** for large and changing collections.

| Mechanism | Strength | Failure mode / limitation |
|---|---|---|
| `?limit=50&offset=5000` | Easy page navigation | Costly large offsets and list instability under inserts |
| `?limit=50&after_id=54321` | Scalable and stable for a supported sort | Requires stable indexed ordering; opaque cursor may be preferable |

**New implementation controls:** Maximum page size, deterministic tie-breaker sorting (`created_at + id`), cursor validation, tenant-bound queries, and documented behavior under deletions.

## 4. Evolving APIs without breaking consumers

**Source alternatives:** URL version (`/v1/users`), header/negotiated version, and backward-compatible evolution.

| Approach | Advantage | Cost |
|---|---|---|
| URL path version | Visible and simple to route | Coexisting versions and migration overhead |
| Header/media-type version | Keeps resource URI stable | Less obvious to troubleshoot |
| Backward-compatible fields | Reduces unnecessary version churn | Requires strict compatibility discipline |

**New reviewer checklist:** Define what counts as breaking (required request field, removed enum, changed monetary semantics, auth change); publish deprecation timing; test against representative client contracts.

## 5. Error handling

**Source solution:** A **standardized JSON error object**, rather than inconsistent error strings or transport-only statuses.

A newly authored, provider-neutral example based on the source pattern:

```json
{
  "type": "https://example.invalid/problems/validation",
  "title": "Invalid request",
  "status": 422,
  "detail": "The supplied currency is unsupported",
  "instance": "/payment-intents/attempt-123",
  "correlationId": "demo-correlation-001"
}
```

**New recommendation:** Consider RFC 9457 Problem Details or a documented equivalent; separate validation errors, business refusals, transient technical failure and unknown post-dispatch outcomes. Never expose internal stack traces, tokens or personal data.

## 6. Non-atomic operations

**Source issue:** A cross-service operation cannot simply be assumed to commit atomically across independently managed systems.

| Source solution | Good fit | Trade-off |
|---|---|---|
| Transaction resource / tracked workflow | Visible lifecycle with a single status endpoint | Requires orchestration and durable state |
| Saga | Distributed steps with compensations | Compensation can fail or differ from a true rollback |

**New payment-specific qualification:** A completed external payment is **not** rolled back by merely reverting a local database row; reversal/refund is a separate business operation with its own finality and reconciliation rules.

## 7. Long-running asynchronous operations

**Source alternatives:**

- **202 Accepted + Task resource:** start work and poll an operation status.
- **Webhooks:** downstream async notification; authentication and retries needed.
- **WebSockets / Server-Sent Events:** server pushes progress to active clients.

New synthetic example:

```http
POST /report-jobs
HTTP/1.1 202 Accepted
Location: /report-jobs/job-2026-001
Retry-After: 10
```

Client polls `GET /report-jobs/job-2026-001` until a terminal state. Define `QUEUED`, `RUNNING`, `SUCCEEDED`, `FAILED` and expiration.

**New recovery controls:** Durable queueing, access-scoped status URLs, non-guessable IDs, callback signature verification, bounded retries and dead-letter review.

## 8. Idempotency and retry safety

**Source solutions:** Client-provided `Idempotency-Key` for retryable commands, plus server-enforced unique business keys where appropriate.

**New engineering recipe for payment initiation:**

1. Define scope: e.g. merchant + operation type + idempotency key.
2. Store a hash of the normalized, non-sensitive request and current outcome.
3. Reject reuse of the same key with materially different parameters.
4. Prevent concurrent duplicate dispatch via durable unique claim/lock.
5. On timeout **after dispatch**, keep an unknown state and inquire with the provider; never assume `DECLINED`.
6. Return stored confirmed outcome for equivalent subsequent retries and define key expiry.

**Source boundary:** The storage algorithm above is a modern payment-reliability expansion, not a verbatim algorithm from the original ten-problem guide.

## 9. Managing complex data graphs

**Source alternatives:** **GraphQL facade**, **JSON:API/OData**, and **Backend for Frontend (BFF)** for channel-oriented representations.

| Option | Advantage | Risk |
|---|---|---|
| GraphQL facade | Client selects graph fields | Query depth, cost, authorization and caching |
| JSON:API / OData | Standardized query and relationship semantics | Additional protocol complexity |
| BFF | Tailored representation per web/mobile channel | Service maintenance and logic duplication |

**New review control:** Enforce query cost/complexity budgets and consistent field-level access across nested resources.

## 10. Bulk operations

**Source alternatives:** A **single batch endpoint** (synchronous) and **asynchronous batch processing** for large workloads.

Example:

```http
PATCH /employees/bulk-update
Content-Type: application/json
```

```json
{
  "employees": [
    {"id": "EMP-101", "department": "Operations"},
    {"id": "EMP-102", "department": "Support"}
  ]
}
```

**Source trade-off:** Partial success needs per-item outcomes; the original mentions HTTP **207 Multi-Status**. **New qualification:** 207 is one possible contract choice, originally defined for WebDAV; it is not a universal requirement for bulk REST operations. HTTP 200/202 with explicit item outcomes is also defensible if clearly specified.

For large jobs, return 202 plus a correlation/task identifier and include durable per-item status, restart and result retention policies.

## Cross-cutting source conclusions

The source's closing recommendations emphasize **API as a developer product**, **security by default**, **documentation**, **HTTP caching (`Cache-Control`, `ETag`, `Last-Modified`)**, **rate limiting**, observability and designing for high-load mobile use.

### New API review checklist

- [ ] Resources and command names follow agreed conventions.
- [ ] Each request, response, filter, cursor and conditional field is specified.
- [ ] Authentication, authorization, data exposure and tenant isolation are explicit.
- [ ] Idempotent operations and ambiguous provider outcomes have a recovery contract.
- [ ] `429`, timeout, validation, retry, and terminal business refusal semantics are distinct.
- [ ] Partial/bulk processing specifies per-item atomicity and error aggregation.
- [ ] Webhooks are authenticated, replay-safe and observable.
- [ ] OpenAPI schemas and example payloads are validated in CI.
- [ ] Breaking changes have a migration/deprecation policy.
- [ ] Non-functional requirements specify measurable latency, throughput and availability.

## Downloadable reference

- [Editable API parameterization guide (RTF)](https://github.com/SergeiBudnik/architecture-analysis-hub/raw/refs/heads/main/static/editable/api-parameterization-public.rtf)
- [OpenAPI 3.1 payment-intent reference JSON](https://github.com/SergeiBudnik/architecture-analysis-hub/raw/refs/heads/main/static/editable/payment-intents-reference-openapi.json) (new, fictional educational contract)
- [Employee Bulk Update API](../examples/employee-bulk-update-api.md), [Async Report Sequence](../examples/async-accounting-report-sequence.md), [Payment State Machine](../payments/state-machine.md).

**Public adaptation, CC BY 4.0.** No bank- or scheme-specific interface is represented as authoritative. Original source file remains private.
