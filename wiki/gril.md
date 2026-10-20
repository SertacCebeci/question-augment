---
description: "A two-stage multi-turn RL framework trains a solve-or-clarify choice with a detection reward that decays with turns taken to ask, plus a penalty for asking when input is already sufficient."
aliases: ["GRIL", "Grounded Reasoning via Interactive Reinforcement Learning"]
sources: ["arxiv-2604-19656"]
---
# GRIL

> Choosing to reason is itself a decision contingent on available information — so the reward has to grade the choice, not just the answer that follows it.

## Definition / Mechanism

Anonymous (2026) name **ungrounded reasoning** the
failure mode where a language model, missing a premise it needs, fabricates
one and reasons on from it instead of asking. They formalize a problem as a
multi-turn MDP over two actions available at every turn — solve (commit to
the input as sufficient) or clarify (name the missing premise and stop) —
and state the failure as a selection error: "Ungrounded reasoning occurs
precisely when models select a_solve in states where a_clarify is
appropriate."[^c1]

GRIL (Grounded Reasoning via Interactive Reinforcement Learning) trains this
choice with an asymmetric environment: on an incomplete problem, clarifying
correctly is answered with the missing premise so the model can continue
solving; soIving anyway draws negative feedback and the episode ends. On a
complete problem, solving correctly ends the episode; clarifying draws an
"unnecessary" signal. The stage-1 detection reward decays with how many
turns the model takes before it asks: `R_detect = r_base · γ_d^n_prior`,
where `n_prior` is the number of turns generated before the clarify action
and `γ_d ∈ (0,1)` — "models that recognize missing information early receive
higher rewards than those that generate extensive ungrounded tokens before
requesting clarification." Stage 2 rewards only a correct answer after
the premise is supplied (`R_solve`), so detection is trained as a means to
solving, not as an end in itself. On complete problems the reward is
outcome-based minus a fixed penalty for clarifying unnecessarily:
`R_comp = r_correct · 1[correct] − λ · 1[unnecessary clarification]`, which
"prevents models from adopting a trivial strategy of always requesting
clarification regardless of input completeness." Training mixes complete
and incomplete problems 1:1, since either alone biases the learned policy
toward one action.

## Why it matters

Trained this way, the choice to ask is graded on two axes at once — how
promptly the model recognized the gap, and whether it actually used the
answer it got — rather than folded into one end-to-end correctness signal
that only ever rewards the final token. Against supervised fine-tuning on
the identical clarify/solve-labelled data, GRIL opens a wide gap: on
Qwen2.5-1.5B, "the SR gap is 30 percentage points (61.6% vs 31.6%)," which
the authors attribute to RL's access to the consequence of a choice —
imitation has no equivalent signal to learn from. The trained policy
generalizes: it transfers to out-of-distribution domains (HotpotQA,
CommonsenseQA) it was never trained on, and its precision on complete
problems stays above 0.96 even as recall on incomplete ones roughly
doubles, so the gain is not bought by becoming reflexively cautious.

## Limits

"Our results are obtained in an idealized interactive setting where an
oracle-like environment can judge insufficiency and provide the correct
missing premise after a clarification action; real users may refuse, be
uncertain, or provide noisy/partial information, so gains may not fully
transfer to real-scenario dialogues." The incomplete-problem set is built
by deleting one numeric-value sentence from math word problems and checking
automatically that the result is unsolvable, which covers a narrow,
synthetic class of missing-information types and may not generalize past
arithmetic-style problems. Evaluation of efficiency uses turn count and
response length as proxies for clarification quality, not a direct measure
of it or of real user cost. `unverified`: whether the decayed detection
reward, tuned here at γ_d = 0.5 with a single fixed missing premise per
problem, still shapes early asking correctly when a problem is missing more
than one premise or the premise itself is ambiguous.[^c5]

## Related

[[detection-to-abstention-gap]] · [[abstention]] · [[clarification-timing-decay]] · [[clarification-request]] · [[ask-f1-selective-escalation-metric]]

[^c1]: arxiv-2604-19656 — "Ungrounded reasoning occurs precisely when models select asolve in states where aclarify is appropriate."
[^c5]: arxiv-2604-19656 — "Our results are obtained in an idealized interactive setting where an oracle-like environment can judge insufficiency and provide the correct missing premise after a clarification action; real users may refuse, be uncertain, or provide noisy/partial information, so gains may not fully transfer to real-scenario dialogues."
