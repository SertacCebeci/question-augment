---
description: "A joint trigger-and-routing architecture that reads a proactive agent's wake and grounding decisions off one temporal-graph-learning forward pass instead of an LLM call on every event."
aliases: ["TGL trigger", "graph-native proactive trigger", "joint trigger-and-routing architecture"]
sources: ["liu-2026-proactive"]
---
# TGL proactive trigger

> Treats a proactive agent's always-on activity stream as a heterogeneous
> temporal graph rather than text, and reads the wake-up decision and the
> context-selection decision off two node-classification heads sharing one
> small graph encoder — so the expensive LLM is invoked only after the
> trigger fires, not on every event.

## Definition / Mechanism

Liu, Zhang, Abdi et al. (2026) cast the two
decisions a proactive assistant must make on every event — "when to
intervene at all, and what to ground the intervention on" — as node
classification on a graph built from the raw event stream, instead of as
a language-modelling problem: "We formulate proactive triggering and
context selection as joint node-level prediction over a heterogeneous
temporal event-entity graph rather than as a language-modelling problem,
enabling a lightweight always-on controller before downstream LLM
generation."[^c1]

A trigger head over event nodes and a routing head over entity nodes sit
on a shared temporal-graph-learning (TGL) [[backbone-of-a-formula|backbone]] — three relation-aware
GATv2 layers with a Jumping Knowledge head — and are trained jointly: "A
trigger head over event nodes produces a wake-up probability (addressing
the expensive-triggering problem) and a routing head over entity nodes
produces a per-entity relevance score (addressing the ungrounded-
suggestions problem), both read off one forward pass and trained jointly."
[^c2]

The downstream language agent is called only once the trigger head
clears its deployed threshold, consuming the routed entities as
structured context; the LLM never sees the raw event stream. Across the
ProactiveAgent benchmark and 14 language-agent backbones, the TGL trigger
raised F1 relative to LLM-as-trigger baselines and ran far faster: "TGL
improves F1 on each of 14 backbones (mean +16.7, up to +46.0); in
trigger-architecture comparisons, one TGL checkpoint gives the strongest
trigger AUCs and the most stable deployed threshold. It runs at 11.13 ms
per event on a GPU server and 13.99 ms on a consumer laptop, ∼ 4–7× and
∼ 12–83× faster than every single-forward LLM-as-trigger configuration
tested in each regime, with a ∼220 MiB BF16 resident footprint deployable
on-device."[^c3]

## Known as

| Field | Name there | Relation |
|---|---|---|
| This paper (Liu et al. 2026) | TGL (temporal-graph-learning) trigger | exact |
| This wiki | graph-native proactive trigger | exact — descriptive name for the same joint architecture |
| This wiki | joint trigger-and-routing architecture | exact — names the two-head design specifically |

## Transfer

| | |
|---|---|
| **Home field** | temporal graph learning / graph neural networks: continuous-time dynamic-graph encoders (TGAT, TGN) and relation-aware attention (GATv2) that produce node-level readouts from a heterogeneous, time-evolving graph |
| **Here** | the "should the agent act/ask now" decision and the "on what evidence" decision become two node-classification readouts — trigger over event nodes, routing over entity nodes — off one shared encoded graph built deterministically from the event log |
| **What survives** | the encoder's inductive bias that structure (which entities recur, which events touch which entities) is native to a graph and lossy once flattened to text or a feature row — carried over as the reason the graph-native trigger beats an LLM reading the same events serialised as text |
| **What does not** | any claim that graph node classification generalises to triggers on free-form, non-structured user input; the method needs the event stream already available as (actor, verb, object, timestamp) tuples, which this paper's benchmark supplies but a general dialogue turn does not |

## Limits

This note's claim rests on the assumption that a proactive agent's input
is already available as a structured, timestamped event log — the
paper's own graph construction is "deterministic from the event stream by
a rule-based extractor." Where the assistant's input is genuinely
unstructured text (a chat turn, an open-ended query) rather than an
operating-system event stream, nothing here shows the graph encoder
still beats an LLM trigger. The F1 and latency comparisons are all on the
authors' ProactiveAgent benchmark and the 0.6–8B Qwen3 backbone range
tested; no independent replication is cited.

## Related

[[proact-architecture]] · [[ig-redundancy-coverage-utility]] · [[breakdown-aware-proactive-intervention]] · [[value-of-information]]

[^c1]: liu-2026-proactive — "We formulate proactive triggering and context selection as joint node-level prediction over a heterogeneous temporal event-entity graph rather than as a language-modelling problem, enabling a lightweight always-on controller before downstream LLM generation."
[^c2]: liu-2026-proactive — "A trigger head over event nodes produces a wake-up probability (addressing the expensive-triggering problem) and a routing head over entity nodes produces a per-entity relevance score (addressing the ungrounded-suggestions problem), both read off one forward pass and trained jointly."
[^c3]: liu-2026-proactive
