---
description: "In group-relative RL a prompt whose rollouts all agree yields zero advantage; waste peaks at success rates near 0 or 1, so a predictor of within-question reward variance can pick informative prompts."
aliases: ["Goldilocks zone prompt selection", "reward-variability prompt selection", "zero-variance rollout groups", "value-based sampling"]
sources: ["arxiv-2602-14868", "doi-10-48550-arxiv-2608-02831", "arxiv-2512-19512", "arxiv-2512-07710", "arxiv-2512-07478", "openalex-org-w7131909710", "arxiv-2511-18902"]
---
# Zero-variance group waste

In GRPO-style training with a binary verifiable reward, each prompt receives G sampled answers and each answer's advantage is its reward standardized within the group. Goldilocks RL points out that the informativeness of a prompt is therefore a function of the model's current success probability p on it, and that the extremes carry no signal.[^c1]

## Mechanism

**Zero-variance event.** If all G rollouts are correct or all are wrong, every advantage is zero and the prompt contributes no gradient. The probability is p^G + (1-p)^G, minimized at p = 1/2 and approaching 1 as p goes to 0 or 1.[^c2] Prompts at the extremes thus waste a whole group of rollouts almost surely, whatever the model or budget.

**Shrinking gradient.** Under a bounded per-token-gradient assumption the gradient norm is bounded by a constant times sqrt(p(1-p)), so it also vanishes at the extremes.[^c3] The authors state that this is a simplified intuition for why intermediate-difficulty questions give more informative updates, not a full account of RL dynamics.[^c4]

**Selecting before rolling out.** Since p is unknown for unseen questions, a small Selector network is trained online to regress the empirical sqrt(p̂(1-p̂)) of past groups, using a replay buffer of recent (question, target) pairs; the next training question is the highest-scoring candidate from a random pool, with epsilon-greedy exploration.[^c5] This differs from the closest predecessor, which predicts success probability and picks questions near a target difficulty; Goldilocks predicts the reward variability of the group itself.[^c6]

**Selecting after rolling out.** VSPO takes the other timing. It rolls out the batch first, drops prompts whose group reward variance falls below a small threshold, and redraws the replacements from the survivors: "then replaces them by resampling from the remaining samples."[^c19] The redraw weight is a task value V = (R_max − µ)·σ², with µ and σ² the group's reward mean and variance and R_max the best reward in the batch, turned into probabilities by a temperature softmax. The first factor is read as difficulty, since it "represents the potential improvement gap between the best" rollout and the group average, while σ² stands for the policy's uncertainty.[^c20] Resampling duplicates prompts, and a prompt drawn N times has its advantage counted N times. The paper's point is that "This shows that sampling xK N times is equivalent to" scaling that advantage, and it adds a value-smoothing clip that shrinks repeated samples.[^c21] The authors also say that value-based sampling "can cause training instability" when used alone.[^c22]

**Measured.** On OpenMathReasoning and Polaris, the method improved over standard GRPO, and in a Qwen2.5-7B run produced substantially fewer zero-variance groups than both GRPO and the success-probability baseline.[^c7] An average training reward near 0.5 does not by itself imply intermediate per-question success, since it can come from a mixture of very easy and very hard questions; this is why the target is within-question variance and not the mean.[^c8]

**Keep the rollouts, shrink the zero-variance rate.** The Shopee report of a hundred-billion-scale MoE run takes the opposite view from filtering. It names dynamic sampling as the industrial default and rejects it on cost: "Existing industrial approaches, such as dynamic sampling, attempt to alleviate this issue by"[^c14] discarding the groups, and "However, this strategy further exacerbates computational inefficiency,"[^c15] since large portions of rollouts are ignored. Instead the authors raise the number of samples per prompt. "Experimental results show that expanding the exploration space reduced the overall" zero-variance rate, "zero-variance rate by 17%,"[^c16][^c17] and they chose a sampling size by weighing that gain against compute. Their residual problem is that "5% of sample groups still exhibited zero-variance rewards,"[^c18] which they handle at the advantage step with a stochastic reshaping (RLZVP) rather than by dropping groups. So one paper reads the same waste as a rate to be lowered by more rollouts, not as a set of prompts to be removed.

