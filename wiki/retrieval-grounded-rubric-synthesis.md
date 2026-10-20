---
description: "A rubric generator shown retrieved past cases and their expert rubrics writes more varied, case-matched criteria; the RL policy trained on them scored 17.89 against 10.69 without retrieval."
aliases: ["Rubric-RAG", "retrieval-augmented rubric generation", "in-context rubric synthesis from retrieved cases", "retrieval-conditioned rubric writing"]
sources: ["doi-10-48550-arxiv-2510-15859"]
---
# Retrieval-grounded rubric synthesis

A [[question-specific-rubric]] is written for one case. This note is about how that case-specific rubric is produced when no human writes it. The mechanism in this paper is retrieval followed by in-context generation. A seed set of consultations, each with its expert rubric, is embedded and stored in two pools: one of case–rubric pairs, and one of every unique rubric with its own embedding.[^c1] For a new query, the system retrieves the most similar cases and the most similar rubric candidates, then reranks them with a second model.[^c2] The retrieved cases and rubrics are then given to a generator as in-context exemplars, and the generator writes the rubric for the new case.[^c3]

The rubric is then used as a reward. Each criterion carries a signed weight, positive for desirable clinical behaviour and negative for unsafe or misleading behaviour, and a judge model checks each criterion against each sampled response. The reward for a rollout is the weighted sum of the criteria the judge marks true.[^c4][^c5] So the generator's output is the whole reward specification for that case, and retrieval is the only thing that varies what the generator sees.

What was measured: in an ablation the authors compare rubrics generated with retrieved exemplars against rubrics generated without them. Lexical diversity of the rubrics falls from 0.107 with retrieval to 0.070 without it, "indicating reduced" diversity.[^c6] The downstream gap is the larger result: on HealthBench-Hard the policy scores 17.89 with retrieved exemplars and 10.69 without, which the authors call a "substantial performance difference observed downstream in HealthBench-Hard."[^c7] The authors' explanation is that retrieval keeps each rubric matched to its scenario, and so reduces redundancy between cases: "using retrieval methods ensures that the rubrics remain closely matched to each clinical scenario, significantly reducing redundancy between cases."[^c8]

What survives from the per-question idea is that the target is the case, not a general standard. What the retrieval adds is a second source of criteria: other cases' rubrics, which show the generator what a complete checklist looks like for a similar consultation. This is a different mechanism from grading with retrieved exemplars in [[exemplar-retrieval-grounded-grading]], which retrieves graded essays to calibrate a grader rather than to write criteria.

## Limits

- The seed rubrics are human-written and few. The authors name this as the main constraint: "ORBIT currently relies on a limited number of" human-created rubric seeds.[^c9] Retrieval cannot supply criteria that no seed contains. The paper points to grounding the seeds in clinical guidelines as the next step: "grounding the initial evaluation criteria in established clinical practice guidelines" is named as "an important direction for future research."[^c12]
- The seeds come from HealthBench rubrics, and the headline evaluation is HealthBench-Hard, which is a benchmark of the same family.[^c10] Whether any seed case overlaps an evaluation case is not established in the parts I read. (my inference)
- Diversity is measured lexically, and the paper treats less redundancy as better without checking that the extra criteria are clinically correct. The downstream gain is the evidence that matters, and it is one comparison in one training setting. (my reading)
- If a retrieved rubric is wrong, the generator sees it as an exemplar and may reproduce the error for the new case. This is my inference from the design. The generator prompt's figure caption lists "anti-copying" among its fixed elements,[^c13] but I did not read the prompt's text.
- The rubric is only as reliable as the judge that applies it. The paper finds that a stronger evaluator during training "markedly enhances the resulting policy performance," so the retrieval gain and the judge choice are confounded in any comparison across judges.[^c11]
- The comparison I read is with and without retrieval, and it does not isolate retrieval from the choice of generator model. The paper also compares rubric generators in an appendix table, which I did not read. (my reading)

## Related

- [[question-specific-rubric]] — the per-question rubric this mechanism produces, measured there against one fixed rubric
- [[amortized-rubric-generation]] — a generator trained to write question-only rubrics; retrieval here supplies the exemplars at inference instead of distilling them into weights
- [[bootstrap-rubric-generation]] — a policy that writes its own rubrics as reward; the seed source here is fixed and human-made
- [[exemplar-retrieval-grounded-grading]] — the same retrieve-then-prompt pattern applied to grading essays rather than writing criteria
- [[criterion-saturation-headroom]] — what happens to the weighted reward once the criteria are fixed and some saturate during training
- [[rubric-criterion-dropout]] — a different remedy for reward hacking on a fixed rubric, by sampling criteria rather than generating them

[^c1]: doi-10-48550-arxiv-2510-15859 — "Diagnostic Database Construction. Given a seed dataset"
[^c2]: doi-10-48550-arxiv-2510-15859 — "subsequently employing a reranker Mre to"
[^c3]: doi-10-48550-arxiv-2510-15859 — "serve as in-context exemplars to guide rubric synthesis."
[^c4]: doi-10-48550-arxiv-2510-15859 — "Instead of sparse binary rewards such as exact answer matching"
[^c5]: doi-10-48550-arxiv-2510-15859 — "Positive weights reward desirable clinical behaviors; negative weights penalize unsafe or misleading ones."
[^c6]: doi-10-48550-arxiv-2510-15859 — "from 0.107 (RAG) to 0.070 (no-RAG), indicating reduced"
[^c7]: doi-10-48550-arxiv-2510-15859 — "substantial performance difference observed downstream in HealthBench-Hard (17.89"
[^c8]: doi-10-48550-arxiv-2510-15859 — "using retrieval methods ensures that the rubrics remain closely matched to each clinical"
[^c9]: doi-10-48550-arxiv-2510-15859 — "ORBIT currently relies on a limited number of"
[^c10]: doi-10-48550-arxiv-2510-15859 — "from HealthBench rubrics and an embedding model Memb"
[^c11]: doi-10-48550-arxiv-2510-15859 — "employing stronger evaluators during training markedly enhances the resulting policy performance"
[^c12]: doi-10-48550-arxiv-2510-15859 — "grounding the initial evaluation criteria in established clinical practice guidelines"
[^c13]: doi-10-48550-arxiv-2510-15859 — "The prompt fixes the generator role, output schema, scoring convention, and anti-copying"
