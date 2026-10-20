---
description: "When a question's entity name matches several entities, a complete answer is the union over every branch; LLM search agents keep high precision but lose recall, and most failures are missing evidence."
aliases: ["ambiguous multi-hop answer completeness", "DeepAmbigQA", "name ambiguity branch enumeration"]
sources: ["doi-10-48550-arxiv-2511-01323"]
---
# Ambiguous-name branch coverage

A question such as "Which actor from the film Heat won at least one Academy Award?" is ambiguous in the name, not in the intent: several films share the title. The complete answer is not one entity but the union of answers across every film. Ji et al. build DeepAmbigQA (3,600 questions, half with explicit name ambiguity) to measure this jointly with multi-hop reasoning.[^c1]

## How the benchmark makes branches

The generator takes a knowledge graph aligned to Wikipedia, builds an executable plan of chained operations (retrieve entities, apply a filter), and for an ambiguous name re-executes the same plan with each candidate entity. Each execution is one valid reasoning branch, so the gold answer set is verifiable.[^c2] Each question needs at least two reasoning steps, some up to eight, and non-ambiguous items still reach answer sets of up to 43 entities.[^c3]

## What was measured

- The best model, GPT-5 with a dense-retrieval tool over Wikipedia, reached exact match 0.21 on non-ambiguous and 0.13 on ambiguous questions.[^c4]
- Precision is high (typically above 70%) while recall and exact match are far lower: models return partial but not exhaustive sets.[^c5]
- Ambiguity costs recall: GPT-5 drops from 0.71 to 0.48 once ambiguity is introduced, read by the authors as failure to disambiguate and explore multiple valid branches.[^c6]
- Failure breakdown: incomplete information extraction (answer entities never in the retrieved documents, or a branch not covered) dominates; for GPT-5 it is 71% of failures. Weaker models also make more reasoning errors (over 30% for Qwen2.5-3B versus 12% for GPT-5).[^c7]

## What helped and what did not

- Query expansion, an explicit disambiguation step before answering, raised recall in every model, most on ambiguous questions (GPT-5 +0.13 recall), but gave only marginal precision and exact-match gains.[^c8]
- Evidence extraction (filtering retrieved text) gave small gains (GPT-5 +0.01 precision, +0.02 recall on non-ambiguous), consistent with the loss being missing evidence rather than noise.[^c9]
- Giving the model a SPARQL tool over the knowledge graph made things worse across all models, mainly through non-executable queries.[^c10]

My reading: the asker-side lesson is that a name with several referents should be treated as a fan-out of subquestions to enumerate, and a system that answers one branch confidently will look precise while being incomplete. The paper itself only shows that explicit expansion helps partly.

## Limits

- Ambiguity here is name-entity ambiguity resolved by enumerating all readings; the systems never ask the user, so nothing is shown about when clarifying beats enumerating.
- One retrieval setup (e5-base dense retrieval, Wikipedia); the weak retriever may inflate the "missing evidence" share.
- Gold answers come from Wikidata, so completeness is relative to the knowledge graph.
- The improvements from the added modules are modest and not combined or tested for significance in the text I read.

## Related

- [[breadth-oriented-information-seeking]] — same finding (recall far below precision, set-level exactness) without the ambiguity branching
- [[referent-match-set-ambiguity]] — typing ambiguity by the size of the match set; here multiplicity of referents is enumerated rather than asked about
- [[task-ambiguity]] — ambiguity over which task is meant, a different axis from which entity
- [[set-membership-versus-cell-completion-gap]] — another case where partial set correctness hides incompleteness

[^c1]: doi-10-48550-arxiv-2511-01323 — "a dataset of 3,600 questions requiring multi-hop reasoning and half of them explicit name ambiguity resolving"
[^c2]: doi-10-48550-arxiv-2511-01323 — "For ambiguous names, the same plan can be re-executed"
[^c3]: doi-10-48550-arxiv-2511-01323 — "Each question"
[^c4]: doi-10-48550-arxiv-2511-01323 — "achieving only 0.21 and 0.13 EM on the nonambiguous and ambiguous subsets, respectively"
[^c5]: doi-10-48550-arxiv-2511-01323 — "While precision remains high (typically"
[^c6]: doi-10-48550-arxiv-2511-01323 — "GPT-5’s recall drops from 0.71"
[^c7]: doi-10-48550-arxiv-2511-01323 — "exhibits 71% of failures in this category"
[^c8]: doi-10-48550-arxiv-2511-01323 — "GPT-5’s recall shows a 0.13 increase on ambiguous queries"
[^c9]: doi-10-48550-arxiv-2511-01323 — "These small"
[^c10]: doi-10-48550-arxiv-2511-01323 — "However,"
