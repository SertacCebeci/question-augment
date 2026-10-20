---
description: "A benchmark scores reasoning by the weighted share of an expert's solution checkpoints the model's chain of thought covers, judged by a model, alongside final-answer accuracy."
aliases: ["Reasoning Path Fidelity", "Reasoning Process Fidelity", "RPF", "checkpoint recall", "expert-path fidelity"]
sources: ["arxiv-2512-01274"]
---
# Reasoning path fidelity

Final-answer accuracy cannot tell a sound derivation from a right guess, so a benchmark can score the reasoning itself against a reference derivation. SUPERChem calls this Reasoning Path Fidelity (RPF). Its items carry expert explanations, and the authors decompose each one into "discrete, atomic knowledge units, referred to as Checkpoints": critical logical steps, intermediate calculations or conceptual inferences.[^c1] The expert solution is the reference because "step-by-step expert solutions provide granular checkpoints for process-level assessment."[^c2] Each checkpoint carries a weight, which the paper ties to its "difficulty and importance within the derivation process."[^c3]

A judge model reads the question, the checkpoints and the candidate's reasoning, and marks a checkpoint matched when the reasoning captures its concept, implication or example. Matching is "not through strict string matching, but through semantic equivalence."[^c4] The score is weighted recall: the summed weight of matched checkpoints over the total weight.[^c5] The judge is Gemini 2.5 Pro, which the authors run at temperature 1.0 as an evaluator.[^c6]

The metric is built to catch the case accuracy misses. Its stated purpose is to penalize a correct answer reached through wrong logic, which the paper glosses as "correct answer but wrong logic".[^c7]

On the paper's two-axis plot, GPT-5 (High) and Gemini 2.5 Pro sit in the high-accuracy, high-fidelity corner. Their RPF is the highest of the frontier models, 59.2% and 59.5%, with accuracy of 38.5% and 37.9%.[^c8] DeepSeek-V3.1-Think reaches 37.3% accuracy, but "its RPF is notably lower at 52.5%".[^c9] The authors read this gap as a style: it "points to a highly effective yet unconventional reasoning style" rather than luck.[^c10] The numbers are the paper's; the reading of a gap as a difference in cognitive style is the authors' interpretation.

## Relation to outcome-consistency checks

The lucky-guess concern is the one [[process-outcome-consistency-verification]] addresses, with a different tool. There a verifier asks whether the derivation supports the stated outcome, which needs no reference path. RPF asks how much of one expert's path the reasoning recovers. A sound route that differs from the expert's gets no credit under recall, while a consistency check would not penalize it. This difference is my inference from the two designs; neither work tests one measure against the other.

The measure also sits next to the answer-choice shortcut in [[option-matching-shortcut]]. A closed set of options can deliver a right answer without the deduction behind it, and a fidelity score is one way to see past the choice. Whether RPF separates those cases in practice is not tested in the text read (my reading).

## Limits

- No agreement check between the judge and human graders appears in the text read; a search of the full text for agreement or validation found none. The score is only as reliable as the judge's matching, and the paper reports no error rate for it.
- Checkpoint weights come from the annotation process, and the text read gives no sensitivity test. A different weighting or a different expert path changes the score, and the paper does not show by how much.
- Each item has one expert path. The paper credits reasoning "that may use alternative valid terminologies", which is variation in wording. A different valid route to the same result earns credit only where its steps match a checkpoint in meaning (my reading).
- The measure is tested on one benchmark of chemistry multiple-choice items with up to 26 options. Open-ended answers and other domains are not covered.
- The profile of frontier models is descriptive. The text read does not show that RPF predicts performance on any other task.

## Related

- [[process-outcome-consistency-verification]] — the same lucky-guess failure, caught by a consistency check between derivation and outcome instead of a recall of a fixed path
- [[option-matching-shortcut]] — the answer-choice route to a right answer that a fidelity score is meant to see past
- [[reasoning-shortcut]] — shortcuts in reasoning generally, the failure family RPF is built to expose
- evidence-entailment-fidelity — the same word for a check of the trace against the passages it was given, not against an expert's checkpoints

[^c1]: arxiv-2512-01274 — "discrete, atomic knowledge units, referred to as Checkpoints"
[^c2]: arxiv-2512-01274 — "step-by-step expert solutions provide granular checkpoints for process-level assessment"
[^c3]: arxiv-2512-01274 — "difficulty and importance within the derivation process"
[^c4]: arxiv-2512-01274 — "not through strict string matching, but through semantic equivalence"
[^c5]: arxiv-2512-01274 — "is calculated as the weighted recall of these reasoning checkpoints"
[^c6]: arxiv-2512-01274 — "utilizes Gemini 2.5 Pro (temperature set to 1.0) as an expert evaluator"
[^c7]: arxiv-2512-01274 — "correct answer but wrong logic"
[^c8]: arxiv-2512-01274 — "maintaining the highest reasoning fidelity (59.2% and 59.5%, respectively)"
[^c9]: arxiv-2512-01274 — "its RPF is notably lower at 52.5%"
[^c10]: arxiv-2512-01274 — "points to a highly effective yet unconventional reasoning style"
