---
description: "An agent's action log can be encoded as a graph of temporal and subsuming-structure edges, from which loop, breadth and length metrics are read that the final outcome alone hides."
aliases: ["Graphectory", "trajectory graph", "action graph of an agent run", "process graph of agent trajectories"]
sources: ["arxiv-2512-02393"]
---
# Trajectory graph with process metrics

An agent run is a log of actions in the order they were taken. Graphectory turns that log into a directed graph. Each node is a distinct action, keyed by its type and arguments. Two kinds of edge connect the nodes: a temporal edge for each transition in the chronological order, and a structural edge when two actions "operate on subsuming entities within the problem space."[^c1] The subsuming relation is domain-specific: it "can vary depending on the problem domain," and in software repair it runs from directory to file to block.[^c2] Reasoning is deliberately not a node. The agents follow a ReAct pattern, so every action is preceded by a reasoning step, and the authors judged generic reasoning nodes unhelpful because such reasoning is hard to tell apart.[^c3]

Once the graph exists, it gives counts that a flat log does not. Node count is the number of distinct actions. Temporal edge count is the number of transitions. Loop count is the number of times the agent decides to repeat a previously executed action, and the average loop length is the number of actions that pass before such a repeat.[^c4][^c13] Maximum structural out-degree marks where effort is concentrated.[^c14] A companion object, Langutory, is "a compact, human-readable abstraction of the Graphectory" — a string over logical phases. For program repair the phases are "Localization, Patching, and Validation," so one run can be read as a sequence and compared with the planning the system was prompted to follow.[^c5]

Applied to 4000 trajectories from eight agent-model pairs, the measure separates outcomes.[^c15] "Across agents and backbone models, Graphectory of unresolved issues is consistently larger than that of resolved ones, with more back edges."[^c6] Node count also "is positively correlated with the strength of the backbone LLM," and the abstract ties larger graphs to "reflecting deeper exploration, broader context gathering, and more thorough validation."[^c7][^c16]

The authors are explicit about what the metrics can say. They "capture the extent of effort an agent performs to resolve a task," and "alone, their values cannot reveal whether the effort is useful or useless."[^c8] They are meant to relate effort to difficulty or to success: "they can be used to assess how the effort is aligned" with difficulty.[^c17] The structure is borrowed from classic software analysis. "For classic software systems, the inter-procedural control flow graph" captures execution semantics, and "Similarly, Graphectory serves as a structured representation of agentic trajectories."[^c9]

## What transfers

What survives the move from software agents to any other question-answering process is the construction, not the numbers. A graph of this kind needs a log of discrete, comparable actions and some notion of which actions act on which entities. A tool-using agent has these. A plain conversation with no actions does not, unless its turns are first given keys and a containment relation. That step is my inference; the paper does not attempt it.

## Limits

- The data are programming agents only: "We study agentic programming systems, namely SWE-agent [48] and OpenHands [45]," on SWE-bench Verified issues.[^c10] Other domains are named as possible but are not tested.
- The phase map was not produced automatically. "Two authors and a frontier LLM" labelled the actions, so the Langutory depends on a labelling step, even though the analysis that follows is automated.[^c11]
- The metric set is a choice: "This paper discusses the metrics that we believe are more general yet representative."[^c12] Other graph statistics would give other readings.
- Reported differences are correlations across runs. Larger graphs for unresolved issues do not show that the wandering causes the failure.
- Because reasoning is excluded from the nodes, two runs with identical actions but different reasoning look the same to the graph.

## Related

- [[process-report-alignment-evaluation]] — scores a research agent's process against its final report; here the object is one run's action graph, with no report
- [[intermediate-action-feedback]] — also moves evaluation from the final result to intermediate steps, but scores proposed actions rather than the path taken
- [[online-trajectory-monitoring-intervention]] — the same graph built incrementally during the run and used to interrupt it

[^c1]: arxiv-2512-02393 — "The nodes in Graphectory are agent actions, and two nodes are connected through an edge"
[^c2]: arxiv-2512-02393 — "represents a subsuming navigation relationship, which can vary depending on the"
[^c3]: arxiv-2512-02393 — "We only consider actions as nodes, and not reasoning, since agents follow the ReAct principle"
[^c4]: arxiv-2512-02393 — "Measures the number of distinct actions in the trajectory"
[^c5]: arxiv-2512-02393 — "human-readable abstraction of the Graphectory that represents language of trajectories"
[^c6]: arxiv-2512-02393 — "Across agents and backbone models, Graphectory of unresolved issues is consistently larger than that of resolved ones, with more back edges"
[^c7]: arxiv-2512-02393 — "is positively correlated with the strength of the backbone LLM"
[^c8]: arxiv-2512-02393 — "metrics capture the extent of effort an agent performs to resolve a task"
[^c9]: arxiv-2512-02393 — "Similarly, Graphectory serves as a structured representation of agentic trajectories"
[^c10]: arxiv-2512-02393 — "We study agentic programming systems, namely SWE-agent [48] and OpenHands [45]"
[^c11]: arxiv-2512-02393 — "two authors and a frontier LLM"
[^c12]: arxiv-2512-02393 — "This paper discusses the metrics that we believe are more general yet representative"
[^c13]: arxiv-2512-02393 — "repeat a previously executed action"
[^c14]: arxiv-2512-02393 — "Maximum out-degree considering structural edges, indicating effort focus"
[^c15]: arxiv-2512-02393 — "a systematic evaluation of 4000 trajectories"
[^c16]: arxiv-2512-02393 — "reflecting deeper exploration, broader context gathering, and more thorough validation"
[^c17]: arxiv-2512-02393 — "But they can be used to assess how the effort is aligned"
