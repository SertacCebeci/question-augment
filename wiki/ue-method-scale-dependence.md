---
description: "Across 9 models and 22 languages, the best uncertainty-estimation method for flagging an LLM's wrong answers switches with model scale, from token-probability to self-verbalized confidence."
aliases: ["scale-dependent UE method selection"]
sources: ["alfarano-2026"]
---
# UE method scale-dependence

> The uncertainty-estimation (UE) method that best predicts an LLM's error is
> not fixed: an open-box method built from token probabilities wins at small
> scale, and a closed-box method built from the model's own stated confidence
> overtakes it as scale grows.

## Definition / Mechanism

Alfarano, Bacciu & Mansour (2026) compare the top-2
open-box methods (Token [[entropy|Entropy]], Self Certainty) against the top-2
closed-box methods (Self Verbalized, Lexical Similarity) — the four that
scale best across all languages — over the Qwen3 family from 4B to 235B
parameters, averaged across 22 languages. They evaluate "the top-2 open-box
(Token Entropy, Self Certainty) and top-2 closed-box (Self Verbalized,
Lexical Sim.) methods (selected for figure clarity) that scale best across
all languages".[^c1]

Token Entropy changes only modestly across scale. Self Verbalized rises
"substantially with scale (from 0.65→0.66→0.77 AUROC)", and at 30B "Token
Entropy significantly outperforms Self Verbalized (19 of 22 languages at
30B, paired DeLong tests; Appendix L), but this relationship reverses at
235B where Self Verbalized achieves the highest AUROC among all methods."[^c2]

The paper's own practical reading: "at smaller scales, open-box methods such
as Token Entropy provide the most reliable uncertainty signal; at larger
scales, Self Verbalized surpasses all alternatives by a significant
margin".[^c3]

## Why it matters

On stall 2 — and on any stopping or commitment decision that reads a
confidence score off the model — a UE pipeline fixed once and reused across
deployments of different scale silently picks the losing method at one end
of the range: the choice of UE method is a hyperparameter of *deployment
scale*, not a one-time pick.

## Limits

- Established on one model family (Qwen3, 4B–235B) swept for scale, with
  Gemma3-27B and Claude Sonnet 4.5 as separate large-scale points, not a
  second full sweep; whether the crossover generalizes to other model
  families is not tested here.[^c4]
- Limited to four of the nine methods the paper evaluates (two open-box, two
  closed-box, selected because they scale best); the other five methods'
  scale behaviour is reported only in an appendix this note does not draw
  on.
- The only metric is AUROC for error detection; scale-dependence under
  [[calibration]] error or other UE metrics is not established here.

## Related

[[abstention]] · [[semantic-entropy]]

[^c1]: alfarano-2026 — "we evaluate the top-2 open-box (Token Entropy, Self Certainty) and top-2 closed-box (Self Verbalized, Lexical Sim.) methods (selected for figure clarity) that scale best across all languages"
[^c2]: alfarano-2026 — "Self Verbalized, by contrast, improves substantially with scale (from 0.65→0.66→0.77"
[^c3]: alfarano-2026 — "open-box methods such as Token Entropy provide the most reliable uncertainty signal; at larger scales, Self Verbalized surpasses all alternatives by a significant margin"
[^c4]: alfarano-2026
