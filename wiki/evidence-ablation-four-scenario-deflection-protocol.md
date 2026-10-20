---
description: "Varying only the context (none, gold, gold plus distractors, distractors only) separates memory from grounding and shows LVLMs hallucinate instead of deflecting when evidence is missing or noisy."
aliases: ["parametric-oracle-realistic-adversarial evaluation", "deflection versus hallucination protocol", "VLM-DeflectionBench scenarios"]
sources: ["openalex-org-w7154655864"]
---
# Evidence-ablation four-scenario deflection protocol

Accuracy alone hides how a model fails. Moratelli et al. (VLM-DeflectionBench, knowledge-based visual QA) distinguish two wrong outputs: a deflection ("Sorry, I cannot answer...") and a hallucination, an answer not traceable to the retrieved evidence. Both fail the request, but "when faced with insufficient evidence, deflection is the preferable failure mode."[^c1]

## The four scenarios

The same question is asked with a controlled context Z(x): Parametric (empty), Oracle (gold only), Realistic (gold plus distractors) and Adversarial (distractors only).[^c2] Each has an ideal: Parametric should yield minimal accuracy (confirming the questions need retrieval), Oracle high accuracy, Realistic accuracy despite distractors, Adversarial maximal deflection.[^c3] Comparing the four isolates what comes from memory, from grounding and from noise-handling.

Because the instruction is strict grounding, every incorrect non-deflecting answer is scored as hallucination.[^c4]

## What was found (20 LVLMs)

- Handing over the correct evidence does not fix grounding: one model still hallucinates on 41.6% of queries with oracle evidence, which the authors read as "grounding, not retrieval, is the primary bottleneck."[^c5]
- Adding distractors drops accuracy by 10-20 points, and hallucination often exceeds 40%.[^c6]
- Most open-weight models attempt to answer rather than deflect, even in the adversarial setting.[^c7]
- No model is balanced: one over-deflects, one is good only with clean evidence, one gives up oracle accuracy for adversarial robustness.[^c8]
- Stronger refusal prompts raise adversarial deflection (one model 57.6% to 98.2%) but in the realistic setting accuracy collapses (another 57.7% to 9.2%), so prompting is "a powerful but blunt tool".[^c9]

The mechanism is that deflection requires telling absent support from noisy support; a refusal instruction moves the threshold but does not add that discrimination. (That reading is my inference from the trade-off, not a tested claim.)

## Keeping the probe valid

A curation step removes questions that gating models answer without retrieval, and drops distractors that let a gating model answer correctly, so retained items stay retrieval-dependent as models improve.[^c10]

## Limits

- Incorrect answers in Realistic may be misgrounding (picking a distractor) rather than fabrication; the authors merge them anyway.[^c11]
- Parametric accuracy of some proprietary models (27.0%, 23.7%) is attributed to training-set contamination, a guess, not tested.
- Judge is GPT-4o; only agreement with humans was reported.
- Visual-language setting; transfer to text-only QA is untested here.
- Prompt variants were three hand-written strictness levels; model-specific tuning might do better.

## Related

- [[parametric-knowledge-gates-retrieval-noise-damage]] — noise harms most where the model's own knowledge is weak
- [[accuracy-masks-selective-reliability]] — accuracy alone hides abstention behavior
- [[wise-refusal]] — when refusing is the right answer
- [[abstention-base-rate-sensitivity-in-rl]] — how strongly abstention is pushed shifts the trade-off

[^c1]: openalex-org-w7154655864 — "However, when faced with insufficient evidence, deflection is the preferable failure"
[^c2]: openalex-org-w7154655864 — "Adversarial (ZA (x) = K − ) includes only distractors."
[^c3]: openalex-org-w7154655864 — "Adversarial should maximize"
[^c4]: openalex-org-w7154655864 — "we assume all incorrect responses as hallucinations."
[^c5]: openalex-org-w7154655864 — "showing that"
[^c6]: openalex-org-w7154655864 — "accuracy drops by 10–20"
[^c7]: openalex-org-w7154655864 — "systems attempt to answer questions rather than"
[^c8]: openalex-org-w7154655864 — "Overall, no model achieves balanced reliability"
[^c9]: openalex-org-w7154655864 — "prompt engineering is a powerful but blunt tool for the"
[^c10]: openalex-org-w7154655864 — "if any gating model"
[^c11]: openalex-org-w7154655864 — "We acknowledge that in the Realistic"
