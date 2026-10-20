---
description: "Prior dialogue complexity raises cognitive load and selectively amplifies the framing effect (not status quo bias); LLMs given dialogue context partly reproduce this load-bias interaction."
aliases: ["load-bias interaction in conversation", "dialogue complexity as cognitive load proxy"]
sources: ["arxiv-2601-11049"]
---
# Dialogue complexity amplifies the framing effect

In a pre-registered study (N = 1,648), participants answered six classic choice problems through a chatbot after prior dialogues of varying complexity. Two biases appeared: the framing effect and status quo bias.[^c1] The authors treat the complexity of earlier dialogue as a proxy for cognitive load, so the same question is asked under different mental demand depending on what came before it.

## What was found

- Higher dialogue complexity raised both reported and measured load (t = 9.475, p < .001, d = 0.59).[^c2]
- The raised load selectively increased susceptibility to the framing effect. Status quo bias was not affected.[^c3] The authors suspect their binary choice task was too simple for load to matter there, and call this speculative.[^c3]
- LLMs (GPT-4 family, GPT-5, open-source) were asked to predict individual decisions from demographics plus prior dialogue. Adding dialogue context made predictions significantly more accurate in several scenarios, though the gain depended heavily on the choice problem.[^c4]
- The models reproduced the human bias patterns and load-bias interactions. The GPT-4 family aligned best with humans, ahead of GPT-5 and open-source models.[^c1b]
- Perturbing human utterances changed little. The authors conclude the models lean on the structure of the prior dialogue, not fine-grained human responses.[^c5]
- Sensitivity to load stayed limited unless the prompt explicitly asked for it. Explicit bias prompting in the status quo task led to overestimation.[^c6]

## Why it matters for asking and answering

For an asker, the same framed question is answered differently depending on the load carried by preceding turns, so wording effects are not constant across a conversation. For an answerer or simulator, context history is a predictive signal for how biased the reply will be. This reading is my inference from the findings, not something the study tested directly.

## Limits

- Six choice problems, two biases; results varied by problem, and the authors call the predictive results "mixed".
- The load manipulation is a proxy (dialogue complexity), validated by self-report and a measured index, not by direct manipulation of working memory.
- The explanation for the null status quo result is speculation by the authors.
- LLM prediction accuracy is not shown to carry over to other biases, tasks or populations.

## Related

- [[diagnostic-anchoring-in-agentic-llms]] — another cognitive bias studied in LLM-mediated settings
- [[problem-framing]] — a different sense of framing (problem setting), not the gain/loss wording effect here

[^c1]: arxiv-2601-11049 — "demonstrating the load-bias interaction."
[^c2]: arxiv-2601-11049 — "confirming that increased prior dialogue complexity increased both perceived and measured cognitive load."
[^c3]: arxiv-2601-11049 — "increased dialogue complexity selectively increased susceptibility"

[^c4]: arxiv-2601-11049 — "the degree of improvement varied by task and was highly dependent on the choice problem."
[^c1b]: arxiv-2601-11049 — "Across all models tested, the GPT-4 family"

[^c5]: arxiv-2601-11049 — "This suggests that the models are primarily"
[^c6]: arxiv-2601-11049 — "explicit bias prompting (HL3 in Status quo bias experiments) led to overestimation,"
