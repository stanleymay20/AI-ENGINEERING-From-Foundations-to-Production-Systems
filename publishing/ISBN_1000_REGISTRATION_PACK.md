# ScrollLibrary Press — 1,000 ISBN Registration Pack

**Prepared:** 7 September 2026  
**Jurisdiction:** Germany  
**Recommended agency:** German ISBN Agency / MVB GmbH  
**Working publisher/imprint:** ScrollLibrary Press

## Recommendation

Purchase the **1,000-ISBN publisher block** if ScrollLibrary Press is intended to become a genuine multi-title publishing operation.

The German ISBN Agency currently displays these package prices:

| Package | Displayed price, excl. VAT |
|---|---:|
| 1 ISBN | €70 |
| 10 ISBNs | €225 |
| 100 ISBNs | €300 |
| **1,000 ISBNs** | **€400** |

Source: https://german-isbn.de/isbn/preise-und-pakete

The page still labels the tariff as **Stand 01.08.2022**, so the exact amount must be confirmed in the live checkout before payment.

### Why 1,000 makes sense here

The incremental displayed cost from 100 to 1,000 numbers is only **€100 + VAT**. If ScrollLibrary Press is expected to publish multiple formats, revised editions, translations, new titles, and eventually third-party authors under publishing agreements, the larger allocation avoids repeatedly exhausting small ranges.

This should be viewed as **publisher infrastructure**, not as 1,000 ISBNs for a single book.

## Important legal/operational restriction

German ISBN guidance states that the ISBN belongs to the purchaser, may not be sold or given away, and may only be used for products for which the declared rights holder has the relevant author and/or publishing rights.

Therefore:

- do not resell individual ISBNs to unrelated self-publishing authors;
- do not let another publisher use the ScrollLibrary Press range as its own;
- do assign ISBNs to titles ScrollLibrary Press actually publishes under appropriate rights agreements;
- maintain a permanent internal allocation ledger.

Official guidance: https://german-isbn.de/isbn/isbn-leitlinien

## Information the owner will need for the MVB purchase

The purchasing step requires account/legal details that must be supplied by the publisher owner. Prepare:

- publisher / rights-holder legal name;
- intended publisher/imprint name: **ScrollLibrary Press**;
- business or publisher postal address;
- country: Germany;
- contact person;
- telephone number;
- email address;
- billing details;
- tax/VAT details if applicable;
- payment method.

Do not place private address, tax, or payment data in this public GitHub repository.

## Initial ISBN allocation policy for this book

Do not assign actual numbers until MVB has issued the range.

| Internal slot | Product | Format | Status |
|---|---|---|---|
| AIENG-2026-PB | AI Engineering: From Foundations to Production Systems | 6×9 paperback | Reserve first appropriate ISBN |
| AIENG-2026-HC | AI Engineering: From Foundations to Production Systems | 6×9 hardcover | Reserve separate ISBN |
| AIENG-2026-EPUB | AI Engineering: From Foundations to Production Systems | EPUB 3 | Reserve separate ISBN |

A Kindle edition can technically publish without an ISBN, but the EPUB edition should have its own ISBN for consistent publisher-controlled metadata and wider distribution.

## Future allocation categories

A 1,000-number range should accommodate:

- new ScrollLibrary Press titles;
- paperback/hardcover/ebook variants;
- materially revised editions;
- translations;
- course/study editions that qualify as distinct editions;
- third-party authors published under ScrollLibrary Press agreements.

A new ISBN is required for each edition/format where ISBN rules require a distinct identifier. Never recycle an assigned ISBN.

## Allocation ledger schema

Maintain a private publisher ledger with these fields:

```text
isbn
internal_product_id
title
subtitle
author
contributor
format
language
edition
publication_date
imprint
rights_holder
territory
status
assigned_date
vlb_status
kdp_status
ingram_status
ebook_distribution_status
notes
```

The ISBN number itself and public book metadata can be public after assignment. Private publisher/account data should remain outside Git.

## VLB recommendation

After ISBN assignment, evaluate participation in the **Verzeichnis Lieferbarer Bücher (VLB)** so the title can be discoverable in German-language book-trade systems. The German ISBN Agency describes VLB as the central metadata platform feeding bookstores and other recipients.

Source: https://german-isbn.de/fuer-einsteiger/der-weg-zum-buchhandel/verzeichnis-lieferbarer-b%C3%BCcher-vlb

## Owner action required

1. Open the official German ISBN Agency shop: https://german-isbn.de/
2. Select the **1,000 ISBN** allocation.
3. Register the publisher using the final legal/publisher details.
4. Confirm the displayed price and VAT before purchase.
5. Complete payment personally.
6. Provide the assigned ISBN range/prefix back to the production workflow.

Once the range is issued, the production system can assign the first three ISBNs, update print/EPUB metadata, generate final barcode-ready covers, and move the project toward proof approval.