---
description: "Gating a debate's revised answer on a logit-confidence margin before log-odds fusion beats zero-shot and debate baselines on system-level discrimination in all twelve comparisons."
aliases: ["CGF", "confidence-gated debate fusion", "gated confidence fusion", "A-CGF"]
sources: ["doi-10-48550-arxiv-2606-13591"]
---
# Confidence-gated fusion

A two-agent debate yields four outputs: each agent's zero-shot answer and confidence, and each agent's post-debate answer and confidence. The question of this work is how to report one confidence for the system. Its premise: existing confidence estimators "are designed for a single model and a single response," and the common practice of reporting one agent's confidence "ignores evidence from the rest of the multiagent process."[^c1]

Confidence-gated fusion (CGF) answers in two steps. First, a gate: each agent "independently decides whether to retain its zero-shot prediction or" switches to its debated answer. The switch happens only when the debate raises the agent's confidence "by more than a learned threshold" in logit space, that is, when logit(c_i,1) − logit(c_i,0) exceeds a threshold τ_i fitted on validation data.[^c2] Second, fusion: the protocol "performs a probability fusion on the two surviving streams," adding their log-odds and applying the discount described in [[log-odds-dependence-discount]].[^c3]

The asymmetric variant, A-CGF, changes when debate happens. Rather than a full symmetric debate, it runs "one-sided debate (or persuasion step)" when the initial logit imbalance between the agents is large, so the more confident agent argues to the less confident one; balanced cases get the symmetric debate.[^c4] The same gate then applies after the persuasion step.

The reported effect is on discrimination of the system-level confidence. "CGF and A-CGF improve system-level confidence discrimination over zero-shot, standard debate, and debate-on-disagreement baselines in all twelve comparisons."[^c5] The paper's ablation separates the two components: "each alone yields substantially lower AUARC and higher t-Brier" than the combination.[^c6] Fusion on zero-shot streams, without the debate, is "significantly less effective" than the full protocol.[^c7] The authors also state that "the improvements from confidence gating combined with fusion are not achievable" with either mechanism alone.[^c8]

A second family, weighted stream voting (WSV), treats the four outputs as independent votes weighted by learned parameters, and the routed confidence is softmax-normalized. Against CGF, the one-sided sign test "did not show evidence of a performance difference between CGF" and WSV.[^c9] WSV is competitive, and "is strongest on the least ambiguous" task, but it is "less consistent across settings" (my reading of the conclusion).[^c15]

## Limits

- The parameters are learned, not derived. "All calibration functions and the aggregation parameters are optimized on a validation set." The routing step is non-differentiable, so the authors optimize it with TPE and early stopping.[^c10] The reported gains rest on that validation fit; a gate whose threshold is chosen on other data was not tested in the parts read (my reading).
- The protocol is two agents and one round: "This work is limited to the two-agent, one-round" setting.[^c11] Gating at later rounds is described as possible, but the authors "leave a systematic study of larger and multi-round" systems to future work.[^c12]
- The baselines are adapted. For the confidence-aware debate baseline, the authors "implement only the final-decision component" on stored outputs, so the control is "not a reproduction of ConfMAD."[^c13] Stored one-round generations "cannot reproduce the in-debate intervention," so the comparison is to a reconstruction.[^c14]
- The evaluation spans five benchmarks, 30 model pairs and two confidence estimators; the "twelve comparisons" are the protocol-baseline pairings reported with a multiple-comparison correction (pHolm ≤ .0016). The claim is about discrimination (AUARC) and the reliability of the probabilities. Task accuracy is described as remaining "competitive" with the baselines, not improved.[^c16]
- What the gate does to the case where both agents are wrong is not separated in the parts read. My inference: a gate that accepts only confident switches can also lock in a confident wrong answer, and the discrimination metric would not show it unless the errors are examined directly.

## Related

- [[log-odds-dependence-discount]] — the fusion step's correction for the correlated streams that survive the gate
- [[confidence-weighted-debate-submartingale]] — confidence-weighted counting in debate, with a theorem under a different model
- [[disagreement-retention-in-debate]] — a debate protocol that changes which messages are exchanged, not how confidence is reported
- [[debate-elicits-sycophancy]] — a failure of debate that a confidence gate does not address directly

[^c1]: doi-10-48550-arxiv-2606-13591 — "single agent ignores evidence from the rest of the"
[^c2]: doi-10-48550-arxiv-2606-13591 — "more than a learned threshold"
[^c3]: doi-10-48550-arxiv-2606-13591 — "performs a probability fusion on the two surviving"
[^c4]: doi-10-48550-arxiv-2606-13591 — "rather than conducting a full symmetric debate across all cases"
[^c5]: doi-10-48550-arxiv-2606-13591 — "CGF and A-CGF improve system-level confidence discrimination over zero-shot, standard debate, and"
[^c6]: doi-10-48550-arxiv-2606-13591 — "each alone yields substantially lower AUARC and higher t-Brier"
[^c7]: doi-10-48550-arxiv-2606-13591 — "fusion on zero-shot streams is significantly less effective"
[^c8]: doi-10-48550-arxiv-2606-13591 — "gating combined with fusion are not achievable"
[^c9]: doi-10-48550-arxiv-2606-13591 — "did not show evidence of a performance difference between CGF"
[^c10]: doi-10-48550-arxiv-2606-13591 — "The routing step is non-differentiable"
[^c11]: doi-10-48550-arxiv-2606-13591 — "This work is limited to the two-agent, one-round"
[^c12]: doi-10-48550-arxiv-2606-13591 — "we leave a systematic study of larger and multi-round"
[^c13]: doi-10-48550-arxiv-2606-13591 — "adapted control for the selection rule, not a reproduction of ConfMAD"
[^c14]: doi-10-48550-arxiv-2606-13591 — "cannot reproduce the in-debate intervention"
[^c15]: doi-10-48550-arxiv-2606-13591 — "less consistent across settings"
[^c16]: doi-10-48550-arxiv-2606-13591 — "Task accuracy remains competitive with"
