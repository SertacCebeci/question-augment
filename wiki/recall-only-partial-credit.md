---
description: "Partial credit for a multi-answer item, scored as the share of correct options captured, is recall alone, so it cannot register over-selection; precision or F1 has to sit beside it."
aliases: ["overlap accuracy", "set-overlap partial credit", "fraction-of-gold credit", "recall-equivalent accuracy"]
sources: ["arxiv-2512-22966", "doi-10-48550-arxiv-2607-05150", "arxiv-2512-14102"]
---
# Recall-only partial credit

Some items have several correct answers: a differential diagnosis with five possible conditions, a set of tests to order. A common way to give partial credit is to take the overlap between the model's selected set and the gold set, and divide by the size of the gold set. The clinical benchmark did this, so that a model which named three of five correct conditions scored "3 out of 5, or 60%."[^r1] The authors state what that measure is: "the degree of overlap between predicted multiple-choice answers and ground truth, which effectively corresponds to recall."[^r2] Overlap over the gold set is recall. It rewards each correct option found and charges nothing for an incorrect option added.

That asymmetry is the concept. The score records omissions, and says nothing about over-selection. The authors name the consequence in their own terms: "This quantitative approach, while objective and allowing partial credit, does not capture several clinically important dimensions."[^r3] The gap they point to is that a model which lists more options gets more credit without a corresponding gain in correctness. Their repair was to report precision (the share of selected options that were correct) and F1 alongside recall, so that "omission-driven versus over-selection errors" could be told apart.[^r4] The precision figures themselves sit in a supplement this note does not rely on; the point is the decomposition, not the numbers.

The same decomposition explains why the recall-only score can mislead on ranking. Two systems with equal recall can differ in how many wrong options they add, and only a precision-type measure separates them. My inference, from the definition rather than from a measurement in the paper, is that a system that selects every option reaches a perfect recall score. Whether that happens in practice depends on how the answers are presented; the benchmark does not test it.

The distinction also cuts across weighting. A missed option may matter more or less depending on its clinical role, and an extra option may be harmless or dangerous. The authors say so directly: more grounded evaluation "will require clinician-weighted or safety-oriented metrics that distinguish critical omissions from lower-impact errors."[^r5] Plain recall and plain precision both treat every option alike, which is the other half of the blind spot.

The same asymmetry appears in ranked retrieval, where the object is a top-k list rather than a gold set. A remote-sensing retrieval study makes the point with its own measures: vision-language retrievers are "usually evaluated only in terms of recall (R@k)," and their precision at k shows that they "tend to retrieve false positives and thus non-relevant images."[^r7][^r8] P@k counts the share of the top-k that are relevant, not the share of gold options found, so the arithmetic differs. My inference is that the principle is the same: a score that counts only what was found cannot see what was added.

For an asker or an answerer, the transferable part is narrow. When a multi-answer item is scored by overlap with the gold set, the score is one-sided, and a reported gain may be a gain in coverage bought with extra guesses. Read it with its precision beside it.

A recall-type score can be repaired from inside the reward. In a claim-level caption reward, the supported details that the reference does not contain can add to recall only up to the number of reference claims still uncovered, at a discounted weight; "The cap operation restricts residual credit by this bound."[^r6] The mechanism is set out in [[reference-anchored-residual-credit]]. It covers over-selection only among supported extras. An unsupported extra is a precision matter, and the same reward gives it nothing on that side. Whether the bound changes a benchmark ranking like the one above was not tested in that paper.

## Limits

- The benchmark was a single clinical set of 36 vignettes. Whether recall-only scoring changed the ranking of the three models was not reported in the text I read.
- The claim that selecting every option maxes recall is my inference from the metric's definition. It was not measured.
- Precision and F1 are described as reported in a supplement, which I did not read. The point made here rests on the authors' description of why they were added, not on those figures.
- The note covers set-overlap scoring only. Partial credit for ranked lists, or for graded relevance, follows different rules.
- The authors' own remedy (clinician-weighted metrics) is named but not built or tested here.

## Related

- [[weighted-nugget-recall]] — partial credit weighted by the importance of each gold unit, a different correction for the same question of how much a partial answer is worth
- [[answer-option-surface-cue]] — a multiple-choice score can be beaten without the tested knowledge; a recall-only score is exposed to a similar move, by listing options
- [[neurosymbolic-text-to-logic-retrieval]] — the ranked-retrieval case of the same blind spot: its evaluation reports precision at k beside recall for a joint-embedding baseline
- [[max-over-references-scoring]] — the other one-sided multi-answer score: a best-match rule over gold answers, which temporal QA benchmarks use and which overstates multi-answer performance; the set-level and answer-F1 measures are its stricter replacements

[^r1]: arxiv-2512-22966 — "calculated as the proportion of correct predictions"
[^r2]: arxiv-2512-22966 — "the degree of overlap between predicted multiple-choice answers and ground truth"
[^r3]: arxiv-2512-22966 — "does not capture several clinically important dimensions"
[^r4]: arxiv-2512-22966 — "To partially separate omission-driven versus"
[^r5]: arxiv-2512-22966 — "clinician-weighted or safety-oriented metrics"
[^r6]: doi-10-48550-arxiv-2607-05150 — "The cap operation restricts residual credit by this bound"
[^r7]: arxiv-2512-14102 — "which are usually evaluated only in terms of recall (R@k)"
[^r8]: arxiv-2512-14102 — "indicating that they tend to retrieve false positives and thus non-relevant"
