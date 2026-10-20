---
description: "Giving a greedy context-optimizing agent web-search and browser tools, with no mechanism to prune or backtrack, measurably lowers task performance below the tool-free baseline."
aliases: ["Context Pollution", "naive tool-addition degradation"]
sources: ["huang-2026-context"]
---
# Context pollution from naive tool addition

> Handing a sequential, greedy context optimizer the ability to search and
> browse the web does not by itself help it — measured across two task
> families, it makes the agent worse than not searching at all.

## Definition / Mechanism

Take a standard sequential context-training pipeline: one context
trajectory is kept, updated at each step from training feedback, with no
population or backtracking. Adding a Wikipedia-search tool and a
browser-use tool to the optimizer agent in this pipeline (Seq-IS) degrades
downstream performance relative to the same pipeline without those tools
(Seq): average ChrF++ on five low-resource-translation language pairs
drops from 31.13 to 29.68, and the HealthBench rubric score drops from
0.4629 to 0.4484. Step-level tracing on the translation task shows the
mechanism: a small context update (~200 tokens) introduces a
performance-degrading artifact, and the optimizer cannot remove it — over
many subsequent steps it repeatedly re-adds and re-removes content around
the same low score, rather than recovering.[^c1]

A second, related failure the same pipeline shows is getting stuck: the
optimizer periodically tries to prune an over-large context region (e.g.
excess dictionary support) but always re-adds what it just pruned instead
of discovering a better allocation, so context length grows and collapses
in a repeating sawtooth rather than converging.[^c2]

## Why it matters

This is the negative result that motivates
[[beam-search-context-training]]: it shows that "add information-seeking
tools" is not itself the lever that improves an asking/seeking agent —
without some way to discard what a search introduced and try alternatives
in parallel, active information seeking can net out to a *worse* agent
than a closed, no-search one. Any design that lets an agent decide to
seek external information needs a corresponding way to un-do a bad
retrieval, or the option to seek is a risk, not a gain.

## Limits

The diagnosis that the missing ingredient is specifically "an explicit
backtracking mechanism" is the paper's interpretation of the traced
example (Fig. 2–3), not an isolated ablation that adds only backtracking
and holds everything else fixed; the quantitative drop (31.13→29.68,
0.4629→0.4484) is established, but the causal account of *why* is the
authors' reading of the trace, and the finding is shown on one [[backbone-of-a-formula|backbone]]
model (Gemini-2.5-Flash) and two of the paper's four task families.

## Related

[[beam-search-context-training]]
- [[hierarchical-context-isolation]] — contradicts

[^c1]: huang-2026-context — "the average score drops from 31.13 (Seq) to 29.68 (Seq-IS)"
[^c2]: huang-2026-context — "these pruned resources are invariably re-added in subsequent steps. This implies that the optimizer is stuck in a loop"
