---
description: "A learned estimator reads a question's text before any reasoning and predicts a multi-feature difficulty profile, which sets whether to decompose and how many thoughts each step gets."
aliases: ["complexity-aware recursive decomposition", "CARD", "MRCE", "pre-generation difficulty estimation", "multi-dimensional complexity profiling"]
sources: ["arxiv-2601-04210"]
---
# Preemptive complexity estimation

Before any reasoning is generated, a separate estimator reads the question text and returns a profile of its difficulty. In the CARD paper the estimator, MRCE, is a "Qwen3-0.6B base model fine-tuned with LoRA", and it predicts 30 features "from question text".[^c1] The features fall into four groups; the first two are arithmetic structure and "Reasoning depth (vars, entities, estimated_steps)", and the other two are semantic difficulty (trap level, difficulty) and calibrated failure probabilities for 1.5B- and 7B-class models.[^c2] The profile is collapsed into one score, a weighted sum of step count, trap level, difficulty and the 7B failure probability, with weights "0.30, 0.25, 0.25, 0.20".[^c3]

The score is used before generation, in two places. The first is a gate. The algorithm's parameter list sets "tau_dec =3.0", so a question below that score is answered directly; a question above it is split into K steps, with K read from the profile's own estimated-steps field, "K = p_q . estimated_steps".[^c4] The second is a per-step budget. Each sub-step is profiled again "via recursive MRCE profiling", and an easy step gets one thought, a moderate one a count that scales with its score, and a hard one the maximum. The listing sets "tau_high =6.0 , alpha =1.5", and the paper gives the bands as "Easy steps get 1 thought, moderate steps scale linearly (5-9 thoughts)" and "hard steps use exhaustive search (10 thoughts)".[^c5] My reading: the budget is fixed by the predicted profile before the first thought is drawn, not by anything observed during generation. That is the sense of "preemptive" in the paper's title.

What was measured. On GSM8K with Qwen3-1.7B, CARD "hits 89.2% accuracy at 921" tokens, against zero-shot "(87.5%, 1,798 tokens)" and RDoLT, a fixed three-tier decomposition, "(87.9%, 1,987 tokens)".[^c6] Split by predicted score into quartiles, the easiest quartile got "CARD allocates just 367 tokens per problem, achieving 94.2% accuracy", and the hardest got "CARD uses 1,897 tokens, deploying deep recursive decomposition" and reached "achieving 71.2% accuracy versus" the fixed baseline's "68.3% at 2,003 tokens".[^c7] The paper's summary of its comparison with beam search is that "intelligent preemptive allocation beats exhaustive search", with "CARD surpasses this by +1.9 points at nearly half the tokens".[^c8]

The ablation bears on where the difficulty signal comes from. Asking a model to estimate complexity in a prompt "reaches only 77.4% accuracy at 1,287 tokens", and chain-of-thought self-assessment does worse; the authors conclude that "LLMs lack the introspective calibration to self-assess complexity accurately without specialized training."[^c9] Removing the reasoning-depth group loses accuracy and tokens to over-decomposition: "Without these features, CARD cannot predict how many reasoning steps are required". Within the features, the step count matters most: "estimated_steps is most important (10.8 point loss, 1,687 tokens)".[^c10]

What transfers, by my reading and not as a measured result: the split between a cheap estimate of difficulty made before effort, and an effort decision taken from that estimate, both whether to break a question up and how much effort each piece gets. Someone asking or answering could hold that split without the machinery. What does not transfer is the feature set. The 30 features, their weights and the thresholds are arithmetic choices, and the paper says other domains need their own features.

## Limits

The evidence is grade-school and competition math (GSM8K and MATH-500) with three small models, from 0.6B to 1.7B parameters. The paper states that "CARD works well for mathematical reasoning, but other domains" and that they "require domain-specific feature engineering and complexity annotation".[^c11] Commonsense, code and logical inference are not tested.

The weights 0.30, 0.25, 0.25 and 0.20 and the thresholds 3.0 and 6.0 are stated, not derived, and the text I read gives no sensitivity analysis. My inference: a different weighting would move questions across the gate with no change in the features themselves, so the gate's placement is a design choice the results depend on.

The training pairs are described only as "annotated problem-profile pairs to learn".[^c12] The text does not say how the annotations were produced. Whether the profile tracks difficulty or the annotator's judgement of it is therefore open from this text alone.

The quartile table divides questions by the estimator's own score. It shows that the allocation behaves as designed, not that the score matches an independent measure of difficulty; that is my reading of how the table is built.

Each table gives single values, with no spread across seeds or runs. The text is still a draft with venue template text ("Make sure to enter the correct conference title"), so its numbers are preprint numbers.[^c13]

## Related

- [[complexity-tiered-strategy-routing]] — also places a query on a difficulty scale before answering; there one tier is chosen per query from a categorical scale, while CARD gates decomposition and sets a graded budget for each sub-step, recursively.
- [[accuracy-cost-strategy-routing]] — predicts each strategy's accuracy and cost; CARD predicts features of the question and derives the budget from them, not from predicted outcomes.
- [[problem-model-before-reasoning]] — fixes the problem's structure before reasoning; the same move of settling the shape before the effort, here done by the answerer rather than by a trained estimator.
- [[shared-history-prompt-difficulty-prediction]] — also predicts difficulty to steer test-time compute, but from an optimization history rather than from the question text.
- [[test-time-scaling]] — the resource being distributed: the number of sampled thoughts is the compute that a preemptive profile allocates.

[^c1]: arxiv-2601-04210 — "Qwen3-0.6B base model fine-tuned with LoRA"
[^c2]: arxiv-2601-04210 — "breaks down into four groups: Arithmetic structure, Reasoning depth (vars, entities, estimated_steps)"
[^c3]: arxiv-2601-04210 — "0.30, 0.25, 0.25, 0.20"
[^c4]: arxiv-2601-04210 — "Params : tau_dec =3.0"
[^c5]: arxiv-2601-04210 — "Easy steps get 1 thought, moderate steps scale linearly (5-9 thoughts)"
[^c6]: arxiv-2601-04210 — "hits 89.2% accuracy at 921"
[^c7]: arxiv-2601-04210 — "CARD allocates just 367 tokens per problem, achieving 94.2% accuracy"
[^c8]: arxiv-2601-04210 — "intelligent preemptive allocation beats exhaustive search"
[^c9]: arxiv-2601-04210 — "LLMs lack the introspective calibration to self-assess complexity accurately without specialized training."
[^c10]: arxiv-2601-04210 — "estimated_steps is most important (10.8 point loss, 1,687 tokens)"
[^c11]: arxiv-2601-04210 — "require domain-specific feature engineering and complexity annotation"
[^c12]: arxiv-2601-04210 — "annotated problem-profile pairs to learn"
[^c13]: arxiv-2601-04210 — "Make sure to enter the correct conference title"
