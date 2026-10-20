---
description: "A reply can be true, direct and still not answer: completeness is a property **The desideratum (Åqvist 1965;"
aliases: ["conclusiveness condition", "desideratum of a question", "knowing-who condition", "epistemic answerhood"]
sources: ["aqvist-1965", "hintikka-1976", "hintikka-1989", "hintikka-2007", "wang-2016"]
---
# Conclusive answer

> A reply can be true, direct and still not answer: completeness is a property
> of the reply **and the asker's model together**, not of the reply.

## Definition / Mechanism

**The desideratum (Åqvist 1965; Hintikka 1976).** To ask is to issue an[^s1][^s2][^s3][^s4][^s5]
imperative: *bring it about that I know who b is.* The question's content is
therefore the epistemic state it demands — its **desideratum**. Studying
questions reduces to studying desiderata.

```text
"Who is b?"           desideratum   ∃x K(b = x)
"Who murdered b?"     desideratum   ∃x K M(x, b)
```

**The conclusiveness condition (Hintikka 1989a).** A reply "*a* murdered *b*"
gives the asker $K\,M(a,b)$. This does **not** entail $\exists x\,K\,M(x,b)$:
existential generalisation fails inside the knowledge operator. The desideratum
is met only with the extra premise $\exists x\,K(a = x)$ — the asker knows who
$a$ is. That premise is the conclusiveness condition, and it is a fact about
the asker, not about the reply. The degenerate case: *"Who gave the first
speech?" — "The first speaker."* True, direct, and worth nothing.

**Functional form (Hintikka 1996, 1999).** For a dependence question — how does
$y$ depend on $x$? — the desideratum is $\exists f\,K\,\forall x\,E(x,f(x))$.
An experiment yielding $K\,\forall x\,E(x,g(x))$ is conclusive only if
$\exists f\,K\,\forall x\,(f(x) = g(x))$: having the function is not knowing it.

**What makes it non-trivial.** Whether $\exists x\,K(b=x)$ holds depends on how
the asker cross-identifies objects across its epistemic alternatives —
Hintikka's world-lines, drawn perspectivally (acquaintance) or publicly
(description) (Hintikka 1989b). Conclusiveness is relative to a declared
identification scheme; there is no scheme-free reading (Wang 2016).

## Why it matters

1. **A second acceptance test, orthogonal to information gain.** Stall 5's other
   rows score a reply by how much it moves the distribution. This one asks
   whether the reply's referring term resolves inside the asker's own model. A
   reply may pass one and fail the other.
2. **The repair is a different question, not the same one again.** Conclusiveness
   failure has a canonical continuation: stop re-asking the original question and
   ask the identification sub-question $\exists x\,K(a=x)$ — *who is a?* In the
   interrogative model of inquiry (Hintikka 2007), a big question is answered
   through a chain of small operative questions put to a source; an unmet
   conclusiveness condition is exactly what makes the chain continue.
3. **This wiki's inference** (no source cited here states it): [[entropy]]-based
   scoring is blind to the failure in its most dangerous form. A tautological
   description leaves $H$ flat and is caught by [[surprisal]]. A *fresh opaque
   name* — "the owner of service X", "the standard config" — collapses the
   posterior onto one label and therefore scores as maximal gain, while the
   agent cannot act on the label at all. Bits measure the cut; conclusiveness
   measures whether the surviving world is reachable from what the asker already
   holds.

## Transfer

| | |
|---|---|
| **Home field** | quantified epistemic logic and the semantics of wh-questions; an ideal agent, a first-order model, logical omniscience, one fixed identification scheme |
| **Here** | an agent deciding whether a returned reply is usable as a constraint |
| **What survives** | the desideratum as the reply's acceptance test; the failure of existential generalisation as a named defect type; the identification sub-question as the standard repair; the requirement that the scheme be declared |
| **What does not** | logical omniscience — a real agent may hold the identifying fact and fail to retrieve it, which the logic cannot distinguish from not holding it; decidability — quantified epistemic logics are frequently undecidable (Wang 2016), so the theory hands over no procedure; and any graded version, since the condition is binary while every other row on this stall is in bits |

## Limits

- The condition is **binary**. There is no partial conclusiveness, no cost of
  obtaining it, and no noise model, so it cannot be traded against anything.
- Whether conclusiveness is genuinely required is context-dependent; Wang (2016)
  records that it is debatable how pervasive the requirement is. A reply naming
  an unresolvable entity is sometimes exactly enough — when the next action is to
  pass the name on unchanged.
- The test is only as sharp as the identification scheme, which the theory does
  not choose. Two schemes disagree about whether the same reply was conclusive.
- The **imperative-epistemic theory of questions** — the broader Åqvist–Hintikka
  claim that asking *is* issuing an epistemic imperative — is not covered here.
  This note takes only its answer-acceptance component; the imperative reading as
  a constraint on question *formulation* is an open gap.
- Point 3 of *Why it matters* is this wiki's own inference; no source cited here
  connects the conclusiveness condition to information-theoretic answer scoring.
- The exposition of Hintikka (1989a, 1989b, 1996, 1999) here follows Wang's
  (2016) survey, and the attribution to Åqvist (1965) follows SEP "Questions"
  §4.1; neither primary text was read for this note.

## Related

[[question-as-partition]] · [[constraint-as-information]] · [[surprisal]] · [[possible-worlds]] · [[elicitation-protocols]] · [[tacit-knowledge]]

[^s1]: aqvist-1965
[^s2]: hintikka-1976
[^s3]: hintikka-1989
[^s4]: hintikka-2007
[^s5]: wang-2016
