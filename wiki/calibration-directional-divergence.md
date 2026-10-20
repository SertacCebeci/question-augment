---
description: "Shared calibration rules reduce LLM-judge noise but not directional disagreement: three judges given identical rules moved toward parity, sharpened preference, or stayed entrenched."
aliases: []
sources: ["arxiv-2604-24158"]
---
# Calibration directional divergence

> Give three judges the same rulebook and they do not converge — they
> each become more themselves.

## Definition / Mechanism

Three LLM judges (GPT-5, Gemini-2.5-Pro, DeepSeek-v3) scored the same
pairwise city-trip comparisons before and after being given an identical
set of eight calibration rules plus few-shot examples, derived from
[[two-point-disagreement-threshold|two-point disagreements]] with human
experts, in Banerjee et al. (2026). Each judge's
directional preference between the two compared lists was tracked with a
confidence-weighted aggregated-score ratio (ASR) before and after
calibration. The three judges did not move the same way: "Pre-calibration,
Gemini skewed slightly against 𝐿1. Calibration shifts its ASR significantly
toward equilibrium (0.71 → 0.98)" — noise reduction that reads as
correction toward parity. DeepSeek moved the opposite direction on the same
rules: "DeepSeek amplifies its initial preference for 𝐿1 (1.30 → 2.88)... By
removing ambiguity, calibration makes the model more decisive in its
specific interpretation of the rules... leading to polarization
('sharpening') rather than consensus." GPT-5 barely moved at all: "GPT
shows minimal movement (0.58 → 0.64), suggesting its evaluation heuristics
are deeply entrenched and less sensitive to few-shot prompts." The paper
names the overall pattern directly: calibration acts "as a 'clarifier'
rather than a universal corrector: it reduces noise while revealing how
models interpret rules."[^c4]

## Why it matters

A calibration step is usually judged by whether it moves multiple judges
toward agreement. This result separates two things a shared rulebook can
do that look identical from the outside — reduce a judge's internal
inconsistency (noise) — and shows that reducing noise does not imply
convergence between judges: the same rules sharpen one judge's prior bias
and only shift a different judge toward parity. A practitioner comparing
judges' post-calibration scores must therefore check the *direction* of
each judge's shift, not just whether its variance dropped, before treating
the calibrated panel as more trustworthy than the uncalibrated one.

## Limits

Three judges, one task (paired city-trip recommendation, four
dimensions), one calibration rule set — the paper does not test whether
the three-way split (parity / sharpening / entrenchment) is a property of
these specific models or a general property of rule-based LLM-judge
calibration. It also reports no statistical test on the ASR shifts
themselves (unlike the alignment deltas in Table 2), so the size of each
judge's directional move is not itself certified against chance.[^c4]

## Related

- [[two-point-disagreement-threshold]]
- [[calibration]]
- [[effective-independent-votes]]
- [[rubric-complexity-normalized-reward]]

[^c4]: arxiv-2604-24158 — "Calibration stabilizes reasoning and harmonizes heuristics, acting as a “clarifier” rather than a universal corrector: it reduces noise while revealing how models interpret rules"
