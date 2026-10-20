---
description: "Construal selection changes what kind of problem a fixed model takes an input to be; answer accuracy alone cannot show it, so the answer must be paired with its supporting facts."
aliases: ["task construal", "prompt-induced task framing", "answer-support organization"]
sources: ["arxiv-2512-12688"]
---
# Construal selection

Construal selection is the deepest of the three levels, and the one that concerns the task as a whole. "Construal selection concerns the organization of the task as a whole."[^k1] The contrast the paper draws is with the two levels below it: frames "guide the criteria for judgment" and salience "guides the foregrounding of information", while "construal determines what kind of problem the model treats the input as posing."[^k2] The paper's first sentence on the subject puts it plainly: "The same input can thereby be treated as" a classification, verification, reasoning, comparison or evidence-selection problem.[^k3]

The test case is multi-hop question answering. The same question and context can be presented as a direct-answer task, a supporting-facts-first task, a bridge-reasoning task, or a comparison task. "A direct-answer prompt centers the final response."[^k4] A supporting-facts-first prompt organizes the task around the evidential path, a bridge prompt makes intermediate entities central, and a comparison prompt foregrounds distinctions between entities. Each of these is a different organization of the same input, and the output is expected to show it.

What is measured is the coupling between answer and support. "The main object of analysis is the relation between answers and supporting structure."[^k5] The paper's reason is that the two can come apart: "A model can produce the correct answer without selecting the appropriate supporting facts" and can also identify relevant facts without producing the correct answer.[^k6] So it defines a joint score per example, the product of answer F1 and supporting-fact F1, which "is high only when the model both answers the question and selects appropriate supporting facts."[^k7] The construal effect is then a type-matched gain: bridge prompts on bridge questions and comparison prompts on comparison questions, each compared with the direct-answer baseline. "Construal selection therefore cannot be captured by answer accuracy alone."[^k8]

The paper places construal below salience in difficulty, because it asks for more: it "asks the model to reorganize the task as a structured procedure involving intermediate support, reasoning type, or answer–evidence coordination."[^k9] The paper's reading of its own results is that construal effects are "less uniform" than frame effects.[^k10]

The concept also points outside the prompt. The paper says that "task-level organization may require decomposition, routing, verification, structured outputs, or tool-mediated intermediate steps", which places construal at the level of the harness rather than the wording.[^k11]

## Limits

- The construal results come from one benchmark family, multi-hop QA, in English. The paper's own statement of scope is that the study "focuses on three English-language benchmark tasks".[^k12]
- The prompts were hand-written, and the paper says future work should "test paraphrased prompt families and broader prompt" distributions to separate category effects from wording effects.[^k13] A construal label such as "bridge" names a family of wordings; the effect of the category itself is not yet separated from the effect of one phrasing.
- The paper states that a single prompt may not be enough: its own discussion of harnesses says construal may need structure "beyond a single prompt". Where a prompt alone sustains a construal, and where it does not, is not measured here.[^k14]
- The term is borrowed from cognitive grammar, where meaning is conceptualization and "the same content can be profiled, focused, and construed in different ways".[^k15] What survives the transfer is that one content admits several construals. What does not is any claim about human conceptualization: the paper measures answer–support coupling in a model, not construal in a person.
- Whether the type-matched gains are positive, and by how much, depends on the model and the question type. The text read here does not establish a general direction for them, and I have not read the full HotpotQA result tables.

## Related

- [[frame-activation]] — the criterion level below: wording moves the judgment rule with the input fixed
- [[salience-control]] — the foregrounding level below: wording moves which evidence is central
- [[answer-structure-specification]] — a query can be given an expected answer structure so the answer can be checked; construal is the prompt-side choice of what structure the answer is taken to have, which is my reading and not the paper's claim

[^k1]: arxiv-2512-12688 — "Construal selection concerns the organization of the task as a whole."
[^k2]: arxiv-2512-12688 — "construal determines what kind of problem the model treats the input as posing"
[^k3]: arxiv-2512-12688 — "The same input can thereby be treated as"
[^k4]: arxiv-2512-12688 — "A direct-answer prompt centers the final response."
[^k5]: arxiv-2512-12688 — "The main object of analysis is the relation between answers and supporting structure."
[^k6]: arxiv-2512-12688 — "A model can produce the correct answer without selecting the appropriate supporting facts"
[^k7]: arxiv-2512-12688 — "This score is high only when the model both answers the question and selects appropriate supporting facts."
[^k8]: arxiv-2512-12688 — "Construal selection therefore cannot be captured by answer accuracy alone."
[^k9]: arxiv-2512-12688 — "asks the model to reorganize the task as a structured procedure involving intermediate support, reasoning type, or answer–evidence coordination"
[^k10]: arxiv-2512-12688 — "so their effects are less uniform"
[^k11]: arxiv-2512-12688 — "since task-level organization may require decomposition, routing, verification, structured outputs"
[^k12]: arxiv-2512-12688 — "The present study focuses on three English-language benchmark tasks"
[^k13]: arxiv-2512-12688 — "so future work should test paraphrased prompt families and broader prompt"
[^k14]: arxiv-2512-12688 — "multi-step task construal may require external structure beyond a single prompt"
[^k15]: arxiv-2512-12688 — "the same content can be profiled, focused, and construed"
