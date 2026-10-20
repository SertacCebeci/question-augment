---
description: "In multi-turn RAG, questions that need earlier turns to be understood are retrieved worse as last-turn queries; rewriting recovers most of the gap (R@5 0.39 to 0.52 on non-standalone)."
aliases: ["non-standalone question", "context-dependent turn", "conversational query rewrite gain"]
sources: ["arxiv-2602-23184", "arxiv-2512-04868"]
---
# Non-standalone question retrieval gap

A non-standalone question is a user turn that "cannot be understood without the prior turns". Its pronouns and ellipses point back to earlier turns, so a retriever fed only the last turn has little to match on.[^c1]

## What was measured

In MTRAG-UN (666 conversation-prefix tasks, six domains), the share of non-standalone questions was raised deliberately: 17.7% in the earlier MTRAG benchmark against 45.7% here.[^c2] Retrieval was run on the 468 answerable and partially answerable tasks with BM25, BGE, Granite R2 and Elser, using either the last turn (LT) or an LLM query rewrite (RW). Rewrite beat last-turn in every case.[^c3] The best retriever, Elser, reached recall@5 of 0.40 on last turn and 0.49 on rewrite.[^c4]

Split by standalone status for Elser R@5, non-standalone questions (214 tasks) scored 0.39 on last turn and 0.52 on rewrite. Standalone ones (254) scored 0.40 and 0.46. So last-turn retrieval is about equally weak on both kinds, and rewriting lifts the non-standalone kind most.[^c5] The authors state that "Rewrite helps for both standalone and non-standalone questions, but more so for non-standalone questions."[^c6]

My reading, not a claim of the paper: the standalone row suggests that rewriting also adds retrieval-useful content (topic terms from the conversation) beyond resolving references. The paper does not test why.

## Domain difficulty

The new enterprise corpora scored worse (R@5 of .32 Banking and .39 Telco against about .52 for the others). The authors point to longer documents, denser hyperlinks and near-duplicate pages across companies as likely causes, offered as likely, not isolated.[^c7]

## Parsing-side evidence (KBCQA)

The same turn-level problem appears where a question must be parsed into an executable query rather than matched to passages. In SEAL, a system for knowledge-base conversational QA on the SPICE benchmark, the paper states that "coreference and ellipsis phenomena present key challenges" for the task.[^c9] Its answer is to have the LLM complete the latest question from the dialog history before any parsing.[^c14] The authors argue the resolution cannot be avoided: "the LLM is ultimately required to resolve coreferences and ellipses" whichever way the history is supplied.[^c10] They also argue that concatenating the raw history is worse, because "redundant information may degrade the accuracy of keyword matching" in the later question-type step.[^c11]

What this does not establish is the rewrite's own share of the gain. The step sits inside a local memory module that "includes resolved entities and completed semantic intent," so an ablation of that module tests more than the rewrite.[^c12] The reported drop is small: "the absence of local memory slightly diminishes performance stability, though less than calibration."[^c13]

## Limits

- Only one rewrite prompt family was used, with GPT-OSS 20B best; the rewrite quality itself was not separated from retriever choice.
- The standalone labels come from annotators, and the subset sizes are single-run counts without variance.
- Conversations come from a small set of annotators and passages were first retrieved with Elser, which may favor Elser.[^c8]
- The domain-gap explanation is unverified.
- My reading, not the paper's: the parsing-side evidence is one system on one benchmark (SPICE), and no test separates the rewrite from the rest of its local memory, so whether rewriting moves a parser as much as it moves a retriever is untested here.

## Related

- [[hypothesis-conditioned-query-rewriting]] — another way of rewriting a query before retrieval
- [[ambiguity-graded-response-strategy]] — what to do when the question itself, not just its context, is unclear
- [[underspecified-question-eager-answering]] — the other open challenge in the same benchmark

[^c1]: arxiv-2602-23184 — "NONstandalone Question - the user question cannot be understood without the prior turns"
[^c2]: arxiv-2602-23184 — "(17.7% in MTRAG and 45.7% in MTRAG-UN)"
[^c3]: arxiv-2602-23184 — "In all cases Query Rewrite outperforms the last turn."
[^c4]: arxiv-2602-23184 — "Granite English R2 performs better than BGE-base 1.5 embeddings, but Elser still performs best."
[^c5]: arxiv-2602-23184 — "Table 3: Elser R@5 standalone results"
[^c6]: arxiv-2602-23184 — "Rewrite helps for both standalone and non-standalone questions, but more so for non-standalone questions."
[^c7]: arxiv-2602-23184 — "Banking and Telco contain substantially longer documents and denser hyperlink structures"
[^c8]: arxiv-2602-23184 — "likely contain biases toward those individuals and Elser retriever"
[^c9]: arxiv-2512-04868 — "coreference and ellipsis phenomena present key challenges"
[^c10]: arxiv-2512-04868 — "the LLM is ultimately required to resolve coreferences and ellipses"
[^c11]: arxiv-2512-04868 — "redundant information may degrade the accuracy of keyword matching"
[^c12]: arxiv-2512-04868 — "which includes resolved entities and completed semantic intent"
[^c13]: arxiv-2512-04868 — "the absence of local memory slightly diminishes performance stability, though less than calibration"
[^c14]: arxiv-2512-04868 — "based on contextual information"
