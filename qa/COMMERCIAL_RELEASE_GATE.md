# Commercial Release Gate

## Current status

**Technical interior:** PASS  
**Dataset/reproducibility:** PASS  
**Working imprint:** ScrollLibrary Press  
**ISBN strategy:** own German publisher range; 1,000-number allocation recommended  
**Commercial release:** HOLD pending ISBN purchase/assignment, final covers, retailer preflight, and physical proof

## Verified production outputs prepared from v2.4

- 394-page, exact 6 x 9 in print interior master
- KDP-specific pre-ISBN interior candidate with bookmarks, annotations/links, and metadata removed while preserving the rendered pages exactly
- IngramSpark pre-ISBN PDF/X-1a:2001 grayscale interior candidate
- EPUB 3 pre-ISBN candidate with native navigation, MathML, six semantic tables, all instructional images, and the permanent companion-repository link

## Imprint decision

**ScrollLibrary Press** is the recommended working publishing imprint for this title and future ScrollLibrary publishing activity.

A preliminary broad web search did not surface an obvious exact-match publisher/trademark for the name. This is not legal/trademark clearance. Formal DPMA/EUIPO clearance remains an owner/legal task before relying on the name as a registered mark or legal company identity.

See `publishing/SCROLLLIBRARY_PRESS_IMPRINT_ARCHITECTURE.md`.

## ISBN decision

Use publisher-owned ISBNs rather than a platform-issued free ISBN.

The German ISBN Agency currently displays a 1,000-number allocation at **€400 + VAT** (price page marked Stand 01.08.2022; verify at live checkout). Given the intended ScrollLibrary Press publishing scope, the 1,000-number range is the recommended infrastructure choice.

The first three format-specific allocations for this book will be:

1. paperback
2. hardcover
3. EPUB

Actual ISBNs remain **PENDING OWNER PURCHASE / MVB ASSIGNMENT**.

See `publishing/ISBN_1000_REGISTRATION_PACK.md`.

## Pricing direction

Working German launch prices, subject to live KDP/Ingram economics and proof approval:

- paperback: **€44.99**
- hardcover: **€64.99**
- EPUB/Kindle: **€12.99**

See `publishing/PRICING_AND_FORMAT_STRATEGY.md`.

## KDP production note

The archival/publication master intentionally retains useful PDF metadata and navigation. The KDP upload candidate is a separate derivative because KDP's print submission guidance warns against bookmarks, annotations, and metadata in uploaded print PDFs.

## IngramSpark production note

The IngramSpark candidate is generated separately as a PDF/X-1a:2001 grayscale print interior. Final submission should still be checked in IngramSpark's own preflight after the ISBN and final cover template are fixed.

## EPUB production note

The EPUB candidate is reflowable rather than a PDF conversion. The print-only static table of contents is removed, EPUB navigation is generated natively, formulas are emitted as MathML, and the companion GitHub repository is included in the front matter.

A local structural preflight verified:

- valid EPUB ZIP/mimetype packaging
- parseable XML/XHTML package content
- no missing local href/src targets
- 48 XHTML content documents
- 27 images including cover
- 891 MathML elements
- six semantic tables
- companion repository link present
- print-only static TOC absent

Final commercial EPUB release remains pending official EPUBCheck validation after the identifier/publisher metadata are finalized.

## Remaining launch blockers

1. **Owner purchase of 1,000 ISBN allocation**
   - register final publisher/legal details with the German ISBN Agency
   - provide issued publisher range/prefix to production

2. **Formal imprint/name clearance**
   - DPMA/EUIPO or appropriate professional clearance if the name will be registered/protected

3. **Assign three ISBNs**
   - paperback
   - hardcover
   - EPUB

4. **Propagate identifiers**
   - metadata master
   - copyright page
   - EPUB package metadata
   - retailer records
   - VLB record
   - release manifest

5. **Final paperback and hardcover wraps**
   - generate from each retailer's exact template
   - include final spine/back copy and barcode-safe area

6. **Retail metadata/pricing**
   - approve author bio
   - confirm publication date and territories
   - run live KDP/Ingram price economics
   - publish compliant German fixed prices

7. **Final validation**
   - official EPUBCheck
   - KDP Print Previewer
   - IngramSpark preflight

8. **Physical proof**
   - inspect code size, gutter, binding, grayscale figures, tables, equations, headers/folios, cover alignment, spine, and barcode

## Release rule

Do not call the edition commercially released until final ISBN/imprint metadata, cover wraps, EPUBCheck, retailer preview/preflight, and physical proof have all passed.