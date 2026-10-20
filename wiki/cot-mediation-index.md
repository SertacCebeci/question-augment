---
description: "CMI scores how much an answer causally depends on CoT-token hidden states, by patching them against matched control patches; behavioral CoT gains do not predict it."
aliases: ["CoT Mediation Index", "CMI", "layerwise CoT activation patching audit", "CoT bypass regime"]
sources: ["arxiv-2602-03994"]
---
# CoT Mediation Index

A causal test of whether an emitted chain of thought is used by the model that emitted it. The audit compares a with-CoT run against a no-CoT run. It patches hidden states from the no-CoT run into the with-CoT run at the CoT token positions, one layer at a time, and records how far the log-probability of a reference answer falls.[^c1] This is the "CoT drop". A matched placebo, the "control drop", patches the same number of random non-CoT positions, averaged over several draws.[^c2]

The index subtracts the placebo from the CoT drop and divides by the floored sum of the two. It is zero when both drops are below a noise floor, so numerical noise cannot produce a spurious effect.[^c3] Bypass is defined as 1 − CMI. Low CMI means the decision is weakly coupled to the explicit CoT text under these interventions.[^c4] Peaks or bands in the layer profile are called "reasoning windows", which the authors label an analysis heuristic.[^c5]

## What was measured

- Across model families, CMI is usually depth-localized. Only a small subset of layers carries most of the CoT-specific effect.[^c6]
- Mean CMI ranged from 0.1230 (Phi-mini-MoE-instruct) down to 0.0000 (Qwen3-4B). The share of layers that were active ranged from 27.03% to 0.00%.[^c7]
- Routing depth differs by architecture even at similar size: DialoGPT-large follows CoT in early layers and Qwen3-0.6B in late layers.[^c8]
- Scale alone did not help. phi-4 had much lower CMI than Phi-4-mini-reasoning, though it is nearly four times larger. The authors theorise that reasoning-specific training explains this.[^c9]
- Mixture-of-experts models had more distributed profiles. The authors' explanation, routed computation, is a hypothesis.[^c10]
- On TruthfulQA, nearly all instances were near-total bypass (CMI ≈ 0).[^c11] On GSM8K, instances that are computationally expensive for the model tended to show higher CMI.[^c12]

The point for questioning and answering is that a rationale that reads well is not evidence the answer was derived from it. Behavioral gains under CoT do not imply the computation depends on the emitted text.[^c13]

## Limits

- Low CMI at a layer means only that no CoT-position mediation remains at that layer. Attention can move CoT information into non-CoT positions earlier, so the authors say it "may point to complete CoT bypass, but not necessarily so".[^c14]
- Activation patching can introduce distribution shift and fragility unrelated to the target mechanism. Residual confounds may remain in deep layers.[^c15]
- Models are small (0.6B to 8B, plus phi-4), the prompt sets are small (heatmaps use 20 StrategyQA prompts), and compute limits statistical power. The paper reports no significance tests that I saw.[^c16]
- The thresholds (drop floor, denominator floor) are free parameters. The authors give no sensitivity analysis in the slices I read. This is my observation.
- The MoE and reasoning-training explanations are untested conjectures. The paper does not run controlled ablations.
- Whether bypass means the answer was computed latently or is simply easy (as in TruthfulQA, where the baseline favors the myth answer) is not separated. That reading is mine.

## Related

- [[cot-reasoning-faithfulness-by-truncation]] — a behavioral, text-level faithfulness test; this note is the internal-state counterpart.
- [[stance-consistency-plus-causal-influence-faithfulness]] — another pairing of a surface signal with a causal-influence check.
- [[cot-monitorability-information-bound]] — what a CoT monitor can learn is bounded by how much the trace carries.
- [[cot-intervention-health-metrics]] — other measures of CoT interventions.

[^c1]: arxiv-2602-03994 — "We patch hidden states from x¬c into xc at the CoT token positions and measure the"
[^c2]: arxiv-2602-03994 — "In practice, we average this quantity over multiple random draws to reduce variance."
[^c3]: arxiv-2602-03994 — "If ∆cot,ℓ + ∆ctrl,ℓ is tiny, the estimate is dominated by numerical noise and sampling variance, so"
[^c4]: arxiv-2602-03994 — "Low CMI indicates that the model’s decision is weakly coupled to"
[^c5]: arxiv-2602-03994 — "This is an"
[^c6]: arxiv-2602-03994 — "Across many models, we observe that"
[^c7]: arxiv-2602-03994 — "27.03%"
[^c8]: arxiv-2602-03994 — "indicates the dependence"
[^c9]: arxiv-2602-03994 — "We theorise this to be due to the latter being trained specifically for reasoning, while"
[^c10]: arxiv-2602-03994 — "A plausible explanation for this is that their computation is routed rather"
[^c11]: arxiv-2602-03994 — "We find a near-total bypass"
[^c12]: arxiv-2602-03994 — "tend to exhibit higher CMI, whereas low-computation cases tend to have low CMI."
[^c13]: arxiv-2602-03994 — "Together, these"
[^c14]: arxiv-2602-03994 — "which may point to complete CoT bypass,"
[^c15]: arxiv-2602-03994 — "residual"
[^c16]: arxiv-2602-03994 — "This constrains"
