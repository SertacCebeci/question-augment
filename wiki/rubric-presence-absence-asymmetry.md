---
description: "Rubric reward is about 90% presence-based (contains X) and under 9% absence-based (avoids Y); training under such a rubric raises presence satisfaction while absence satisfaction stays flat."
aliases: ["presence-based rubric weight", "over-specified inclusion", "under-specified avoidance", "enumerability asymmetry in rubrics"]
sources: ["doi-10-48550-arxiv-2605-12474", "arxiv-2512-16272"]
---
# Rubric presence–absence asymmetry

A rubric is a list of weighted criteria, and the criteria come in two kinds. A presence-based criterion rewards the response for containing something: a fact, an entity, a disclaimer, a format. An absence-based criterion penalizes the response for having something: an error, an unsupported claim, a forbidden feature. The paper's point is that the two kinds are not equally available to the rubric writer. Positive criteria can be listed; the ways an answer can go wrong cannot be enumerated in the same way. "A rubric can list facts, entities, disclaimers, and formatting requirements that should appear, but it is much harder to enumerate all the ways an answer can become misleading, bloated, tangential".[^c1]

In the rubric collection the paper analyzes (12,956 items over 500 prompts, classified by an LLM), presence-based criteria carry 90.2% of the rubric weight. Absence-based criteria carry 8.6%, and 1.1% is uncategorized.[^c2] "A similar imbalance appears on HealthBench" (76.1% presence, 22.5% absence).[^c3]

The consequence shows up during training. Presence-based satisfaction rises from 27.6% to 42.5% (+14.9 pp), while absence-based satisfaction slightly declines from 51.6% to 49.6% (−2.0 pp).[^c4][^c5] Responses grow longer and carry more claims, and presence-based satisfaction tracks length and claim count, while absence-based satisfaction shows no such association.[^c6] The paper's reading is that the policy can add relevant-seeming content and formatting, which raises presence scores, without any check that the content is correct.

This matters beyond RL. A grader built this way rewards coverage and is blind to error; an answerer who knows the grader can add material to satisfy it. The rubric-based and rubric-free judges in the paper disagree for this reason: rubric-based judges prefer the RL checkpoint on 85.8% of prompts, while rubric-free judges prefer the base on 78.4%.[^c7] The paper attributes the gap to the rubric rewarding "completeness and explicit coverage more directly than it penalizes verbosity, factual drift, and relevance loss."[^c8]

The same asymmetry shows up on the judge's side in a different setting. In a study of LLM judges grading generated COBOL, the authors find that "Several error types reflect omissions rather than incorrect content," and they generalize that "foundation models often excel at recognizing what is in the input, but struggle to reason" about what is missing.[^c11][^c12] A judge that is asked to find what is present is strong, and one that must notice an absent status check or initialization is weak. This is a parallel in a judge rather than a rubric, and the paper does not measure it against a presence-based or absence-based rubric (my inference: the two findings point the same way).

## Limits

- The evidence is correlational, and the paper says so: "These analyses are correlational," and the results "do not by themselves establish a causal mechanism."[^c9] The mechanism is named as "a plausible optimization pathway", not shown.[^c10]
- The 90/9 split comes from one analysis set of 500 prompts' rubrics, with an LLM classifier doing the categorization. The classifier's error rate is not reported in the text I read.
- The imbalance is a fact about the rubrics the paper studied. It does not say that every rubric is presence-heavy, nor that absence criteria cannot be written; the paper says that "it is much harder" to write them, not impossible.
- Whether rebalancing the weights toward absence criteria would close the rubric-free gap is not tested. The paper's conclusion asks for "reward design that more directly accounts for undesirable behavior," which is a direction, not a result.
- Absence-based items would need the judge to check truth ("verified correctness"), which is itself a verifier task with the failure modes in [[rubric-verifier-failure-modes]]. Moving weight to absence criteria does not remove the verifier problem; it changes which errors matter (my inference).

## Related

- [[rubric-formation-gap]] — the rubric's content, not the judge, limits what is graded; this note is about which kind of content the rubric tends to contain
- [[violation-enumerated-rubric-verdict]] — a grading format that counts violated guidelines, an attempt to make absence checks explicit; not tested against this asymmetry here
- [[sparse-assignment-dense-criteria]] — fine-grained binary checklists in RL, where the granularity of the criteria is the design variable
- [[llm-judge-biases]] — length and format preferences of judges, which the presence-based rubric also rewards
- [[reward-overoptimization]] — the general pattern of a proxy that rises while quality falls

[^c1]: doi-10-48550-arxiv-2605-12474 — "it is much harder to enumerate all the ways an answer can become misleading, bloated, tangential"
[^c2]: doi-10-48550-arxiv-2605-12474 — "criteria rather than absence-based criteria"
[^c3]: doi-10-48550-arxiv-2605-12474 — "A similar imbalance appears on HealthBench"
[^c4]: doi-10-48550-arxiv-2605-12474 — "Presence-based rubric satisfaction rises from 27.6%"
[^c5]: doi-10-48550-arxiv-2605-12474 — "absence-based satisfaction slightly declines from 51.6% to 49.6%"
[^c6]: doi-10-48550-arxiv-2605-12474 — "Presence-based rubric satisfaction is positively associated with response length and total claim count"
[^c7]: doi-10-48550-arxiv-2605-12474 — "rubric-based judges prefer the checkpoint on 85.8% of prompts"
[^c8]: doi-10-48550-arxiv-2605-12474 — "and explicit coverage more directly than it penalizes verbosity, factual drift, and relevance loss"
[^c9]: doi-10-48550-arxiv-2605-12474 — "These analyses are correlational"
[^c10]: doi-10-48550-arxiv-2605-12474 — "Presence-based categories suggest a plausible optimization pathway"
[^c11]: arxiv-2512-16272 — "Several error types reflect omissions rather than incorrect content"
[^c12]: arxiv-2512-16272 — "foundation models often excel at recognizing what is in the input, but struggle to reason"
