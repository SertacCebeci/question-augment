---
description: "An LLM act-or-escalate choice follows a model-specific implicit confidence threshold, unrelated to scale or self-calibration, missing the cost-optimal 1 - c_l/c_w unless reasoning meets cost framing."
aliases: ["escalation threshold", "act-or-escalate threshold", "implicit threshold p*"]
sources: ["arxiv-2604-08588", "arxiv-2602-19509"]
---
# Implicit escalation threshold

Every action an agent takes contains an implicit choice to implement rather than escalate to a human. DiSorbo and Ju model it as a decision under uncertainty: the agent predicts, estimates its probability of being correct p̂, and escalates when p̂ falls below a threshold τ.[^c1] Escalating costs the human labor c_ℓ; implementing a wrong answer costs c_w > c_ℓ; a correct implementation costs nothing.[^c2]

## The optimal threshold and the cost of deviation

With perfectly calibrated p̂, the unique cost-minimising threshold is τ* = 1 − c_ℓ/c_w.[^c3] At cost ratio R = 4 this is 75%. A systematic bias μ in p̂ shifts the effective threshold to τ* − μ, so expected cost rises with |μ|: overconfident models implement too aggressively, underconfident ones escalate too often.[^c4] This is the paper's own theory (proofs in its appendix, not rechecked here).

## What models actually do

The authors give each scenario an external accuracy signal (a decision-tree summary) and fit a line to escalation rate against accuracy; the accuracy where the fit crosses 50% is the model's implicit threshold p*. Across eight models in four families it ranges from about 53% to above 100%. Qwen3.5-9B and GPT-5-mini implement even at low accuracy (p* ≈ 54%), while GPT-5-nano, Llama 4 Maverick, Llama 3.3 70B and Mixtral 8x7B escalate even when quite accurate (p* > 91%).[^c5] The spread persists inside every family: GPT-5-nano (91%) versus GPT-5-mini (53%) differ by 38 points, so scale does not predict direction.[^c6]

Self-estimated accuracy, recovered by mapping the no-signal escalation rate onto the signal curve, does not explain this: it spans 76% to 97% and is "largely independent" of p*; a model can be overconfident yet cautious, or slightly underconfident yet aggressive.[^c7] Across 304 model-by-condition pairs, 201 (66%) were overconfident, but direction varies by model and domain.[^c8] So there are two separate quantities to measure, belief about accuracy and threshold on that belief.

## Moving the threshold

Scored against the R = 4 optimum, Qwen3.5-9B reaches 62.0% decision accuracy at baseline, 63.9% with cost framing alone, 61.9% with thinking alone, and 78.8% with both; GPT-5-mini goes 64.7% → 87.1% with reasoning plus cost framing.[^c9] Thinking alone fails because the model predicts better but escalates less; the two interventions are complementary.[^c10] Supervised fine-tuning on chain-of-thought targets that extract the signal's accuracy and compute the expected cost (R × error rate against 1) reached 100% on all training cost ratios and on the held-out MovieLens domain; removing the signal dropped it to about 84% as the model hallucinated accuracies.[^c11]

## A second barrier: an imperfect escalation target

Khaled's escalation rule generalises the cost-only cascade: escalate when P_fail > C_esc/U_correct + (1 − P_oracle). The first term is the cost barrier; the second, the imperfection barrier, is the chance the stronger model also fails. When P_oracle → 1 it vanishes and the standard rule returns; when a correct answer is worth far more than escalation, the imperfection barrier dominates.[^c12] The paper's own derivation; it does not measure P_oracle per query.

## Limits

- Tasks are binary predictions of recorded human preferences; escalation is a single yes/no with fixed, stated costs. Open-ended or multi-step agents, with unknown costs, are untested.
- The signal is an externally supplied accuracy; the fine-tuned policy depends on it and degrades without it, so it fixes the threshold rule, not the model's calibration.
- p* is a linear-fit summary; the authors note non-monotonic curves, and some p* exceed 100%, meaning the fit extrapolates.
- Prompting results are one open model and one reasoning model with small samples (50 per thinking run); the perfect SFT score is on a template-matched arithmetic rule, and the held-out domain is a single dataset.
- That scale does not predict threshold is shown on four pairs of models only.

## Related

- [[expected-utility]] — the cost comparison underlying τ*
- [[value-of-information]] — asking versus acting is the same cost trade-off
- [[two-stage-abstention-paradigm]] — abstention as a separate decision after prediction
- [[uncertainty-aware-router]] — routing by uncertainty, as here with a threshold
- [[step-level-risk-calibrated-router]] — risk-calibrated escalation per step

[^c1]: arxiv-2604-08588 — "The agent escalates when its estimated probability of being correct p̂ falls below a threshold τ."
[^c2]: arxiv-2604-08588 — "Correct implementations incur zero cost."
[^c3]: arxiv-2604-08588 — "Then τ ∗ = 1 − cℓ /cw is the unique threshold that minimizes expected cost."
[^c4]: arxiv-2604-08588 — "Then expected cost is increasing in"
[^c5]: arxiv-2604-08588 — "Qwen3.5-9B and GPT-5-mini have low thresholds (p∗ ≈ 54%), meaning they prefer to implement even at low accuracy levels."
[^c6]: arxiv-2604-08588 — "This variation persists within every model family we test."
[^c7]: arxiv-2604-08588 — "but the two are largely independent"
[^c8]: arxiv-2604-08588 — "Across 304 model × condition pairs, 201 (66%) are overconfident."
[^c9]: arxiv-2604-08588 — "The combination of thinking and cost framing achieves 78.8% accuracy, a substantial improvement over all other Qwen conditions."
[^c10]: arxiv-2604-08588 — "Neither intervention is sufficient alone; they are complementary."
[^c11]: arxiv-2604-08588 — "Without the signal, accuracy drops from 100% to approximately 84% as the model"
[^c12]: arxiv-2602-19509 — "the primary reason to avoid escalation is"
