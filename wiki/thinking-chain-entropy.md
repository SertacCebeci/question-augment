---
description: "Mean per-token entropy inside a VLM's <think> block predicts hallucination better than answer-token entropy once thinking collapses the answer distribution, across three model families."
aliases: ["chain entropy", "thinking chain entropy", "Hthink"]
sources: ["singal-2026"]
---
# Thinking chain entropy

> In thinking-mode VLMs, the [[entropy]] of tokens inside the reasoning chain is a more reliable single-pass hallucination signal than the entropy of the final answer token, because generating the chain itself destroys the answer-token signal.

## Definition / Mechanism

For a VLM that generates a `<think>...</think>` block before its answer,
chain entropy $H_{think}$ is the mean per-token Shannon entropy
$H_t = -\sum_v p_t(v)\log p_t(v)$ over the thinking tokens, computed from
the softmax already produced during greedy decoding — no extra forward
pass, no sampling. Running four VLMs on identical POPE adversarial samples
(1,000 binary yes/no object-presence questions), Singal finds three
distinct patterns for answer-token entropy $H_{ans}$: Qwen3-VL-8B-Thinking
collapses to chance, GLM-4.1V-9B-Thinking does not collapse, and
InternVL3-8B thinks selectively (chains on only 50% of samples).

"Running Qwen3-VL-8B-Thinking and Qwen3-VL-8B-Instruct (the same model family, same vision encoder, differing only in whether a thinking chain is generated) on identical POPE adversarial samples, answer entropy achieves AUROC = 0.899 for hallucination detection in the non-thinking model but falls to AUROC = 0.492 (chance) in the thinking model."[^c1]

Across the two families with enough false positives to measure reliably (Qwen, GLM), chain entropy beats answer entropy on the same samples: "We show that thinking chain signals are consistently superior to answer entropy across the two families with sufficient statistical power (Qwen and GLM): Hthink achieves 0.647 (Qwen) and 0.759 (GLM) vs. answer entropy of 0.492 and 0.716 respectively."[^c2]

A 300-sample VQAv2 pilot and a HallusionBench run replicate the direction: "Chain entropy outperforms answer entropy on all answer types pooled (0.680 vs. 0.595)."[^c3]

For InternVL3-8B the chain-content margin (0.608 vs 0.602) is small and statistically unreliable (nFP = 17); there, chain *presence* — not chain content — carries the signal (false-positive rate 13.1% with no chain vs 6.0% with one).

## Why it matters

The mechanism is conditioning: a thinking chain $z$ that fully resolves the
question before the answer token drives $H(a\mid x,z)$ toward zero,
collapsing the very distribution conventional uncertainty methods read —
so answer-entropy-based abstention (the method under [[abstention]])
silently stops working for exactly the model class it is increasingly
deployed on. Chain entropy recovers a usable signal from the same forward
pass, at no extra inference cost, which is the precondition for the gate in
[[chain-entropy-abstention-gate]].

## Limits

"This holds strongly for Qwen and GLM, but with only marginal and statistically unreliable advantage for InternVL3 (nFP = 17)."[^c4]

GLM's recipe does not collapse at all, and the paper names the mechanism a
conjecture rather than a proven law — "We conjecture these findings reflect
structural properties of thinking-mode decoding; verification across
additional model families is ongoing" — pending replication beyond one
author's four models on two benchmarks plus one VQAv2 pilot.[^c5]

## Related

[[abstention]] · [[semantic-entropy]] · [[chain-entropy-abstention-gate]] · [[entropy-threshold-clarification-trigger]]

[^c1]: singal-2026 — "Running Qwen3-VL-8B-Thinking and Qwen3-VL-8B-Instruct (the same model family, same vision encoder, differing only in whether a thinking chain is generated) on identical POPE adversarial samples, answer entropy achieves AUROC = 0.899 for hallucination detection in the non-thinking model but falls to AUROC = 0.492 (chance) in the thinking model."
[^c2]: singal-2026 — "We show that thinking chain signals are consistently superior to answer entropy across the two families with sufficient statistical power (Qwen and GLM): Hthink achieves 0.647 (Qwen) and 0.759 (GLM) vs. answer entropy of 0.492 and 0.716 respectively."
[^c3]: singal-2026 — "Chain entropy outperforms answer entropy on all answer types pooled (0.680 vs. 0.595)."
[^c4]: singal-2026 — "This holds strongly for Qwen and GLM, but with only marginal and statistically unreliable advantage for InternVL3 (nFP = 17)."
[^c5]: singal-2026 — "We conjecture these findings reflect structural properties of thinking-mode decoding; verification across additional model families is ongoing."
