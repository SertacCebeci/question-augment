---
description: "Widening and narrowing cannot happen at once. Creating and judging are ```text DIVERGE generate options — NO judgement, NO answers, NO elimination CONVERGE eliminate options — apply criteria, rank,"
aliases: ["diverge/converge"]
sources: ["osborn-1953", "parnes-1959", "diehl-1987", "designcouncil-2007", "shannon-1956", "arxiv-2512-23601", "arxiv-2512-04488"]
---
# The divergent / convergent split

> Widening and narrowing cannot happen at once. Creating and judging are
> separate phases — the framework says they must be separated, not where the
> seam falls.

## Principle

```text[^s1][^s2][^s3][^s4][^s5]
DIVERGE   generate options   — NO judgement, NO answers, NO elimination
CONVERGE  eliminate options  — apply criteria, rank, choose
```

Mixed together, both degrade: early judgement dries up production, late
judgement makes deciding impossible.

## Where it appears

[[question-formulation-technique]] (produce → prioritize),
[[question-burst]] (generate → select); the **double diamond** — a four-phase
process model (Discover / Define, Develop / Deliver) built by the Design
Council's design and innovation team in 2004 and published in *Eleven
Lessons: Managing Design in Eleven Global Brands* (`designcouncil-2007`),
which runs the split twice, once over the problem and once over the
solution; and **Osborn's brainstorming rules** (Osborn 1953, *Applied
Imagination*), whose first rule — defer judgement — is the divergent half
stated as a rule for a group.

## Known as

| Field | Name there | Same thing? |
|---|---|---|
| Design methods | diverge/converge | exact — the same abstract split, phase for phase |
| Design methods | double diamond | close — an **instantiation**: it fixes the number of phases at four and adds a problem-before-solution ordering that the bare split does not carry |
| Creativity research | Osborn's brainstorming rules | **not this concept** — a specific rule set (defer judgement, quantity, wild ideas, combine) for the divergent phase of a *group*, with an empirical record of its own (Parnes & Meadow 1959; Diehl & Stroebe 1987) that does not attach to the general split |

The split has also been written into an LLM prompt. In a study of programming-task generation, one stage asks the model to "explore the thematic space of context C without imposing any constraints from the target programming concept," and a second stage selects "promising idea from the brainstormed list and refine it into a valid programming task."[^s6] The authors state the principle in the same terms as this note: "Divergent thinking aims to generate many diverse ideas without judgment, while convergent thinking selects and refines the best ideas into a concrete solution."[^s6] The measure of success there is [[effective-diversity]], the count of distinct tasks among those that pass a utility check.

## Why it matters

The information-theoretic reading of "generate first, answer none" is owned
by [[channel-capacity]] — feedback buys efficiency, not reach — together
with the Transfer that licenses it; this note does not restate it. What this
note contributes is the split as a **scheduling constraint** on asking: no
elimination step may run while options are still being produced, and no
production step may run once criteria are being applied.

> **Conjecture (this wiki):** batch and adaptive asking are not rivals but
> each correct in its own phase — batch during divergence, adaptive during
> convergence. This is an inference from the analogy in the Transfer below,
> established nowhere in the literature cited here.

**What the framework cannot decide.** It does not locate its own seam: for
any concrete asking episode it gives no criterion, and no measurement, for
where divergence ends and convergence begins. Any transition rule is
imported from outside it.

## Transition criterion

| | Criterion | Standing |
|---|---|---|
| Practical | the rate of new-axis discovery drops | craft rule from the design-methods sources; "axis" is undefined |
| Theoretical | the marginal [[mutual-information]] of a new question falls below the cost of ranking it | **conjecture (this wiki)** — rests on the analogy below, not on a result |

## Transfer

The import is $C_{FB} = C$ (Shannon 1956), mapped here onto a
*judgement-free generation phase* — a different mapping from
[[channel-capacity]]'s batch-vs-adaptive one, so it carries its own
preconditions.

