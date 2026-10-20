---
description: "Score a reasoning item's post-edit answer separately from its pre-edit answer to split revision failure into staleness, over-correction and evasion."
aliases: ["DeltaLogic", "revision gap", "inertia rate", "over-flip rate"]
sources: ["arxiv-2604-02733"]
---
# Minimal-edit belief-revision benchmark

> Getting the original answer right is not the capability under test — getting
> the *updated* answer right, and only the updated part, is.

## Definition / Mechanism

DeltaLogic (2026) turns a reasoning item into a
before/after pair by one deterministic minimal premise edit. An episode is
the tuple $e = (P, q, y_0, P', y_1, t)$: a premise set $P$, a
query $q$, the gold label $y_0$ before the edit, the edit type $t$ (support
insertion, defeating-fact insertion, support removal, irrelevant-fact
addition), the minimally edited premises $P' = \delta(P)$, and the gold label
$y_1$ that edit deterministically forces.[^c1]

Scoring is split into two passes rather than one: $Acc_{init} = \Pr(\hat y_0 =
y_0)$ before the edit, $Acc_{rev} = \Pr(\hat y_1 = y_1)$ after it. Splitting
the episodes into $C$ (gold label should change) and $U$ (gold label should
stay) exposes three distinct failure modes instead of one accuracy number:
inertia — keeping the pre-edit answer when $C$ demanded a change; over-flip —
changing the answer when $U$ demanded no change; and abstention — retreating
to "Uncertain" regardless of which was correct — the gap $Acc_{init} -
Acc_{rev}$ is the single-number version, the **revision gap**.[^c2]

On the reported runs (Qwen3-0.6B/1.7B/4B, Phi-4-mini-instruct; 20–30 episodes
per subset, built from FOLIO and ProofWriter), a model that answers well
before the edit does not answer well after it: Qwen3-1.7B's revision gap is
0.200, and Qwen3-0.6B reaches its revision accuracy only by abstaining on
every episode, which the inertia/over-flip/abstain split — not raw accuracy —
makes visible.[^c3]

The four edit types are not equally hard for the same model: adding a fact
that supports the query is a positive update the tested models get mostly
right, while removing a fact that grounded the original answer, or adding one
that defeats it, requires recognizing that support is now gone or reversed —
the harder direction, where the Qwen family stays inertial.[^c4]

Scale does not fix this by itself: a 4B model preserved essentially the same
inertia profile as the 1.7B model from the same family, while a different
model family at a comparable size (Phi-4-mini) traded inertia for non-zero
over-flip and abstention instead of resolving the trade-off.[^c5]

## Why it matters

A single post-edit accuracy number conflates three different reasons a model
could be wrong after new evidence arrives: it never updated, it updated too
much, or it dodged by abstaining. Reporting $Acc_{init}$ next to $Acc_{rev}$
with the inertia/over-flip/abstain split turns "the model got worse after the
edit" into "the model specifically fails to retract a defeated commitment"
or "the model specifically over-generalizes an irrelevant edit" — a
diagnosis [[agm-belief-revision|AGM's postulates]] state as a target
(vacuity, success) but do not, by themselves, measure in a trained model's
outputs.

## Limits

The reported evaluation is small (20 or 30 episodes per subset, four models,
CPU-only causal-LM scoring by token log-likelihood) and the paper itself
frames the numbers as evidence for the existence and shape of the failure
modes rather than a leaderboard. Episodes are single-step (one edit, one
re-answer): the taxonomy does not extend, untested, to chains of successive
edits or to free-form justification quality. The four edit types are
constructed from two existing datasets (FOLIO, ProofWriter) with
deterministic gold labels; the taxonomy's applicability to premises whose
post-edit truth value is not mechanically derivable is unverified.

## Related

- [[agm-belief-revision]] — the postulates this benchmark's metrics give an
  empirical, model-output test for.
- [[belief-base-revision]] — the finite, non-closed belief set an edit
  operator here effectively rewrites.
- [[answer-stability-abstention]] — a different trigger (adding an
  "I don't know" option) for the same family of question: is the model's
  answer change genuine belief change or noise.
- [[abstention]] — the reject option this benchmark's abstain rate measures
  as a possible failure rather than a virtue.
- [[calibration]] — the general problem of a model's confidence tracking
  correctness, of which "does the model know it must update" is a special
  case.

[^c1]: arxiv-2604-02733 — "Definition 1 (DeltaLogic episode). A DeltaLogic episode is a tuple e = (P, q, y0 , P ′ , y1 , t), where P is the original premise set, q is the hypothesis or query, y0 is the original gold label, P ′ is the minimally edited premise set, y1 is the revised gold label, and t is the edit type."
[^c2]: arxiv-2604-02733 — "The inertia rate is Inertia = Pr(ŷ1 = ŷ0 | e ∈ C, ŷ0 = y0 ), The over-flip rate is OverFlip = Pr(ŷ1 ̸= ŷ0 | e ∈ U, ŷ0 = y0 ), We also report abstention rate, Abstain = Pr(ŷ1 = Uncertain), because some models appear stable only by retreating into uncertainty."
[^c3]: arxiv-2604-02733 — "On the 30-episode Qwen evaluation subset, Qwen3-1.7B reaches 0.667 initial accuracy but only 0.467 revision accuracy, a revision gap of 0.200, while Qwen3-0.6B reaches 0.400 revision accuracy only through universal abstention."
[^c4]: arxiv-2604-02733 — "Adding a new premise that explicitly supports the query is easier than revising a previously justified belief once its support disappears or once a defeating fact arrives."
[^c5]: arxiv-2604-02733 — "Qwen3-4B is larger than Qwen3-1.7B but preserves essentially the same inertia profile. That is evidence against a naive “more scale fixes revision” story and in favor of the paper’s narrower claim: minimal belief revision is a distinct capability worth measuring directly."
