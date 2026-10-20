---
description: "A clarification agent bounded by a domain knowledge graph, greedily asking the question with the greatest expected entropy reduction over the graph-supported hypotheses."
aliases: ["knowledge-guided agentic framework", "KG-guided ambiguity mitigation"]
sources: ["abbasian-2026"]
---
# Knowledge-graph-guided clarification

> Do not let the LLM invent the candidate hypotheses or the eligible
> questions; let a domain graph fix both, and use the graph only to bound
> what the [[entropy]]-reduction rule is allowed to choose from.

## Definition / Mechanism

The framework sits between the asker and an otherwise unmodified downstream
LLM. An inner LLM proposes search terms from the query; a deterministic
controller resolves them against a task-specific knowledge graph to retrieve
a bounded set of hypotheses $H_0$, each given equal initial weight. The
knowledge graph does not generate the final response: "It defines which
hypotheses are supported, which missing facts can distinguish them and how
each possible answer changes the active hypothesis set."[^c1]

At each turn the controller scores every unasked, graph-eligible binary
variable by its expected reduction in Shannon entropy over the current
hypothesis-weight distribution and asks the arg-max: "The controller
selected the variable with the greatest expected reduction in entropy." The
inner LLM only phrases the chosen variable as a natural-language question;
it cannot change which variable was chosen. After an answer, hypotheses
incompatible with it are removed and the remaining weights renormalized.[^c2]

Clarification stops on one of three conditions: "It stopped when the
remaining hypotheses supported a task output, no unasked question could
distinguish them further or the task's interaction limit was reached."[^c3]

## Why it matters

Against direct prompting and a rephrase-only baseline (Rephrase-and-Respond),
across five downstream LLMs on two masked-evidence health benchmarks, the
framework "increased overall exact Top-1 accuracy by at least 57.1
percentage points and selective exact Recall@5 by at least 77.7 percentage
points" for diagnosis retrieval, and improved dietary-safety accuracy for
every tested model while also lowering predictive entropy under repeated
generation.[^c4]

## Transfer

| | |
|---|---|
| Home field | Information theory / active learning — greedy expected-entropy-reduction question selection, the same rule as [[generalized-binary-search]] and [[expected-information-gain]]. |
| Here | The same arg-max-expected-entropy-reduction rule, but run only over a hypothesis set and question set that a domain knowledge graph has already fixed, with a separate LLM restricted to wording. |
| What survives | The selection formula itself: uniform prior over retrieved hypotheses, greedy arg-max of expected entropy drop, renormalization after each answer. |
| What does not | Any optimality guarantee tied to searching over *all* possible questions — GBS's mass-splitting bound is a property of an unconstrained candidate set; here the graph, not the criterion, decides eligibility, and the paper reports accuracy/entropy outcomes rather than a query-complexity bound. |

## Limits

- Evaluated on two constructed benchmarks with masked, known ground truth
  (Synthea-derived diagnosis cases; a curated dietary-safety knowledge
  graph) and a simulated oracle answering from the withheld field, not live
  patients — reported effect sizes rest on this controlled setting.
- The inner LLM (GPT-5.5) both proposes search terms and phrases questions;
  the deterministic controller's choice of *what* to ask is isolated from
  wording, but the framework's hypothesis retrieval step still depends on
  one LLM's term proposals.
- Entropy ties are broken by a fixed deterministic rule rather than a
  principled tie-break; the paper does not report how often ties occur.

## Related

[[generalized-binary-search]] · [[expected-information-gain]] · [[patient-context-ambiguity]] · [[value-of-information]]

[^c1]: abbasian-2026 — "It defines which hypotheses are supported, which missing facts can distinguish them and how each possible answer changes the active hypothesis set."
[^c2]: abbasian-2026
[^c3]: abbasian-2026
[^c4]: abbasian-2026 — "it increased overall exact Top-1 accuracy by at least 57.1 percentage points and selective exact Recall@5 by at least 77.7 percentage points across the five evaluated models compared with direct prompting"
