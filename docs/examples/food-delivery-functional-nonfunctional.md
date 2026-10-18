---
title: Complete FR/NFR Example — Food Delivery
sidebar_position: 19
---

# Food Delivery Marketplace: Functional and Non-Functional Requirements

**Source:** `FT_NFT_EXAMPLE.docx`, **Example_2**, STORAGE v1.0.0 (2025-09-04). Its eleven logical source groups are preserved below: **A–I and K** (the original uses K after I; no J section exists). Requirements and numeric values are **sample targets**, not measured production outcomes.

## A. Catalog and Search

| ID | Source requirement |
|---|---|
| FR-CAT-01 | List restaurant name, delivery time, featured dishes, rating and current promotions |
| FR-CAT-02 | Search restaurant by name |
| FR-CAT-03 | Filter by cuisine, rating, time and price |
| FR-CAT-04 | Sort by delivery time, rating, relevance or promotion |
| FR-CAT-05 | Pagination or infinite-scroll / lazy loading |

## B. Menu and Dish Details

| ID | Source requirement |
|---|---|
| FR-MENU-01 | Show name, price, weight, calories and photo |
| FR-ITEM-01 | Dish details include description, macronutrients, calories and price |
| FR-ITEM-02 | Ingredients and allergens where available |
| FR-ITEM-03 | Dish variants, spice level, sauce and other modifiers |
| FR-ITEM-04 | Availability and related item recommendations |

## C. Basket and Pricing

| ID | Source requirement |
|---|---|
| FR-CART-01 / 02 | Add from menu or from dish page with selected quantity |
| FR-CART-03 | Basket lines, weight, unit price, delivery cost/time and total |
| FR-CART-04 / 05 | Increase/decrease quantity and remove items |
| FR-CART-06 | Promo code and amount recalculation |
| FR-CART-07 | Preset and custom tips |
| FR-CART-08 | Minimum order / area coverage, delivery address, ASAP or slot selection |

## D. Checkout and Payments

| ID | Source example requirement |
|---|---|
| FR-PAY-01 | Card online, cash to courier, card to courier (mPOS) |
| FR-PAY-02 | SCA/3-D Secure for online cards; status via webhooks |
| FR-PAY-03 | Confirm order and issue electronic receipt |
| FR-PAY-04 | Cancel before Preparing; issue partial/full refund |
| FR-PAY-05 | Optional card-on-file **tokenized by processor** |
| NFR-PAY-01 | Example target: PCI DSS SAQ-A scope, TLS 1.2+, signed provider callback |
| NFR-PAY-02 | Example p95 payment initiation ≤ **600 ms**, webhook confirmation ≤ **3 sec** |
| NFR-PAY-03 | Payment availability **99.95%**; API/DB idempotency; logs ≥ **6 years** |

**Source-quality warning:** SAQ-A eligibility depends on the actual integration and PCI responsibilities; it cannot be guaranteed by stating a requirement. Financial data retention also depends on applicable laws/contracts.

## E–G. Support, Tracking and Notifications

| Area | Source requirements |
|---|---|
| Chat FR-SUP-01/02 | Online/offline support, reply alerts, virus-scanned attachments |
| NFR-SUP-AVAIL-01 | **99.9% monthly** chat availability |
| NFR-SUP-RET-01 | Chat 12-month online and 24-month archive history; deletion example ≤ 30 days |
| NFR-SUP-FILE-01 | Up to 25 MB/file, 100 MB/conversation |
| FR-TRK-01 | Live courier position/ETA on a map |
| NFR-TRACK-01 | Courier position updates at least once per **15 sec**; GPS smoothing |
| FR-NOTIF-01 | Push, SMS or email on key order state changes |
| NFR-NOTIF-01 | Delivery according to platform monitoring/queue SLO |

## H. Authentication, Addresses and Coverage

| ID | Source requirement |
|---|---|
| FR-AUTH-01/02 | Email/password or phone OTP signup/login; optional Apple/Google login |
| FR-AUTH-03–05 | Password reset, optional MFA, sign out all devices |
| FR-ADDR-01–04 | Address CRUD/default, geocoding, coverage and saved locations |
| NFR-AUTH-01 | bcrypt/argon2, JWT/session rotation and rate limits |
| NFR-AUTH-02 | p95 login ≤ **500 ms**, address ops ≤ **300 ms** |
| NFR-ADDR-01 | Manual address entry if geocoder unavailable |

## I. Ratings, ETA and Order Status

| ID | Source requirement |
|---|---|
| FR-RATE-01–03 | 1–5 ratings, one review per order, moderation, official replies, aggregation |
| FR-ETA-01 | ETA displayed in restaurant card and basket; dynamic recalculation |
| FR-STAT-01 | Order: NEW → CONFIRMED → PREPARING → READY_FOR_PICKUP → PICKED_UP → (NEARBY) → DELIVERED |
| FR-STAT-02 | Reassign courier or pause restaurant with ETA/notification updates |
| NFR-RATE-01 | Review cannot publish until ≥ 15 min post-delivery; abuse controls |
| NFR-RATE-02 | p95 publish/aggregate ≤ **300 ms**; eventual consistency ≤ **1 min** |
| NFR-ETA-01 | ETA MAE ≤ **6 min** for distance ≤ 5 km; recalc at least every **30 sec** |
| NFR-STAT-01 | Immutable, attributable history of status transitions |

Source exception statuses include CANCELLED_USER, CANCELLED_RESTAURANT, FAILED_PAYMENT and REFUNDED. These are example order/payment outcomes, not a single universal transition chain.

## K. Shared Platform NFRs

| ID | Source target |
|---|---|
| NFR-PLAT-01/02 | iOS/Android + responsive web; RU and EN |
| NFR-PLAT-03/04 | HTTPS/TLS 1.2+, distinct User/Courier RBAC |
| NFR-PERF-01 | **1 million active users/day**, **10,000 RPS** sustained and **20,000 RPS** burst as example assumptions |
| NFR-SLO-01 | Core API **99.9% monthly**, p95 catalog 200 ms, cart 300 ms, order 400 ms, 5xx ≤ 0.2% |
| NFR-A11Y-01 | WCAG 2.2 AA |
| NFR-OBS-01 | Latency/errors, webhook delivery, ETA accuracy and queue metrics |
| NFR-DR-01 | RPO ≤ **5 min**, RTO ≤ **30 min**, quarterly drills |
| NFR-SEC-01 | Mask PII; 90-day online logs plus ≥ 365-day archive |

## Architectural interpretation (added)

These numeric expectations are **not mutually validated** by the source. Before using them in a real solution, a team must establish concurrent-active load, request mix, seasonal peaks, payment-provider boundaries, cost, actual data retention duties and verification methods.

For a filled functional SRS see [Food Delivery SRS](food-delivery-srs.md). For the source's first support-console example see [Support Console FR/NFR](support-console-fr-nfr.md). For an editable sheet use the [Source Downloads](source-examples-downloads.md).

**License:** [CC BY 4.0](../license.md).
