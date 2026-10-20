---
description: "Across ten LLMs on matched bandit trials, inference-time thinking sharpened value-guided choice and evidence-sensitive confidence but did not raise measured exploration."
aliases: ["thinking-exploration dissociation", "evidence-use vs information-seeking dissociation"]
sources: ["xiong-2026-thinking", "arxiv-2512-01725"]
---
# Thinking-mode exploration dissociation

> Giving ten open-weight LLMs a private thinking trace before a bandit
> choice made them use the evidence they already had better, but it did not
> make them seek more information — a named split between two things "more
> reasoning" is usually assumed to buy together.

## Definition / Mechanism

Ten open-weight models (Gemma 4, GPT-OSS, Nemotron 3, Qwen 3.5/3.6) each ran
600 matched horizon-style two-armed bandit trials (Wilson et al. 2014
protocol) in thinking and non-thinking modes, fitted with the
[[exploration-signature-decomposition]]: "On average, thinking strengthened
value-guided action and reduced uncertainty-independent choice noise,
without producing UCB-like exploration or strengthening Thompson-like
exploration."[^c1]

Across the nine models comparable across modes, "the mean changes were
Δγ = 1.38, Δη = −0.22, and Δλ = −2.21 in value-equivalent units... The
positive Δγ moved mean γ from −1.45 to −0.07, not above zero; mean η
decreased from 0.26 to 0.04, and mean λ from 4.01 to 1.79."[^c2]

Reported confidence also became better calibrated to the evidence actually
in hand rather than more exploration-seeking: "the mean within-model
Spearman correlation between reported confidence and chosen task evidence
increased from 0.16 without thinking to 0.43 with thinking."[^c3]

The dissociation was not an artifact of how the thinking trace was sampled:
sweeping temperature, top-p and top-k during thinking generation changed
choice noise and thinking length but "did not reproduce the broader
non-thinking choice pattern or the joint changes across outputs."[^c4]

## Why it matters

Stall 2 asks which axis to query first, and several of the map's rows
([[thompson-sampling|Thompson sampling]], UCB-style scoring, [[information-directed-sampling|information-directed sampling]])
assume an agent that trades exploitation for exploration as it reasons
more. This result is a direct, measured counter-case for one family of
agents under one controlled task: giving a language model more
inference-time computation strengthened its use of *already-available*
evidence and its confidence [[calibration]], but supplied no matching increase
in the two standard information-seeking signatures. An asking pipeline that
scales "thinking budget" expecting more active axis-exploration as a side
effect should not assume it from this result.

A measure of a different kind, on a different task, gave a different
answer. When the task is to enumerate every valid answer rather than to
choose among bandit arms, the extended-reasoning paradigm raised the rate at
which models found new correct solutions: "Long-CoT models demonstrate
significantly higher rates of Error Correction and New Solution" discovery.[^c5]
The two results do not conflict on my reading: the bandit study fits choice
signatures, while the enumeration study counts correct answers recovered from
a fixed set. The enumeration comparison is also not a clean test of thinking
alone, since for DeepSeek and GPT the two paradigms are different models:
"DeepSeek-R1 [13], and o4-mini [16]" against DeepSeek-V3 and gpt-4o-mini.[^c6]

## Limits

The claim is narrow on purpose. "Because the non-thinking estimates were
heterogeneous and one model's non-thinking choices did not track value, we
cannot conclude that thinking removed a previously identifiable exploration
strategy" — the source itself withholds the stronger claim that thinking
*suppresses* exploration, only that it did not *add* it. The task is a
two-armed, matched-horizon bandit with a numeric reward and a countable
warm-up history, not open-ended natural-language question selection; ten
open-weight model families were tested, not proprietary frontier models;
and the paper explicitly declines to say the thinking-length and
confidence patterns establish metacognitive control or monitoring as
processes, only that they are consistent with them.

## Related

[[exploration-signature-decomposition]] · [[thompson-sampling]] · [[expected-information-gain]]

- [[reasoning-overconfidence]] — the enumeration setting where a thinking paradigm did raise new-solution discovery
- [[cognitive-rigidity]] — the hypothesis offered for why a short chain stops searching

[^c1]: xiong-2026-thinking — "On average, thinking strengthened value-guided action and reduced uncertaintyindependent choice noise, without producing UCB-like exploration or strengthening Thompson-like exploration."
[^c2]: xiong-2026-thinking — "the mean changes were ∆γ = 1.38, ∆η = −0.22, and ∆λ = −2.21 in value-equivalent units (Fig. 3). The positive ∆γ moved mean γ from −1.45 to −0.07, not above zero; mean η decreased from 0.26 to 0.04, and mean λ from 4.01 to 1.79."
[^c3]: xiong-2026-thinking — "the mean within-model Spearman correlation between reported confidence and chosen task evidence increased from 0.16 without thinking to 0.43 with thinking"
[^c4]: xiong-2026-thinking — "Within the tested ranges, the decoder sweeps did not reproduce the broader non-thinking choice pattern or the joint changes across outputs."
[^c5]: arxiv-2512-01725 — "Long-CoT models demonstrate significantly higher rates of Error Correction and New Solution"
[^c6]: arxiv-2512-01725 — "DeepSeek-R1 [13], and o4-mini [16]"
