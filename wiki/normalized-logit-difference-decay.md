---
description: "NLDD corrupts one CoT step and measures the normalized loss of answer logit margin; it finds a reasoning horizon near 70-85% of chain length and models whose accuracy ignores the chain."
aliases: ["NLDD", "reasoning horizon", "anti-faithful regime", "mapping gap"]
sources: ["arxiv-2602-11201"]
---
# Normalized logit difference decay

Whether a chain-of-thought explains an answer can be asked per step. Ye et al. corrupt one intermediate step (keeping surface coherence, at most a two-token difference from the clean chain), truncate the steps after it, and compare the answer's logit margin on the clean and corrupted chains. The metric is NLDD = (LD_clean − LD_corrupt) / |LD_clean| × 100.[^c1] Dividing by the clean margin makes models with different output scaling comparable (for instance Gemma-2's logit soft-capping); samples with near-zero clean margin are dropped.[^c2]

## Three readings of the sign

Positive NLDD means corruption degrades confidence, so the answer depends on the chain. Near zero means weak coupling. Negative means "confidence reversal": corrupting the chain raises the answer margin.[^c2] On GSM8K, Llama and DeepSeek both exceed 96 NLDD at 100% clean accuracy. On PrOntoQA Gemma reaches 99.0% accuracy at an NLDD of -52.5%, so the trace acts as post-hoc rationalization rather than a driver.[^c3] Accuracy alone cannot separate these regimes.

## Reasoning horizon

The horizon k* is the corruption position with maximum mean NLDD. It falls at about 85% of the chain on GSM8K (step 5 of 6), about 80% on Dyck-n, and 70-100% on PrOntoQA.[^c4] Past k*, further reasoning tokens add negligible or negative causal influence. Representational similarity (RSA) stays stable across the horizon, which the authors call "a representational echo without causal force".[^c5] In Gemma's PrOntoQA, extended reasoning deepens the anti-faithfulness, interfering with a pre-existing correct computation.[^c6]

## Mapping gap

Internal encoding and use come apart. In Gemma on Dyck-n, linear probes recover stack depth at 82.0% accuracy while the model scores 0.0% on the task with a full CoT.[^c7] Representational fidelity does not ensure causal use. This means a correct probe readout cannot stand in for a faithful answer, and neither can a correct final answer.

## Limits

- The chains are truncated rather than replaced, so low NLDD at step k may mean weak reliance on k, or that steps before k already sufficed.[^c8]
- The normalization assumes architectural differences scale margins proportionally; the authors say this is "supported empirically but not guaranteed".[^c8]
- RSA and TAS use one layer (50% depth). Three models of 6.7-9B parameters and three synthetic or benchmark tasks were tested; the "consistent" horizon is a pattern over these, not a law. GSM8K uses a first-token margin as a proxy for multi-token answers.[^c2]
- That a chain "is" post-hoc when NLDD is negative is the authors' reading; corruption can also act as a distractor on its own (my inference).

## Related

- [[cot-reasoning-faithfulness-by-truncation]] — a coarser truncation probe with no corruption or logit margin
- [[stance-consistency-plus-causal-influence-faithfulness]] — another faithfulness test that adds causal intervention
- [[accuracy-masks-unstable-reasoning]] — accuracy hiding what the reasoning does, here at step level
- [[cot-monitorability-information-bound]] — what a chain can reveal to a monitor

[^c1]: arxiv-2602-11201 — "NLDD quantifies proportional confidence loss:"
[^c2]: arxiv-2602-11201 — "Negative values represent confidence reversal, where corruption paradoxically increases the answer"
[^c3]: arxiv-2602-11201 — "near-perfect task performance can coexist with a lack of functional dependence on CoT."
[^c4]: arxiv-2602-11201 — "The horizon occurs at a consistent relative depth across tasks."
[^c5]: arxiv-2602-11201 — "a representational echo without causal force"
[^c6]: arxiv-2602-11201 — "Extended reasoning"
[^c7]: arxiv-2602-11201 — "stack-depth information with 82.0% accuracy"
[^c8]: arxiv-2602-11201 — "supported empirically but not guaranteed"
