---
description: "Finding facts that exist and refusing facts that do not are separate capabilities: a model can score high on one and fabricate often, so each needs its own measure."
aliases: ["grounding versus hallucination resistance", "grounding versus fabrication", "hallucination resistance"]
sources: ["arxiv-2601-08847"]
---
# Grounding-fabrication dissociation

A model can be good at answering from a document and bad at declining when the document has no answer. RIKER measures these as two separate quantities. Grounding is accuracy on single-document questions whose answers are present: "Grounding failures indicate the model could not locate or correctly extract information from documents that definitively contain the answer".[^c1] Fabrication is the error rate on probes whose answer is absent, where "any specific answer constitutes unambiguous fabrication".[^c2]

The probe is built so that a refusal is clearly the right reply. The entity names in the L11 probe "are drawn from unused portions of the entity pool, ensuring they are plausible but definitively absent".[^c3] The only correct response is "Unknown" or an equivalent. Because the entity is absent, any specific answer cannot have come from the corpus.

The central result is that the two do not track each other. "strong grounding performance does not predict hallucination resistance".[^c4] The example pairs two models: "DeepSeek-V3.1 achieves 95.1% grounding accuracy" and yet "exhibits a 17.3% fabrication rate", against a much lower rate for GLM-4.5. The abstract puts the same point as "models excelling at finding facts that exist may still fabricate facts that do not".[^c5]

The distinction matters for how one asks about a model's reliability. A single accuracy number averages over both behaviours and can hide either. The paper concludes that "Applications requiring high factual reliability must evaluate both capabilities independently".[^c6] The paper's broader taxonomy also keeps "Faithfulness", the colloquial sense of any confidently wrong answer where correct information existed, separate from both, which is a third and broader measure.[^c7]

## Limits

The fabrication probes are the easiest form of the failure: the entity is absent by construction and the correct reply is one word. Fabrication under subtler conditions, where the absent item is plausibly implied, is not what was measured. The paper names this gap itself: "Instead of single-answer questions (entity name or amount value)" a finer test would use lists of items.[^c8]

The dissociation rests on a small set of model pairs in one enterprise corpus. The "eight times higher" comparison is a ratio of two numbers, not a fitted relation, and no mechanism is isolated that explains why grounding and refusal come apart.

The paper does not vary prompt pressure in the passages read, so whether the rates move under it is untested here; that gap is my inference. The wiki's [[non-monotonic-prompt-pressure-hallucination]] note reports that such pressure does change fabrication in a different setting.

## Related

- [[calibrated-accuracy]] — one score that puts grounding and absent-persona abstention on a single axis; by the dissociation above, such a merge can hide one of the two, which is my inference.
- [[abstention]] — declining when the answer is absent is the behaviour the fabrication probe scores.
- [[knowledge-verbalization-dissociation]] — another case where what a model holds internally and what it says come apart.
- [[non-monotonic-prompt-pressure-hallucination]] — fabrication rate changing with prompt pressure, an axis the RIKER probe holds fixed.

[^c1]: arxiv-2601-08847 — "Grounding failures indicate the model could not locate or correctly extract information from documents that definitively contain the answer"
[^c2]: arxiv-2601-08847 — "any specific answer constitutes unambiguous fabrication"
[^c3]: arxiv-2601-08847 — "ensuring they are plausible but definitively absent"
[^c4]: arxiv-2601-08847 — "strong grounding performance does not predict hallucination resistance"
[^c5]: arxiv-2601-08847 — "models excelling at finding facts that exist may still fabricate facts that do not"
[^c6]: arxiv-2601-08847 — "must evaluate both capabilities independently"
[^c7]: arxiv-2601-08847 — "Faithfulness aligns with the colloquial enterprise definition of"
[^c8]: arxiv-2601-08847 — "Instead of single-answer questions (entity name or amount value)"
