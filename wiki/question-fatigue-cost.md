---
description: "A clarifying question gets dearer as more have been asked, so asking becomes a budget; the simulated user's answers also decay with each question. Both are modelled assumptions, not measured."
aliases: ["question fatigue", "user fatigue cost", "escalating ask cost", "asking as a depleting budget"]
sources: ["arxiv-2512-18571"]
---
# Question-count-escalating cost

When a question is put to a person, its cost need not be the same each time. ESearch-R1 prices a dialogue action as a base price that grows with the number of questions already asked. The fatigue term is "a fatigue penalty factor" in the cost formula, and the stated growth factor is set so that "cost increased with each query (growth factor α = 0.2)."[^c1][^c2] So the k-th question costs more than the first, linearly in the count under the formula as written.

The answering side is made to degrade as well. The simulated user gives a detailed answer to the first question, and after that the authors model the chance of a useful reply falling: "the probability of receiving a useful answer decays exponentially" as the number of questions rises.[^c3] The two pressures act in the same direction. A question is dearer to ask and worth less to receive as the count grows, so the marginal value of the next question falls while its price rises.

The paper's stated point is that this structure teaches restraint. The authors describe the effect on the trained agent as an implicit negative reward that teaches it "asking is a limited resource."[^c4] Their reported result is that the agent "reduces unnecessary human interactions" by using memory where it can.[^c5]

The concept, stated plainly, is that asking is a budget that depletes with use. This is a different shape from a fixed burden per question. Where a fixed per-question burden makes the number of questions a single trade-off, here each further question is priced higher than the last and returns less, so a policy should ask a few well-chosen questions and then turn to other actions. Inside a mixed action space, this dialogue price is one of several prices a policy weighs, see [[heterogeneous-action-cost-substitution]].

## Limits

- Neither function is measured on people. The oracle is a model, introduced "to enable closed-loop evaluation without human-in-the-loop latency."[^c6] The paper gives no human data on how attention or answer quality change with the number of questions. The linear growth of the cost and the exponential decay of usefulness are design choices, and the true shape (exponential, linear, or a threshold after a few questions) is open.
- The text lists the growth factor α among the parameters varied in the sensitivity analysis. It does not report varying the decay rate of answer usefulness, so the answer-side assumption is not tested for robustness in the text.
- The fatigue term is never separated from the rest of the reward in an ablation. The dialogue ablation removes Ask entirely; no run keeps Ask and sets the growth factor to zero. The paper therefore does not show that escalation, rather than the base price of asking, produces the restraint it reports.
- Real attention may not follow this path. A person asked five questions may give shorter answers, stop answering, or answer with less care. None of these is modelled. The note covers only the two shapes the simulator assumes.
- Human fatigue measured in other settings, such as [[survey-satisficing-and-task-count]], concerns respondents on long questionnaires, not replies to an agent's questions. It supports the direction of the effect, not its size or form.

## Related

- [[elicitation-burden-tradeoff]] — a linear per-question burden with a non-monotonic optimum; a fixed price per question, where this note's price rises with use
- [[candidate-set-entropy-question-selection]] — names the question-fatigue versus premature-commitment tension that an escalating price puts a number on
- [[survey-satisficing-and-task-count]] — fatigue in human survey tasks, the closest measured analogue, in a different setting
- [[heterogeneous-action-cost-substitution]] — the action space in which this dialogue price competes with memory lookup and movement

[^c1]: arxiv-2512-18571 — "is a fatigue penalty factor"
[^c2]: arxiv-2512-18571 — "cost increased with each query (growth factor α = 0.2)"
[^c3]: arxiv-2512-18571 — "the probability of receiving a useful answer decays exponentially"
[^c4]: arxiv-2512-18571 — "asking is a limited resource"
[^c5]: arxiv-2512-18571 — "reduces unnecessary human interactions"
[^c6]: arxiv-2512-18571 — "To enable closed-loop evaluation without human-in-the-loop latency"
