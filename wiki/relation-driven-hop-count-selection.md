---
description: "The depth a knowledge-graph answer needs can be read from the relations a traversal activates, not only from the question; a relation mask raised KG-CoT accuracy by 3.4 and 8.2 points."
aliases: ["relation-driven hop selection", "adaptive hop-count selection", "relation activation mask", "question-only hop selection"]
sources: ["arxiv-2512-15219"]
---
# Relation-driven hop-count selection

Before a model walks a knowledge graph to answer a question, it has to fix how many hops to walk. The conventional selector reads the question and nothing else. RFKG-CoT argues that this input is incomplete, because the same question can need one hop or several depending on the relations the graph holds around its topic entity. The paper's own contrast is a direct "brother" relation, answered in "1-hop for direct" form, against "2-hop for indirect" father-son chains.[^c1] The question-only selector "relies solely on question features to determine hops", and the paper's claim is that it therefore "fails to adapt" to the graph.[^c2][^c3]

The mechanism keeps the question-based estimate and adds a record of what the traversal did. A relation activation mask, initialized to zero, is introduced "to track which relations are activated during reasoning."[^c4] Each reasoning step scores relations by their activation probability, and the mask accumulates the relations that step activates. A small network then maps the question representation concatenated with the mask to a score for each candidate hop count, and the depth is the argmax. In the paper's words, "We combine this mask with the original question q to determine the optimal number of hops H."[^c5] The depth becomes a joint function of the question and the part of the graph the question's reasoning actually touched. The concatenation is "converts the 768+m dimensional concatenated vector of q and mask to T dimensional vector."[^c6]

## What was measured

The paper reports one ablation with ChatGPT as the answering model. The relation mask alone, added to KG-CoT, moves accuracy from 82.1 to 85.5 on WebQSP and from 51.6 to 59.8 on CompWebQ; the paper summarizes this as the variant that "outperforms KG-CoT by 3.4 pp on WebQSP but 8.2 pp on CompWebQ."[^c7] The paper reads the larger CompWebQ gain as the mask "improving path quality by prioritizing relevant relations, particularly valuable for more complex reasoning scenarios."[^c8] That reading is the authors'. The slices read do not show path-level data that would test it directly.

## Limits

- The selector chooses among a fixed menu. The number of reasoning steps is set per dataset, and "the number of reasoning steps T was set to 2 for WebQSP and WebQuestions," with 1 for SimpleQuestions and 3 for CompWebQ.[^c9] A question that needs more hops than the cap is not tested, and the mask cannot add hops the menu lacks.
- The gain is not uniform across tasks. On single-hop SimpleQuestions the full model reaches 87%, and the paper attributes the modest gain partly to "the hop-count selector (designed for multi-hop tasks) has limited utility here."[^c10]
- The mask records the subgraph the traversal reached. The paper reports that "the correct answer appears in generated reasoning paths for 92.3% of WebQSP."[^c11] A depth chosen over a subgraph that lacks the answer cannot recover it. The mask improves the choice of depth, not the coverage of the graph.
- The graph reasoner is trained by "computing the L2 distance between e and a."[^c12] Four benchmarks, one fine-tuned question encoder (bert-base-uncased), and one training run per setting are what the slices read describe. No variance over seeds or splits appears there, so the reported gains are single point estimates.
- The conclusion says the approach "naturally supports incremental KG updates without retraining the LLM."[^c13] The experiments read do not test a changed graph, so that claim is untested here.

## Related

- [[hop-depth-difficulty-with-entropy-check]] — there a generator sets path length as the intended difficulty of a question; here the depth is chosen at answer time from the graph the question touches.
- [[stop-continue-criteria-in-retrieval-loops]] — a similar fixed-budget problem in a retrieval loop, where the decision is when to stop rather than how deep a single question's structure goes. My inference: the mask suggests a signal drawn from the evidence itself, but that paper's findings concern a different decision, so they do not transfer directly.
- [[symbolic-grounded-depth-gap]] — a chain found in a graph need not be realized in text. The mask decides which chains are walked; that note asks whether they can be said.
- [[retrieval-utilization-gap]] — the mask acts on what is retrieved, the retrieval side of that split. The few-shot path guidance in the same paper acts on how the paths are used.

[^c1]: arxiv-2512-15219 — "1-hop for direct"
[^c2]: arxiv-2512-15219 — "relying solely on question features to determine hops"
[^c3]: arxiv-2512-15219 — "yet the selector fails to adapt"
[^c4]: arxiv-2512-15219 — "to track which relations are activated during reasoning"
[^c5]: arxiv-2512-15219 — "We combine this mask with the original question q to determine the optimal number of hops H"
[^c6]: arxiv-2512-15219 — "converts the 768+m dimensional concatenated vector of q and mask to T dimensional vector"
[^c7]: arxiv-2512-15219 — "outperforms KG-CoT by 3.4 pp on WebQSP but 8.2 pp on CompWebQ"
[^c8]: arxiv-2512-15219 — "improving path quality by prioritizing relevant relations, particularly valuable for more complex reasoning scenarios"
[^c9]: arxiv-2512-15219 — "the number of reasoning steps T was set to 2 for WebQSP and WebQuestions"
[^c10]: arxiv-2512-15219 — "the hop-count selector (designed for multi-hop tasks) has limited utility here"
[^c11]: arxiv-2512-15219 — "the correct answer appears in generated reasoning paths for 92.3% of WebQSP"
[^c12]: arxiv-2512-15219 — "computing the L2 distance between e and a"
[^c13]: arxiv-2512-15219 — "naturally supports incremental KG updates without retraining the LLM"
