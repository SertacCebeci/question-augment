---
description: "Frontier LLMs answer when clarification, abstention, or escalation would be safer 30–91% of the time, measured across five models on medical benchmarks."
aliases: ["LLM premature closure", "false action rate", "premature closure rate", "inappropriate commitment under uncertainty"]
sources: ["handler-2026", "arxiv-2512-10739", "doi-10-48550-arxiv-2508-15746"]
---
# Premature closure

> The answerer's failure mode measured directly: committing to an answer
> when the safer move was to clarify, abstain, escalate, or refuse — and it
> is common, model-dependent, and only partly fixable by asking nicer.

## Definition / Mechanism

Handler, Bedi & Shah (2026) define LLM premature closure as
inappropriate commitment under uncertainty: providing an answer,
recommendation, or clinical guidance when the safer response would be
clarification, abstention, escalation, or refusal.[^c1]

Because the behavior looks different in different task formats, they measure
it two ways: in structured multiple-choice settings (MedQA, AfriMed-QA with
the correct option removed) it is **false action** — selecting an answer when
no valid option exists; in open-ended settings (HealthBench, HealthBench
Professional adversarial queries) it is giving confident or specific guidance
when clarification, uncertainty-flagging, escalation, or refusal was
warranted.[^c2]

Across five frontier models (GPT-5.4, Claude Opus 4.7, Grok 3, Gemini 2.5
Pro, DeepSeek R1), baseline rates were high and consistent across formats:
models falsely selected an answer on an average of 71% of unanswerable
multiple-choice items, gave inappropriate direct answers on 30% of standard
HealthBench questions, and endorsed unsafe actions on 78% of
physician-authored adversarial queries.[^c3]

A stratified result narrows what "uncertainty" means operationally: models
showed the highest premature-closure rates in scenarios that were
underspecified but carried no obvious danger cue (baseline 73–96%, average
81%) and substantially lower rates when the scenario was underspecified but
urgent (baseline 5–36%, average 19%) — the paper reads this as models being
selectively sensitive to perceived urgency while remaining insensitive to
missing context when nothing flags risk.[^c4]

## Known as

| Field | Name there | Relation |
|---|---|---|
| Clinical diagnostic reasoning | premature closure (cognitive error) | close — same shape of failure, not measured the same way |
| This paper, structured QA | false action rate | exact |
| This paper, open-ended QA | premature closure rate | exact |

The paper's own attribution: "In medicine, premature closure describes the
cognitive error of committing to a diagnosis or plan before sufficient
information has been gathered."[^c5]

Not this concept: [[abstention]] is the general $(f,g)$ selective-answering
framework and its risk–coverage apparatus; premature closure is one
benchmark-specific measurement of how often that choice is made wrong, with
no coverage curve or named cost of rejection.

## Why it matters

This gives stall 10 a number instead of a framework: on a fixed task family,
an un-prompted frontier LLM commits when it should not roughly 30–91% of the
time depending on format, and the rate is not uniform across models or across
what kind of missing information is at stake — a model can be well-calibrated
to explicit risk and blind to implicit insufficiency at once, which means
"the model knows when to stop" cannot be checked with a single aggregate
rate.

A second trigger is reported in a different setting. In the olympiad-mathematics agent Intern-S1-MO, the authors name a "premature conclusion bias" in the same family: "when reasoning budgets are exhausted, models tend to rush toward" incomplete or incorrect final answers, instead of acknowledging partial progress.[^c7] Here the cause is an exhausted budget, not missing information, so the trigger differs from the clinical one above. The authors state the bias as an observation that motivates their design and do not measure its rate. Their mitigation is to train the model to "produce partial deductive progress in single-turn attempts," so that unfinished work is still written down as sub-lemmas that a later round can use (see [[verified-lemma-memory]]).[^c8]

A third setting names the same error inside an agent's own diagnostic trail. In Deep-DxSearch, a retrieval-augmented diagnostic agent, three physicians adjudicated each failed case into a taxonomy of error causes. "Premature diagnostic closure" is defined there as "finalizing diagnosis without sufficient evidence," and it accounts for more rare-disease failures than common ones, "surpassing the 24 observed in common diseases" in the count of 31.[^c9][^c10] The authors' description of the behaviour is that the model sometimes finishes "finalizing diagnoses before fully exploring latent pathologies," and they propose that future versions "enforce even more rigorous differential diagnosis protocols before the agent is permitted to conclude a case."[^c11][^c12] This is a count of adjudicated failures in one agent's outputs, not the commitment rate over unanswerable items used above, so it does not reproduce the 30–91% range; it shows the closure error occurs in a retrieval-driven agent and is more frequent in rare cases.

## Limits

- Single domain (clinical medicine) and outcome scoring relied on LLM-based
  judges against physician-written rubrics rather than exclusively human
  evaluation; the authors report strong inter-judge agreement but note this
  "may not fully capture nuanced clinical reasoning or edge cases," and the
  study "remains an evaluation under controlled settings rather than
  real-world deployment."[^c6]
- The construct bundles four distinct safer responses (clarify, abstain,
  escalate, refuse) into one rate; the note above does not distinguish which
  of the four would have been correct in a given failure, so it measures
  *that* commitment was wrong, not *what* the right non-commitment would have
  been.
- Five models, one time window (Nov 2025–Apr 2026); rates on newer models are
  not implied.

## Related

[[abstention]] · [[safety-oriented-prompting]] · [[clarification-benchmarks]] · [[calibration]] · Commitment

[^c1]: handler-2026 — "We define LLM premature closure as inappropriate commitment under uncertainty: providing an answer, recommendation, or clinical guidance when the safer response would be clarification, abstention, escalation, or refusal."
[^c2]: handler-2026 — "In the structured multiple-choice setting, premature closure was measured as false action: selecting an answer when the correct option had been removed."
[^c3]: handler-2026 — "At baseline, models falsely selected an answer on an average of 71% of unanswerable multiple-choice items, gave inappropriate direct answers on 30% of standard HealthBench questions, and endorsed unsafe actions on 78% of adversarial queries."
[^c4]: handler-2026 — "Models exhibited the highest rates of premature closure in underspecified low-risk scenarios (baseline premature closure 73–96% across models, average 81%), and substantially lower rates in underspecified urgent scenarios (baseline 5–36%, average 19%)."
[^c5]: handler-2026 — "In medicine, premature closure describes the cognitive error of committing to a diagnosis or plan before sufficient information has been gathered"
[^c6]: handler-2026 — "outcome assessment relied on LLM-based judges using structured rubrics rather than exclusively human clinician evaluation"
[^c7]: arxiv-2512-10739 — "when reasoning budgets are exhausted, models tend to rush toward"
[^c8]: arxiv-2512-10739 — "produce partial deductive progress in single-turn attempts"
[^c9]: doi-10-48550-arxiv-2508-15746 — "finalizing diagnosis without sufficient evidence"
[^c10]: doi-10-48550-arxiv-2508-15746 — "surpassing the 24 observed in common diseases"
[^c11]: doi-10-48550-arxiv-2508-15746 — "finalizing diagnoses before fully exploring latent pathologies"
[^c12]: doi-10-48550-arxiv-2508-15746 — "more rigorous differential diagnosis protocols before the agent is permitted to conclude a case"
