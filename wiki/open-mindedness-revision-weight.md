---
description: "Open-mindedness as a weight in [0,1] on how much an argument moves a stated belief; prompting agents to be open-minded raised their belief change, with model-dependent levels."
aliases: ["open-mindedness", "open-mindedness level"]
sources: ["arxiv-2512-06573"]
---
# Open-mindedness as a revision weight

In the belief-revision model used here, an argument pushes on an agent's stated belief strength, and the push is scaled by a single number. "The actual effectiveness of that argument depends on λα ∈ [0, 1], which is the open-mindedness of α."[^c1] The argument's force is a vector that tries to shift the strengths in some direction; the open-mindedness weight decides how much of that shift lands. A weight near zero leaves the belief where it was, whatever the argument says; a weight near one lets the argument move the belief in full.

The paper does not compute this update. It states the equation and then implements it through the prompt: "We operationalize this belief revision equation through our prompt design."[^c2] So the agent is told a level, from 1 (very low) to 5 (very high), and is asked to predict its own updated strength. The open-mindedness of the agent is therefore a prompted setting, not a parameter of the model that is read out and checked.

The measurable claim is that the setting does what it says. The authors' hypothesis was that "prompting LLMs to be open-minded will lead to more belief changes in their given belief boxes," and they report that "belief change from misaligned to aligned and from aligned to misaligned increases with the level of open-mindedness."[^c3] They test this two ways, by the change rate on the Aporia ethics set and by the Big Five Inventory-2 personality scale across the five levels. On the inventory, Phi-4 scores rise steadily, while "others achieved their highest scores at levels 3 or 4."[^c4] The model that changed least was the most reluctant: "GPT-4o-mini is very reluctant to change its belief, especially for the first two open-mindedness levels."[^c5] Across the three models, the authors conclude that "the agents behaved according to their corresponding level on the open-mindedness scale."[^c6]

The construct is not the one in the virtue literature. The authors contrast their setting with "actively open-minded thinking," which the cited work links to higher accuracy in judging arguments "regardless of prior beliefs."[^c7] Their weight is a disposition to revise on argument; it is not shown to improve judgment, so the two should not be read as one trait.

## Limits

- The inventory is not validated for this use. The authors say explicitly: "we do not make the claim that the BFI2 is validated for use with LLMs, nor that the traits it measures correspond to what we would call 'open-mindedness.'"[^c8] The agreement between the inventory and the belief-change rate is therefore a consistency check, not a second measurement of one quantity.
- The weight does not reach the top. Even at the highest level, "we observed persistent resistance to belief change by the target agent."[^c9] A level of 5 means "more open than the others," not "fully revisable," and the paper does not say what the residual resistance is.
- Levels do not map evenly to behavior across models. Llama-3.3 peaks on the inventory at level 3, and the paper reports that at high levels Phi-4's belief change "surpassed that of Llama-3.3, contrary to expectations based on the BFI-2 results."[^c10]
- The sample is small: 46 Aporia samples and 100 MMLU questions, three runs for the inventory and five for the debates, with one debate design. The pattern of who changes belief depends on the rule and the dataset.
- Whether a prompted level is a stable disposition across contexts, or only a framing that the model reads once, is not tested.

## Related

- [[belief-box]] — the stated belief whose strength this weight moves
- [[peer-group-size-belief-change]] — the same weight, held at its maximum, under group pressure
- [[debate-elicits-sycophancy]] — concession under argued pressure versus a direct question, a related measure of how a model yields
- [[receptivity-gated-counterfactual-nudge]] — gates an explanation on inferred receptivity; this weight is a set-point the prompt fixes rather than one inferred per listener (my contrast)

[^c1]: arxiv-2512-06573 — "that argument depends on λα ∈ [0, 1], which is the open-mindedness of α"
[^c2]: arxiv-2512-06573 — "We operationalize this belief revision equation through our prompt design."
[^c3]: arxiv-2512-06573 — "belief change from misaligned to aligned and from aligned to misaligned increases with the level of open-mindedness"
[^c4]: arxiv-2512-06573 — "others achieved their highest scores at levels 3 or 4"
[^c5]: arxiv-2512-06573 — "GPT-4o-mini is very reluctant to change its belief, especially for the first two open-mindedness levels"
[^c6]: arxiv-2512-06573 — "The agents behaved according to their corresponding level on the open-mindedness scale."
[^c7]: arxiv-2512-06573 — "a higher degree of actively openminded thinking is associated with higher accuracy in evaluating arguments, regardless of prior beliefs"
[^c8]: arxiv-2512-06573 — "we do not make the claim that the BFI2 is validated for use with LLMs"
[^c9]: arxiv-2512-06573 — "we observed persistent resistance to belief change by the target agent"
[^c10]: arxiv-2512-06573 — "surpassed that of Llama-3.3, contrary to expectations based on the BFI-2 results"
