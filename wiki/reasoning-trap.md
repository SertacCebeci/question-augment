---
description: "Closed-system multi-agent debate forms a Markov chain over evidence and outputs, so the Data Processing Inequality bounds joint mutual information with the evidence as non-increasing round over round."
aliases: ["Debate Trap", "Reasoning Trap", "DPI Bound", "Theorem 1 (Shin 2026)"]
sources: ["shin-2026"]
---
# Reasoning Trap

> When copies of one model debate under shared weights with the evidence
> handed to them only once, expected [[mutual-information|mutual information]] between their output
> and that evidence cannot rise again — debate can preserve the *answer*
> while steadily erasing the *reasoning behind it*.

## Definition / Mechanism

Let $E$ be the evidence set for a claim and $O^t$ agent $i$'s reasoning
output at round $t$. Reasoning faithfulness is $F(t) = I(E; O^t)$ (mutual
information). Under standard multi-agent debate (MAD) — agents share
parameters $\theta$, $E$ is supplied once at $t=0$ and never re-injected,
round $t{+}1$ depends only on round $t$ and $\theta$, and aggregation is
symmetric — the sequence $E \to O^0 \to O^1 \to \cdots \to O^T$ is a Markov
chain, so by the Data Processing Inequality
$\mathbb{E}[I(E; O^{t+1})] \le \mathbb{E}[I(E; O^t)]$: faithfulness is
non-increasing in expectation along the debate trajectory, strictly so
whenever the round's aggregation step is non-injective (majority voting,
summary aggregation).[^c1]

The bound generalises to any protocol satisfying the same four conditions —
the paper checks single-agent Chain-of-Thought, Reflexion-style
self-critique and linear Tree-of-Thought traversal against them and finds
all four apply, while Self-Consistency and Mixture-of-Experts (which break
condition (i) or (iii)) fall outside it. A vote-aggregating protocol is
additionally floored: reducing the final output to a $K$-way vote tally
caps $I(E; O^T) \le \log_2 K$ regardless of the evidence's own [[entropy]]
$H(E)$, independent of how much was known before the vote.[^c2]

Empirically, in the 16-condition SciFact/FEVER evaluation, the "Trap
proper" debate configuration (DebateCV) retains 88% of baseline answer
accuracy while its Supported Faithfulness Score ([[supported-faithfulness-score]])
drops 43%; majority-vote debate collapses faithfulness to 1.7% of baseline
(Wilcoxon $p<10^{-6}$, Cohen's $d=-0.96$), consistent with the
vote-aggregation floor.[^c3]

## Known as

| Field | Name | Relation |
|---|---|---|
| multi-agent-reasoning (this paper, general case) | Reasoning Trap | exact — the paper's name for the phenomenon this theorem bounds |
| multi-agent-reasoning (this paper, MAD instance) | Debate Trap | exact — the same theorem read on standard multi-agent debate specifically (accuracy preserved, faithfulness measurably drops, Definition 2) |
| information theory | closed-system application of the Data Processing Inequality | close — same inequality, applied to a reasoning chain rather than a single observation channel; see `## Transfer` |

## Why it matters

For a wiki about asking, this is a bound on **self-questioning inside a
closed loop**: agents that only ever condition on each other's prior
outputs cannot, in expectation, recover evidence-grounding they did not
already have — no matter how many rounds or how the rounds are aggregated.
It is the multi-step, multi-agent generalisation of what
[[data-processing-inequality]] already says about a single agent answering
its own questions, instantiated and measured for debate specifically.

## Transfer

| | |
|---|---|
| **Home field** | information theory: the Data Processing Inequality for a Markov chain $X \to Y \to Z$ |
| **Here** | a multi-round, multi-agent reasoning trace treated as a Markov chain $E \to O^0 \to O^1 \to \cdots$, with faithfulness read as $I(E; O^t)$ |
| **What survives** | the monotone-non-increase ordering, and its strict form under any non-injective (vote-like) aggregation step |
| **What does not** | the four preconditions are load-bearing and checkable per protocol (shared $\theta$, evidence given once, round-$t{+}1$ depends only on round $t$, symmetric aggregation); heterogeneous-agent debate only weakens, not removes, the bound, and any evidence-reinjecting variant (e.g. [[evidence-grounded-socratic-reasoning]]) is explicitly outside its scope by construction |

## Limits

This note's claim rests entirely on the paper's own four-condition
characterisation of "closed-system": a protocol that looks like debate but
violates one condition (distinct weights per agent, evidence re-supplied
mid-round) is not covered, and the paper states the generalisation beyond
MAD to CoT/Reflexion/ToT as a "conditional extension" and "falsifiable
research program," not a tested claim across paradigms — the empirical core
is MAD only. The quantitative 88%/43%/1.7% figures are measured with one
metric (SFS) on two datasets (SciFact, FEVER) and one metric family; they
are cited here as the paper's own diagnostic evidence, not replicated
elsewhere. `shin-2026` is a single-author 2026 arXiv preprint and this
note's numbers are `[?]` pending independent verification.

## Related

[[data-processing-inequality]] · [[mutual-information]] · [[evidence-grounded-socratic-reasoning]] · [[supported-faithfulness-score]]

[^c1]: shin-2026
[^c2]: shin-2026 — "Proposition 1 (Vote-Aggregation Floor). Let VK denote a verdict space of size K. Under any protocol whose final output strips atomic claims and reduces OT to a vote tally v ∈ VK , the operational faithfulness satisfies SFS(OT ) → 0 as the vote tally contains no atomic claims to verify against E. Equivalently, I(E; OT ) ≤ H(v) ≤ log2 K regardless of H(E)"
[^c3]: shin-2026 — "Across 16 experimental conditions, the Trap-proper configuration (DebateCV, C13) preserves 88% of baseline accuracy while our Supported Faithfulness Score (SFS) drops by 43%; in the extreme, majority-vote debate (C15) reduces evidence grounding to 1.7% of baseline (Wilcoxon p < 10−6 , Cohen’s d = −0.96)."
