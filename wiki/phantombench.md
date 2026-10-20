---
description: "PhantomBench measures LM abstention with 60K+ generated non-existent terms and entities verified absent from a web corpus, and finds abstention on them predicts abstention on rare real concepts."
aliases: ["PhantomBench", "PHANTOM-T", "PHANTOM-E"]
sources: ["jung-2026"]
---
# PhantomBench

> Instead of asking whether a model answers correctly, ask whether it will
> even say "I don't know" about something that was never there.

## Definition / Mechanism

Jung & Gonen (2026) build non-existent **terms** (abstract
concepts, e.g. blended from existing words: "entermolecule chemistry" from
"enteric" + "macromolecule") and non-existent **entities** (recombined
structural pattern + lexical item, e.g. "Methods in Intelligent Human") by
generation, then verify non-existence with an exact-match filter against
Dolma v1.7 (2.3T tokens) via Infini-gram — a concept with zero corpus
matches across four casing variants is kept as non-existent by
construction. "The first large-scale benchmark of its kind, comprising more
than 60K non-existent terms and entities derived from real concepts across
diverse domains."[^c1]

Each concept is queried with prompts of varying presupposition (existence,
meaning, date, place, plus etymology/application/relation for terms). A
model's output is scored by an LLM judge for a binary
abstain/non-abstain decision, validated against four human annotators on a
120-response sample via the Alternative Annotator Test. Hallucination rate
(HR) is the fraction of non-abstaining responses: "we evaluate a total of
21 models of various types and sizes."[^c2]

"We show staggering hallucination rates across the board (with average
rates as high as 86.7% in some cases), and note that even frontier models
surprisingly fail to abstain on non-existent concepts, especially when the
input presumes their existence." Larger, reasoning, and
domain-specialized variants hallucinate *more* than smaller
general-purpose ones within the same family.[^c3]

Across 64 settings (4 prompt types × 2 datasets × 8 models), [[abstention]]
rate on non-existent concepts correlates strongly with abstention rate on
independently-sourced *rare* real concepts (Pearson ρ = 0.755, p < 0.001)
and only weakly with abstention on *common* concepts (ρ = 0.322, p =
0.009) — evidence that a synthetic, verifiably-absent concept is a usable
stand-in for the untestable case of a real concept a model has barely
seen.[^c4]

## Why it matters

It gives the answerer's abstention decision (stall 10) a **manufactured
ground truth**: whether a concept exists is undecidable to check at scale
for real rare concepts, but decidable by construction for a generated one,
so hallucination can be measured directly (any content about the concept
is a hallucination) rather than inferred from disagreement with a
reference answer.

## Limits

- The rare-concept correlation is established on a narrower slice (8
  models, 2 datasets, 4 prompt types) than the headline 21-model, 60K-concept
  result; the proxy claim does not automatically extend to every model or
  prompt type in the full benchmark.
- Non-existence is verified against one corpus (Dolma) with exact-match
  search; a concept absent from Dolma but present in a model's own
  (different) training data would be mis-labelled non-existent for that
  model.
- Abstain/non-abstain is judged by an LLM (validated on 120 human-labelled
  responses, not the full evaluation set), so per-instance judge error is
  possible even though the judge–human agreement reported is high. [?]

## Related

[[abstention]] · [[sage-abstention-evaluation]] · [[calibration]] · [[clarification-benchmarks]]

[^c1]: jung-2026 — "the first large-scale benchmark of its kind, comprising more than 60K non-existent terms and entities derived from real concepts across diverse domains"
[^c2]: jung-2026 — "we evaluate a total of 21 models of various types and sizes"
[^c3]: jung-2026 — "We show staggering hallucination rates across the board (with average rates as high as 86.7% in some cases), and note that even frontier models surprisingly fail to abstain on non-existent concepts, especially when the input presumes their existence."
[^c4]: jung-2026 — "abstention rates on non-existent and rare concepts show a strong Pearson correlation (ρ = 0.755, p < 0.001), compared to a much weaker correlation between non-existent and common concepts (ρ = 0.322, p = 0.009)"
