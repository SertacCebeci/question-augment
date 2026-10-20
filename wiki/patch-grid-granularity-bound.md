---
description: "A late-interaction retriever's patch grid caps how small an evidence region it can localize: small boxes lose efficiency to grid quantization, so the grain returned is set by the localizer too."
aliases: ["patch quantization bound", "grid-quantized region localization", "patch-to-region relevance propagation", "area efficiency bound"]
sources: ["arxiv-2512-02660"]
---
# Patch-grid granularity bound

A page-level retriever that scores a query against a grid of image patches already holds a spatial signal it usually throws away. In ColPali-style late interaction, the model "sums the maximum similarity between each query token and all document patches" to produce one page score.[^c1] Keeping the per-patch maximum instead gives a heatmap: "This captures the maximum relevance of patch j to any query token, forming a spatial heatmap over the page."[^c2] The paper's point is that this signal is "computed but discarded when returning page-level results."[^c3] The retrieval system "knows which page contains the answer but not where on the page."[^c4]

When the page is also split into OCR text regions with bounding boxes, each region can take a score as the IoU-weighted average of the patches it overlaps. The paper says its approach "operates at inference time without additional training."[^c5] On BBox-DocVQA, given a page that holds the answer, ColQwen3-4B with a median threshold reaches a 59.7% hit rate at IoU ≥ 0.5, against about 6.7% for random region selection.[^c6][^c7]

## The bound: the grid sets the grain

The grid is the first limit on grain. Each patch is an s × s pixel cell (s = 14 pixels for a 448 × 448 input and a 32 × 32 grid).[^c8] A region of width w and height h is covered by whole patches, so only part of the covered area is target. The paper's Theorem 1 bounds the efficiency, the ratio of target area to covered patch area, by wh / ((w + s)(h + s)), the worst case over all alignments of the box with the grid. For ColPali at s = 14, the paper's Corollary 1 gives a paragraph of 200 × 50 pixels at most 73% efficiency, a table cell of 100 × 30 at most 60%, and a label of 50 × 20 at most 46%.[^c9] The stated consequence is that "smaller regions suffer disproportionately from patch quantization."[^c10]

The same limit appears in the experiments. The authors call one of their two regimes "a precision-bound regime where patch quantization limits dominate regardless of model capacity."[^c11] Consistent with that, scaling inside one architecture saturates: ColQwen3-8B "yields negligible gains" over ColQwen3-4B (59.8% against 59.7% at IoU@0.5), while a 250M model reaches 45.5%.[^c12] The paper's per-category table is read the same way: mathematics and economics are lowest, "likely due to denser tabular content and smaller region sizes where patch quantization effects are more pronounced."[^c13]

Two things follow from the bound. The first is that the grain a system can return is set by its localizer's cell size, whatever grain the question needs. The second is my inference: a question whose evidence is a label or a table cell is then served at the grid's resolution, so the failure shows up as lost precision on small evidence rather than as a retrieval miss. The paper does not measure that failure directly; its hit rates are overall figures per category.

## Limits

- The hit rate is conditional. The question the paper answers is: "Given a page containing the answer, can our approach identify the specific region?"[^c14] Page-level retrieval accuracy (Stage 1) "is outside our scope."[^c15] Nothing here says how often the right page is found in the first place.
- The regions are not free. They come from one OCR system, chosen "for its layout-aware region segmentation that groups semantically coherent blocks."[^c16] A different segmentation changes the boxes that are scored, so the hit rate depends on the OCR as well as the grid.
- The aggregation choice matters. The paper says "The choice of aggregation strategy affects retrieval quality depending on region size and content density."[^c17] The IoU-weighted default is argued for on principle, and the sections read do not compare it with max or mean aggregation on the same benchmark.
- The bound is a worst case over box alignments. The values quoted for 200 × 50, 100 × 30 and 50 × 20 boxes are bound values, not measured efficiencies for those boxes; the paper does not report measured efficiency at this level of detail in the sections read.
- One benchmark, one resolution and one OCR configuration. The grid size is fixed by the model at 448 pixels. A higher-resolution grid would change s, and the paper only suggests this ("may benefit from higher-resolution patch grids"), without testing it.
- The concept is machine retrieval for a machine answerer. Nothing here tests a human asker or answerer, or a question whose grain is chosen by a human.

## Related

- [[query-adaptive-evidence-granularity]] — the grain a question needs can be chosen per query by a planner; this note adds the other side, that the grain a localizer can return is capped by its grid whatever the question needs.
- [[two-stage-reranking]] — the same cheap-then-costly shape: a pooled first stage picks candidate pages, and the costly per-patch scoring runs only on that short list.
- [[coarse-to-fine-evidence-zoom]] — zooming re-inspects a span at finer resolution. My inference is that a single fixed grid offers no finer level to zoom into, which is the limit stated above.

[^c1]: arxiv-2512-02660 — "a MaxSim operation that sums the maximum similarity between each query token and all document patches"
[^c2]: arxiv-2512-02660 — "This captures the maximum relevance of patch j to any query token, forming a spatial heatmap over the page."
[^c3]: arxiv-2512-02660 — "This information is computed but discarded when returning page-level results."
[^c4]: arxiv-2512-02660 — "The retrieval system knows which page contains the answer but not where on the page."
[^c5]: arxiv-2512-02660 — "Our approach operates at inference time without additional training."
[^c6]: arxiv-2512-02660 — "ColQwen3-4B with percentile50 thresholding achieves 59.7% hit rate at IoU@0.5"
[^c7]: arxiv-2512-02660 — "for random region selection"
[^c8]: arxiv-2512-02660 — "Each patch corresponds to an s × s pixel region where s = I/G = 14 pixels."
[^c9]: arxiv-2512-02660 — "A table cell (100 × 30 pixels): efficiency ≤ 60%"
[^c10]: arxiv-2512-02660 — "smaller regions suffer disproportionately from patch quantization"
[^c11]: arxiv-2512-02660 — "a precision-bound regime where patch quantization limits dominate regardless of model capacity"
[^c12]: arxiv-2512-02660 — "yields negligible gains"
[^c13]: arxiv-2512-02660 — "smaller region sizes where patch quantization effects are more pronounced"
[^c14]: arxiv-2512-02660 — "Given a page containing the answer, can our approach identify the specific region?"
[^c15]: arxiv-2512-02660 — "is outside our scope"
[^c16]: arxiv-2512-02660 — "that groups semantically coherent blocks"
[^c17]: arxiv-2512-02660 — "The choice of aggregation strategy affects retrieval quality depending on region size and content density"
