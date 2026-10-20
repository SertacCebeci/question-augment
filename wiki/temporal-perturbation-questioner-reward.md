---
description: "A label-free RL reward scoring a self-generated video question by how much Solver confidence drops when frame order is perturbed, training a Questioner toward temporal questions."
aliases: ["temporal-aware Questioner reward", "temporal perturbation sensitivity reward", "r^Q_temp", "temporal sensitivity score", "temporal inertia test"]
sources: ["huang-2026-evovid", "doi-10-48550-arxiv-2603-11481"]
---
# Temporal-perturbation Questioner reward

> In a Questioner–Solver self-play loop over raw, unannotated video, reward
> a candidate question by how much the Solver's own confidence collapses
> when the video is shuffled — turning "does this question actually need
> temporal order?" into a verifiable, label-free training signal.

## Definition / Mechanism

EvoVid trains a single base model to alternate between two roles, a
Questioner $\pi_Q$ and a Solver $\pi_S$, over unlabeled video with no human
annotation, external teacher, or reward model.[^c1]

While training $\pi_Q$ (with $\pi_S$ frozen), a candidate question $q$ is
scored on both the original video $v$ and a temporally perturbed version
$\tilde v = \sigma(v)$, obtained by a permutation $\sigma$ of the frame
sequence. Let $s(v,q)$ and $s(\tilde v,q)$ be the Solver's confidence
(agreement of its $M$ sampled candidate answers with the majority-voted
answer) on the original and perturbed video respectively. The reward is

$$r^Q_{\text{temp}} = \max\bigl(0,\; s(v,q) - s(\tilde v,q)\bigr)$$

added to a preliminary correctness/diversity reward $r_Q$ as
$r^Q_{\text{total}} = r_Q + \lambda_q\, r^Q_{\text{temp}}$. A question whose
answer the Solver can still give confidently after the frames are
shuffled earns no bonus; a question that only a correctly-ordered video
supports is rewarded in proportion to how much confidence the shuffle
destroys.[^c2]

A complementary Solver-side reward, $r^S_{\text{temp}}$, trains $\pi_S$ (with
$\pi_Q$ frozen) to localize the video segment its answer actually depends
on, scored by IoU against the frame window the Questioner sampled from;
the two rewards target different agents and different failure modes and
their gains are reported as additive rather than redundant.[^c3]

## Why it matters

The map's other trained-reward entries ([[investigative-question-grpo-training]],
EIG-as-preference-reward) score a question by a judge's opinion or by an
exactly computable information quantity over an enumerable answer set.
This reward needs neither: it manufactures a verifiable label from the
input's own structure (frame order) by re-running the same frozen Solver
on a corrupted copy of the input and taking the confidence gap as the
signal — a way to make "is this question actually anchored to information
that could be lost" checkable without ground truth, when the input has an
exploitable invariance (order) to perturb. Ablating it costs +0.7% average
accuracy across six video benchmarks against the vanilla self-evolving
baseline (49.2% including the Solver reward alone, 50.0% with both,
+1.4% over vanilla self-evolving); random shuffle, reverse-order, and
block-wise shuffle all beat no perturbation, while reverse-order (which
preserves most of the local temporal structure) gives the smallest gain of
the three.[^c4]

## Transfer

| | |
|---|---|
| **In its home field** | Reinforcement learning with a verifiable reward (as in RLVR / GRPO-style training): a reward is trusted only when it is checkable against ground truth or a rule, not a learned judge's opinion. |
| **Here** | The "ground truth" is manufactured, not given: the frame permutation is a known corruption of the same input, and the Solver's own confidence drop under it stands in for a label of "this question needed temporal order." |
| **What survives** | The verifiability property — the reward requires no human annotation and no separate judge model, only a comparison the pipeline can compute itself. |
| **What does not** | Generality of the trick: it depends on the input carrying an invariance whose corruption a competent Solver should be sensitive to (frame order, for video). A modality or axis without such a structural invariance to perturb has no equivalent signal available. |

The same probe is read on the answering side in INFACT. Its temporal intervention applies "frame-level shuffling or reversal" to an order-sensitive subset of questions,[^c6] and the score is "the rate at which model ceases to predict the original ground-truth label" after the intervention.[^c7] A model that keeps its answer after the frames are destroyed is read as showing "temporal insensitivity and reliance on order-invariant cues."[^c8] Where the reward above uses the Solver's confidence drop to train a Questioner, the benchmark uses the flip rate to rank answerers, and reports that "many open-source baselines exhibit nearzero TSS on factuality."[^c9] The two uses share the operation and differ in the readout. The reading of a retained answer as inertia is the authors' interpretation; the text read does not check it against a model that keeps its answer for other reasons (my inference).

## Limits

The claim rests on frame-order shuffling being a good proxy for "requires
temporal reasoning" — a Solver that is confidently wrong on both the
original and shuffled video, or one whose confidence is miscalibrated for
other reasons, would produce a reward gap that reflects Solver brittleness
rather than question quality; the paper tests three shuffle variants and
does not report how often a low-confidence-gap question is nonetheless
temporally meaningful. Results are reported on four Qwen-family base
models (3B–8B) across six benchmarks after three self-evolution rounds; a
3B-scale model showed degradation in later iterations that the authors
attribute to limited model capacity, so the reward's benefit is not shown
to be monotonic in training rounds at every scale.[^c5]

## Related

[[investigative-question-grpo-training]] · [[self-evolving-visual-questioner]] · [[question-generation-as-policy]] · [[expected-information-gain]]

[^c1]: huang-2026-evovid — "The paradigm builds upon two roles initialized from a single pretrained base model: a Questioner and a Solver. Given an unlabeled video v, the Questioner πQ generates a question q ∼ πQ (· | v), while the Solver πS produces M candidate answers"
[^c2]: huang-2026-evovid
[^c3]: huang-2026-evovid — "Intersection-over-Union (IoU): S rtemp = IoU(Ŵ, W)."
[^c4]: huang-2026-evovid — "temporal-aware Questioner reward rtemp improves the average performance across the six benchS marks by +0.7%, while using only the temporal-grounded Solver reward rtemp increases the average to 49.2%, corresponding to a +0.6% gain. Combining both rewards produces the full model, achieving 50.0% average performance, which surpasses VANILLA self-evolving by +1.4%."
[^c5]: huang-2026-evovid — "we apply our method to four base models: Qwen2.5-VL-3B-Instruct [35], Qwen2.5-VL-7B-Instruct [35], Qwen3-VL-4B-Instruct [36], and Qwen3-VL-8B-Instruct [36]."
[^c6]: doi-10-48550-arxiv-2603-11481 — "We apply temporal intervention to these videos via frame-level shuffling or reversal."
[^c7]: doi-10-48550-arxiv-2603-11481 — "We define TSS as the rate at which model ceases to predict the original ground-truth label"
[^c8]: doi-10-48550-arxiv-2603-11481 — "If a model retains the Base prediction after intervention, it indicates temporal insensitivity and reliance on order-invariant cues."
[^c9]: doi-10-48550-arxiv-2603-11481 — "many open-source baselines exhibit nearzero TSS on factuality"
