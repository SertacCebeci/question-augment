---
description: "A cheap answerer samples several times and defers to a stronger one only when the samples disagree; the agreement gate replaces token confidence as the routing signal."
aliases: ["self-consistency cascade", "self-consistency deferral", "agreement-gated teacher deferral", "sampling-based cascade"]
sources: ["arxiv-2512-02543"]
---
# Agreement-gated deferral

A two-model cascade answers with the cheap model and calls the expensive one only when the cheap answer is not trusted. The usual trust signal is a confidence score such as token probability. Sarukkai et al. use the agreement of the cheap model's own samples instead. At each agent step the student "samples N = 3 candidate actions" under the same retrieved context.[^c1] By default agreement means identity: "agreement requires all sampled actions to be identical."[^c2] If the samples agree the student's action runs; otherwise "the system defers to the" teacher for that step.[^c3]

The premise is stated in the paper: "the student’s understanding of the correct action should be stable across" multiple samples when the in-context examples have worked.[^c4] The disagreement is read as a symptom: uncertainty in the student's output "manifesting as disagreement among samples."[^c5] The authors justify this over a confidence score because of how agents write their output. When the model first produces reasoning before its action, "computing the uncertainty in the generated answer either requires marginalizing out the" reasoning path.[^c6] Sampling sidesteps this by comparing the actions themselves, which "naturally allows for the comparison of answers of different" lengths.[^c7] The authors call it "an effective way to implement cascades in agentic settings with large action spaces."[^c8]

In the full system the gate sits after in-context distillation. The student's prompt holds retrieved teacher steps, and the gate catches the steps where those examples do not steer it, since "there may remain" such "situations where retrieved exemplars fail to effectively guide the student LLM."[^c9] The paper reports that the combination beats the gate alone: on ALFWorld the full method is "outperforming Student (Cascade only) configurations at equivalent cost levels."[^c10] On AppWorld the full method achieves "3.5× cost reduction while recovering 79% of teacher accuracy."[^c11] The paper's summary of the gate is that "self-consistency provides an effective automatic deferral signal."[^c12]

The gate also has a cost structure of its own. Every step draws N student calls before any decision, and the teacher is called only on disagreement, so the savings depend on how often the samples agree. The part of the paper read does not separate the cost of the N draws from the cost of the deferrals; that accounting is my inference from the algorithm, not a reported figure.

## Limits

- Agreement is not correctness. A student that is stably wrong passes the gate, and the gate has no way to see it. The paper does not measure the rate of consistent errors. My inference is that the student failures the paper finds, mostly coverage gaps in the retrieved examples, would be exactly the kind that repeated sampling does not expose. The paper's own attribution of those failures is by an LLM judge, and the authors note that "While LLM-based attribution is imperfect" but still useful.[^c13]
- The default test is exact identity. The text says "By default," which implies alternatives exist, but the section read does not test a looser equality or how sensitive the gate is to paraphrase.
- The results are on two agent benchmarks (ALFWorld and AppWorld) with one teacher-student pair per run. The gap to the teacher grows with difficulty: "the gap to Teacher widens on harder tasks."[^c14] The gate is a single operating point; a difficulty-based alternative "trades 2.4× higher cost for 12 percentage points of accuracy," so the gate is not the only frontier point.[^c15]

## Related

- [[majority-vote-mode-certificate]] — the same sample vote used as an estimator of the mode; that note asks how likely the vote has found the mode, while this gate asks only whether the vote is unanimous.
- [[confidence-calibrated-cascade-judgment]] — a cascade routed by a confidence score; the gate here swaps that score for sample agreement.
- [[uncertain-agreement]] — agreement under high entropy is weaker evidence than agreement under confidence; a unanimous gate inherits that worry.
- [[self-consistency-difficulty-score]] — the same sample agreement used as a difficulty signal rather than a routing decision.
- [[knowledge-distillation]] — the teacher-student pairing; here no weights move, and the student only sees teacher traces in its context.

[^c1]: arxiv-2512-02543 — "the student samples N = 3 candidate actions conditioned on"
[^c2]: arxiv-2512-02543 — "By default, agreement requires all sampled actions to be identical"
[^c3]: arxiv-2512-02543 — "if they diverge, the system defers to the"
[^c4]: arxiv-2512-02543 — "the student’s understanding of the correct action should be stable across"
[^c5]: arxiv-2512-02543 — "manifesting as disagreement among samples"
[^c6]: arxiv-2512-02543 — "computing the uncertainty in the generated answer either requires marginalizing out the"
[^c7]: arxiv-2512-02543 — "which naturally allows for the comparison of answers of different"
[^c8]: arxiv-2512-02543 — "effective way to implement cascades in agentic settings with large action spaces"
[^c9]: arxiv-2512-02543 — "situations where retrieved exemplars fail to effectively guide the student LLM"
[^c10]: arxiv-2512-02543 — "outperforming Student (Cascade only) configurations at equivalent cost levels"
[^c11]: arxiv-2512-02543 — "while recovering 79% of teacher accuracy"
[^c12]: arxiv-2512-02543 — "While self-consistency provides an effective automatic deferral signal"
[^c13]: arxiv-2512-02543 — "While LLM-based attribution is imperfect"
[^c14]: arxiv-2512-02543 — "the gap to Teacher widens on harder tasks"
[^c15]: arxiv-2512-02543 — "difficulty-based routing trades 2.4× higher cost for 12 percentage points of accuracy"