**The same test one level down.** Audio-reasoning RL with rubric rewards applies the zero-variance logic to criteria rather than prompts. For each criterion the within-group deviation of its binary verdicts is computed, and a criterion with zero deviation is dropped: "In both cases, it assigns every rollout the same verdict, and thus contributes nothing to the group-relative advantage."[^c9] Survivors are ranked by that deviation and the most discriminative are kept, "retain the top M most discriminative ones or all, if fewer than M survive."[^c10] So a criterion met by every rollout is treated as mastered and one met by none as out of reach, which is the prompt-level case restated for each criterion.

**Imbalance across classes.** In multi-class anatomy recognition the same all-agree pattern appears with the classes in place of the prompts. Anatomy-R1 reports that for common structures the policy "rapidly converges and may correctly identify the structure in all M responses", while for rarer ones "the policy consistently fails, incorrectly identifying the structure in all M" responses.[^c11][^c13] The authors trace this to uneven learning across classes, since the model learns common anatomies "far more quickly than rarer, more complex structures".[^c12] The remedy they chose changes the prompts that feed each group rather than the selection rule; see [[rollout-question-augmentation]]. Whether a difficulty-keyed selector would do better on the same classes is not tested there.

**Score the failed rollouts instead.** A different remedy keeps every prompt and changes the reward of the failed rollouts, which is soft outcome scoring. Search-P1 gives a trajectory with a wrong final answer partial credit: a weighted sum with α = 0.8 on partial answer correctness, plus a term for "reasoning quality independent of the final answer", the stated aim being "converting zero-reward samples into useful training" signal.[^c23][^c24] The gain is uneven across tasks: soft scoring gives "modest gains for single-hop tasks", and the largest effect is on the internal multi-hop advertising set, "the highest gain for AD-QA".[^c25] This changes which rollouts carry signal rather than how many groups come out all-equal. The paper does not compare it with prompt filtering at equal compute, so whether the two remedies stack or substitute is not shown there (my inference).

**A different gain weight.** VADE (arxiv-2511-18902) scores each candidate by an approximate information gain, I = p(1−p)^2, rather than by the gradient-norm bound above. The gain is stated as "from selecting this data point for policy gradient optimization is approximately" that expression.[^c26] The form is taken from the theory of sample information gain "as presented in Knapsack RL,"[^c27] and the paper states that selecting the top items by it "theoretically maximizes the single-step training gain."[^c28] The weight still vanishes at both extremes, but its maximum sits at p = 1/3 rather than 1/2 (my arithmetic: the derivative is (1−p)(1−3p)), so it favours questions the policy solves less than half the time. Whether the two weights rank prompts differently in practice is not compared in the sections I read.

## Limits

- The gradient bound is an upper bound under an assumed uniform per-token gradient bound; it does not show intermediate prompts give larger actual gains.
- Binary verifiable rewards only; the footnoted extension covers rewards of the form verifier plus a term converging to a constant.
- The target is estimated from G samples, so p̂ is noisy for small G (my inference; the paper has a group-size ablation I did not read).
- On Polaris with Qwen2.5-7B a history-based baseline reached the highest final accuracy, so the advantage is not uniform.
- A single selector GPU is reserved in the compute comparison; I did not verify the cost accounting in detail.
- Nothing here concerns open-ended or clarifying questions.
- The criterion-level filter reuses the same G-sample estimate of variance. With few rollouts a criterion can show zero deviation by chance and be dropped, and the audio paper does not discuss this (my inference).
- The 17% reduction in the Shopee run is one reported figure for one model; the text gives no sweep over the sampling size and no accuracy comparison against dynamic sampling, so whether more rollouts beat filtering at equal compute is not shown there (my inference from the printed text).
- The value-based resampling in VSPO reweights prompts after their rollouts are already paid for, so it saves no generation; it changes which prompts fill the batch. I read only the method sections of that paper, not its experiments or its temperature and smoothing ablations, and I did not find a comparison against a pre-rollout selector such as the Selector above (my inference).

## Related

