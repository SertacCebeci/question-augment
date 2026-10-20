---
description: "A token-level uncertainty score from the L2 norm of top-K logits, aggregated over an adaptively early-stopped generation prefix, that approaches full-generation accuracy at a fraction of the tokens."
aliases: ["Logit Magnitude", "logit magnitude uncertainty"]
sources: ["zhu-2026-towards"]
---
# Logit Magnitude

> A partial-generation uncertainty estimator: score a response as unreliable from the raw magnitude of its logits during generation, and stop generating once that score has stabilised — cutting the tokens needed before an unreliability signal is available.

## Definition / Mechanism

For generation step $t$, let $\ell_t^{(1)},\dots,\ell_t^{(K)}$ be the top-$K$ logits the model emits (unnormalised, pre-softmax). The token-level score is the L2 norm of their positive part, $u_t = \sqrt{\sum_{k=1}^K \max(\ell_t^{(k)},0)^2}$. Generation proceeds token by token while a set $H_t$ tracks the indices of the current top-$M$ token-level scores seen so far; a patience counter resets whenever a new token enters $H_t$ and otherwise increments. Generation stops at $\tau$ once an end-of-sequence token appears or $H_t$ has gone unchanged for $W$ consecutive steps; the sequence-level score is the mean of the token scores in the final $H_\tau$, min-max normalised.[^c1]

Rationale for using raw logits rather than the softmax-normalised probability: softmax discards the absolute strength of the model's evidence, which the logit magnitude retains as a token-level [[calibration|reliability]] signal.[^c2]

## Why it matters

On Qwen3.5-4B, the early-stopped estimator lost almost no discriminative power relative to observing the full sequence while cutting the token budget substantially: AUROC 0.791 vs 0.793 on COQA (19.4 → 16.3 tokens) and 0.750 vs 0.751 on NewsQA (15.7 → 11.7 tokens); similar behaviour held on Gemma4-4B. In the full-generation setting ($\tau=T$) Logit Magnitude was best or highly competitive against multi-generation baselines ([[semantic-entropy|Semantic Entropy]], Self-Consistency) and single-generation baselines (sequence [[entropy]], LogTokU, hidden-state score, self-certainty) across COQA, NewsQA and the clinical emrQA benchmark.[^c3]

## Limits

The comparison is confined to three QA datasets (COQA, NewsQA, emrQA) and three LLM families (Qwen3.5, Gemma4, Llama3); the paper does not report Logit Magnitude's behaviour on open-ended generation outside QA, nor on non-English text. The early-stopping guarantee (that a stable top-$M$ set means further generation would not change the estimate much) is stated informally here — the paper's actual bound (Appendix C) was not read for this note and is not claimed. [?] Appendix C's early-stopping error bound is unverified — see the `generation-efficient-uncertainty-estimation-taxonomy` gap.

## Related

[[semantic-entropy]] · [[metaue]]

[^c1]: zhu-2026-towards
[^c2]: zhu-2026-towards — "Probability-based uncertainty scores, such as sequence entropy [12], normalise logits into relative probabilities with softmax and may discard the absolute strength of model evidence. Recent work suggests that raw logits retain useful information about evidence strength and model reliability"
[^c3]: zhu-2026-towards — "on Qwen3.5-4B, Logit Magnitude achieves an AUROC of 0.791 on COQA compared with 0.793 for full generation, and 0.750 on NewsQA compared with 0.751, while reducing the average token budget from 19.4 to 16.3 and from 15.7 to 11.7, respectively."
