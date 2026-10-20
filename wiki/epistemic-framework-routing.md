---
description: "Classify a question into one mutually exclusive reasoning framework (frequentist vs Bayesian) before solving; hard selection matched soft mixing at 7x speed, since blended answers are incoherent."
aliases: ["universe routing", "belief space routing", "epistemic control layer", "reasoning-framework selection"]
sources: ["arxiv-2603-14799"]
---
# Epistemic framework routing

Some questions look alike on the surface but belong to different reasoning frameworks. "Is this coin fair (alpha = 0.05)?" calls for frequentist testing. "Given a uniform prior, what is P(theta > 0.6 | 60 heads)?" calls for Bayesian inference.[^c1] Wang calls each framework a "belief space universe": a tuple of axioms, an inference procedure and a solver. Two universes are epistemically incompatible if an axiom of one is equivalent to the negation of an axiom of the other.[^c2] The routing problem is to predict the single most probable universe for the question, then call that universe's solver.[^c3]

## Why selection, not mixing

The paper's Proposition 1 (given only as a proof sketch) says any convex combination of the outputs of two incompatible solvers lies in the validity domain of neither universe.[^c4] The author's argument is that a 60/40 blend of a frequentist and a Bayesian answer is an incoherence, not a compromise. Empirically, soft (weighted) routing and hard (argmax) routing both scored 97.25%, but hard routing took 5.5 ms against 38.2 ms for soft.[^c5] The explanation offered is that a trained router puts near-100% probability on one universe, so the soft mixture collapses to selection plus overhead.[^c6]

A second consequence is modularity. New universes can be added by training only the router, leaving existing solvers untouched.[^c7] In an expansion from 5 to 7 universes, rehearsal with 10% replay gave 0.00% forgetting. EWC still forgot 75.00%, and naive fine-tuning forgot 86.84%.[^c8]

## What the router learns

The router is a fine-tuned classifier over 7 universes: frequentist, Bayesian, three physics frameworks, a mixed class and an ill-posed class. The training set is 685 synthetic GPT-4 samples.[^c9] TF-IDF baselines reach near-perfect test accuracy by keyword matching but fall by about 26 points on unseen phrasings. Fine-tuned transformers show 1.8–2.3 times smaller gaps.[^c10] Keyword injection ("consider the prior" added to frequentist questions) fooled TF-IDF 89.91% of the time and the fine-tuned model 4.59%.[^c11] Zero-shot cloud models all struggled on the ill-posed class (64.7–94.1%, against 100% for the router). The author reads this as evidence that detecting ill-posed questions benefits from explicit boundary training.[^c12]

The label "ill posed" matters for asking and answering. One of the classes is a refusal to pick a framework, because the question itself does not fix one.

## Limits

- The data are 685 synthetic samples over only 7 mathematical and physical universes. Legal, ethical and causal frameworks were not tested.[^c13]
- Single-label hard routing cannot handle tasks that cross framework boundaries inside one problem.[^c13]
- Only routing accuracy was measured, not end-to-end task performance with downstream solvers. The claim that confusion corrupts downstream steps rests on worked examples in an appendix, which I did not read.[^c13]
- On 1,001 real MMLU questions with coarse proxy labels, the router reached only 56.8% (TF-IDF 46.2%), so transfer from synthetic to natural phrasing is weak.[^c14]
- The test set has n = 109, so five of six cloud-model comparisons were not statistically distinguishable.[^c15]
- "Hard equals soft" was measured only where universes were already separable. It is not shown for overlapping frameworks. The proposition is a sketch, not a proof; and "semantic understanding" is the author's inference from the gap, not a tested mechanism.
- The continual-learning comparison covers one router and one regularizer. "Modular architectures are fundamentally more amenable" is a stronger claim than that evidence supports.

## Related

- [[state-gated-strategy-routing]] — routes among answering strategies by state, not among incompatible frameworks
- [[uncertainty-aware-router]] — a router that uses confidence; here confidence also tracked accuracy on MMLU
- [[step-level-risk-calibrated-router]] — another router whose reliability depends on calibration

[^c1]: arxiv-2603-14799 — "Q1 demands frequentist statistics—null hypothesis testing, p-values, and rejection regions—while Q2 demands Bayesian statistics—prior specification, likelihood computation, and posterior integration."
[^c2]: arxiv-2603-14799 — "Two universes ui , uj are epistemically incompatible if ∃ a ∈ Aui , b ∈ Auj such that b ⇔ ¬a."
[^c3]: arxiv-2603-14799 — "The router then invokes the corresponding solver"
[^c4]: arxiv-2603-14799 — "ŷ does not belong to the validity domain Vu of any u ∈ U ."
[^c5]: arxiv-2603-14799 — "Soft (MoE-style weighted)"
[^c6]: arxiv-2603-14799 — "Soft combination then reduces to hard selection with additional computational overhead."
[^c7]: arxiv-2603-14799 — "New universes can be added by training only the router, without modifying existing solvers."
[^c8]: arxiv-2603-14799 — "Rehearsal with just 10% replay (29 samples) achieves zero forgetting."
[^c9]: arxiv-2603-14799 — "We curate 685 samples across 7 universes"
[^c10]: arxiv-2603-14799 — "but accuracy drops by 26pp on held-out questions with novel phrasings."
[^c11]: arxiv-2603-14799 — "fools TF-IDF baselines"
[^c12]: arxiv-2603-14799 — "suggesting that detecting illposed questions benefits from explicit boundary training."
[^c13]: arxiv-2603-14799 — "Single-label hard routing cannot handle genuinely multi-step tasks that require crossing framework"
[^c14]: arxiv-2603-14799 — "A router trained on 477 synthetic questions outperforms TF-IDF by +10.6pp (56.8% vs. 46.2%)."
[^c15]: arxiv-2603-14799 — "the remaining five are not statistically distinguishable at n = 109."
