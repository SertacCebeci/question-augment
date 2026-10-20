---
description: "**This wiki's inference, not a result.** Every novelty-based stopping rule Three steps; only the first belongs to someone else. 1."
aliases: ["self-confirming run"]
sources: ["guest-2020", "prechelt-1998"]
---
# Self-confirming run

> **This wiki's inference, not a result.** Every novelty-based stopping rule
> read here assumes the observations inside its confirmation window arrive
> from a process that does not know the rule is watching. An asker who picks
> its own next question breaks that assumption — every question it can select
> is scored over the axes it has already modelled, so the run it reads as
> empty is the one its own criterion could not have filled.

## The claim

Three steps; only the first belongs to someone else.[^s1][^s2]

1. **The sources make the independence assumption explicit.** guest-2020
   condition their whole rate argument on keeping "the interview questions,
   sample characteristics, and other study parameters relatively consistent",
   and their bootstrap estimates the stopping point by re-running the rule
   over *randomly reordered* interviews — exchangeability is not tested, it is
   imposed by the design. In prechelt-1998 the counterpart is structural: the
   epochs inside a patience window are produced by a training algorithm that
   has no access to the stopping criterion, and the signal is scored on a
   held-out validation set.
2. **An adaptive asker supplies both sides of the window.** Under a greedy
   selection rule ([[expected-information-gain]], [[generalized-binary-search]],
   [[adaptive-submodularity]]) each question in the window is chosen by the
   same agent that will read the window's emptiness as a stop. The restriction
   is not that such a rule prefers predictable questions — it prefers the
   opposite, ranking a question high exactly when the modelled answer
   distribution is dispersed. It is that the score is a function of $\theta$
   and **undefined off $\theta$** ([[expected-information-gain]], *Where it
   applies*: "EIG is a SELECTION engine", not an exploration one), so however
   high-scoring the $R$ questions are, none of them can be the question that
   would return a constraint on an axis $\theta$ does not contain
   ([[unknown-unknowns]]).
3. **Therefore (this wiki):** an empty confirmation run measures the asker's
   question policy at least as much as the answerer's exhaustion, and the
   measurement is biased toward stopping. The bias does not shrink as $R$
   grows; a longer run is more of the same policy, so lengthening $R$ — the
   move `confirmation-run-length` (draft dropped) records as buying conservatism — buys less
   here than in the interview setting it was measured in, while costing the
   same questions.

**What this adds to what the wiki already has.** [[unknown-unknowns]] and
[[qualitative-saturation]] (*Limits*: "the failure mode of
[[unknown-unknowns]] is invisible to a novelty counter by construction")
already say that a novelty counter cannot see an unmodelled axis. The
increment here is about the counter's *own window*: when the $R$ questions are
supplied by the selection criterion, the emptiness is **produced rather than
observed**, and it does not dilute with $R$ — so $R$ must be specified by
**generator** as well as by length.

**What it would change in a derived procedure.** The confirmation window would
be specified by its generator: the $R$ questions would have to come from a
source independent of the stop decision — an instrument fixed before the base,
or probes drawn from the axis generator ([[grand-tour-question]]) rather than
from the scoring rule. A stopping rule would then declare two things, $R$ and
where the run's questions come from, and a run filled from the selection
criterion itself would not count as evidence of anything. That is a real
charge against the ask budget, though this wiki cannot yet size it: against
the *illustrative* user budget of 10–30 questions ([[question-budgets]], which
marks those counts as illustrative and uncalibrated), $R = 3$ would be a tenth
to a third of the budget, spent on questions deliberately *not* chosen for
information gain.

## Transfer

| | |
|---|---|
| In its home field | interviews from a fixed guide (guest-2020) or epochs from a fixed training algorithm (prechelt-1998); in both, the stream is exogenous to the stopping rule |
| Here | a question sequence in which each item is selected by the agent that also owns the stopping rule |
| What survives | the window itself, and the requirement — implicit in both sources, load-bearing here — that what fills it be independent of the decision it feeds |
| What does not | the transportability of the measured stopping points. guest-2020's medians are computed over random orderings of a fixed question set; an adaptively chosen sequence is not an ordering of a fixed set, so no number from that bootstrap indexes it |

## Limits

- **Conjecture, typed as one.** No source states it. Neither guest-2020 nor
  prechelt-1998 is writing about an agent that selects its own observations,
  and neither reports an experiment that could confirm or refute the bias.
- The step-2 premise is [[expected-information-gain]]'s own scope statement,
  which holds for criteria computed over a represented $\theta$. An asker
  whose policy already includes generation off the modelled axes (an explicit
  exploration slot, random probes, a fixed protocol) is outside the argument,
  and for it the conjecture says nothing.
- It gives no size. "Biased toward stopping" is a direction; nothing here
  estimates how many constraints an empty run misses, and no measure of
  answer novelty is fixed in this wiki to estimate it with.
- The proposed repair — an independent generator for the run — is untested and
  costs strictly more than not doing it, since those questions are chosen
  against the selection criterion. Whether the trade is worth it depends on
  the cost of a premature stop, which [[question-budgets]] records this wiki
  as not having.
- The claim is about the *confirmation* window only. It says nothing about
  whether the base $B$ or the threshold $T$ is affected, and the same
  dependence may act on those without this note noticing.

## Related

`confirmation-run-length` (draft dropped) · [[qualitative-saturation]] · [[expected-information-gain]] · [[grand-tour-question]] · [[unknown-unknowns]] · [[question-budgets]]

[^s1]: guest-2020
[^s2]: prechelt-1998
