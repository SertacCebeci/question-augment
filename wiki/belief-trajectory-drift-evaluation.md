---
description: "Scoring a model by how its probability and reasoning for one event move over time, not by final correctness; larger reasoning budgets coincided with more volatile updates."
aliases: ["narrative drift", "temporal drift", "confidence drift", "probability volatility", "human-imitation evaluation"]
sources: ["arxiv-2601-13545"]
---
# Belief-trajectory drift evaluation

Final-answer accuracy hides how an answerer arrived there. TruthTensor queries each model on the same live prediction-market event at regular intervals until resolution, and compares the resulting trajectory with the market-implied probability, which it treats as a human reference.[^c1] Drift is split into three kinds. Narrative drift is inconsistent reasoning about the same event over time. Temporal drift is failure to update appropriately as information arrives, either by ignoring it or by overreacting to noise. Confidence drift is a gap between stated confidence and actual calibration.

Two concrete measures are named: probability volatility, meaning shifts "that cannot be explained by new information", and reasoning-trace divergence between time points.[^c2] Temporal drift is assessed by comparing model updates with market updates after information events and by correlating information arrival with probability shifts.[^c3] The framework's claim is that models with high narrative drift are poor imitators of human probabilistic reasoning.[^c4]

Measured finding: across nearly one million probability updates from eight deployed frontier models, the authors report that performance cannot be summarized by a single score.[^c5] Models with smaller output budgets produced more compact updates and lower variance in revisions, while larger token budgets gave richer causal modeling but more sensitivity to transient information, increasing temporal drift.[^c6]

For asking and answering: a question asked repeatedly is a probe of belief stability. An answer's quality has a time axis, and the stability of a response to irrelevant change is a separate property from its correctness. That reading is my inference from the work.

## Limits

- The reference is the market consensus. Treating it as "human-like" and well-calibrated is assumed, not tested here; markets can be wrong or thin.
- The drift definitions are conceptual. I did not find thresholds separating justified updating from noise, and "not explained by new information" requires a judgment of what counts as information.
- The capacity-volatility link is stated from a descriptive comparison of eight models, with confounds such as vendor, prompt format and token budget. It is not a controlled test.
- Whether low drift causes better answers, or merely correlates with caution, is not established.

## Related

- [[refinement-drift-under-forced-deliberation]] — drift across forced revision steps rather than across time.
- [[knowledge-integration-decay]] — another way answers degrade as information accumulates.

[^c1]: arxiv-2601-13545 — "tracking how model probability estimates and reasoning"
[^c2]: arxiv-2601-13545 — "bility shifts that cannot be explained by new information"
[^c3]: arxiv-2601-13545 — "Comparing model updates to market updates following"
[^c4]: arxiv-2601-13545 — "Models that exhibit high narrative drift are poor human imitators"
[^c5]: arxiv-2601-13545 — "we show that performance cannot be summarized by"
[^c6]: arxiv-2601-13545 — "richer causal modeling but also amplify sensitivity to transient"
