---
description: "In RLVR the accuracy gradient and the calibration-error gradient have negative Fisher inner product for overconfident policies; masking confidence tokens from reward advantage removes the conflict."
aliases: ["accuracy-calibration tradeoff gradient conflict", "DCPO masked gradient decoupling"]
sources: ["arxiv-2603-09117"]
---
# Accuracy-calibration gradient conflict

Folding a calibration term into an RLVR objective makes two gradients pull against each other on the same parameters. Cheng et al. (2026, DCPO paper) report that earlier coupled methods "improve calibration but often entangle confidence learning with correctness optimization, leading to accuracy–calibration tradeoffs."

## Mechanism

Two objectives are written as policy gradients over trajectories y: accuracy, with gradient E[(R - E[R]) g], and calibration error, whose gradient is E[(dl/dc)(phi - E[phi]) g] with sign reversed (g is the score function, phi a confidence-dependent term). Their Fisher-metric inner product reduces to minus (dl/dc) times Cov(R(y), phi(y)). For overconfident models this is strictly negative, so, in the authors' words, "the Fisher-metric inner product between these two gradients is negative, implying an optimization conflict".[^c1] Any coupled update therefore cannot improve both at once, which the paper offers as the reason the tradeoff appears and why a single reward struggles to reach a Pareto-optimal point.

A companion proposition says accuracy maximisation alone, without entropy regularisation, puts all mass on one correct trajectory (mode collapse), which sharpens confidence-relevant distributions.

## The decoupling

The remedy acts at the level of tokens. The output is split into a reasoning block and a confidence block, separated by a delimiter. Each block gets its own reward and its own group-normalised advantage; a token mask applies each advantage only to its block. The paper states the effect: "derived from correctness supervision do not affect confidence estimation, and vice versa".[^c2] The two objectives share one policy but no longer share a gradient path.

Reported result: on Qwen3-8B across five math benchmarks, accuracy gain matched vanilla GRPO while ECE fell from 0.435 to 0.128 ("decreasing it from 0.435 to 0.128").[^c3]

## Limits

The negative inner product is derived under assumptions about the overconfident regime (the proof leans on an assumption that gives the covariance a sign); the note does not establish it for well-calibrated policies. The decoupling guarantees non-interference only through the mask: the shared weights can still couple the blocks indirectly, which was not measured here. Evidence is on verbalized confidence for math and code with verifiable rewards; open-ended tasks are untested. The 71.6% ECE reduction is the authors' own comparison to the base model, not an independent replication.

## Related

- [[reward-only-advantage-miscalibration]] — a different proof of why reward-only advantages wreck calibration (AUC inconsistency).
- [[decoupled-claim-calibration-training]] — the same separation, achieved with stages and a DPO/GRPO split plus reward masking.
- [[calibration-aware-policy-optimization]] — fixes the advantage estimator instead of separating token blocks.
- [[calibration]] — the property being protected.
- [[fisher-information]] — the metric used for the inner product.

[^c1]: arxiv-2603-09117 — "the Fisher-metric inner product between these two gradients is negative, implying an optimization conflict"
[^c2]: arxiv-2603-09117 — "derived from correctness supervision do not affect confidence estimation, and vice versa"
[^c3]: arxiv-2603-09117 — "decreasing it from 0.435 to 0.128"
