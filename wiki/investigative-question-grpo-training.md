---
description: "Training the question-generation step itself, not through an Inside the BodyCam-VQA pipeline, Gupta et al."
aliases: ["GRPO for question generation", "group relative policy optimization for probe questions"]
sources: ["gupta-2026"]
---
# Investigative-question GRPO training

> Training the question-generation step itself, not through an
> information-theoretic label but through a composite format-plus-judge
> reward — and the trade-off that buys.

## Mechanism

Inside the [[probe-question-video-captioning|BodyCam-VQA]] pipeline, Gupta et al. (2026) train the model that turns structured video details into[^s1]
investigative questions with Group Relative Policy Optimization (GRPO)
rather than supervised fine-tuning (SFT). The base model is
Qwen3-4B-Thinking, adapted with LoRA and run at 4-bit quantisation. The
reward combines two terms with equal weight ($\alpha=\beta=0.5$):

```text
R(o_i) = α · r_format(o_i) + β · r_judge(o_i)
```

- $r_\text{format}$ is rule-based: structural integrity of the output,
  presence of chain-of-thought tags, a length penalty, and keyword bonuses.
- $r_\text{judge}$ is a separate large foundation model scoring the
  generated question's investigative relevance as a binary $\{0,1\}$
  judgement.

Both the SFT and the GRPO variant start from the same cold-start data: 288
examples pairing structured input details, chain-of-thought tokens and a
hand-selected high-quality question, produced with proprietary models.

## Why it matters

On the 359-clip benchmark, GRPO training of the 4B model reached the highest
human factual-accuracy score of any question-generation variant tested
(0.91), against 0.87 for SFT of the same 4B model, 0.86 for SFT of a 30B
model, and 0.78 for the untrained 4B base model. The completeness score
moved the other way: GRPO's 0.55 is below the 30B SFT model's 0.64. Gupta et
al. read this as GRPO "minimizing hallucinations" — the generated questions,
and the answers they pull out of the video, stay closer to what the video
actually shows — at the cost of asking about a narrower slice of it. They
also report that scaling the SFT model from 4B to 30B raised completeness
without raising factual accuracy: more parameters buy coverage, not
grounding, in their results.

## Known as

| Field | Name there | Match |
|---|---|---|
| LLM training (Gupta et al. 2026) | GRPO for question generation | exact — this note's object |
| LLM training (Gupta et al. 2026, algorithm name) | group relative policy optimization for probe questions | exact — the full algorithm name applied to this task |

**Not this concept.** [[preference-optimization-for-questions]] trains a
question-asking policy by a different route — DPO on pairs labelled by an
exactly-computed EIG over an enumerable answer set — and reports a different
kind of result (cross-domain transfer of a ranking ability). Both are
"train the question-generator with a scored objective," but the score, the
algorithm, and what is measured afterward differ, so this is filed as
`close`, not the same object.

## Transfer

| | |
|---|---|
| **In its home field** | GRPO groups several sampled completions for one prompt and uses their relative reward to estimate an advantage with no learned value function, developed for domains with a verifiable reward — a checkable proof step, a unit-testable code fix. |
| **Here** | The verifiable half of the reward is kept as $r_\text{format}$ (checkable structural compliance), but the substantive half, $r_\text{judge}$, is a separate LLM's own opinion of "investigative relevance" — there is no ground truth to check that judgement against. |
| **What survives** | Group-relative advantage estimation itself, and the empirical result that RL training beats SFT on the property its reward actually targets (grounding, i.e. factual accuracy) even starting from a smaller base model. |
| **What does not** | The verifiability that motivated GRPO in its home field. A judge-scored reward can reward a plausible-sounding but ungrounded question exactly as it would reward a well-grounded one; Gupta et al. do not report the judge's own agreement with the human factual-accuracy raters, so the size of that risk is unmeasured here. |

## Limits

- One base-model size pair (4B vs 30B), one domain (BWC video), one judge
  model per training run; the trade-off (accuracy up, completeness down) is
  this configuration's, not shown to be a general property of GRPO vs SFT
  for question generation.
- The 288-example cold-start set is small and was itself built with
  proprietary models under a selection procedure not described in the
  material read for this note, so both SFT and GRPO start from a training
  signal whose own quality is not independently checked.
- $r_\text{judge}$'s binary relevance score has no reported correlation with
  the human factual-accuracy score used to evaluate the final output; the
  reward that shapes the policy and the metric that evaluates it are only
  assumed to point the same way.

## Related

[[preference-optimization-for-questions]] · [[probe-question-video-captioning]] · [[dual-judge-completeness-recall]] · [[expected-information-gain]]

[^s1]: gupta-2026
