---
description: "Across seven LLMs on a PL/SQL benchmark, giving a priced option to ask did not raise accuracy overall, and helped only on tasks with a structural anchor."
aliases: ["ProcArena"]
sources: ["zhang-2026", "arxiv-2512-10195"]
---
# Direct-interactive accuracy gap (ProcArena)

> Giving an agent a priced channel to ask does not uniformly raise its
> accuracy: whether it helps depends on whether the task already supplies a
> structural anchor for what is missing.

## Definition / Mechanism

ProcArena pairs every Interactive PL/SQL task with a Direct counterpart:
the Direct version gives the Solver the complete (but not interactive)
requirement and forbids any `ask_user`/`ask_selector`/environment call
before submission; the Interactive version gives an underspecified or
internally contradictory requirement but allows the priced
[[solver-user-simulator-protocol|Solver-User Simulator protocol]] actions to
recover what was withheld. Across seven tested models (GPT-5.5, GPT-5.4
Mini, GPT-5.2, Gemini-3.1 Pro, GLM-5.3, GLM-5.2, DeepSeek V4 Pro), the
strongest model, Gemini-3.1 Pro, reaches 62.2% execution accuracy pooled
over two SQL dialects in Direct mode and only 57.8% in Interactive mode;
the weakest, DeepSeek V4 Pro, falls from 36.8% to 23.7%.[^c1]

The direction of the gap is not uniform across task categories. For
Synthesis tasks (write a procedure from scratch, no attachment) and Editing
tasks (a procedure attachment is given to modify), Direct-mode accuracy is
close — 59.8% against 66.2% for Gemini-3.1 Pro — but under interaction the
two separate sharply, to 48.1% against 73.5% for the same model: asking
recovers what the requirement withheld for Editing, where the attachment
already anchors most of what was removed, but for Synthesis, which has no
such anchor, the missing requirement facts must be recovered entirely
through the priced ask actions, and accuracy falls.[^c2]

A human audit of 180 sampled `ask_user` replies, stratified over solver
models and sub-scenarios, found 85.6% acceptable against the task's oracle
evidence, with the residual failures scattered over six categories and no
dominant mode.[^c3]

The same asymmetry shows up in a medical dialogue benchmark, AutoMedic, built on the [[closed-loop-standardized-patient-evaluation]] design. Each static multiple-choice item is turned into a virtual patient; a doctor agent questions a patient and a clinical staff agent, then answers, and the same agent also answers the item unaided. Across 11 LLMs and six QA sets the authors report that "all LLMs suffer a performance drop when moving from static QA to conversational settings."[^c4] Their accuracy score carries the drop inside it: conversational accuracy is multiplied by the ratio of conversational to static accuracy, and that ratio "quantifies the drop-off in performance" as a penalty factor.[^c5] Across models the two accuracies are correlated (r = 0.7547 in the paper), with a "strong positive correlation exists between static and conversational accuracy."[^c6] The correlation is weakest for open biomedical models ("weakest correlation (r = 0.6260)") and highest for proprietary ones ("demonstrate the highest correlation (r = 0.9350)").[^c7][^c8] The authors attribute the weak biomedical link to fine-tuning: "suboptimal fine-tuning strategies may hinder the effective translation of this knowledge into clinical dialogue."[^c9] My reading is that this makes the gap a property of how a model turns static knowledge into dialogue, not of its static knowledge alone; the paper does not separate the two causes.

## Why it matters

This is a same-benchmark, same-tasks, controlled comparison of "give the
full spec up front" against "let the agent ask under a real budget," not a
comparison across different benchmarks. It shows a real system where the
option to ask is priced and available can still lose to not needing to ask
at all — the value of the asking channel is conditional on whether the task
independently supplies enough structure to make the missing facts cheap to
recover.

## Limits

- One domain (PL/SQL/database procedure generation) and two dialects
  (PostgreSQL, Oracle); the anchor/no-anchor account of the direction is the
  paper's own explanation of its own subscenario results (A2, B3 also rise
  under interaction for the same structural reason), not an independently
  manipulated variable.
- The "user" side of every Interactive episode is a held-out LLM (DeepSeek
  V4 Flash) rather than a person, so some of the Interactive-mode loss may
  reflect simulator noise rather than the cost of asking itself — see the
  human-audit figure above.
- Each task runs once per model; no variance/repeat-run statistics are
  reported for the headline 62.2%/57.8% figures.
- The AutoMedic replication uses one proprietary model for the patient and clinical staff roles, so the size of the dialogue drop is conditional on that simulator.[^c10] Its correlations are across models, not within a model over repeated runs, and the penalty factor is the paper's design choice, not a measured quantity.

## Related

[[solver-user-simulator-protocol]] · [[clarification-benchmarks]] · [[defect-localization]] · [[closed-loop-standardized-patient-evaluation]] — the SP-style encounter design that AutoMedic's static pairing builds on

[^c1]: zhang-2026 — "Gemini-3.1 Pro is the strongest model in both modes, at 62.2% and 57.8% pooled over the two dialects. GPT-5.5 follows at 61.6% and 57.0%. DeepSeek V4 Pro is last in both, at 36.8% and 23.7%."
[^c2]: zhang-2026 — "In the Direct mode Synthesis and Editing are close: 59.8% against 66.2% for Gemini-3.1 Pro, and 59.9% against 64.4% for GPT-5.5. In the Interactive mode they separate, to 48.1% against 73.5% for Gemini-3.1 Pro."
[^c3]: zhang-2026
[^c4]: arxiv-2512-10195 — "all LLMs suffer a performance drop when moving"
[^c5]: arxiv-2512-10195 — "factor. It quantifies the drop-off in performance"
[^c6]: arxiv-2512-10195 — "strong positive correlation exists between static"
[^c7]: arxiv-2512-10195 — "weakest correlation (r = 0.6260)"
[^c8]: arxiv-2512-10195 — "demonstrate the highest correlation (r = 0.9350)"
[^c9]: arxiv-2512-10195 — "suboptimal fine-tuning strategies may hinder the effective translation of this knowledge into clinical dialogue"
[^c10]: arxiv-2512-10195 — "for the patient and clinical staff roles"
