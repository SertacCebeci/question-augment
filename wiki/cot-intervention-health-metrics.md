---
description: "Three counterfactual interventions on a reasoning trace (remove, paraphrase, replace with irrelevant text) give signatures separating post-hoc, encoded and internalized reasoning."
aliases: ["necessity paraphrasability substantivity metrics", "CoT pathology diagnosis", "CoT health metrics"]
sources: ["arxiv-2602-13904"]
---
# CoT intervention health metrics

A stated reasoning trace can fail an answerer in different ways, and a single "is the trace faithful" score hides which. The source paper (arxiv-2602-13904) defines three metrics with one shared form: sample a trace and answer, then measure how the log-probability of the same answer changes after an intervention on the trace. Each metric lies in (-1, 1) and higher is healthier.[^c1]

**The three interventions.**
- Necessity: drop the trace by instructing the model not to think. Near 0 means the trace is not load-bearing; near 1 means the answer collapses without it.[^c2]
- Paraphrasability: rewrite only the trace, keeping meaning and length. Near 0 means the trace is paraphrasable; persistently negative scores mean sensitivity to surface form, expected under encoded or steganographic use.[^c3]
- Substantivity: replace the trace with a same-length trace from an irrelevant task. It separates a trace whose content matters from one whose mere presence (extra forward passes) matters.[^c4]

**Three pathologies and their expected signatures.**
- Post-hoc: the answer is fixed before or early in the trace, so the trace is unnecessary; the paper expects a positive Cohen's d on necessity and unpredictable values for the other two.[^c5]
- Encoded: the trace is load-bearing but only through a codebook or surface regularities, so paraphrasing hurts while irrelevant replacement is not distinct.[^c6]
- Internalized: computation happens in the forward passes of the trace, so the literal content is not load-bearing; the model appears reliant on the trace yet is paraphrasable and substitutable.[^c7]
- Healthy: reliant on the trace, paraphrasable, not substitutable.[^c8]

**How it was tested.** The authors fine-tuned OLMo-3-7B-Think with LoRA into "model organisms" with known pathologies: encoded traces via a fixed codebook, irrelevant cross-domain traces for internalized, and the answer revealed in the prompt for post-hoc. Three Reasoning Gym tasks were used, and Cohen's d against the pre-SFT baseline was tracked over checkpoints.[^c9] Their summary: post-hoc is most saliently diagnosed by necessity, internalized by substitutability, encoded by paraphrasability, though the last signal may attenuate as training proceeds.[^c10] Metrics detect pathologies at different speeds, so a suite across checkpoints covers more than any single one.[^c11]

## Limits

- The pathologies are induced by SFT, not found in the wild; the paper says the organisms are hard to train while keeping accuracy high, which may explain some metrics deviating from expectation.[^c12]
- Paraphrasability signal faded late in training on Largest Island, and the substitutability signal for encoded reasoning stayed slightly negative there.[^c12]
- Passing is not faithfulness: the authors say absence of these pathologies does not mean a perfectly faithful chain of thought, and the metrics assume reasoning in text space.[^c13]
- The healthy baseline is operational (the model before the intervention), not a ground-truth label.[^c14]
- Interventions such as removing or substituting the trace may push some model families off-distribution (the authors flag this).
- Nothing here concerns question asking; applying it to an answerer's stated rationale is my inference.

## Related

- [[cot-monitorability-information-bound]] — theoretical bound on what a trace can reveal; these metrics probe causal reliance instead
- [[hint-adherence-without-acknowledgement]] — another way a trace can omit what drove the answer
- [[reasoning-faithfulness-observer-effect]] — pressure on traces under oversight

[^c1]: arxiv-2602-13904 — "Each of the metrics lies in the range (−1, 1), with higher values always being healthier."
[^c2]: arxiv-2602-13904 — "When the log-probability without the CoT present is much lower than the original logprobability, the metric will tend toward 1"
[^c3]: arxiv-2602-13904 — "persistently negative scores indicate sensitivity to surface form, which is expected under encoded or steganographic use of the CoT"
[^c4]: arxiv-2602-13904 — "whether the content of the CoT is load-bearing, or if it is only the presence of the CoT which matters"
[^c5]: arxiv-2602-13904 — "the expected Cohen’s d for necessity is positive, while the expected Cohen’s d values for"
[^c6]: arxiv-2602-13904 — "Under this pathology, the CoT is load-bearing - removing it hurts"
[^c7]: arxiv-2602-13904 — "because the specific literal content of the CoT is not load-bearing, we expect it to be both"
[^c8]: arxiv-2602-13904 — "the model is reliant on the CoT, the CoT can be paraphrased without"
[^c9]: arxiv-2602-13904 — "Cohen’s d is calculated as the difference"
[^c10]: arxiv-2602-13904 — "Specifically, post-hoc pathology is most saliently diagnosed by the necessity metric, while"
[^c11]: arxiv-2602-13904 — "different metrics may detect pathologies at varying speeds"
[^c12]: arxiv-2602-13904 — "challenging to train internalized and encoded model organisms to elicit the internalized or"
[^c13]: arxiv-2602-13904 — "the absence of particular pathologies does not"
[^c14]: arxiv-2602-13904 — "we operationally define healthy as the model’s relative reasoning"
