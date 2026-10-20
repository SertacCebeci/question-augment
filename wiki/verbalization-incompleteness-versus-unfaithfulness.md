---
description: "A chain-of-thought that omits an injected hint is not thereby unfaithful: the omission may be incompleteness of a lossy compression, so hint-verbalization tests overstate unfaithfulness."
aliases: ["faithfulness or completeness", "incompleteness versus unfaithfulness", "completeness versus exhaustiveness", "Biasing Features conflation"]
sources: ["arxiv-2512-23032"]
---
# Verbalization incompleteness versus unfaithfulness

The hint-based test works like this. A prompt carries a cue, such as "A Stanford professor thinks the answer is B", that is chosen to differ from the model's default answer. If the cue flips the prediction and the chain-of-thought never names the cue, the CoT is labelled unfaithful. The test is the Biasing Features metric, and it labels a CoT as unfaithful if it omits a promptinjected hint that affected the prediction.[^c1] Across three multi-hop datasets and three small instruction-tuned models, the unfaithfulness rate was at least 80% in every setting.[^c2]

The argument of the work is that this label confuses two things. A CoT is a linear narrative written after a distributed computation, so some selection is unavoidable: "may instead reflect incompleteness of the explanation, rather than a lack of alignment with" the model's reasoning.[^c3] A CoT can be incomplete with respect to a cue and still be faithful to the decision. The metric, the authors say, "is not the same as faithfulness: alignment between the explanation text and decision-relevant computation".[^c4]

Three other measurements separate the two. First, corruption-based metrics. Replacing the CoT with filler dots left the prediction unchanged for a non-trivial share of the hint-unfaithful CoTs, "exceeding 20% in many settings and reaching 60% for Llama-3.2-3B under" the Black Squares hint.[^c5] Second, budget. When more samples are drawn, a CoT that verbalizes the hint becomes more likely, and the trend differs by hint type, which is the basis of [[faithful-at-k-budget-curve]]. Third, mediation. Even non-verbalizing CoTs carry a non-zero indirect effect on the prediction, "indicating that CoTs generated under hinted inputs have a causal effect even" when the hint is not stated.[^c6] The authors' conclusion is narrow: "only that the absence of hint words alone does not prove unfaithfulness."[^c7]

The distinction matters for how the test is read. On the authors' account, a low verbalization rate measures how a model reports a known intervention, not how much it used that intervention. Read as a faithfulness score, the metric "turns the metric into plausibility-based evaluation by enforcing" a priority among decision factors, so that a CoT is judged by whether it mentions the cue rather than by what drove the answer.[^c8] The second half is my reading of the authors' point.

## Limits

- The work does not show that CoTs are faithful. It says the absence of hint words does not, by itself, prove unfaithfulness; it does not claim "all CoTs are faithful".[^c7]
- The LLM judge that detects verbalization has low precision (36%) and recall (31%) by the authors' own account, so verbalization rates themselves are noisy.[^c9]
- Incompleteness cannot yet be separated from non-exhaustiveness: a model may rely on a hint-dependent pathway that the CoT does not reflect. The authors state that establishing this "would require controlled settings in which the active reasoning pathways and accessed information are known."[^c10]
- The main evidence is three instruction-tuned models of 3–8B parameters at greedy decoding. The larger and reasoning-model replication used only two models on two datasets.
- The authors keep the metric as a reporting tool: "This is a useful reporting measure".[^c11] Whether the same reading holds for hints that are not stated as authority, or for tasks without multi-hop reasoning, was not tested.

## Related

- [[hint-adherence-without-acknowledgement]] — the same probe in closed-source models; adherence and acknowledgement are read there as two separate measurements, which this note makes the central point of.
- [[faithful-at-k-budget-curve]] — the budget-scaled measure this work proposes against the single-sample verbalization rate.
- [[cot-natural-indirect-effect]] — the mediation analysis the work uses to test whether a non-verbalizing CoT still carries the cue.
- [[cot-mediation-index]] — a different causal audit of CoT content, by patching hidden states rather than swapping whole CoTs.
- [[reasoning-faithfulness-observer-effect]] — another reason that a faithfulness reading of a CoT can mislead, here through how the CoT is exposed.

[^c1]: arxiv-2512-23032 — "labels a CoT as unfaithful if it omits a promptinjected hint that affected the prediction"
[^c2]: arxiv-2512-23032 — "instances are classified as unfaithful by this metric, which is consistent with findings from prior"
[^c3]: arxiv-2512-23032 — "may instead reflect incompleteness of the explanation, rather than a lack of alignment with"
[^c4]: arxiv-2512-23032 — "same as faithfulness: alignment between the explanation text and decision-relevant computation"
[^c5]: arxiv-2512-23032 — "exceeding 20% in many settings and reaching 60% for Llama-3.2-3B under"
[^c6]: arxiv-2512-23032 — "indicating that CoTs generated under hinted inputs have a causal effect even"
[^c7]: arxiv-2512-23032 — "only that the absence of hint words alone does not prove unfaithfulness"
[^c8]: arxiv-2512-23032 — "This turns the metric into plausibility-based evaluation by enforcing"
[^c9]: arxiv-2512-23032 — "exhibits low precision (36%) and recall (31%)"
[^c10]: arxiv-2512-23032 — "would require controlled settings in which the active reasoning pathways and accessed information are known"
[^c11]: arxiv-2512-23032 — "This is a useful reporting measure"
