---
description: "Insufficient counterparts built by deletion, substitution or question swap carry surface cues such as passage count and word overlap that predict the label without testing sufficiency."
aliases: ["residual cues in paired negatives", "construction artifacts in sufficiency contrasts", "cue audit for paired negatives"]
sources: ["doi-10-48550-arxiv-2609-37469"]
---
# Construction cue leakage in contrast sets

A benchmark that tests whether evidence is sufficient compares a sufficient set with an insufficient counterpart. Whatever else differs between the two sides becomes a cue a scorer can use in place of sufficiency. The paper states the mechanism directly: a benchmark "compares passages that support an answer with passages that do not, so anything else that differs between the two sides becomes a cue a scorer can use in place of sufficiency."[^c1] The leakage is therefore a property of how the insufficient side was built, not of the scorer alone.

Each of the three constructions leaks in its own way. Deletion removes a needed passage, which shrinks the evidence set, so passage count can carry the label: "Passage count alone scores 0.891 on IIRC."[^c2] Substitution keeps the count fixed but chooses a distractor that usually shares fewer of the question's important words with it than the passage it replaces. On HotpotQA, minimum IDF coverage (the lowest share of the question's IDF-weighted words found in any single passage) alone scores 0.941 at zero added passages.[^c3] Question swap keeps the evidence fixed and changes the question. On SQuAD 2.0, counting how many of the question's words appear in the passage separates answerable from unrelated questions almost perfectly (0.993), but "scores only 0.573 against the unanswerable questions" that the annotators wrote about each passage.[^c4]

The cues do not always survive a control. The paper adds the same 5 to 20 passages to both sides of each pair and reorders the full sets with BM25. "Adding passages hides some cues but not others": with 20 additions, an added passage often has the lowest coverage on both sides, so "The two sides tie on this cue in 97.9%" of pairs and the minimum-IDF score falls to 0.510.[^c5] A classifier that reads only the passages does not fall to chance, however. "The evidence-only classifier still scores 0.743," showing that it uses differences in the passages beyond the controlled cue.[^c6]

The paper's construction-level audit is what makes the leak visible. The paper reads its own table this way: "Table 2 shows how often each cue gives the sufficient side of a pair the higher score."[^c7] The audit is a list of cues the authors thought to check: passage count, minimum IDF coverage, a question-only classifier, an evidence-only classifier, and subsets where one cue is held equal.

## Limits

The audit checks a finite set of cues. Its clean result on one cue is not a clean result on the benchmark: the evidence-only classifier still scores well above chance after controls, so the paper has not shown that no other cue remains. A cue that the audit did not name stays untested.

The controls are one cue at a time. The paper's subset check holds one cue fixed and reports the scorers' accuracy within that subset, but it does not hold several cues fixed at once, so a combination of cues can still leak.

The effect of a control depends on the dataset. Minimum IDF coverage leaks strongly on HotpotQA, passage count on IIRC, and question wording on SQuAD 2.0; a different benchmark may leak through a cue the authors did not measure. The absence of a detected cue is evidence only for the cues checked.

My inference, not the paper's: the same leakage applies to any paired benchmark where the negative is produced by a rule (delete, swap, substitute), not by a human who must write a plausible near-miss. The SQuAD 2.0 contrast fits this reading: the same word-overlap cue scores 0.993 against unrelated questions and 0.573 against the annotators' near-misses, but one pair of datasets does not prove the pattern for others.

## Related

- [[clever-hans-effect]] — the scorer's reliance on a correlated cue; this note is the benchmark-side origin of such a cue
- [[provenance-cue-leakage]] — a label predicted by who produced the example, another construction-side shortcut
- [[answer-option-surface-cue]] — the keyed option of a multiple-choice item beaten by its surface form
- [[counterfactual-hard-negative]] — a contrast pair meant to teach evidence over language priors, which this note says can teach a surface cue instead when built by a rule
- [[pre-generation-evidence-sufficiency]] — the scorer whose evaluation this audit checks
- [[evidence-insufficiency-regimes]] — the three ways evidence falls short that each construction targets

[^c1]: doi-10-48550-arxiv-2609-37469 — "compares passages that support an answer with passages that"
[^c2]: doi-10-48550-arxiv-2609-37469 — "Passage count alone scores 0.891 on IIRC"
[^c3]: doi-10-48550-arxiv-2609-37469 — "the distractor usually"
[^c4]: doi-10-48550-arxiv-2609-37469 — "scores only 0.573 against the unanswerable questions"
[^c5]: doi-10-48550-arxiv-2609-37469 — "Adding passages hides some cues but not others"
[^c6]: doi-10-48550-arxiv-2609-37469 — "The evidence-only classifier still scores 0.743"
[^c7]: doi-10-48550-arxiv-2609-37469 — "Table 2 shows how often each cue gives the sufficient side of a pair the higher"
