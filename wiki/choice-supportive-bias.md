---
description: "Choice-supportive bias: an LLM's tendency to credit its chosen option with more positive and its rejected option with more negative attributes, measured as a chosen-rejected gap."
aliases: ["choice-supportive bias", "CSB", "choice-supportive bias in LLMs"]
sources: ["arxiv-2512-03082"]
---
# Choice-supportive bias

Choice-supportive bias (CSB) is the systematic attribution of positive traits to the option a reasoner chose and negative traits to the options it rejected. The authors take it as a human bias that "originates in human cognitive architecture",[^c1] and define it as the tendency "to retroactively attribute more positive qualities to chosen options and more negative qualities to rejected ones".[^c2] In a language model the same pattern is a shift in later evaluation: once an option has been picked, the model's assessment of that option drifts toward the pick. The authors stress that it is context-dependent, which separates it from fixed demographic biases: "CSB is context-dependent: it favors whatever option was chosen, regardless of its inherent qualities."[^c3]

The proposed mechanism is an attention pattern, not a stored opinion. The authors describe models that "over-attend to whether an option was chosen while under-utilizing available facts".[^c4] They place the source in training data: "LLMs learn spurious correlations from training data where positive justifications consistently accompany chosen options."[^c5] On this account the model learns an association between choice status and evaluation valence, and the bias follows that association rather than the option's features. This is the authors' hypothesis. The reported experiments measure outcomes, not the mechanism, so the account is supported by plausibility rather than by a test that isolates it. My reading is that it predicts the bias should track the decision context, since the association is learned per context.

The bias is measured as a chosen-versus-rejected gap under two protocols, both replicated from an earlier study.[^c6] In the memory protocol, the gap is a difference in attribution accuracy: the measure "quantifies memory fidelity disparities using normalized accuracy differences" between chosen and rejected options. In the evaluation protocol, a forced choice comes first, then neutral features are evaluated and scored on a tendency scale "(-5 to +5)".[^c7] For gpt-4o-mini the baseline memory gap is large: "the baseline exhibited a mean accuracy gap for seen features of 0.321".[^c8] In the evaluation protocol the same model shows "a 4.3-point score gap between chosen (1.76) and rejected (-2.54) options".[^c9]

## Limits

- The measured quantity is a gap, and the gap alone does not separate bias from a real difference in the features. The protocol randomizes feature order and inserts distractors to control this, "Feature order randomization and distractor insertion follow the original implementation".[^c10] Whether those controls are sufficient is my inference, not something the paper tests.
- The evaluation scorer is a model from the same family as the models under test: the evaluation agent is "retained as GPT-4o for scoring consistency".[^c11] A scorer that shares the model's habits could share its bias.
- The headline reductions are reported two ways. The abstract gives "a 81.5% improvement in memorybased experiments",[^c12] while the introduction says RDG "reduces CSB-driven attribution errors by 83.7%".[^c13] These are different summaries of the same experiments, and the text does not reconcile them.
- The data are simulated. The authors concede that "our synthetic training data simplifies real-world decision scenarios where choices lack explicitly enumerated features."[^c14] The clinical and financial settings cited as motivation are not tested here.
- Coverage is narrow: four models, "with 50 trials per model",[^c15] and a single prior protocol. Whether the gap appears in other model families, or grows with the number of options, is not measured.

## Related

- [[choice-blindness-in-preference-labels]] — a different failure of tracking choice: there the evaluator misses that a choice label was swapped; here the model over-credits the choice it already made.
- [[belief-entrenchment]] — a prior state predicting later updates; CSB is one way a prior selection could steer a later evaluation. This pairing is my reading, not the paper's.

[^c1]: arxiv-2512-03082 — "originates in human cognitive architecture"
[^c2]: arxiv-2512-03082 — "the tendency to retroactively attribute more positive qualities to chosen options and more negative qualities to rejected ones"
[^c3]: arxiv-2512-03082 — "CSB is context-dependent: it favors whatever option was chosen, regardless of its inherent qualities"
[^c4]: arxiv-2512-03082 — "over-attending to whether an option was chosen while under-utilizing available facts"
[^c5]: arxiv-2512-03082 — "LLMs learn spurious correlations from training data where positive justifications consistently accompany chosen options"
[^c6]: arxiv-2512-03082 — "We replicate the memory-based protocol and metrics from (Zhuang et al., 2025)"
[^c7]: arxiv-2512-03082 — "using the original Tendency Score metric (-5 to +5)"
[^c8]: arxiv-2512-03082 — "the baseline exhibited a mean accuracy gap for seen features of 0.321"
[^c9]: arxiv-2512-03082 — "baseline GPT-4o-mini exhibited a 4.3-point score gap between chosen (1.76) and rejected (-2.54) options"
[^c10]: arxiv-2512-03082 — "Feature order randomization and distractor insertion follow the original implementation"
[^c11]: arxiv-2512-03082 — "the evaluation agent (retained as GPT-4o for scoring consistency)"
[^c12]: arxiv-2512-03082 — "a 81.5% improvement in memorybased experiments"
[^c13]: arxiv-2512-03082 — "reduces CSB-driven attribution errors by 83.7%"
[^c14]: arxiv-2512-03082 — "our synthetic training data simplifies real-world decision scenarios where choices lack explicitly enumerated features"
[^c15]: arxiv-2512-03082 — "with 50 trials per model to match the prior work"
