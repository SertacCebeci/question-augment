---
description: "The same source share reads differently by word class, so per-part-of-speech means of those shares give hallucination features that a per-token score cannot."
aliases: ["syntax-aware attribution aggregation", "POS-conditioned source profile", "part-of-speech attribution profile"]
sources: ["arxiv-2512-07515"]
---
# Part-of-speech stratified source attribution

Once each generated token's probability has been split into source shares (see [[residual-probability-decomposition]]), the shares still lack a reference point. A large share from one source is not, by itself, a sign of anything. The paper's example makes the point: "high FFN contribution might be normal for a function word but suspicious for a proper noun."[^p1] The same number means different things depending on the word class of the token that carries it. That is the concept this note holds: conditioning per-token source shares on a syntactic category before reading them.

The mechanism has three steps. First, each generated token gets a part-of-speech tag from spaCy. Second, sub-word tokens inherit the tag of their word, so a noun split into pieces counts as a noun in every piece; the paper's rule is that "generated sub-word tokens inherit the POS tag of their" parent word.[^p2] Third, for each tag τ the feature is the mean of the seven-dimensional share vector over the tokens carrying that tag, and the classifier's input is the concatenation of these per-tag means: "is the concatenation of these POS-specific vectors."[^p3] The vector therefore has seven entries for every tag in the tag set.

The aggregation is what gives the paper its features. A per-token score cannot separate a function word from a named entity; a per-tag mean can, because the tag is kept. The paper contrasts this with named-entity recognition, which is "limited to specific entity" types, while POS tagging "covers all tokens," including numerals and adpositions.[^p4][^p5] The paper's example of a pattern worth reading is "low RAG contribution on nouns," given in the introduction as indicative of hallucination.[^p6]

The paper's classifier does not treat one profile as universal. Its feature importances point at different cells in different models: "While RAG_NOUN dominates in Llama2 (Figure 3) and Mistral," the excerpt says, "Llama3-8B relies heavily on" relational structures, with adpositions ranking highest.[^p7] The LayerNorm contribution to numerals is a hallucination signal in Llama2-7B, but "this pattern reverses in Llama2-13B," where higher values track factuality.[^p8] From this the authors conclude that the signals call for "a learnable approach rather than static heuristics."[^p9]

## Limits

- The tagger is external. The paper says that "our feature engineering depends on external linguistic tools (POS taggers)," which may limit generalization to domains such as code, where standard syntax is less defined.[^p10] Its future-work list names the same gap: "aggregation to non-English and specialized domains."[^p11]
- The signals are model-specific. The paper states that "hallucination signals are model-specific rather than" universal.[^p12] A category-conditioned reading such as "nouns rely on LayerNorm" is therefore a claim to check per model, not a transferable threshold.
- The advantage over entity-based aggregation is asserted, not shown here. The contrast with named-entity recognition is the authors' argument. The excerpt I read contains no ablation that swaps POS tags for entity types and measures the difference.
- The per-tag mean discards order and position. Whether one anomalous token inside a long noun span is diluted by its neighbours is not addressed. This is my inference from the formula, not a tested result.
- Tag inheritance is one resolution of the mismatch between sub-word tokens and whole-word tags. The text does not compare alternatives, so its effect on the features is unknown. My inference.
- The importance scores (SHAP) describe what the paper's classifier uses. A category that matters to a detector is not thereby shown to be a mechanism inside the model.

## Related

- [[residual-probability-decomposition]] — the seven per-token shares that this aggregation averages
- [[parametric-suppression]] — the FFN-overwrite account; a per-category reading is one way to ask whether suppression concentrates in particular word classes, which this note does not test
- [[single-pass-internal-signal-detector]] — one-pass detectors fed with internal signals; this aggregates those signals by syntax before any classifier sees them

[^p1]: arxiv-2512-07515 — "high FFN contribution might be normal for a function word but suspicious for a proper noun"
[^p2]: arxiv-2512-07515 — "generated sub-word tokens inherit the POS tag of their"
[^p3]: arxiv-2512-07515 — "is the concatenation of these POS-specific vectors"
[^p4]: arxiv-2512-07515 — "which is limited to specific entity"
[^p5]: arxiv-2512-07515 — "POS tagging covers all tokens"
[^p6]: arxiv-2512-07515 — "low RAG contribution on nouns"
[^p7]: arxiv-2512-07515 — "While RAG_NOUN dominates in Llama2"
[^p8]: arxiv-2512-07515 — "this pattern reverses in Llama2-13B"
[^p9]: arxiv-2512-07515 — "a learnable approach rather than static heuristics"
[^p10]: arxiv-2512-07515 — "our feature engineering depends on external linguistic tools (POS taggers)"
[^p11]: arxiv-2512-07515 — "aggregation to non-English and specialized domains"
[^p12]: arxiv-2512-07515 — "hallucination signals are model-specific rather than"
