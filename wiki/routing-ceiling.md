---
description: "When one answering mode already recovers 99%+ of achievable accuracy, per-query routing has near-zero possible gain regardless of the trigger signal — a headroom bound, not a signal-quality claim."
aliases: ["routing ceiling", "best-case gating ceiling"]
sources: ["lee-2026"]
---
# Routing ceiling

> Before judging whether a signal can pick the right answering mode, ask
> how much picking it right could possibly gain — the router may have
> nothing to route into.

## Definition / Mechanism

Lee et al. (2026) compute, on all four tested model families, an oracle
best-case combination between a retrieval mode and a domain-adapted
parametric mode over 2,860 held-out queries, before evaluating any actual
router. Retrieval alone reaches 99.3–99.8% of that best-case combined
accuracy, leaving 0.2–0.7% of accuracy for any router to [[competitive-llm-probing|compete]] for.[^c1]

The parametric mode adds almost nothing on its own terms too: its
standalone accuracy is 0.058–0.081, and it is right where retrieval is
wrong on only 5–14 of 2,860 queries.[^c2]

Gating with a hindsight-optimal threshold collapses to always-retrieval —
both oracle gates match retrieval-only accuracy to floating-point precision
on every model — so the ceiling is not a tuning problem the right threshold
could recover.[^c3]

Random gating falls 3.6–5.9 points below always-retrieval in proportion to
how often it mixes in the parametric mode, confirming the ceiling bites
in the direction that matters.[^c4]

This ceiling alone predicts the observed routing failure, independent of
whatever triggers the routing decision: "this ceiling predicts the routing
verdict … on its own; the trigger's verdict … has a different explanation."[^c5]

## Why it matters

A pre-registered [[sequence-likelihood-confidence|confidence signal]] failing
to discriminate correct from incorrect answers is a claim about the signal.
This is a separate, prior claim: even a perfect signal would have almost
nothing to gain in this setting, because one candidate answerer already
dominates. The two findings must not be read as evidence for each other —
a weak signal in a headroom-free setting proves nothing about that signal
elsewhere, and a headroom-free setting says nothing about whether a
*different* setting has room for a router to matter.

## Limits

- Established for retrieval-dominated extractive QA specifically; the
  paper leaves open whether the ceiling generalizes to settings where
  retrieval does not dominate, and this note's claim inherits that scope.[^c6]
- The ceiling is measured against an oracle (hindsight-best) gate, an upper
  bound on any real router — a real router can only do worse, never better.
- Computed on 7–9B open models on two domain corpora; not evidence about
  ceilings under other model scales or task types.

## Related

[[sequence-likelihood-confidence]] · [[value-of-information]] · [[abstention]] · [[expected-information-gain]]

[^c1]: lee-2026 — "RAG-only reaches 99.3– 99.8% of the best-case combined accuracy (retrieval recall@4 of 0.847 and 0.961; Section 4), leaving 0.2–0.7% of accuracy for any router to compete for."
[^c2]: lee-2026 — "FT-only accuracy is 0.058–0.081, and the fine-tuned model is right where retrieval is wrong on only 5 to 14 of 2,860 queries—the same gap counted from the parametric side."
[^c3]: lee-2026 — "Best-case gating saturates at always-retrieval. Both gates return accuracy identical to RAG-only, to floating-point precision, on every model: the threshold chosen with hindsight reduces to a policy that never selects the parametric mode."
[^c4]: lee-2026 — "Random gating falls below RAG-only on every model, by 3.6 to 5.9 points (from unrounded values), in proportion to how often the parametric mode is mixed in."
[^c5]: lee-2026 — "This ceiling predicts the routing verdict of Section 7 on its own; the trigger’s verdict, as Section 9 shows, has a different explanation."
[^c6]: lee-2026
