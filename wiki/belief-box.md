---
description: "A belief box states an agent's belief as a proposition with a 1-5 strength in its prompt; a persuader that holds the proposition it argues grows more persuasive as the strength rises."
aliases: ["belief box formalism"]
sources: ["arxiv-2512-06573"]
---
# Belief box

A belief box is a set of propositions, each with a strength on a 5-point Likert scale, written into an agent's prompt. The agent's stance then exists as explicit text rather than only as a pattern in its weights.[^c1] The authors take the term from philosophy of mind and cognitive science, where "it often describes a common assumption of computationalism."[^c2] The box can be empty, meaning the agent holds no stated belief, or hold one or more propositions, each with its own strength.

The strength is the handle the experiments turn. At the end of each debate round, an agent "reassess[es] a new belief strength for their existing belief" through a prompt-based evaluation of the debate so far, and the belief change rate is the share of target agents whose strength moved.[^c3] The authors state the purpose directly: "An advantage of the belief box is that it allows us to observe the belief change over the course of a group discussion."[^c3]

In the persuasion setup, a persuading agent with a box holding the aligned proposition p at strength 1 or 5, or its negation at strength 1 or 5, or nothing at all (the neutral case), argues against a target that holds the opposing proposition at strength 5. The result is that "agents who held the aligned belief that they aimed to persuade the target agent toward were more persuasive than those who did," with "persuasiveness increasing as the aligned belief strength grew."[^c4] The reverse case behaves in the opposite direction: when the persuader shares the target's misaligned belief but argues for the opposite, "persuasiveness declined when that belief grew stronger."[^c5] The box, in other words, does not only record a stance; the stance's strength changes how hard the agent argues. The paper does not isolate the mechanism. A plausible reading, which is mine and untested in the paper, is that a stated strength sets how much the agent has at stake in defending the proposition.

## Limits

- The validity claim is narrow. The abstract says the results "demonstrate the feasibility and validity of the belief box technique in reasoning and decision-making tasks"[^c6], but the evidence is three chat models (Llama-3.3 70B, Phi-4 14B, GPT-4o-mini) on one multiple-choice set and one ethics set of 46 samples, each in homogeneous groups.
- The persuasion effect is not uniform. The authors report that the stronger-negation pattern holds "for all LLMs tested except Phi-4"[^c7], and that the neutral baseline "behaved inconsistently," higher than the weak-belief conditions for one model and lower for another.[^c8]
- The box is a prompt. Nothing in the paper shows that a stated strength corresponds to any internal state of the model. The belief strength is whatever the model reports when asked to revise it, so the measure is a self-report.
- Only the persuader's box and the target's open-mindedness are varied in this experiment; the target's own box is held at strength 5, so the effect of a weak target belief is not tested here.

## Related

- [[open-mindedness-revision-weight]] — the disposition that sets how far a box's strength moves under argument
- [[peer-group-size-belief-change]] — the same box run under group pressure, where the target's strength is what erodes
- [[debate-elicits-sycophancy]] — a persuader's own position matters once an opinion has to be dislodged; the same asymmetry in the direct versus argued probing of an LLM
- [[agm-belief-revision]] — the formal revision theory the paper cites as lineage; its operations act on belief sets, whereas the box revises a Likert score (my contrast, not the paper's claim)

[^c1]: arxiv-2512-06573 — "The belief box is provided to the agent as part of the prompt."
[^c2]: arxiv-2512-06573 — "where it often describes a common assumption of computationalism"
[^c3]: arxiv-2512-06573 — "An advantage of the belief box is that it allows us to observe the belief change over the course of a group discussion."
[^c4]: arxiv-2512-06573 — "Agents who held the aligned belief that they aimed to persuade the target agent toward were more persuasive than those who did"
[^c5]: arxiv-2512-06573 — "persuasiveness declined when that belief grew stronger"
[^c6]: arxiv-2512-06573 — "The results demonstrate the feasibility and validity of the belief box technique in reasoning and decision-making tasks."
[^c7]: arxiv-2512-06573 — "This was true for all LLMs tested except Phi-4"
[^c8]: arxiv-2512-06573 — "The baseline experiment with neutral agents (p = 0) behaved inconsistently"
