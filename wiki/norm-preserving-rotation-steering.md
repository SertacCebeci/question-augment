---
description: "Steering a hidden state by removing its component along a fixed direction and rescaling to the original norm needs no tuned strength, unlike additive steering that adds a scaled vector."
aliases: ["norm-preserving steering", "orthogonal activation rotation", "norm-preserving activation rotation"]
sources: ["arxiv-2512-24574"]
---
# Norm-preserving rotation steering

Additive activation steering writes the edited state as x' = x + α v, where v is a steering direction and α a strength that must be tuned. The rule in the CREST paper is different in form. After each reasoning step, the representation of the last token is changed "to enforce orthogonality with the pre-computed steering direction, while preserving the original activation magnitude."[^c1] Concretely, the component of x along v is removed and the remainder is scaled back to the norm of x, with the paper using the ℓ2 norm.[^c2]

The stated reason for this form is to remove the strength parameter. "Previous steering methods require tuning the steering strength for each model",[^c3] and the paper's answer is that "by preserving the activation norm, we avoid the need for such tuning."[^c4] A second motive is activation outliers, which "are a well-known issue in LLMs, often leading to highly unstable activation magnitudes". The authors argue that "Our norm-preserving strategy mitigates this problem by preventing large norm fluctuations during inference."[^c5]

What the rule does, mechanically, is narrower than "orthogonal steering" suggests. The direction v is not an arbitrary vector: it is the head-specific mean activation over non-linear steps, after projection onto a shared low-rank subspace, since the raw vector "inevitably carries noise". The projection is motivated by the observation that "the signal-to-noise ratio of the raw head vector is low", and the paper therefore adopts "a shared subspace to filter out the" noise components.[^c6] The rule then acts on the state the model already has: at each step boundary the component along v is set to zero, and the rest is rescaled.

The rescaling is the part that is easy to misread. Removing the component along v shrinks the norm, and the rescale restores it, so every component orthogonal to v is multiplied by the same factor greater than or equal to one. The state is not left unchanged off the direction; only its total length is held fixed. (My inference from the stated formula; the paper does not analyse this factor.)

The rule was used with a calibration on MATH500 and applied elsewhere. The paper reports that "Despite being calibrated only on MATH500, CREST generalizes effectively to both in-domain and out-of-domain tasks," and the abstract gives the headline pair: "CREST improves accuracy by up to 17.5% while reducing token usage by 37.6%."[^c7] The gains are attributed by the authors to "the intrinsic redundancy in chain-of-thought reasoning", which is an interpretation rather than a measured quantity in the parts I read.[^c8]

## Limits

- The no-tuning claim is a design argument plus a statement about prior methods. In the slices read there is no head-to-head comparison with an additive variant at a tuned α, so the size of the benefit over tuned additive steering is not shown here.
- A parameter remains. The paper says: "In CREST, the only hyperparameter is the number of attention heads to steer."[^c9] That count is chosen by ablation on R1-1.5B and R1-7B for AIME22–24, so "no tuning" means no strength tuning, not no tuning.
- The norm-stability motive is argued, not measured in the parts I read. No norm statistics before and after the rule are reported in those parts.
- Failure modes remain. "these failures typically involve repetitive outputs", and the authors write that "CREST could be further enhanced by incorporating early-exit strategies to mitigate repetition."[^c10] The rule does not address repetition.
- The overhead claim, "the test-time steering incurs negligible overhead", is the authors' own.[^c11] I did not check throughput numbers.
- The result is tested on distilled and some larger reasoning models and on a fixed benchmark set; it is not shown for a model where the calibration direction was built differently.

## Related

- [[cognitive-heads]] — the heads on which this rule is applied, and the step labels that define the direction v
- [[gated-activation-steering-for-abstention]] — the contrasting form: additive, scaled to the layer's mean residual norm, and applied only at tokens a probe gates on
- [[detection-correction-gap]] — a probe-direction steering that did not correct outputs; this rule was not tested on that setting

[^c1]: arxiv-2512-24574 — "to enforce orthogonality with the pre-computed steering direction, while preserving the original"
[^c2]: arxiv-2512-24574 — "We use ℓ2 norm here."
[^c3]: arxiv-2512-24574 — "Previous steering methods require tuning the steering strength for each model"
[^c4]: arxiv-2512-24574 — "by preserving the activation norm, we avoid the need for such tuning"
[^c5]: arxiv-2512-24574 — "Our norm-preserving strategy mitigates this problem by preventing large norm fluctuations during inference"
[^c6]: arxiv-2512-24574 — "we adopt a shared subspace to filter out the"
[^c7]: arxiv-2512-24574 — "CREST improves accuracy by up to 17.5% while reducing token usage by 37.6%"
[^c8]: arxiv-2512-24574 — "The performance gains of CREST can be largely attributed to the intrinsic redundancy in"
[^c9]: arxiv-2512-24574 — "In CREST, the only hyperparameter is the number of attention heads to steer."
[^c10]: arxiv-2512-24574 — "these failures typically involve"
[^c11]: arxiv-2512-24574 — "the test-time steering incurs negligible overhead"
