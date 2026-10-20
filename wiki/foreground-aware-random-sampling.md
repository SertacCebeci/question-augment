---
description: "Random draws that force foreground into a set share of patches are a harder baseline for 3D active learning than plain random; most active learners fail to beat them reliably."
aliases: ["Foreground Aware Random sampling", "Random 33% FG", "Random 66% FG", "foreground-oversampled random baseline"]
sources: ["arxiv-2511-19183"]
---
# Foreground-aware random sampling

Plain random sampling is the baseline active learning is usually judged against, and it costs nothing to run. In 3D biomedical segmentation it is a weak comparator for a reason that lies in the data, not the learner. A target such as an organ or tumour often fills a small part of the volume, so a uniformly drawn patch is mostly background, and background is cheap to annotate. The paper says the standard Random baseline "often queries image regions that are purely background, which require minimal annotation effort."[^f1] Because classes also differ in size, a uniform draw shows a "bias favoring large classes".[^f2] The paper's diagnosis is that the baseline is handicapped by the setting, not by randomness itself: the standard Random baseline is "artificially disadvantaged when combined with partial annotations."[^f3]

Foreground-aware random sampling keeps the draw random and changes where the patch is centred. The paper's version simulates screening an image for a randomly chosen foreground class, so that foreground is in the query by design. Its aim is to "ensure that foreground is present in a specific percentage of" the queries.[^f4] The two variants differ in that percentage. For the 33% variant the proportion of fully random selections rises to 66%, "while 33% of patches are drawn with the aforementioned foreground oversampling."[^f5] The 66% variant is the more foreground-heavy one by its name; the parts of the paper read here do not give its exact split, so that reading is mine.

What the comparison found is the point. Foreground-aware random strategies outperform plain Random on every measured metric except the foreground-efficiency score, which is the exception the paper names.[^f16] The paper's summary is that "Foreground Aware Random methods are a much harder baseline than purely Random, and most AL methods have issues outperforming them reliably."[^f6] Random 66% FG "seems to be the best overall method based on the AUBC mean rank".[^f7] Only one active method clearly competes with it: "Entropy outperforms Random 66% FG slightly more often than it is outperformed".[^f8] The abstract compresses the result to the claim that "none reliably surpasses an improved Foreground Aware Random sampling".[^f9]

The stake is prior work. The paper reports that Burmeister et al. found AL methods do not "reliably outperform advanced Random sampling strategies where the sampling is adapted to the 3D structure"[^f15], and notes that "Crucially, this is the only work investigating improved Random baselines."[^f10] The paper's question is "how improved Random baselines would have changed the verdict of other works".[^f11] For someone asking whether active learning helps on a 3D task, the answer depends on which random is the comparator. A verdict that AL beats random may be a verdict against the weak one.

## Limits

- The evidence comes from four datasets, three label regimes each, and nnU-Net models. The verdict is not uniform across them: on AMOS, "AL methods are generally outperformed by Random strategies."[^f12] The paper's own finding is that the benefit of AL depends on task-specific parameters.
- The 33% and 66% shares are fixed by the authors. The parts read here contain no sweep over the share, so whether the right foreground fraction is the same elsewhere is not shown.
- The baseline is not harder across the board. On Final Dice, Random 66% FG is, in the paper's words, "apart from Random, the worst performing method as AL methods"[^f13], because the AL methods "become better for later annotation budgets."[^f17] It is harder on the area-under-budget measure and at early budgets.
- The paper ties performance to "foreground selected is an important factor for the performance of a QM."[^f14] That is a pattern across its strategies. Changing the foreground share of a single strategy was not isolated, so the causal reading is mine.
- Carrying the result beyond 3D biomedical segmentation is my inference. The argument rests on a background class that dominates the volume, a property the paper names for its setting.

## Related

- [[foreground-efficiency]] — the cost measure that rewards this baseline for drawing little foreground, so it can rank it well on the one metric where it loses.
- [[annotated-area-cost]] — another case where a raw count of queried items misstates the labelling work.
- [[class-balanced-query-model-selection]] — also finds that the class balance of the queried set decides which query model wins, in federated active learning.

[^f1]: arxiv-2511-19183 — "purely background, which require minimal annotation effort"
[^f2]: arxiv-2511-19183 — "bias favoring large classes"
[^f3]: arxiv-2511-19183 — "artificially disadvantaged when combined with partial annotations"
[^f4]: arxiv-2511-19183 — "ensure that foreground is present in a specific percentage of"
[^f5]: arxiv-2511-19183 — "while 33% of patches are drawn with the aforementioned foreground oversampling"
[^f6]: arxiv-2511-19183 — "most AL methods have issues outperforming them reliably"
[^f7]: arxiv-2511-19183 — "Random 66% FG seems to be the best overall method based on the AUBC mean rank"
[^f8]: arxiv-2511-19183 — "Entropy outperforms Random 66% FG slightly more often than it is outperformed"
[^f9]: arxiv-2511-19183 — "none reliably surpasses an improved Foreground Aware Random sampling"
[^f10]: arxiv-2511-19183 — "Crucially, this is the only work investigating improved Random baselines"
[^f11]: arxiv-2511-19183 — "how improved Random baselines would have changed the verdict of other works"
[^f12]: arxiv-2511-19183 — "AL methods are generally outperformed by Random strategies"
[^f13]: arxiv-2511-19183 — "apart from Random, the worst performing method as AL methods"
[^f14]: arxiv-2511-19183 — "foreground selected is an important factor for the performance of a QM"
[^f15]: arxiv-2511-19183 — "reliably outperform advanced Random sampling strategies where the sampling is adapted to the 3D structure"
[^f16]: arxiv-2511-19183 — "measured metrics with the exception of FG-Eff"
[^f17]: arxiv-2511-19183 — "become better for later annotation budgets"
