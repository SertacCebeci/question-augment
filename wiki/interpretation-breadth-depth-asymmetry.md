---
description: "Human answerers commit to few readings of a question and cover them thoroughly; LLM answerers spread thinly over many readings, including ones few humans address."
aliases: ["breadth over depth hedging", "over-answering", "interpretation overaddressing"]
sources: ["arxiv-2604-15140"]
---
# Interpretation breadth-depth asymmetry

> Given the same fan of possible readings, humans pick a few and answer them
> exhaustively; LLMs, left to a default prompt, try to answer all of them a
> little.

## Definition / Mechanism

**The measurement ([[interpretation-space]], [[arxiv-2604-15140|Srikanth,
Boyd-Graber & Rudinger (2026)]]).** For each question's interpretation space
$S_I$ and each interpretation $i \in S_I$, the proportion of human answers
that address $i$ is computed, interpretations are binned by that human
frequency, and the average probability that an LLM answer (haiku-4.5,
qwen3-32b, both with default prompting) addresses $i$ is plotted per bin.
Agreement with human preference is the diagonal; placement above it is
**over-answering** — addressing interpretations humans rarely choose to.[^c1]

**The finding.** With default prompting, both LLMs systematically
over-answer: for interpretations fewer than 10% of humans address, haiku
addresses them over 20% of the time and qwen over 40%. Prompting
claude-sonnet-4.5 to mimic a specific human community's answering style does
not correct this and can worsen it. Measured directly as the mean/median
share of an answer's eligible segments spent on a single interpretation
(Table 1 of the source), humans dedicate more segments per interpretation
than any tested LLM configuration (default or mimic) — i.e. humans favor
**depth** (fewer interpretations, each addressed more exhaustively) where
LLMs favor **breadth** (more interpretations, each addressed thinly). The
pattern holds across communities with distinct rhetorical norms, and LLM
answers are also systematically longer — the extra length is attributed to
addressing interpretations the asker likely did not intend rather than to
elaborating on the one(s) they did.[^c2]

## Why it matters

This separates two failure modes that "hedging" usually collapses into one:
an answerer can hedge *within* a reading (qualify its confidence) or hedge
*across* readings (address several at once instead of committing to the
asker's likely one). The asymmetry is measured at the second, structural
level — how many of the question's possible readings an answer touches —
independent of anything the answer says about its own certainty, and it
persists even when the model is told which community's norms to imitate,
suggesting the shortfall is in reading the question's intended partition,
not in surface style.

## Limits

The source's own reading: this is one candidate explanation (a "core feature
of human pragmatic reasoning") among others the paper does not rule out —
e.g. an incentive difference (human answerers pay a cost per word or per
reply that LLMs, prompted to be maximally helpful, do not) could produce the
same breadth/depth split without any difference in how well the intended
reading is identified. Tested on two LLMs (haiku-4.5, qwen3-32b) plus one
mimicking model (claude-sonnet-4.5) on English Reddit questions from nine
communities; generalization to other models, prompting strategies beyond
"default" and "mimic," or non-Reddit answering settings is unverified.

## Related

- [[interpretation-space]]
- [[false-premise-question]]
- [[levels-of-information-need]]
- [[hedged-mirage]]

[^c1]: arxiv-2604-15140 — "even when fewer than 10% of humans address i, haiku addresses it over 20% of the time and qwen 40%"
[^c2]: arxiv-2604-15140 — "humans favor depth over breadth (Table 1), opting to address fewer interpretations more exhaustively"
