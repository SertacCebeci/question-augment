---
description: "A multi-round dialogue strategy that picks the next question not to fill a known axis but to discover which axis a tacit, unarticulated unease is about, stopping once a friction point is concrete."
aliases: ["Socratic Elicitation", "E operator", "EVN elicitation stage"]
sources: ["yu-2026-more"]
---
# Friction-point elicitation

> Before an axis can be selected by any of the criteria on this stall, the
> asker may not know what the axis is: this is the pipeline stage that
> exists to find it, by dialogue rather than by scoring over a defined set
> of candidates.

## Definition / Mechanism

InciteResearch's [[staged-socratic-hint-policy|Socratic]]-Elicitation (E) stage takes an arbitrary vague
input $t_0$ and runs multi-round human-machine dialogue to externalise it
into a five-dimensional **researcher profile** state: "we represent the
cognitive state in the research process as the vector $P_{profile} =
(f, m, c, r, t)$, corresponding to five core dimensions: Friction Points
$f$, research motivation $m$, constraints $c$, research taste $r$, and
refined topic $t$."[^c1]

The first question $q_1$ is chosen to locate the most central friction
point: "the goal of generating $q_1$ is to maximize the amount of user
information obtained in the subsequent dialogue, that is, to select the
question that maximally reduces the expected uncertainty of the researcher
profile."[^c2]

Every later turn is routed by a dynamic triage-and-deepen rule rather than
a fixed script, ending only when a clear friction point is identified, not
at a fixed turn count: "InciteResearch performs triage to evaluate the
information density. If the response contains concrete friction points,
the system executes deepening to probe the underlying causes; if the
response is vague, InciteResearch switches the analytical angle; if the
response implies resource restrictions, InciteResearch elicits formal
boundary constraints."[^c3]

An ablation that removes this stage from the full pipeline (keeping
assumption-violation and necessity-checking) shows it is load-bearing, not
cosmetic: "When removing the E operator, it causes the second largest
decline in novelty, from 4.250 to 3.730, while impact also drops from
4.397 to 4.132 ... proving that human inspiration [is] structurally
important in the current implementation."[^c4]

## Transfer

| | |
|---|---|
| Home field | Bayesian experiment design / information theory: [[expected-information-gain]] scores a candidate question by the expected drop in [[entropy]] of a formally defined distribution over hypotheses. |
| Here | The same verbal goal — ask what most reduces expected uncertainty — is stated as the design intent for $q_1$, but over an *undefined* tacit state: no distribution over $P_{profile}$ values is ever specified. |
| What survives | The ordering principle (question value ∝ expected uncertainty removed) and the two-mode fallback (deepen vs. switch) as a usable heuristic when no formal [[possible-worlds|hypothesis space]] exists yet. |
| What does not | Any computation. No prior, no likelihood, no number is produced or reported for "expected uncertainty reduced" — it is asserted, not measured, so the note cannot claim EIG's guarantees (Lindley optimality, greedy near-optimality) transfer with it. |

## Limits

- The uncertainty-reduction claim for $q_1$ is a stated design goal, not a
  computed quantity: the paper defines no probability distribution over
  $P_{profile}$ and reports no measurement of how much uncertainty a given
  question removed, so it cannot be checked against the EIG criterion it
  echoes.
- Evidence for the stage's effect is one ablation on the authors' own
  benchmark, scored by LLM judges (novelty/feasibility/impact, 1–5) with a
  human check on only 26 proposals in one of four domains
  (κ = 0.624 LLM–human agreement); no independent replication.
- Single arXiv preprint (2026), not peer reviewed; the five-dimension
  profile schema $(f,m,c,r,t)$ is fixed by the authors a priori and its
  [[sufficient-statistic|sufficiency]] for domains outside the four benchmark modes is untested.

## Related

[[expected-information-gain]] · [[mutual-information]] · [[socratic-method]] · [[five-whys]]

[^c1]: yu-2026-more — "we represent the cognitive state in the research process as the vector Pprofile = (f, m, c, r, t), corresponding to five core dimensions: Friction Points f , research motivation m, constraints c, research taste r, and refined topic t."
[^c2]: yu-2026-more — "The goal of generating q1 is to maximize the amount of user information obtained in the subsequent dialogue, that is, to select the question that maximally reduces the expected uncertainty of the researcher profile."
[^c3]: yu-2026-more — "InciteResearch performs triage to evaluate the information density. If the response contains concrete friction points, the system executes deepening to probe the underlying causes; if the response is vague, InciteResearch switches the analytical angle; if the response implies resource restrictions, InciteResearch elicits formal boundary constraints."
[^c4]: yu-2026-more
