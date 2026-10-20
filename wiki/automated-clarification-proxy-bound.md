---
description: "Proves automated disambiguation evidence gathered without asking is capped by what an ideal human clarification answer would reveal about true intent, under a sufficiency assumption."
aliases: ["automated proxy for clarification", "Proposition 1 (Somayajula et al. 2026)"]
sources: ["somayajula-2026"]
---
# Automated-clarification-proxy bound

> Executing probes against the environment can only ever approach, never
> exceed, what asking the user directly would have revealed about intent.

## Definition / Mechanism

Somayajula, Liu & Lei (2026) model an NL2SQL question's
unobserved true intent as a random variable $Z$, an ideal human
clarification answer as $U$, and SOMA-SQL's automated evidence — candidate
SQL disagreement plus [[ambiguity-driven-execution-probing|probe execution
results]] — as $Y$. Their Proposition 1 states: "Proposition 1 (Automated
proxy for clarification). For (x, S), suppose the automated proxy Y is a
noisy approximation of the ideal human clarification signal U in the sense
that, after conditioning on U and (x, S), observing Y provides no further
information about Z. Then, I(Z; Y | x, S) ≤ I(Z; U | x, S). Thus, human
clarification is an information-theoretic ceiling, and SOMA-SQL constructs
a tractable automated proxy below this ceiling."[^c1]

The paper further argues the gap is not fixed: "Real database workloads are
repetitive: for a fixed schema S, many questions follow recurring intent
patterns. As historical log covers these patterns, retrieved [[efe-planning-as-variational-inference|ambiguity]]
records Cx recover previously resolved ambiguity decisions, narrowing the
gap between I(Z; Y | x, S) and I(Z; U | x, S). The remaining gap is
concentrated on rare or novel intents where the log lacks precedent."[^c2]

## Why it matters

For stall 4, this gives the actual license for treating execution as an
answerer at all: it says such a substitute is bounded by, not free to
exceed, the human source it replaces, and names *where* the bound is loose
(novel intents with no query-log precedent) — turning "does the agent need
to ask?" into a question about how repetitive the workload is.

## Transfer

| | |
|---|---|
| In its home field | The data-processing/[[sufficient-statistic|sufficiency]] inequality: if $Y$ carries no information about $Z$ beyond what $U$ already carries (a Markov-style sufficiency condition), then $I(Z;Y)\le I(Z;U)$ — a direct instance of the reasoning behind [[data-processing-inequality]]. |
| Here | $Z$ is the user's unobserved SQL intent, $U$ the answer a human would give to a clarification question, $Y$ the evidence SOMA-SQL assembles from candidate disagreement and executed probes instead of asking. |
| What survives | The ordering itself: no automated evidence-gathering procedure can, in expectation, extract more about intent than the human answer it substitutes for — a ceiling on what asking-the-database can do relative to asking-the-user. |
| What does not | The premise is asserted, not verified: it requires that $Y$ be conditionally independent of $Z$ given $U$ and $(x,S)$ — the paper gives no test for when execution evidence satisfies this, only the historical-log argument for why the gap should shrink on repeated schemas. |

## Limits

The bound rests entirely on an unverified sufficiency assumption about $Y$
given $U$; the paper offers no independent measurement of $I(Z;U\mid x,S)$
or $I(Z;Y\mid x,S)$ to confirm the gap empirically; it argues the ordering
must hold if the premise holds, and gives a plausibility argument (log
coverage) rather than evidence for the premise itself.

## Related

[[ambiguity-driven-execution-probing]] · [[data-processing-inequality]] · [[text-to-sql-ambiguity-taxonomy]] · [[mutual-information]]

[^c1]: somayajula-2026
[^c2]: somayajula-2026 — "Real database workloads are repetitive: for a fixed schema S, many questions follow recurring intent patterns. As historical log covers these patterns, retrieved ambiguity records Cx recover previously resolved ambiguity decisions, narrowing the gap between I(Z; Y | x, S) and I(Z; U | x, S). The remaining gap is concentrated on rare or novel intents where the log lacks precedent."
