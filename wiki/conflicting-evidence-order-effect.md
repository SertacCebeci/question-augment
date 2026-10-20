---
description: "Presenting the same correct-and-incorrect evidence pair in reverse order changes 11–25% of predictions and shifts accuracy, calibration and confidence together."
aliases: ["CIC/ICC order effect", "correct-first vs incorrect-first order effect"]
sources: ["han-2026-when", "arxiv-2512-02299"]
---
# Conflicting-evidence order effect

> Two identical documents, one supporting and one contradicting the answer,
> produce a different answer and a different confidence depending only on
> which one the model reads first.

## Definition / Mechanism

Han, Lan & Kilicoglu (2026) evaluate six open-weight LLMs
(4B–14B parameters) on HealthContradict, a biomedical yes/no benchmark where
each of 920 questions is paired with one correct and one incorrect retrieved
document. Presenting both documents with the correct one first (CIC) versus
the incorrect one first (ICC) — same two documents, order reversed — changes
outcomes: "accuracy drops for every model and 11.4%–25.2% of predictions
flip."[^c1]

The two orders are not equivalent on any measured axis: "'CIC' consistently
outperforms 'ICC' in both accuracy and AUROC, with an 11.1-point mean
accuracy gap and a 10.0-point mean AUROC gap." [[calibration|Calibration]] error follows the
same ranking — mean ECE 0.084 (CIC) versus 0.168 (ICC), mean Brier 0.134
versus 0.230 — "the same ordering holds under calibration-error metrics."[^c2]

The direction of the shift is not simple "conflict adds uncertainty": adding
the correct document to an incorrect-only prompt (IC→CIC) makes four of six
models *more* confident (lower [[entropy]], higher logit margin), while adding
the incorrect document to a correct-only prompt (CC→ICC) reliably reduces
confidence more than CC→CIC does (mean Δ logit margin −3.79 vs −2.40). "This
suggests that uncertainty often tracks which document becomes behaviorally
dominant rather than contradiction itself."[^c3]

## Why it matters

This is a controlled decomposition — same evidence, only order varied — so
the accuracy and confidence gap cannot be attributed to which facts were
available, only to their position in the prompt. It is evidence that a
"consistency check" over retrieved constraints cannot treat retrieved
evidence as an unordered set: two answerers holding literally the same two
documents disagree with each other, and with themselves under reordering,
at a rate (11–25% of predictions) large enough to be the dominant source of
error in the conflicting-evidence condition rather than a minor artifact.

## Limits

- Single benchmark (HealthContradict, biomedical yes/no questions drawn from
  TREC Health Misinformation tracks) and six open-weight models 4B–14B
  parameters; whether the magnitude generalizes to free-form QA, larger
  models, or non-biomedical domains is untested here.
- Only two-document conflicts (exactly one correct, one incorrect) are
  tested; order effects with more documents or with partial/graded
  disagreement are not measured.
- The paper attributes the asymmetry to "which document becomes
  behaviorally dominant" as an interpretation of the pattern, not a
  mechanism it isolates experimentally (e.g. by intervening on attention or
  position encoding directly).
- Not independently replicated outside this paper and the benchmark's
  original release (Zhang et al. 2026, not read here); `replicated: false`.
- The benchmark's original release, Zhang et al. (2026), was read after the note above was written. It also reports an order effect on the same two-document pairs, but its direction is not uniform across models. BioMed-Llama-3.2-1B does better when the correct document comes later, by 5.9 points between the two orders; Meditron3-Qwen2.5-7B does better when it comes first, by 7.0 points.[^c4][^c5] So "correct-first is better" holds for the models Han et al. tested, and it is not a general law of the benchmark.
## Related

han-2026-when · [[conflict-aware-abstention-score]] · [[abstention]] · [[parametric-context-failure-rates]] — the same benchmark read through over-reliance and vulnerability rates, not the order of the documents

[^c1]: han-2026-when — "accuracy drops for every model and 11.4%–25.2% of predictions flip"
[^c2]: han-2026-when
[^c3]: han-2026-when — "This suggests that uncertainty often tracks which document becomes behaviorally dominant rather than contradiction itself."
[^c4]: arxiv-2512-02299 — "from a later position of the correct document in conflicting contexts"
[^c5]: arxiv-2512-02299 — "indicating that it benefits from the earlier position of the correct"
