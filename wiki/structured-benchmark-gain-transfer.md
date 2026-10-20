---
description: "Gains newer models post on a structured indoor spatial benchmark can vanish on open-world scenes, where the layout and scale priors that carried them no longer hold."
aliases: ["indoor benchmark gain mirage", "open-world transfer gap", "benchmark distribution gain transfer"]
sources: ["arxiv-2512-19683"]
---
# Structured benchmark gain transfer

A benchmark samples a particular distribution of scenes: how large they are, how regular their layouts, whether anything moves. A score on it measures skill on that distribution, and a gain across model versions may measure something else if the distribution carries answers by itself. The work this note rests on tests the case for spatial reasoning. It compares two benchmarks on the same model families. On an indoor set, VSI-Bench, newer versions "consistently outperform older ones by a substantial margin," and the authors cite "+24.1 gain of InternVL3.5-38B to InternVL2-40B."[^n10][^n9] On OpenBench, a set of pedestrian-perspective open-world scenes built from stereo cameras, LiDAR and IMU/GPS, the same comparison gives little: "newer model versions show only" marginal gains over their predecessors.[^n1][^n11] The abstract puts the result as "the performance gains observed in structured indoor benchmarks vanish in open-world settings."[^n2]

The mechanism the authors give is a prior that the indoor scenes allow. "In indoor scenes, models can leverage linguistic priors to answer correctly even without visual inputs."[^n4] The open-world set is built to break this: "In our open-world scenes, these priors fail, forcing a reliance on visual cues."[^n5] The indoor set is described by its constraints, "Constrained Scale" and "Structured layouts," with "Static, no motion," where the open-world set adds "Large Scale Variation" and "Unstructured layout."[^n6][^n12]

The authors also offer a source for the indoor gains. Newer versions may have seen more data of the benchmarks' kind: "more spatial QA data similar to the benchmarks are included."[^n3] They say this "may explain the observed progress" and do not test it.[^n7]

What survives the transfer as a general point is a question to put to any benchmark gain: does it come from the capability the benchmark names, or from the scene distribution it samples? A way to ask it is to move the same items to a distribution where the sampled priors fail and see whether the gain holds. The work does this with a new set rather than a re-weighting of the old one (my reading of the design).

## Limits

- One comparison: a new benchmark against one indoor benchmark, on two model families. The two sets differ in scale, layout, motion and semantic diversity together, so the text cannot attribute the drop to any one of them. The work does not vary them one at a time (my reading).
- The version-to-version comparison uses the largest or latest models of each family, and one human result is marked as "means evaluated on a tiny subset."[^n8] The gain figures are reported point values; no interval is given in the part read.
- The training-data explanation for the indoor gains is posited, not measured. Nothing here shows that the indoor gains are contamination.
- The claim covers spatial questions about scene geometry. It is not a claim about benchmarks in general, and a benchmark whose sampled prior is correct for its target distribution would not show this gap.

## Related

- [[counterfactual-image-grounding-audit]] — the same work's blinding test, which removes the image to measure how much a model's answer depends on it
- [[visual-robustness-score]] — an atypical-image test that separates what a model knows about typical objects from what it sees
- [[post-cutoff-corpus-benchmark-isolation]] — a different protection of a benchmark's gain: removing what models already memorised rather than the scene prior

[^n1]: arxiv-2512-19683 — "newer model versions show only"
[^n2]: arxiv-2512-19683 — "vanish in open-world settings"
[^n3]: arxiv-2512-19683 — "more spatial QA data similar to the benchmarks are included"
[^n4]: arxiv-2512-19683 — "In indoor scenes, models can leverage linguistic priors to"
[^n5]: arxiv-2512-19683 — "In our open-world scenes, these priors fail, forcing a reliance"
[^n6]: arxiv-2512-19683 — "Constrained Scale"
[^n7]: arxiv-2512-19683 — "which we posit may explain the observed progress"
[^n8]: arxiv-2512-19683 — "means evaluated on a tiny subset"
[^n9]: arxiv-2512-19683 — "+24.1 gain of InternVL3.5-38B to InternVL2-40B"
[^n10]: arxiv-2512-19683 — "consistently outperform older ones by a substantial margin"
[^n11]: arxiv-2512-19683 — "built from pedestrian-perspective videos captured with synchronized stereo cameras"
[^n12]: arxiv-2512-19683 — "Large Scale Variation"
