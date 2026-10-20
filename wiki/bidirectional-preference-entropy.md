---
description: "Scoring a pairwise judge in both response orders and taking the binary entropy of the averaged preference gives an order-neutral uncertainty score that ranks judge errors better."
aliases: ["BPE", "bidirectional preference entropy", "order-averaged preference entropy"]
sources: ["arxiv-2602-13110"]
---
# Bidirectional preference entropy

A pairwise LLM judge's confidence in "A" or "B" is contaminated by where the response was placed. Bidirectional Preference Entropy (BPE) removes that nuisance by asking the same question twice with the order swapped and scoring the aggregate.

## Mechanism

The judge is queried on the pair in forward order and in reverse order. Preferring response rA means label A in the forward prompt and label B in the reverse prompt, so the two probabilities are aligned to the same preference and averaged: p̄ = (p_fwd + p_rev)/2. The uncertainty score is the binary entropy of p̄, maximal at p̄ = 0.5.[^c1] The paper's rationale is that a reliable judge should give rA a similar probability whichever slot it occupies.[^c2] Disagreement across orders pulls p̄ toward 0.5 and so raises the score. BPE therefore penalizes position bias through the aggregate and does not measure it directly.[^c3]

The cost is two greedy forward passes per pair. The map from the pair to (score, prediction) is deterministic, so exchangeability of labeled pairs carries over to the scored tuples. That is what lets the score feed a conformal threshold (see [[conformal-risk-control-selective-judging]]).[^c4]

## What was measured

Baselines were max softmax probability, verbalized confidence, Swap-and-Aggregate (both orders, discrete agreement as confidence) and simulated annotators. Judges were Qwen-2.5 at 7B, 14B and 32B and Llama-3.1-70B, on MT-Bench, RewardBench and Chatbot Arena. BPE and Swap-and-Aggregate share a prediction rule, so their accuracy is identical and only the confidence signal differs. Within that pair BPE improved ECE, AUROC and AUPRC in every model-dataset cell.[^c5] The authors read this as probability-level averaging carrying more information than collapsing each pass to a vote.

## Limits

- It handles order effects only. Length, self-preference and familiarity biases are not neutralized by swapping, and a judge that is confidently wrong in both orders gets a low score. This is my inference from the construction.
- The baselines that do not swap were run with randomized order, so the comparison partly measures averaging over two passes, not only the entropy transform. Whether entropy beats other monotone transforms of p̄ is not isolated in the text I read.
- Binary preference with ties removed; open-ended or multi-way judgments are not covered.
- Needs token probabilities, so closed judges that expose none are excluded. The evidence is open-weight models only.

## Related

- [[llm-judge-biases]] — the biases BPE addresses, position among them
- [[mcq-answer-position-bias]] — the same order sensitivity in multiple-choice answering
- [[conformal-risk-control-selective-judging]] — the calibration layer that consumes the score
- [[pseudo-ensemble]] — permuting presentation to get several readings from one model
- [[judge-score-self-prediction]] — another way a judge's own signal is turned into a reliability estimate

[^c1]: arxiv-2602-13110 — "gives pfwd = Pθ (y=A | xfwd ) and the reverse pass gives prev = Pθ (y=B | xrev ), since preferring rA corresponds to label A in the"
[^c2]: arxiv-2602-13110 — "Intuitively, a reliable judge should assign a similar preference probability to rA regardless of whether it appears first"
[^c3]: arxiv-2602-13110 — "BPE therefore penalizes position bias through the aggregated preference rather than measuring it directly (Appendix B.1)."
[^c4]: arxiv-2602-13110 — "BPE preserves exchangeability."
[^c5]: arxiv-2602-13110 — "Within this bidirectional pair, BPE strictly improves over S&A on ECE, AUROC, and AUPRC in every model–dataset cell, indicating"
