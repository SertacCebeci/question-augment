---
description: "Separate deriving an answer from packaging it into the requested schema — a second reformatting pass, or a reasoning trace before the formatted output — and most of the format tax reverses."
aliases: ["two-pass generation", "decoupled reasoning and formatting", "freeform-then-reformat"]
sources: ["arxiv-2604-03616", "arxiv-2512-02499"]
---
# Reasoning–formatting decoupling

> A format-requesting instruction taxes accuracy because it asks the model to
> derive the answer and package it in the same breath. Split the two acts —
> in two calls or in one scratchpad — and most of the tax reverses.

## Definition / Mechanism

Lee, D'Antoni & Berg-Kirkpatrick (2026) isolate the
[[format-restriction-effect|format tax]] to the format-requesting prompt, not the
decoder's grammar mask, and test two ways of keeping the prompt but changing
what the model conditions on when it commits to structure:

- **2-Turn.** The first call answers in natural language with no mention of
  formatting; the second call reformats that answer into the target schema.
  "The first call generates a freeform answer with no mention of formatting,
  and the second reformats it into the target structure." The cost is a
  second inference call and roughly double the tokens.
- **Thinking.** A single call, but the model emits a hidden reasoning trace
  before its visible answer: "Thinking allows the model to reason in a
  scratchpad before producing structured output — the format-requesting
  prompt is the same, but by the time the model generates its answer, it
  conditions on a full reasoning trace rather than the prompt alone."[^c2]

Across six open-weight models, three reasoning benchmarks and four formats,
"2-Turn significantly improves accuracy in 42 of 72 model–task–format
comparisons (p < 0.05, average +6.8 pp), while significantly worsening only
2." "Thinking significantly improves 43 of 72 comparisons (+9.2 pp
average) but carries more risk: 11 comparisons (15%) significantly worsen."
[^c4] Thinking token counts stay aligned between freeform and structured
generation (r = 0.72) and mention formatting in under 3% of sentences, so it
works by holding a reasoning phase temporally prior to the formatting
commitment, the same separation 2-Turn enforces across calls — not by
changing the prompt.

A clinical case of the same split is stroke outcome prediction from discharge summaries, with open-source LLaMA-3-8B. The first call's output is itself structured: it "produces a structured chain-of-thought output containing key clinical cues," with provisional reasoning and a tentative prognosis.[^c6] A second call, the "extraction LLM," reads that text and "returns a single mRS score between 0 to 6."[^c10] The authors' account of why the single-call arm does worse is the format tax again: single-step models "struggle to balance complex reasoning with rigid output constraints."[^c7] In development they "produced free-text or mixed-format outputs" under detailed reasoning instructions,[^c9] and the two-step design "consistently outperformed the single-step baseline" on MAE and on ±1 accuracy.[^c8][^c11] The split here removes only the final integer from a rationale that already has a schema, so it is not a move from structured to freeform generation. The paper gives no test of the first call without structure (my reading).

## Why it matters

The format-restriction effect shows *that* asking for a schema costs
accuracy and *where* the cost enters (the prompt, not the mask). This gives
the lever: an asker who needs a parseable reply does not have to accept the
tax as the price of parseability — deriving the content and choosing its
container are separable acts, and forcing them into one generation is what
costs the accuracy, not the schema itself.

## Limits

- 2-Turn is the safer mitigation (3% of cells worsen) but doubles latency and
  token cost: "The 2-Turn strategy that recovers most lost performance
  introduces practical costs: additional API calls, increased latency, and
  roughly doubled token consumption. For latency-sensitive applications, this
  overhead may be prohibitive."[^c5]
- Thinking is stronger on average but riskier (15% of cells worsen,[^c4]
  above) and "does not transfer to writing: on WritingBench, it fails to
  close the gap and sometimes widens it." Neither mitigation is uniformly
  better.
- Both are tested only on open-weight models 3B–32B; recent closed-weight
  models already resist the tax without decoupling, so whether decoupling
  helps them further is unmeasured.
- Recovery is *most* of the tax, not all of it — the paper reports averages,
  not a claim that either method restores freeform-baseline accuracy in
  every cell.
- The clinical case is one institution's 464 patients: "the models were evaluated using data from a single center."[^c12] Prompts were "guided by iterative trial and error,"[^c13] and the single-step arm was tuned on the same exploration subset ("Prompt exploration was performed using the same exploration subset as"[^c14]), so the contrast is between two tuned pipelines.
- The arms differ in more than the packaging: one call against two, different prompts, and a first call that writes a prognosis. Nothing holds the reasoning content fixed while varying only where the format is requested, so the gain cannot be credited to decoupling alone (my inference).
- The format failures that motivate the design are anecdotal: "During development, we observed that single-step LLMs often"[^c15] — the paper reports no count.

## Related

[[format-restriction-effect]] · [[structured-output]] · [[constrained-decoding]] · [[survey-response-model]]

[^c2]: arxiv-2604-03616 — "Thinking allows the model to reason in a scratchpad before producing structured output—the formatrequesting prompt is the same, but by the time the model generates its answer, it conditions on a full reasoning trace rather than the prompt alone."
[^c4]: arxiv-2604-03616 — "Thinking significantly improves 43 of 72 comparisons (+9.2 pp average) but carries more risk: 11 comparisons (15%) significantly worsen."
[^c5]: arxiv-2604-03616 — "The 2-Turn strategy that recovers most lost performance introduces practical costs: additional API calls, increased latency, and roughly doubled token consumption. For latency-sensitive applications, this overhead may be prohibitive."
[^c6]: arxiv-2512-02499 — "produces a structured chain-of-thought output containing key clinical cues"
[^c7]: arxiv-2512-02499 — "struggle to balance complex reasoning with rigid output constraints"
[^c8]: arxiv-2512-02499 — "This two-step design consistently outperformed the single-step baseline"
[^c9]: arxiv-2512-02499 — "produced free-text or mixed-format outputs"
[^c10]: arxiv-2512-02499 — "returns a single mRS score between 0 to 6"
[^c11]: arxiv-2512-02499 — "the Single-Step LLM baseline performed worse than COPE"
[^c12]: arxiv-2512-02499 — "the models were evaluated using data from a single center"
[^c13]: arxiv-2512-02499 — "guided by iterative trial and error"
[^c14]: arxiv-2512-02499 — "Prompt exploration was performed using the same exploration subset as"
[^c15]: arxiv-2512-02499 — "During development, we observed that single-step LLMs often"
