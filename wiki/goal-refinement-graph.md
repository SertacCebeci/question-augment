---
description: "The one field that turns elicited answers into a specification for a living, KAOS (Dardenne, van Lamsweerde & Fickas 1993) models what is wanted as an AND/OR graph of **goals**."
aliases: ["goal model", "goal refinement tree", "AND/OR goal graph", "KAOS goal model"]
sources: ["dardenne-1993", "letier-2002", "van-lamsweerde-2001", "yu-1997", "arxiv-2512-24119"]
---
# Goal refinement graph

> The one field that turns elicited answers into a specification for a living,
> and does it with two checkable conditions: every element of the distillate
> must be used in a proof, and refinement stops when a leaf has exactly one
> owner.

## Definition / Mechanism

KAOS (Dardenne, van Lamsweerde & Fickas 1993) models what is wanted as an[^s1][^s2][^s3][^s4]
AND/OR graph of **goals**. An AND-refinement says satisfying all subgoals
suffices for the parent; an OR-refinement says satisfying one alternative
suffices. Three conditions do the work (van Lamsweerde 2001):

**Completeness.** With $R$ the requirements, $As$ the environmental
assumptions, $D$ the domain properties and $G$ the goals, the specification is
complete iff for every $g \in G$:

$$R, As, D \models g \quad\text{and}\quad R, As, D \not\models \text{false}$$

**Pertinence.** A requirement belongs in the specification only if *its
specification is used in the proof of at least one goal* (attributed to
Yue 1987). The check is a proof-usage check, not an intuition: an element that
appears in no proof is not a requirement but a hidden assumption.

**Termination.** Refine until each leaf is assignable to a **single agent**. A
leaf owned by an agent in the system-to-be is a *requirement*; one owned by an
agent in the environment is an *assumption* — an obligation the distillate
cannot enforce, only hope for. Letier & van Lamsweerde (2002) give the
realizability conditions an assignment must meet: the agent must be able to
**monitor** the variables in the goal's antecedent and **control** those in its
consequent, and they supply refinement tactics for when it cannot.

The graph is also a **question generator**: asking HOW about a goal produces
subgoals, asking WHY produces the parent goal that was left implicit
(van Lamsweerde 2001, §5.3). New axes appear from a structural operation on
what is already written, not from new observation.

## Known as

| Name | Relation |
|---|---|
| KAOS goal model | exact |
| AND/OR goal graph | exact |
| goal refinement tree | exact |
| goal-oriented RE (GORE) | close — a family of approaches including i\* and the NFR framework; the entailment-based conditions above are KAOS's alone |

## Why it matters

Stall 8 had a definition of distillation and no procedure. This supplies one:
a distillate is finished when (a) the goals are entailed, (b) nothing in it is
unused, and (c) every leaf has one owner. (c) is an *internal* termination
criterion — unlike every stopping rule in Stopping, the threshold is
not a number someone supplies. And the requirement/assumption split makes the
[[constraint-as-information]] point structural: what the system cannot enforce
is labelled rather than silently absorbed.

## Transfer

| | Home field | Here |
|---|---|---|
| Object | a software specification | the distillate of a question–answer record |
| $G$ | elicited stakeholder goals | the constraints the answers supplied |
| Check | $R, As, D \models g$, machine-checkable in real-time temporal logic | the same check, only as strong as the formalisation you can afford |
| What survives | pertinence as a usage test; single-agent assignability as a termination criterion; HOW/WHY as refinement and abstraction operators | |
| What does not | the entailment itself. KAOS's formal layer is "2-button" and optional, used in practice for critical aspects only; soft goals admit no clear-cut satisfaction, only qualitative [[bounded-rationality|satisficing]] labels | |

## Limits

- **Completeness is relative to $G$.** A goal nobody stated is invisible to the
  entailment check — the same failure [[issue-tree]] names for MECE, and the
  reason [[unknown-unknowns]] is not addressed by any of this.
- **The author's own open problem.** Which alternative OR-refinement, and which
  agent assignment, to select "is by and large an open problem… a systematic
  approach has not emerged so far in the RE literature" (van Lamsweerde 2001,
  §5.6). The graph structures the choice; it does not make it.
- **Soft goals are outside the formalism.** Satisficing is propagated as
  qualitative labels, so the pertinence and completeness tests do not apply to
  exactly the goals most likely to be contested.
- **i\* is a different object.** Yu (1997) models intentional *dependencies
  between actors*, not refinement with entailment semantics; the checkable
  conditions above are KAOS's, and citing "goal-oriented RE" for them
  overstates i\*.
- **The reading of pertinence against [[sufficient-statistic|sufficiency]] is this wiki's, not the
  literature's.** See Related below; neither van Lamsweerde 2001 nor the
  statistics literature draws the comparison.

## Related

[[sufficient-statistic]] · [[issue-tree]] · [[constraint-as-information]] · [[data-processing-inequality]] · [[unknown-unknowns]] · [[context-free-questions]]

This wiki reads pertinence as the operational, checkable counterpart of what
[[sufficient-statistic]] states as a bound: sufficiency says the distillate may
lose nothing about $\theta$, pertinence says it may contain nothing unused in a
goal's proof. The two bounds point in opposite directions and no source joins
them; the comparison is this note's inference.

A measured counterpart of the usage test now exists for models: GeoBench asks multimodal LLMs which given condition a geometry proof never uses, and finds that this sub-skill is among the strongest correlates of their solving accuracy.[^s5] See [[irrelevant-premise-filtering]].

[^s1]: dardenne-1993
[^s2]: letier-2002
[^s3]: van-lamsweerde-2001
[^s4]: yu-1997
[^s5]: arxiv-2512-24119 — "Among them, task I.P.F., S.D., and T.S. show the strongest correlations"
