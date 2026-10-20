---
description: "Auditing a benchmark's tool schemas, executable code and reference trajectories found defects in 71.5% of BFCL multi-turn entries, so a wrong score can be the question's fault, not the answerer's."
aliases: ["benchmark error audit", "ground-truth defect audit", "benchmark repair"]
sources: ["arxiv-2603-05553", "arxiv-2512-14698", "arxiv-2512-05537", "arxiv-2511-21522"]
---
# Reference-answer defect audit

A question set is only as good as the three things behind it: the interface the answerer is shown, the machinery that executes or checks the answer, and the reference answer. EigenData audited the multi-turn part of the Berkeley Function-Calling Leaderboard (BFCL-V3) by running separate agents on each layer. One agent examined ground-truth trajectories and evaluation logic. A second exercised the benchmark's executable functions on synthesized edge cases. A third cross-checked the backing data for constraint violations.[^c1]

## What was found

Of 200 multi-turn entries, 143 (71.5%) carried at least one defect, in three families.[^c2]

- **Schema errors (39 entries, 19.5%).** The interface told the answerer something false. Examples: `close_ticket` declares `ticket_id` as an integer while the data and ground truth use the string "ticket_001"; a cruise-control function takes "m/h" and returns "km/h"; a documented response key differs from the one implemented.[^c3] A model that follows such a schema faithfully cannot succeed.
- **Implementation errors (91 entries, 45.5%).** The checker's own code was wrong. `setHeadlights("auto")` fell into an else branch and turned the lights off. `tail(lines=0)` returned the whole file because of `content[-0:]`. A zipcode lookup silently returned "00000" for an unrecognized city.[^c4] The paper states that these "silently penalize models that produce valid outputs".
- **Trajectory and evaluation errors (82 entries, 41%).** The reference was too rigid (rename-then-move scored wrong against move-then-rename, though the filesystem ends identical; integer 32 required where the API returns 32.0), flatly mislabeled (a word-sort where a line-sort was asked), or missing alternative valid paths.[^c5]

The three families overlap, so the total is deduplicated and is smaller than their sum.

## Repair and what it changed

Each family was routed to its own fixer: schema rewrite checked against implementation and ground-truth usage, an iterative debug loop for code, and selective trajectory modification. The orchestrator propagated a schema fix to the matching implementation and to every affected trajectory.[^c6] The authors also replaced turn-level trajectory matching with a check of final database state, and report that the repaired benchmark with this metric resolved rank inversions in the original leaderboard and tracked human judgments of functional correctness better.[^c7]

A second finding bears on answering. On the repaired set, pass rates were 57.0% (key function) and 53.8% (config match) alone, 41.0% when both were required and 33.6% under all three criteria, so a single-axis check hides independent failure modes.[^c8]

The mechanism, in my reading: a score is a joint product of answerer and question apparatus. When the apparatus is defective, the error falls on the answerer, and rankings built on those scores mislead. Auditing the apparatus is therefore a precondition for treating any low score as evidence about the answerer.

A second instance comes from video temporal grounding, where the apparatus is a set of natural-language queries with reference time spans. Re-annotating three popular grounding benchmarks found, on Charades-STA, that 20.6% of samples violated query uniqueness and 34.9% had annotation-accuracy problems. The re-annotated suite also re-ranked models against the legacy benchmarks, which the authors read as confirming that prior evaluation standards were unreliable.[^c10] The defects sit in the question wording and its reference spans rather than in executable code, so this is a different apparatus under the same account. The criteria the authors used to define a valid query are in [[grounding-query-validity-criteria]].

A clinical instance of the same point comes from incidentaloma detection in radiology reports. The authors reviewed the best model's errors: "we reviewed its 33 errors among 560 evaluated" lesions.[^c11] Four of those were missed incidentalomas that the model had read correctly, because the annotators had overlooked cues of prior evaluation, and "These were annotation errors rather than model failures."[^c12] The gold standard also sets a ceiling the model can pass. Annotator agreement was 0.76 macro-F1 and the best model reached 0.79, which the authors describe as having "closely matched the inter-annotator agreement of 0.76."[^c13] A gold label, then, is evidence about the reference, not a fixed measure of the answerer; the count of four is from one model's error set and says nothing about the other systems.

