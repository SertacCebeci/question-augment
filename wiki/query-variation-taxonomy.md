---
description: "Queries written for one information need differ by six transformation types; four (misspelling, naturality, ordering, paraphrase) change only syntax, and they make up 57% of observed variation."
aliases: ["UQV taxonomy", "query variation categories", "query transformation taxonomy", "syntax-changing query variations", "same-need query transformations"]
sources: ["doi-10-48550-arxiv-2111-13057"]
---
# Query-variation taxonomy

People who want the same thing rarely type the same query. The UQV100 collection makes this concrete: crowd workers given one backstory wrote many queries for it, and "workers on average created 57.7 unique queries for a given information need as instantiated as a backstory"[^c1]. The question the work asks is what separates two such queries that share a need. Three annotators took 100 sampled pairs and "performed an open card sort",[^c2] each pile naming a transformation T with T(q_i) = q_j, and the piles were then merged into categories. The result is six categories.

The categories split by whether the meaning changes. Generalization or specialization (narrowing or broadening within the same need) and aspect change (moving to a related but different facet of the need) change what is asked. The other four keep it: "The last four of these categories change the query syntax but not its semantics."[^c3] Among them:

- **Misspelling** adds or removes spelling errors.
- **Naturality** moves between keyword and natural-language form; the definition reads "Moves between keyword queries and"[^c4] natural language queries.
- **Ordering** changes the order of words.
- **Paraphrasing** rewrites one or more words: "we are applying a paraphrasing transformation"[^c5] takes "cures for a bald spot" to "cures for baldness".

Taken across the annotated sample, the syntax-preserving changes "account for 57% of all the transformations,"[^c6] and the semantic changes make up the other 43%. The taxonomy is not a list of how users revise searches within a session or in e-commerce. The authors draw that line themselves: "unlike previous categorizations that describe how users revise queries in" other settings, they study "query variations for the same information need which is a related but different problem."[^c7]

A later sample of 550 random pairs fixed the distribution. The annotators reached only moderate agreement: "was moderate (Cohen’s 𝜅 = 0.42)", and "the disagreements were highest for the naturality and paraphrasing categories."[^c8]

Why the categories matter to an asker: a need can be written in several equally valid ways, and the categories name which kinds of change should leave the need untouched and which change it. The authors use the taxonomy for diagnosis: each generator "follows a category of our taxonomy of query variations which allows us to diagnose ranking models’ effectiveness."[^c9] The use for a person formulating a question is my inference from that; the work does not test it.

## Limits

- One sample. The 100 pairs come from UQV100, whose queries were "written by crowd workers who received a" backstory. These are elicited queries, not logged searches, so the mix of categories in real search behaviour is not established here.
- The annotators were the authors, and agreement was moderate. The disagreements fall in the two largest syntax categories, so the boundary between naturality and paraphrasing is the least settled part of the scheme.
- Misspelling is not observed. The UQV100 queries had already been corrected: "spelling-corrected by its authors, we added the category misspellings,"[^c10] and the table marks its counts with "spelling errors were already fixed for the UQV100 pairs."[^c11] The category is defined by construction, so its share of real variation is absent.
- The text and the table disagree. The text says "be the most common with 33% of all transformations falling into"[^c12] naturality among the syntax-changing categories. Table 2 lists paraphrasing at "215 (32.92%)" and naturality at "118 (18.07%)".[^c13] I read the table as the more reliable of the two, but the paper does not reconcile them.
- The semantic categories are defined and sampled but never generated: "We leave the exploration of query variation generators for"[^c14] gen./specialization and aspect change to future work.
- The taxonomy describes pairs of queries for one need. It does not say which variants a particular asker would produce, nor whether a variant of the same category has the same effect on a retrieval system as another.

## Related

- [[query-variation-robustness]] — what ranking pipelines do when the syntax-preserving categories are applied; only those four categories are tested there.
- [[levels-of-information-need]] — the question asked versus the need behind it; the taxonomy holds the need fixed and varies only its expression.
- [[information-need-reification]] — making the need itself explicit as a specification, the step this taxonomy takes for granted.
- [[query-to-question-reformulation]] — keyword versus question form, the naturality category seen from the retrieval model's side.
- [[reformulation-pattern-library]] — a library of query transformations mined for a retrieval goal; the authors set their categories apart from that kind of work.

[^c1]: doi-10-48550-arxiv-2111-13057 — "workers on average created 57.7 unique queries for a given information need as instantiated as a backstory"
[^c2]: doi-10-48550-arxiv-2111-13057 — "performed an open card sort"
[^c3]: doi-10-48550-arxiv-2111-13057 — "The last four of these categories change the query syntax but not its semantics"
[^c4]: doi-10-48550-arxiv-2111-13057 — "Moves between keyword queries and"
[^c5]: doi-10-48550-arxiv-2111-13057 — "we are applying a paraphrasing transformation"
[^c6]: doi-10-48550-arxiv-2111-13057 — "account for 57% of all the transformations"
[^c7]: doi-10-48550-arxiv-2111-13057 — "same information need which is a related but different problem"
[^c8]: doi-10-48550-arxiv-2111-13057 — "the disagreements were highest for the naturality and paraphrasing categories"
[^c9]: doi-10-48550-arxiv-2111-13057 — "which allows us to diagnose ranking models’ effectiveness"
[^c10]: doi-10-48550-arxiv-2111-13057 — "spelling-corrected by its authors, we added the category misspellings"
[^c11]: doi-10-48550-arxiv-2111-13057 — "spelling errors were already fixed for the UQV100 pairs"
[^c12]: doi-10-48550-arxiv-2111-13057 — "be the most common with 33% of all transformations falling into"
[^c13]: doi-10-48550-arxiv-2111-13057 — "215 (32.92%)"
[^c14]: doi-10-48550-arxiv-2111-13057 — "We leave the exploration of query variation generators for"
