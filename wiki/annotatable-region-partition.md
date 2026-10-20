---
description: "Active learning on point clouds queries a region rather than a point, so the partition is a parameter: a 2D grid of columns works as well as supervoxels only while its edge length stays small."
aliases: ["region separation", "column-based region separation", "annotatable region partition", "2D grid columns for annotation"]
sources: ["arxiv-2512-05759"]
---
# Annotatable region partition

In 3D active learning the oracle is asked about a region, not a single point. The paper frames the problem as "finding regions that can be efficiently annotated by a human".[^c1] The partition of the cloud into regions therefore decides what a query can contain. Here the partition is a 2D grid on the XY-plane: "We divide the point cloud into spatial columns of a given grid resolution r using a 2D grid on the XY-plane."[^c2] The stated purpose is to bound the work of one query, "as the number of points that can be queried is limited by the size of the column".[^c3] Storage follows from the same geometry: "each column can be described using straightforward x-y-coordinates".[^c4] A query is then a bounded, indexable patch, not a set of point indices.

The alternative is an unsupervised segmentation into supervoxels. VCCS, the method used by the prior work ReDAL, "aims to produce over-segmentation masks that are fully consistent with" the local spatial geometry.[^c5] The authors report that such approaches "sometimes struggle to find coherent supervoxels that can be easily annotated on real-world data".[^c6] In their own attempt on Toronto-3D, "we found that VCCS, which is the clustering method used in ReDAL, was not able to produce reliable clusters".[^c7]

The grain matters. With the ReDAL selection held fixed, and only the partition varied, "columns with an edge length of 0.5 meters are competitive with the supervoxels used by ReDAL",[^c8] while "with a larger edge length of 3.0 meters the selected columns are not competitive anymore."[^c9] The partition is therefore a parameter that decides whether the regions are competitive at all, not a neutral preprocessing step. A similar dependence on grain appears in [[requested-span-granularity-gradient]], where the size of the requested span sets difficulty.

The partition is kept separate from the score. Each region is ranked by averaging a per-point uncertainty over its points; the paper defines "the average entropy for a region S" this way and does the same for the variation ratio (see [[variation-ratio]]).[^c10] Two knobs, the grid and the score, can then be varied one at a time, which is what the ablation does.

## Limits

- Only edge lengths of 0.5, 1.0 and 3.0 m are tested. The optimum is not identified. The paper names "a location-dependent adjustment of the grid resolution" as future work.[^c11]
- Results vary more on the private Freiburg data: "there is more variation found in the Freiburg results", so the paper interprets S3DIS and Toronto and treats Freiburg as validation.[^c12]
- Columns always include floor and ceiling, which inflates the annotated area indoors (see [[annotated-area-cost]]).
- The claim that "columns are robust under domain changes"[^c13] is made in the conclusion. The paper checks three datasets, so this is not a general robustness result.
- The VCCS failure is one implementation on one dataset. It does not show that supervoxels fail in general.
- The grid assumes the XY-plane is the natural axis of a scene. Data where ground is not roughly horizontal is not tested; that limit is my inference.

## Related

- [[annotated-area-cost]] — the covered-area measure that rewards this partition's compact regions.
- [[variation-ratio]] — the ensemble score the paper averages over each region.
- [[requested-span-granularity-gradient]] — the grain of a request as a difficulty variable in another setting.
- [[label-complexity-as-noisy-lossy-compression]] — pool-based selection as a code; the regions here are the units that get selected.

[^c1]: arxiv-2512-05759 — "but also finding regions that can be efficiently annotated by a human"
[^c2]: arxiv-2512-05759 — "We divide the point cloud into spatial columns of a given grid resolution r using a 2D grid on the XY-plane"
[^c3]: arxiv-2512-05759 — "as the number of points that can be queried is limited by the size of the column"
[^c4]: arxiv-2512-05759 — "each column can be described using straightforward x-y-coordinates"
[^c5]: arxiv-2512-05759 — "aims to produce over-segmentation masks that are fully consistent with"
[^c6]: arxiv-2512-05759 — "such approaches sometimes struggle to find coherent supervoxels that can be easily annotated on real-world data"
[^c7]: arxiv-2512-05759 — "we found that VCCS, which is the clustering method used in ReDAL, was not able to produce reliable clusters"
[^c8]: arxiv-2512-05759 — "columns with an edge length of 0.5 meters are competitive with the supervoxels used by ReDAL"
[^c9]: arxiv-2512-05759 — "with a larger edge length of 3.0 meters the selected columns are not competitive anymore"
[^c10]: arxiv-2512-05759 — "we define then the average entropy for a region S as"
[^c11]: arxiv-2512-05759 — "one could utilize a location-dependent adjustment of the grid resolution"
[^c12]: arxiv-2512-05759 — "there is more variation found in the Freiburg"
[^c13]: arxiv-2512-05759 — "columns are robust under domain changes"
