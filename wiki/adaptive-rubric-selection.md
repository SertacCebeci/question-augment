---
description: "Scoring each criterion of a shared rubric pool for relevance to the prompt and keeping only the relevant ones improves rubric rewards and prompts, most for weaker models."
aliases: ["adaptive criteria selection", "per-prompt rubric selection", "relevance-gated rubric subset", "adaptive Health-SCORE"]
sources: ["doi-10-48550-arxiv-2601-18706"]
---
# Adaptive rubric selection

A rubric pool is a fixed set of criteria written once and shared across many prompts. Adaptive selection does not apply the whole pool to every prompt. For each prompt, a judge scores every pool item for its relevance on a discrete scale, "a relevance score on a five-point scale", and the items whose scores pass a cut are the ones used for that prompt.[^c1] The rest are not applied. The point is stated plainly in the paper: "Rubrics receiving higher relevance scores are then selectively retained, ensuring that only the appropriate criteria contribute to the final evaluation."[^c2]

The same selected subset then serves two uses. As a training reward, a judge checks the response against each kept criterion, awards +1, -1 or 0 per criterion, and the points "are then summed and normalized to produce a sequence-level reward."[^c3] As in-context guidance, the kept criteria are placed in the prompt, so that "rubrics also function as an evaluation checklist, encouraging the model to verify each requirement as it generates the response."[^c4]

## Why the subset helps

The motive is dilution. A criterion that matters for one kind of conversation can be noise for another. The paper's example is a SOAP-note formatting rule, which "should only be applied when the prompt explicitly" asks for structured clinical documentation.[^c5] Applying the whole pool regardless makes the signal weaker, and the authors say so directly: "indiscriminately including all rubric criteria can dilute the" learning or guidance signal, "introducing many constraints, some of which may not be relevant to the specific conversation."[^c6]

## What was measured

In the selection ablation the adaptive variant is compared with the same pool applied in full. The authors report that "mechanism consistently improves evaluation scores across all settings and models," and that this holds both when the mechanism is used in training and when it is used only at inference, through in-context learning.[^c7] The effect is described as "particularly stronger for weaker models", with Qwen3-8B named as the example.[^c8]

In the main comparison, reward formulations built from the adaptive subset were ranked above fixed multi-axis rubrics and per-prompt LLM-generated rubrics. The paper's reading is that "adaptively selecting relevant evaluation criteria provides a more effective training signal than either fixed or automatically generated rubrics."[^c9] Inference-time use is reported too: the paper says that using adaptive selection "purely at inference time also yields consistent performance gains."[^c10] A further, related result is that the same rubric text placed in a frontier model's prompt raised its scores, with the paper naming GPT-5, o3 and GPT-4.1.[^c11]

What the measurements show is a comparison between an adaptive subset and the full pool, and between adaptive and non-adaptive rubric sources. They do not show a comparison between an adaptive subset and a random subset of the same size. The paper does not run that control in the text I read, so whether the gain comes from relevance or simply from using fewer criteria is open.

## Limits

- The text I read reports the direction of the ablation, not its size or spread. I did not check the table's margins against run-to-run noise.
- Relevance is itself judged by an LLM. The authors concede that "automated evaluation may still exhibit biases or inconsistencies" in safety-critical domains.[^c12] A criterion wrongly scored irrelevant is never shown to the policy, and the paper does not measure how often that happens.
- The cut and the five-point scale are not varied in the parts I read, so I cannot say how sensitive the subset is to them (my inference).
- The experiments are on health data. The authors write that their "findings may not imply universal applicability across all healthcare tasks or non-medical domains."[^c13]
- The pool is fixed in advance. Whatever the pool omits, selection cannot recover. Per-prompt rubrics that write new criteria are a different answer to the same problem (see [[question-specific-rubric]]).

## Related

- [[clustered-criteria-pool]] — how the shared pool itself was built, from physician rubrics; this note is about choosing from such a pool per prompt
- [[question-specific-rubric]] — writes new criteria for each question; adaptive selection instead picks from a pool written in advance, so its coverage is capped by that pool (my inference)
- [[rubric-criterion-dropout]] — also applies a subset of criteria, but a random mask each step for regularization; selection here is deterministic and keyed to relevance, so the two answer different questions
- [[false-credit-propagation]] — a flat sum counts criteria whose licensing condition is absent; per-prompt selection removes some inapplicable criteria before the sum, for conditions the pool author anticipated, though it does not model dependencies between criteria (my inference)
- [[rubric-conditioning-gap]] — the lift from placing a rubric in context, measured forward-only; the in-context use here is the same lever at inference time

[^c1]: doi-10-48550-arxiv-2601-18706 — "relevance score on a five-point scale"
[^c2]: doi-10-48550-arxiv-2601-18706 — "Rubrics receiving higher relevance scores are then selectively retained, ensuring"
[^c3]: doi-10-48550-arxiv-2601-18706 — "all selected rubrics are then summed and normalized to produce a sequence-level reward"
[^c4]: doi-10-48550-arxiv-2601-18706 — "rubrics also function as an evaluation checklist, encouraging the model to verify each requirement"
[^c5]: doi-10-48550-arxiv-2601-18706 — "should only be applied when the prompt explicitly"
[^c6]: doi-10-48550-arxiv-2601-18706 — "indiscriminately including all rubric criteria can dilute the"
[^c7]: doi-10-48550-arxiv-2601-18706 — "mechanism consistently improves evaluation scores"
[^c8]: doi-10-48550-arxiv-2601-18706 — "The effect is particularly stronger for weaker"
[^c9]: doi-10-48550-arxiv-2601-18706 — "criteria provides a more effective training signal"
[^c10]: doi-10-48550-arxiv-2601-18706 — "also yields consistent performance gains"
[^c11]: doi-10-48550-arxiv-2601-18706 — "Health-SCORE can improve performance even for frontier models such as GPT-5, o3"
[^c12]: doi-10-48550-arxiv-2601-18706 — "automated evaluation may still exhibit biases or inconsistencies"
[^c13]: doi-10-48550-arxiv-2601-18706 — "not imply universal applicability across all healthcare tasks or non-medical domains"
