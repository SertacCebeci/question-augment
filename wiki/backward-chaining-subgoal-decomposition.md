---
description: "Decomposing a problem backward from its target conclusion into the intermediate conditions it needs is one of the sub-skills most correlated with geometry solving accuracy."
aliases: ["sub-goal decomposition", "backward chaining", "necessary-precondition decomposition", "backward chaining from the conclusion"]
sources: ["arxiv-2512-24119", "arxiv-2512-03360"]
---
# Backward-chaining sub-goal decomposition

A geometry proof can be built forward from the givens or backward from the conclusion. The paper names the backward form and measures it: "a common reasoning strategy involves backward chaining, starting from the target conclusion and identifying the necessary preconditions required to derive it."[^c1][^c2] Formally, the target is a state s_t, the last rule r_t that produced it has a preceding state set S_rt, and one application of r_t derives s_t from S_rt. The question put to a model is "What conditions must be established to derive conclusion s_t?"[^c3] The correct answer is the set of necessary intermediate conditions, S_rt minus the initial premises.[^c4]

The distractors are built so that a partial answer fails. The paper's construction takes the wrong options from two places: a subset of the correct intermediate conditions, and intermediate states from elsewhere in the reasoning graph that are not on this route.[^c5] A model that names some of the required conditions but not all, or names a condition from a different branch, is therefore marked wrong. The skill being measured is to hold the target fixed and enumerate what it requires, one rule back at a time.

As with irrelevant premise filtering, the evidence that this matters is a correlation. Across MLLMs, sub-goal decomposition is one of the three strongest correlates of final-answer accuracy on the full benchmark, and on the out-of-distribution GeoQA and Geometry3K sets it is among the two strongest.[^c6][^c9] The paper's summary is that "Sub-Goal Decomposition and Irrelevant Premise Filtering significantly impact complex problem-solving success."[^c7] Its introduction states the design intent directly: decomposition "breaks problems into atomic steps."[^c8]

A different paper measures the order contrast that this one leaves open. HBLR, a framework for logical reasoning over text, assumes the conclusion and recursively verifies the premises that would support it. Its ablation compares that backward module with a forward variant that keeps the verification step: "On average, backward reasoning yields a 5.69% improvement."[^c10] The authors' explanation is that forward reasoning spreads over redundant branches. Their analysis of plan-and-solve output finds that "forward reasoning tends to overuse" the premises that are available, so the forward chains are longer than they need to be.[^c11] The contrast is measured on logical-deduction benchmarks with answer accuracy, not on geometry, so it supports the backward order on a different task rather than confirming the measure used above.

## Limits

- **A correlation across models, not a teaching result.** The coefficients relate a task score to solving score across models. Nothing in the text tests whether prompting a model to chain backward, or training it on this task, raises its solving accuracy.
- **Backward against forward is not compared.** The paper calls backward chaining "a common reasoning strategy"; the text I read does not measure forward chaining as a contrast, so it does not show backward chaining is the better order.
- **One reasoning graph per item.** The necessary conditions are defined by the single graph the generator produced. Where a problem admits several valid proofs, a different set of preconditions could be equally necessary; the item then penalises a correct alternative. This is my inference from the construction.
- **Synthetic geometry.** The items come from a formal generator with verified steps; transfer to human-written problems, where the target and its preconditions are less cleanly defined, is not shown here.
- **The probe is recognition, not generation.** The model chooses among options; it does not produce the decomposition unprompted. Whether generation tracks recognition is not tested in this text.

## Related

- [[irrelevant-premise-filtering]] — the complementary sub-skill: which given conditions a proof never uses, where this note asks which intermediate conditions a conclusion needs.
- [[goal-refinement-graph]] — KAOS refines a goal by asking HOW (producing subgoals) and WHY (recovering the parent goal); backward chaining is the same refinement read in the proof direction.
- [[self-ask-decomposition]] — decomposes a question into sub-questions to answer in turn; a related move, without the requirement that the sub-questions be the preconditions of a target.
- [[plan-before-search-anchoring]] — writing an ordered sub-question plan before retrieval; the same planning step in a retrieval setting.

[^c1]: arxiv-2512-24119 — "a common reasoning strategy involves backward chaining, starting"
[^c2]: arxiv-2512-24119 — "from the target conclusion and identifying the necessary preconditions required to derive it"
[^c3]: arxiv-2512-24119 — "we prompt the MLLMs with the question: What conditions must be established to"
[^c4]: arxiv-2512-24119 — "the necessary intermediate conditions excluding initial premises"
[^c5]: arxiv-2512-24119 — "systematically constructed as A ∪ B"
[^c9]: arxiv-2512-24119 — "task S.D. and T.S. exhibit the strongest correlations, followed by I.P.F."
[^c6]: arxiv-2512-24119 — "Among them, task I.P.F., S.D., and T.S. show the strongest correlations"
[^c7]: arxiv-2512-24119 — "Sub-Goal Decomposition and Irrelevant Premise Filtering significantly impact complex problem-solving"
[^c8]: arxiv-2512-24119 — "Sub-Goal Decomposition breaks problems into atomic steps"
[^c10]: arxiv-2512-03360 — "On average, backward reasoning yields a 5.69% improvement"
[^c11]: arxiv-2512-03360 — "forward reasoning tends to overuse"
