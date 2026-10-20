---
description: "Prompt-sensitive known knowledge is held in a model's parameters yet can fail under one phrasing and succeed under another, so a failed question is not proof the model lacks the answer."
aliases: ["PSK", "Prompt-Sensitive Known Knowledge"]
sources: ["doi-10-48550-arxiv-2412-12472"]
---
# Prompt-sensitive known knowledge

A model can hold a fact and still fail to produce it. The survey that formalizes the LLM knowledge boundary names this case prompt-sensitive known knowledge (PSK). Its definition places the knowledge inside the parameters, but the knowledge is "sensitive to the form of the prompt".[^c1] The category is therefore about the gap between possessing an answer and eliciting it, and the gap is opened by the question, not only by the model.

The definition is existential over two sets of expressions. Let Qk be every input-output pair that could verify a piece of knowledge k, and let Q̂k be the subset actually used to check the model. PSK holds when some expression in Qk gets the right answer with probability above a threshold, while some expression in Q̂k does not. The survey writes the success test as the predicted answer's probability exceeding a threshold ε. The first clause places the knowledge in the model; the second makes it prompt-sensitive. The survey's words for the first clause are that "appropriate expressions in Qk can be found for successful verification".[^c2]

The survey gives two ways the surrounding context pushes a model from a known answer to a wrong one. It states the pattern directly: "Even though LLMs possess the required knowledge, they often produce untruthful responses when"[^c3] the model is misled by context, which is the prompt-sensitive known case. The two forms are untruthful context, where "Incorporating false information into the context significantly biases LLMs",[^c4] and irrelevant context, where "extraneous details divert the model from generating" a precise answer.[^c5]

For someone asking, the consequence is that one phrasing is a sample of the model's knowledge, not a census of it. A question that is answered wrongly may hide a fact the same model returns under a different wording, and a question stuffed with misleading or irrelevant detail may lose a fact the model would otherwise give. My inference, not the survey's claim: a well-posed question with the distracting material removed is the cheapest way to move a fact from the prompt-sensitive region toward the prompt-agnostic one. The survey does not measure how often this recovery happens.

## Limits

- The survey defines PSK and illustrates it with context-driven failures. In the part read, it reports no count of how much knowledge falls in this category and no experiment that recovers it by rephrasing.
- Verification is finite. The survey says the prompt-agnostic nature of knowledge "can only be approximated using a limited subset" of expressions.[^c6] The same holds for PSK. One successful expression in Qk plus one failure in Q̂k places a fact in PSK, but no finite set of failed phrasings shows that no working phrasing exists. The label is positive-certified; its negation is not.
- The threshold ε is a free parameter. The survey's definition uses "output probability is larger than a threshold"[^c7] without fixing a value in the part read, so the boundary between PSK and the other types moves with the chosen threshold.
- The survey maps PSK onto the unknown-known cell of the Know-Unknow quadrant.[^c8] That is the survey's own mapping. The wiki's unknown known is a different thing: knowledge the asker holds but does not say, see [[tacit-knowledge]]. The two share only the shape "known, but not surfaced".

## Related

- [[knowledge-boundary]] — the three nested boundaries that PSK sits between, and the four-type taxonomy it belongs to.
- [[query-level-uncertainty]] — a pre-generation score that reads one prompt form. My inference: a PSK query can be scored as beyond the boundary when only that phrasing is read.
- [[knowledge-boundary-aware-reward]] — an answer-side solvability flag from sampled responses to one prompt. It varies the answer, not the phrasing, so it inherits the same blind spot. My inference, not a claim of that note.
- [[tacit-knowledge]] — the wiki's unknown known, held by the asker rather than the model.

[^c1]: doi-10-48550-arxiv-2412-12472 — "but is sensitive to the form of the prompt"
[^c2]: doi-10-48550-arxiv-2412-12472 — "found for successful verification"
[^c3]: doi-10-48550-arxiv-2412-12472 — "Even though LLMs possess the required knowledge, they often produce untruthful responses when"
[^c4]: doi-10-48550-arxiv-2412-12472 — "Incorporating false information into the context significantly biases LLMs"
[^c5]: doi-10-48550-arxiv-2412-12472 — "extraneous details divert the model from generating"
[^c6]: doi-10-48550-arxiv-2412-12472 — "In practice, however, the prompt-agnostic nature of k can only be approximated using a limited subset"
[^c7]: doi-10-48550-arxiv-2412-12472 — "output probability is larger than a threshold"
[^c8]: doi-10-48550-arxiv-2412-12472 — "can be viewed as a form of the known-knowns and the unknown-knowns"
