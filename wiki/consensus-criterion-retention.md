---
description: "Keeping only the rubric criteria that all three independent generators propose, after clustering, yielded criteria two experts rated more clinically relevant than a single generator's."
aliases: ["consensus rubric construction", "unanimous criterion retention", "cross-generator agreement filter for rubrics"]
sources: ["openalex-org-w7202416508"]
---
# Consensus criterion retention

A rubric is a set of criteria, and the first decision is which criteria go in. One way to decide without a physician for each item is to let several generators propose criteria independently and keep only those they agree on. In the ConRub-Med construction, three models (GPT-5 Mini, Gemini 2.5 Pro and Claude Sonnet 4.5) each produce 20–30 atomic candidate criteria from the question and reference context, without seeing each other's output. The stated purpose is "To reduce dependence on any one generator."[^c1]

A separate model then screens the pooled candidates for domain errors, logical contradictions and reference conflicts, and clusters the ones that express the same proposition. The retention rule is set-based. For each cluster, the support set is the set of generators that proposed at least one member. A cluster survives only if that set has all three generators, and where reference-coverage tags exist, they must agree within the cluster.[^c2] Each surviving cluster contributes one criterion, its longest member, which the reviewer keeps, rewrites or excludes. So the rule counts generators, not proposals: a generator that repeats a point many times adds one vote.

The construction produced 5,166 prompts with 49,046 prompt-specific criteria and 10,332 global controls.[^c3] The clearest measurement is a source-blind expert study on 17 matched questions. Two experts rated the consensus panels against single-generator panels of the same size and the same covered/uncovered mix. Both experts rated 99.3% of the consensus-pipeline criteria as clinically relevant, against 86.8% and 86.0% for the single-generator panels.[^c4] In the binary-scoring ablation, consensus rubrics reached a medical average of 49.26, against 47.51–48.93 for the single-generator variants, with the largest gains on HealthBench-Hard and GPQA-Diamond.[^c5] The gain was not uniform: IFEval-Loose was lower than for the single-generator variants.[^c6]

## Limits

Unanimity measures agreement, not correctness. The authors name the obvious failure: "The three generators may share the same error, and unanimous support can exclude useful criteria identified by only" one or two models.[^c7] A criterion that every generator misses, or every generator gets the same wrong way, passes the filter without any sign of trouble. Shared blind spots of this kind are what [[universal-criterion-miss]] measures in other settings, and nothing in this method detects them.

The expert evidence is thin. It covers 17 questions drawn from one source (RaR-Medicine), and the medical-validity ratings are near ceiling in both conditions. The paper reports that atomicity and non-redundancy show no clear difference between the conditions, so the measured gain is in clinical relevance alone.[^c8] The authors also note that "Rubric construction also relies on several large hosted models," so a cheaper construction is untested (my inference: the filter's effect on a weaker generator set is unknown).

The ablation is one seed. By my arithmetic from the reported averages, the consensus medical average exceeds the single-generator averages by 0.33 to 1.75 points, a gap one seed does not bound. Whether unanimity beats a looser majority rule is not tested in the parts I read.

## Related

- [[universal-criterion-miss]] — counts criteria that every model fails; the shared-blind-spot problem that a unanimous generator set inherits rather than solves.
- [[supervised-cross-model-consensus]] — agreement among several LLMs' answers, learned by a meta-learner; here agreement among criteria proposals, with a fixed intersection and no learning.
- [[expert-report-derived-atomic-rubrics]] — takes its criteria from expert-written reports rather than from model generators, a different route to the same kind of atomic rubric.
- [[synthetic-rubric-level-inflation]] — model-written rubrics raise absolute scores; the consensus step decides which criteria enter, not how high the scores sit.

[^c1]: openalex-org-w7202416508 — "To reduce dependence on"
[^c2]: openalex-org-w7202416508 — "are available, the tags agree within the cluster."
[^c3]: openalex-org-w7202416508 — "The final training set contains 5,166 prompts and 59,378"
[^c4]: openalex-org-w7202416508 — "Both experts rate 99.3% of the criteria"
[^c5]: openalex-org-w7202416508 — "highest medical average, 49.26 versus 47.51–48.93 for"
[^c6]: openalex-org-w7202416508 — "The improvement is not uniform, however: its IFEval-Loose score"
[^c7]: openalex-org-w7202416508 — "The three generators may share the same error, and unanimous support can exclude useful criteria identified by only"
[^c8]: openalex-org-w7202416508 — "atomicity and non-redundancy show no clear"
