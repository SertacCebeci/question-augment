---
description: "A memory that groups a self-play solver's recurring failure causes under skill nodes, tracked Active or Mastered, and uses those states to target the question-generator's next round."
aliases: ["DiagEvo memory", "diagnosis-guided curriculum"]
sources: ["wei-2026-diagevo"]
---
# Hierarchical error-cause memory

> What a self-play question-generator asks next, decided not by difficulty
> or novelty but by which of the solver's own diagnosed weaknesses are
> still unresolved.

## Mechanism

Wei et al. (2026) build DiagEvo around a memory
$M_t = (V_t, E_t, a_t)$: a set of skill nodes $V_t$, a set of error causes
$E_t$, and an assignment $a_t$ from causes to nodes. "We introduce DiagEvo,
whose diagnostician extracts recurring error causes from this history and
stores them in a hierarchical error-cause memory. The memory groups related
causes under skill nodes and tracks each as Active or Mastered according to
self-consistency on targeted questions. The challenger uses these states
and recurrence counts to balance cause-targeted generation with free
exploration."[^c1]

Each cause carries a curriculum state (Active/Mastered) and an
active-episode failure count $f_t(e)$. A lightweight diagnostician LLM
compares a failed solver trajectory against one that reached the majority
pseudo-label, isolates their earliest reasoning divergence, and either
matches it to a known cause or files it as new. The generation mix for the
next round is set by the total failure count $F_t = \sum_e f_t(e)$ relative
to the round-1 reference $F_1$: "More failures under Active causes increase
cause-targeted generation. Promotion resets a cause's frequency."[^c2]

A cause is promoted to Mastered — its frequency reset to zero — once
solver self-consistency on questions targeting it clears a threshold:
"Promotion uses the mean p1(x) over all questions generated for an Active
cause... When at least one targeted question is available and the score
reaches θup, the cause becomes Mastered."[^c3]

Mastered causes stay available for "cross-state stitching" — pairing an
Active cause with a Mastered sibling in the same skill node to keep
generation from narrowing too fast.

## Why it matters

This is a concrete answer to stall 2 (which axis first) inside a closed
self-play loop: axis selection is driven by a record of the solver's *own*
diagnosed error causes rather than by an externally supplied difficulty
signal, human examples, or a document corpus.

Measured effect: "On Qwen3-8B, it reaches 72.3% mean accuracy across five
mathematical reasoning benchmarks, 4.5 percentage points above R-Zero...
Its mean accuracy across all nine benchmarks is 57.4%, 1.1 percentage
points above DARC."[^c4]

Ablations reported in the abstract attribute part of this gain to the
memory specifically: "Ablations show that the hierarchical error-cause
memory and [[double-confidence-filtering|double-confidence filtering]] both contribute to these gains."[^c5]

## Limits

- Every claim here is Wei et al.'s own reported result, on their three
  solvers (Qwen3-4B/8B, OctoThinker-8B) and nine benchmarks; no independent
  replication was read for this note.
- The pseudo-label a failure is diagnosed against is itself majority-vote,
  not ground truth — the extracted "error cause" is a relative difference
  between two responses, not a verified reasoning defect.
- The mechanism needs an LLM diagnostician and an embedding-based
  deduplication step; its cost and failure modes when the diagnostician
  itself misclassifies a cause are not analysed in the material read here.

## Related

[[investigative-question-grpo-training]] · [[double-confidence-filtering]] · [[expected-information-gain]] · [[optimal-decision-tree]]

[^c1]: wei-2026-diagevo — "We introduce DiagEvo, whose diagnostician extracts recurring error causes from this history and stores them in a hierarchical error-cause memory. The memory groups related causes under skill nodes and tracks each as Active or Mastered according to self-consistency on targeted questions. The challenger uses these states and recurrence counts to balance cause-targeted generation with free exploration."
[^c2]: wei-2026-diagevo
[^c3]: wei-2026-diagevo
[^c4]: wei-2026-diagevo — "On Qwen3-8B, it reaches 72.3% mean accuracy across five mathematical reasoning benchmarks, 4.5 percentage points above R-Zero. Its mean accuracy across all nine benchmarks is 57.4%, 1.1 percentage points above DARC."
[^c5]: wei-2026-diagevo — "Ablations show that the hierarchical error-cause memory and double-confidence filtering both contribute to these gains."
