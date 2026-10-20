---
description: "A question type whose answer can add a new axis to the model mid-session Most of the axis-discovery generators the wiki already holds run *outside* the questioning loop: grand-tour-question and pre…"
aliases: ["dimension discovery"]
sources: ["tiwari-2026"]
---
# Dimension proposal

> A question type whose answer can add a new axis to the model mid-session
> — admitted only if it passes three structural gates, not by the asker's
> or the informant's say-so alone.

## Definition / Mechanism

Most of the axis-discovery generators the wiki already holds run *outside*[^s1]
the questioning loop: [[grand-tour-question]] and [[premortem]] condition
what gets asked before the session starts, and even
[[problem-solution-coevolution]] is an observed protocol effect rather than
a checkable admission step. Tiwari et al. (2026) instead
make axis growth one of five question types scored by the same
[[cross-type-eig|selection criterion]] as any other: a "dimension proposal"
question can add a new active dimension $d$ to the preference state, with a
signed feature loading $\phi_d$ and a Beta confidence, but the candidate
must first pass three named gates — **grounding** (it must tie to
observable features of the decision alternatives), **feature novelty** (it
must not duplicate an existing dimension's loading), and **coherence** (it
must not contradict rules already accepted; see
[[population-prior-mining]]). A proposal that fails a gate is not added;
the active-dimension set only grows through this admitted path.

## Why it matters

In the paper's own ablation (Table 2, Normalized Regret Reduction), adding
this transform to a system that already had population priors moved four
of five personas from 0.063–0.100 to 0.237–0.281 — the largest single jump
of any ablation step, larger than adding population priors alone (which
left three of five personas within 0.01–0.03 of the no-priors condition)
or than adding the remaining question types on top of it. On this
evidence, letting the axis set grow inside the same scored loop that asks
about existing axes did more for early-turn regret than either a richer
prior or a richer question menu over a fixed axis set — bearing directly
on Axes's open question of how a newly found axis gets weighted
without a separate hunting phase.

## Limits

- The gap is not uniform: for the Global-balanced persona, adding the
  remaining three question types on top of priors-plus-discovery *lowered*
  NRR from 0.281 to 0.128 (Table 2) — more transform diversity was not
  monotonically better once discovery was already present, and the paper
  does not explain the drop for that persona specifically.
- The three gates are named and described narratively; the paper reports
  no numbers on how often each one fires or how often a rejected proposal
  was later shown to be a real axis (a false-negative rate) — only the
  downstream regret is measured.
- The paper does not state whether admitting a new dimension preserves the
  particle weights already assigned to existing dimensions (the invariance
  [[reverse-bayesianism]] proves for a different, discrete-consequence
  model) or reallocates them; this note claims only what is stated.
- Evaluated only in the same simulated portfolio domain as
  [[cross-type-eig]]; the fixed 75-portfolio catalog bounds how many
  genuinely new dimensions a real session could ever propose.

## Related

[[cross-type-eig]] · [[problem-solution-coevolution]] · [[reverse-bayesianism]] · [[population-prior-mining]] · [[grand-tour-question]]

[^s1]: tiwari-2026
