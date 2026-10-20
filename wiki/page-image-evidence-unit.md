---
description: "Retrieval can index each rendered guideline page as one image, with no OCR or text chunking, so tables and flowcharts stay intact; the work argues this but never tests it against text."
aliases: ["page-level visual retrieval", "visual document retrieval", "page image as evidence unit", "visual page retriever"]
sources: ["doi-10-1145-3811238-3811871", "arxiv-2512-16802", "arxiv-2511-22850", "arxiv-2511-16654"]
---
# Page-image evidence unit

In this design the atomic unit of evidence is a whole page, kept as an image. The authors treat "each individual guideline page image resulting from a pdf-to-image conversion" as "as our atomic evidence unit for retrieval and citation", so one object serves as the chunk, the retrieval key and the thing the reader is shown.[^c1]

The pipeline does almost nothing to the pages before indexing. The 305 guideline PDFs were rendered at 720 DPI, rescaled and centre-padded to one 5390×7940 canvas, and not cleaned further. The authors state that "We intentionally did not do any text extraction or structure parsing", and the page is never OCR'd.[^c2] The motive is stated in one sentence: "We directly retrieve page images instead of text, which avoids OCR errors and keeps" structures such as tables and flowcharts.[^c9]

The encoder is ColQwen2.5, which maps page images and text queries into one shared space. Its sequence outputs are "by mean pooling over the sequence" to one fixed-length vector per page or query.[^c4] The index is an exact FAISS flat index, and the paper uses "the raw L2 distance as the retrieval score", without normalising the vectors.[^c3]

The argument against chunking is that text segmentation can break up the evidence itself: "Our page-level visual indexing approach eliminates the need for standard text" segmentation, which may split clinically relevant information in paragraphs.[^c5]

What survives the transfer to other retrieval settings is the choice of the page as the unit of both matching and citation. A question is then matched against what an encoder can read off a rendered layout, not against a paragraph. Whatever the match depends on (a table's header, a branch in a flowchart) is carried by the image and not by any extracted text. This is my reading of the design, not something the paper measures.

A later comparison supplies the text baseline this note lacks. On a 120-question glycobiology benchmark, page-image retrieval with ColPali is set against text chunks and against multi-modal conversion, and the ranking depends on the generator: with Gemma-3-27B-IT, text and conversion beat the page-image route, while with GPT-4o the spread between the three narrows to about six points.[^c10][^c11] That comparison measures answer accuracy, not the OCR errors and lost tables the page unit is meant to avoid, so the motive stated above is still untested. See [[capacity-dependent-evidence-modality]].

A second text comparison comes from SLEUTH, which runs clue agents on two evidence sets at once: the top-5 page images from ColPali, and the top-5 text pages from MinerU and BGE M3, merged before answering. Using only the visual pages scored higher on both benchmarks, by "+2.58% and +2.34% points," and the authors read the result as pages that "serve as a highly compressed and structure-preserving" representation.[^c12][^c13] The same text notes narrow cases where the text side helps, "mainly when exact textual normalization is required (e.g., strict digit"[^c14] This is one architecture with merged evidence sets, so it compares the two inputs only inside that pipeline. See [[evidence-dense-context-distillation]].

## Limits

- No text-chunk baseline. The paper never runs the same corpus through OCR or chunked-text retrieval. Its advantages over text (no OCR errors, kept tables) follow from the design and are not measured. The ablations remove reranking, query rewriting and routing, not the page unit (my reading of Tables 5 and 6).
- The end-to-end scores belong to the whole pipeline, with reranking, rewriting, routing and a GPT-based filter. They cannot be credited to the page unit.
- The authors say the raw L2 score "makes the retrieval-confidence threshold easier to calibrate during" inference.[^c6] No calibration experiment appears in the work.
- Cross-page evidence is not addressed. A rule split over two pages is retrieved as two independent units, and the paper does not test whether the answer recovers the rule. This is my inference from the one-page-one-unit design.
- The downscaling from 5908×8063 pixels to a 5390×7940 canvas is not tested for small table text. Whether the encoder reads fine print at this resolution is unreported.
- The corpus is 305 guidelines from one platform: "we got PDFs of ophthalmology-related guidelines from the Medlive (Yimaitong)".[^c7] The authors also name the coverage limit: "the guideline corpus, which is inherently incomplete and may not capture recent updates".[^c8]

## Related

- retrieval-routing-with-evidence-fallback — the page units are what the router sends to retrieval and what the filter keeps or drops
- [[reranker-as-relevance-judge]] — the page filter is an LLM relevance judgment over candidate pages, with the same family-bias risk that note describes
- [[capacity-dependent-evidence-modality]] — the text-baseline comparison this note lacks; the page-image route becomes competitive only with a stronger generator
- [[image-summary-index-loss]] — a slide-as-image index against a summary-text index on 40 earnings-call questions: the image arm ranks higher on mAP@5 and nDCG@5, a measured text baseline for a slide unit, though not for the OCR-and-chunk route this note's motive names

[^c1]: doi-10-1145-3811238-3811871 — "as our atomic evidence unit for retrieval and citation"
[^c2]: doi-10-1145-3811238-3811871 — "We intentionally did not do any text extraction or structure parsing"
[^c3]: doi-10-1145-3811238-3811871 — "use the raw L2 distance as the retrieval score"
[^c4]: doi-10-1145-3811238-3811871 — "by mean pooling over the sequence"
[^c5]: doi-10-1145-3811238-3811871 — "Our page-level visual indexing approach eliminates the need for standard text"
[^c6]: doi-10-1145-3811238-3811871 — "makes the retrieval-confidence threshold easier to calibrate during"
[^c7]: doi-10-1145-3811238-3811871 — "we got PDFs of ophthalmology-related guidelines from the Medlive (Yimaitong)"
[^c8]: doi-10-1145-3811238-3811871 — "the guideline corpus, which is inherently incomplete and may not capture recent updates"
[^c9]: doi-10-1145-3811238-3811871 — "We directly retrieve page images instead of text, which avoids OCR errors and keeps"
[^c10]: arxiv-2512-16802 — "Text and Multi-modal augmentation outperformed OCR-free"
[^c11]: arxiv-2512-16802 — "within-model differences were small"
[^c12]: arxiv-2511-22850 — "setting by +2.58% and +2.34% points, respectively."
[^c13]: arxiv-2511-22850 — "serve as a highly compressed and structure-preserving"
[^c14]: arxiv-2511-22850 — "mainly when exact textual normalization is required (e.g., strict digit"
