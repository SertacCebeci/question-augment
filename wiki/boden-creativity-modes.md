---
description: "Boden's creativity modes as search regimes: combinational search imports a distant mechanism, exploratory search moves within fixed rules, transformational search rewrites the rules."
aliases: ["Boden's three modes of creativity", "combinational, exploratory and transformational creativity", "combinational creativity", "transformational creativity"]
sources: ["arxiv-2511-20471"]
---
# Boden's creativity modes as search regimes

Margaret Boden's three forms of creativity can be read as three procedures over a space of solutions, each defined by what it changes. The work writes the target problem as P, the immutable task requirements as H, and the mutable rules or assumptions as R; the admissible solutions are those that address P while satisfying H and R.[^b1] Under that formulation, combinational search changes the source structure a solution is built from, exploratory search changes the candidate while R stays fixed, and transformational search changes R itself.[^b2]

Combinational search works by importing structure. It proposes an analogue from a context that is functionally relevant to the target but unfamiliar, solves the analogue, abstracts the mechanism that made it work, maps that mechanism onto the target, and then evaluates the result.[^b3] The analogue has to meet two conditions at once, relevant and unfamiliar, which is what separates it from analogy used only to help a solver. The steps are explicit, so a failure can be assigned to analogue retrieval, mechanism abstraction or downstream transfer.[^b4] In the paper's ablation, removing the cross-domain transfer lowers the pairwise preference more than removing either of the other two operators.[^b5]

Exploratory search works locally. It starts from a candidate already explored and searches for neighbouring alternatives,[^b6] keeping the problem formulation and the rules fixed. Novelty comes from walking parts of the existing space that have not been visited, not from importing outside structure or changing the space.

Transformational search works on the frame. Boden describes it as changing the defining dimensions of a conceptual space so that possibilities the original space excluded become reachable.[^b7] The operator proposes alternative rule sets while keeping the immutable requirements, then solves under them. It adds a filter, because "Not every change to R constitutes a useful transformation"; only rule changes that keep the task and its core difficulty while opening a meaningfully different region are retained.[^b8]

What survives the transfer from cognitive science, and what does not. What survives is the distinction of what each mode changes: source, candidate, or rule. What the operator form does not carry over is Boden's account of creative acts in people, which the work does not test. The mapping to operators is the authors' interpretation of Boden, and the authors are explicit that "UoT does not claim analogy, iterative search, or rule modification as new primitives."[^b9] In my reading, the three operators are old techniques given a common vocabulary, and the vocabulary is what the note contributes.

## Limits

The modes are compared only as three variants of one framework, on one backbone family for the novel tasks and on two backbones for HypoArena. The ablations show that the operators do not account for the whole gain: for the exploratory mode, "suggests that its overall advantage is not driven primarily by mechanism switching alone".[^b10] The transfer operator is also not self-sufficient. The failure analysis finds that "C-UoT often loses retrieved mechanisms during final synthesis", so an analogy can be found and still not reach the answer.[^b11]

The work states that "The current implementation nevertheless depends substantially on the reasoning, search, abstraction," and transfer capabilities of the underlying foundation model.[^b12] So the modes describe what a search does, and how well it runs depends on the model that runs it.

The scores are judgments of novelty and utility, and "judgments of novelty, usefulness, and hypothesis quality may" reflect evaluator preference, as the authors themselves note.[^b13] Nothing here shows that a mode produces a better question; the work measures answers to tasks it set.

## Related

- [[creative-search-task-regime]] — which of the three modes performs best depends on the task's constraint and objective specificity; this note names the modes, that one says where each pays off.
- [[retrieval-analogical-warmstart]] — warm-start replays the nearest past instance of the same elicitation; combinational search instead seeks a distant, unfamiliar analogue.
- [[problem-solution-coevolution]] — changing the frame of a problem is the transformational mode seen from the answering side; the two notes describe the same movement from different sides (my reading).
- [[technique-novelty-divergent-creativity]] — scores how novel a solution is; the modes above say where a novel solution is supposed to come from.

[^b1]: arxiv-2511-20471 — "Let P denote a target problem, H immutable task requirements, and R mutable rules or assumptions"
[^b2]: arxiv-2511-20471 — "transformational reasoning changes R itself"
[^b3]: arxiv-2511-20471 — "Operationally, C-UoT proposes distant analogues, solves the source problem, abstracts the transferable"
[^b4]: arxiv-2511-20471 — "This explicit decomposition also makes the reasoning process inspectable, allowing failures to be localized"
[^b5]: arxiv-2511-20471 — "The largest ablation effect occurs for C-UoT, whose full variant is preferred in 58.3% of comparisons"
[^b6]: arxiv-2511-20471 — "starts from an existing candidate and searches for neighboring alternatives"
[^b7]: arxiv-2511-20471 — "Boden characterizes transformational creativity as changing the defining dimensions of a conceptual"
[^b8]: arxiv-2511-20471 — "Not every change to R constitutes a useful transformation"
[^b9]: arxiv-2511-20471 — "UoT does not claim analogy, iterative search, or rule modification as new primitives"
[^b10]: arxiv-2511-20471 — "suggests that its overall advantage is not driven primarily by mechanism switching alone"
[^b11]: arxiv-2511-20471 — "C-UoT often loses retrieved mechanisms during final synthesis"
[^b12]: arxiv-2511-20471 — "The current implementation nevertheless depends substantially on the reasoning, search, abstraction,"
[^b13]: arxiv-2511-20471 — "judgments of novelty, usefulness, and hypothesis quality may"
