---
description: "A parameter-free two-pass prompting technique that abstains when adding an \"I don't know\" option changes a model's MCQA answer, the largest composite-risk drop of tested baselines."
aliases: ["Second Guess", "answer stability", "answer-switching abstention"]
sources: ["aravindan-2026", "kadavath-2022"]
---
# Answer-stability abstention

> Ask the same multiple-choice question twice — once with the normal
> options, once with an "I don't know" option added — and treat a changed
> answer as the abstention signal. No weights, no sampling, no self-report:
> the model's own instability is the score.

## Definition / Mechanism

Aravindan & Kejriwal (2026) propose **Second Guess**: the
model answers a question $Q$ with choices $C=\{c_1,c_2,c_3,c_4\}$, giving
response $R_1$; the same question is asked again with "I don't know"
inserted at a random position as a fifth option, giving $R_2$. If
$R_1=R_2$ the original answer is kept; if $R_1\neq R_2$ — regardless of
what it changed to — the final output is forced to "I don't know."
"If the model's answer remains consistent between stages (R1 = R2), the
original answer choice is retained. Conversely, if the response changes
(R1 ≠ R2), regardless of what it changed to, the model's output is
classified as an abstention response 'I don't know'."[^c1]

Evaluated on four instruction-tuned models (2B–8B parameters: Mistral-7B,
Llama-3.1-8B, Granite-3.3-2B, Qwen3-4B) on four MCQA benchmarks
(CommonsenseQA, QASC, MMLU-Pro, SuperGPQA), against three baselines —
augmented-prompt-only, self-evaluation ([[kadavath-2022|Kadavath et al.
2022]]), and [[entropy]] thresholding (mean + 1 SD of token entropy) — Second
Guess gives the largest drop in **composite risk** (incorrect answers plus
wrongly-abstained correct answers, defined by Shen & Kejriwal 2025):
"Second Guess improves performance across all metrics, achieving
particularly strong gains in Composite Risk with a 10.81% drop, while
using only 2 model queries, just as much as Self-Evaluation." The next
best baseline (self-evaluation) reached a 7.69% drop; entropy thresholding
3–6%.[^c2]

On LoRA-finetuned Qwen and Llama, Second Guess kept an 8% composite-risk
improvement while entropy thresholding lost most of its effect: "Entropy
Thresholding loses out on finetuned models since with finetuning, the
confidence of the models on that dataset increases and token entropy is no
longer very informative on the models' uncertainty."[^c3]

The improvement is inversely related to the model's base accuracy on the
task — "The fitted line (y = −0.47x + 38.97) demonstrates that for every 1%
increase in base accuracy, the expected composite risk reduction decreases
by approximately 0.47 percentage points" — with the weakest model/dataset
pairs (e.g. Llama on SuperGPQA, ≈32% base accuracy) seeing composite-risk
reductions exceeding 25%, and a strong pair (Qwen on CommonsenseQA, ≈85%)
seeing none.[^c4]

Most of the gain is not the model choosing "I don't know" directly: "The
models rarely select[] the 'I don't know' option and instead tend[] to
switch between wrong answers. For example, the Qwen model on MMLU Pro,
switches only 2 of its incorrect answers in the Original Prompt to 'I
don't know' in the Augmented Prompt, while switching 21 of those to some
other choices in the latter prompt, showing that most of the error rate
reduction came from capturing this option switching behaviour rather than
explicit abstention by the model."[^c5]

## Known as

| Field | Name there | Relation |
|---|---|---|
| LLM uncertainty estimation (Aravindan & Kejriwal 2026) | Second Guess | exact — the paper's own name for the technique |
| LLM uncertainty estimation (Aravindan & Kejriwal 2026) | answer stability / behavioral stability | exact — the paper's descriptive term for the underlying signal |

[^c6]

## Why it matters

This gives [[abstention]]'s selection function $g$ a concrete,
zero-access-required instantiation: instead of thresholding a score
(entropy, a self-reported probability), $g$ is computed from whether the
answer itself is stable under a perturbation of the option set — two
forward passes, no logits, no held-out [[calibration]] set, usable on
black-box small models. Finding 4 above changes what the mechanism should
be credited with: the gain is mostly a second chance to pick a different
wrong answer being caught, not the model volunteering "I don't know" — the
signal exploited is answer-switching under perturbation, not a willingness
to abstain.

## Limits

- Evaluated only on models under 10B parameters; the inverse relationship
  between base accuracy and the improvement means the paper does not know
  whether the effect holds for frontier-scale models.
- No chain-of-thought: "this study evaluates models without
  Chain-of-Thought (CoT) reasoning... the absence of CoT likely
  underestimates the baseline capabilities of evaluated models."[^c7]
- Composite risk is a metric defined in a companion paper (Shen &
  Kejriwal 2025, not read here) — the 10.81% figure is not directly
  comparable to a plain accuracy or coverage number without that
  definition in hand.
- One run per model–dataset pair reported in the main results table; no
  independent replication.

## Related

[[abstention]] · [[chain-entropy-abstention-gate]] · kadavath-2022 · [[semantic-entropy]]

[^c1]: aravindan-2026
[^c2]: aravindan-2026 — "Second Guess improves performance across all metrics, achieving particularly strong gains in Composite Risk with a 10.81% drop, while using only 2 model queries, just as much as Self-Evaluation."
[^c3]: aravindan-2026
[^c4]: aravindan-2026 — "The fitted line (y = −0.47x + 38.97) demonstrates that for every 1% increase in base accuracy, the expected composite risk reduction decreases by approximately 0.47 percentage points."
[^c5]: aravindan-2026
[^c6]: aravindan-2026
[^c7]: aravindan-2026
