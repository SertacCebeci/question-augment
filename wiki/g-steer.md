---
description: "A trained policy that chooses Retrieve, Ask or Stop per user-specific factor from an explicit evidence state, optimized by a reward that trades target coverage against interaction cost."
aliases: ["G-STEER", "target-anchored policy optimization"]
sources: ["yoon-2026"]
---
# G-STEER

> One policy, three actions per factor — pull from memory, ask the user, or
> stop — trained to buy coverage of the factors that matter at the lowest
> interaction cost.

## Definition / Mechanism

Yoon & Lee (2026) formulate personalized query refinement as
a sequential decision problem in which a policy conditions on the query,
the user profile, and an accumulated evidence state Σt that records, per
candidate framing factor, its grounding status, supported value, and
evidence source: "The agent selects at ∈ {Retrieve, Ask, Stop}." Retrieve
pulls from persistent user memory, Ask elicits from the user directly, and
Stop ends refinement and emits the refined query from Σt.[^c1]

After supervised warm-up on graph-scaffolded trajectories, the policy is
optimized with trajectory-level GRPO against a reward that combines a
coverage-and-alignment term with two cost terms — one for the number of
Retrieve/Ask actions taken, one for redundant or multi-target questions.
The acquisition cost is asymmetric by design: "We set λask > λret because
asking the user imposes greater burden than retrieving from memory."[^c2]

At inference the offline elicitation targets and the dependency graph
used to build training trajectories ([[intent-elicitation-graph]]) are not
available; the policy induces its own evidence-state slots by prompting
and updates them from whatever Retrieve or Ask returns, choosing among the
three actions at each step until it selects Stop.[^c4]

Evaluated on PDR-Bench, the trained policy reached the strongest target
coverage and personalization score of every tested method while cutting
interaction: "G-STEER achieves the strongest overall weighted target
coverage and the highest downstream report personalization across both
evaluated DRAs, while asking roughly one third as many user questions as a
strong clarification baseline." Against the strongest ask-only baseline
specifically: "stronger performance than CEP-Clarify+Rewrite while asking
4.09 user questions on average, compared with 12.04 for
CEP-Clarify+Rewrite."[^c3]

## Why it matters

This folds three of the wiki's separately-treated decisions — which
factor to address next (stall 2), whether to retrieve or ask (stall 4),
and when to stop (stall 7) — into one policy conditioned on a single
evidence-state representation, rather than a ranking step, a source-choice
rule, and a stopping rule computed independently. The reported question
count (4.09 vs 12.04 for comparable or better coverage) is evidence that
routing some factor-grounding through memory retrieval, and reserving Ask
for what memory cannot supply, cuts interaction cost sharply.

## Limits

- **The comparison is to the paper's own baselines on one benchmark**
  (PDR-Bench, a research-report personalization dataset); no claim here
  extends the 4.09-vs-12.04 result past that dataset and the two deep
  research agents tested.
- **The reward's coverage term depends on an embedding-similarity match**
  between covered evidence slots and reference elicitation targets, scored
  by the same class of model (GPT-5.4 / sentence-transformers) used to
  build the targets — the evaluation is not independent of the target
  construction pipeline.
- **The action set is fixed to three** (Retrieve, Ask, Stop); the policy
  does not choose among multiple sources the way stall 4 more generally
  allows (multiple experts, tools, or document types), only between one
  memory store and one user.
- The asymmetric cost weights λask > λret are a design choice justified by
  a stated intuition about user burden, not measured against an actual
  cost-of-asking figure.

## Related

[[intent-elicitation-graph]] · [[value-of-information]] · [[expected-information-gain]] · [[bounded-rationality]]

[^c1]: yoon-2026 — "The agent selects at ∈ {Retrieve, Ask, Stop}."
[^c2]: yoon-2026 — "We set λask > λret because asking the user imposes greater burden than retrieving from memory."
[^c4]: yoon-2026 — "The IEG is used only for trajectory construction and is unavailable at inference."
[^c3]: yoon-2026 — "G-STEER achieves the strongest overall weighted target coverage and the highest downstream report personalization across both evaluated DRAs, while asking roughly one third as many user questions as a strong clarification baseline."
