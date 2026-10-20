---
description: "Scoring each retrieval step by novelty plus answer-likelihood gain gives a dense signal to stop, continue or expand search during RL, then annealed away; it beats outcome-only RL by 8.6-9.4 EM."
aliases: ["information utility", "DeepControl", "extent and resolution control", "annealed control forcing"]
sources: ["arxiv-2602-01672"]
---
# Information-utility retrieval control

A search agent that is trained only on final-answer correctness gets no feedback on intermediate acquisition choices, so it over-retrieves when evidence is weak and quits early when more evidence would help.[^c1] DeepControl replaces that blind spot with one per-step score, the information utility, and uses it to regulate two separate axes of acquisition: extent (continue searching or not) and resolution (how much retrieved detail to show).[^c2]

## The utility

For the l-th search step the utility is a convex mix, U = ρ·Novelty + (1−ρ)·Effectiveness.[^c3] Novelty asks whether the retrieved content is unseen relative to what is already in the reasoning state. Effectiveness asks whether the injected evidence raises the model's likelihood of a correct answer, measured as a length-normalized log-likelihood of the gold answer strings under a fixed reasoning trace, so that stochastic reasoning does not contaminate the measure.[^c4] The two decay differently: novelty falls quickly after the first retrieval, while effectiveness stays non-zero later, so later evidence is "less novel but still useful for improving answer confidence".[^c5] Using novelty alone would therefore stop too early; this is why both terms are mixed (my inference from the figure description, not an isolated result here).

## Two controls

Extent. If utility stays below δstop for mstop consecutive steps, the controller injects "Stop searching". Conversely, if the agent tries to terminate while recent utility is high (at least δcont) but the gold-answer score is still low, a one-shot "Continue the search for one additional step" is injected.[^c6] Intervention happens only when the agent's choice looks clearly suboptimal under the signal.

Resolution. Retrieved sources are trees (document summary, section, paragraph). Only roots enter the context; the agent may call expand, and during training the top-scoring leaves by utility, together with their ancestors, define target expansions the model is supervised to follow, limiting context growth while keeping high-utility evidence.[^c7]

## Annealing

The control messages are removed gradually during training (annealed control forcing), so the final policy acts well with no controller at test time.[^c8] The default schedule gave the best no-control result; too fast or too slow annealing hurt.[^c9] Utility is a training-time monitor, not a test-time component.

## Measured effect

Across seven QA benchmarks, average EM rose by 9.4 points (Qwen2.5-7B) and 8.6 points (Qwen2.5-3B) over Search-R1.[^c10] Ablations (3B, PPO) show that removing granularity control, continuation control, or both lowers results, and the tool-usage penalty had the largest effect among reward ablations.[^c11] The gain also held with BM25 in place of the E5 retriever.[^c12]

## Limits

- The continuation rule as trained uses a gold-answer score, so it needs labels; gold-answer-free variants are only mentioned as appendix discussion and I did not read their results.
- Evaluated on open-domain QA with Qwen2.5 3B/7B and EM only; no human or non-QA tasks.
- Effectiveness is computed from model likelihood, so it inherits the model's miscalibration; the paper's own thresholds (δstop = 0.2, δcont = 0.3, τscore = −2.0) are hand-set.
- The control schedule and the hierarchical corpus both change at once relative to Search-R1, so the full gain cannot be attributed to utility alone beyond the ablations.
- GRPO showed action-format degeneration in this setting, so PPO was preferred.[^c13]

## Related

- [[coverage-driven-retrieval-control]] — same stop/continue-from-marginal-gain idea, but at inference with a fixed element schema
- [[reasoning-gap-driven-retrieval]] — decides retrieval from the reasoning state
- [[calibrated-retrieval-budget-allocation]] — budgeting how much to retrieve
- [[retrieval-utilization-gap]] — retrieved evidence not being used, which resolution control targets

[^c1]: arxiv-2602-01672 — "However, outcome-only supervision provides limited guidance for intermediate retrieval decisions, especially in long-horizon settings"
[^c2]: arxiv-2602-01672 — "extent, i.e., whether retrieval should continue, and resolution, i.e., how much retrieved detail should be exposed."
[^c3]: arxiv-2602-01672 — "where ρ ∈ [0, 1] balances novelty and effectiveness"
[^c4]: arxiv-2602-01672 — "whether it increases the"
[^c5]: arxiv-2602-01672 — "suggesting that later evidence is often less"
[^c6]: arxiv-2602-01672 — "explicitly terminating further search steps."
[^c7]: arxiv-2602-01672 — "The model is then supervised to follow these targets, prioritizing highutility evidence while limiting context growth."
[^c8]: arxiv-2602-01672 — "gradually removes control signals so that the final policy performs reliably without external intervention"
[^c9]: arxiv-2602-01672 — "The default annealing schedule achieves the best final no-control"
[^c10]: arxiv-2602-01672 — "improves average EM by 9.4 points with Qwen2.5-7B and"
[^c11]: arxiv-2602-01672 — "the tool-usage penalty has the largest effect among reward-related ablations"
[^c12]: arxiv-2602-01672 — "D EEP C ONTROL still improves over Search-R1 under BM25 retrieval."
[^c13]: arxiv-2602-01672 — "GRPO exhibits action-format degeneration in our setting"
