---
description: "A closed-loop ASR architecture treating transcription as stateful multi-turn refinement, routing each user turn into confirm/new-input/correct and repairing via Locate-Reason-Modify."
aliases: ["Agentic ASR", "Interactive ASR"]
sources: ["jiang-2026-towards"]
---
# Agentic ASR

> A speech-recognition system stops treating every new utterance as fresh
> input: it classifies the turn as acceptance, new content, or a correction
> of what it already transcribed, and only the last case triggers an
> explicit locate-reason-modify repair of its running hypothesis.

## Definition / Mechanism

**Jiang, Zhu, Wang et al. (2026)** replace single-pass
ASR ($Y = \mathrm{ASR}(I)$) with **Interactive ASR**: a stateful process
conditioned on transcription history, $Y_t = \mathrm{InteractiveASR}(Y_{[:t-1]}, I_t)$,
rather than independent one-shot decoding on each new speech input.[^c1]

Their solution, **Agentic ASR**, is a three-stage closed loop run at every
turn $t$. (1) *Semantic correction* rewrites the raw ASR hypothesis $H_t$
into an explicit, context-consistent instruction $H'_t$, because the user's
own correction utterance is itself ASR output and may be garbled. (2)
*Intent routing* classifies $H'_t$ into one of three types — confirmation
(accept the current state), new input (treat as fresh transcription), or
correction (edit the existing state) — and the state-update rule branches
on that label. (3) For a correction intent, a *Locate-Reason-Modify*
pipeline finds the editable span in the history, infers the intended edit
from the instruction and context, and applies it: $\mathrm{ReasoningCorrector} =
\mathrm{Modify} \circ \mathrm{Reason} \circ \mathrm{Locate}$, rather than an
unconstrained one-step rewrite.[^c2]

Across GigaSpeech, WenetSpeech, ASRU2019 and four other multilingual /
named-entity / code-switching test sets, each additional interaction turn
monotonically lowers the semantic error rate: on GigaSpeech Test it drops
from 21.47% at turn 0 to 12.35% after one correction turn and to 3.49% by
turn 10; on ASRU2019 Test from 28.57% to 10.32% after one turn and 1.36% by
turn 10.[^c3]

## Why it matters

Intent routing is a general schema for interpreting a response inside a
clarification loop: it answers stall 4 (the constraint's source is the
user's *next* turn, not a fresh input) by first deciding what kind of turn
was just received, before deciding what to do with it — the same move the
wiki elsewhere calls out in [[clarification-request]] for a recogniser
confidence scale rather than an LLM classifier. The evaluation harness
built on top of this framework (round-wise S2ER as a per-turn stopping
test, [[sentence-level-semantic-error-rate]]) instantiates stall 7 for a
domain with a ground-truth reference available at eval time.

## Transfer

| | |
|---|---|
| **Home field** | speech recognition / human-computer interaction: an acoustic front-end, a follow-up utterance that is itself noisy input |
| **Here** | any asking system that must decide, on receiving a reply, whether it accepts what it has, should treat the reply as unrelated new content, or must repair a specific span of its current answer |
| **What survives** | the three-way turn classification before any repair is attempted; decomposing repair into locate-then-infer-then-apply rather than an unconstrained rewrite |
| **What does not** | the acoustic-specific machinery (a speech front-end producing the first hypothesis, TTS-synthesized feedback) — nothing here is shown to transfer to a text-only or non-perceptual asking loop |

## Limits

- Evidence is confined to ASR: acoustic input, an LLM refinement module and
  a single evaluated [[backbone-of-a-formula|backbone]] (Qwen3-ASR-1.7B transcribing, Qwen3-32B doing
  intent routing and correction); no experiment tests the framework outside
  speech.
- The three-way intent label (confirmation / new input / correction) is
  itself produced by an LLM classifier with no reported accuracy figure of
  its own — the monotonic S2ER drop is evidence the whole loop works, not
  evidence the routing step is correctly labelled turn by turn.
- All corrective feedback in the reported experiments comes from an LLM
  User Simulator's synthesized speech (via TTS), not from real users in the
  loop; the human-in-the-loop case is not run end to end.

## Related

[[clarification-request]] · [[sentence-level-semantic-error-rate]] · [[clarification-benchmarks]] · Source

[^c1]: jiang-2026-towards — "In contrast, Interactive ASR formulates transcription as a stateful multi-turn refinement process."
[^c2]: jiang-2026-towards — "the update is carried out through three stages: semantic correction, intent routing, and reasoningbased correction."
[^c3]: jiang-2026-towards — "S 2 ER on GigaSpeech Test drops from 21.47% at Loop 0 to 12.35% after only one interaction and reaches 3.49% by Loop 10, while ASRU2019 Test improves from 28.57% to 10.32% after one loop and to 1.36% by Loop 10."
