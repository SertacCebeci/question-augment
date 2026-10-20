---
description: "A benchmark can be made hard by sampling items a reference model fails; the hardness then belongs partly to the sampler, so cross-model scores on that set are confounded."
aliases: ["difficulty-stratified sampling", "adversarial item selection", "difficulty enrichment of a benchmark"]
sources: ["doi-10-48550-arxiv-2604-27470"]
---
# Difficulty-enriched item sampling

A benchmark can be made hard without writing harder items. Draw a large pool, rate each item by how a reference model handles it, and sample the final set so that the items that reference model fails are over-represented. HealthBench Professional did this for clinician chats. Physicians wrote 15,079 candidate conversations, and "each example was rated for difficulty against recent OpenAI frontier models".[^c1] The rating came from the physician's Likert score of the model's final response. The authors used "two difficulty tags", typical and difficult, with difficult meaning the lowest scores.[^c2]

The sampler then took difficulty as its primary tag. The released set was built to "increase the weight of hard cases for our current frontier models by roughly 3.5x relative to the underlying task distribution".[^c3] In the good-faith pool the enrichment was stronger: "difficult tasks were enriched by about 8x".[^c4] The stated purpose is to keep the benchmark informative as models improve, "to enable continued measurement of progress".[^c5]

The mechanism is the point of the note. Difficulty here is a property of a pair, an item and a model, not of the item alone. The sampler's signal is one model family's failures, so the selected set is weighted toward the failure modes of that family. Any later comparison on the set inherits that weighting. The same pattern appears in [[model-dependent-benchmark-difficulty]], where which game is hardest depends on the model tested; here the dependence was written into the sample before any other model was run.

The effect is visible in the results. On the hardest red-teaming slice, the system under test "scored 55.8 versus 30.0 for physicians" and "beat every other model, including GPT-5.4".[^c6] The authors read this as evidence that gains "appear when cases are adversarial or" failure-prone.[^c7] That reading is partly built in: the slice was selected for cases the reference model fails, so a gap on it is in part a gap the selection was designed to produce. This is my inference, not a result the paper states.

## Limits

- The difficulty label is a snapshot. The authors say it "provides a snapshot in time for particular" OpenAI models, "rather than a canonical difficulty for all models".[^c8]
- The confound is acknowledged, not removed: "This partially confounds comparisons across models".[^c9] The authors' answer is that OpenAI models "perform well even despite this selection pressure", which says the top system is strong on the hard slice, not that the slice is neutral for other models.
- Transfer to other models is asserted from examples, not isolated. The paper states that "examples difficult for our models were also difficult for other models" and that "models from other providers also exhibited similar failure modes on these examples".[^c10] In the text I read, I did not find a comparison against an unselected sample of the same pool, so the size of the confound is not measured.
- Labels are physician judgments, and they are not always shared. "In some cases, when authoring physicians flagged possible flaws, other physicians did not agree".[^c11] Difficulty tags inherit that disagreement.
- One clinical domain, one model family as the selector. Whether the mechanism changes a question's answerability or only a benchmark's hardness is not tested here.

## Related

- [[model-dependent-benchmark-difficulty]] — the same dependence of difficulty on the model, seen there in a negotiation benchmark's game ranking.
- [[llm-red-teaming]] — red-teaming searches for failures directly; sampling filters a fixed pool. The shared worry is a blind spot inherited from a shared model family, which that note states for red-teamers and which applies here because the selector and the system under test are both OpenAI models (my inference).

[^c1]: doi-10-48550-arxiv-2604-27470 — "Each example was rated for difficulty against recent OpenAI frontier"
[^c2]: doi-10-48550-arxiv-2604-27470 — "We used two difficulty tags"
[^c3]: doi-10-48550-arxiv-2604-27470 — "increasing the weight of hard cases for our current frontier models by roughly 3.5x relative to the underlying task distribution"
[^c4]: doi-10-48550-arxiv-2604-27470 — "For good faith tasks in particular, difficult tasks were enriched by about 8x"
[^c5]: doi-10-48550-arxiv-2604-27470 — "to enable continued measurement of progress"
[^c6]: doi-10-48550-arxiv-2604-27470 — "beat every other model, including GPT-5.4"
[^c7]: doi-10-48550-arxiv-2604-27470 — "the strongest improvements in ChatGPT for Clinicians appear when cases are adversarial or"
[^c8]: doi-10-48550-arxiv-2604-27470 — "this difficulty rating provides a snapshot in time for particular"
[^c9]: doi-10-48550-arxiv-2604-27470 — "This partially confounds comparisons across models"
[^c10]: doi-10-48550-arxiv-2604-27470 — "examples difficult for our models were also difficult for other models"
[^c11]: doi-10-48550-arxiv-2604-27470 — "In some cases, when authoring physicians flagged possible flaws, other physicians did not agree"
