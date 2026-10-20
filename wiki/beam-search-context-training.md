---
description: "Optimizer maintains K candidate contexts, expands each with information-seeking tools, and prunes to the top K by validation score, keeping the prior best as a \"do nothing\" option."
aliases: ["BeamSearch-IS", "beam-search context training", "search-based context optimization"]
sources: ["huang-2026-context"]
---
# Beam-search context training with active information seeking

> A population-based alternative to greedy, single-trajectory context
> optimization: keep several candidate contexts alive, let each explore an
> update — including calls to web-search and browser tools — and prune by
> held-out validation score before the next round.

## Definition / Mechanism

The optimizer's modifiable state is a discrete, human-readable context
(read/write via a structured, database-like interface rather than one
monolithic prompt). At step $t$ it holds a beam of $K$ candidate contexts
$\mathbb{C}_t$. Each step has two phases: **expansion**, where every
candidate in the beam spawns $M$ children by running the ordinary
context-training loop (executor runs a task, a reward scores it, an
optimizer agent — now equipped with a Wikipedia-search tool and a
browser-use tool — proposes an update), with later children in the same
family explicitly prompted to diverge from earlier ones; and
**selection**, where all children plus the previous step's best candidate
(an "elitism" / do-nothing slot) are scored on a held-out validation set
and the top $K$ survive.[^c1]

On low-resource translation (five languages, Gemini-2.5-Flash), this
procedure (BeamSearch-IS) reached an average ChrF++ of 34.51, against
29.68 for the same tools added to a single greedy trajectory (Seq-IS),
31.94 for a non-iterative best-of-8 baseline, and 31.13 for the tool-free
greedy baseline (Seq); on HealthBench it scored 0.5026 against 0.4484 for
the naive tool-augmented greedy version and 0.4629 for the tool-free
greedy baseline.[^c2]

## Why it matters

The gain is not from adding search tools — a greedy optimizer given the
same tools scores *below* its tool-free version on both benchmarks (see
[[context-pollution-naive-tool-addition]]). The gain comes specifically
from the population-and-prune structure: multiple candidates absorb bad
retrievals independently, and validation-based pruning discards the ones a
web search poisoned before they can propagate, rather than requiring the
optimizer to notice and undo the damage itself.

## Transfer

| | |
|---|---|
| Home field | Sequence decoding / combinatorial search — beam search as a bounded-width alternative to greedy or exhaustive search |
| Here | The beam is not tokens of one sequence but whole candidate *contexts* of a context-optimization training loop; the score is held-out task performance, not a language-model log-probability |
| What survives | Bounded population width $K$; expand-then-prune per step; keeping the best-so-far as a "do nothing" branch (elitism) |
| What does not | No optimality guarantee (decoding-time beam search has none either, but here there is not even a monotone objective — validation score can be noisy); the width buys robustness to noisy tool calls, not search completeness, and costs $K\times M$ optimizer/executor calls per step instead of one |

[^c3]

## Limits

The comparison holds one [[backbone-of-a-formula|backbone]] (Gemini-2.5-Flash as executor/optimizer)
and a fixed, small training budget (128 train / 64 validation examples);
whether the gain size holds at larger training budgets, or with a weaker
optimizer model that cannot itself judge validation quality well, is not
shown in what this note covers.

## Related

[[context-pollution-naive-tool-addition]]

[^c1]: huang-2026-context — "we maintain a small population of 𝐾 candidate contexts, denoted by ℂ𝑡 , and prune them using validation feedback"
[^c2]: huang-2026-context
[^c3]: huang-2026-context
