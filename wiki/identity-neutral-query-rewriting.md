---
description: "User identity cues in a question skew generated answers while internal factual knowledge stays stable; removing only question-irrelevant identity terms cut identity-dependent bias 57-89%."
aliases: ["identity-robust generation", "IRG", "selective identity neutralization", "personalization bias mitigation"]
sources: ["arxiv-2601-09141", "arxiv-2512-04981", "arxiv-2511-19956"]
---
# Identity-neutral query rewriting

A user's stated identity ("As a high school student...", "I am unemployed...") can change the correctness, utility and safety of an answer to an objective question, although the model's internal knowledge does not change. The remedy tested here is to decide, per identity term, whether the question needs it, strip the ones it does not, answer the neutral question, and only then optionally restore identity as style.

## The mismatch that motivates it

On TruthfulQA with Llama3.3-70B-Instruct, the same question was posed under 18 identities from six categories (education, religion, race, career, age, gender). A probe trained on attention-head activations reached 86-87% accuracy with a coefficient of variation of 0.33% across identities, whereas generation accuracy varied with a CV of 1.12%, differing by up to 3.8%.[^c1] The authors read this as identity cues not distorting the factual representation but influencing decoding, so the fix should control how identity enters generation, not alter the model.[^c2]

## The three stages

1. **Detect and test relevance.** A named-entity model finds identity spans; an LLM runs a counterfactual check: would removing the term change the information required to answer?[^c3]
2. **Neutral generation.** Only terms judged irrelevant are removed (as a clause, or replaced by a word like "individual"); the core answer is generated from this query, so factual, safety-critical and task-essential content is not influenced by spurious cues.[^c4]
3. **Optional personalization** with a check that the final output keeps the neutral content's meaning.

## What was measured

Against vanilla prompting, personalization bias fell by 77%, 89%, 73% and 57% on TruthfulQA, MMLU-Pro, AmbigQA and StrongReject.[^c5] A system instruction telling the model not to use identity (prompt steering) was unstable: it reduced bias by 11%, 73%, 10% on the first three but raised it by 32% on StrongReject.[^c6] The relevance step agreed with humans on 98.8% of 500 inspected TruthfulQA samples.[^c7] Residual bias comes from two errors: a critical identity term wrongly removed, and a non-critical one kept because it is topically related to the question.[^c8]

## Why it matters for asking and answering

My inference: a question carries two kinds of information, what must be known to answer and who is asking, and answer quality is safest when the first is separated from the second before generation. The paper frames this as an information-flow problem in which identity should affect only presentation.

A neighbouring study applies the same move to demographically styled prompts rather than to explicit identity statements. Its neutralization step "removes or masks demographic cues before passing the prompt" to the model.[^c11] The reported effect belongs to the combined pipeline: after neutralization and multi-generation the cross-group divergences fall, and the largest gap comes down from 0.28 to 0.22.[^c12] The neutralization was not isolated from the voting step, so the figure is not evidence that removing identity terms alone produces that gain. The divergence measure itself is in [[cross-group-response-divergence]].

## Limits

- Only explicit identity statements were handled; implicit cues from writing style, prior context or preferences were left for future work.[^c9]
- Behavioral probing was done on one model (Llama3.3-70B) and one benchmark; the generality of the "stable knowledge, skewed decoding" reading is the authors' interpretation, not tested by intervention.
- Bias is reduced, not eliminated, and the relevance judge can delete an identity that truly matters (the risk is highest for medical or legal questions; that example is my inference).
- The method adds LLM calls per query; cost was not weighed here.
- A user-side rewrite does not reach a fill made by an intermediate instruction layer. In a text-to-image study, adding specificity to the user prompt did not reliably reduce demographic bias while that layer was left unchanged.[^c10]

## Related

- [[author-cue-review-bias]] — a gender cue leaving correctness unchanged yet moving style and approval
- [[demographic-conditioned-mirage]] — demographic descriptor steering output instead of evidence
- [[social-sycophancy]] — the answerer adapting to user cues
- [[llm-judge-biases]] — other non-content cues shifting model judgments
- [[intermediary-instruction-default-fill]] — the same question-side problem in text-to-image generation, where a default instruction fills unspecified attributes that a user rewrite does not remove
- [[cross-group-response-divergence]] — the distance between answer distributions across groups, the measure used by the demographic-neutralization study above

[^c1]: arxiv-2601-09141 — "the top attention heads achieve consistently strong probing accuracy (86–87%) with a Coefficient of Variation (CV) of only 0.33%"
[^c2]: arxiv-2601-09141 — "These findings indicate that identity cues do not distort the model’s underlying factual representations"
[^c3]: arxiv-2601-09141 — "we perform a counterfactual relevance check with a LLM to determine"
[^c4]: arxiv-2601-09141 — "ensuring that factual, safety-critical, and task-essential content is"
[^c5]: arxiv-2601-09141 — "achieving consistent and substantial bias"
[^c6]: arxiv-2601-09141 — "PS increases bias on StrongReject by"
[^c7]: arxiv-2601-09141 — "The rewritten queries has a 98.8% agreement rate with human"
[^c8]: arxiv-2601-09141 — "truly critical identity terms are mistakenly removed when the model judges them to"
[^c9]: arxiv-2601-09141 — "personalization effects may also arise implicitly,"
[^c10]: arxiv-2512-04981 — "does not reliably mitigate demographic bias"
[^c11]: arxiv-2511-19956 — "removes or masks demographic cues before passing the prompt"
[^c12]: arxiv-2511-19956 — "After applying our neutralization and multi-generation"
