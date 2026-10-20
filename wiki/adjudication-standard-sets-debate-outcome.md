---
description: "In a multi-agent debate the adjudicator's evaluative standard, not the debaters, decided where one ablated exchange converged: the same council reversed winner when scored by logic versus by ethics."
aliases: ["adjudicator value system", "evaluative standard as debate hyperparameter", "adjudicator-driven debate convergence"]
sources: ["doi-10-48550-arxiv-2605-12718"]
---
# Adjudication standard sets debate outcome

In the CHAL framework a debate is run by a council of LLM agents, each assigned an epistemic persona, and a separate adjudicator that scores each exchange. The paper treats the adjudicator's value commitments as configurable hyperparameters: a logic system and an ethics system, weighted by the user. Its stated scope is that these choices "spanning epistemology, logic, and ethics are elevated to configurable hyperparameters governing agent reasoning and adjudication outcomes."[^c1]

The mechanism it tests is a controlled swap of the standard. Holding the debaters fixed, the paper runs an ablation with two council members, an Empiricist and a Supernaturalist, debating whether free will exists. The adjudicator is set to pure logic, to balanced logic and ethics, or to pure ethics.[^c2] Under pure logic and under balanced adjudication the Empiricist dominates, because the Supernaturalist's metaphysical claims fail falsifiability challenges. Under pure ethics the result reverses: "under pure ethics, the outcome reverses entirely, with the Supernaturalist favored despite presenting similar arguments."[^c3] The appendix states that the design isolates the variable: "The only variable that changes across conditions is the adjudicator configuration."[^c4]

The paper's own reading is that the scoring standard, more than the debaters, fixes the result: "This highlights the adjudicator as the primary force driving where the" debate converges.[^c5] In the sense the paper uses, the standard determines both where the exchange converges and which position counts as the most defensible under it. The same two debaters, given different standards, end at different positions. Beliefs move toward whatever the standard rewards, which is my reading of the mechanism; the passages read do not describe the update rule in those words.

For asking and answering, the consequence is that a debate's answer is an answer under a standard, and the standard is chosen before the debate starts. A question put to a debate is therefore partly a question about which errors and which kinds of argument are admissible. This is the same structure that [[evaluation-choices-encode-error-priorities]] finds for accuracy claims, where the metric's weights are the normative choice. Here the weights sit on the adjudicator of an argument rather than on a metric. The transfer is my inference; the paper makes the point only for its own adjudicator.

## Limits

- The evidence is one topic ("Does free will exist?"), two council members, and ten sampled trajectories per configuration.[^c2] The passages read report no variance or significance test. A reversal in ten runs is a directional result, not an estimate of its size.
- All agents are LLMs prompted with assigned personas. Whether the Supernaturalist "fails" a falsifiability challenge is the adjudicator model's judgement under a prompt, not a human's.
- The ablation shows that the adjudicator's weights change the outcome for this council. It does not show that the outcome under one weighting is more correct. The paper says that its goal "is therefore not value-neutral reasoning, which" no LLM system can guarantee, and that the aim is a configuration whose influence "can be systematically studied and compared."[^c6]
- The paper's other ablation, varying council size on the same topic, is also a single topic. The two ablations are not crossed, so the interaction between council diversity and the standard was not measured.
- The comparison is between configurations of this framework. No run in the passages read compares it against an unstructured debate under the same adjudicator.

## Related

- [[evaluation-choices-encode-error-priorities]] — the same point for accuracy metrics: the weights are the normative choice
- [[defeasible-domain]] — the kind of question where an adjudication standard, rather than a reference answer, decides the outcome
- [[confidence-weighted-debate-submartingale]] — another debate-level rule, the aggregation of confidence, which changes how beliefs move
- [[llm-judge-biases]] — the judge model's own biases enter as part of any scoring standard

[^c1]: doi-10-48550-arxiv-2605-12718 — "spanning epistemology, logic, and ethics are elevated to configurable hyperparameters governing agent reasoning and adjudication outcomes."
[^c2]: doi-10-48550-arxiv-2605-12718 — "across 10 trajectories on the topic"
[^c3]: doi-10-48550-arxiv-2605-12718 — "under pure ethics, the outcome reverses entirely, with the Supernaturalist favored despite"
[^c4]: doi-10-48550-arxiv-2605-12718 — "The only variable that changes across conditions is the adjudicator configuration"
[^c5]: doi-10-48550-arxiv-2605-12718 — "This highlights the adjudicator as the primary force driving where the"
[^c6]: doi-10-48550-arxiv-2605-12718 — "The goal is therefore not value-neutral reasoning, which"
