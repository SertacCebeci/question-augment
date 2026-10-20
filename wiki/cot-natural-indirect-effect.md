---
description: "The natural indirect effect of a hint through the CoT swaps in the hinted run's CoT with the input fixed; a non-zero effect means a non-verbalized CoT still carries part of the cue's influence."
aliases: ["CoT natural indirect effect", "causal mediation of chain-of-thought", "CoT mediation analysis", "NIE through the CoT"]
sources: ["arxiv-2512-23032"]
---
# CoT natural indirect effect

Causal mediation analysis splits the effect of an intervention on an outcome into a direct path and a path through an intermediate variable. Applied to a CoT, the intervention is a hint added to the input, the outcome is the probability the model assigns to the hinted answer token, and the intermediate variable is the CoT. The total effect of the hint is then split into two terms, each computed by holding one part fixed.[^c1]

The direct effect, the natural direct effect (NDE), holds the CoT fixed and varies only the input: it is the expected difference in the hinted-answer probability when the hinted prompt and the unhinted prompt are paired with the same CoT.[^c2] The indirect effect, the natural indirect effect (NIE), holds the input fixed and substitutes the CoT produced under the hinted input. It is the difference between the probability with the hinted CoT and with the unhinted CoT, both under the unhinted input.[^c3] The NIE is therefore a measure of how much of the prediction change runs through the text the model generated, not through the cue directly.

The reason to use it is that the hint-verbalization test cannot see this path. A CoT can reproduce the hint's effect without the words of the hint. The work reports a non-zero NIE in several settings, which the authors read as "indicating that CoTs generated under hinted inputs have a causal effect even" when the hint is not verbalized.[^c4] The effect also reaches the non-hinted options. Under the Professor hint, CoTs "can influence predictions by suppressing alternative choices, not just by boosting the" hinted one.[^c5] The sign can also flip: for Qwen-3-32B under the Metadata hint, NIE values were "strictly negative", which the authors read as CoTs playing "a suppressive role" in reasoning models when an implicit hint is given.[^c6]

Transferring this formalism from statistics requires care. The mediator here is a sampled string, not a measured quantity, so the NIE depends on which CoT is substituted. It is a whole-text intervention and does not say which sentence carries the effect. What survives the transfer is the decomposition itself: a difference between the total and direct paths, with the CoT as the path. What does not survive is any reading of the NIE as a count of reasoning steps. The standard identification of a mediation effect assumes that no unmeasured variable confounds the CoT and the outcome; the work does not discuss this assumption, and my reading is that it is not verified here.

## Limits

- The outcome is the probability of the hinted token, not whether the answer flips. The paper also reports the summed probability of the non-hinted options, so the two effects are not interchangeable.
- The NDE and NIE are "often similar in magnitude", and "they vary across models and tasks".[^c7] Several confidence intervals include zero; for the Professor hint, "some NDEs are not significantly" different from zero.[^c8]
- Results are for three instruction-tuned models and, in a subset, two larger models. The sign pattern for reasoning models is a single-model observation.
- The NIE does not test whether the CoT is faithful. A CoT can carry a causal effect and still be an incomplete or misleading account of the reasoning; the work argues only that it is not purely post-hoc.

## Related

- [[verbalization-incompleteness-versus-unfaithfulness]] — the claim this decomposition supports: a non-verbalized CoT can still be causal.
- [[cot-mediation-index]] — a different causal audit: activation patching of CoT-token hidden states against matched controls, rather than substitution of whole CoTs.
- [[faithful-at-k-budget-curve]] — a verbalization-based check that the NIE does not depend on.
- [[alpha-gameability-of-faithfulness-metrics]] — a reminder that a faithfulness metric can be scored high without a dependence between explanation and intervention, which an NIE test would also need to rule out.

[^c1]: arxiv-2512-23032 — "total effect into direct and indirect"
[^c2]: arxiv-2512-23032 — "adding a hint to the input, holding the CoT fixed"
[^c3]: arxiv-2512-23032 — "input fixed while substituting in the CoT induced"
[^c4]: arxiv-2512-23032 — "indicating that CoTs generated under hinted inputs have a causal effect even"
[^c5]: arxiv-2512-23032 — "can influence predictions by suppressing alternative choices, not just by boosting the"
[^c6]: arxiv-2512-23032 — "in reasoning models, CoTs may play a suppressive"
[^c7]: arxiv-2512-23032 — "Although NDE and NIE are often similar in magnitude, they vary across models and"
[^c8]: arxiv-2512-23032 — "some NDEs are not significantly"
