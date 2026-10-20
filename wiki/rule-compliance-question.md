---
description: "Asking whether an actor's behaviour complies with a rule, given the state the rule depends on, needs visual grounding, rule knowledge and causal reasoning together, unlike an attribute question."
aliases: ["compliance judgment", "rule-violation question", "regulation-aware question", "implicit-rule question"]
sources: ["arxiv-2511-18286"]
---
# Rule-compliance question

A rule-compliance question asks whether an actor's behaviour is permitted under a rule, where the verdict depends on a state the rule refers to. The paper's term is "compliance judgment". Its example is a roadside image and the question "Is the pedestrian violating traffic rules given current signal states and crosswalk topology?"[^c1] The authors set this against the questions that dominate existing traffic VQA, which "predominantly query explicit object attributes or rely on" video cues.[^c2]

The mechanism the authors give is that the answer is a verdict rather than a readout. They say it "necessitates a tripartite integration of" visual-semantic grounding, "(ii) regulatory knowledge internalization, and (iii) counterfactual causality".[^c3] My inference from that list: a model that reads the pedestrian's position correctly still cannot answer, because the signal phase decides the verdict. The question therefore has to bring the conditioning state into view, or the answerer has to recover it, and an attribute question never asks for that recovery.

The motivation is the same point made at the level of benchmarks. The authors say that localization tasks "disregard causal relationships",[^c5] and their illustration is a vehicle that can be "in a crosswalk but not violating if signals permit".[^c4] So one visible configuration, an object inside a zone, has different correct answers depending on a state that a question about the object alone does not mention. For asking, this means a compliance question has two parts: the behaviour and the conditions the rule places on it. For answering, it means the answerer must hold the rule and check the behaviour against the state, rather than describe the scene.

The concept is not specific to traffic. Any verdict that depends on a conditional rule has the same shape: an action, a rule with conditions, and a state that switches the conditions. The traffic case is the paper's; the general shape is my reading.

## Limits

- The claim that existing benchmarks cannot test this is an argument from the benchmark's design and its motivating example. In the slices I read, the paper reports no accuracy split by question type, so the claim that compliance questions are harder for the models is not measured here.
- The dataset is roadside traffic only. The rules are those the annotators encoded, and the slices I read do not test whether the verdicts match the traffic law of any place.
- The paper lists counterfactual causality as a third ingredient, with the example "Would the cyclist have violated if the light were green?". I found no separate measure for the counterfactual form.
- The difference is partly one of phrasing. A rule question can state the conditioning state inside the question, which removes the recovery step. The paper does not compare the two phrasings, so how much the recovery step costs is open.

## Related

- [[descriptive-versus-interventional-question]] — the same split between what-is and what-if questions; a compliance question adds a rule between the state and the verdict.
- [[implicit-reference]] — another case where the target is named through scenario knowledge, not a visible cue.
- [[implicit-requirement-recovery-bottleneck]] — in coding agents the missing requirement must be recovered by the agent; the recovery burden is similar when a rule's state is left implicit.

[^c1]: arxiv-2511-18286 — "RoadSceneVQA pioneers image-based compliance judgment, demanding models to answer questions like"
[^c2]: arxiv-2511-18286 — "predominantly query explicit object attributes or rely on"
[^c3]: arxiv-2511-18286 — "(ii) regulatory knowledge internalization, and (iii) counterfactual causality"
[^c4]: arxiv-2511-18286 — "in a crosswalk but not violating if signals permit"
[^c5]: arxiv-2511-18286 — "disregard causal relationships"
