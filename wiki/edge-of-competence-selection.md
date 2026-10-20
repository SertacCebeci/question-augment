---
description: "A question extends a solver beyond its base only where pass@1 is low but pass@k is above zero; elsewhere RL merely sharpens what the solver already does."
aliases: ["edge of competence", "solvability gap", "pass@k headroom", "boundary-of-competence training data"]
sources: ["arxiv-2512-07783", "doi-10-48550-arxiv-2605-07153"]
---
# Edge-of-competence selection

A solver's answers to one question can be read through its pass@k curve, the chance that at least one of k samples is correct. Read this way, a question falls into one of three regimes for training. Where the solver is already right on most samples, RL raises the first-sample accuracy (pass@1) while the k-sample accuracy stays flat, because the correct answers were already in the sampled pool. The paper calls this sharpening: "RL only sharpens existing capabilities".[^c1] Where the solver is right on almost no sample, there is no correct trajectory for RL to reinforce. The middle regime is the one the paper calls the edge of competence. There the base model "retains non-zero pass@128 accuracy" on the question,[^c2] and RL on such data produces "pass@128 performance" gains beyond the base model.[^c3]

The paper's controlled experiments fix the pre-training and vary the difficulty of the RL data. On in-distribution operation counts (2 to 10) RL gains pass@1 but not pass@128 under any data regime. On the just-out-of-range counts (11 to 14) RL improves pass@128, with "up to +42% pass@128 when well-calibrated" as the reported peak.[^c4] Where tasks are already covered, or too far out, the gain disappears: "gains vanish when tasks are already covered or too".[^c5] The paper reads this as a reconciliation of the literature. Studies that find RL does not raise pass@128 on well-covered math and coding, and studies that find large gains on synthetic tasks with little pre-training coverage, measure different regions of the difficulty spectrum. As the paper puts it, "RL yields no advantage on in-domain tasks that the base model already solves".[^c6]

As a selection rule, the paper recommends filtering RL data "where the model fails at pass@1 but succeeds at pass@k", and suggests re-evaluating the pool as the model improves, since "out-of-distribution tasks will drift into the solvability gap".[^c7][^c8] The gap is therefore a property of a (solver, question) pair, measured by sampling against a known answer, not a property of the question alone.

What transfers to question selection is the shape: the value of a question sits between what the answerer already does reliably and what it cannot reach at all. What does not transfer is the measurement. The paper selects training data for a solver whose answers are labelled. An asker choosing questions has no labels, so the pass@1-versus-pass@k gap is available only where answers can be checked. This transfer is my inference, not the paper's claim.

## Limits

- Synthetic and small. The model is a decoder "with 100M parameters on a large-scale synthetic" reasoning corpus.[^c9] Whether the three regimes have the same boundaries for pretrained language models on natural tasks is not shown in the sections read.
- One difficulty axis. Operation count defines the regimes. The edge is located by the base model's pass@128 against ground truth, so a question's edge is not known before a labelled sampling run.
- One RL algorithm. Training uses "Using GRPO [Shao et al., 2024], we train on curated subsets".[^c10] Other objectives were not compared in the sections read.
- The iterative re-selection the paper describes is stated as a consequence. No iterated run appears in the sections read.
- The criterion is k = 128. The paper treats a pass@128 gain as "genuine" capability; whether a k-sample gain is a new capability or a better search over the same distribution is the paper's reading, and it is kept here as theirs.
- Label-free substitutes are not tested against this criterion. Agreement among a solver's own samples can be high on a consistently wrong answer, so a vote-based edge may pick a different region (my inference).
- Factual QA points the other way on zero coverage. In closed-book factual RL with a binary reward, the questions whose correct answer never appears in 128 pre-RL samples are "only ∼18% of the full training data," and training on them "alone recovers ∼83% of the full-data RL gain."[^c11] That paper reads the gain as rare correct rollouts being reinforced, which is not the "no correct trajectory" reading above. The two papers study different tasks and different k, so this limits the rule's scope; it does not refute it (my inference). See [[rare-correct-rollout-reinforcement]].

## Related

- [[self-consistency-difficulty-score]] — a label-free difficulty proxy that also peaks near the solver's boundary; the pass@k gap here needs labels.
- [[learnability-posterior-curriculum]] — steers a question generator toward topics near the solver's capability boundary.
- [[query-level-uncertainty]] — estimates the boundary from the query before any answer exists, where this note uses sampled answers.
- [[rare-correct-rollout-reinforcement]] — a factual-QA result in which the zero-coverage bin carries most of the RL gain, against this note's regime reading.

[^c1]: arxiv-2512-07783 — "RL only sharpens existing capabilities"
[^c2]: arxiv-2512-07783 — "retains non-zero pass@128 accuracy"
[^c3]: arxiv-2512-07783 — "pass@128 performance when applied on the edge of competence data"
[^c4]: arxiv-2512-07783 — "up to +42% pass@128 when well-calibrated"
[^c5]: arxiv-2512-07783 — "gains vanish when tasks are already covered or too"
[^c6]: arxiv-2512-07783 — "RL yields no advantage on in-domain tasks that the base model already solves"
[^c7]: arxiv-2512-07783 — "where the model fails at pass@1 but succeeds at pass@k"
[^c8]: arxiv-2512-07783 — "out-of-distribution tasks will drift into the solvability gap"
[^c9]: arxiv-2512-07783 — "models with 100M parameters on a large-scale synthetic"
[^c10]: arxiv-2512-07783 — "Using GRPO [Shao et al., 2024], we train on curated subsets"
[^c11]: doi-10-48550-arxiv-2605-07153 — "accounts for only ∼18% of the full training data, it alone recovers ∼83% of the full-data RL gain"
