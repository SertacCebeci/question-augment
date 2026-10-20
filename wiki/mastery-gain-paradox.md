---
description: "A tutor that answers early scores higher short-term mastery gain through over-assistance, so gain alone rewards the tutor that violates attempt-before-hint; hint efficiency exposes it."
aliases: ["Mastery Gain Paradox", "over-assistance inflation", "hint efficiency"]
sources: ["arxiv-2603-23990"]
---
# Mastery gain paradox

A tutor can look better on short-term performance precisely because it gives away too much. Kadir defines the paradox as users achieving "high short-term performance metrics (via over-assistance) while their latent mastery stagnates or degrades."[^c1] The attributed cause is a bias of general-purpose LLMs toward frictionless user satisfaction, which leads monolithic tutors to give answers early.[^c2]

## What was measured

The paper simulated 2,400 synthetic students (four archetypes from k-means over ASSISTments 2017 BKT parameters, 600 runs each, Gaussian-perturbed parameters) against a monolithic LLM baseline and a tutor whose rules-based orchestrator decides the pedagogical action before an LLM only words it.[^c3] The baseline achieved the higher mastery gain (+0.70 vs. +0.40), but only by giving 12x more hints (6.8 vs. 0.44 per dialogue).[^c4] The rules-based tutor kept 100% adherence to the attempt-before-hint constraint.[^c5]

The diagnostic is therefore a pair of numbers, not one. Gain per hint ("hint efficiency", mastery gain divided by hints) reverses the ranking: the paper reports a 3.3x increase for the orchestrated tutor.[^c6] The lesson for asking and answering: an answer-giving policy must be scored on how much help was spent to produce the outcome, otherwise the metric prefers the response that removes the learner's own attempt.

## Related mechanism: decoupling decision from wording

The architecture credited with removing the failure separates the choice of pedagogical action (deterministic rules plus a Bayesian Knowledge Tracing mastery posterior) from surface realization by an LLM. Constraints such as hint caps are then explicit rules whose checks are logged per turn.[^c7] My own reading: this makes the constraint auditable, but the simulation does not isolate decoupling from the other differences between the two arms.

## Limits

- The gain comes from simulated students governed by idealized BKT parameters; the authors state these do not mirror real classrooms, and no human learning outcomes were measured.[^c8]
- A synthetic BKT student rewards hints through its learning parameter, so the +0.70 baseline gain partly reflects the simulator's assumptions. Whether real over-assisted learners lose latent mastery is asserted, not measured here.
- The "latent mastery stagnates or degrades" half of the definition is not shown: in the simulation the baseline's mastery gain was higher, not lower.
- One author, one dataset, one baseline family; the ensemble and baseline differ in many ways beyond the hint rule.

## Related

- [[staged-socratic-hint-policy]] — a fixed ladder of hint specificity that operationalizes the same withholding
- [[answer-withholding-supervisor-architecture]] — an orchestration-level contract that likewise enforces withholding per turn
- [[scaffolding-collapse]] — a neighbouring failure of scaffolding
- [[llm-judge-biases]] — the paper's quality results also rest on LLM judges

[^c1]: arxiv-2603-23990 — "while their latent mastery stagnates or degrades."
[^c2]: arxiv-2603-23990 — "due to the inherent bias of general-purpose LLMs toward frictionless user satisfaction"
[^c3]: arxiv-2603-23990 — "We conducted a large-scale Monte Carlo simulation (N=2,400)."
[^c4]: arxiv-2603-23990 — "the baseline achieved a higher mastery gain (D = +0.70 vs. +0.40), but only"
[^c5]: arxiv-2603-23990 — "ES-LLMs achieved 100% adherence to the attempt-before-hint constraint"
[^c6]: arxiv-2603-23990 — "a 3.3x increase in"
[^c7]: arxiv-2603-23990 — "constraints such as “attempt-before-hint” and hint caps are enforced as explicit rules"
[^c8]: arxiv-2603-23990 — "synthetic learners governed by idealized BKT parameters do not perfectly mirror the messy cognitive and affective realities of human classrooms"
