---
description: "Evidence falls short in three distinct ways: part of the question is uncovered, passages are on topic with no answer span, or the needed facts sit across passages none of which suffices alone."
aliases: ["failure regimes of insufficient evidence", "missing-coverage, topical-but-answerless and cross-passage insufficiency", "three ways evidence falls short"]
sources: ["doi-10-48550-arxiv-2609-37469"]
---
# Evidence insufficiency regimes

Insufficient evidence is not one thing. Retrieved passages can fail a question in three ways that a single relevance or confidence signal does not separate, and the paper names each regime and builds a separate reader for it.[^c1]

The first regime is missing coverage. "A set of passages can omit support for one part of the question, even while its remaining passages are relevant."[^c2] The passages are on topic, but one component the question asks for has no support anywhere in the set. Substitution (a required passage swapped for a distractor) and deletion (a required passage removed) make this regime visible. The content reader targets it by splitting the question into overlapping windows and checking that each window is matched by one source.

The second regime is topical but answerless. "Passages can be on topic but offer no answer-bearing span."[^c3] Here the passages share the question's vocabulary and subject, yet no span answers it. Question swaps isolate this case, where the evidence is fixed and the question is changed to one the passage does not answer. The span reader targets it by asking whether an extractive QA model prefers some passage span to its no-answer option.

The third regime is cross-passage. "The needed facts can be spread across passages," so no single passage is sufficient but their combination is.[^c4] The paper places this regime in the multi-hop settings it tests (HotpotQA, IIRC, MuSiQue). The latent reader targets it by reading the top passages together in one forward pass of a small frozen model.

The three regimes overlap. In the paper's words, "regimes overlap, and together they explain why the best single relevance" signal differs from dataset to dataset.[^c5] The paper's ablation supports the split in a weak form: "Table 6 evaluates every subset of the three readers," and each reader leads on the regime it targets. Content coverage is strongest on the evidence-removal sets, the span reader on IIRC, and the latent reader on SQuAD 2.0, whose authored near-misses reuse the passage vocabulary.[^c6] Removing any one reader lowers the average, "to 0.817 without latent, 0.799 without span, and 0.779 without content."[^c7] A deployed scorer cannot tell which regime a record comes from, which is the authors' reason for summing all three.[^c8]

## Why the split matters

A per-passage relevance grade sees only the first two regimes at best: it can say a passage is about the question, but it cannot see that the question's second part is uncovered, and it cannot see facts that only combine across passages. The paper's own relevance baselines (UPR, RAGAS, CRAG) are per-passage judges, and the authors note that "a relevant passage can omit the fact" the answer needs.[^c9] A span detector, in turn, sees answer-like text even when the answer is missing, which is why it fails on NeoQA's deleted-fact sets, where the surviving news still has plausible spans.[^c10]

## Limits

The taxonomy is the authors' construction, motivated by the three ways their contrasts were built. Its completeness is not shown: "the regimes overlap," and no other failure type is tested. Real retrieval is evaluated only in aggregate across five datasets, not split by regime, so the regimes are not shown to account for real retriever failures.

The per-regime attribution rests on one reader per regime, each a different model family (a token-level window matcher, a 125M extractive QA model, a frozen 1.5B LM). A regime's reader leading does not show that the regime is the cause of the failure; it shows only that the reader is sensitive to that kind of contrast. The latent reader also sees only five passages, so its cross-passage regime is tested with a fixed cap.

My inference, not the paper's: a generator that is shown a set in the cross-passage regime may fail for a reason the generator's own confidence cannot expose, which matches the paper's point that generators stay confident. The paper does not test generators on the three regimes separately.

## Related

- [[pre-generation-evidence-sufficiency]] — the scorer that uses one reader per regime and sums them
- [[set-level-selection-over-relevance]] — choosing evidence as a set can score coverage and non-redundancy that per-item relevance cannot see; the cross-passage regime is the same blind spot
- [[retrieval-utilization-gap]] — a different split of failure, into evidence never retrieved versus evidence retrieved but misused
- [[literal-match-dependence]] — evidence found by literal word overlap, which is the cue the topical-but-answerless regime exploits
- [[relevance-completeness-divergence]] — topical relevance does not track completeness, the same dissociation seen in a human rating

[^c1]: doi-10-48550-arxiv-2609-37469 — "The resulting contrasts show three distinct ways evidence can be insufficient"
[^c2]: doi-10-48550-arxiv-2609-37469 — "a set of passages can omit support for one part of the question"
[^c3]: doi-10-48550-arxiv-2609-37469 — "passages can be on topic but offer no answer-bearing span"
[^c4]: doi-10-48550-arxiv-2609-37469 — "the needed facts can be spread across"
[^c5]: doi-10-48550-arxiv-2609-37469 — "regimes overlap, and together they explain why the best single relevance"
[^c6]: doi-10-48550-arxiv-2609-37469 — "Table 6 evaluates every subset of the three readers"
[^c7]: doi-10-48550-arxiv-2609-37469 — "to 0.817 without latent, 0.799 without span, and 0.779 without content"
[^c8]: doi-10-48550-arxiv-2609-37469 — "A deployed scorer cannot tell which contrast"
[^c9]: doi-10-48550-arxiv-2609-37469 — "a relevant passage can omit the fact"
[^c10]: doi-10-48550-arxiv-2609-37469 — "still contain plausible answer spans after the"
