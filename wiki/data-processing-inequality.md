---
description: "Information is never created by processing. Only preserved or lost. If $X \\to Y \\to Z$ forms a Markov chain: No amount of processing of $Y$ can produce information about $X$ that was not in $Y$."
aliases: ["DPI"]
sources: ["cover-2006", "mit-ocw-6-441-lecture-notes"]
---
# Data processing inequality

> Information is never created by processing. Only preserved or lost.

## Theorem

If $X \to Y \to Z$ forms a Markov chain:[^s1][^s2]

$$I(X;Z) \leq I(X;Y)$$

No amount of processing of $Y$ can produce information about $X$ that was not
in $Y$.

This is the data-processing inequality, a standard result of classical
information theory; statement and proof in Cover & Thomas, *Elements of
Information Theory* (2006) `cover-2006`, with the same treatment beside the
chain rules in the MIT OCW 6.441 lecture notes `mit-ocw-6-441-lecture-notes`.

## Transfer

| | |
|---|---|
| **Observation (home field)** | random variables with a joint law; $I$ is an expectation over that law |
| **Here** | one natural-language answer produced by an agent: $X$ the external fact, $Y$ the agent's weights plus context, $Z$ its output |
| **What survives** | the ordering $I(X;Z) \le I(X;Y)$ — no post-hoc processing adds information about a fixed $X$ |
| **What does not** | the Markov chain is assumed, not verified: an agent that covertly reaches $X$ (a tool call, retrieval) breaks it. And no quantitative bound transfers — $I(X;Y)$ for weights + context is unobservable, so the inequality gives a direction, not a number, and says nothing about how much of it is surfaceable |

## The hard consequence

The theorem above is Cover & Thomas; the reading below is this wiki's
inference from it (conjecture), not a result.

```text
If the agent generates and answers its own questions,
it cannot produce information that is absent from both
its weights and its context.
```

10,000 questions make the model's **latent** knowledge explicit — a real and
valuable operation, because explicit knowledge can be conditioned on in later
steps. But it brings in no **new** information.

Three sources of new information are identifiable here (this wiki's
classification, not an exhaustive result):

1. **The user** — intent that lives in their head, not the model's
2. **The external world** — reading files, searching, executing
3. **Commitment** — making an arbitrary choice and binding to it (this
   creates a new constraint; see [[constraint-as-information]])

The third is placed outside the inequality by construction: $X$ is
undetermined, so there is nothing to extract and the ordering does not apply.
That placement is a modelling choice, not a consequence of the theorem.

## Practical reading

The split decides what a self-answered question is worth. For questions
**about the external world** the inequality binds, and a fabricated answer is
noise, not a constraint on $X$. For **commitment questions** it does not
bind — there the answer is true by construction, because it is the answer
that fixes $X$.

## Limits

- Holds for Markov chains $X \to Y \to Z$. Reading the agent as $Y$ (weights
  + context) and its outputs as $Z$ is reasonable, but it makes the bound
  relative to what is *already in* weights and context — which is not
  observable.
- Commitment is placed outside the inequality by fiat ($X$ undefined). That is
  a modelling choice, not a theorem.
- The three sources of new information are an enumeration by this wiki, not a
  proved partition; a fourth channel — a tool the agent may call — sits under
  "the external world" only by stipulation.
- Says nothing about how much of $I(X;Y)$ the agent can actually *surface*.
- `cover-2006` and `mit-ocw-6-441-lecture-notes` carry `verified: prior`
  rather than a verification date, so both count as `[?]` until re-checked;
  the theorem statement is textbook-standard, the page and theorem number are
  not asserted here.

## Related

[[mutual-information]] · [[constraint-as-information]] · [[semantic-entropy]]

[^s1]: cover-2006
[^s2]: mit-ocw-6-441-lecture-notes
