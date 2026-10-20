---
description: "Not a single model but a system of components. Named by zaharia-2024 [zaharia-2024]."
aliases: ["compound AI", "systems over models"]
sources: ["zaharia-2024", "arxiv-2511-18298"]
---
# Compound AI systems

> Not a single model but a system of components. Named by Zaharia et al. in > the BAIR post, February 2024 [zaharia-2024].

## Thesis

Zaharia et al. (BAIR blog, 18 February 2024) define a compound AI system as[^s1]
"a system that tackles AI tasks using multiple interacting components,
including multiple calls to models, retrievers, or external tools", and argue
that "state-of-the-art AI results are increasingly obtained by compound
systems with multiple components, not just monolithic models"
[zaharia-2024]. The components they name are model calls, retrievers, tools,
verifiers and control logic; their support is worked examples (AlphaCode 2,
Medprompt) and design patterns — routing, verification, end-to-end
optimisation of the pieces — not a new measurement.

## Known as

| Field | Name there | Relation |
|---|---|---|
| AI systems engineering (BAIR) | compound AI system | exact — the name given in [zaharia-2024] |
| Industry usage | compound AI | exact — the same object, shortened |
| Commentary on the field | systems over models | close — a slogan for the shift the post argues for; it names the argument, not the object |

## Why it matters

**This wiki's inference (conjecture).** If capability lives in the
orchestration rather than in any one model, then question-asking ability is
better placed as a *system component* than embedded in the model — which
implies an architectural split:

```text
QUESTION POLICY   decides what to ask     →  thinking
ELICITATION       delivers the question   →  transport
```

Nothing in [zaharia-2024] compares an embedded arrangement with a
componentised one. [[elicitation-protocols]] records the same split and calls
it what it is: a design principle, not a result.

## Asking as a compound system

Decomposed into components:

| Component | Job |
|---|---|
| Generator | produce candidate questions ([[question-burst]] mode) |
| Classifier | determine question type ([[uncertainty-decomposition]]) |
| Router | decide who is asked ([[question-budgets]]) |
| Scorer | prioritise ([[expected-information-gain]], [[value-of-information]]) |
| Answerer | answer and record as a constraint ([[constraint-as-information]]) |
| Monitor | watch for contradiction ([[cusum]]) |
| Distiller | extract a sufficient statistic ([[sufficient-statistic]]) |
| Controller | decide when to stop ([[stopping-rules]]) |

Each box names the note the wiki currently has for that job — not a
demonstrated component, and not in every case a theory of that job. The
Router and Classifier boxes are the thinnest: [[question-budgets]] prices
asking and separates budgets by the *source* of the answer, but says of
itself that it "does not select which question goes in which budget";
[[uncertainty-decomposition]] types the agent's *uncertainty*, not the
question, and its own note treats the mapping from type to action as
motivated rather than forced.

## Transfer

| | |
|---|---|
| In its home field | components are model calls, retrievers, tools and verifiers composed over an AI task that has a measurable end-task metric — benchmark accuracy, cost, latency [zaharia-2024] |
| Here | components of a questioning loop whose output is a constraint set over $W$; no end-task metric is defined for the loop |
| What survives | the architectural claim that capability lives in the orchestration; that components can be swapped and evaluated separately; the policy/transport split |
| What does not | the post's evidence — it is about application benchmarks, not about asking; any claim that this particular eight-box decomposition is the right or the complete one; any guarantee about the *composition* of components |

## Limits

- `[?]` `zaharia-2024` is recorded in `wiki/meta/sources.json` as verified
  prior to the current verification regime, and no URL is stored with it. The
  post is at `bair.berkeley.edu/blog/2024/02/18/compound-ai-systems/`; on
  2026-09-10 that host refused connection from here and the text was read
  through the AIhub mirror (15 March 2024).
- The BAIR post is a position piece — worked examples and design patterns, no
  new measurement — so "the best-performing applications are compound" is an
  argued trend, not a measured result.
- The component table is this wiki's decomposition (conjecture), not from the
  source; two of its boxes are placeholders, as stated above.
- The policy/elicitation split is a design principle argued here, not a
  measured result: no source in this wiki compares the embedded and the
  componentised arrangement.
- Components each having a theory does not give the *composition* one; the
  interaction between, say, scorer and monitor is unstudied.
- A measured counterpoint from a different system, not a test of the thesis. BioSage's retrieval agents, with query planning, did not reliably beat plain retrieval: "vanilla RAG outperformed agent-based approaches"[^s2] on its cross-disciplinary benchmark for GPT-4o and Phi-14B. On GPQA the GPT-4o agent scored below the vanilla model, and the authors read this as base-model knowledge being "more valuable than our retrieval mechanisms for this benchmark."[^s4] The first agent version "showed mixed results, with significant improvements for Llama-3-70B"[^s3]. These are one team's numbers on its own benchmarks, and the text read reports no repeated runs or intervals (my reading). They bear on whether adding orchestration helps answers, not on the asking decomposition above. A translation-style component, described in [[cross-field-answer-gap]] but not scored, is the nearest the paper comes to a question-side step.

## Related

[[question-budgets]] · [[elicitation-protocols]] · [[stopping-rules]] · [[uncertainty-decomposition]] · [[multi-agent-clarification]]

[^s1]: zaharia-2024
[^s2]: arxiv-2511-18298 — "vanilla RAG outperformed agent-based approaches"
[^s3]: arxiv-2511-18298 — "showed mixed results, with significant improvements for Llama-3-70B"
[^s4]: arxiv-2511-18298 — "more valuable than our retrieval mechanisms for this benchmark"
