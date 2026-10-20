---
description: "Steering a reasoning model only at the first token of each reasoning step, not at every token, stops the edit from compounding and widens the usable strength range."
aliases: ["stepwise steering", "ReflCtrl stepwise steering", "step-level representation steering", "delimiter-gated steering"]
sources: ["arxiv-2512-13979"]
---
# Step-boundary steering

An additive steering intervention can be applied at every decoding position, or only at positions that a structure picks out. The second choice is what the ReflCtrl paper calls stepwise steering. The reasoning trace is cut into steps at the paragraph delimiter, and the offset is added only where "we restrict the perturbation to step-boundary positions, the first token generated after each reasoning step delimiter."[^s1] The offset is the same direction the all-token method would use. What changes is the set of positions where it lands.

The reason the paper gives is about autoregressive generation. A perturbed hidden state feeds later attention, so the shift accumulates: the all-token edit has the effect of "causing the distributional shift to compound across tokens."[^s2] At large strength this pushes the representations away from the training distribution, "limiting the usable intervention range."[^s3] Restricting the edit to step starts leaves the tokens inside each step with their own dynamics. The paper's example gives the scale of the reduction: "a 2000-token trace may contain only 10–20 steps."[^s4] Perturbed positions therefore fall by roughly a hundredfold at that length (my arithmetic, not the paper's).

What was measured is one comparison, on DeepSeek-R1-Distill-Llama-8B with GSM8k. The all-token baseline "degrades significantly at strengths below −0.2 or above +0.3."[^s5] The stepwise version stays near baseline across the same range, and at any fixed reasoning-token count it "consistently outperforms all-token intervention."[^s6] The direction of effect is shared: stepwise steering "maintains the same direction of effect as all-token steering while supporting a substantially wider range" of strength.[^s7] This is the mechanism behind the paper's headline saving, a reduction of reasoning tokens by up to 43.2% at preserved accuracy.

What transfers is the choice of where an additive edit lands in a generated sequence. The gate here is structural, set by a delimiter, and needs no learned probe. That is the contrast with [[gated-activation-steering-for-abstention]], where a probe decides which tokens receive the offset. The same distinction bears on [[pre-committed-answer-before-cot]], which notes that steering at every decoding position, answer tokens included, can make a flip look like an edit to a belief when it is partly direct answer biasing. A region-restricted edit is the remedy that note lists as untested. The step-boundary edit is one such restriction, in a different paper, and it does not test the answer-token case itself. (My inference.)

## Limits

- The head-to-head comparison is a single setting. The paper states that "stepwise steering offers two clear advantages over all-token intervention on DeepSeek-R1-Distill-Llama-8B (GSM8k)."[^s8] The broader tables use other models with the stepwise method alone, not with the all-token baseline.
- The gate is the "\n\n" delimiter. A model or prompt that reasons without paragraph breaks would give few or no boundary positions. This was not tested. (My inference.)
- The paper argues that step starts are the right positions, because the direction is extracted from first-token representations. No other set of positions is compared against step starts, so the choice is argued, not measured against alternatives.
- The reflection direction the method steers is built from steps labelled by keywords: the paper identifies "reflection-related steps via keywords."[^s9] Any error in those labels carries into the direction, and the method's effect is only as good as that direction.
- The accuracy results are averages over runs; the variance is reported in an appendix I did not read. The claim of preserved accuracy should be read with that in mind.
- The method is shown on math and general-reasoning multiple-choice tasks. It is not shown for open-ended answering, where a "step" is harder to delimit.

## Related

- [[mean-difference-steering-vector]] — the all-token baseline this edit restricts; the offset itself is the same kind of object
- [[gated-activation-steering-for-abstention]] — gates the offset by a probe; here the gate is a delimiter
- [[pre-committed-answer-before-cot]] — the answer-token confound that a region-restricted edit would address
- [[reflection-confidence-coupling]] — the reflection direction that stepwise steering acts on

[^s1]: arxiv-2512-13979 — "we restrict the perturbation to step-boundary positions, the first token generated after each reasoning step delimiter"
[^s2]: arxiv-2512-13979 — "causing the distributional shift to compound across tokens"
[^s3]: arxiv-2512-13979 — "limiting the usable intervention range"
[^s4]: arxiv-2512-13979 — "a 2000-token trace may contain only 10–20 steps"
[^s5]: arxiv-2512-13979 — "The all-token baseline degrades significantly at strengths below −0.2 or above +0.3"
[^s6]: arxiv-2512-13979 — "stepwise steering consistently outperforms all-token intervention"
[^s7]: arxiv-2512-13979 — "maintains the same direction of effect as all-token steering"
[^s8]: arxiv-2512-13979 — "stepwise steering offers two clear advantages over all-token intervention on DeepSeek-R1-Distill-Llama-8B (GSM8k)"
[^s9]: arxiv-2512-13979 — "identify reflection-related steps via keywords"
