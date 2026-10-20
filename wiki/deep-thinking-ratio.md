---
description: "Deep-thinking ratio counts tokens whose next-token distribution keeps changing until late layers; it tracks accuracy positively where output length tracks it negatively."
aliases: ["DTR", "deep-thinking tokens", "layer-wise settling depth"]
sources: ["arxiv-2602-13517"]
---
# Deep-thinking ratio

Reasoning effort is usually proxied by how many tokens a model emits. This work argues that effort lives in depth, not length: a token needs more thinking when its predictive distribution keeps being revised across layers. The paper's stated premise is that "simple tokens stabilize early with shallow computation, whereas difficult tokens requiring more thinking exhibit distributional shifts in deeper layers".[^c1]

## Mechanism

For each generated token, the intermediate-layer distribution is compared with the final-layer distribution by Jensen-Shannon divergence. The settling depth is the first layer at which the running minimum of that divergence falls below a threshold g. A token is "deep-thinking" if it settles at or beyond a depth fraction rho of the layer stack. The deep-thinking ratio (DTR) of a sequence is the share of such tokens; "A higher DTR indicates that a larger fraction of tokens undergo extended computation for distributional".[^c2] The reported default is g = 0.5 and rho = 0.85, and stricter settings lower the ratio while keeping a positive slope against accuracy (the paper's sweep).

## What was measured

Across eight reasoning-model variants (GPT-OSS, DeepSeek-R1-distill, Qwen3) on AIME 24/25, HMMT 25 and GPQA-diamond, length was an unreliable proxy: "Output token count exhibits a moderate negative correlation (average 𝑟 = −0.544), suggesting that".[^c3] DTR on the same setting reached an average correlation of 0.828 with accuracy, and beat length-based and confidence-based baselines.

## Use: Think@n

Samples are ranked by DTR computed on only a short prefix (50 tokens), and unpromising ones are abandoned early. The paper reports "Think@𝑛 achieves the best overall performance while reducing inference cost by", roughly half relative to majority-vote self-consistency.[^c4] My inference: for asking and answering, this suggests a response's quality signal can be read from the internal trajectory of its first tokens rather than its length or verbalized confidence, but only where internal activations are accessible.

## Limits

- Needs white-box access to per-layer logits; closed models cannot be scored.
- Evidence is correlational across model-benchmark pairs, on math and graduate science only; no test on open-ended, ambiguous, or clarification-seeking questions.
- The authors caution that "We note that our proposed method does not imply that early-settling" tokens are suboptimal; DTR is a complement to length, not a verdict on any token.[^c5]
- Thresholds g and rho were tuned on these benchmarks; the correlation is more sensitive to g.
- The 50-token prefix result came from a preliminary ablation on one benchmark (AIME 25).

## Related

- [[returns-per-token-spent]] — both ask what a token of compute buys, but DTR measures effort quality, not gain per cost.
- [[sequence-likelihood-confidence]] — a confidence baseline that DTR is reported to outperform.
- [[self-consistency-difficulty-score]] — voting-based signal that Think@n matches at lower cost.

[^c1]: arxiv-2602-13517 — "simple tokens stabilize early with shallow computation, whereas difficult tokens requiring more thinking exhibit distributional shifts in deeper layers"
[^c2]: arxiv-2602-13517 — "A higher DTR indicates that a larger fraction of tokens undergo extended computation for distributional"
[^c3]: arxiv-2602-13517 — "Output token count exhibits a moderate negative correlation (average 𝑟 = −0.544), suggesting that"
[^c4]: arxiv-2602-13517 — "Think@𝑛 achieves the best overall performance while reducing inference cost by"
[^c5]: arxiv-2602-13517 — "We note that our proposed method does not imply that early-settling"
