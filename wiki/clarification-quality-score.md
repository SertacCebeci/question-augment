---
description: "An LLM-judge rubric scoring each agent-initiated clarification 0-2 on relevance, specificity, timing and non-redundancy, averaged per trace as a proxy for question quality."
aliases: ["Clarification Quality Score", "CQS"]
sources: ["wu-2026"]
---
# Clarification Quality Score

> Instead of scoring only whether the task succeeded, score each question
> the agent asked: was it precise, necessary and targeted, or generic and
> redundant.

## Definition / Mechanism

For a task execution trace with clarification events $e \in E_C(\tau)$, an
LLM judge assigns each event a score $s_C(e) \in \{0,1,2\}$ — 2 if the
question "directly targets a critical slot, constraint, or risk point"
and helps the agent avoid errors, 1 if it is related but vague, 0 if it is
"irrelevant, overly generic, redundant, or focused on an irrelevant aspect
of the task." The judge is instructed on five dimensions: relevance,
specificity, timing, non-redundancy and risk awareness. The per-event score
is normalized $q_C(e) = s_C(e)/2$ and averaged over all clarification
events in the trace: $\mathrm{CQS}(\tau) = \frac{1}{|E_C(\tau)|}\sum_{e \in
E_C(\tau)} q_C(e)$. If no clarification event occurs in a trace, CQS is
undefined for it and excluded from averages.[^c1]

CQS is one of a triad of event-conditioned process metrics the same paper
defines over the same trace structure: Feedback [[information-utilization-rate|Utilization Rate]] scores
whether human feedback is subsequently acted on, using a binary per-event
label rather than CQS's three-level, halved scale, and Control Request
Justification scores whether a control request was warranted using the
same 0/1/2 scale as CQS but judging over-asking versus under-asking rather
than clarification quality.[^c2]

## Why it matters

CQS lets a benchmark separate *how often* an agent asks from *how good*
each question is — a system that asks constantly can still score low if
its questions are generic, and one that rarely asks can score at ceiling
if what it does ask is targeted. In the source paper, CQS moves in
opposite directions across domains as human agency rises (near-ceiling and
flat in Coding, 0.71 → 0.90 in Research), showing the metric is sensitive
to domain structure, not just to agent policy.[^c3]

## Limits

CQS is an LLM-judge score against a five-dimension rubric, not a measure
of the actual information the question would resolve (no ground-truth
$|W|$ or [[entropy]] computation backs it); it is undefined for traces with no
clarification event, which silently drops agents that clarify rarely from
the average rather than scoring their silence as 0.

## Related

[[has-bench]] · [[clarification-benchmarks]] · [[expected-information-gain]] · [[mutual-information]]

[^c1]: wu-2026 — "For each clarification event e ∈ EC (τ ), the evaluator assigns a score sC (e) ∈ {0, 1, 2} based on whether the clarification is precise, necessary, non-redundant, and targeted to task-relevant uncertainty. We normalize the event score as qC (e) = sC (e)/2"
[^c2]: wu-2026 — "Thus, unlike CQS and CRJ, which use a three-level event score normalized by 1/2, FUR uses a binary per-feedback utilization label."
[^c3]: wu-2026
