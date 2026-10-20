---
description: "Proof verifiers trained to enumerate localized errors before a verdict, with the verdict tied to that list, are argued to beat 0-7 score regression, which can be fit without locating errors."
aliases: ["error finding", "error-finding verifier", "localized critique before verdict", "error enumeration instead of score prediction"]
sources: ["doi-10-48550-arxiv-2606-13473", "arxiv-2511-22832"]
---
# Error-enumeration verdict format

The obvious way to train a verifier for long proofs is to regress a score on the 0–7 scale used for grading. The authors reject this ("We deliberately avoid this formulation.") and instead ask the verifier for a structured output: a step-by-step analysis, a list of concrete errors (or none), and then one verdict from four classes, no_errors, minor_gaps, has_errors or fundamentally_wrong.[^c1] The argument is that a regression objective "does not need to know where the candidate is wrong, or why, to drive its loss" down.[^c2] The same point, from process supervision, is that "localizing errors rather than predicting aggregate scores leads to" more reliable verifiers.[^c3] The paper's summary of the task is that "it requires localizing and describing errors, not ranking them."[^c4]

The mechanism is a coupling between the two parts of the output. The verdict is meant to be a function of the list: a verifier that calls a proof no_errors must commit to an empty error list, and one that calls it fundamentally_wrong must list substantive errors. The authors say this is "what makes the Verifier Expert usable as a building block," because the error list is a critique the fixer can act on, and because the verdict and the critique "cannot drift out of sync."[^c5] A score regressor would need a further post-processing step to recover the same critique structure.[^c6]

The training reward mirrors the output. It is a composite, with the error term weighted 0.7 and the verdict term 0.3.[^c7] The error term is a semantic match between predicted and reference errors, scored by a frontier LLM judge, which rewards an error that is "spatially localized (the model points to the right step)" as well as one "semantically described."[^c8] The verdict term is order-aware: a verdict at distance 0 from the reference class gets reward 1, at distance 1 gets 0.5, and at distance 2 or more gets 0.[^c13] The authors say this "makes the verdict reward tolerant of a single-step miscalibration."[^c14] The composite is built so that matching the verdict alone is not enough: "a model that only matches the verdict (e.g. by predicting no_errors on every" example cannot score well, and matching the error list is "harder to do without actually reading the proof."[^c15][^c9]

The training data is taken from the Proof Expert's own verifier. Each scored candidate already has an analysis and a verdict tied to the judge that set its pessimistic-min score, so the authors say the data is "harvested, almost for free."[^c10] The verdict classes are unbalanced in that data, and the authors "rebalance the four classes to avoid letting the Verifier Expert collapse to the" two extremes.[^c11] The reason for training a separate verifier rather than calling the Proof Expert's judges is cost: the judge pipeline takes seconds per candidate, while the trained model's per-candidate cost "is in the hundreds of milliseconds."[^c12]

## Limits

- The slices I read contain no comparison of error-enumeration against score regression on verification accuracy or on downstream search. The claim that the format is better is a design argument, not a measured result. (my reading)
- The error term is itself graded by a frontier LLM judge comparing predicted and reference errors. The verifier is trained toward a target produced by another judge, so it inherits the judge problems discussed in [[pessimistic-min-judge-aggregation]].
- Nothing enforces the coupling between list and verdict: both are generated text. The format makes an inconsistent output a training loss, not an impossibility. (my inference)
- A list of plausible-sounding errors can be padded. The paper documents surface gaming in its own RL runs (length, format, shortcut phrases), but does not test padded error lists against the error term. (my inference)[^c16]
- Localization accuracy, meaning whether the named step is the broken one, is not reported in the parts I read. The format targets the gap between detecting and naming a flaw, which [[cot-judge-detection-localization-gap]] measures in other judges; here that gap is not measured.
- The class rebalancing is a manual choice, and the intermediate classes are the rarest in both the RL distribution and the harvested data.[^c17]
- Staging without a coupled list is a weaker form. An entity-matching prompt stages matched and unmatched tokens, then the influential attributes, and only then asks for the yes/no verdict. Nothing there ties the verdict to a scored error list, and the gains over a plain prompt were mixed across its six datasets, so the staging alone is not shown to carry them (my reading).[^c18]

## Related

- [[cot-judge-detection-localization-gap]] — the measured gap between flagging a broken chain and naming the step; this format is aimed at that gap, untested here
- [[defect-localization]] — localizing a defect as the target of a critique
- [[agentic-iteration-gap-under-localized-verifier-feedback]] — localized feedback drives correction in puzzles; the enumerated error list plays the same role for the fixer
- [[pessimistic-min-judge-aggregation]] — the aggregator whose verdict and critique the verifier is trained to reproduce

[^c1]: doi-10-48550-arxiv-2606-13473 — "We deliberately avoid this formulation."
[^c2]: doi-10-48550-arxiv-2606-13473 — "does not need to know where the candidate is wrong, or why, to drive its loss"
[^c3]: doi-10-48550-arxiv-2606-13473 — "localizing errors rather than predicting aggregate scores leads to"
[^c4]: doi-10-48550-arxiv-2606-13473 — "it requires localizing and describing errors, not ranking them."
[^c5]: doi-10-48550-arxiv-2606-13473 — "so the two cannot drift out of sync."
[^c6]: doi-10-48550-arxiv-2606-13473 — "contrast, would require an additional layer of post-processing to recover the same critique structure."
[^c7]: doi-10-48550-arxiv-2606-13473 — "The Verifier Expert is trained with a composite reward that mirrors the structure of its output:"
[^c8]: doi-10-48550-arxiv-2606-13473 — "is spatially localized (the model points to the right step)"
[^c9]: doi-10-48550-arxiv-2606-13473 — "harder to do without actually reading the proof."
[^c10]: doi-10-48550-arxiv-2606-13473 — "It is harvested, almost for free,"
[^c11]: doi-10-48550-arxiv-2606-13473 — "We rebalance the four classes to avoid letting the Verifier Expert collapse to the"
[^c12]: doi-10-48550-arxiv-2606-13473 — "cost is in the hundreds of milliseconds."
[^c13]: doi-10-48550-arxiv-2606-13473 — "distance 0 yields a reward of 1,"
[^c14]: doi-10-48550-arxiv-2606-13473 — "This makes the verdict reward tolerant of a single-step miscalibration"
[^c15]: doi-10-48550-arxiv-2606-13473 — "a model that only matches the verdict (e.g. by predicting no_errors on every"
[^c16]: doi-10-48550-arxiv-2606-13473 — "Format hacking. The policy converged on a small set of surface templates"
[^c17]: doi-10-48550-arxiv-2606-13473 — "The intermediate classes (minor_gaps, fundamentally_wrong) are deliberately"
[^c18]: arxiv-2511-22832 — "Based on steps 1 and 2, ask LLM whether these"
