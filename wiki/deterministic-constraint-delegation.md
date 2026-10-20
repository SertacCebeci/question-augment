---
description: "An agent architecture that keeps constraint elicitation on an LLM but delegates constraint enforcement to a deterministic, non-LLM component, closing most of the compliance gap to text-only baselines."
aliases: ["MACS", "Multi-Agent Commerce System", "deterministic constraint delegation"]
sources: ["huang-2026-macs"]
---
# Deterministic constraint delegation

> A third split of authority in a compound agent: not who may interrupt with a
> question, but who is trusted to say a constraint the user gave was actually
> satisfied.

## Definition / Mechanism

Huang et al. (2026) built MACS, a two-agent conversational
recommender over a fixed merchant catalog: "MACS uses LLMs for language-facing
tasks such as interpreting user requests, eliciting preferences, and
generating responses, while correctness-critical operations, including
product retrieval, hard-constraint filtering, brand exclusion, and
progressive relaxation, are executed deterministically by the merchant
agent."[^c1]

The shopping agent never touches the catalog directly: "The shopping agent
never retrieves products directly; all calls go through the merchant agent's
structured API, so the LLM cannot hallucinate catalog contents." Hard
constraints (brand exclusions, price ceilings, specification minimums)
compile to SQL `WHERE` clauses and are checked against ground truth computed
the same way, independent of any LLM.[^c2]

## Findings

On a 140-query single-turn benchmark MACS reached an 87.1% pass rate with
perfect brand compliance (1.000) against 72.1% (GPT-4o-mini + injected
catalog) and 68.6% (Gemini 2.5 Flash Lite + injected catalog): "The gap
reflects MACS's SQL-enforced constraint pipeline, which text-only systems
cannot replicate structurally."[^c3]

An ablation that strips the SQL `WHERE`-clause enforcement while keeping
catalog injection (MACS-NoSQL) confirms the mechanism is load-bearing, not
just correlated with the architecture: "MACS-Full achieved avg=0.681 /
pass=85.3%; MACS-NoSQL dropped to avg=0.628 / pass=81.3% (−0.053 avg, −4.0
pp). The sharpest effect appeared on the 19 brand-constrained queries:
brand_score fell from 1.000 to 0.684 (−0.316), confirming that SQL
predicates, not prompt instructions, enforce brand compliance."[^c4]

## Why it matters

[[multi-agent-clarification]] and [[uncertainty-aware-multi-agent-scaffold]]
both split a compound agent by who may ask. MACS splits it by who may
certify an answer as satisfying a constraint: the same LLM that elicits and
phrases preferences is never the component whose word is taken that a
constraint holds. That is a different axis of the same stall — not which
agent gets the turn, but which agent's output counts as ground truth once a
constraint has been accepted.

## Transfer

| | |
|---|---|
| In database systems | a predicate over a schema is evaluated by the query engine, not by the client requesting it |
| Here | an elicited constraint (budget, exclusion, spec minimum) is compiled to a `WHERE` clause and checked by a component the LLM cannot bypass |
| What survives | the guarantee: once a constraint is accepted into state, its satisfaction is checked the same way every time, independent of generation quality |
| What does not | the predicate itself is trusted only as far as the extraction step that produced it — MACS does not verify that the LLM extracted the right slot value, only that the accepted value is then enforced without drift |

## Limits

- Single consumer-electronics catalog (laptops); the paper states results
  "should not be interpreted as evidence of generalization to other merchant
  catalogs or recommendation domains."
- The baselines receive MACS's own retrieved candidate pool rather than
  performing independent retrieval, so the comparison isolates
  constraint-aware generation over a shared pool, not end-to-end retrieval.
- No human evaluation; response quality is scored by an LLM judge
  (GPT-4o-mini) at temperature 0.
- The extraction step that turns free text into a slot value is still an LLM
  job — deterministic enforcement bounds what happens after extraction, not
  extraction error itself.

## Related

[[multi-agent-clarification]] · [[uncertainty-aware-multi-agent-scaffold]] · [[compound-ai-systems]] · [[session-persistent-preference-state]]

[^c1]: huang-2026-macs — "MACS uses LLMs for language-facing tasks such as interpreting user requests, eliciting preferences, and generating responses, while correctness-critical operations, including product retrieval, hard-constraint filtering, brand exclusion, and progressive relaxation, are executed deterministically by the merchant agent."
[^c2]: huang-2026-macs
[^c3]: huang-2026-macs
[^c4]: huang-2026-macs — "MACS-Full achieved avg=0.681 / pass=85.3%; MACS-NoSQL dropped to avg=0.628 / pass=81.3% (−0.053 avg, −4.0 pp). The sharpest effect appeared on the 19 brand-constrained queries: brand_score fell from 1.000 to 0.684 (−0.316), confirming that SQL predicates, not prompt instructions, enforce brand compliance."
