---
description: "Deriving contradiction through questions. Exposing someone's inconsistency The practice is Plato's Socrates in the early dialogues (4th c. BCE);"
aliases: ["elenchus"]
sources: ["vlastos-1983", "clark-2015"]
---
# Socratic method / elenchus

> Deriving contradiction through questions. Exposing someone's inconsistency
> without asserting anything.

## Mechanism

The practice is Plato's Socrates in the early dialogues (4th c. BCE); the[^s1][^s2]
schema below is the reconstruction Vlastos (1983) called the **standard
elenchus**.

```text
1. The interlocutor asserts a thesis          T   (Socrates takes T to be false)
2. Questions elicit further premises the
   interlocutor also grants                   P1, P2, ...
3. Socrates argues — and the interlocutor
   agrees — that  P1 ∧ P2 ∧ ... ⊢ ¬T
4. Socrates claims T has been shown false;
   he asserted none of P1, P2 in his own name
```

Vlastos (1983) also named the gap in it, *the problem of the elenchus*: step 4
does not follow from step 3. An inconsistent set $\{T, P_1, P_2\}$ shows only
that its members cannot all be true — not which one to give up. Vlastos's
proposed repair is an unstated [[staged-socratic-hint-policy|Socratic]] assumption: whoever holds a false
moral belief also holds true beliefs that entail its negation, so the
inconsistency always falls on $T$.

## Known as

| Field | Name there | Relation |
|---|---|---|
| Ancient philosophy | elenchus / elenchos (ἔλεγχος) | `exact` |
| Education, cognitive behavioural therapy | Socratic questioning, guided discovery | **not this concept** |

*Socratic questioning* in CBT is defined as guided discovery — questions that
lead the client to construct an appraisal they had not articulated, ending in
a new belief rather than in aporia (Clark & Egan 2015, who also report that no
direct evidence establishes it as the beneficial ingredient of CBT). Its
endpoint is constructive where the elenchus is purely refutative, so it is a
different object and was removed from this note's aliases rather than kept as
an alias.

## Its defining feature: aporia

The aim is not to supply the right answer but to **remove false certainty**.
The outcome is usually not knowledge but the interlocutor's realisation "I did
not know."

## Transfer

The wiki reads aporia in information-theoretic terms. That import is only
partial:

| | |
|---|---|
| In its home field | [[entropy|Shannon entropy]] $H$ of a probability distribution over a defined, exhaustive outcome set; a number in bits, additive over independent variables. |
| Here | The interlocutor's implicit distribution over answers to $T$. The elenchus neither elicits it nor measures it; it records only that a certainty was withdrawn. |
| What survives | The direction and its evaluative consequence: an answer that destroys a false certainty *raises* admissible uncertainty and is still a good answer. Rising uncertainty is not by itself a failed answer. |
| What does not | Every number. No outcome set is defined, so there is no $H$, no bits, no additivity, no before/after difference, no way to rank two elenchoi by magnitude — and no ground for calling the post-aporia state the "true" $H$: the method supplies no distribution at all, only the withdrawal of one. |

## Why it matters

**This wiki's reading — a conjecture, not a claim in the literature:** the
elenchus is the classical counterpart of a *silent fork*, a
[[maximum-entropy-principle]] violation. If a model (or a person) silently
picked a value on an unasked axis, elenctic questioning makes the pick
visible by forcing the premises that fix it into the open. Nothing in
Vlastos (1983) frames the elenchus in these terms; the bridge is this wiki's
and is untested.

## Limits

- The schema and the *problem of the elenchus* here are taken from secondary
  summaries of `vlastos-1983`, not from the article read in full — `[?]`
  until the verifier confirms. Vlastos's is also one reconstruction among
  several contested ones; no rival reading has been checked here.
- The entropy account of aporia is this wiki's **analogy**, not a
  measurement: no distribution over answers is defined and no $H$ of an
  interlocutor is ever observed. Compare the Neyman–Pearson analogy in
  [[dialectic-red-team]].
- Refutes; does not construct. Aporia is the end state.
- Step 3 identifies an inconsistent set, not a culprit: the method does not
  say which belief falls, and Vlastos's repair needs an extra assumption
  about the interlocutor's other beliefs.
- Requires an interlocutor who commits to theses, and historically a
  questioner who already knows the contradiction; nothing in the method says
  how to find one.

## Related

[[premortem]] · [[maximum-entropy-principle]] · [[unknown-unknowns]] · [[dialectic-red-team]]

[^s1]: vlastos-1983
[^s2]: clark-2015
