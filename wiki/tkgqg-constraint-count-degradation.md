---
description: "Across LLM-based and adapted static question generators, faithfulness scores drop as more temporal constraints or graph hops are added, at a magnitude comparable between the two axes."
aliases: ["temporal-constraint-count difficulty", "ChronoQG main results"]
sources: ["liu-2026-chronoqg"]
---
# TKGQG constraint-count degradation

> Adding a temporal filter to a generated question hurts a generator's
> faithfulness about as much as adding another graph hop does — measured,
> not assumed.

## Definition / Mechanism

On the [[chronoqg]] benchmark, generation quality (BLEU-4) falls as the
number of accepted temporal filters in a question's trace grows, holding
hop count fixed:

"On ChronoQG-Cron, one-hop questions drop from 0.547 BLEU-4 with one
temporal constraint to 0.443 with two temporal constraints, and further to
0.238 with three or more temporal constraints."[^c1]

The same generators degrade by a comparable amount when hop count grows
instead, holding constraint count fixed:

"On ChronoQG-Cron, under one time constraint, performance drops from 0.547
for one-hop questions to 0.356 for two-hop questions and 0.307 for
three-hop questions."[^c2]

Across the benchmark's single- versus multi-constraint splits the same
pattern holds for every method tested: "Multi-constraint splits are
consistently harder than single-constraint splits. Across most backbones
and methods, performance drops from the '-S' splits to the corresponding
'-M' splits. For instance, GPT-4o-mini with zero-shot prompting drops from
0.458 to 0.288 BLEU-4 on Cron and from 0.410 to 0.328 BLEU-4 on Event."[^c3]

## Why it matters

The number of temporal constraints a question must carry — how many axes
of the [[temporal-constraint-taxonomy]] it touches at once — is not a
free-form difficulty variable added for the benchmark's sake: it degrades
generation faithfulness on its own, independent of and comparably to graph
depth. A selection or generation policy that adds constraints without
budgeting for this cost is spending accuracy it has not accounted for.

## Limits

The result is measured only on LLM-based generators (prompting baselines
and adapted static-KGQG methods) under BLEU-4/ROUGE, on two source
knowledge graphs (CronKG, EventKG); it says nothing about whether the same
degradation holds for a generator trained end-to-end for TKGQG from the
start, or for constraint counts beyond three (the paper merges "three or
more" into one bucket). BLEU/ROUGE are surface-overlap metrics, not a
direct measure of whether the temporal constraint itself survived the
rewrite.

## Related

[[chronoqg]] · [[temporal-constraint-taxonomy]] · [[constraint-as-information]]

- [[temporal-hop-count]] — "hop" here means a graph hop; in temporal QA a hop can instead be a temporal expression the question must resolve, a third count this note does not measure

[^c1]: liu-2026-chronoqg — "On ChronoQG-Cron, one-hop questions drop from 0.547 BLEU-4 with one temporal constraint to 0.443 with two temporal constraints, and further to 0.238 with three or more temporal constraints."
[^c2]: liu-2026-chronoqg — "On ChronoQG-Cron, under one time constraint, performance drops from 0.547 for one-hop questions to 0.356 for two-hop questions and 0.307 for three-hop questions."
[^c3]: liu-2026-chronoqg
