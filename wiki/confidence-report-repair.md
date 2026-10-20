---
description: "Remove abstention from the RL action space; train a mandatory calibrated confidence report with a proper score plus correctness reward, and threshold only at deployment."
aliases: ["report-level repair", "mandatory confidence report training"]
sources: ["che-2026"]
---
# Confidence-report repair

> Instead of letting an RL policy choose whether to answer during training,
> make it answer every question and report a calibrated confidence; decide
> whether to commit only afterward, at deployment.

## Mechanism

Che, Yuan, Zhao & Yu (2026) propose the structural fix to
[[gate-saturation-collapse]]: remove the discrete abstain action from
training entirely. The model answers every prompt and additionally emits a
confidence $c \in [0,1]$, scored by a strictly proper rule (Brier) plus a
correctness reward at weight $\alpha>1$; [[abstention]] is applied only at
deployment time by thresholding $c$ against the rational cutoff $t^{*}$.

"4. Repair. Move abstention from the action space to a" mandatory
confidence report, trained with a strictly proper score plus a correctness
reward and thresholded only at deployment: the report channel has no
shared vanishing factor, and its calibrated optimum is interior and
attracting.[^c1]

## Why it does not collapse

Because the confidence output is deterministic given the input signal
(no action distribution), there is no policy-level KL to anchor and no
shared saturating gate between the reward gradient and the anchor's
restoring force.

"[[emit-only-feedback-obstruction|Proposition 8]] (No shared vanishing factor; anchor-robust)." The Brier
objective's gradient in the confidence-head parameters carries no
action-[[saturation]] factor, and the calibrated optimum ($c \equiv \bar q$)
is an interior, attracting equilibrium under the anchor.[^c2]

A pure proper score alone is not sufficient: at weight $\alpha \le 1$ the
composite's accuracy gradient can still go negative on hard prompts (a
model can gain score by degrading accuracy and reporting the degradation
honestly); the design needs $\alpha>1$ so the correctness term always
pulls accuracy the right way.

## Evidence

At matched initialization and anchor strength, the action-level (penalty)
rule deploys nothing at any signal quality in the paper's live-model
runs, while the report-level rule stays near-rational at all three tested
signal qualities.

"the penalty rule forfeits all of a 46.9%-coverage optimum" while the
report-level mechanism captures 97% of that utility at strong signal
($\lambda=4.5$).[^c3]

"The design lesson, in one sentence: train confidence continuously, with a
proper score plus a correctness reward at" weight $\alpha>1$, and
threshold only at deployment.[^c4]

## Transfer

| | Home field (RL alignment) | Here (answerer's commitment, stall 10) | Survives | Does not |
|---|---|---|---|---|
| Object | Moving a discrete action (abstain) out of the RL objective into a continuously-scored auxiliary channel | A general recipe for training an answerer's "how much to commit" decision without training it to hide | The claim that *properness alone is not the operative variable* — what matters is that the channel used for training has no reachable zero-gradient region, which generalizes past this specific reward shape | The paper's [[calibration]] guarantee (interior, attracting optimum) is proved for a linear/sigmoid confidence head on a bounded feature; it is not shown for confidence heads with no such structure |

## Limits

The repair is validated on a two-type simulated model and single/few-seed
runs on Qwen2.5-1.5B and 7B — the same limited model-scale evidence base as
[[gate-saturation-collapse]]. The composite score's calibration guarantee
assumes the confidence feature is nonconstant on the support of the input
distribution and degrades by $O(\beta)$ (or $O(\beta^2)$ under an extra
margin condition) under a proximal anchor; the paper does not test the
repair under production RLHF pipelines' actual anchor implementations
beyond the true-KL and proximal comparisons reported.

## Related

- [[gate-saturation-collapse]] — the failure mode this repair is designed against
- [[value-of-information]] — the decision-theoretic threshold the deployment-time gate reads
- [[investigative-question-grpo-training]] — a question-generation policy trained with a composite reward in the same family

[^c1]: che-2026 — "4. Repair. Move abstention from the action space to a"
[^c2]: che-2026 — "Proposition 8 (No shared vanishing factor; anchor-robust)."
[^c3]: che-2026 — "the penalty rule forfeits all of a 46.9%-coverage optimum"
[^c4]: che-2026 — "The design lesson, in one sentence: train confidence continuously, with a proper score plus a correctness reward at"
