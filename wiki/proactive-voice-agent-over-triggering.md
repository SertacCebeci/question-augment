---
description: "A four-task multimodal voice-agent benchmark finds models over-trigger on ambient silence and, by ablating digital context, shows grounded-trigger recall depends on that context, not audio alone."
aliases: ["ProVoice-Bench", "over-triggering propensity", "decision-to-speak / task-execution gap"]
sources: ["arxiv-2604-15037"]
---
# Proactive voice-agent over-triggering

> Silence is the default a proactive agent must earn the right to break;
> current multimodal models break it too often, and separately, do not
> know what to do once they have.

## Definition / Mechanism

Xu, Wang & Wang (2026) build ProVoice-Bench, "the
first evaluation framework specifically designed to assess proactivity in
voice agents," comprising "1,182 meticulously curated samples across four
novel proactive tasks." Each sample is a quintuple grounded in both
conversational audio and a synthesized mobile "digital context" (calendar,
messages, app state), and the four tasks isolate four distinct trigger
kinds an agent must detect *before* it decides whether to interrupt:
implicit linguistic intent requiring a tool call, a user-defined semantic
topic surfacing later in someone else's speech, a user-defined acoustic
event, and a spoken statement that contradicts the digital context. The
benchmark scores each sample twice: an interaction-decision layer
(Accuracy, Recall, and — the metric that isolates over-triggering — False
Positive Rate, the fraction of unnecessary interventions on trials with no
valid trigger) and, conditional on that decision being correct, a
Response Accuracy that jointly LLM-judges the predicted tool call and
text response against ground truth.

Across seven evaluated MLLMs, the decision layer shows a specific,
repeatable failure: "a widespread tendency toward over-triggering...
particularly evident in LTM tasks, where most models tend to respond
regardless of whether actual trigger points exist in the conversation.
Similarly, in CFC tasks, models frequently fail to recognize when a
conversation proceeds without any violation of the digital context."[^c2]
This is a directional bias toward acting, measured by FPR specifically,
recurring across two unrelated trigger kinds (silence-monitoring and
fact-checking).

A second, separately measured gap sits above the decision layer: "a
fundamental gap between 'knowing when to speak' and 'knowing what to do.'
Current models frequently suffer from semantic drift during interactions
or generate hallucinated tool calls." Correct trigger detection does
not transfer to a correct tool call or response.

The paper isolates *why* context-dependent recall fails with a causal
probe: removing the digital context input and re-running the benchmark,
"the absence of digital context leads to a
substantial decline in Recall for the CFC task, which relies on such
information to determine interaction timing. Similarly, this removal
results in decreased Accuracy and Recall in PIC tasks, where digital
context is essential for accurately inferring users' implicit
intentions." Recall on these tasks is grounding-dependent, not an
audio-processing limitation, shown by subtraction rather than inference
from the main table alone.

## Why it matters

Existing benchmark decompositions of proactive initiative
([[act-silent-stop-decomposition]] on mobile GUI agents,
[[local-ask-correctness-e2e-gap]] on structural-engineering workflows)
each split "should the agent act" from a downstream outcome. ProVoice-Bench
adds two things neither does: it names the specific *direction* of the
decision failure — FPR-driven over-triggering, not a symmetric
act/silent confusion — and it supplies an ablation, not just a
correlation, tying one input (digital context) to one failure mode
(context-dependent recall) independent of the over-triggering bias. A
system builder deciding where to spend budget on a proactive assistant
now has two separable levers: suppressing false triggers (a
decision-threshold problem) and grounding trigger detection in structured
context rather than raw audio (a retrieval/input problem) — conflating
them, as an aggregate accuracy score would, hides that the second lever
does nothing for the first.

## Limits

- All 1,182 samples are synthesized (LLM-scripted scenes, TTS speech,
  simulated acoustics); no human-recorded proactive-interaction data is
  used, so the measured over-triggering rate is a property of this
  synthetic distribution, not a validated human-interaction base rate.
- Seven MLLMs, all in the 7B–33B range; no frontier closed model is
  evaluated, and the paper does not test whether over-triggering
  attenuates with scale.
- Response Accuracy is gated by a correct trigger decision
  (`I(pred=gt)`), so the "decision-to-execution gap" is read off two
  jointly-scored numbers rather than an independent execution-only test;
  a model that never over-triggers could still show a large gap for
  reasons the metric does not separate from noise.
- The digital-context ablation is reported only for CFC and PIC, on
  Recall/Accuracy; no equivalent causal probe isolates the source of the
  LTM/CFC over-triggering bias itself.

## Related

[[act-silent-stop-decomposition]] · [[local-ask-correctness-e2e-gap]] · [[proactivity-taxonomy]] · [[value-of-information]] · [[abstention]]

[^c2]: arxiv-2604-15037 — "The results reveal a widespread tendency toward over-triggering. This is particularly evident in LTM tasks, where most models tend to respond regardless of whether actual trigger points exist in the conversation. Similarly, in CFC tasks, models frequently fail to recognize when a conversation proceeds without any violation of the digital context."
