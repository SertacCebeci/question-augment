---
description: "A model answers first, then reasons, then answers again; the first answer's token confidence at test time decides whether the reasoning is generated at all."
aliases: ["think once, answer twice", "answer-think-answer early exit", "VideoAuto-R1 routing"]
sources: ["arxiv-2601-05175"]
---
# Answer-first confidence-gated reasoning

Instead of training a model to choose between thinking and not thinking, the model is trained to always emit a short initial answer, then a reasoning block, then a reviewed answer. Whether the reasoning is kept is decided later, at inference, by how confident the initial answer was.[^c1]

## Mechanism

**Template.** The output is `\boxed{a1}<think>r</think>\boxed{a2}`, with exactly two boxed answers and one think block.[^c2] The authors say this decouples "when to think" (a test-time rule) from "how to think" (learned by RL).[^c3]

**Training reward.** Reward is w1 Rtask(a1) + w2 Rtask(a2) + a format term + a fallback term, with w2 > w1.[^c4] The heavier second weight penalises a correct first answer overwritten by a wrong second one. Asymmetric weights such as 0.9:1.1 or 0.8:1.2 beat 1:1 on several benchmarks.[^c5]

**Fallback string.** When a problem cannot be answered without reasoning, the model writes "Let's analyze the problem step by step" in the first box. A bonus is paid when it does this and a2 is correct, which discourages low-confidence guesses and rewards deferral followed by accurate reasoning.[^c6]

**Gate.** Decoding stops at the end of the first box. The score is the mean log-probability of the answer tokens; if it is at least log tau the answer is accepted, otherwise generation continues. A fallback string gets minus infinity, forcing continuation.[^c7] The first answer is under ten tokens, so the check is cheap. Tau was 0.97, tuned on a small held-out set.[^c8]

## What was measured

- On perception benchmarks (MVBench, MMVU) mean first-answer confidence exceeded 0.93, about 25% of samples went on to think, and reasoning added little. On the reasoning-heavy VideoMMMU confidence fell to about 0.87, the think ratio rose to 51%, and accuracy gained about 4%.[^c9]
- Recall of the thinking route on samples where a1 was wrong but a2 right was consistently high, so most think-needed cases were routed to reasoning.[^c10]
- Adding the fallback reward improved reasoning benchmarks.[^c11]

## Limits

- The evidence is on video question answering with short verifiable answers; the paper does not test open-ended answers, where there is no brief box to score.
- Confidence is the model's own token probability with a fixed threshold; no guarantee on error rate is given (contrast [[dual-threshold-risk-controlled-early-exit]]). The claim that confidence tracks need is supported by averaged benchmark-level correlations and a recall figure, not by a calibration analysis I read.
- The fallback relies on the model learning to refuse; how often it over-defers was not something I checked.

## Related

- [[dual-threshold-risk-controlled-early-exit]] — also stops on confidence, but calibrates the threshold to a stated error rate
- [[moderate-adaptive-reasoning-length]] — adaptive reasoning length as the shared goal
- [[selective-abstraction]] — the fallback string is a deferral, not an abstention from answering
- [[deep-thinking-ratio]] — another measure of how much a model reasons

[^c1]: arxiv-2601-05175 — "During inference, the model uses the confidence score of the initial answer to determine whether"
[^c2]: arxiv-2601-05175 — "We enforce exactly two \\boxed{...}"
[^c3]: arxiv-2601-05175 — "This template decouples when to think, handled at test time by our early-exit"
[^c4]: arxiv-2601-05175 — "R = w1 Rtask (a1 ) + w2 Rtask (a2 ) + λ Rfmt + α Rfallback"
[^c5]: arxiv-2601-05175 — "asymmetric weights such as 0.9 : 1.1 or 0.8 : 1.2 outperform the uniform 1 : 1 setting across multiple benchmarks."
[^c6]: arxiv-2601-05175 — "rewards honest deferral followed by accurate reasoning."
[^c7]: arxiv-2601-05175 — "we set s(a1 ) = −∞, forcing continuation of the CoT and final answer generation."
[^c8]: arxiv-2601-05175 — "The early-exit confidence threshold τ is set to 0.97"
[^c9]: arxiv-2601-05175 — "average confidence drops to approximately 0.87, the think ratio increases to 51%"
[^c10]: arxiv-2601-05175 — "The resulting recall is consistently"
[^c11]: arxiv-2601-05175 — "adding the fallback reward α consistently improves performance on"
