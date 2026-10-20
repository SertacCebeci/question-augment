---
description: "A rejected answer made fluent and plausible yet contradicted by the evidence, differing from the truth in one targeted error type, so a contrast pair teaches evidence over language priors."
aliases: ["counterfactual hard negatives", "hard negative synthesis", "linguistically plausible rejected response", "contradicting perturbation"]
sources: ["arxiv-2512-24052", "doi-10-48550-arxiv-2506-04585"]
---
# Counterfactual hard negative

A counterfactual hard negative is a wrong answer built on purpose to be hard to tell from the right one by fluency alone. The construction starts from a response taken as correct (for the work here, the ground-truth caption of an audio clip) and edits it toward one named error type. The generator is told to "synthesize counterfactual errors corresponding to the hallucination taxonomy."[^c1] Examples are swapping the order of events, changing a count, or inventing a sound that is not there.[^c2] The result is a response that reads like the chosen one but contradicts the evidence. In the paper's words, these candidates "mimic the linguistic fluency of the chosen response while strictly contradicting the temporal logic of the audio."[^c3]

The selection rule makes the plausibility explicit. Human judges keep the candidate that is "linguistically plausible under caption-only reasoning" yet "clearly incorrect given the acoustic evidence."[^c4][^c5] So the rejected answer is chosen to be the one a reader who only has the caption would accept. That is what makes it hard: it is not a random wrong answer, it is the wrong answer the shortcut produces. The paper names that shortcut. Models "often fall back on language priors, generating responses that are semantically plausible yet acoustically incorrect."[^c6]

The mechanism the authors give is about what a contrast can teach. Positive examples alone are not enough; the model "must learn to distinguish the true acoustic timeline from linguistically plausible but chronologically manipulated alternatives."[^c7] A pair whose two members differ in form but not in plausibility gives the optimiser no reason to prefer the evidence. A pair whose rejected member is plausible but wrong in one named way does. The error type is what makes the negative counterfactual: the edit is known, so the contrast is about one thing.

The paper reports the effect on its own diagnostic set, not as a controlled comparison of negative types. On temporal relation items the error rate of the aligned model fell, "dropping it from 30.5% to 15.9%."[^c8] The paper attributes this to preference optimisation on these pairs. The construction and its training use are one package in that result; the text I read does not separate them.

The same move, one targeted edit away from a true statement, builds labelled negatives for claim verification over scientific figures. The MuSciClaims benchmark takes claims from article results sections and "we create contradictory claims by perturbing these" supporting claims.[^c11] The edits are of named kinds: directional terms are "replaced with their opposites," and numerical values are changed, mostly experiment details "such as statistical significance."[^c13][^c14] The construction is meant to make the evidence that supports the original claim count against the edited one: "Our perturbations ensure that the modified claim is a contradiction of the supported claim."[^c12] The evidence here is a figure rather than an acoustic timeline, so the contrast tests reading of a picture, not of a sound.

## Limits

- The negatives are written by text-only language models from captions, not from the audio. The paper says its pipeline is built "around caption-level representations that serve as a proxy for acoustic input." Whether a negative plausible under the caption is also plausible to a model that hears the sound is not tested.
- The selection of one rejected response per item is done by ten volunteers. I found no agreement figure for that choice in the portion I read; this is my reading, not a result from the paper.
- I found no ablation in the text that compares counterfactual hard negatives with random or unedited negatives. So the paper does not show that the hardness of the negative, rather than the preference signal itself, drives the gain.
- The evaluation view and the training view "share the same underlying audio samples, questions, and hallucination taxonomy."[^c9] The gain on the paper's own diagnostic set is the large one; the gains on public benchmarks are 1.3% on MMAU-Test and 1.6% on MMAR.[^c10] My inference: the negatives teach the error types of this construction, and the public gains may not come from the same mechanism.
- One base model (Qwen2.5-Omni) and one pair-generation pipeline were used. The construction is not shown to work for other models or other error types.
- The figure-claim negatives are written by hand: "we use a manual claim perturbation process."[^c15] Their quality was checked by a second annotation only on part of the data: "For a subset of data, three annotators."[^c16] The 100% agreement the paper reports is over that subset, so the construction's reliability on the rest is not shown.

## Related

- [[audio-temporal-hallucination-taxonomy]] — the four error types that the negatives are generated to instantiate.
- [[controlled-error-injection]] — the same edit-a-correct-answer move, used there to label a test set rather than to form a contrast pair.
- [[coverage-separation-offline-online]] — offline preference methods learn only from the pairs supplied, so the negatives set what they can see.
- [[cot-hallucination-trap]] — the fluent but ungrounded output that these negatives are built to imitate.
- [[distractor-similarity-reasoning-inflation]] — a hard negative placed in the input rather than in the answer; the similarity sits in a different place.
- [[observation-inference-coupling]] — the pair test that a perturbed claim feeds: whether the verdict flips when the edit touches the observation, the inference, or both.
- [[crossed-image-text-edit-families]] — the same contrast logic on image and question, with a fixed gold label per cell.

[^c1]: arxiv-2512-24052 — "synthesize counterfactual errors corresponding to the hallucination taxonomy"
[^c2]: arxiv-2512-24052 — "swap the chronological order of events, modify specific counts, or fabricate"
[^c3]: arxiv-2512-24052 — "they mimic the linguistic fluency of the chosen response while strictly contradicting the temporal logic of the audio"
[^c4]: arxiv-2512-24052 — "Selection criteria prioritize responses that are linguistically plausible under caption-only reasoning"
[^c5]: arxiv-2512-24052 — "yet clearly incorrect given the acoustic evidence"
[^c6]: arxiv-2512-24052 — "often falls back on language priors, generating responses that are semantically plausible"
[^c7]: arxiv-2512-24052 — "distinguish the true acoustic timeline from linguistically plausible but"
[^c8]: arxiv-2512-24052 — "dropping it from 30.5% to 15.9%"
[^c9]: arxiv-2512-24052 — "share the same underlying audio samples, questions, and hallucination taxonomy"
[^c10]: arxiv-2512-24052 — "on MMAU-Test and 1.6% on MMAR, outperforming latest SOTA methods"
[^c11]: doi-10-48550-arxiv-2506-04585 — "we create contradictory claims by perturbing these"
[^c12]: doi-10-48550-arxiv-2506-04585 — "Our perturbations ensure that the modified claim is a contradiction of the supported claim"
[^c13]: doi-10-48550-arxiv-2506-04585 — "Directional terms are replaced with their opposites"
[^c14]: doi-10-48550-arxiv-2506-04585 — "Numerical values, primarily associated with experiment details such as statistical significance"
[^c15]: doi-10-48550-arxiv-2506-04585 — "we use a manual claim perturbation process"
[^c16]: doi-10-48550-arxiv-2506-04585 — "For a subset of data, three annotators"
