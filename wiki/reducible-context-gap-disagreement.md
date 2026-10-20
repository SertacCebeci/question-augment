---
description: "Expert-grader disagreement on rubric items is mostly case-specific; the part tied to a tag is missing context or ambiguous phrasing, not genuine domain ambiguity (OR 2.55 vs 1.01)."
aliases: ["reducible vs irreducible uncertainty in rater disagreement", "information-gap disagreement", "case-specific rater disagreement"]
sources: ["arxiv-2602-22758"]
---
# Reducible context gaps drive expert disagreement

In HealthBench's physician meta-evaluation (60,896 binary met/not-met judgments, 186 physicians, 34 rubric criteria), 22.5% of cases show disagreement between graders. Variance decomposition finds the cause is mostly neither the rater nor the rubric: physician identity accounts for 2.4%, rubric identity for 3.6–6.9% of disagreement variance, and about 81.8% is a case-level residual. The paper reads this in Kahneman's terms (level noise versus pattern and occasion noise).[^c1]

Metadata labels, rubric wording, specialty, surface-feature triage and embeddings all fail to explain the residual (AUC 0.58 and 0.485 for the predictors).[^c2] Only two features carry signal, each worth roughly 3% of variance: completion quality, with disagreement highest for borderline completions (an inverted U), and uncertainty type.[^c3]

## The dissociation

Physician-validated prompt tags, assigned in a separate consensus process and so exogenous to the grading labels, split prompts into no uncertainty, irreducible-only uncertainty (genuine medical ambiguity) and any reducible uncertainty (missing context, ambiguous phrasing). Disagreement was 13.2%, 13.4% and 28.0%. Relative to no uncertainty, irreducible-only has OR 1.01 (p = 0.90) and reducible has OR 2.55.[^c4] A second tag, insufficient context, agrees: 35.3% versus 25.8% disagreement (OR 1.56).[^c5]

The mechanism the authors propose: graders split when the scenario leaves out what is needed to judge a response, not when medicine itself is unsettled. So what looks like an irreducible ceiling on agreement is partly a property of how the prompt was written, and can be changed by supplying the missing information. In the paper's words, physicians "do not disagree more on cases with genuine medical ambiguity".[^c6]

For asking and answering, this is a measured case that the information a question lacks, rather than the difficulty of the domain, predicts when competent judges diverge. That bears on when clarifying questions should be asked: it supports asking for context over deliberating harder. This is my inference, not tested here.

## Limits

- Effect sizes are small. Pseudo R² for the uncertainty tags is 3.4%, so about 97% of disagreement stays unexplained by anything examined.[^c7]
- The tags exist only for the consensus subset (8,526 cases; 3,230 with context tags), so the dissociation is not shown across the whole dataset.
- The result is observational. The "reducible" label is a physician judgment about the prompt; no experiment added the missing context and measured whether disagreement fell. The causal reading (closing gaps lowers disagreement) is the authors' suggestion, not a demonstrated intervention.
- Single benchmark, binary rubric grading of medical chat; the paper itself notes predictability may differ for standardized image grading. Other domains are untested.
- Two raters per case at the median limits the resolution of pattern versus occasion noise; the residual lumps them together.

## Related

- [[uncertainty-decomposition]] — the same reducible/irreducible cut, here applied to rater disagreement rather than agent action choice
- [[clinician-veto]] — clinician review of AI output, the setting where such labels are used
- [[hard-easy-effect]] — difficulty-dependent judgment patterns, comparable to the inverted-U with completion quality
- [[clarification-benchmarks]] — context-insufficient prompts are the ones where asking pays

[^c1]: arxiv-2602-22758 — "Rubric identity accounts for 15.8% of met/not-met label variance but"
[^c2]: arxiv-2602-22758 — "(AUC = 0.485). Disagreement follows an inverted-U with completion quality (AUC ="
[^c3]: arxiv-2602-22758 — "show meaningful effects, each explaining ∼ 3% of variance."
[^c4]: arxiv-2602-22758 — "more than doubles disagreement odds; irreducible uncertainty has no effect"
[^c5]: arxiv-2602-22758 — "predicts higher disagreement (35.3% vs. 25.8%; OR = 1.56"
[^c6]: arxiv-2602-22758 — "physicians do not disagree more on cases with"
[^c7]: arxiv-2602-22758 — "remains unexplained by the features we examined."
