---
title: For Educators & Practitioners
sidebar_position: 5
---

# For Educators & Practitioners

**Architecture & Analysis Hub** is a free, editable learning library by **Sergei Budnik** for business analysts, systems analysts, solution architects, fintech engineers and educators.

Use the teaching examples to explain architectural decisions, review system requirements or give students practical design exercises. Materials are **fictional and provider-neutral**: they are not live bank specifications, implementation warranties or payment-scheme certification guidance.

**Start with:** [Browse all downloads](downloads.md) · [Payment architecture](payments/overview.md) · [Share feedback](contribute.md) · [Public adoption log](community-adoption.md).

## Three ready-to-use learning paths

### 1. From requirements to an architecture decision (45–60 minutes)

**Audience:** BA/SAs, graduate students and junior solution architects.

**Resources:** [Extended SRS template](templates/full-stack-srs-outline.md), [Travel Booking SRS](examples/travel-platform-srs.md), [API Design patterns](architecture/api-design-patterns.md), [editable documents](downloads.md).

**Workshop outline:**

1. **10 min — Identify actors and boundaries.** Choose one booking flow; distinguish customer, booking service, external supplier and payment provider.
2. **15 min — Trace requirements.** Pick three functional requirements and two measurable NFRs. Find gaps, contradictions or undefined success criteria.
3. **15 min — Propose an HLD.** Assign ownership, interfaces, data and the likely failure points.
4. **10–20 min — Review and compare.** Explain one architectural decision, a rejected alternative and a verification/test case.

**Participant output:** A short requirement-to-component traceability table, one architecture sketch and a documented trade-off. No prior download or registration is required.

### 2. Payment lifecycle and reconciliation (45–60 minutes)

**Audience:** fintech engineers, payment architects and technically oriented analysts.

**Resources:** [Card acquiring/authorization](payments/acquiring-processing.md), [Clearing, Settlement & Reconciliation](payments/clearing-settlement-reconciliation.md), [worked reconciliation example](payments/reconciliation-worked-example.md), [PlantUML sources](payments/diagrams.md).

**Workshop outline:**

1. Identify who owns the commercial order, authorization, capture, clearing record, financial ledger and merchant payout.
2. Draw the sequence from card authorization to merchant funding and mark the financial-finality boundaries.
3. Review a synthetic reconciliation break; determine which source is authoritative and how to investigate it.
4. Discuss why a gateway timeout cannot automatically be interpreted as a payment decline.

**Participant output:** A sequence diagram, state ownership table and one reconciliation investigation checklist.

### 3. Event-driven reliability and recovery (45–60 minutes)

**Audience:** integration engineers, solution architects, and platform teams.

**Resources:** [Kafka event-driven processing](payments/event-driven-processing.md), [Kafka offset/crash recovery](payments/kafka-offset-recovery.md), [event contracts](payments/event-driven-contracts.md).

**Workshop outline:**

1. Trace a payment-related event through an outbox, broker, inbox and worker.
2. Simulate a consumer restart after business processing but before offset commit.
3. Identify where duplicate delivery may occur, and where idempotency must be enforced.
4. Specify one operational alert and a DLQ redrive policy that does not duplicate a financial side effect.

**Participant output:** Annotated event sequence, duplicate-protection invariant and recovery acceptance tests.

## How to use or adapt these materials

- **Study:** Read examples online, inspect diagrams and compare alternative designs.
- **Teach:** Use a topic as a classroom exercise, training session or reading assignment.
- **Adapt:** Download and edit DOCX, RTF, XLSX, Draw.io, BPMN or PlantUML public editions where available.
- **Attribute:** Credit **Sergei Budnik**, link the original resource and [CC BY 4.0](license.md), and indicate changes.
- **Check your boundaries:** Remove employer/client information and any personally identifiable data before sharing an adaptation. Validate real-world security, compliance and provider requirements independently.

**Suggested attribution:** "Adapted from Architecture & Analysis Hub by Sergei Budnik, licensed CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/). Changes: [brief description]."

The public CC BY licence covers **author-owned public editions** as described on the [license page](license.md). It does not grant rights to confidential source files, third-party materials or trademarks.

## Want to review, reuse or co-develop a learning exercise?

1. [Propose a documentation improvement](https://github.com/SergeiBudnik/architecture-analysis-hub/issues/new/choose) — tell us which page and what to improve.
2. [Share a genuine use of a resource](https://github.com/SergeiBudnik/architecture-analysis-hub/issues/new/choose) — optional, only if you are comfortable describing your experience publicly.
3. [See the community adoption log](community-adoption.md) — records are added **only after verification and permission**.
4. [Read the contribution guidance](contribute.md) — GitHub contributions are welcome; no endorsement or testimonial is required.

You can use the library without reporting anything. **We do not publish usage claims, participation counts or endorsements that have not been independently verified.**

## Educational collaboration

For an informal online walkthrough or to suggest a practice-oriented workshop, please open a [community discussion issue](https://github.com/SergeiBudnik/architecture-analysis-hub/issues/new/choose). No membership, fee or certification is implied by this invitation.

[About the author](about-the-author.md) · [Publication QA](quality-assurance.md).
