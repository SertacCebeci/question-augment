---
description: "For a prediction whose target lies outside a graph, paths are picked hop by hop by the gain each candidate adds to a frozen predictor's cross-entropy, then distilled into a cheap selector."
aliases: ["off-graph prediction", "information-gain path retrieval", "utility-aware graph path selection", "marginal-utility path retrieval"]
sources: ["arxiv-2512-23489"]
---
# Off-graph path selection

A graph can enter an LLM's reasoning in two roles. In in-graph question answering the answer is itself a node or relation inside the graph, so retrieval is a search for a route to it.[^c1] In off-graph prediction the target lies outside the graph and the graph is only evidence. In the venture-capital setting the prediction target, startup success, is outside the network, and "the graph serves solely as retrievable evidence."[^c2] The selection criterion follows from the role. A path is worth keeping for what it tells a predictor about an external label, not for where it ends. The paper states the contrast directly: graph-LLM methods that optimise entity and relation correctness do not select paths "by its marginal utility to an external predictor."[^c3]

## Mechanism

The selector works on an expansion tree grown from one target. The tree is breadth-first, of depth at most three, "retaining up to three previously unseen neighbors per node."[^c4] At each hop the same frozen LLM is asked to predict the outcome twice: once from the path so far, S, and once from S extended by one candidate neighbour. The gain of the candidate is then computed from the gold label. Its first term "rewards the reduction in the prediction error," in binary cross-entropy (the paper writes "CE denotes binary crossentropy").[^c5][^c6] A second term "encourages confidence once the correctness is taken into account."[^c7]

The gain is task-specific by construction. A neighbour that is structurally dense but does not move the predictor toward the correct answer earns little or nothing, whatever its topology. Gains are computed for failed companies as well as successful ones, and the selector is trained to "prefer extensions that push the LLMs towards the correct class with higher confidence."[^c8]

The greedy hop-by-hop choice is admitted to be approximate and is modelled on decision-tree splits: "Although this heuristic does not guarantee a globally optimal path, it provides an efficient approximation."[^c9] The gains then serve as offline labels. A selector receives the baseline and extended path, scores the three siblings at each hop, and is trained to rank them by gain. It is "trained offline using task-specific information gain signals computed by a frozen LLM, then deployed at inference to extract a compact set of high-value investment chains."[^c10] The gain labels come from a frozen Llama-3.1-8B classifier, which "returns the success probabilities."[^c12] The reason for the selector is the context budget: "Indiscriminately feeding all paths to an LLM overwhelms its context window and dilutes attention."[^c11]

## What was measured

In the authors' ablation, removing the graph-retrieval component "cuts Precision by 1.3% and F1 by 2.5%."[^c13] Feeding all three-hop neighbours, or picking paths at random, also degrades results: "Both naively concatenating all 3-hop neighbors and picking paths at random degrade performance."[^c14] In the error analysis, "correctly classified startups had longer retrieved paths (4.44 vs. 3.31)." That is a correlation, which the authors read as richer context aiding reasoning. It is not an intervention on path length.[^c15]

## Limits

- One dataset. "We trained and evaluated MIRAGE-VC solely on PitchBook," a proprietary set. The public alternative was judged "too outdated for modern LLM-based prediction."[^c16][^c20] Nothing in the text shows the selector transfers to other data.
- Off-graph generalisation is asserted, not tested. The conclusion says "This paradigm extends naturally to other off-graph tasks such as recommendation and risk assessment."[^c17] The experiments I read are on VC only; the recommendation and risk cases are the authors' extension.
- The gain needs a label. Training gains are computed from the gold outcome, so the selector learns from labelled history. Whether its choices stay good on a later period is not measured in the text (my inference).
- The labeller and the reader differ. Gains come from an 8B classifier, while the main results use GPT-3.5-turbo, which the authors call limiting.[^c18] They also flag "a potential data-leakage risk with newer LLMs," which is why the main table keeps the older model.[^c19] Whether paths chosen for one predictor help a different reader is not tested in what I read (my inference).
- The ablation table has rows whose full-model comparison I did not verify in the slice I read. The selector's margin over random picking is therefore the authors' claim, not a number I checked (my inference).
- The method is greedy and not globally optimal, as the authors concede. Its gains are per-target and per-hop, so it says nothing about how paths interact across targets.

## Related

- [[information-utility-retrieval-control]] — also scores each retrieval step by a gain in answer likelihood, but on a search agent's own trace, mixed with a novelty term, and only as a training-time monitor. Here the gain is a label for a separately trained selector that is deployed at inference.
- [[expected-information-gain]] — the decision-theoretic quantity a realised gain approximates. The paper's gain is one observed difference against a known label, not an expectation over outcomes.
- [[cross-domain-evidence-integration]] — the same paper also fuses three evidence streams through a learned gate. That integration question is a different concept and is not written in this note.

[^c1]: arxiv-2512-23489 — "where the answer is a node within"
[^c2]: arxiv-2512-23489 — "the graph serves solely as retrievable evidence"
[^c3]: arxiv-2512-23489 — "selecting multi-hop evidence by its marginal utility to an external predictor"
[^c4]: arxiv-2512-23489 — "retaining up to three previously unseen neighbors per node"
[^c5]: arxiv-2512-23489 — "the first term rewards the reduction in the prediction error"
[^c6]: arxiv-2512-23489 — "CE denotes binary crossentropy"
[^c7]: arxiv-2512-23489 — "the second encourages confidence once the correctness is taken into account"
[^c8]: arxiv-2512-23489 — "the selector is explicitly trained to prefer extensions that push the LLMs towards the correct class with higher confidence"
[^c9]: arxiv-2512-23489 — "Although this heuristic does not guarantee a globally optimal path, it provides an efficient approximation"
[^c10]: arxiv-2512-23489 — "then deployed at inference to extract a compact set of high-value investment chains"
[^c11]: arxiv-2512-23489 — "Indiscriminately feeding all paths to an LLM overwhelms its context window and dilutes attention"
[^c12]: arxiv-2512-23489 — "returns the success probabilities"
[^c13]: arxiv-2512-23489 — "Removing the graph retrieval component significantly cuts Precision by 1.3% and F1 by 2.5%"
[^c14]: arxiv-2512-23489 — "Both naively concatenating all 3-hop neighbors and picking paths at random degrade performance"
[^c15]: arxiv-2512-23489 — "correctly classified startups had longer retrieved paths (4.44 vs. 3.31)"
[^c16]: arxiv-2512-23489 — "We trained and evaluated MIRAGE-VC solely on PitchBook"
[^c17]: arxiv-2512-23489 — "This paradigm extends naturally to other off-graph tasks such as recommendation and risk assessment"
[^c18]: arxiv-2512-23489 — "Given the limitations of GPT-3.5-turbo"
[^c19]: arxiv-2512-23489 — "a potential data-leakage risk with newer LLMs"
[^c20]: arxiv-2512-23489 — "too outdated for modern LLM-based prediction"
