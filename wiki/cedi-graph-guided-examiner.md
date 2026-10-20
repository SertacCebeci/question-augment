---
description: "An MLLM examiner selects among four named question strategies while traversing a scene-graph state space, eliciting measurably more hallucinations than static evaluation."
aliases: ["CEDI", "Contextualized Evaluations of MLLMs through Dynamic multi-round Interactions"]
sources: ["li-2026-contextualized"]
---
# CEDI graph-guided examiner

> An evaluator agent that decides, turn by turn, *which* question to ask a
> vision-language model by walking a scene-graph [[possible-worlds|state space]] and choosing
> among four named strategies — and is shown to surface more failures than
> any single fixed protocol.

## Definition / Mechanism

CEDI recasts benchmark evaluation as a three-party interaction: an examiner
MLLM (backed by GPT-4o), the evaluatee VLM, and a grader. Given a
ground-truth scene graph $G=(V,E,A)$ for an image, the examiner first builds
a goal-driven scenario and a context sub-graph $G_s=(V_s,E_s,A_s)$, then
conducts a multi-turn interview modelled as traversal over $G_s$: at each
turn $t$ it selects a target node $v_t \in V_s$ (or keeps $v_{t-1}$ for a
follow-up) and generates a question anchored to that node's attributes and
incident relations, so every question stays verifiable against $G$. At each
turn the examiner actively selects one of four question types, conditioned
on dialogue history and previously used types: **regular** (queries an
observed element of $G_s$ to establish a factual baseline), **follow-up**
(keeps the same node, testing consistency with an earlier claim),
**adversarial** (asks about a plausible but absent object/attribute/relation
$\notin G_s$ that commonly co-occurs with the visual content, to expose
reliance on language priors over evidence), and **unanswerable** (injects a
fabricated element $p \notin G$ and composes a follow-on question $q(p)$
whose answer is undefined under $G$, formally $G \not\models p \Rightarrow G
\not\models q(p)$ — a well-grounded model must detect and refuse or correct
the unsupported premise).[^c1]

Applied to visual hallucination detection, CEDI's interactive examiner is
compared against a caption-based examiner, a prompt-only baseline, and a
single-turn binary-question examiner (POPE-style). On the accuracy metric
reported in the paper's Table 1 (lower means the examiner elicited more
wrong answers), CEDI drives evaluatee accuracy below the static POPE
examiner's for every tested model: InternVL3-8B 61.65% (POPE) → 58.49%
(CEDI); Qwen2.5-7B 66.90% → 58.36%; GPT-4o 67.89% → 67.38%. Across graders
and datasets the paper reports CEDI eliciting more hallucinations than
caption- and prompt-only baselines as well (coverage +3–19pp, VALOR
per-turn hallucination rate +5–23pp, scene-graph edit distance 1.2–2.9×
higher).[^c2]

## Known as

| Field | Name there | Relation |
|---|---|---|
| agent-evaluation | CEDI | exact — the paper's acronym |
| agent-evaluation | Contextualized Evaluations of MLLMs through Dynamic multi-round Interactions | exact — the acronym's expansion, same object |

## Why it matters

For stall 2 (which axis first), CEDI is a concrete instance of an axis-selection
policy that is not a single scalar score: it is a *typed repertoire* — the
next question is chosen both by *where* the traversal is (which node/axis)
and by *which strategy* to apply there (confirm, stress-test, or actively
try to break the model), with the choice conditioned on the running
dialogue rather than recomputed from scratch each turn. That interactive,
strategy-varying selection elicits substantially more failures than any one
fixed static protocol (^c2) is this wiki's reading of the result as an
argument that, for evaluation-as-questioning, the identity of the
*strategy* — not just the axis — is part of what "which question next" must
select.

## Limits

- The 61.65→58.49 / 66.90→58.36 / 67.89→67.38 comparison (Table 1) rests on
  an automatic re-parse of CEDI's free-form transcript into yes/no
  questions by a third LLM (Qwen3-30B-A3B-Instruct-2507), so part of the gap
  could reflect the parser rather than the examiner's question strategy.
- Ground truth is a human- or dataset-annotated scene graph; the mechanism
  needs that annotation to construct adversarial and unanswerable
  questions and to grade the transcript, so it does not transfer to domains
  without a structured ground truth.
- The examiner's own strategy-selection policy (which of the four types to
  use next) is itself an MLLM prompted to choose, not a scored or optimized
  rule — no claim is made that this choice is itself near-optimal by any
  criterion.
- Demonstrated only on visual hallucination in VLMs with GPT-4o as the
  examiner [[backbone-of-a-formula|backbone]]; generalization to other MLLM backbones or other agent
  domains is not evaluated here.

## Related

[[clarification-request]] · [[semantic-entropy]] · [[neyman-pearson-lemma]] · [[information-gathering-interview-style]]

[^c1]: li-2026-contextualized — "From this scaffold, the examiner actively selects one of four question types to elicit different hallucination behaviors"
[^c2]: li-2026-contextualized — "Table 1 shows that CEDI elicits more hallucinations than yes/no probing."
