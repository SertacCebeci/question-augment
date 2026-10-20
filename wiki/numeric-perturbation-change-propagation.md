---
description: "Counterfactual numeric edits test whether a chain follows a changed number: whether the new value reaches the steps, whether the structure adapts, and whether the answer moves."
aliases: ["counterfactual numeric perturbation", "change propagation rate", "counterfactual sensitivity", "numeric counterfactual sensitivity"]
sources: ["arxiv-2512-00552"]
---
# Numeric perturbation and change propagation

A model's answer to a question with one number changed can be compared with its answer to the original. The paper builds matched pairs this way. Its modifications are "percentage-based shifts" of ±10%, ±20% and ±30%, absolute value changes, temporal adjustments for year-based queries, and quantity multipliers, applied to numbers that a regex-based detector finds in the question.[^c1] For each pair, the paper asks three questions, which it names: "change propagation (whether modified values appear in reasoning steps)", reasoning adaptation ("structural modifications in logical chains"), and answer adjustment.[^c2]

The mechanism is a dependency test. If a chain actually computes with the given numbers, a changed number should reach the step that uses it, the structure of the chain should change where the arithmetic changes, and the final value should move. A chain that matches a stored template keeps its steps and the old result, because nothing in the template depends on the value. The paper frames the question as whether models "truly understand mathematical relationships or merely" do so, and states the conclusion it draws: "apparent mathematical competence relies heavily on memorized solution templates rather than flexible computational understanding."[^c3] The template reading is the paper's interpretation of the failures; the test itself only shows that the chain did not follow the change.

The headline result is brittleness. The paper says the model shows "brittle reasoning when numerical parameters shift".[^c4] Its table gives per-metric rates over 999 pairs. Reading the extracted columns in the order of their headers, change propagation is about 0.677, reasoning adaptation about 0.991 and answer adjustment about 0.999. I could not confirm the column alignment from the text extraction, so I rely on this only to note that the propagation figure, not the answer figure, carries the paper's brittleness claim (my reading).

## Limits

- Propagation is a string test. A changed value counts as reaching the steps only if it appears in them, so a model that rounds, rewrites the quantity in words, or carries it implicitly is scored as not propagating. How often this happens is not reported (my inference).
- Answer adjustment does not show correctness. The extracted definition of the answer measure seems to include a correctness term, but the text is garbled at that point, so I do not state what it checks. Where an answer moves, the test does not verify that the new answer is right.
- Some perturbed questions may be unnatural or unit-inconsistent, since the edits are regex-driven. The text does not report a naturalness check.
- Memorization is inferred, not measured. The paper has no control of unseen problems of the same difficulty, so the template explanation is one reading among those that fit the propagation numbers.
- One model, one benchmark (MenatQA), and the authors' own choice of perturbation magnitudes. The ±10 to ±30% grid is not justified in the sections I read.

## Related

- [[bayes-consistency-under-ablation]] — a score that tracks how behaviour moves under perturbation when accuracy saturates; the same probe family, applied to a different signal.
- [[clean-accuracy-masks-adversarial-collapse]] — a clean score that hides collapse under input perturbation; this note is a numeric-edit version of that concern.
- [[clever-hans-effect]] — reliance on a cue that breaks once the correlation changes; the template account here is the same failure, shown through an edited number.
- [[accuracy-masks-unstable-reasoning]] — accuracy averages over routes that differ in soundness, the reason a propagation test is needed beside the answer.

[^c1]: arxiv-2512-00552 — "percentage-based shifts"
[^c2]: arxiv-2512-00552 — "change propagation (whether modified values appear in reasoning steps)"
[^c3]: arxiv-2512-00552 — "relies heavily on memorized solution templates rather than flexible computational understanding"
[^c4]: arxiv-2512-00552 — "they demonstrate brittle reasoning when numerical parameters shift"
