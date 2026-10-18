---
title: BPMN 2.0 — Activities and Subprocesses
sidebar_position: 17
---

# BPMN 2.0: Activity Types and Modeling Decisions

**Provenance:** The private `BPMN_FAQ.docx` in STORAGE includes long text originating from **Visual Paradigm** documentation. This public page is **independently written** on the same general BPMN topics, **not a relicensing or reproduction of the vendor's prose or illustrations**.

## Choose the right task type

| BPMN activity | Use when | Example in a booking workflow |
|---|---|---|
| User task | A person completes work in software | Operator confirms an exception |
| Service task | System invokes a managed service | Request payment-provider status |
| Send task | Workflow sends a message | Send order confirmation |
| Receive task | Process waits for a message | Wait for asynchronous order status |
| Manual task | Human works without process engine support | Inspect goods before dispatch |
| Business rule task | A rule engine evaluates policies | Select approval workflow |
| Script task | Process engine executes its own script | Normalize process variables |

**Do not** model a message to another independent participant as a plain sequence flow; in BPMN, message flows cross pool boundaries.

## Task, sub-process and call activity

- **Task:** atomic from the process model's viewpoint, even if software internals are complex.
- **Sub-process:** expands to a set of activities that share a local process context; can be collapsed for overview.
- **Call activity:** invokes a separately defined reusable process/activity.

## Common sub-process semantics

| Feature | Modeler's question |
|---|---|
| Loop | Does one task/sub-process repeat until a condition changes? |
| Multi-instance | Are there multiple independent instances for different items/users? |
| Compensation | What business undo/compensating action is available after completed work? |
| Ad hoc | Are activities intentionally flexible in ordering/selection? |
| Event sub-process | What interrupts or observes an enclosing scope? |

**New payment-specific review:** Financial compensation is not a SQL rollback. Reversal, refund and dispute have independent network/provider rules and statuses.

## Common errors to check

1. Every gateway decision has well-defined exits, including an error/timeout path.
2. Pools represent independent participants; lanes represent internal responsibilities.
3. Timer events match SLA/expiry meaning (boundary interrupting versus non-interrupting).
4. Service tasks specify retries and unknown-result behavior.
5. Compensation paths exist only where the external effect is actually reversible.
6. Validate BPMN 2.0 XML, not just the picture.

## Editable example

[Food Delivery process (.bpmn)](../editable-source-diagrams.md) is a fictional learning example with payment choice, restaurant fulfilment, courier acceptance and customer receipt.

**Third-party exclusion:** The original Visual Paradigm marketing text and embedded images are not reissued under this site's [CC BY 4.0](../license.md). Only this independent guide is offered under the author's public license.
