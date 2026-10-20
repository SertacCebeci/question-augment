---
description: "A document-QA system can return a bounding box by aligning its answer string to OCR segments; the box survives losing generative answering only where the answer is an exact span."
aliases: ["answer localization", "text-to-region alignment", "post-hoc answer grounding", "answer bounding box"]
sources: ["arxiv-2511-18192"]
---
# Answer span localization

A document question-answering system can return an answer together with the region of the page it came from. In one agentic pipeline this is a separate tool step that runs after the answer exists: "After QA generates answer A, the agent invokes GroundAnswer(A) to localize the answer."[^a1] The page is first read by OCR into text segments, each with a box. The box is then taken from the segment the answer matches: "For exact matches to OCR segment" the paper uses that segment's box, merges the boxes of multi-segment answers into one region, and for computed answers "the module highlights supporting evidence."[^a2] Where an answer string occurs more than once, "Ambiguous answers are disambiguated using contextual cues from retrieved segments and" the question keywords.[^a3]

So the location is not predicted from the image as a second output. It is a function of where the answer string sits in the OCR output. Two consequences follow from that design. Both are my reading of the design; the paper reports only the numbers below.

First, the box is capped by the OCR. The authors name the dependence: "reliance on OCR quality means that documents with severe noise, degradation," can produce unreliable results.[^a4]

Second, localization and generation are separable in the measurements. Removing generative QA, and keeping only exact string matches from the retrieved segments, cost text accuracy but not much localization: the paper reports that this variant "degrades ANLS by -1.7 on DocVQA and -1.0 on FUNSD, while maintaining comparable mAP" (the mAP drops are -0.1 and -0.8).[^a5] The authors explain the retained localization by the design: "exact-match answers still align to correct bounding boxes when they exist in the document."[^a6] Read as a mechanism, the box follows the span. When the answer is a copied span, generation adds text accuracy and little else to the box. A paraphrased or summed answer has no single segment to point to, so for that kind of answer the box is weaker or absent. The paper does not count how many gold answers were exact spans, so the size of this effect on the full benchmark is not known.

Retrieval also feeds the box. Passing the whole OCR text to the answerer, with no retrieval step, "causes -2.5 ANLS and -1.6 mAP" on DocVQA.[^a7] The span that the box is built from is chosen before it is located, so a retrieval miss is also a localization miss.

Measurement uses two axes. Text accuracy is ANLS; spatial precision is "spatial precision (mAP@IoU 0.50:0.95)".[^a8] Reported on the four benchmarks, the system reaches 50.1 mAP on DocVQA, 50.3 on FUNSD and 60.2 on CORD.[^a9] A box that the answer is read from is judged by overlap with a gold region, not by whether the answer string is right, which is what lets the two axes come apart.

## Limits

- Localization is compared with one other system. The paper says "as other baselines do not predict bounding boxes," so the comparison is with DLaVA alone.[^a10]
- Explicit OCR text does not uniformly help localization. DLaVA's OCR-dependent mode scored below its OCR-free mode on spatial grounding, and the authors offer a guess: "suggesting that integrating explicit OCR text may introduce noise or" confusion in its spatial head. The guess is not tested here.[^a11]
- The ablation covers DocVQA and FUNSD only. The no-generation result is not reported for CORD or SROIE in the passages read.
- The IoU score measures overlap with a gold box. It does not show that the box is the region a reader would point to for an answer that has no single source segment; that gap is my inference from the design.
- Cost: the tool chain is sequential and the latency is "approximately 3.2 s/query on DocVQA," against 0.4 s for DocLayLLM.[^a12] The box adds one step to that chain.
- The fallback "No answer found" is given "to avoid unsupported responses" when no segment is retrieved.[^a13] The paper does not report localization for those cases, so whether a refused answer has a box is not known.

## Related

- [[conjunctive-answer-grounding-credit]] — scores whether an answer is localized as well as correct; this note is about how a system produces the box, the scoring question is that note's.
- [[grounding-answer-dual-axis-audit]] — crosses localization success with answer correctness; a span-derived box is the localization axis such an audit would read.
- [[ocr-answer-token-coverage]] — a span-selecting answerer can return only what OCR recovered, and the same OCR bounds the box here.
- [[traceable-evidence-chain]] — ties an answer to a retrieved source as a record; this ties it to a region of the page.
- [[visual-evidence-scoring]] — predicts localization as a confidence signal for a selector, rather than producing the box.

[^a1]: arxiv-2511-18192 — "After QA generates answer A, the agent invokes GroundAnswer(A) to localize the answer."
[^a2]: arxiv-2511-18192 — "For computed answers, the module highlights supporting evidence."
[^a3]: arxiv-2511-18192 — "Ambiguous answers are disambiguated using contextual cues from retrieved segments and"
[^a4]: arxiv-2511-18192 — "reliance on OCR quality means that documents with severe noise, degradation,"
[^a5]: arxiv-2511-18192 — "degrades ANLS by -1.7 on DocVQA and -1.0 on FUNSD, while maintaining comparable mAP"
[^a6]: arxiv-2511-18192 — "exact-match answers still align to correct bounding boxes when they exist in the document"
[^a7]: arxiv-2511-18192 — "Feeding entire OCR text directly to the QA module causes -2.5 ANLS and -1.6 mAP"
[^a8]: arxiv-2511-18192 — "spatial precision (mAP@IoU 0.50:0.95)"
[^a9]: arxiv-2511-18192 — "ARIAL achieves 50.1 mAP@IoU on DocVQA, 50.3 on FUNSD, and 60.2 on CORD"
[^a10]: arxiv-2511-18192 — "as other baselines do not predict bounding boxes"
[^a11]: arxiv-2511-18192 — "suggesting that integrating explicit OCR text may introduce noise or"
[^a12]: arxiv-2511-18192 — "ARIAL incurs higher latency (approximately 3.2 s/query on DocVQA)"
[^a13]: arxiv-2511-18192 — "to avoid unsupported responses."
