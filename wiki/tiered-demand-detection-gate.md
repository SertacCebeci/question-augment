---
description: "A single forward pass predicts one of three escalating intervention tiers per turn — silent, fast, memory-grounded — with abstention still possible after the costliest tier fires."
aliases: ["IntentFlow demand detection", "DD-MM-PAS decision token", "tiered intervention gate"]
sources: ["arxiv-2604-08000"]
---
# Tiered demand-detection gate

> Instead of one silent-or-speak bit, or a value computed over a fixed
> action set, one forward pass names a cost tier — and the priciest tier
> can still say nothing once it has looked.

## Definition / Mechanism

PASK's Demand Detector, at each dialogue step $t$, predicts a single
decision token
$d_t \in \{\texttt{<silent>}, \texttt{<fast\_intervention>}, \texttt{<full\_assistance>}\}$,
"corresponding to no intervention, direct low-latency assistance from the
current context, and memory-grounded reasoning, respectively."[^c1]

The three tokens are not a flat classification but an escalating cost
ladder gating what the system is allowed to spend before it may act:
`<silent>` returns nothing and waits; `<fast_intervention>` answers
immediately from the context already in the prompt, in under a second,
with no memory lookup; `<full_assistance>` alone is permitted to invoke
the retrieval pipeline — an observation summary and salient entities are
extracted, sent to the hierarchical memory module, distilled by a second
model, and only then does the system decide again. Critically, paying
the retrieval cost does not commit the system to answering: "$I\tilde{}_t$
denotes the refined memory evidence produced by MemLoader, and $f_{final}$
may either return a response or $\emptyset$ if the retrieved evidence does
not justify intervention." The gate is therefore two decisions chained,
not one: *whether to look*, then, having looked, *whether to speak*.

The decision token is produced directly by the primary model in the same
pass that would otherwise require a separate reasoning step — a design
choice stated explicitly against an alternative the authors reject: "we
first internalize this reasoning process through large-scale, high-quality
supervision, so that intent understanding becomes an efficient forward
prediction rather than a costly explicit deliberation step." A
curriculum-trained supervised stage establishes the three-way decision and
memory distillation; a subsequent DAPO reinforcement-learning stage adds
a rule-based reward for token validity and intervention timing plus an
LLM-judged reward for the alignment, reasonableness and necessity of the
content produced.

On the authors' own Proactive Demand Detection Benchmark, the tiering
exposes an asymmetry rather than a uniform difficulty: "Many models are
good at either helping or staying silent, but not both. This is reflected
in the large gaps between Demand and No-Dem. performance: for example,
Qwen3.5-Flash scores 29.1 vs. 93.1[.]" A model tuned toward one branch
of the gate (recognizing when help is needed) trades off against the other
(recognizing when it is not), rather than both improving together with
scale or prompting alone.

## Known as

| Field | Name there | Relation |
|---|---|---|
| This paper (proactive AI) | IntentFlow's decision token $d_t$ | exact |
| Proactive-service POMDP survey ([[intervention-advantage]]) | four-mode gate $\{$silent, ask, assist, act$\}$ scored by a value difference | close — both gate speech behind an explicit non-silent case, but the POMDP gate scores one value comparison over a fixed action set, while this gate is a forward-predicted token that additionally *tiers cost* (fast vs. memory-grounded) and allows a second, post-retrieval abstention that the four-mode gate does not separately model |
| Graph-native proactive trigger ([[tgl-proactive-trigger]]) | trigger head + routing head over an event graph | close — both replace an LLM-reasoning step with a fast forward pass to decide whether to act, but TGL's routing head only scores *what* to ground on once triggered, with no distinct low-cost "fast" tier and no late abstention after retrieval |

## Why it matters

Most "when to speak" gates in this wiki are binary (silence vs.
intervene) or score a fixed action menu by value. This mechanism makes
the *cost of finding out* part of the decision itself: a system can commit
to a cheap answer, commit to an expensive lookup, or decline at either
point — and the benchmark result shows these are not one skill but two
that a model can hold unevenly.

## Limits

- The reported benchmark numbers, the DAPO training recipe, and the
  LatentNeeds dataset (100k synthetic + 2.1K real sessions) are this
  paper's own construction; `arxiv-2604-08000` is a single 2026 preprint
  with no independent replication.
- "Necessity" and "reasonableness" in the RL reward are scored by an
  LLM judge, not verified against ground truth, so the claim that
  full-assistance interventions are non-redundant is judge-graded,
  unverified here.
- The asymmetry finding (^c4) is reported per-model on one benchmark's
  domain mix (work / learning / daily); whether it generalizes to other
  proactive-assistance settings is not established by this source.

## Related

[[intervention-advantage]] · [[tgl-proactive-trigger]] · [[breakdown-aware-proactive-intervention]] · [[value-of-information]] · [[abstention]]

[^c1]: arxiv-2604-08000 — "corresponding to no intervention, direct low-latency assistance from the current context, and memory-grounded"
