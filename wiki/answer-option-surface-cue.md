---
description: "The keyed option of a multiple-choice item can be told apart by its length and qualifier words, so a test-taker can beat chance by reading the options alone, without the knowledge tested."
aliases: ["length bias in multiple-choice items", "qualifier word bias", "exploitable option pattern"]
sources: ["arxiv-2601-02158"]
---
# Answer-option surface cue

A multiple-choice item can give away its key without the question being answered. The keyed option may differ from the distractors in features unrelated to content, such as its length or the qualifier words it carries. When such differences arise in writing rather than by design, a test-taker can pick the answer from the options alone.

FormationEval, a 505-question benchmark on petroleum geoscience, measured two such cues in its own generated items before release. The first is length. Before repair, "Correct answers were uniquely longest in over 55% of questions" against an expected 25% for four options, and correct options averaged 86.6 characters against 69.8 for distractors.[^c1][^c2] The authors trace part of this to the generation step itself: the few-shot examples had been wrong in the same direction, since "two of three examples had the longest option as the correct answer",[^c3] while the prompt asked the model to "Balance answer options in length and structure".[^c4]

The second cue is qualifier words. Absolute words "appeared only in distractors (49 instances, 0% correct rate)",[^c5] while hedges such as "may" appeared only in correct answers, 13 instances at a 100% correct rate.[^c6]

Repair moved the cue rather than removing it. Mitigation expanded 136 distractors with technical context to reduce the length imbalance,[^c7] and the uniquely-longest rate fell to 43.2%, with correct options averaging 87 characters against 74 for distractors.[^c8] Each absolute word was replaced with synonyms, but "The absolute-word synonyms all have 0% correct rate", so the marker became a class of words rather than one word.[^c9] "Length bias is still above the 25% baseline."[^c10]

For the answerer, the arithmetic is the point. At 43.2%, a rule that picks the uniquely longest option is right on those items less than half the time, and the paper concludes that "a length-based strategy would fail more often than it succeeds."[^c11] My reading is that this is still above the 25% a random guess gives on the same four-way items, which is why the paper says the patterns "could be exploited well above random chance."[^c12] The cue is therefore a route to a correct key that bypasses the content the item was written to test.

## Limits

- The paper does not report the accuracy a test-taker would reach by using these cues. "Could be exploited" is the authors' inference from the rates; in the sections I read, no exploit was run against a model or a human.
- The cue was measured on one benchmark, produced by one generation pipeline and reviewed by one domain expert. Whether other multiple-choice sets carry the same cues is not tested here.
- The authors argue that the residual bias should not change model comparisons, because "any bias-based advantage would affect all" models alike.[^c13] That is an assumption. A model that reads surface form more heavily could gain more from the cue, and the paper does not test this.
- The absolute-word counts are small (the synonym counts are in the single or low double digits), so the 0% rates are suggestive rather than tight estimates.
- The cue is a property of this item pool. It says nothing about how often a length or qualifier pattern appears in multiple-choice items written with other procedures.

## Related

- [[item-writing-guidelines]] — the rule set that asks for homogeneous, equal-length, plausible distractors; this cue is what can remain when such a rule is only partly met
- [[llm-judge-biases]] — verbosity bias: a judge also favors the longer answer, so a length cue reaches the grader as well as the test-taker
- [[option-matching-shortcut]] — options change how a reasoning model answers, by matching candidates rather than by cues in their wording
- [[mcq-answer-position-bias]] — another systematic bias of the same kind of generation step, in where the key is placed
- [[distractor-strength-reward-signal]] — whether wrong options are attractive decides whether a reward trains reasoning or guessing; a surface cue lets a guesser avoid that attraction

[^c1]: arxiv-2601-02158 — "Correct answers were uniquely longest in over 55% of questions"
[^c2]: arxiv-2601-02158 — "averaging 86.6 characters versus 69.8 for distractors"
[^c3]: arxiv-2601-02158 — "two of three examples had the longest option as the correct answer"
[^c4]: arxiv-2601-02158 — "Balance answer options in length and structure"
[^c5]: arxiv-2601-02158 — "appeared only in distractors (49 instances, 0% correct rate)"
[^c6]: arxiv-2601-02158 — "answers (13 instances, 100% correct rate)"
[^c7]: arxiv-2601-02158 — "Mitigation involved expanding 136 distractors with technical context to reduce length imbalance"
[^c8]: arxiv-2601-02158 — "After mitigation, correct answers average 87 characters versus 74"
[^c9]: arxiv-2601-02158 — "The absolute-word synonyms all have 0% correct rate"
[^c10]: arxiv-2601-02158 — "Length bias is still above the 25% baseline."
[^c11]: arxiv-2601-02158 — "a length-based strategy would fail more often than it succeeds"
[^c12]: arxiv-2601-02158 — "Combined, these patterns could be exploited well above random chance."
[^c13]: arxiv-2601-02158 — "any bias-based advantage would affect all"
