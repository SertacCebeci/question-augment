---
description: "Across 12 LLMs, five prior same-user coding sessions raise first-turn success and cut turns-to-completion on recurring, user-specific ambiguity, though the benchmark stays far from saturated."
aliases: ["CAPA", "Cross-Session Adaptation to Personalized Ambiguity", "personalized ambiguity adaptation"]
sources: ["xu-2026-fewer"]
---
# CAPA: personalized-ambiguity benchmark

> A coding request's [[efe-planning-as-variational-inference|ambiguity]] can be user-specific and recurring — the same
> user leaves the same kind of detail out every time — and a benchmark that
> hands an assistant five of that user's already-resolved sessions measures
> whether it exploits the pattern instead of asking again.

## Definition / Mechanism

Xu et al. (2026) formulate personalized ambiguity
adaptation as a task: given a user's *n* previously resolved coding
sessions and a new ambiguous request that opens a held-out session, an
assistant should infer the user's recurring ambiguity-resolution pattern,
produce a correct executable solution, and clarify only when the history
leaves the intended implementation underdetermined. CAPA instantiates this
over HumanEval tasks rewritten by six coding-specific ambiguity mechanisms
(e.g. habitual context omission, domain-cognitive polysemy): "CAPA contains
600 coding sessions across 60 balanced user–ambiguity cells, including 300
held-out evaluation sessions. We evaluate 12 recent LLMs under no-history
and same-user-history conditions using executable success, first-turn
success, and turns-to-completion."[^c1]

Under same-user history (five resolved sessions from the same user
prepended to the new request), the effect is consistent but partial:
"Same-user history improves ES for 11 of the 12 models and FT-ES for all 12
models, while reducing average TTC for every model," and averaged across
the 12 models, "history increases ES by 6.8 pp but FT-ES by 15.6 pp, while
reducing TTC by 0.81 turns." History helps a model recognise the intended
interpretation and answer sooner more than it turns eventual failures into
successes.[^c2]

An ablation separates generic multi-turn context from personalization
proper: "Even when user-specific information is removed through shuffling,
models still benefit from resolved-session context, with ES improving by
up to 10.67 pp over no history... Restoring correctly matched same-user
history yields further consistent gains in FT-ES (2.0–12.0 pp) and TTC
(0.04–0.19 turns)," showing a real personalization effect beyond generic
few-shot context.[^c3]

## Why it matters

This is a measured answer to "does resolved history let an assistant skip
re-asking an axis it has already been told about, for this user, before?" —
and the answer is only partially yes: even the strongest model (Claude
Opus 4.8) still leaves close to 40% of sessions needing clarification or
failing on the first response after history is added, and frontier
first-turn success stays under two-thirds. History is evidence that lowers
the need to ask, not a substitute for asking when the pattern genuinely
does not transfer to the new task.

## Limits

- All ambiguity is synthetically injected into HumanEval tasks by a
  three-stage generation pipeline, not sampled from real user–assistant
  logs; the six mechanisms were validated by 20 annotators (Fleiss' κ =
  0.66) recognising them, not by confirming they match real long-tail
  coding ambiguity.
- History is supplied as five complete resolved sessions in-context, with
  no parameter update or persistent storage — the result says nothing
  about retrieval-limited or token-budget-limited settings, or about
  histories with a mix of relevant and irrelevant tasks.
- `xu-2026-fewer` is an unreviewed 2026 arXiv preprint — `[?]` pending
  verifier confirmation.

## Related

[[same-user-history-gating]] · [[clarification-benchmarks]] · [[adaptation-suppresses-clarification]] · [[evidence-driven-online-preference-adaptation]]

[^c1]: xu-2026-fewer — "CAPA contains 600 coding sessions across 60 balanced user–ambiguity cells, including 300 held-out evaluation sessions. We evaluate 12 recent LLMs under no-history and same-user-history conditions using executable success, first-turn success, and turns-to-completion."
[^c2]: xu-2026-fewer — "Same-user history improves ES for 11 of the 12 models and FT-ES for all 12 models, while reducing average TTC for every model."
[^c3]: xu-2026-fewer — "Even when user-specific information is removed through shuffling, models still benefit from resolved-session context, with ES improving by up to 10.67 pp over no history"
