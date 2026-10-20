---
description: "A flat rubric sum counts a criterion's reward or penalty even when the rubric condition that licenses it is absent, so a locally correct judgment still feeds a wrong reward."
aliases: ["FCP", "false credit", "unlicensed credit in rubric rewards", "false penalty in rubric rewards"]
sources: ["doi-10-48550-arxiv-2606-03361", "doi-10-48550-arxiv-2601-18706"]
---
# False credit propagation

A rubric-based reward is often a weighted sum of criterion-level judgments. Each criterion gets a local score, and the scores are added as if each were an independent source of utility.[^c1] The weakness is structural. A criterion's contribution is counted whenever its own judge assigns it a high score, even if a prerequisite or context condition that makes the criterion applicable is missing.

The paper calls this failure False Credit Propagation (FCP): "We call this failure False Credit Propagation (FCP): a criterion contributes reward or penalty without the rubric-level condition that licenses that contribution."[^c2] The case that matters is the one where the local judge is right. The authors say FCP "can occur even when each local criterion score is reasonable on its own:"[^c3] The judge correctly detects the evidence use or the missing caveat. The error is in the sum, which does not ask whether the condition that licenses the credit holds.

The paper's example is a summary of a drug study, with a rubric that gives a penalty for missing an uncertainty caveat (-3) and a penalty for clinical advice (-2). When the response gives no clinical advice, the advice penalty is correctly absent, but the caveat penalty is still counted; the paper's figure labels this a false penalty, "C4 counted despite C3 absent".[^c13] The figure caption states the general point: "Flat aggregation can propagate unsupported credit or" penalties.[^c6] The authors also argue this is not merely noise that averages out: "these invalid utilities are not" averaged away, but "merely averaged away; they become part of the" scalar reward and so shape what the policy learns.[^c5]

The licensing condition takes two typed forms in the paper, a prerequisite relation and an activation relation. For the activation case the paper writes "or activation condition that makes their utility applicable is present."[^c4] Both are typed relations between criteria. Flat aggregation has no place to store them.

## How it is measured

The authors measure FCP at the level of criteria, not of final reward. A leakage case is an edge (j, i) where the child is locally supported and the parent is not: "the child is locally supported but the parent is not,"[^c7] The leaked normalized utility is then averaged over those cases. Flat aggregation leaks 0.0922 and GEAR 0.0032: "0.0922 to 0.0032, a 96.5% relative reduction over"[^c8]

A leakage score alone rewards a method that suppresses every dependent criterion. So the diagnostic is paired with a preservation measure on edges where both parent and child are supported: "To avoid rewarding methods that simply suppress all dependent criteria, we also measure preservation on satisfied dependencies."[^c9]

## Limits

- The diagnostic runs on local judge scores, and the authors say so: "the scalable FCP diagnostic is based on local judge scores;"[^c10] the human-grounded audit "covers only a limited subset of"[^c14] cases.
- FCP is defined relative to a dependency graph, and the method "cannot recover criteria the rubric omits."[^c11] Wrong or absent edges are a second source of error: the paper says they can leave "valid utility or leave false credit uncorrected."[^c12]
- The leakage threshold of 0.5 on local scores is a choice of the diagnostic, not a property of FCP (my inference).
- The reported setting is three benchmarks (HealthBench, WritingBench, PLawBench) with two policy backbones. Whether the failure is as large in other rubric styles is not tested here.
- The work does not establish that the local judges are right; it shows that a correct local judgment can still be mis-aggregated. Wrong judgments are a separate source of error.

## Related

- [[soft-dependency-retention]] — the mechanism the paper proposes to reduce FCP
- [[dependency-aware-checklist-scoring]] — the same licensing idea for a dependency DAG, applied as an all-or-nothing product rather than as a reward; a related but different correction
- [[threshold-gated-rubric-coverage]] — gates a coverage count on a threshold; it does not model which criterion licenses which
- [[pessimistic-min-judge-aggregation]] — aggregates across judges rather than across criteria; a different layer of the same reward
- [[adaptive-rubric-selection]] — a flat sum too (+1, -1, 0 per criterion), but over criteria an LLM judge first keeps as relevant to each prompt. That filters by applicability per prompt, not by the dependency edges FCP measures, and the Health-SCORE paper states that its selected items "contribute equally" and that rubric satisfaction is "treated as a discrete outcome," so severity is unweighted.[^c15]

[^c1]: doi-10-48550-arxiv-2606-03361 — "is to reduce criterion-level judgments to a flat"
[^c2]: doi-10-48550-arxiv-2606-03361 — "We call this failure False Credit Propagation (FCP): a criterion contributes reward or"
[^c3]: doi-10-48550-arxiv-2606-03361 — "each local criterion score is reasonable on its own:"
[^c4]: doi-10-48550-arxiv-2606-03361 — "or activation condition that makes their utility applicable is present."
[^c5]: doi-10-48550-arxiv-2606-03361 — "merely averaged away; they become part of the"
[^c6]: doi-10-48550-arxiv-2606-03361 — "Flat aggregation can propagate unsupported credit or"
[^c7]: doi-10-48550-arxiv-2606-03361 — "the child is locally supported but the parent is not,"
[^c8]: doi-10-48550-arxiv-2606-03361 — "0.0922 to 0.0032, a 96.5% relative reduction over"
[^c9]: doi-10-48550-arxiv-2606-03361 — "To avoid rewarding methods that simply suppress all dependent criteria, we also measure preservation on satisfied dependencies."
[^c10]: doi-10-48550-arxiv-2606-03361 — "the scalable FCP diagnostic is based on local judge scores;"
[^c11]: doi-10-48550-arxiv-2606-03361 — "nor can it recover criteria omitted from the rubric."
[^c12]: doi-10-48550-arxiv-2606-03361 — "valid utility or leave false credit uncorrected."
[^c13]: doi-10-48550-arxiv-2606-03361 — "C4 counted despite C3 absent"
[^c14]: doi-10-48550-arxiv-2606-03361 — "covers only a limited subset of"
[^c15]: doi-10-48550-arxiv-2601-18706 — "items contribute equally, and rubric satisfaction is"