| | In its home field | Here |
|---|---|---|
| The object | a discrete memoryless channel: a fixed, known law $p(y\mid x)$ over a fixed input alphabet | the divergence phase — questions produced while no answer is returned |
| Feedback | the receiver returns each output before the next symbol is sent | the asker reads an answer before writing the next question |
| What survives | feedback does not raise capacity; it buys scheme complexity, delay and error exponent | the structural expectation that withholding answers during generation costs *route*, not *reach*, and that answering during convergence shortens the route |
| What does not | $C_{FB}=C$ is a **memoryless, asymptotic** equality over a fixed input alphabet | during divergence the axis set is still being created, so there is no fixed input alphabet and no channel held constant across the phase; "not answering during divergence loses no information" is therefore an **analogy, not a consequence** of the theorem, and no numeric $C$ exists to check it against |

## Limits

- `osborn-1953` is `[?]` — cited but not confirmed.
- **The note's own claim rests on evidence for one half only.** Deferred
  judgement is measured on the divergent side — Parnes & Meadow (1959,
  *J. Educ. Psychol.*) found brainstorming instructions raised the
  production of good ideas — while nothing cited here measures the
  convergent half, and no source cited measures the split as a whole
  against a mixed mode. The scheduling constraint is therefore
  half-supported.
- The mixed part of Osborn's record is about *groups*, not about the split:
  Diehl & Stroebe (1987, *JPSP*) found real brainstorming groups
  underproduce nominal groups mostly through **production blocking** — only
  one member may speak at a time — with free riding and evaluation
  apprehension smaller contributors. That is a defect of the group
  procedure, not evidence against separating generation from judgement.
- The transition criterion — "rate of new-axis discovery drops" — has no
  defined measurement of "axis".
- **The split has been compared against a mixed mode, once, in LLM output.** The prompting study reports that its two-stage prompt yields "significantly more distinct high-utility tasks (about 1.6×) than baselines," where the baselines give theme and concept together.[^s7] This narrows the half-support above but does not close it. The two-stage prompt also tells the model to "go back to select another idea and try again" when a candidate fails, so the stage split and the retry instruction are bundled, and no arm separates them.[^s8] The gain therefore cannot be assigned to the scheduling constraint alone; that attribution is my inference from the prompts, not a result of the study. The study is one generator and one domain.

## Mixed-mode comparison in LLM agents

One brainstorming study compares three arms with two persona-bearing LLM
agents: separate ideation, where the agents "work in parallel without mutual
awareness"; together from the start; and separate-then-together.[^s9] Cluster
purity, which measures how distinct each agent's ideas stay, was highest in
separate ideation: the study reports that separate ideation "produced the
highest purity, reflecting stronger within-agent" clustering.[^s10] Purity
fell in the other two arms: "The together and separate-then-together modes
have reduced purity as agents integrated" each other's ideas.[^s11] The staged
arm had the strongest overall LLM-graded result,[^s12] and depth and novelty
rose across the sequence from separate to together to staged.[^s13]

Read against the split, isolation keeps the two generators apart, pooling
mixes them, and the staged arm is the diverge-then-converge order. That
mapping is my inference: the study asks which collaboration mode diversifies
ideas, not whether a scheduling constraint holds. It bears on the mixed-mode
gap named under Limits, for LLM agents rather than human groups. Its measures
are embedding-cluster purity and LLM-assigned grades, with one question and no
human rater, so it narrows the gap without closing it.

## Related

[[question-formulation-technique]] · [[question-burst]] · [[channel-capacity]] · [[adaptive-submodularity]] · [[mutual-information]]

[^s1]: osborn-1953
[^s2]: parnes-1959
[^s3]: diehl-1987
[^s4]: designcouncil-2007
[^s5]: shannon-1956
[^s6]: arxiv-2512-23601 — "explore the thematic space of context C without imposing any constraints from the target programming concept"
[^s7]: arxiv-2512-23601 — "significantly more distinct high-utility tasks (about 1.6×) than baselines"
[^s8]: arxiv-2512-23601 — "go back to select another idea and try again"
[^s9]: arxiv-2512-04488 — "where agents work in parallel without mutual awareness."
[^s10]: arxiv-2512-04488 — "produced the highest purity, reflecting stronger within-agent"
[^s11]: arxiv-2512-04488 — "The together and separate-then-together modes have reduced purity as agents integrated"
[^s12]: arxiv-2512-04488 — "yielded the strongest overall performance, balancing divergent exploration with convergent"
[^s13]: arxiv-2512-04488 — "gains in Depth but steady increases in Novelty"
