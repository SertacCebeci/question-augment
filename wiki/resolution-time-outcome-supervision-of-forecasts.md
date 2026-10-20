---
description: "Forecast questions that resolve after a causal cutoff supply free labels; a log-score reward on the resolved outcome trains a smaller model to better Brier and calibration than a larger one."
aliases: ["Foresight Learning", "Future-as-Label", "outcome-resolved reinforcement learning for forecasting"]
sources: ["arxiv-2601-06336"]
---
# Resolution-time outcome supervision of forecasts

A question about the future carries its own answer key: the event resolves later, so no annotator is needed. Foresight Learning builds a training loop on this. At time t the predictor sees only information dated up to t and emits a probability for an event that resolves at s > t. A separate frozen resolver, which sees post-t sources, decides what happened. The reward arrives only then.[^c1]

## Mechanism

**Two roles with an information gap.** The predictor is the model being trained. The resolver is a fixed pretrained model that never sees model outputs and is used solely to resolve outcomes, not to score or rank predictions.[^c2] Learning is driven by the gap between the predictor's masked view at t and the resolver's unmasked view at s.[^c3]

**Reward.** The terminal reward is the log score, y·log(p) + (1−y)·log(1−p), a strictly proper scoring rule. There are no intermediate rewards.[^c4] Overconfident wrong predictions are penalised heavily, so the signal favours calibrated probabilities.[^c5]

**Optimisation.** Group Relative Policy Optimization: four trajectories per event, each reward minus the group mean as advantage. This reduces variance from outcome noise when feedback is only terminal.[^c6]

**Leakage control.** Inputs come only from sources published at or before t. Articles with missing or ambiguous timestamps are excluded. All training events resolve after the base model's knowledge cutoff, so outcomes cannot sit in parametric memory.[^c7]

**Not plain supervised learning.** In expectation the reward maximises the log-likelihood of realised outcomes given the prediction-time information. The authors still treat it as a policy over reasoning trajectories evaluated retrospectively, not a differentiated likelihood.[^c8]

## Measured results

Training used 5,120 synthetic binary questions (predictions dated July 2024 to January 2025). The tests were 500 held-out synthetic questions and 293 human-written Metaculus questions, all predicted on or after 1 February 2025.[^c9] Metaculus results for Qwen3-32B, pretrained versus trained, were Brier 0.2472 versus 0.1793 and ECE 0.2175 versus 0.1042. On synthetic questions ECE went from 0.1732 to 0.0598. Qwen3-235B scored Brier 0.2111 on Metaculus.[^c10] A seven-sample median ensemble gave only modest gains, which the authors read as showing the improvement comes from the objective, not from sampling or scale.[^c11]

## Limits

- Resolution is by a frozen LLM (Gemini-2.5-Flash). The authors say its errors add noise but not an endogenous reward; the size of that noise was not measured, and low-confidence resolutions were discarded, which could bias the retained questions.[^c12]
- Horizons run from days to a few weeks; longer delays were not tested.
- The training questions were generated from news by a model, so the distribution is narrow (politics, economics, corporate actions). The authors offer higher-salience Metaculus events as one possible reason for the transfer and say it needs study.[^c13]
- One model family, one run per condition, no validation set, no confidence intervals reported. Whether Brier improvement reflects better discrimination or only better calibration is not separated (my inference; see [[calibration-training]] on Brier mixing the two).
- Binary outcomes only; richer outcome spaces are claimed to generalise, not shown.

## Related

- [[log-score-verbalized-confidence-reward]] — same proper-scoring reward, there applied to stated confidence on answers with checkable correctness
- [[calibration-training]] — human forecasting calibration training; Brier mixes calibration and resolution
- [[post-cutoff-corpus-benchmark-isolation]] — the same leakage logic: keep evaluation events after the knowledge cutoff
- [[confidence-first-segmented-credit-rl]] — another RL setup with Brier-type confidence rewards

[^c1]: arxiv-2601-06336 — "Time creates free supervision: forecasts about real-world events resolve to verifiable outcomes."
[^c2]: arxiv-2601-06336 — "The resolver has access to post-t information unavailable to the predictor and is used solely to resolve outcomes, not score or rank predictions."
[^c3]: arxiv-2601-06336 — "Learning is driven by the information gap between the predictor’s masked view at time t and the resolver’s unmasked view at time s."
[^c4]: arxiv-2601-06336 — "Each episode terminates after outcome resolution; there are no intermediate rewards."
[^c5]: arxiv-2601-06336 — "overconfident incorrect predictions incur large penalties, while appropriately uncertain predictions are penalized less severely."
[^c6]: arxiv-2601-06336 — "By comparing trajectories generated under identical pre-t information, GRPO reduces variance from outcome noise"
[^c7]: arxiv-2601-06336 — "All training events resolve strictly after the pretrained model’s knowledge cutoff, ensuring that realized outcomes cannot be encoded in the model’s parametric memory."
[^c8]: arxiv-2601-06336 — "In expectation, optimizing this reward corresponds to maximizing the log-likelihood of realized outcomes conditioned on the information available at prediction time."
[^c9]: arxiv-2601-06336 — "Both test sets consist exclusively of predictions made on or after February 1, 2025, ensuring strict temporal separation between training and evaluation."
[^c10]: arxiv-2601-06336 — "Qwen3-32B-RL (160)"
[^c11]: arxiv-2601-06336 — "indicating that the improvements stem from the training objective rather than increased sampling or model scale."
[^c12]: arxiv-2601-06336 — "resolution errors introduce noise but do not induce endogenous reward signals."
[^c13]: arxiv-2601-06336 — "While this hypothesis requires further study"
