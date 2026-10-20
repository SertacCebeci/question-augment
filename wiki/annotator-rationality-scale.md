---
description: "A rater's rationality scales the reward gap in a pairwise preference model; near zero the label is close to noise, at or below zero it can favour the worse answer."
aliases: ["rationality scale", "scale heterogeneity model", "annotator sharpness parameter", "heterogeneous rationality in preference labels", "teacher rationality scale"]
sources: ["arxiv-2512-03208"]
---
# Annotator rationality scale

A pairwise preference label is usually modeled as a logistic choice on the reward gap: the probability that a rater prefers answer 1 over answer 0 is a logistic function of the difference in their latent rewards. The rationality-scale model keeps that form and multiplies the gap by a scale that depends on the rater's context $x$. The choice probability becomes a logistic function of $\sigma(x)\,[r(s,a^{(1)}) - r(s,a^{(0)})]$. The noise is taken as Gumbel, and the difference of two independent Gumbel variables with a common scale is logistic, which is why the logistic form appears.[^r1] The scale is the rater's sharpness: "The value of σγ∗ (x) reflects the rationality or expertise of the teacher."[^r2]

The sign matters as much as the size. A positive scale means the rater tends to pick the answer with the higher true reward. A scale at or below zero is read as a rater who is non-expert or adversarial: "the teacher exhibits non-expert or even adversarial behavior, potentially preferring" lower-reward responses.[^r3] So the same pair of answers carries different evidence about the reward depending on who labelled it. A scale near zero makes the label close to a coin flip; a negative one makes it point the wrong way. Setting the scale identically to one recovers the homogeneous case, "a homogeneous preference BTL setting (Ouyang et al., 2022)."[^r4]

The scale is learned, not fixed. The paper writes it as $\sigma(x) = \psi_0(x) + \gamma^\top \psi(x)$ with known features and an unknown $\gamma$, and requires $\psi_0$ not to vanish identically: this condition "is essential for the identifiability of" both $\gamma$ and the reward parameter $\theta$.[^r5] Fitting $\theta$ and $\gamma$ jointly by maximum likelihood is nonconvex. The paper's Lemma 1 gives a biconvex structure instead: the loss is "convex in θ when γ is fixed, and convex in γ when θ is fixed," though not jointly convex.[^r6] This is why the fit alternates between the two blocks.

The scale also changes the uncertainty of the learned reward. The variance of the reward estimator is not only the inverse information for $\theta$. Relative to the homogeneous model, "the reward estimator includes an additional adjustment term" that corrects for the scale, and this term "which accounts for heterogeneity in human preferences captured by γ" is part of the variance the paper uses for confidence intervals.[^r7][^r8] A reward interval built as if every rater were equally sharp is therefore not the interval the paper derives.

## Limits

- The scale is a function of observed context $x$ only. A rater's sharpness that $x$ does not capture is outside the model; the paper's heterogeneity is heterogeneity in $x$, not in an unobserved annotator identity (my reading of Assumption 2).
- Identifiability needs $\psi_0 \not\equiv 0$, and the convergence and inference results need the bounded-parameter and weak-coupling conditions. "Assumption 4 controls the interaction strength between ψ(x) and z."[^r9] Whether those hold for a given LLM preference dataset is a check the paper's theorems leave to the reader (my reading).
- The noise family is assumed to be Gumbel, giving the logistic link. I did not see a test under other noise families in the portion read.
- The paper says irrational labels "exist in real-world datasets," and cites other work for that; it does not measure how often a fitted scale comes out negative in the data read.
- The asymptotic results are large-sample statements; Theorem 2 needs the iteration count to grow with $n$. Finite-sample behaviour is not shown in the part read.
- The empirical section (Section 6) was not read in this pass, so no claim here rests on its numbers.

## Related

- [[rater-effects-latent-score-model]] — the rating-scale analogue: a strictness offset and a reliability variance per rater for numeric scores. Here the rater's effect is a multiplicative sharpness on pairwise choices. Both down-weight unreliable raters, but by different parameters.
- [[choice-blindness-in-preference-labels]] — corrupted preference labels; a negative scale is a structured case in which a rater's labels track the reward backwards.
- [[dawid-skene-annotator-model]] — per-annotator reliability inferred without ground truth; the scale is a context-dependent reliability for pairwise labels.
- [[pessimistic-lower-bound-selection]] — uses the variance this scale feeds into to bound each candidate's reward from below before best-of-N selection.

[^r1]: arxiv-2512-03208 — "Gumbel random variables with the same scale parameter follows the logistic distribution"
[^r2]: arxiv-2512-03208 — "The value of σγ∗ (x) reflects the rationality or expertise of the teacher."
[^r3]: arxiv-2512-03208 — "the teacher exhibits non-expert or even adversarial behavior, potentially preferring"
[^r4]: arxiv-2512-03208 — "to a homogeneous preference BTL setting (Ouyang et al., 2022)."
[^r5]: arxiv-2512-03208 — "is essential for the identifiability of"
[^r6]: arxiv-2512-03208 — "convex in θ when γ is fixed, and convex in γ when θ is fixed."
[^r7]: arxiv-2512-03208 — "which accounts for heterogeneity in human preferences captured by γ"
[^r8]: arxiv-2512-03208 — "the reward estimator includes an additional adjustment term"
[^r9]: arxiv-2512-03208 — "Assumption 4 controls the interaction strength between ψ(x) and z."
