---
description: "A vision-language model proposes object, property and action symbols; a grammar weights them by occurrence in positive versus negative examples; programs are ranked by accuracy."
aliases: ["vision-language programs", "VLP", "program induction over VLM-grounded symbols", "neurosymbolic visual concept induction"]
sources: ["arxiv-2511-18964"]
---
# VLM-grounded program induction

A rule is induced from a few labelled images by a three-stage pipeline in which the
vision-language model never states the rule itself. It is asked only for perception:
the model proposes candidate symbols for the task (objects, properties, actions), and
VLM-backed functions map each image to a structured description of those symbols.[^c1]
Those functions are terminals of a typed domain-specific language, and symbolic
operators (existence, and/or/not, counts, comparisons) compose them into a boolean
program that is run on each image.[^c1]

The search is probabilistic. The domain-specific language is turned into a
probabilistic context-free grammar, and the grammar is the prior over programs. The
method is training-free, so "most rules are assigned uniform probabilities"; the one
exception is the symbols the VLM discovered, which are weighted by how often they occur
in each class: a symbol "that occurs more frequently in positive examples is assigned
higher probability."[^c2][^c3] Because the VLM functions are evaluated once per image
before search, the enumeration itself runs over symbolic programs only.[^c4]

Candidates are ranked by a two-level criterion: accuracy on the labelled examples first,
prior probability only to break ties.[^c5] The top program is the induced rule, and it
can be executed on held-out images to infer labels. The search is bounded in practice:
a Heap Search run "with a 10-second budget" and a depth cap.[^c6]

## What it was measured to do

On Bongard-style few-shot tasks and 10-shot logical benchmarks, the authors compare
"five different base VLMs with and" without the pipeline.[^c7] The gain is reported as
"up to 13.5% on average across all datasets" in balanced accuracy.[^c8] The largest gains
fall on the synthetic CLEVR-Hans3 tasks: "the strongest improvements across all models
occur on the compositionally complex CLEVR-Hans3" dataset.[^c9] The authors read this as
a case where "structured reasoning offers greater advantages when perceptual uncertainty"
is high.[^c10] Against dedicated reasoning models, the pipeline is reported to need
"substantially fewer tokens than dedicated reasoning models, despite executing more
prompts."[^c11]

The mechanism claim is the decoupling itself: perception is a learned, flexible
interface, and the reasoning is a short, inspectable program. The paper's claim that
the program supports shortcut detection rests on the same readability: the authors say
programmatic structure lets one "provide human-interpretable explanations that enable"
shortcut mitigation.[^c12]

## Limits

- The program can only use symbols the VLM proposed. "VLP can only reason about
  symbols that have been retrieved during the symbol grounding stage."[^c13] A relevant
  property that the VLM never names cannot be induced at all, whatever the search budget.
- The pipeline is not immune to shortcuts: "VLP is not entirely free from shortcut
  learning."[^c14] The paper presents readability as a way to find shortcuts, not as a
  guarantee against them.
- The occurrence-based prior is estimated from the few labelled examples. With six
  positives and six negatives, the counts are noisy and the weighting can favour a
  spurious symbol that happens to co-occur with the positive class (my inference; the
  paper does not measure this).
- Results depend on decoding. Switching from sampling to greedy decoding lowered one
  model's score, and the authors note that "the small amount of exploration introduced by
  sampling might still be beneficial."[^c15]
- The gains are not uniform. Reading Table 1 myself, several cells are negative, for
  example one model on COCOLogic and another on Bongard-RWR; the reported "up to 13.5%"
  is an average-level headline, not a per-dataset guarantee.
- Accuracy-first ranking over a few examples can prefer a program that fits the examples
  by chance; the paper's held-out query accuracy is the only check against this (my
  inference).

## Related

- [[llm-guided-program-induction-smc]] — also induces programs from examples, but by
  sequential particle updates scored against human learning curves; here one enumeration
  over a grammar is scored by accuracy on the examples.
- [[neurosymbolic-text-to-logic-retrieval]] — the same division of labour (a model for
  perception, a logic for the check), but the rule there comes from a text query, not
  from labelled examples.
- [[clever-hans-effect]] — shortcut learning; a readable program is a target for finding
  such shortcuts, though the paper says it does not remove them.

[^c1]: arxiv-2511-18964 — "Rather than embedding reasoning inside the VLM, VLP leverages the model to produce structured visual descriptions that are compiled into neurosymbolic programs."
[^c2]: arxiv-2511-18964 — "Since VLP is trainingfree, most rules are assigned uniform probabilities."
[^c3]: arxiv-2511-18964 — "that occurs more frequently in positive examples is assigned"
[^c4]: arxiv-2511-18964 — "To improve efficiency, outputs of all VLM functions V"
[^c5]: arxiv-2511-18964 — "Candidate programs are ranked by a two-level criterion"
[^c6]: arxiv-2511-18964 — "with a 10-second budget"
[^c7]: arxiv-2511-18964 — "we compare the performance of five different base VLMs with and"
[^c8]: arxiv-2511-18964 — "up to 13.5% on average across all datasets"
[^c9]: arxiv-2511-18964 — "The strongest improvements across all models occur on the compositionally complex CLEVR-Hans3"
[^c10]: arxiv-2511-18964 — "structured reasoning offers greater advantages when perceptual uncertainty"
[^c11]: arxiv-2511-18964 — "substantially fewer tokens than dedicated reasoning models, despite executing more prompts"
[^c12]: arxiv-2511-18964 — "provide human-interpretable explanations that enable"
[^c13]: arxiv-2511-18964 — "VLP can only reason about symbols that have been retrieved during the symbol grounding stage."
[^c14]: arxiv-2511-18964 — "VLP is not entirely free from shortcut learning."
[^c15]: arxiv-2511-18964 — "the small amount of exploration introduced by sampling might still be beneficial"
