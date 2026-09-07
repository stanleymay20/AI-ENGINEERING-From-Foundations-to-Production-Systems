# Commercial Release Gate

## Current status

**Technical interior:** PASS  
**Dataset/reproducibility:** PASS  
**Commercial release:** HOLD pending ISBN/imprint/cover/proof decisions

## Verified production outputs prepared from v2.4

- 394-page, exact 6 x 9 in print interior master
- KDP-specific pre-ISBN interior candidate with bookmarks, annotations/links, and metadata removed while preserving the rendered pages exactly
- IngramSpark pre-ISBN PDF/X-1a:2001 grayscale interior candidate
- EPUB 3 pre-ISBN candidate with native navigation, MathML, six semantic tables, all instructional images, and the permanent companion-repository link

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

## Remaining launch decisions

1. **ISBN ownership and assignment**
   - choose own ISBN versus platform-provided ISBN
   - if own ISBN, fix publisher/imprint and ISBN agency jurisdiction

2. **Publisher/imprint wording**
   - must match the ISBN registration and all retailer metadata

3. **Paperback paper choice**
   - recommended launch default: black-and-white interior, white paper, matte cover
   - page count: 394

4. **Final cover wrap**
   - generate from the retailer's exact template after ISBN, paper, binding, and page count are locked
   - include back-cover copy and barcode-safe area

5. **Retail metadata and pricing**
   - final description, subjects/categories, keywords, author bio, territories, publication date, list price

6. **Physical proof**
   - order and inspect at least one proof before enabling broad distribution

## Release rule

Do not call the edition commercially released until the final ISBN/imprint metadata, cover wrap, EPUBCheck result, retailer preview/preflight, and physical proof have all passed.
