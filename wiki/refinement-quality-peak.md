---
description: "Iterative LLM refinement of an explanation raises expert-judged quality to a peak within a few rounds, then can drive it below the unrefined start; where to stop is a design question."
aliases: ["inverted-U refinement trajectory", "over-refinement", "non-monotonic refinement", "refinement peak"]
sources: ["arxiv-2512-21066", "arxiv-2512-23717", "arxiv-2512-05965"]
---
# Refinement quality peak

Revising one's own output is not guaranteed to improve it monotonically. In a case study, a multimodal LLM turned a SHAP explanation of rice yield into farmer-facing advice over 11 rounds (Rounds 0–10), and crop scientists and LLM judges scored every round. Average quality rose by 30–33% over Round 0, peaking at Rounds 3–4, and then fell "after which quality declined, below the starting point for crop scientists."[^c1] The authors draw the consequence directly: "Refinement therefore requires strategic early stopping, which challenges assumptions of monotonic improvement."[^c2]

The mechanism, as the authors read it, is a shift in what the revisions add. Each round the model analyzes its previous output, identifies gaps, writes supplementary analyses and rewrites the advice. Early rounds "lack analytical depth (analogous to bias)," while continuing past the optimum "introduces verbosity and abstraction."[^c11][^c12] The criteria that need grounding fell: "the late-round decline of Contextual Relevance, Crop Science Credibility, Practicality, and Specificity in both groups" is the pattern the authors report.[^c13] Conciseness fell from the outset, and Cost Consideration rose while the dataset held no economic variables, so that "steady improvement rested on economic reasoning generated without grounding data."[^c3] The authors describe the criteria as following "distinct trajectories," which is why one iteration count cannot serve all of them.[^c4]

The shape itself is the transferable part. The authors fit a derivative-based GAM to each panel's curve and report an inverted U with an estimated peak at Round 2.50 for crop scientists and at "an estimated peak at Round 3.53" for LLM judges.[^c5] The analogy to the bias–variance trade-off is theirs, not a measured decomposition: they hypothesize that "explanation comprehensiveness has an optimum, by analogy with the bias–variance trade-off."[^c6] Read this way, a simple explanation gives biased information and an over-extended one overwhelms the reader. What the study measures is only that the curve has an interior maximum; that the cause is verbosity and ungrounded abstraction is their interpretation of the criteria.

A second setting, with a different task and metric, shows the same kind of interior optimum. In a multi-agent debate that rewrites harmful requests into less explicit forms, the best result came after one debating round: "effectiveness peaks at just one round of debating,"[^c14] and beyond that "while additional rounds lead to diminishing or" returns, which the paper describes as diminishing or even negative.[^c15] Adding debaters did not help the same measure: a clear gain "observe a clear performance gain as more debaters"[^c16] was not seen across three to six. The text read gives only a tentative reason for the late-round loss. The metric there is a test model's refusal rather than a judged quality score, so the two curves share a shape, not a demonstrated cause.

Locating the peak needs someone to score the rounds, which is why the authors pair the curve with a judge question. A panel of LLM judges could locate the expert peak, though the judges' absolute levels are not usable. See [[ordinal-judge-fidelity]]. The stopping signal they propose is the running maximum of a screened judge's round scores, not a fixed iteration budget. A fixed budget is what most retrieval loops use in practice (see [[stop-continue-criteria-in-retrieval-loops]]), so the same stop decision appears here in a different loop.

## Limits

- One case: "this study is based on data from a single crop system (rice)."[^c7] The authors also "relied on a single generation model (Claude Sonnet 4)," so the curve may belong to that model.[^c8]
- The stopping rule is not validated. The authors say it is "distilled from a single case study, not a validated stopping algorithm."[^c9]
- The evaluation scores recommendations at generation time. "Without field validation of implementation outcomes over time," the study cannot say whether the Round 3–4 advice helps farmers more than the Round 10 advice.[^c10]
- The peak location is sensitive to which criteria are averaged. Conciseness peaks early and Cost Consideration late, so a different criterion mix moves the peak. (my inference from the per-criterion curves)
- Whether the decline comes from iteration itself or from the growing length of the output is not separated by an ablation in the parts read. (my inference)
- Extra self-revision can also hurt in other settings: see [[deliberation-cascade]], where self-critique at every node lowers return. That is a different system, and the two results do not show a shared cause.

- A loop whose score kept rising over the caps tested does not show a peak. In an image-editing loop where a critic rewrites the instruction after each output, the benchmark score rose at every turn cap from two to eight, and the paper does not test beyond eight.[^c17] So an interior peak is not a general property of refinement; it is an observed shape in some settings. See [[output-grounded-instruction-refinement]].

## Related

- [[ordinal-judge-fidelity]] — the judges that can locate this peak are miscalibrated in level, but their ordering of rounds holds
- [[stop-continue-criteria-in-retrieval-loops]] — stopping in retrieval loops: budgets versus state-dependent tests
- [[deliberation-cascade]] — more self-questioning and self-critique lowered task return in a multi-agent hierarchy
- [[llm-judge-biases]] — the judge-side biases (verbosity, self-preference) that a peak-locating judge inherits
- [[refinement-signal-reversal]] — the same debate study, paired per query: one revision step both removes and restores the signal it targets
- [[output-grounded-instruction-refinement]] — a critic-rewrite loop on image editing whose score rose over the tested turn caps, the counterexample to a fixed interior peak

[^c1]: arxiv-2512-21066 — "after which quality declined, below the starting point for crop scientists"
[^c2]: arxiv-2512-21066 — "Refinement therefore requires strategic early stopping, which challenges assumptions of monotonic improvement."
[^c3]: arxiv-2512-21066 — "steady improvement rested on economic reasoning generated without grounding data"
[^c4]: arxiv-2512-21066 — "the seven quality criteria follow distinct trajectories"
[^c5]: arxiv-2512-21066 — "an estimated peak at Round 3.53"
[^c6]: arxiv-2512-21066 — "explanation comprehensiveness has an optimum, by analogy with the bias–variance trade-off"
[^c7]: arxiv-2512-21066 — "this study is based on data from a single crop system (rice)"
[^c8]: arxiv-2512-21066 — "relied on a single generation model (Claude Sonnet 4)"
[^c9]: arxiv-2512-21066 — "distilled from a single case study, not a validated stopping algorithm"
[^c10]: arxiv-2512-21066 — "without field validation of implementation outcomes over time"
[^c11]: arxiv-2512-21066 — "lack analytical depth (analogous to bias)"
[^c12]: arxiv-2512-21066 — "introduces verbosity and abstraction"
[^c13]: arxiv-2512-21066 — "The late-round decline of Contextual Relevance, Crop Science Credibility, Practicality, and Specificity in both groups"
[^c14]: arxiv-2512-23717 — "effectiveness peaks at just one round of debating"
[^c15]: arxiv-2512-23717 — "while additional rounds lead to diminishing or"
[^c16]: arxiv-2512-23717 — "observe a clear performance gain as more debaters"
[^c17]: arxiv-2512-05965 — "We observe a clear and consistent performance scaling as we increase the maximum number of"
