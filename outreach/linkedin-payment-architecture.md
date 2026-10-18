# LinkedIn post — Payment Architecture

**Status:** Draft, **not published**. First-person copy for Sergei Budnik.

An approved card payment is not the same as a settled payment.

And a timeout is not proof that a transaction failed.

When designing payment systems, those two distinctions affect almost everything: state ownership, retries, merchant notifications, ledger posting and reconciliation.

I’ve published an open, provider-neutral architecture walkthrough covering:

• Authorization and capture — what has actually been approved?  
• Presentment, clearing and settlement — when do financial obligations move?  
• Merchant payout versus scheme settlement — why are they different?  
• Reconciliation breaks — how should discrepancies be investigated?  
• Unknown outcomes — why should a retry never blindly create a second payment?

The reference includes a worked synthetic transaction, architecture decisions and editable PlantUML diagrams.

Read and reuse it here:  
https://sergeibudnik.github.io/architecture-analysis-hub/docs/payments/clearing-settlement-reconciliation

All examples are educational, fictional and not tied to any confidential client implementation.

I’d be interested to hear from other payment engineers and architects: **Which payment lifecycle boundary is most often misunderstood in your projects?**

#Payments #SolutionArchitecture #FinTech
