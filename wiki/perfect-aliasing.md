---
description: "A probe fitted where truth and the prescribed action coincide cannot tell them apart; on rival contexts their AUROCs must sum to one, so an inverted truth probe may be an action probe."
aliases: ["semantic identification failure", "complete-agreement aliasing", "truth-action label aliasing"]
sources: ["doi-10-48550-arxiv-2609-10739"]
---
# Perfect aliasing

Consider a probe fitted on trials where two candidate targets agree on every example. The fitting objective then receives the same supervision under either reading, so the labels cannot say which target the fitted score measures. The paper calls this perfect aliasing, the complete-agreement limit of label agreement.[^c1]

In a controlled binary reporting game the two targets are the truth, the ground-truth bit stated in the system prompt, and the prescribed action, the answer the task asks for. On ally trials these coincide, so a truth probe and an action probe fitted on ally data solve the same optimization.[^c2] On rival trials the prescribed action is the complement of the truth.[^c3] A score aligned with the prescribed label therefore reads the truth backwards, which means a below-chance ally-fit readout cannot, by itself, show that truth information was removed.

The consequence is an identity rather than a correlation. One fitted direction scored against two complementary labels yields AUROCs that sum to one, because AUROC is antisymmetric under label negation. The paper checks the identity at every recorded layer of every cell and reports that it holds across 751 cell-layer pairs.[^c4] Its own framing is that this is a check that the pipeline computes what is intended, not a finding about the model.[^c5] The practical upshot: a below-chance ally-fit "truth" AUROC is numerically the same as an above-chance prescribed-action AUROC, and the protocol gives no way to tell which one was measured.[^c6]

The empirical case is a reward-trained Gemma-2-9B policy that answers falsely on all evaluated rival trials. Its conventional ally-fit probe scores 0.006 ± 0.005 AUROC across three training seeds, while a probe fitted on mixed ally and rival contexts scores 1.000 on the same held-out activations.[^c7][^c8] The paper's reading is that a sub-chance readout is not evidence of lost truth: the true bit remains linearly recoverable under a different fitting distribution.[^c9][^c10]

## What breaks the alias

The paper makes two changes, each removing a different equality. A randomized codebook gives every trial a fresh symbol pair and orientation, so which character denotes the prescribed answer changes trial to trial and the emitted surface symbol no longer fixes the action.[^c11] Fitting on mixed ally and rival contexts then gives the probe labelled examples on which truth and action differ. In the headline cell the mixed-fit probe reaches 1.000 by layer 4 and holds it to the final layer.[^c12] The paper's prescription follows: decorrelate the prescribed output from the semantic action, or "no probe fit on compliant behaviour can be identified" at all.[^c13]

The alias is a property of the labels and the fit, not of how often the policy lies. Saturation does not predict inversion: "an arm at deception exactly 1.000 does not invert, while another at lower" deception does.[^c14]

## Limits

- The identity fixes what the labels cannot decide. It does not say which interpretation an optimizer selects, nor what a fitted score measures outside its fitting support.[^c15]
- Label equality does not prove that two distinct directions exist, nor rule out a unique regularized optimum; it shows only that the labels cannot choose between the two targets.[^c16]
- The mixed-fit comparison changes two things at once: more training examples and access to labelled rival contexts. It establishes linear recoverability, "rather than isolating the benefit of decorrelation."[^c17]
- One game with a single-token answer. "All results come from a single secret-bit game with a single-token" answer.[^c18] Whether the same structure appears in long-form deception "is untested, and is the obvious next experiment."[^c19]
- The bit is stated in the prompt and the probe reads the final prompt position. A direction recovering it "may be decoding a retained copy of the input rather than anything the" policy computed.[^c20] The paper's inferred-truth control narrows this concern but does not remove it, and recovery at the answer position does not establish preserved belief or causal use. "Decodability is not causal use."[^c21]
- Saturation is one family in four. "Three of four families never reached it."[^c22]

## Related

- [[correctness-probe-transfer-needs-joint-training]] — there a below-chance probe is read as a direction present but pointed elsewhere; the alias is one candidate for how a fitted direction ends up with the wrong sign (my inference, not the paper's claim).
- [[frozen-probe-cross-scoring]] — the paper's other identification failure: refitting a probe per condition moves rival AUROC over a wide range, where one frozen direction scored on the same conditions does not.
- [[cross-model-domain-adaptation-probe]] — adapts a source probe to new models without target labels; what such adaptation can identify depends on which label set the source probe was fitted on (my inference).

[^c1]: doi-10-48550-arxiv-2609-10739 — "We call this perfect aliasing, the complete-agreement"
[^c2]: doi-10-48550-arxiv-2609-10739 — "Our ground-truth and prescribed-action labels coincide on every"
[^c3]: doi-10-48550-arxiv-2609-10739 — "the prescribed-action label is the complement of truth; a score aligned with that prescribed label will"
[^c4]: doi-10-48550-arxiv-2609-10739 — "this identity holds across 751 cell-layer pairs to floating-point"
[^c5]: doi-10-48550-arxiv-2609-10739 — "This is not a correlation to interpret; it is a proof, and the measurement only checks that our pipeline"
[^c6]: doi-10-48550-arxiv-2609-10739 — "the protocol offers no way to tell which they measured."
[^c7]: doi-10-48550-arxiv-2609-10739 — "answers falsely on all evaluated rival trials, the conventional probe scores 0.006 ±"
[^c8]: doi-10-48550-arxiv-2609-10739 — "while mixed-fit probes score 1.000"
[^c9]: doi-10-48550-arxiv-2609-10739 — "A below-chance readout alone does not establish loss of truth information."
[^c10]: doi-10-48550-arxiv-2609-10739 — "true bit remains linearly recoverable under a different fitting distribution."
[^c11]: doi-10-48550-arxiv-2609-10739 — "each trial draws a fresh symbol pair and a random orientation"
[^c12]: doi-10-48550-arxiv-2609-10739 — "the mixed-fit probe reaches 1.000 by layer 4 and holds it"
[^c13]: doi-10-48550-arxiv-2609-10739 — "Otherwise no probe fit on compliant behaviour can be identified"
[^c14]: doi-10-48550-arxiv-2609-10739 — "an arm at deception exactly 1.000 does not invert, while another at lower"
[^c15]: doi-10-48550-arxiv-2609-10739 — "The argument does not determine which interpretation best describes a particular fit outside its"
[^c16]: doi-10-48550-arxiv-2609-10739 — "the existence of two distinct linear directions, nor preclude a numerically unique regularized optimum."
[^c17]: doi-10-48550-arxiv-2609-10739 — "rather than isolating the benefit of decorrelation."
[^c18]: doi-10-48550-arxiv-2609-10739 — "All results come from a single secret-bit game with a single-token"
[^c19]: doi-10-48550-arxiv-2609-10739 — "appears in long-form deception is untested, and is the obvious next experiment."
[^c20]: doi-10-48550-arxiv-2609-10739 — "a direction recovering it at AUROC 1.000 may be decoding a retained copy of the input rather than anything the"
[^c21]: doi-10-48550-arxiv-2609-10739 — "Decodability is not causal use."
[^c22]: doi-10-48550-arxiv-2609-10739 — "Three of four families never reached it."
