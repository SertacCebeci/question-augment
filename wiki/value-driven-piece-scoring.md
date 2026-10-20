---
description: "Score each candidate reasoning step of a solution on novelty, difficulty and impact, min-max normalize within the problem, and reveal only the top-scoring ones as hints."
aliases: ["value-driven piece identification", "bottleneck-value scoring", "PieceHint value scoring"]
sources: ["arxiv-2604-15830"]
---
# Value-driven piece scoring

> Not every step of a solution is worth revealing as a hint — score the steps, and only the pivotal ones earn one.

## Definition / Mechanism

Given a ground-truth solution parsed into reasoning pieces $P(q) = \{p_1, \dots, p_n\}$ — each a logically complete step such as a lemma, a key substitution or a non-obvious insight — a stronger LLM assigns each piece a discrete value score on three criteria: novelty (is the insight non-trivial), difficulty (does deriving it demand mathematical maturity), and impact (does later reasoning critically depend on it), as proposed for RL training of LLM reasoners by Fang et al. (2026).[^c1]

Scores are min-max normalized within each problem, $D(p_i) = \frac{V(p_i) - V_{min}}{V_{max} - V_{min}}$, so values are comparable across problems of different absolute difficulty; the top pieces by this normalized value are then the ones offered as hints, rather than the first steps in solution order.[^c2]

## Why it matters

Against two alternative ways of choosing which piece to reveal — position-based (truncating a fixed prefix of the solution, e.g. the first 25% or 50%) and random selection — value-driven scoring wins consistently: prefix truncation wastes hints on routine early steps the model already handles and misses bottlenecks that appear later, random selection hits bottlenecks only by chance, while scoring finds the pivotal lemmas and key insights "regardless of position." A case study on a combinatorial word problem makes the difference concrete: "50% prefix wastes hints on routine steps the model can handle; random selection hits bottlenecks inefficiently; PieceHint identifies where models actually struggle and strategically bridges these gaps."[^c4]

This is a general answer to "which of several candidate disclosures is worth making now": rank candidates by an estimate of how much each would unblock the recipient, not by where each sits in a fixed sequence.

## Limits

The value score comes from a single stronger LLM judge on a fixed rubric (novelty, difficulty, impact); the work does not report inter-judge agreement or sensitivity to the judge model. Min-max normalization is per-problem, so a problem with uniformly low-value pieces still yields a normalized top-k, i.e. the mechanism can manufacture apparent bottlenecks out of a solution that has none. Demonstrated only on mathematical reasoning solutions with a clean step decomposition; whether "reasoning piece" parses cleanly in less formal domains is unverified.

## Related

- [[curriculum-sequencing-policy]] — also splits "what to reveal/ask next" from execution, but sequences prerequisite topics rather than scoring solution steps.
- [[expected-information-gain]] — a different basis for ranking candidates, by expected reduction in uncertainty rather than by an LLM-judged novelty/difficulty/impact rubric.
- [[progressive-piece-withdrawal]] — the companion mechanism that removes these scored pieces over training, lowest value first.

[^c1]: arxiv-2604-15830 — "We employ a stronger LLM to assign each piece a discrete value score V (pi ) based on three criteria: (1) novelty—whether the insight is non-trivial, (2) difficulty—whether deriving this step demands mathematical maturity, and (3) impact—whether subsequent reasoning critically depends on this result."
[^c2]: arxiv-2604-15830 — "we normalize scores within each problem via min-max normalization"
[^c4]: arxiv-2604-15830 — "50% prefix wastes hints on routine steps the model can handle; random selection hits bottlenecks inefficiently; PieceHint identifies where models actually struggle and strategically bridges these gaps."