The same account reaches proof verification. A verifier that flags a flaw in a correct proof is scored as wrong, so a bad reference looks like a weak verifier. The paper's abstract says that "existing benchmarks underestimate its effectiveness on stronger models due to inherent annotation errors."[^c14] Its case study reads the apparent drop in true-positive rate on stronger models as largely a labelling artifact: "decrease in TPR is largely an illusion caused by dataset" annotation.[^c15] The evidence is a set of "concrete examples of mislabeling in the original dataset," found by re-examining false negatives.[^c16] The authors also concede that the classification of each finding is a judgement: "whether it should be judged as an error depends entirely on subjective" criteria when the flaw is minor.[^c17] Their case study "focus[es] primarily on the False Negative" cases,[^c18] so the rate of mislabelled references is measured only where the verifier disagreed with the label.

## Limits

- Only 200 multi-turn cases from one benchmark were audited and repaired; the authors say scaling to the full benchmark is future work.[^c9]
- Comparison with other evaluation paradigms (reward-model or simulation based) is deferred, and every agent role used frontier LLMs, so the cost of the audit and its false-positive rate are not reported in the passages I read.
- The audit's own errors were not independently measured by me; the human-agreement claim rests on the authors' evaluation, and I did not verify its size.
- The setting is executable tool-calling; whether the 71.5% rate carries to open-ended question answering is untested.

## Related

- [[validity-screening-protocol]] — screening items for validity before use; this note supplies a measured defect rate for one benchmark
- [[benchmark-contamination-convergent-audit]] — another audit of benchmark trustworthiness, aimed at leakage rather than defects
- [[obstacle-driven-state-audit]] — state-based checking of whether a task is actually completed
- [[pessimistic-min-judge-aggregation]] — a verifier whose measured gain on proof benchmarks is read against the same kind of mislabelled reference

[^c1]: arxiv-2603-05553 — "the C ODING AGENT’s TestingAgent and JudgeAgent exercise the benchmark’s executable functions against synthesized edge cases"
[^c2]: arxiv-2603-05553 — "In total, these errors affect 143 out of 200 entries (71.5%) in BFCL’s multi-turn evaluation suite"
[^c3]: arxiv-2603-05553 — "A model that follows the schema strictly produces a type-correct call that fails at runtime."
[^c4]: arxiv-2603-05553 — "these bugs silently penalize models that produce valid outputs, inflating error rates and"
[^c5]: arxiv-2603-05553 — "overly rigid evaluation, which"
[^c6]: arxiv-2603-05553 — "with E IGEN C ORE ensuring that a schema fix propagates to both the corresponding"
[^c7]: arxiv-2603-05553 — "produces benchmarks that are both more reliable (fewer false negatives from schema mismatches"
[^c8]: arxiv-2603-05553 — "This 23.4 percentage-point gap between the easiest"
[^c9]: arxiv-2603-05553 — "focuses on 200 multi-turn cases; scaling the repair and evaluation to the full benchmark remains"
[^c10]: arxiv-2512-14698 — "confirming the unreliability of prior evaluation"
[^c11]: arxiv-2512-05537 — "we reviewed its 33 errors among 560 evaluated"
[^c12]: arxiv-2512-05537 — "These were annotation errors rather than model failures"
[^c13]: arxiv-2512-05537 — "closely matched the inter-annotator agreement of 0.76"
[^c14]: arxiv-2511-21522 — "its effectiveness on stronger models due to inherent annotation errors."
[^c15]: arxiv-2511-21522 — "decrease in TPR is largely an illusion caused by dataset"
[^c16]: arxiv-2511-21522 — "concrete examples of mislabeling in the original dataset,"
[^c17]: arxiv-2511-21522 — "whether it should be judged as an error depends entirely on subjective"
[^c18]: arxiv-2511-21522 — "we focus primarily on the False Negative"
