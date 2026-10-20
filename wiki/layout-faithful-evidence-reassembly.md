---
description: "Recombining selected image crops for a vision-language answerer, keeping their relative and global positions, beat fixed raster-order concatenation in one pilot on ultra-high-resolution imagery."
aliases: ["layout-aware patch reassembly", "relative and global-layout preservation", "spatially faithful canvas", "layout-preserving crop composition"]
sources: ["arxiv-2511-20460"]
---
# Layout-faithful evidence reassembly

A search over a very large image ends with a set of selected regions, and something has to be done with them before the answering model sees anything. One option is to place them in a fixed raster order. Another is to keep them where they sat in the source image. The ZoomSearch paper treats this as a design variable with three settings: sequential concatenation in "a fixed raster order from upper left to lower right";[^c2] a relative-layout version, "relative-layout preserving, which compacts the canvas while" keeping the spatial relations among the patches;[^c1] and a relative and global-layout version that also keeps each patch's orientation with respect to the whole image, so that it "keeps their global orientation with respect to the original" image.[^c4]

## The mechanism

The adopted method, Layout-Aware Patch Reassembly, takes the selected patches and first sorts them into a coarse 3 × 3 partition of the search grid. "This anchors each patch to one of nine" quadrants, so that every patch keeps the quadrant it came from.[^c3] Inside each quadrant, rows and columns that contain no selected cells are removed, which compacts the block without changing the order of the cells that remain. Each non-empty block is then resized to one common cell size and placed in a fixed slot of a neutral gray canvas. The result is a canvas that is "compact in token budget" while the quadrant structure stays visible.[^c13] Nothing is trained; the canvas is an input transformation for an unchanged foundation model.

## What was measured

The comparison of reassembly strategies is a pilot, not the main benchmark. It runs on a subset of LRS-VQA, with the hierarchical search selecting the top-k patches per question. The text reads: "we randomly sample 2,000" question–image pairs with images of at least 2K, and uses a small backbone, "backbone for all subsequent pilot studies on this subset."[^c7][^c8] On that subset, "the relative & global-layout preserving strategy clearly performs best, achieving the highest" accuracy on almost all categories.[^c5] The authors' explanation is that when several patches are found, "both their mutual spatial relations and their coarse locations" help the model exploit spatial cues after reassembly.[^c9] "The third strategy consistently achieves the best results", which the authors take to show that spatial cues at both local and global levels matter.[^c6]

The clearest account of what the layout does at answer time is a qualitative case, not a rate. The reassembled canvas "renders spatial descriptors such as" a phrase like "bottom part of the image" unambiguous, because each patch keeps its absolute position in the original frame.[^c10] My reading: a question that refers to places in the image has something to refer to on the canvas, which a fixed-order concatenation does not provide.

## Limits

- The ordering was measured on one subset with a small backbone, with top-k selection. The full pipeline reports results with a larger backbone on the two benchmarks. The text read does not show the reassembly step alone, against the same selection, on those benchmarks; the component ablation in the supplement was not read for this note.
- The effect is an ordering between three strategies. The sections read give no effect size for the pilot gap, so the size of the advantage is not established here.
- Layout does not recover what the search missed. The paper's own failure case is an undercount caused by an incomplete search. There the layout confines the count to one quadrant, which the authors say "mitigates" the error, "although it does not eliminate it entirely."[^c11][^c12] The layout constrains where the answer is counted; it does not add the patch that was dropped.
- The canvas gives the answerer spatial words to use, but the paper does not test whether the answerer reads them more accurately than a raster-order arrangement of the same crops, beyond the aggregate comparison.
- The concept is tested for a machine answerer that receives the canvas as its only input. Human readers of such a composite were not studied in the text read. The resize to a common cell and the gray padding may cost detail; the paper does not measure that cost.

## Related

- [[reader-facing-evidence-rendering]] — the same question for memory QA: the artifact handed to the reader moves accuracy by a wide margin even when the content is held fixed. Here the rendering is the spatial arrangement of image crops, and the two results come from different domains, not one shared measurement.
- [[coarse-to-fine-evidence-zoom]] — the search whose selected regions this reassembly composes; that note's limits cover why a located region is not always answered correctly.
- [[patch-grid-granularity-bound]] — the grid whose cells the canvas keeps; a coarse grid caps how small a returned region can be, and the quadrant anchoring here is built on the same grid.

[^c1]: arxiv-2511-20460 — "relative-layout preserving, which compacts the canvas while"
[^c2]: arxiv-2511-20460 — "in a fixed raster order from upper left to lower right"
[^c3]: arxiv-2511-20460 — "This anchors each patch to one of nine"
[^c4]: arxiv-2511-20460 — "keeps their global orientation with respect to the original"
[^c5]: arxiv-2511-20460 — "the relative & global-layout preserving strategy clearly performs best"
[^c6]: arxiv-2511-20460 — "The third strategy consistently achieves the best results"
[^c7]: arxiv-2511-20460 — "we randomly sample 2,000"
[^c8]: arxiv-2511-20460 — "backbone for all subsequent pilot studies on this subset"
[^c9]: arxiv-2511-20460 — "both their mutual spatial relations and their coarse locations"
[^c10]: arxiv-2511-20460 — "the reassembled canvas renders spatial descriptors such as"
[^c11]: arxiv-2511-20460 — "the layout anchors patches to their original quadrants"
[^c12]: arxiv-2511-20460 — "although it does not eliminate it entirely"
[^c13]: arxiv-2511-20460 — "compact in token budget"
