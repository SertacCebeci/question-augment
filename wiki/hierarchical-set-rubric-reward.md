---
description: "A set-level rubric is judged once on the whole selected set, a document-level rubric is judged per document and averaged over the set, and both enter one weighted reward."
aliases: ["hierarchical reward aggregation", "set-level and document-level rubric reward", "rubric-weighted hierarchical aggregation"]
sources: ["doi-10-48550-arxiv-2608-03527"]
---
# Hierarchical set rubric reward

A reward for a selected set can be built from two kinds of criterion that are scored at different grain. A set-level criterion is one judgment about the whole set. A document-level criterion is judged for each member and then averaged. The paper combines both in one weighted average. Each rubric carries a weight from 1 to 5, and the reward for a selected document set D is the weighted sum of the set-level scores and the averaged document-level scores, divided by the total weight.[^c1]

The set-level term is one call: an LLM judge gives a normalized score between 0 and 1, and for a set-level rubric it "scores whether the selected documents D collectively satisfy the query requirements."[^c2] The document-level term is a mean: the judge scores each selected document against the rubric, and "average the scores over the selected set."[^c3] So a document-level criterion such as source authority contributes once per member, while a set-level criterion such as conciseness contributes once for the set. The reward is then used in GRPO; if the output cannot be parsed as a list of document IDs, the reward is set to −1 instead.[^c7]

The paper also gates the document-level criteria. Source authority and timeliness are "defined only for" relevant documents, so "an irrelevant document does not satisfy the source authority rubric even if" it comes from an authoritative source.[^c4][^c5] A document that is off topic cannot earn credit for being authoritative. This is written into the rubric definition, which the judge reads; the reward formula itself does not multiply the terms.

The structure is a response to a flat sum. In a flat sum, each criterion adds credit whatever condition licenses it, which is the failure described in [[false-credit-propagation]]. Here the licensing condition, relevance, is part of the definition of the document-level criteria. The set-level criteria are the ones that cannot be assigned to any one document, and they are where the selection objective of [[set-level-selection-over-relevance]] enters the reward.

## Limits

- The paper does not ablate the hierarchy. Its ablations change the training stage and the SFT labels. No run I read replaces the two-level reward by one flat average over all rubrics, so the claim that the hierarchy helps is not measured here.
- The gate depends on the judge deciding relevance first. The paper gives no check of how often that judgment is wrong, and the reward inherits any error in it.
- Rubric weights are produced by the rubric generator, a GPT-5.1 call. I found no sensitivity analysis over the weights in the sections I read, and no human check of the judge's scores (my reading).
- Averaging gives each document an equal vote regardless of its rank or its share of the set. Whether this rewards padding a set with many weak but on-topic documents is not discussed (my inference).
- The reward is computed for one query at a time, with the judge seeing the candidate list. Its cost is one or more LLM calls per rollout, which the authors name as a limit: "The construction of rubric-based rewards relies on GPT-5.1,".[^c6]

## Related

- [[set-level-selection-over-relevance]] — the selection objective this reward scores; this note is only the aggregation.
- [[false-credit-propagation]] — a flat rubric sum counts a criterion whether or not its licensing condition holds; the relevance gate here is the same kind of condition, written into the rubric.
- [[within-group-ordinal-utility-aggregation]] — another way to combine rubric criteria, by within-group ordering rather than by set and item scores.
- [[weight-stratified-criterion-pass-rate]] — shows that pooled rubric rates can hide the split by weight; this paper's 1-to-5 weights are not analysed that way.
- [[authority-signals-framework]] — a taxonomy of what makes a cited source authoritative, which is the kind of judgment the document-level authority rubric asks for.

[^c1]: doi-10-48550-arxiv-2608-03527 — "aggregation with rubric weights:"
[^c2]: doi-10-48550-arxiv-2608-03527 — "scores whether the selected documents D collectively satisfy the query requirements."
[^c3]: doi-10-48550-arxiv-2608-03527 — "average the scores over the selected set:"
[^c4]: doi-10-48550-arxiv-2608-03527 — "Both dimensions are defined only for"
[^c5]: doi-10-48550-arxiv-2608-03527 — "does not satisfy the source authority rubric even if"
[^c6]: doi-10-48550-arxiv-2608-03527 — "The construction of rubric-based rewards relies on GPT-5.1,"
[^c7]: doi-10-48550-arxiv-2608-03527 — "final reward is set to −1"
