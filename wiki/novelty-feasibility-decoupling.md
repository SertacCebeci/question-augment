---
description: "Expert ratings of AI-generated research plans tie novelty weakly to feasibility (r = 0.23) and moderately to impact (r = 0.56), so the axes need not trade off by default."
aliases: ["novelty-feasibility trade-off", "novelty versus feasibility", "originality-feasibility correlation"]
sources: ["arxiv-2601-09714", "arxiv-2512-16969"]
---
# Novelty-feasibility decoupling

When experts score a generated idea on several axes, the axes are not fixed in opposition. In one study, six domain experts rated 30 expert–proposal pairs, drawn from five agentic ideation workflows, on a 0–5 scale for novelty, feasibility and impact.[^c8] Novelty was defined as "perceived originality and divergence from standard literature"[^c1]; feasibility as "realism for a typical Ph.D.-level" researcher working for one to two months.[^c2]

The pooled correlations were 0.23 between novelty and feasibility, which the paper labels "weak positive",[^c3] and 0.56 between novelty and impact, "moderate positive".[^c4] The authors read the first as meaning that "experts did not systematically perceive highly novel ideas as infeasible."[^c5] The workflow means lean the same way. The two workflows with the highest novelty mean, 4.17/5, were Google Co-Scientist and Gemini 3 Pro.[^c6] Co-Scientist also "leads on feasibility (3.00)"[^c7], so the most novel workflow was not the least realistic one. Gemini 3 Pro, equally novel, scored lower on feasibility, by my reading of the table about 2.8, so the pattern is not uniform across workflows.

What survives the transfer is a method point rather than a result. A single quality score hides whether the axes move together. Whether novelty costs feasibility is an empirical quantity for each setting and each rater pool. This differs from the case in [[innovation-correctness-tradeoff-in-problem-generation]], where fine-tuning raised novelty of generated math problems while lowering their correctness. Correctness can be checked against an answer; feasibility here is a rated perception, so the two couplings need not agree. [[question-generativity]] makes a related point from the other side: a second axis of value, separate from uncertainty removed, that a selection rule scoring one axis cannot see.

## Limits

- The correlation rests on 30 ratings. With r = 0.23, a Fisher-z interval (my computation) runs from about −0.14 to 0.54. It does not separate "no relation" from a moderate positive one, so the study cannot show that novelty is free of feasibility costs.
- Feasibility is what experts perceived for a Ph.D.-level researcher. No plan was carried out, so the study does not test whether high-novelty plans could be executed.
- Each expert rated five proposals,[^c8] one per workflow per seed idea, so each workflow mean rests on six ratings. The domain table is thinner still: its caption says "5 proposals",[^c9] but its n column sums to six, with cells of one or two items. Domain claims rest on very few proposals.
- The workflows are built on different systems (the paper names GPT-5.1 and Gemini 3 Pro), so workflow-level means cannot be cleanly attributed to architecture, and the axes cannot be separated from the systems that produced them.
- The abstract says reflection-based approaches "score significantly lower (2.33/5)";[^c10] no significance test is reported. By my reading of the table, 2.33 is the reflection workflow's overall mean and its novelty mean is 2.17, so the headline number is not the novelty figure. Treat the headline numbers with that in mind.
- The paper does not test plagiarism: "This experiment does not directly replicate plagiarism-detection protocols from prior work."[^c11] Its reference list also contains placeholder-looking identifiers such as "arXiv:2501.00001",[^c12] which were not checked here.

- A benchmark study across many models reports the two axes as levels, not as a correlation: "feasibility consistently lags behind novelty and detailedness".[^c13] Its feasibility is computed differently, as graph similarity to an expert implementation template, where "similarity indicates that the proposed idea does not align with accepted solution workflows".[^c14] So it is a distance from a template, not a rated perception, and it does not test the correlation above. The slices read give no within-model correlation between the two axes; that absence is my reading, not the paper's claim.

## Related

- [[retrieval-dissimilarity-novelty-reward]] — a training reward that scores novelty alone, so it cannot show what feasibility does under it
- [[practical-inquiry-model]] — the conception quadrant in which both axes sit, scored in one benchmark
- [[innovation-correctness-tradeoff-in-problem-generation]] — novelty against correctness in generated problems, a different coupling measured differently
- [[question-generativity]] — a second axis of a question's value that a single uncertainty criterion does not capture
- [[skeptical-critic-fact-cross-check]] — a critic-revise loop whose measured effect is on grounding, not on originality

[^c1]: arxiv-2601-09714 — "perceived originality and divergence from standard literature"
[^c2]: arxiv-2601-09714 — "realism for a typical Ph.D.-level"
[^c3]: arxiv-2601-09714 — "0.23 (weak positive)"
[^c4]: arxiv-2601-09714 — "0.56 (moderate positive)"
[^c5]: arxiv-2601-09714 — "suggests that experts did not systematically perceive"
[^c6]: arxiv-2601-09714 — "Gemini 3 Pro achieve the highest mean novelty (4.17/5)"
[^c7]: arxiv-2601-09714 — "while Google Co-Scientist leads on feasibility (3.00)"
[^c8]: arxiv-2601-09714 — "We analyzed responses from 6 experts, each scoring 5 proposals"
[^c9]: arxiv-2601-09714 — "Domain-stratified results across 5 proposals and 6 experts per proposal"
[^c10]: arxiv-2601-09714 — "reflection-based approaches score significantly lower (2.33/5)"
[^c11]: arxiv-2601-09714 — "This experiment does not directly replicate plagiarism-detection protocols from prior work"
[^c12]: arxiv-2601-09714 — "arXiv:2501.00001"
[^c13]: arxiv-2512-16969 — "feasibility consistently lags behind novelty and detailedness"
[^c14]: arxiv-2512-16969 — "similarity indicates that the proposed idea does not align with accepted solution workflows"
