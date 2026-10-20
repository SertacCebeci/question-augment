---
description: "A query's skeleton is what survives stripping schema names and literal values; counting a model's errors per skeleton shows which query structures it fails on."
aliases: ["query skeletons", "SQL skeleton", "query template", "structural skeleton of a query"]
sources: ["arxiv-2511-18934"]
---
# Query skeleton

A query in SQL, Cypher or nGQL can be split into what belongs to one database and what belongs to the query's form. Remove the table and column names, node labels, edge types and literal values, and what remains is the skeleton: the syntactic and semantic shape of the query with open slots. The paper's premise is that many queries share such a shape: "many of them share the same underlying syntactic and semantic structures once instance-specific elements are stripped away."[^c1] In its figures a slot is written as a typed placeholder such as <COLUMN>, <LITERAL> or <TABLE>, so one skeleton stands for many concrete queries over many schemas.

The paper's claim is that this object is shared across languages: "We identify query skeletons as a shared optimization target of Text-to-Query tasks."[^c2] That is a claim about the task, not about any one dialect.

The mechanism the paper builds on the skeleton has three parts.

**Measuring a skeleton error.** A predicted query is compared with the gold query by structure, not by execution. Where a parser exists, both are parsed to abstract syntax trees and the number of non-keep edit operations is counted: "We define the AST-based structural distance as the total number of non-keep operations."[^c3] Where no mature parser exists, as for nGQL, the two skeletons are compared by token-level edit distance. An exact-match test is rejected because "this criterion is overly strict and may lead to false positives": some predicted and gold skeletons "differ slightly in structure but remain semantically equivalent," for instance by a DISTINCT keyword.[^c4] So a prediction is a skeleton error only when its distance passes a threshold, which the experiments set to 2.[^c13]

**Diagnosing a model by skeleton.** Given a target model, the training set is split by K-fold cross-validation, and the error rate is computed per skeleton. Skeletons whose error rate passes 20% form the error-prone set: "we select skeletons with an error rate above 20% to construct the error-prone skeleton set."[^c5] The count is per model, so the same skeleton can be hard for one answerer and easy for another.

**Using the diagnosis to generate.** A generator is fine-tuned on the error-prone skeletons to propose new ones, a teacher LLM instantiates each skeleton with elements of a given schema, a backward step turns the query into a question, and a forward step checks the pair with chain-of-thought. The backward step is the easier direction, and the paper's reason is the same asymmetry that matters for asking: "Since query languages are formal and semantically unambiguous, this backward translation is substantially easier than the forward direction."[^c6]

What was measured: the premise is supported by a per-skeleton failure count, with the observation that "even the most advanced open-source LLMs specialized in code still frequently fail to generate correct skeletons during inference."[^c7] The base models are Qwen2.5-Coder-7B and 14B, fine-tuned on the synthesized data.[^c12] Removing the diagnosis step is the ablation that bears on the mechanism: "Eliminating Dynamic Diagnosis and instead using the full set of skeletons from the original training set results in reduced performance."[^c8]

**Transfer to asking and answering (my inference, not tested in the paper).** Read against the wiki's own frame, a skeleton is an answer's form with its slots open, and the constraints an asker supplies are what fill those slots. An answerer who knows which structure a question calls for can see which slots remain. The paper never treats a natural-language question this way; the mapping is mine.

## Limits

- The measure exists only where the answer is a formal query with an execution or parse. The paper's experiments cover SQL (Spider and BIRD), Cypher (an executable subset of Text2Cypher) and nGQL (NL2GQL). Beyond SQL the authors say "the availability of high-quality datasets and standardized evaluation protocols remains limited."[^c9]
- The distance is a structural proxy, not a semantic one. A count of non-keep edits can call equivalent queries different, which the threshold tolerates rather than removes. The token-level fallback is coarser: "Although this approximation is less fine-grained."[^c10]
- The 20% cut and the threshold of 2 are design choices. In the passages read I did not find a sensitivity analysis over either.
- The diagnosis is per model and per task, and "the augmentation process is still performed independently for each task."[^c11] There is no single model across query languages: "The current setup does not support a unified model that can handle multiple query languages simultaneously."[^c11]
- I read the ablation summary, not the full table, so the size of each component's contribution is not stated here.
- Nothing in the text concerns questions a person asks. A skeleton presupposes a gold query; the transfer to open-ended questions has no such reference.

## Related

- [[entity-agnostic-reasoning-skeleton]] — also abstracts a structure away from instances, but there the abstraction is a plan over entity types for reasoning steps; a query skeleton is a fixed syntactic form whose slots a schema fills.
- [[confusion-targeted-question]] — counts a recognizer's errors per class and aims questions at its rivals; the same count-then-target move, with query skeletons as the classes and generated training data as the output.
- [[model-specific-difficulty-dispatch]] — difficulty is a relation between a task and one answerer; the per-skeleton error rate is that relation read over structures instead of whole tasks.

[^c1]: arxiv-2511-18934 — "many of them share the same underlying syntactic and semantic structures once instance-specific elements are stripped away"
[^c2]: arxiv-2511-18934 — "We identify query skeletons as a shared optimization target of Text-to-Query tasks"
[^c3]: arxiv-2511-18934 — "We define the AST-based structural distance as the total number of non-keep operations"
[^c4]: arxiv-2511-18934 — "this criterion is overly strict and may lead to false positives"
[^c5]: arxiv-2511-18934 — "we select skeletons with an error rate above 20% to construct the error-prone skeleton set"
[^c6]: arxiv-2511-18934 — "Since query languages are formal and semantically unambiguous, this backward translation is substantially easier"
[^c7]: arxiv-2511-18934 — "even the most advanced open-source LLMs specialized in code still frequently fail to generate correct skeletons during inference"
[^c8]: arxiv-2511-18934 — "Eliminating Dynamic Diagnosis and instead using the full set of skeletons from the original training set results in reduced performance"
[^c9]: arxiv-2511-18934 — "the availability of high-quality datasets and standardized evaluation protocols remains limited"
[^c10]: arxiv-2511-18934 — "Although this approximation is less fine-grained"
[^c11]: arxiv-2511-18934 — "the augmentation process is still performed independently for each task"
[^c12]: arxiv-2511-18934 — "we select two open-source models, Qwen2.5-Coder-7B and Qwen2.5-Coder-14B, as base models"
[^c13]: arxiv-2511-18934 — "set the threshold for skeleton error detection to 2"
