---
description: "Scoring each atom of a compositional prompt by its own soft VQA probability and averaging the results sets whether the score reads as atom-level or prompt-level correctness."
aliases: ["Soft-TIFA", "per-atom VQA scoring", "atom-level soft VQA score"]
sources: ["arxiv-2512-16853"]
---
# Atomwise soft verification

A compositional prompt is several checks at once. "Three pink pigs jumping over a sheep" asks for a count, an attribute, a verb and a relation, and an image can pass some and fail others. A judge that returns one number for the whole picture has to decide how to combine those checks, and the usual designs differ in where they decide. VQAScore "uses" one question, which the paper describes as "a single question containing the prompt."[^b1] TIFA "uses an LLM to break the prompt down into component questions," so the coverage of the prompt depends on what the language model chose to ask.[^b2]

Atomwise soft verification keeps the decomposition and fixes both steps. Each atom, the paper's term for an object, attribute or relation, gets one templated question, and the VQA model's answer is kept as a probability rather than a yes or no. The paper's method "generates one question per atom of each prompt using the same templates" that produced the prompts, and "assigns soft scores to each answer as predicted by the VQA model when" the generated image is given.[^b3][^b4] The image score is then a mean over the N atom probabilities.

The mean is the part that decides what is measured. With the arithmetic mean the score "captures atom-level correctness of the T2I model."[^b5] With the geometric mean the score is said to capture prompt-level correctness, "as it penalizes low atom-level scores at the prompt-level," which the authors match to the human rule "where a prompt is incorrect if any component atom is incorrect."[^b6][^b7] My reading of the formula: a geometric mean of probabilities falls to near zero when any one atom probability is near zero, so a single missed atom is enough to pull the score down, while the arithmetic mean lets one missed atom be averaged away by the rest. The same N probabilities therefore answer two different questions, depending only on the aggregator.

On a prompt-level human label, the paper reports that Soft-TIFA with Qwen3-VL-8B "attains an AUROC of 94.5%, compared" with "to 92.4% for VQAScore and 91.6% for TIFA."[^b8][^b9] The comparison uses prompt-level human scores: "The human scores compared against are prompt-level scores."[^b10] The geometric variant "outperforms existing methods on the original, rewritten, and combined sets of" prompts.[^b11]

The decomposition is also offered as a defence against the drift in [[benchmark-drift]]. The paper's claim: "prompt into per-atom questions renders the VQA model more robust to image distribution shift in T2I outputs."[^b12] The sentence that states it is hedged in the same caption: "potentially because breaking the."[^b13]

The aggregator matters because the models differ most at the prompt level. The best model reaches "only 35.8% accuracy at the" prompt level while doing well on single atoms, and "T2I model performance dropping steeply with increase in prompt compositionality."[^b14][^b15]

Compared with the atomic checklists in [[expert-report-derived-atomic-rubrics]], which score a report by the share of binary items passed, this method keeps the atoms but makes each check a probability and makes the aggregator an explicit choice. The checklist reads one share; the soft verifier can read either an atom-level or a prompt-level number from the same run.

## Limits

- Coverage is guaranteed only by construction. The atoms come from the same templates as the prompts, so the question set is complete for GenEval 2. For free-form prompts whose atoms are not templated, the coverage question is open; the authors state a belief rather than a test: "We believe a TIFA-like approach would work well."[^b16]
- A soft score is only as informative as the VQA model's probabilities. The text reports the result across Qwen-family VQA models and concludes "Hence, our method is not oversensitive to the underlying VQA model."[^b17] The range of VQA models is narrow: one family, plus GPT-4o for VQAScore as the comparison.
- The decomposition inherits the VQA model's blind spots. On the verb skill, "VQA models are stricter than human judgment" — the paper reports this as a shortfall of the VQA model, not a fault of the decomposition.[^b18]
- The margins are small. The AUROCs are 94.5, 92.4 and 91.6 on one human-labelled set, and the robustness claim rests on a figure with a hedged explanation. The passages read give point values, not intervals.
- Choosing the geometric mean makes one missed atom decisive. Whether one missed atom is a failure is a choice about what counts as a correct image, and the paper makes it rather than finding it.

## Related

- [[benchmark-drift]] — the time-dependent failure of a frozen judge, against which the per-atom design is offered as a defence
- [[expert-report-derived-atomic-rubrics]] — the same atomization as a binary checklist scored as a share passed; here each atom is a soft probability and the aggregator is chosen

[^b1]: arxiv-2512-16853 — "a single question containing the prompt"
[^b2]: arxiv-2512-16853 — "uses an LLM to break the prompt down into component questions"
[^b3]: arxiv-2512-16853 — "which generates one question per atom of each prompt using the same templates"
[^b4]: arxiv-2512-16853 — "assigns soft scores to each answer as predicted by the VQA model when"
[^b5]: arxiv-2512-16853 — "captures atom-level correctness of the T2I model"
[^b6]: arxiv-2512-16853 — "as it penalizes low atom-level scores at the prompt-level"
[^b7]: arxiv-2512-16853 — "where a prompt is incorrect if any component atom is incorrect"
[^b8]: arxiv-2512-16853 — "Soft-TIFA attains an AUROC of 94.5%, compared"
[^b9]: arxiv-2512-16853 — "to 92.4% for VQAScore and 91.6% for TIFA."
[^b10]: arxiv-2512-16853 — "The human scores compared against are prompt-level scores"
[^b11]: arxiv-2512-16853 — "outperforms existing methods on the original, rewritten, and combined sets of"
[^b12]: arxiv-2512-16853 — "prompt into per-atom questions renders the VQA model more robust to image distribution shift in T2I outputs."
[^b13]: arxiv-2512-16853 — "potentially because breaking the"
[^b14]: arxiv-2512-16853 — "the top-performing model achieves only 35.8% accuracy at the"
[^b15]: arxiv-2512-16853 — "steeply with increase in prompt compositionality."
[^b16]: arxiv-2512-16853 — "We believe a TIFA-like approach would work well"
[^b17]: arxiv-2512-16853 — "Hence, our method is not oversensitive to the underlying VQA model."
[^b18]: arxiv-2512-16853 — "in which VQA models are stricter than human judgment"
