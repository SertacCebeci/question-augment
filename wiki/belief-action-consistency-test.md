---
description: "A stated probability counts as a belief only if, given it, the agent's action carries no extra information about the truth and choices move monotonically with it; testable black-box."
aliases: ["elicited belief validation", "conditional independence of action and outcome given stated belief", "cyclic monotonicity test"]
sources: ["arxiv-2602-06286"]
---
# Belief-action consistency test

A model's verbalized probability can be an isolated text output, unconnected to what the model does. Yamin et al. propose to validate it by eliciting both a probability p(x) and an action a for the same input x, in separate context windows, and testing two conditions on the joint sample (x, p, a, true state θ).[^c1]

**Sufficiency.** A reported belief should summarize all decision-relevant information the agent holds about θ. Formally, for any "perturbed utility maximizer" (expected utility minus a strictly convex regularizer, which covers logit choice, random utility models and KL-regularized policies), action and state are independent given the subjective belief. So if action is still correlated with θ given the elicited p, no such agent can hold p as its belief; it "knows more than it says".[^c2] The test is a nonparametric conditional-mutual-information test, plus a size measure: the cross-validated MSE reduction when A is added to p as a predictor of θ.[^c3]

**Action-guiding.** Choice probabilities should move monotonically with the stated belief. With several actions this is cyclic monotonicity; with a binary state it reduces to: the expected state-1 relative utility of the choice distribution rises with p.[^c4] It is tested by binning p into quantiles and solving a linear program for a utility-difference vector that makes bin means increase; a positive margin means strict monotonicity.[^c5]

**What the pair establishes.** The authors show the two conditions are necessary and sufficient for the data to be rationalized by such an agent who holds the elicited belief as true — with no assumption about its utility function.[^c6] The restriction that utility depends on (a, θ) but not on x matters: otherwise any action pattern is trivially rationalizable without beliefs.[^c7] Passing sufficiency alone is not proof of truthful reporting: an agent acting and reporting independent random values passes.[^c8]

**Findings.** On clinical diagnosis tasks, elicited beliefs often fail sufficiency, yet choices frequently remain monotone in elicited risk; failures are small for the strongest models.[^c9] Monotonicity was strict in 9 of 16 dataset/model pairs, and one pair (Fever–Llama) violated it.[^c10] Internal probabilistic coherence (law of iterated expectation) was a separate dimension: models good on decision-consistency were not necessarily coherent.[^c11]

This differs from calibration: a believer can be miscalibrated in good faith, while a model can state probabilities that do not govern its actions.[^c12] My inference: for questioning, a stated confidence should be trusted as far as downstream behavior is shown to depend on it, not merely because it is accurate.

## Limits

Only binary-state clinical tasks, a few model families, and verbalized numeric probabilities were tested. The test shows a stated number is not a sufficient summary; it cannot show what the model actually believes. Results depend on binning and on having ground-truth outcome samples from the environment. Prompt framing sensitivity varied (Llama most sensitive).

## Related

- [[sufficient-statistic]] — the sufficiency condition is this classical notion applied to a stated belief
- [[confidence-report-repair]] — repairing stated confidence; this note tests whether it is usable first
- [[behavioral-consistency-as-agent-filter]] — another use of agreement between behavior and report
- [[value-action-gap]] — a simpler count of one contradiction between a stated belief and the choice; it does not test sufficiency

[^c1]: arxiv-2602-06286 — "Second, we prompt the model with the same x in a separate context and ask it to take an action a."
[^c2]: arxiv-2602-06286 — "If a rational agent’s actions do have excess correlation with the true state given their elicited PE , the agent must “know more than they say"."
[^c3]: arxiv-2602-06286 — "Under the conditional-independence null, adding the action A should not improve prediction of θ once we"
[^c4]: arxiv-2602-06286 — "Thus, as the elicited probability of the positive state increases, the model’s choice probabilities"
[^c5]: arxiv-2602-06286 — "we solve"
[^c6]: arxiv-2602-06286 — "they are provably necessary and sufficient for there to exist an"
[^c7]: arxiv-2602-06286 — "Otherwise any action distribution a(x) is trivially rationalizable"
[^c8]: arxiv-2602-06286 — "This satisfies a ⊥"
[^c9]: arxiv-2602-06286 — "elicited beliefs often fail the sufficiency"
[^c10]: arxiv-2602-06286 — "In 9 of 16 dataset/model combinations,"
[^c11]: arxiv-2602-06286 — "This"
[^c12]: arxiv-2602-06286 — "an LLM may express probabilities"
