---
description: "A safety metric for the answerer's commit decision — wrongly labelling a high-risk case low-risk — driven to near-total failure by reusing one language's risk heuristic on translated text."
aliases: ["under-triage rate"]
sources: ["albattra-2026"]
---
# Under-triage

> Not every wrong answer looks like a wrong answer: routing a case that
> should be escalated into the "routine, no need to ask further" bucket is a
> commit failure that a plain accuracy number does not surface.

## Definition / Mechanism

Albattra et al. (2026) define the metric directly:
"Under-triage is the proportion of reference see-doctor cases assigned
routine; over-triage is the opposite error."[^c1]

It is a class-conditional error rate on the answerer's risk label, computed
only over the parse-valid subset whose reference risk is the higher-urgency
class — a model that never assigns the low-risk label scores 0 under-triage
regardless of its accuracy elsewhere.

## Why it matters

The paper measures under-triage across five adapted configurations of one
multilingual model in three languages. A zero-shot baseline shows
0.632–0.674 under-triage; after joint English–French–Arabic QLoRA
adaptation, English under-triage is nearly unchanged but French and Arabic
collapse: "Model 4 leaves English under-triage nearly unchanged
(0.718→0.711) but raises it to 0.994 in both French and Arabic (from 0.632
and 0.638)."[^c2]

The cause is traced to the supervision pipeline, not the languages
themselves or the base model: risk labels for the multilingual adaptation
corpus had been recomputed per language by applying an English-keyed
keyword heuristic directly to translated answer text, and "missing English
consultation terms produced language-asymmetric labels heavily skewed
toward routine."[^c3]

Re-deriving the risk label once from the English source and propagating it
to the matched translations by shared case identity — a language-invariant
provenance fix, with no other change to adaptation — "reduces under-triage
from 0.994 to 0.572 in French and 0.558 in Arabic" (and to 0.590 in
English), each below the zero-shot baseline, with the correction confirmed
on the reference high-risk subset (McNemar p = 4.0×10⁻²¹ French, p =
5.3×10⁻²³ Arabic).[^c4]

The same correction does not touch a second, independent failure of the
answerer — see [[adaptation-suppresses-clarification]].

## Transfer

| | |
|---|---|
| **In its home field** | Clinical/telehealth triage: an urgency classification made by trained staff, evaluated against patient outcomes and clinician-adjudicated severity, with an explicit doctrine that a missed high-urgency case is costlier than a false alarm |
| **Here** | An LLM's risk-label output on a health-communication query, scored against a reference label as a class-conditional error rate |
| **What survives** | The ordinal urgency framing and the asymmetric-cost intuition — reporting under- and over-triage separately so aggregate accuracy cannot hide the more costly error |
| **What does not** | The ground truth. The reference labels here are a "transparent deterministic keyword heuristic" over source answer text, not clinician-adjudicated judgements — both targets are silver rather than clinician-adjudicated — so the metric evaluates agreement with a heuristic, not with real clinical urgency |

[^c5.1][^c5.2][^c5]

## Limits

- The reference risk labels are silver (keyword-heuristic), not
  clinician-adjudicated, so the absolute under-triage values are a property
  of that heuristic's severity threshold, not of real clinical risk; the
  paper states this explicitly and warns the result "does not establish
  clinical safety."
- McNemar comparisons treat matched items as independent pairs with no
  cluster-aware confidence interval over source cases; the authors describe
  their own inferential claims as exploratory.
- Measured on one model family (Qwen3.5-9B-Instruct), one adaptation method
  (QLoRA), three health topics, and three languages; whether
  language-asymmetric label provenance causes the same collapse in other
  adaptation pipelines or domains is untested.

## Related

[[adaptation-suppresses-clarification]] · [[clarification-benchmarks]] · [[value-of-information]] · [[expected-utility]]

[^c1]: albattra-2026 — "Under-triage is the proportion of reference see-doctor cases assigned routine; over-triage is the opposite error."
[^c2]: albattra-2026 — "Model 4 leaves English under-triage nearly unchanged (0.718→0.711) but raises it to 0.994 in both French and Arabic (from 0.632 and 0.638)."
[^c3]: albattra-2026 — "Missing English consultation terms produced language-asymmetric labels heavily skewed toward routine."
[^c4]: albattra-2026 — "Model 5 reduces under-triage below Model 1 to 0.572 (French), 0.558 (Arabic), and 0.590 (English)."
[^c5.1]: albattra-2026 — "a transparent deterministic keyword heuristic derives silver risk targets from source answer text."
[^c5.2]: albattra-2026 — "Both targets are silver rather than clinicianadjudicated."
[^c5]: albattra-2026
