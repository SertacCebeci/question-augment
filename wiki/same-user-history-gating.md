---
description: "A parameter-free gate LLM checks a user's resolved coding sessions for evidence resolving a new request's ambiguity, then passes on that evidence or a clarification target."
aliases: ["same-user history gating", "history gating method"]
sources: ["xu-2026-fewer"]
---
# Same-user history gating

> Instead of dumping a user's whole resolved-session history into context,
> a second LLM first decides whether that history actually settles the new
> request's [[efe-planning-as-variational-inference|ambiguity]], and only then extracts what matters.

## Definition / Mechanism

Xu et al. (2026) introduce this as a fix for a gap they
first show empirically: general-purpose memory managers (mem0, A-mem) do
not reliably beat handing over the raw resolved history, because neither
"explicitly identifies recurring ambiguity-resolution patterns or requires
the model to decide whether the retrieved evidence supports direct
implementation."[^c1]

The gate itself: "Our parameter-free workflow introduces a gate LLM that
reviews the resolved history for consistent ambiguity–resolution evidence.
When such evidence is sufficient, the gate highlights the most informative
prior session; otherwise, it provides clarification guidance indicating
what remains unresolved. The highlighted evidence or guidance is added to
the LLM context together with the new ambiguous request, enabling the base
LLM to either generate code directly or request necessary clarification."[^c2]

Evaluated against raw same-user history and against mem0/A-mem on GPT-5.5,
DeepSeek V4 Pro and GLM-5.2: "Our approach explicitly checks for such
ambiguity-resolution evidence and achieves the highest FT-ES and lowest TTC
among the three methods for all evaluated models," and "compared with raw
same-user history, our gating method consistently improves FT-ES by
0.66–13.33 pp while keeping ES within ±1.0 pp across all three models."[^c3]

## Why it matters

This is a working answer to "how should an asker use side information it
already has, before deciding to ask a question at all": route the evidence
through a checker that judges *[[sufficient-statistic|sufficiency]]* (does this settle the axis, or
only narrow it?) before either suppressing the question or asking a
sharper one — not a retrieval or summarization step blind to whether the
retrieved material actually resolves the gap.

## Limits

- Tested on 3 of the 12 benchmarked models (GPT-5.5, DeepSeek V4 Pro,
  GLM-5.2), all on [[capa-personalized-ambiguity-benchmark|CAPA]]'s
  synthetic sessions; generalization to the other 9 models and to real
  user histories is untested by this paper.
- "Parameter-free" means no trained weights, not free of design choices or
  inference cost — a second LLM call is added per turn, and its own error
  rate at judging sufficiency is not separately measured.
- Improves FT-ES and TTC consistently but leaves ES within ±1.0 pp of raw
  history — the gate changes when a correct answer arrives, not whether
  one eventually does.
- `xu-2026-fewer` is an unreviewed 2026 arXiv preprint — `[?]` pending
  verifier confirmation.

## Related

[[capa-personalized-ambiguity-benchmark]] · [[evidence-driven-online-preference-adaptation]] · [[adaptation-suppresses-clarification]]

[^c1]: xu-2026-fewer — "neither explicitly identifies recurring ambiguity-resolution patterns or requires the model to decide whether the retrieved evidence supports direct implementation"
[^c2]: xu-2026-fewer
[^c3]: xu-2026-fewer — "Our approach explicitly checks for such ambiguity-resolution evidence and achieves the highest FT-ES and lowest TTC among the three methods for all evaluated models."
