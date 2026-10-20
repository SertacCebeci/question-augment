---
description: "Reasoning traces that converge on an answer raise its token probability whether or not it is right, so answer-token confidence inflates and loses ranking power; sample agreement does not."
aliases: ["confidence inflation under chain-of-thought", "correctness-agnostic confidence inflation", "answer-token likelihood inflation"]
sources: ["arxiv-2603-16728"]
---
# Implicit answer conditioning

Welch et al. (2026) study uncertainty estimates for vision-language models with and without chain-of-thought (CoT). Their mechanism: as a reasoning trace progresses it commits to a conclusion, which raises the conditional probability of the final answer tokens before they are generated. At the token level this predictability looks the same as genuine confidence, so answer-token likelihood (ATL) measures such as maximum sequence probability, perplexity and mean token entropy reflect commitment to the model's own trace rather than doubt about correctness.[^c1]

## What was measured

Define the reasoning-induced shift as the ATL score with the trace minus the score without it. The signature of the effect is that this shift is about the same for correct and for incorrect predictions, so the added confidence cannot separate them.[^c2] Reported consequences: ATL-based estimates systematically rise under CoT, including on samples that stay or become wrong, while self-reported confidence and sampled consistency show no systematic inflation.[^c3]

Three tests support the account:

- Length is not the cause. Reasoning length correlates negatively with confidence (longer traces, lower confidence), the opposite of what inflation by length would need.[^c4]
- Answer repetition tracks confidence. On open-ended OK-VQA, the number of times the final answer is mentioned in the trace correlates positively with ATL confidence, and the correlation persists among incorrect predictions only. Consistency and self-reported confidence show near-zero correlation.[^c5]
- Masking answer mentions restores ranking. Replacing every occurrence of the predicted answer in the trace with [MASK], with the answer itself unchanged (so accuracy is identical by construction), more than triples the Prediction Rejection Ratio of the maximum-probability score (0.141 to 0.475). Random masking of equally many tokens changes it only moderately. The no-CoT baseline (0.498) is not fully recovered, so conditioning persists beyond explicit mentions.[^c6]

Calibration moves the same way: reasoning worsened the calibration of maximum probability in most settings (one model on MathVista went from 0.047 to 0.200 ECE), while it improved the calibration of consistency in all sixteen model-dataset pairs with a baseline.[^c7] The paper's practical reading is that agreement across sampled answers is the estimate to prefer in reasoning-enabled models, at the cost of multiple generations.[^c8]

For asking and answering: a confidence read off the answer tokens after a long argument for that answer largely measures the argument. A question asker who wants a trustworthy confidence should take it from something the trace could not have pre-committed, such as agreement among independent answers.

## Limits

- Evidence is for vision-language models on multiple-choice and short-answer benchmarks; the mechanism is not shown for text-only models or free-form generation.
- The conditioning claim is partly inference: answer frequency is a proxy that captures only the most explicit form, and the masking intervention was done only on the OK-VQA subset where the answer appears in the trace (n = 3,900). On MathVista random masking itself hurt ranking, so the control is weaker there.[^c6]
- Consistency needs several generations; its cost is acknowledged by the authors.
- Ranking metrics are the primary criterion; ECE is reported only for bounded measures.

## Related

- [[reasoning-contamination-of-verbalized-confidence]] — another route by which reasoning in the same generation corrupts confidence, for stated rather than token confidence
- [[top-skewed-confidence-floor]] — overconfident clustering of confidence scores
- [[confidently-wrong-low-entropy-regime]] — wrong answers carried with low entropy
- [[vote-margin-gate]] — agreement among samples used as a decision signal
- [[calibration]] — the property that degrades

[^c1]: arxiv-2603-16728 — "elevated answer-token probabilities reflect commitment to the model’s own reasoning trace rather than reduced uncertainty about correctness."
[^c2]: arxiv-2603-16728 — "the model becomes more confident in its predicted answer whether or not that answer is correct"
[^c3]: arxiv-2603-16728 — "ATL-based estimates systematically increase confidence, including samples that become or remain incorrect"
[^c4]: arxiv-2603-16728 — "reasoning length exhibits a negative correlation with all UQ estimates: longer traces correspond to lower confidence."
[^c5]: arxiv-2603-16728 — "This correlation persists even for incorrect predictions, indicating correctness-agnostic confidence inflation."
[^c6]: arxiv-2603-16728 — "MSP PRR more than triples (0.141 → 0.475)"
[^c7]: arxiv-2603-16728 — "across all sixteen model–dataset pairs for which a non-reasoning baseline is available, reasoning improves the calibration of consistency."
[^c8]: arxiv-2603-16728 — "The robustness of consistency comes at a computational cost"
