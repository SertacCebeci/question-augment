---
description: "A three-step procedure that filters candidate implicit needs down to those evidence already supports, isolating what legitimately needs a clarifying question."
aliases: ["restore-identify-filter framework", "RIF framework", "behavior-chain-based ground truth construction"]
sources: ["bai-2026-mapsatisfybench"]
---
# Restore-identify-filter

> A benchmark-construction procedure that turns pre-query context,
> spatio-temporal setting, and post-query behavior into a test of which
> implicit needs an agent could have recovered without asking.

## Definition / Mechanism

Given an interaction x = (q, g, h⁻, r, h⁺) — surface query, spatio-temporal
context, pre-query history, response, post-query behavior — restore
combines h⁻, g and h⁺ to reconstruct the user's complete need; identify
diffs that reconstruction against the surface query q to expose implicit
decision factors not stated in q; filter then keeps only the implicit
needs whose evidence can be found in g and h⁻ — the information available
*before* the agent must respond — and discards factors that cannot be
supported before the agent responds. Retained factors are each labeled a
hard constraint or a soft preference and given an evidence-supported
weight combining historical preference strength with current-session
relevance. Bai et al. (2026)[^c1]

## Why it matters

On stall 2, RIF turns "should the agent ask or infer this?" into a
testable filter rather than a judgment call: a candidate implicit factor
belongs in the recover-don't-ask class only if evidence already available
at decision time (g, h⁻) supports it; everything else is the class that
legitimately needs a question. Applied to build MapSatisfyBench, the same
paper found the gap runs the other way in practice — evaluated agents
default toward asking rather than retrieving the evidence RIF shows was
recoverable: "TS ranges from 0.2859 to 0.4942, and even the best model on
this metric, Claude-4.6-opus, remains below 0.50," and "our tool-call
inspection reveals that all models invoke the profile-related tool at a
relatively low rate."[^c2]

## Transfer

| | |
|---|---|
| home field | benchmark/ground-truth construction for map-service agent evaluation |
| here | a filter test for whether stall 2's ask-vs-infer decision is warranted, applied offline to build evaluation labels |
| survives | the restore → identify → filter sequence as a general recipe: reconstruct the full need from surrounding evidence, diff it against the surface query, keep only what already-available evidence supports |
| does not | RIF is run by an annotator with privileged access to h⁺ (post-query behavior); it is not an online decision rule the asking agent can run, since the agent never observes h⁺ before it must act |

## Limits

RIF's filter step is sound for labeling recoverability after the fact, but
it cannot be read as an algorithm the agent itself executes: the business
agent under evaluation "receives the root query q together with the
information available at decision time, and must decide whether to answer
directly, ask clarification questions, or call tools" — h⁺ is withheld
from it by construction. The recoverable/non-recoverable line is drawn by
one benchmark's own LLM-judge-plus-human-review pipeline over map
services only; it has not been checked against an independent
recoverability judgement or another domain.[^c3]

## Related

[[clarification-benchmarks]] · [[value-of-information]] · [[preference-signal-against-asking]]

[^c1]: bai-2026-mapsatisfybench — "we keep only the implicit needs whose evidence can be found in g and h− , which are the information sources available at decision time, and filter out factors that cannot be supported before the agent responds."
[^c2]: bai-2026-mapsatisfybench — "TS ranges from 0.2859 to 0.4942, and even the best model on this metric, Claude-4.6-opus, remains below 0.50."
[^c3]: bai-2026-mapsatisfybench — "The business agent receives the root query q together with the information available at decision time, and must decide whether to answer directly, ask clarification questions, or call tools."