- [[learnability-posterior-curriculum]] — same boundary-seeking variance signal, used in a self-play question generator with Beta posteriors
- [[two-scale-prior-decay]] — a per-item Beta posterior of success probability, kept online from the training batches themselves, so the selector needs no separate rollouts
- [[curriculum-collapse]] — a failure mode of difficulty curricula
- [[model-dependent-benchmark-difficulty]] — difficulty depends on the current model, as here
- [[rubric-difficulty-evolution]] — the criterion-level version of this filter, where criteria are regenerated against each group's rollouts
- [[decision-ambiguous-sample-mining]] — another pre-rollout selector for group-relative RL; it ranks items by a reference model's probability margin between the correct and strongest wrong option, not by predicted within-group reward variance (the DARFT paper does not compare the two)
- [[importance-learnability-decoupling]] — a criterion with zero within-group variance teaches nothing whatever its human weight; the rubric weight and the criterion's learnability are separate quantities
- [[advantage-flip-near-group-mean]] — the other failure of a group's advantage: responses near the mean get the wrong sign, where this note's failure is all rollouts tied

[^c1]: arxiv-2602-14868 — "In GRPO, the advantage is computed by normalizing rewards across a group of G outputs sampled for a single prompt."
[^c2]: arxiv-2602-14868 — "which is minimized at pq = 1/2 and approaches 1 as pq → 0 or pq → 1."
[^c3]: arxiv-2602-14868 — "as pq → 0 or pq → 1, the gradient norm ∥∇θ LPG ∥ → 0, leading to vanishing gradients."
[^c4]: arxiv-2602-14868 — "simplified intuition for why intermediate-difficulty questions can provide more"
[^c5]: arxiv-2602-14868 — "This tuple (q, yq ) is pushed into a replay buffer"
[^c6]: arxiv-2602-14868 — "whereas Goldilocks directly predicts the reward variability of the"
[^c7]: arxiv-2602-14868 — "produces substantially fewer zero-variance rollout groups than both GRPO and PCL."
[^c8]: arxiv-2602-14868 — "an average reward near 0.5 does not by itself imply that individual questions have intermediate success probability,"
[^c9]: doi-10-48550-arxiv-2608-02831 — "In both cases, it assigns every rollout the same verdict, and thus contributes nothing to the group-relative advantage."
[^c10]: doi-10-48550-arxiv-2608-02831 — "retain the top M most discriminative ones or all, if fewer than M survive."
[^c11]: arxiv-2512-19512 — "rapidly converges and may correctly identify the structure in all M"
[^c12]: arxiv-2512-19512 — "far more quickly than rarer, more complex structures"
[^c13]: arxiv-2512-19512 — "For difficult-to-recognize anatomy, the policy consistently fails"
[^c14]: arxiv-2512-07710 — "Existing industrial approaches, such as dynamic sampling, attempt to alleviate this issue by"
[^c15]: arxiv-2512-07710 — "However, this strategy further exacerbates computational inefficiency,"
[^c16]: arxiv-2512-07710 — "expanding the exploration space reduced the overall"
[^c17]: arxiv-2512-07710 — "zero-variance rate by 17%"
[^c18]: arxiv-2512-07710 — "5% of sample groups still exhibited zero-variance rewards"
[^c19]: arxiv-2512-07478 — "then replaces them by resampling from the remaining samples."
[^c20]: arxiv-2512-07478 — "represents the potential improvement gap between the best"
[^c21]: arxiv-2512-07478 — "This shows that sampling xK N times is equivalent to"
[^c22]: arxiv-2512-07478 — "can cause training instability."
[^c23]: openalex-org-w7131909710 — "converting zero-reward samples into useful training"
[^c24]: openalex-org-w7131909710 — "reasoning quality independent of the final answer"
[^c25]: openalex-org-w7131909710 — "the highest gain for AD-QA"
[^c26]: arxiv-2511-18902 — "from selecting this data point for policy gradient optimization is approximately"
[^c27]: arxiv-2511-18902 — "as presented in Knapsack RL"
[^c28]: arxiv-2511-18902 — "theoretically maximizes the single-step training gain"
