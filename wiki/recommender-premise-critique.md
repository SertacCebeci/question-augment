---
description: "RPCBench decomposes an LLM recommender's response into detection, localization and handling-strategy scores and finds proactive detection of a faulty premise, not what follows it, is the bottleneck."
aliases: ["RPCBench", "Recommender-Premise Critique", "recommender-premise critique"]
sources: ["chen-2026"]
---
# Recommender-premise critique

> An LLM acting as a recommender is scored on three separable steps — did it
> notice the request's premise cannot be filled from the visible evidence,
> did it locate why, and did it respond well — and across eleven models the
> first step, not the other two, is where the pipeline fails.

## Definition / Mechanism

Chen et al. (2026) build RPCBench: 4,623 evidence-grounded
recommendation requests over five domains (MovieLens-1M, MIND-small, Yelp
and others), each paired with a visible schema of what the system can and
cannot see. A request's premise is corrupted into one of ten fine-grained
failure types grouped into four classes — underspecified (the query needs
information the visible evidence does not supply), inconsistent (it
conflicts with the visible evidence), unsupported (it asks about an
attribute absent from the schema, as in Figure 1's font-size example), or
boundary (it exceeds the system's functional or safety scope). Each response
is scored on three binary/ordinal variables: proactive detection $D \in
\{0,1\}$, localization quality $L \in \{0,1,2\}$ once detected, and
handling-strategy quality $S \in \{0,1,2\}$. Proactive Detection Rate (PDR)
is the full-sample rate of $D=1$; the composite metric folds localization
and strategy, conditional on detection, into $D$'s harmonic mean:
$\mathrm{CPCC}_m = \mathrm{PDR}_m \cdot \frac{2\cdot \mathrm{CLA}_m \cdot
\mathrm{CSQ}_m}{\mathrm{CLA}_m+\mathrm{CSQ}_m}$.[^c1]

Across eleven general-purpose LLMs (GPT-5.5, Claude-Sonnet-4-6,
Gemini-3.1-Pro-Preview, the DeepSeek-V4 and Qwen3.5 families, two Llama-3.1
sizes), average PDR is 0.5151 and average CPCC only 0.4376, while average
conditional localization (CLA 0.8415) and strategy quality (CSQ 0.7926) are
much higher — the paper's reading: once a flaw is caught, diagnosing and
acting on it are comparatively solved; catching it is not.[^c2]

The underspecified class is the hardest by a wide margin: mean CPCC 0.0595
and mean PDR only 0.1001 against a run-wide PDR average of 0.5151, meaning
models mostly fail before the localization or strategy steps are even
reached.[^c3]

A clean-query control (400 stratified pairs) rules out models simply
flagging everything: the false-positive rate on clean queries is 0.55%
against a matched corrupted-query PDR of 49.45%, so the low detection rate
on corrupted queries is a genuine miss, not noise from an over-eager
critic.[^c4]

## Why it matters

The three-way split (detect / localize / handle) isolates *which* step
in "should this request be answered as asked" fails, rather than reporting
one end-to-end accuracy number. For an agent deciding whether to ask a
clarifying question before recommending, this says the leverage is in
noticing the request cannot be filled from what is visible — not in what
to do once it notices, which current models already do fairly well.

## Limits

- All scoring (D, L, S, strategy type, evidence faithfulness) is by three
  LLM judges with deterministic aggregation; inter-judge Fleiss' κ is
  reported at a macro-average of 0.7583 and a 500-response human check
  agrees with the aggregated judges 82.60% of the time — solid but not
  perfect, and the CPCC numbers this note cites inherit that judge noise.
- The benchmark is recommendation-specific: premise failures are injected
  against a fixed *visible schema* (what the recommender is told it can and
  cannot see), which has no general analogue outside structured-catalogue
  domains — the underspecified/inconsistent/unsupported/boundary taxonomy
  may not transfer to open-domain question answering unchanged.
- `[?]` This is a September 2026 arXiv preprint (arXiv:2609.00918), not yet
  confirmed at a peer-reviewed venue.
- The eleven models tested are general-purpose LLMs prompted into a
  recommender role, not systems trained or fine-tuned for recommendation;
  whether purpose-built recommender agents show the same detection gap is
  not measured here.

## Related

[[false-premise-question]] · [[clarification-benchmarks]] · [[abstention]] · [[sycophantic-capitulation]]

[^c1]: chen-2026 — "we introduce RPCBench, a benchmark for evaluating Recommender-Premise Critique: the ability to detect, diagnose, and properly handle faulty premises in natural-language recommendation requests. RPCBench contains evidence-grounded test instances from five recommendation domains and covers ten types of premise failures."
[^c2]: chen-2026 — "In the 11 evaluated models, the average PDR (premise detection rate) is 0.5151, while the average CPCC (composite premise critique capability) is only 0.4376."
[^c3]: chen-2026 — "The underspecification group U is the hardest category, with a mean CPCC of 0.0595 and a mean PDR of only 0.1001."
[^c4]: chen-2026 — "The clean-query false-positive rate is only 0.55%, while matched corrupted-query PDR is 49.45%"
