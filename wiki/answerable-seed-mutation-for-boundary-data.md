---
description: "Boundary training cases (clarify, follow up, reject) are made by mutating verified answerable seeds, so the refusal rationale cites the specific missing or vague schema element."
aliases: ["seed mutation", "ambiguity injection", "knowledge-deficit injection", "BAR-SQL data synthesis"]
sources: ["arxiv-2601-10318"]
---
# Answerable-seed mutation for boundary data

Models trained or prompted on ordinary data answer every question. Tian et al. (2026) for enterprise NL2SQL manufacture the missing negative class from the positive one. They start from a verified, unambiguous question–SQL pair (a "seed"). They then damage either the question or the context, and they change the target from SQL to a natural-language reply.

## Mechanism

Three mutations produce the non-SQL targets.

- **Ambiguity injection.** A precise seed query is made vague, for example a named province becomes "northern province" and a date becomes "recently". The target becomes a clarification question.[^c1] The synthesized reasoning cites schema evidence that no field matches "indicators" and that "recently" is not a defined window, so the clarification is justified by a concrete gap.
- **Constraint follow-up.** The query omits a filter that a metric definition in the knowledge graph makes mandatory (the paper's example is a lead metric that requires a car series). The target asks for that one parameter.
- **Knowledge rejection.** The context is tampered with: a dimension definition is deleted from the schema, or the query names an undefined metric. The target is a refusal.[^c2] The reasoning "explicitly documents the search-and-failure process", so the refusal is grounded in a search of the altered context and is not a generic one.[^c3]

Because each case is derived from a seed whose answer is known, the label "this cannot be answered, and here is why" is correct by construction. The case also has a minimal pair, the unmutated seed, for which answering is right. The evaluation set is built the same way, with about half answerable and half boundary cases.[^c4]

## What it was measured to do

Frontier general models fail the boundary categories almost completely. The paper reports that Gemini 3 Pro and DeepSeek-V3.2 "score nearly 0% in ambiguity detection", and describes the failure as forced answering: fabricating columns for dimensions that are missing.[^c5] A small base model had 8.47% average accuracy. After supervised fine-tuning on the mutated corpus it reached 67.55%, with Dimension Rejection still weak at 42.37%.[^c6] Reinforcement learning on top lifted the average "from 67.55% to 91.48%".[^c7] That second stage is a reward with a type-conditional grammar term, which gives full credit when the target and the prediction are both natural language.[^c8] So the data creates the possibility of refusing, and the reward then fixes its precision. The paper does not separate the two effects for the boundary classes alone.

## Limits

- The ablation removes only auxiliary reward terms (grammar, format, structure, length). It has no arm that trains without the mutated boundary cases, so the data's contribution is inferred from the base-to-SFT jump (my inference), which also includes plain domain exposure.
- The benchmark is drawn from the same mutated corpus and the same generator as the training data. Held-out instances still share its mutation types, so transfer to boundary cases that are not of these types, or to real users' vagueness, is untested. The ambiguity here is injected lexically, and real ambiguity may not be.
- The reasoning traces come from a teacher model, so their quality is not independently verified in the text I read.
- One domain (enterprise BI with a metric knowledge graph) and one small model family.
- The 50/50 mix may itself shape the refusal rate. The paper does not vary it.

## Related

- [[text-to-sql-ambiguity-taxonomy]] — kinds of ambiguity the mutations are drawn from or could be extended to
- [[underspecified-question-eager-answering]] — the forced-answering failure this data targets
- [[knowledge-boundary-aware-reward]] — a reward-side treatment of the same answer-or-abstain boundary
- [[abstention]] — the behavior being taught
- [[sql-clause-gated-clarification]] — a clarification decision tied to the query's structure

[^c1]: arxiv-2601-10318 — "precise seed queries are rewritten into ambiguous variants"
[^c2]: arxiv-2601-10318 — "we synthesize rejection data by deliberately introducing knowledge deficits"
[^c3]: arxiv-2601-10318 — "The resulting CoT explicitly documents the search-and-failure process"
[^c4]: arxiv-2601-10318 — "Negative & Interactive Tasks (≈50%)"
[^c5]: arxiv-2601-10318 — "Gemini3Pro and DeepSeek-V3.2 score nearly 0% in ambiguity detection"
[^c6]: arxiv-2601-10318 — "SFT using our synthesized corpus significantly elevates performance to 67.55%"
[^c7]: arxiv-2601-10318 — "from 67.55% to 91.48%"
[^c8]: arxiv-2601-10318 — "The second case assigns full credit"
