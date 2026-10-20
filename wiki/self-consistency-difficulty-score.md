---
description: "A question-difficulty proxy built from the solver's own answer agreement rate, transformed to peak at maximal disagreement, used to reward and pre-filter near-capability-boundary questions."
aliases: ["self-consistency difficulty score", "capability-boundary difficulty reward"]
sources: ["xu-2026-rise", "doi-10-48550-arxiv-2606-27376", "doi-10-48550-arxiv-2510-17472", "arxiv-2512-06751", "arxiv-2511-16043"]
---
# Self-consistency difficulty score

> A candidate question's difficulty is estimated without any labelled
> answer, from how often the solver's own sampled answers agree with each
> other, and that estimate both rewards the questioner and filters which
> question-answer pairs enter training.

## Definition / Mechanism

Xu et al. (2026) sample the solver $M$ times on a candidate
question and take the majority-vote agreement fraction as a self-consistency
score: "we compute the self-consistency score c(x, q) ... A larger c(x, q)
indicates that the solver responses are more stable for the question
(x, q)."[^c1]

That score is folded so that it peaks when the solver is most divided
rather than when it is most consistent. The authors credit the construction
to a separately cited work (their reference [36], not further identified in
the slices read here), not original to this paper: "we use this score to
construct the difficulty score [36] d(x, q) = min c(x, q), 1 − c(x, q),
which favors questions near the solver's current capability boundary rather
than overly easy or highly unstable ones."[^c2]

The same score is reused as a training-data filter, discarding both ends of
the distribution: candidates are kept only if "c(x, q) ∈ [τmin , τmax],
where overly easy questions usually provide limited learning value, while
highly unstable ones are often noisy," with the reported operating range
"[τmin , τmax] = [0.3, 0.8]."[^c3]

## Why it matters

This gives a selection criterion for stall 2 that needs no ground-truth
label and no separate reward model: the solver's own answer variance stands
in for question value. It sits between the [[mutual-information]] family (score
by expected [[entropy]] drop against a fixed target) and pure exploration —
here the "target" is the asking model's own current uncertainty, folded to
a mid-range sweet spot instead of maximized directly, which is a different
shape than "ask what reduces entropy most."

Agent0 uses the same agreement fraction in a second role, as a reliability weight on the training signal rather than as a difficulty score. Its pseudo-label is the executor's own majority answer, and the paper's reason for weighting is that on low-agreement tasks "the majority answer is prone to errors."[^c12] The advantage is therefore multiplied by a scale that grows with the score, "where f is an increasing function of self-consistency."[^c13] The form of f is not given in the parts I read. The ablation removes the whole ADPO objective, scaling and trust region together, and the authors attribute the loss to the standard algorithm "does not account for the reliability of pseudo-labels."[^c14] So the drop cannot be assigned to the scaling alone, and the paper does not test this weight against other weights.

## Limits

The reported threshold range $[0.3, 0.8]$ and the $M{=}10$ sample budget
are this paper's configuration on two Qwen-VL backbones; a wider or
narrower band trades off how many candidates survive filtering against how
noisy the survivors are, and that trade-off is not characterized here. The
score conflates two things a solver can be uncertain about — a genuinely
ambiguous or underspecified question and a hard-but-well-posed one — since
majority-vote disagreement looks the same for both; the paper's separate
quality supervisor (question validity check) is what is meant to catch the
former, so this score alone should not be read as a difficulty measure in
isolation from that filter. A sample-level agreement entropy over prompt framings is a related but different quantity, and it has its own blind spot: it "remains close to zero" when the solver is consistently right, "but also when it is consistently wrong".[^c4][^c5] The remedy proposed for that case is a token-level reading, [[solver-token-entropy]].

A different statistic from the same vote is the signal-to-noise ratio of the margin between the leading and the runner-up answer, which the paper defines in the margin view of [[majority-vote-mode-certificate]]. On MATH-500 it tracks the benchmark's own difficulty levels: "harder problems exhibit systematically lower SNR and greater variability."[^c6] The paper reads this as an emergent calibration and calls the SNR "a label-free proxy for epistemic uncertainty and, consequently, for task difficulty."[^c7] Unlike the folded score above, the SNR is not folded: the paper associates low values with "diffuse or multi-modal terminal distributions" and high values with prompts where one answer is produced consistently.[^c8] So in the paper's reading the SNR ranks easy above hard, and does not peak at the capability boundary. This is one benchmark, with the paper's own figures, and it is not replicated here.

The same kind of signal appears on the judging side with a different perturbation. A pairwise judge is asked twice, once per response order, and a case is flagged when the two verdicts disagree; no label is needed. The selective variant of [[evolving-evaluation-meta-prompt]] treats that "order-swap inconsistency" as a label-free proxy for evaluator uncertainty and spends its updates only on the flagged cases.[^c9] The paper reports that its gain over the vanilla judge grows with the share of flagged cases: "the performance gains of LWE over the vanilla baseline increase monotonically with the proportion of inconsistent samples".[^c10] Read against this note, the order-swap flag is the two-sample version of the agreement score: the same label-free disagreement from a different perturbation, and it shares the blind spot. The paper names cases that are consistent but wrong and says they "remain indistinguishable without access to ground-truth labels".[^c11]

## Related

[[skill-aware-dynamic-balancing]] · [[self-evolving-visual-questioner]] · [[self-questioning-vlm-grpo]] · [[expected-information-gain]] · [[edge-of-competence-selection]] — the labelled counterpart: a question is kept where pass@1 is low and pass@k is above zero, which needs ground truth

[[evolving-evaluation-meta-prompt]] — the judging-side use of the same disagreement signal: order-swap flags decide which cases update a judge's meta-prompt

[^c1]: xu-2026-rise
[^c2]: xu-2026-rise
[^c3]: xu-2026-rise
[^c4]: doi-10-48550-arxiv-2606-27376 — "Sample-level self-consistency entropy remains close to zero"
[^c5]: doi-10-48550-arxiv-2606-27376 — "but also when it is consistently wrong"
[^c6]: doi-10-48550-arxiv-2510-17472 — "harder problems exhibit systematically lower SNR and greater variability"
[^c7]: doi-10-48550-arxiv-2510-17472 — "label-free proxy for epistemic uncertainty and, consequently, for task difficulty"
[^c8]: doi-10-48550-arxiv-2510-17472 — "low SNR values arise for diffuse or multi-modal terminal distributions"
[^c9]: arxiv-2512-06751 — "order-swap inconsistency (i.e., disagreement between A vs. B and B vs. A judgments) as a labelfree proxy for evaluator uncertainty"
[^c10]: arxiv-2512-06751 — "the performance gains of LWE over the vanilla baseline increase monotonically with the proportion of inconsistent samples"
[^c11]: arxiv-2512-06751 — "remain indistinguishable without access to ground-truth labels"
[^c12]: arxiv-2511-16043 — "the majority answer is prone to errors"
[^c13]: arxiv-2511-16043 — "where f is an increasing function of self-consistency"
[^c14]: arxiv-2511-16043 — "does not account for the reliability of pseudo-labels"
