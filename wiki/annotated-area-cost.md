---
description: "Annotation effort is better counted as the area a human must survey than as the number of labelled points: sparse picks cover many objects while their point fraction stays small."
aliases: ["annotated area", "covered-area annotation cost", "area-based labelling effort"]
sources: ["arxiv-2512-05759", "arxiv-2511-19183"]
---
# Annotated area as annotation cost

Active learning for segmentation is usually scored by the fraction of points a selection asks the annotator to label. The paper argues that this ledger misstates the work: "the expected annotation effort is not well estimated in existing studies".[^c1] The mechanism is spatial. A small set of scattered points can touch the surfaces of many objects, so a small point fraction still obliges the annotator to survey a large area.[^c2] "Since a human is not efficient in annotating single points, we argue that the covered surface area needs to be considered to estimate the annotation effort."[^c3]

The measure is computed per selected cluster. The exact covered area is hard to obtain, so the paper uses "(half of) the surface A of the cuboid containing the selected points", where each edge length is the extent of the cluster along one axis.[^c4] The cuboid's surface grows as the selected points become sparser, which is the direction in which a point count understates the work. Two queries with the same number of points, one scattered and one a compact patch, therefore get different costs. That consequence is my reading; the paper states the cuboid as its approximation and says the measure "will grow with increased sparsity of the selection points".

Measured this way, the column partition is much cheaper than the supervoxel alternative. Against VCCS the column method "requires way less annotated area (more than an order of magnitude)" for a similar mIoU.[^c5] The ranking depends on the partition, though. On the indoor S3DIS set "the VCCS based approaches are slightly better",[^c6] which the paper attributes to columns: "in indoor environments the annotated area is inflated for our approach".[^c7]

## Limits

- The area is an approximation, a cuboid half-surface, not the surface an annotator actually inspects. The paper says an exact estimate "is not easy to obtain".[^c8]
- No human timing was measured. The one effort figure is context for the manual Freiburg labelling, "The annotation took about 85 working hours",[^c9] and not a comparison of annotation time between selections.
- The claim that point counts mislead is argued from sparse selections and checked only on the paper's own pipelines. The paper does not vary sparsity against measured annotation time.
- The cuboid includes floor and ceiling for columns indoors, so the measure depends on the partition as well as on the points.
- Transfer beyond point clouds is my inference. The idea that the cost of a question is what its answerer must survey, rather than the number of items asked, is not tested in the paper.

## Related

- [[annotatable-region-partition]] — the column partition whose compact regions this measure rewards.
- [[label-complexity-as-noisy-lossy-compression]] — takes the label count as the unit of cost; the paper replaces that unit with covered area.
- [[class-stratified-scheduled-noise-uncertainty-sampling]] — another segmentation selection rule whose claim is also framed as annotation efficiency.
- [[foreground-efficiency]] — a second correction of the same point count, made by counting foreground voxels and fitting a decay; it rests on the premise that background is nearly free to label: "annotating background has a negligible annotation effort compared to foreground."[^c10] Where this note counts the surface a selection spans, that one counts the voxels that carry the work; the two measures are not tested against each other.

[^c1]: arxiv-2512-05759 — "the expected annotation effort is not well estimated in existing studies"
[^c2]: arxiv-2512-05759 — "In this case a small fraction of points can cover the surfaces of many objects."
[^c3]: arxiv-2512-05759 — "Since a human is not efficient in annotating single points, we argue that the covered surface area needs to be considered to estimate the annotation effort."
[^c4]: arxiv-2512-05759 — "we simplify it by using (half of) the surface A of the cuboid containing the selected points"
[^c5]: arxiv-2512-05759 — "requires way less annotated area (more than an order of magnitude)"
[^c6]: arxiv-2512-05759 — "In this setting the VCCS based approaches are slightly better"
[^c7]: arxiv-2512-05759 — "in indoor environments the annotated area is inflated for our approach"
[^c8]: arxiv-2512-05759 — "An exact estimate of this area is not easy to obtain"
[^c9]: arxiv-2512-05759 — "The annotation took about 85 working hours"
[^c10]: arxiv-2511-19183 — "annotating background has a negligible annotation effort compared to foreground"
