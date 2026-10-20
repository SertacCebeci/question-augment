---
description: "Metric scoring whether a multi-party LLM agent sends a targeted question to the correct expert; the lowest of four coordination dimensions, mostly failing by never asking."
aliases: ["IA", "Inquiry Alignment"]
sources: ["ys-2026"]
---
# Inquiry Alignment

> A benchmark metric for whether an LLM agent, facing a goal it cannot complete from its own private knowledge, asks a targeted question of the correct other agent through the right channel — and, across six frontier models, the dimension every model fails hardest.

## Definition / Mechanism

Inquiry Alignment (IA) is one of four dimensions in the SOTOPIA-ToM benchmark, which places 3–5 LLM agents in a multi-party scenario with partitioned private knowledge, a shared knowledge-domain map naming which role holds which kind of fact, and per-agent sharing/withholding policies. IA scores whether an agent "actively acquire[s] missing information by directing targeted requests to the appropriate expert (as specified by the knowledge domain map) using a channel consistent with the information's sensitivity. Only deliberate inquiries are counted, passive receipt is not."[^c1]

Across six models (GPT-4o, GPT-5-nano, GPT-5 high, Llama-4-Maverick, Qwen3-235B, DeepSeek-R1) and four prompting conditions (baseline, CoT-Privacy, ToM-Coach, ToM-Belief), IA is "consistently the lowest-scoring dimension (0.13–0.32), substantially below disclosure alignment (DA, 0.44–0.78) and efficiency (EFF, 0.16–0.99). Even GPT-5, which achieves near-perfect efficiency (EFF ≥ 0.93) and strong disclosure (DA ≥ 0.75), peaks at only IA = 0.29."[^c2]

A failure-mode breakdown attributes the gap to a behavioral deficit rather than a targeting error: "79.8% of failed inquiry items correspond to agents never asking at all, not routing errors (10.3% wrong person) or channel mistakes (9.9% wrong channel)."[^c3]

## Why it matters

IA isolates the asking side of multi-agent coordination — the decision to convert an unfilled information need into a directed question — from disclosure (whether an agent volunteers what it already holds) and from privacy avoidance (whether it withholds what it must). Because disclosure is scored against an explicit list of what to share while inquiry requires inferring "what to ask, whom to ask, and which channel to use from a high-level objective alone"[^c1], the paper's own reading is that this asymmetry — an explicit target for telling versus an inferred target for asking — is why asking underperforms telling in these agents.[^c4]

## Transfer

| | Home field (multi-agent LLM evaluation) | Here (asking, stall 2) |
|---|---|---|
| Formalism | A judge-LLM-scored dimension (0–1) counting deliberate, correctly-routed requests | The same score used as an empirical proxy for "does the agent select the axis it lacks information on and act on that selection" |
| What survives | The behavioral distinction between failing to ask and asking the wrong party or channel | The same distinction: a low asking rate is a selection failure upstream of formulation or source choice |
| What does not | Any claim about *which* axis an agent should ask about first, or an information-theoretic value of the question asked | IA does not rank candidate questions by [[expected-information-gain|expected information gain]]; it only checks whether *a* targeted question was sent to *the* specified expert |

## Limits

The claim rests on scenarios generated and judged by GPT-5.2 (with human review of the generated scenarios but not of every judge call), so the 0.13–0.32 IA range and the 79.8% figure are specific to this benchmark's scenario distribution, its round-robin, four-round simulation cap, and this LLM-as-judge scoring pipeline (95.8% inter-annotator agreement, 94.7% judge accuracy against 30 held-out transcripts) rather than a general measurement of asking behavior outside multi-agent role-play. [ys-2026]

## Related
[[value-of-information]] · [[expected-information-gain]] · [[clarification-benchmarks]]

[^c1]: ys-2026
[^c2]: ys-2026 — "IA is consistently the lowest-scoring dimension (0.13–0.32), substantially below disclosure alignment (DA, 0.44–0.78) and efficiency (EFF, 0.16–0.99). Even GPT-5, which achieves near-perfect efficiency (EFF ≥ 0.93) and strong disclosure (DA ≥ 0.75), peaks at only IA = 0.29."
[^c3]: ys-2026 — "79.8% of failed inquiry items correspond to agents never asking at all, not routing errors (10.3% wrong person) or channel mistakes (9.9% wrong channel)."
[^c4]: ys-2026
