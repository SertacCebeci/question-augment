---
description: "Context selects the category a decision is filed under, and the category sets feature weights; 12 LLMs match its choice-level signatures, strongest where categorization is ambiguous."
aliases: ["problem categorization", "hedonic-functional categorization", "category-selected attention", "categorization account of context effects"]
sources: ["doi-10-48550-arxiv-2609-22225"]
---
# Problem categorization and context effects

In Bordalo et al.'s cognitive account of choice, a decision is not evaluated under one fixed set of weights. The decision-maker first finds the category the present problem belongs to: context features "time to find the most similar category of choices" made in the past.[^c1] The selected category then sets the weights on the features. In the paper's notation the attention weights are "context-dependent attention weights on price and quality", and they "are pinned down in the mental representation of a decision".[^c2] The same two jars can therefore be chosen differently under a hedonic category, which weights quality, and under a functional one, which weights price.

The mechanism selects its category by similarity to memory. A problem is filed under "category from memory that is most contextually similar to the current problem".[^c3] Memory here means the frequencies of past hedonic and functional problems. Raising the hedonic share "lowers the threshold for categorizing a current problem as hedonic".[^c18] A context that has been hedonic more often therefore tilts the next problem toward the hedonic category.

The paper tests this in LLMs with a 140,000-trial product choice set, using hedonic and functional cues in the prompt. It does not test the mechanism directly. It checks three signatures the mechanism predicts. The first is in-context composition: prepending eight examples, "increasing nhed from zero to eight raises the average premium choice rate from 49% to 74%".[^c4] The second is product-level: "cue effects on choices across LLMs peak for" products of midrange hedonic-ness and shrink at both ends, where one category clearly wins.[^c5] The third is ambiguity: the cue effect is largest "when decisions are ambiguous, irrespective of category taxonomy".[^c6] The paper reports that "We find evidence of all three" signatures across models.[^c7]

Ambiguity is a proxy, not a measured category. The paper takes "the decision certainty of" each model under a neutral cue as the measure.[^c8] Across models, "effects on choice rates are negatively associated" with that certainty.[^c9] The authors' reading is that when a model is uncertain how to categorize a problem, "a cue provides a greater update to its posterior beliefs".[^c10]

The headline is narrower than the mechanism. Context "induces human-like shifts in choice and problem categorization", but it "does not reliably reweight attention between features like price and quality".[^c11] So the categorization signatures hold while the attention-weight part of the theory fails; that second half is its own note, [[feature-sensitivity-reweighting]].

## Limits

- The categorization is inferred from choices, and the paper says so: "do not imply shared mechanisms".[^c12] Similar behaviour under a categorization story does not show that the model categorizes; a different process could produce the same three signatures. The authors name no competing process they rule out, and "we do not disambiguate between competing explanations in this work".[^c13]
- The in-context examples stand in for memory, and the paper says they are "not the same as training data, and both may fundamentally differ from human memories".[^c14]
- Product hedonic-ness is a single judge's rating: the paper uses a GPT 5.4 judge, and "judge to rate each product" from 0 to 100.[^c15] The midrange result depends on that ordering. The authors audited the scores by hand, but the audit does not test whether a different judge would order the products the same way.
- The ambiguity proxy is the model's own certainty on the neutral prompt. A model that is less certain about everything would show the same negative association without any categorization step. That is my inference; the paper does not test it.
- One setting only: "We test one canonical economic setting: binary choice between" standard and premium products.[^c16] Whether the signatures survive other decision types is not shown.
- The paper sets the categorization account against bounded cognition. If limited attention drove context sensitivity, more capable models should show less of it. The paper finds that scale and reasoning "do not consistently attenuate context effects on choices".[^c17] That comparison rests on the same 12 models and one task, so it does not rule out a bounded-attention account; it shows that the simple form of that account fails here.

## Related

- [[feature-sensitivity-reweighting]] — the attention-weight half of the same theory; the paper finds it fails in most model-cue combinations while the categorization signatures hold.
- [[bounded-rationality]] — the bounded-cognition family the paper sets against this account. That note is about Simon's satisficing rule, so the link is to the family of explanations, not to a specific model of attention.
- [[context-sensitivity-fingerprint]] — the same phrase for a different object: sensitivity of LLM stereotype output to prompt context, not choice categorization.

[^c1]: doi-10-48550-arxiv-2609-22225 — "time to find the most similar category of choices"
[^c2]: doi-10-48550-arxiv-2609-22225 — "are pinned down in the mental representation of a decision"
[^c3]: doi-10-48550-arxiv-2609-22225 — "category from memory that is most contextually similar to the current problem"
[^c4]: doi-10-48550-arxiv-2609-22225 — "increasing nhed from zero to eight raises the average premium choice rate from 49% to 74%"
[^c5]: doi-10-48550-arxiv-2609-22225 — "cue effects on choices across LLMs peak for"
[^c6]: doi-10-48550-arxiv-2609-22225 — "when decisions are ambiguous, irrespective of category taxonomy"
[^c7]: doi-10-48550-arxiv-2609-22225 — "We find evidence of all three"
[^c8]: doi-10-48550-arxiv-2609-22225 — "We proxy categorization ambiguity with the decision certainty of"
[^c9]: doi-10-48550-arxiv-2609-22225 — "effects on choice rates are negatively associated"
[^c10]: doi-10-48550-arxiv-2609-22225 — "to categorize a problem, a cue provides a greater update to its posterior beliefs"
[^c11]: doi-10-48550-arxiv-2609-22225 — "context induces human-like shifts in choice and"
[^c12]: doi-10-48550-arxiv-2609-22225 — "do not imply shared mechanisms"
[^c13]: doi-10-48550-arxiv-2609-22225 — "we do not disambiguate between competing explanations in this work"
[^c14]: doi-10-48550-arxiv-2609-22225 — "not the same as training data, and both may fundamentally differ from human memories"
[^c15]: doi-10-48550-arxiv-2609-22225 — "judge to rate each product"
[^c16]: doi-10-48550-arxiv-2609-22225 — "We test one canonical economic setting: binary choice between"
[^c17]: doi-10-48550-arxiv-2609-22225 — "do not consistently attenuate context effects on choices"
[^c18]: doi-10-48550-arxiv-2609-22225 — "Raising Fhed /Ffun lowers the threshold for categorizing a current problem as hedonic"
