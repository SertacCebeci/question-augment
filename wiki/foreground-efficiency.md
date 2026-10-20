---
description: "Counting foreground voxels, and fitting how fast a learner closes its gap to full-data training, can reverse the verdict raw voxel counts give; it is a proxy for effort, not measured time."
aliases: ["FG-Eff", "foreground efficiency", "foreground-voxel annotation efficiency", "decay-fitted annotation efficiency"]
sources: ["arxiv-2511-19183"]
---
# Foreground efficiency

Annotation effort in 3D segmentation is often scored in voxels, the number of labelled volume elements. The paper's objection is that a voxel is not a unit of work. A query made only of background and a query containing several structures to be delineated can have the same voxel count, yet "has the same number of voxels as a query containing multiple" structures demands far more labelling work.[^c1] The consequence is a bias: "purely using voxel based metrics measuring annotation effort can lead to a systematic bias favoring QMs which require a large annotation effort per queried voxel."[^c2]

The paper's correction counts only the voxels that carry the work. The premise is that "annotating background has a negligible annotation effort compared to foreground."[^c3] The measure is a curve fit. An exponential decay is fitted "to the performance gap to a model trained on the entire dataset against the number of foreground voxels"[^c4], and the decay parameter γ is the score. "Higher values indicate that a QM is more annotation efficient as it converges faster to the performance" obtained with the full dataset.[^c5] A method scores well if its learning curve closes the gap to full-data training after few foreground voxels have been labelled.

The score can reverse a verdict. Random draws the fewest foreground voxels, so it looks efficient on this measure: "Random consistently draws the least amount of foreground voxels."[^c6] The paper concludes that this good ranking "makes it unclear how much the annotation effort is actually reduced" when AL replaces Random.[^c7] The reverse holds for the strongest active method on accuracy. Predictive Entropy "achieves the best mean rank in both the AUBC" of the AL methods,[^c8] yet the paper says its queries "commonly focus on foreground classes and thus query a lot of foreground", which gives it "a relatively low FG-Eff compared to all other methods."[^c13][^c9] My reading is that the measure asks how little foreground a method must demand per unit of gap closed, a different question from the one accuracy measures ask.

The general point is that the cost of a query is what the answerer must work through, not how many items it contains. [[annotated-area-cost]] makes the same move with covered surface instead of foreground voxels. The transfer from one to the other is my inference.

## Limits

- It is a proxy, not time. The paper says "the number of foreground voxels represents a proxy for annotation effort, the FG-Eff does not replace other performance metrics but should be seen as an extension of them."[^c10] The sections read here contain no measured annotation time.
- It compares methods only within one setting: the paper says FG-Eff "allows meaningful comparisons of QMS across a single Label Regime with identical training setups."[^c11]
- The score depends on an exponential-decay fit. The formal definition is in the paper's appendix, which I did not read in this pass. Whether another curve shape would rank the methods the same way was not tested in the text read.
- The premise that background is nearly free is asserted, not measured. A dataset where background boundaries are hard to draw would weaken it. That is my inference.
- Counting foreground voxels does not separate a compact foreground region from a scattered one with the same count. That is the surface issue [[annotated-area-cost]] raises. Whether the two corrections agree on a real query set was not tested here.
- The paper says that "none of the related work takes this factor into account with any explicit measurement."[^c12] That is a claim about the literature the paper surveyed, not something checked here.

## Related

- [[annotated-area-cost]] — the other correction of the raw count, measured by covered surface rather than by foreground voxels.
- [[foreground-aware-random-sampling]] — the baseline that draws little foreground and so ranks well on this measure while losing on the accuracy measures.

[^c1]: arxiv-2511-19183 — "has the same number of voxels as a query containing multiple"
[^c2]: arxiv-2511-19183 — "purely using voxel based metrics measuring annotation effort can lead to a systematic bias favoring QMs"
[^c3]: arxiv-2511-19183 — "annotating background has a negligible annotation effort compared to foreground"
[^c4]: arxiv-2511-19183 — "fitted to the performance gap to a model trained on the entire dataset against the number of foreground voxels"
[^c5]: arxiv-2511-19183 — "Higher values indicate that a QM is more annotation efficient as it converges faster to the performance"
[^c6]: arxiv-2511-19183 — "Random consistently draws the least amount of foreground voxels"
[^c7]: arxiv-2511-19183 — "makes it unclear how much the annotation effort is actually reduced"
[^c8]: arxiv-2511-19183 — "It achieves the best mean rank in both the AUBC"
[^c9]: arxiv-2511-19183 — "compared to all other methods"
[^c10]: arxiv-2511-19183 — "performance metrics but should be seen as an extension of them"
[^c11]: arxiv-2511-19183 — "allows meaningful comparisons of QMS across a single Label Regime with identical training setups"
[^c12]: arxiv-2511-19183 — "work takes this factor into account with any explicit measurement"
[^c13]: arxiv-2511-19183 — "Predictive Entropy also commonly focus on foreground classes and thus query a lot of foreground"
