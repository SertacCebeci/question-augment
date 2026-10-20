---
description: "A deterministic Twenty-Questions benchmark over a finite attribute table with an exact dynamic-programming oracle, scoring an agent by the extra questions it asks beyond the provably optimal count."
aliases: ["OQA", "Optimal Question Asking", "planning gap"]
sources: ["dutta-2026"]
---
# Optimal Question Asking (OQA)

> A benchmark where the optimal number of questions is computable exactly,
> so a model's inefficiency has a number, not a guess.

## The benchmark (Dutta, Ramachandran & Sra, 2026)

OQA turns question asking into a controlled [[twenty-questions|Twenty Questions]] game over a
finite attribute table (binary or $k$-ary). A target item is sampled
uniformly; each turn asks about one attribute and the reply removes every
item that disagrees, leaving a shrinking candidate set $C_t$. With noiseless
answers the posterior stays uniform on $C_t$, so uncertainty is exact:
$H_t=\log_2|C_t|$. Alongside the model's transcript, a dynamic-programming
oracle computes the optimal expected number of questions under the same
attribute menu.[^c1]

## Planning gap

The benchmark's headline metric is the **planning gap**: the average number
of extra questions the model asks relative to the DP oracle under the same
target distribution, $\mathbb{E}_{x^\star\sim\mathrm{Unif}(X)}[T_{\text{model}}(x^\star)
- T_{\text{DP}}(x^\star)]$. It isolates *execution* inefficiency from the
question-selection problem itself, because the oracle is optimal by
construction for that exact instance.[^c2]

## Theorem 5.1 — optimality of the DP oracle

For any finite deterministic OQA game (candidate set $C$, uniform target,
finite query menu, unit query cost), define $V(C)=0$ on terminal sets and
$V(C)=1+\min_a\sum_{o\in O_a}\frac{|C_o(a)|}{|C|}V(C_o(a))$ otherwise. $V(C)$
is the minimum expected number of additional queries over all allowed
adaptive decision trees, and any policy attaining that minimum at every
reachable set is optimal; the proof is by induction on $|C|$, using that the
target is uniform so each child branch's probability is $|C_o(a)|/|C|$.[^c3]

## Empirical finding

Benchmarked on seven frontier models (GPT-5, GPT-4.1, Gemini 2.5 Pro, Gemini
2.0 Flash, Claude Sonnet 4.5, Claude Haiku 4.5, Grok 4) across Places, Cars
and Animals tables at $N\in\{25,100\}$ candidates and multiway variants up
to 300: "even in a clean setting where uncertainty can be measured exactly,
models leave efficiency on the table" against the DP oracle.[^c4]

## Known as

| Field | Name there | Relation |
|---|---|---|
| This paper (Dutta, Ramachandran & Sra 2026) | Optimal Question Asking (OQA) | exact |
| Active learning / search theory (Jedynak et al. 2012) | Twenty Questions game | close — OQA is this game fixed to a finite attribute table with a benchmarked, oracle-scored implementation, not the general noisy-channel game |

## Transfer

| | |
|---|---|
| **Home field** | [[generalized-binary-search|Generalized binary search]] / active learning (Jedynak et al. 2012; Nowak 2011): adaptive query trees over a finite hypothesis set, optimal splitting under deterministic answers |
| **Here** | An LLM agent's dialogue turns, each turn an attribute query against a hidden target, scored against a DP-computed optimal count |
| **What survives** | The adaptive-decision-tree framing and the exact [[entropy]] accounting $H_t=\log_2|C_t|$; the DP recursion (Theorem 5.1) is tractable here because it caches over the finite set of candidate sets reachable in one benchmark instance |
| **What does not** | The general instance-optimal-tree problem is NP-hard ([[optimal-decision-tree]]); OQA's DP oracle is exact only because each benchmark table is small enough for the reachable-subset cache to stay bounded, not because the underlying problem became tractable in general |

## Limits

- Noiseless, deterministic answers by table lookup — no [[efe-planning-as-variational-inference|ambiguity]], no
  misunderstanding, no free-text answer parsing; real clarifying dialogue is
  none of these.
- The oracle (Theorem 5.1) is optimal for *this* finite instance; it does
  not generalize to a polynomial algorithm for arbitrary attribute tables,
  since the reachable-subset cache can itself grow combinatorially.
- The planning-gap metric charges every extra question equally; it does not
  price the *cost* of a question the way [[value-of-information]] or the
  cost-weighted rule in [[active-inference-context-acquisition]] does.
- Evaluated on three curated attribute domains (Places, Cars, Animals) at
  $N$ up to 300 — no claim of coverage beyond finite, fully-observed
  attribute tables.

## Related

[[active-inference-context-acquisition]] · [[expected-information-gain]] · [[optimal-decision-tree]] · [[generalized-binary-search]] · [[value-of-information]]

[^c1]: dutta-2026
[^c2]: dutta-2026
[^c3]: dutta-2026 — "Then V (C ) is the minimum expected number of additional queries over all allowed adaptive decision trees. Any policy that attains the minimum in (17) at every reachable set is optimal."
[^c4]: dutta-2026 — "We evaluate frontier LLMs on 25- and 100-tier binary OQA datasets, tracking posterior entropy exactly and comparing each model to a dynamic programming (DP) oracle under the same attribute menu and stopping rule. However, even in a clean setting where uncertainty can be measured exactly, models leave efficiency on the table."
