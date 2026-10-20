---
description: "Under group-normalized RL with a noisy binary verifier, the sign of Youden's J = TPR - FPR decides whether accuracy rises or collapses; noise level mostly sets speed, not endpoint."
aliases: ["rate not fate", "Youden's J phase transition in RLVR", "noisy verifiable rewards threshold"]
sources: ["arxiv-2601-04411"]
---
# Youden-index threshold for noisy-reward learning

A binary verifier that grades model answers can be wrong in two ways: it passes bad answers (false positives) or fails good ones (false negatives). The paper models these as flip rates and compresses them into one scalar, Youden's index J = 1 - FN rate - FP rate = TPR - FPR.[^c1] J = 1 is a perfect grader, J = 0 a chance-level one, and J < 0 an inverted one.[^c2]

## What the analysis says

For group-normalized policy gradient (GRPO/REINFORCE), the paper coarse-grains completions into reasoning modes and derives a mean-field drift for the total bad-mode mass. Its sign depends only on the sign of J, which gives two predictions. First, a phase transition at J = 0: accuracy improves only for J > 0, drifts neutrally at J = 0, and degrades for J < 0 as the system anti-learns. Second, "rate, not fate": for any J > 0, noise changes convergence speed but not the basin of attraction.[^c3]

In the authors' summary, when J > 0 the bad-mode mass falls monotonically, and when J < 0 the direction flips and performance collapses.[^c4] A KL penalty toward a reference policy replaces boundary collapse with a unique interior equilibrium, which smooths the transition. It does not turn a misleading verifier into a useful one.[^c5]

## What was measured

Experiments used Python code generation with unit-test verification on Qwen2.5-3B, with noise injected at fixed rates. Even a heavily degraded signal at J = 0.3 still enabled learning, only more slowly. At fixed J = 0.3, FPR 0 with FNR 0.70 reached 15.98%, against 14.64% for FPR 0.70 with FNR 0; so false negatives were more tolerable than false positives in that regime.[^c6] The theory attributes this to different tail rates, O(t^-2) when FN = 0 and O(t^-1) when FN > 0.[^c6]

## For asking and answering

The result bears on any pipeline that trains or selects answers by a checker. Whether the checker is better than chance, in the net sense TPR > FPR, matters more than its raw error rate. If J is at or below zero, more compute is not a fix; the paper's practical advice is to estimate J early.[^c7] This conclusion is the authors' reading of their theory.

## Limits

- Experiments cover one task family (Python coding), one 3B model, and fixed noise rates; the authors say time-varying noise from co-evolving policy and reward model is not investigated.[^c8]
- Generalization to math, LLM-as-judge settings and larger models is stated as expected but not tested.[^c8]
- The test suite itself is imperfect, so estimated TPR and FPR are biased, and truncated rollouts scored zero add false negatives that may explain mismatches in the J < 0 regime.[^c9]
- The theory is a mean-field, small-step bandit abstraction; real sequence-level policies are not a few discrete arms.
- The FP-versus-FN asymmetry rests on one matched pair of settings.

## Related

- [[generative-verification]] — verifiers whose reliability is the J that sets this threshold
- [[verification-weighted-voting]] — another way a verifier's quality enters answer selection
- [[solve-verify-detection-gap]] — verifier discrimination versus solving ability

[^c1]: arxiv-2601-04411 — "J := 1 − δFN − δFP = TPR − FPR1 ∈ [−1, 1]."
[^c2]: arxiv-2601-04411 — "J < 0: Inverted or anti-informative rewarder."
[^c3]: arxiv-2601-04411 — "Noise level affects only the convergence rate, more rollouts or training steps accelerate progress toward the same equilibrium without changing the asymptotic outcome."
[^c4]: arxiv-2601-04411 — "noise primarily reduces the speed of progress rather than changing the eventual basin of attraction"
[^c5]: arxiv-2601-04411 — "but it cannot turn a net-misleading verifier into a learning signal."
[^c6]: arxiv-2601-04411 — "This supports the theoretical investigation that convergence rate is O(t−2 ) if FN = 0 vs. O(t−1 ) for FN > 0."
[^c7]: arxiv-2601-04411 — "If J ≤ 0, scaling RL compute will not fix the problem"
[^c8]: arxiv-2601-04411 — "our experiments employ fixed noise rates."
[^c9]: arxiv-2601-04411 — "incomplete tests introduce systematic bias in estimated (TPR, FPR), particularly for edge cases."
