---
description: "Does requiring the answer in a fixed schema change how good the answer is? Four studies now agree the effect is real and locate it upstream of the decoder, at the format-requesting prompt itself."
aliases: ["format restriction penalty", "structured generation performance gap", "format tax"]
sources: ["arxiv-2604-03616", "geng-2025", "kurt-2024", "tam-2024"]
---
# The format-restriction effect

> Does requiring the answer in a fixed schema change how good the answer is?
> Four studies, disagreeing signs, and — at last — a located source: the cost
> is paid at the prompt, before the decoder ever masks a token.

## What was measured

**Tam, Wu, Tsai, Lin, Lee & Chen (EMNLP 2024, Industry Track)** ran three
conditions — constrained decoding / JSON mode, format-restricting
instruction, and a two-step *NL-to-Format* (answer freely, then convert) —
across GSM8K, Last Letter Concatenation, Shuffled Objects, DDXPlus, MultiFin,
Sports Understanding and Natural Instructions Task 280. They report a decline
in reasoning accuracy that grows with the strictness of the restriction: on
GSM8K, GPT-3.5-Turbo scored 76.60% in natural language against 49.25% in
JSON mode. Classification tasks moved the other way — constraining the option
set removed answer-selection errors. Their proposed mechanism is not parsing
(0.148% failures against a 38.15% gap on Last Letter) but **key order**: 100%
of GPT-3.5-Turbo's JSON-mode responses placed `answer` before `reason`,
converting zero-shot chain-of-thought into zero-shot direct answering.

**Two later studies found the opposite sign.** Kurt (2024, .txt) re-ran
Llama-3-8B-Instruct and reports structured generation at or above
unstructured on all three reasoning tasks, attributing Tam et al.'s gap to
non-identical prompts and an LLM-based parser for the unstructured control
that scored below hand-written regex. Geng et al. (2025),
introducing JSONSchemaBench, report constrained decoding improving
downstream performance by up to 4%, including on GSM8K.

**A fourth, larger study relocates the cost.** Lee, D'Antoni & Berg-Kirkpatrick (2026)
name the gap the **format tax** (freeform performance minus format-constrained
performance) and, across six open-weight models, four API models, four
formats and four tasks, hold the prompt fixed and toggle only the decoder:
"the dominant cost is not imposed by the decoder but enters at the format-
requesting prompt, before any decoder constraint is applied" — masking adds
only −1.6pp on average against −3.9pp from the prompt alone. Requesting
JSON, XML, Markdown or LaTeX "substantially degrade[s] reasoning and writing
performance across open-weight models", but three recent closed-weight
models (claude-haiku-4.5, grok-4.1-fast, gpt-5.4-nano) show near-zero or
positive deltas, so the tax is not inherent to structured generation.[^c5]

## What survives all four

The sign disagrees and so does the proposed mechanism — key order (Tam),
prompting/parsing artefacts (Kurt, Geng), a prompt-level cost the decoder
cannot fix (Lee et al.). What survives is the location: every study that
finds a real effect finds it upstream of the token mask, in what the prompt
asks for or how the unconstrained arm is read — never in the constraint
construction itself.

## Known as

| Field | Name there | Relation |
|---|---|---|
| LLM evaluation (Tam et al. 2024) | the impact of format restrictions | close — ranges over all three restriction conditions, i.e. the umbrella [[structured-output]] names |
| LLM evaluation (Lee et al. 2026) | format tax | close — the same freeform-vs-constrained gap, decomposed into a prompt term and a decoder term |
| Constrained-generation tooling (Kurt 2024; Geng et al. 2025) | structured generation performance | close — measured only on the masking member of [[structured-output]] |
| LLM systems | constrained decoding | **not this concept** — the mechanism ([[constrained-decoding]]); this note is the measured effect of using it |

## Why it matters

Stall 5 asks whether what came back is a constraint. This says the asker's
schema is part of the answer: a schema whose first field is the verdict
forecloses reasoning the same answerer would otherwise do (Tam), and even
where key order is not at issue the format-requesting instruction itself
still costs accuracy before any mask is applied (Lee et al.). The design rule
is upstream of the decoder: separate what is asked from how it is packaged —
[[reasoning-formatting-decoupling]] gives the mechanism that recovers it.

## Limits

- **The key-order claim rests on one descriptive statistic** (answer-before-
  reason in 100% of one model's responses), not a controlled manipulation.
- The four studies do not share one scope (`## Known as`), so disagreement in
  sign is partly disagreement in what was compared.
- Kurt (2024) is a vendor blog post, not peer-reviewed; Geng et al. and Lee
  et al. share a research community with an interest in the result Tam et
  al.'s peer review reached the opposite way.
- Lee et al.'s closed-weight arm covers four API models from three
  providers — too few to call format-tax resistance a general property of
  scale rather than of these systems.
- Nothing here measures answers with no scoreable ground truth — the case
  where a schema is most tempting.

## Related

[[constrained-decoding]] · [[structured-output]] · [[reasoning-formatting-decoupling]] · [[survey-response-model]] · [[elicitation-protocols]] · [[constrained-answer-attribution]]

[^c5]: arxiv-2604-03616 — "Yet we find that structured output requirements—JSON, XML, LaTeX, Markdown—substantially degrade reasoning and writing performance across open-weight models."
