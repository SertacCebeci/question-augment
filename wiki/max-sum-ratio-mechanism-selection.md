---
description: "A max-sum ratio of trigger-to-trigger distances in pretraining data selects whether a shallow transformer learns an induction head or a positional shortcut that fails out of distribution."
aliases: ["max-sum ratio", "trigger-distance diversity", "induction head versus positional shortcut"]
sources: ["arxiv-2512-18634"]
---
# Max-sum ratio mechanism selection

The task is a trigger-output copy. A sequence contains a special trigger token twice, and the model must output the token that follows the first trigger when the trigger appears the second time.[^c1] Two mechanisms solve it on the training data. An induction head "attends back to the location of the previous trigger and copies the token" after it, so it works for arbitrarily long gaps between triggers.[^c2] A positional shortcut instead copies by position: when the first trigger's location can be read off the second, the model answers from position alone. That shortcut is "valid in-distribution but does not reflect the underlying association."[^c3] It is a specific case of the wider reliance on a cue that predicts the answer in training ([[clever-hans-effect]]).

The paper's claim is that the pretraining distribution, not the architecture alone, decides between the two: "the pretraining distribution directly selects the model’s algorithm."[^c4] The quantity doing the selecting is the max-sum ratio of the distribution over the length of irrelevant tokens between triggers. It is the largest mass-weighted inverse length, max over ℓ of ℓ⁻¹q_ℓ, divided by the sum of all mass-weighted inverse lengths, Σ_ℓ ℓ⁻¹q_ℓ.[^c5] The paper's reading of the threshold is that low diversity gives the shortcut: "is low, the model adopts a positional shortcut that fails to generalize OOD."[^c6]

In the infinite-data (population loss) setting the paper proves a two-sided threshold. If the ratio is below a constant ε1, "then the pretrained transformer generalizes OOD, as defined in Definition 2." If it is above a second constant ε2, "there exist OOD test sequences such that the pretrained transformer fails."[^c7][^c8] A finite-sample version "establishes (via gradient concentration) similar transition behavior in the finite-sample setting."[^c22]

The mechanism behind the ratio is a competition inside the attention weights. The positional term is at most its largest single mass term, while the induction term sums over all lengths.[^c9] Their ratio is the max-sum ratio: "of positional memory and the induction head is nothing but the max-sum ratio."[^c10] Read this way, diversity works by spreading the trigger distances, "by varying the distances between trigger occurrences," which weakens the positional signal the shortcut needs.[^c11]

The ratio is not a measure of width alone. For a uniform distribution over K consecutive lengths starting at ℓ0, the ratio falls as K grows, "hence greater diversity of Dℓ gives smaller max-sum ratio."[^c12] Shifting the same kind of range to larger lengths also lowers it: "even with a narrow range, shifting the distribution rightward" yields a smaller ratio, because the measure weights each mass by the inverse length.[^c13] The threshold itself shrinks with the number of triggers in the sequence; "the number of possible triggers makes OOD generalization more difficult."[^c14]

The shortcut is invisible in training when the training data have equal irrelevant-token lengths before the two triggers. The paper notes that "the training data only contain sequences with" that equal structure, and in that setting a positional shortcut "can still achieve 100% training accuracy."[^c15][^c16] Only out-of-distribution test sequences with unequal lengths separate the two mechanisms.

For cost, the paper's example says widening the length range is a weak lever: "may not be efficient to reduce the max-sum ratio," and "biasing pretraining toward longer contexts is substantially more effective."[^c17] The price is that the induction head "may incur greater computational cost due to longer training sequences."[^c18]

## Limits

- The theory covers a single-layer transformer on a synthetic copy task, analysed under an early-phase simplification of gradient descent: "a shallow (single-layer) transformer trained on this synthetic task."[^c19] The threshold is therefore a statement about the early phase of this model, not about training to convergence.
- The validation is controlled and synthetic: "we validate our theoretical predictions with controlled synthetic experiments."[^c20] The paper does not measure the ratio on natural corpora.
- The transfer beyond the setting is offered as evidence, not a theorem: the paper says it presents evidence that a similar transition arises "under standard gradient-based training beyond our theoretical setting."[^c21] No language-model experiment in this note checks the ratio.
- The threshold is characterised only in order: "We also provide a tight" Θ(N_trg⁻¹) bound on the ratio threshold.[^c23] The text gives no numeric value for the threshold a real corpus would have to clear (my reading).
- The ratio is defined on the length distribution of one fixed irrelevant-token structure. Whether natural text has a comparable quantity, or whether it bears on which mechanism an LLM uses, is my inference and is not tested here.

## Related

- [[clever-hans-effect]] — the general reliance on a training-correlated cue; this note gives one measured criterion for when a positional cue, rather than the content feature, is the one learned
- [[ood-confounded-removal-evaluation]] — another case where an out-of-distribution check misleads; here the test that separates the mechanisms is one that varies the gap structure the shortcut depends on

[^c1]: arxiv-2512-18634 — "The model must predict the token that immediately follows the"
[^c2]: arxiv-2512-18634 — "The model attends back to the location of the previous trigger and copies the token"
[^c3]: arxiv-2512-18634 — "valid in-distribution but does not reflect the underlying association"
[^c4]: arxiv-2512-18634 — "the pretraining distribution directly selects the model’s algorithm"
[^c5]: arxiv-2512-18634 — "We define the max-sum ratio as"
[^c6]: arxiv-2512-18634 — "is low, the model adopts a positional shortcut that fails to generalize OOD"
[^c7]: arxiv-2512-18634 — "then the pretrained transformer generalizes OOD, as defined in Definition 2"
[^c8]: arxiv-2512-18634 — "there exist OOD test sequences such that the pretrained transformer fails"
[^c9]: arxiv-2512-18634 — "the magnitude of the former is at most"
[^c10]: arxiv-2512-18634 — "of positional memory and the induction head is nothing but the max-sum ratio"
[^c11]: arxiv-2512-18634 — "by varying the distances between trigger occurrences"
[^c12]: arxiv-2512-18634 — "hence greater diversity of Dℓ gives smaller max-sum ratio"
[^c13]: arxiv-2512-18634 — "even with a narrow range, shifting the distribution rightward"
[^c14]: arxiv-2512-18634 — "the number of possible triggers makes OOD generalization more difficult"
[^c15]: arxiv-2512-18634 — "the training data only contain sequences with"
[^c16]: arxiv-2512-18634 — "can still achieve 100% training accuracy"
[^c17]: arxiv-2512-18634 — "may not be efficient to reduce the max-sum ratio"
[^c18]: arxiv-2512-18634 — "may incur greater computational cost due to longer training sequences"
[^c19]: arxiv-2512-18634 — "a shallow (single-layer) transformer trained on this synthetic task"
[^c20]: arxiv-2512-18634 — "we validate our theoretical predictions with controlled synthetic experiments"
[^c21]: arxiv-2512-18634 — "arises under standard gradient-based training beyond our theoretical setting"
[^c22]: arxiv-2512-18634 — "establishes (via gradient concentration) similar transition behavior in the finite-sample setting"
[^c23]: arxiv-2512-18634 — "We also provide a tight"
