---
description: "Reasoning-oriented training amplifies self-correction, hypothesis testing and uncertainty talk, but the behaviors most tied to correctness (calibration, knowledge alignment) are not amplified."
aliases: ["Behavioral Lift", "amplification-lift mismatch", "amplified does not mean predictive"]
sources: ["doi-10-48550-arxiv-2608-13760"]
---
# Amplification-Lift Gap

A reasoning behavior can become more frequent in a model's trace without becoming more diagnostic of a correct answer. The work defines Behavioral Lift as the accuracy difference when a behavior is present versus absent: Lift(b) = P(correct | b=true) − P(correct | b=false). It is descriptive, not causal: a behavior may be a consequence of being on the right track.[^c1] Across 15 models and 6 benchmarks (text and vision-language), 15,282 traces were annotated.[^c2]

## What was measured

Thinking models strongly amplify self-correction, hypothesis testing and uncertainty acknowledgment, while the highest-Lift behaviors are confidence calibration, knowledge alignment and self-awareness.[^c2] Uncertainty acknowledgment is amplified 3–7x yet is weakly or negatively associated with correctness; confidence calibration is among the strongest positive signals yet barely amplified.[^c2]

Numbers: confidence calibration Lift is +72.2% in VLM benchmarks and +79.6% in LLM benchmarks, yet thinking models are no more likely to show it than instruct models.[^c3] Uncertainty acknowledgment Lift is −16.1% (VLM) and −13.9% (LLM); hypothesis testing is +1.0% in both.[^c4]

Calibration tracks reasoning quality beyond answer correctness: it is rare in lucky guesses and post-hoc rationalizations and common on sound traces (94.7% and 95.9%).[^c5] The ranking holds across modalities, individual benchmarks, response-complexity strata, and reverse conditioning.[^c6]

## Where thinking gains come from

Self-correction has modest overall Lift but is strongly associated with recovery among traces with a detected failure (+39pp), so some behaviors matter mainly after a trace has entered an error state.[^c7] Thinking models win by fewer failures or better recovery, and on a pattern-matching task (LogiQA2) instruct models beat them.[^c8] The gap is also reported at the SFT checkpoint stage and across scale.[^c9]

## Limits

- Lift is correlational; the authors say it is not a causal estimate. The reverse reading (calibrated traces occur because the model already knows the answer) is not excluded. This is also my inference about the confidence-calibration result.
- Annotation of behaviors is by a labeller whose agreement the paper itself calls moderate for key behaviors; I did not verify the details.
- The paper does not isolate the causal contribution of any single training stage.[^c9]
- The proposal to reward calibrated reasoning at process level is a motivation, not something tested here.
- "Amplified" is measured against instruct counterparts of specific model families; other families were not examined.

## Related

- [[thinking-chain-entropy]] — another trace-level signal related to correctness in thinking models
- [[same-model-self-verification-conditional-confidence]] — confidence signals and their reliability as correctness indicators
- [[reasoning-masked-sycophancy]] — longer deliberation not implying sound reasoning

[^c1]: doi-10-48550-arxiv-2608-13760 — "Lift does not imply causation: a"
[^c2]: doi-10-48550-arxiv-2608-13760 — "We find evidence for an Amplification-Lift"
[^c3]: doi-10-48550-arxiv-2608-13760 — "However, thinking models"
[^c4]: doi-10-48550-arxiv-2608-13760 — "Hypothesis testing Lift is +1.0% in both modalities."
[^c5]: doi-10-48550-arxiv-2608-13760 — "Confidence calibration is rare when the answer is correct but the reasoning is weak and common when"
[^c6]: doi-10-48550-arxiv-2608-13760 — "The ranking is stable across modalities, benchmarks, and controls."
[^c7]: doi-10-48550-arxiv-2608-13760 — "Some behaviors matter mainly after failures occur."
[^c8]: doi-10-48550-arxiv-2608-13760 — "Thinking gains come from fewer failures or better recovery."
[^c9]: doi-10-48550-arxiv-2608-13760 — "though these comparisons do not isolate the causal contribution of any single training stage."
