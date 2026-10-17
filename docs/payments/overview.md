---
title: Payment Architecture Reference
sidebar_position: 1
---
# Payment Architecture — public reference patterns

**Author:** Sergei Budnik. These are **new synthetic reference designs**, informed by the author's payments architecture experience and the separate authored RoPay sequence/enterprise reference diagrams. They are **not** extracted bank or client specifications, nor a claim that particular banks implement these patterns.

## New: end-to-end A2A / QR / Deep Link case study

- [A2A QR / Deep Link Architecture](a2a-qr-deeplink.md) — synthetic HLD, provider-neutral initiation flows, API examples, callbacks and recovery.
- [A2A Design Decisions & Traceability](a2a-design-decisions.md) — architecture decisions, requirement mapping and a failure-mode test pack.

## Card acquiring and processing — new case study

- [Card Acquiring & Processing Architecture](acquiring-processing.md) — merchant, gateway, acquirer, network, issuer, authorization, reversal and capture.
- [Acquiring Design Decisions and Tests](acquiring-design-decisions.md) — architectural decisions, failure scenarios, traceability and NFRs.

## Clearing, settlement and reconciliation — new case study

- [Financial Lifecycle HLD](clearing-settlement-reconciliation.md) — authorization, capture, presentment, clearing, interbank settlement and merchant payout.
- [Worked Reconciliation Example](reconciliation-worked-example.md) — GBP 100 synthetic transaction, fee/payout calculation, ledger entries and GBP 0.50 break.
- [Clearing & Settlement Design Decisions](clearing-design-decisions.md) — data contracts, batch/file replay, audit, matching tests and failure controls.
- [Four editable PlantUML diagrams](clearing-settlement-reconciliation.md#8-diagrams) — component architecture, lifecycle, financial sequence and exception sequence.

## Navigate the patterns

1. [End-to-end payment processing](end-to-end.md): channel → orchestration → processor → external rail → merchant outcome.
2. [Payment state machines and idempotency](state-machine.md): intent, attempt, terminal-state handling and delivery safeguards.
3. [Timeouts, retries and reconciliation](reliability.md): safe recovery, callback, polling and ambiguous results.
4. [PlantUML architecture sources](diagrams.md): component HLD, transaction sequence and state diagram.

## Principles

- A **merchant order** is not the same entity as a **payment intent**, **payment attempt**, **authorization** or **ledger entry**.
- A timeout is **not proof of payment failure**.
- Callback delivery may be **at least once**, requiring idempotent consumers.
- Never blindly retry a payment instruction when its prior outcome is unknown.
- A processing acceptance is not necessarily the same as final settlement; distinguish each lifecycle.
- Model every external participant as a separate trust and failure boundary.

## Intended audience

Solution architects, systems analysts, integration engineers and fintech platform engineers who need readable templates and design review checklists. This resource is published freely for education; it is not legal or scheme implementation guidance.