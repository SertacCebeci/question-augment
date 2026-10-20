---
description: "Clarification questions for a complex intent form a prerequisite hierarchy: independent ones go in one parallel turn, dependent ones wait for earlier answers, cutting logical conflicts and user load."
aliases: ["logical clarification", "dependency-ordered clarification", "complex intent decomposition"]
sources: ["arxiv-2601-08653"]
---
# Prerequisite-layered clarification

A complex intent is one that "can be decomposed into multiple elements" and "exhibits prerequisite dependencies among these elements."[^c1] Planning a trip has elements such as destination, dates and activities; the destination logically precedes the activities, because activity suggestions must be relevant to the chosen place. Earlier clarification systems, which ask either sequential single questions or one parallel table, implicitly assume the questions are independent. Liao et al. (Prism) argue that ignoring dependencies yields incoherent suggestions such as diving in Okinawa in December, which raises the user's cognitive load.[^c2]

## Mechanism

1. **Decompose.** The intent is matched to a stored schema (a 429-intent, 27-domain dataset called CID) or, if unmatched, built few-shot from the most similar schemas.[^c3]
2. **Find prerequisites.** GPT-4o predicts the prerequisite elements for each element. Human annotators then check counterexamples, for example whether "activities" can be clarified without first specifying "destination".[^c4]
3. **Layer.** Elements are put into layers under two constraints: elements in one layer are independent, and dependencies flow strictly from earlier to later layers.[^c5]
4. **Ask by layer.** Independent questions share one interactive table in one turn. Dependent questions are deferred to later turns, and each later layer is generated conditioned on the answers so far.[^c6]

The mechanism is a topological ordering of the question set: the number of turns equals the depth of the dependency graph, and the questions per turn equal the width of each layer. This reading is mine, not the paper's wording.

## What was measured

The paper measures a Logical Conflict Rate, "the proportion of clarification questions that violate prerequisite dependencies among intent elements."[^c7] The best model, trained with an intent-aware reward and self-evolved SFT/DPO tuning, reached 11.50% on the TIN test set, the lowest among the compared methods.[^c8] Against Mistral-Interact the authors report a 14.4% higher interaction rating and 34.8% lower task completion time.[^c9] Prior systems degraded when moved from simple to complex intent scenarios.[^c2]

## Limits

- The gain is bundled: layered structure, the reward and the tuning are trained together. The ablation of ordering alone is not isolated in the slices I read, so I do not claim the ordering alone causes the user-load gains.
- Dependencies come from an LLM-proposed, human-validated annotation of 429 common intents. Rare or novel intents rely on few-shot extrapolation, and its accuracy was not established here.
- Cognitive load is measured by proxies (rating, time, tokens). No load instrument is used on real users in the parts I read, and user responses in training are simulated.
- The hierarchy is assumed acyclic and strict, with no soft or mutual dependencies.

## Related

- [[inquitree]] — also encodes subtopic-level logical dependency as a DAG that gates what may be explored next
- [[unsolicited-task-switching-cost]] — another application of Cognitive Load Theory to assistant behaviour
- [[intent-discovery-versus-elicitation]] — the broader setting of eliciting user intent
- [[dependency-aware-checklist-scoring]] — scoring that also respects dependencies among items

[^c1]: arxiv-2601-08653 — "into multiple elements and (2) exhibits prerequisite dependencies"
[^c2]: arxiv-2601-08653 — "Failing to model these dependencies"
[^c3]: arxiv-2601-08653 — "paradigm based on the CID dataset: if the user intent matches an"
[^c4]: arxiv-2601-08653 — "checking counterexamples (e.g., verifying whether"
[^c5]: arxiv-2601-08653 — "(2) dependencies flow strictly from earlier to later"
[^c6]: arxiv-2601-08653 — "questions are grouped into an interactive table within a single"
[^c7]: arxiv-2601-08653 — "Indicates the proportion of clarification questions that violate prerequisite dependencies among"
[^c8]: arxiv-2601-08653 — "Prism achieves the lowest logical conflict"
[^c9]: arxiv-2601-08653 — "task completion time by 34.8% compared to Mistral-Interact"
