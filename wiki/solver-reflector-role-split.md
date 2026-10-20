---
description: "In multi-agent debate, splitting agents into solvers that propose answers and reflectors that verify and weight them lets models with uneven critique skill still contribute."
aliases: ["solver-reflector partition", "WISE role split", "solver and reflector roles"]
sources: ["arxiv-2512-02405"]
---
# Solver-reflector role split

Multi-agent debate (MAD) is usually run with every agent doing the same job: each proposes an answer and reads the others' answers. The WISE framework splits the agents by job instead. Its abstract names the two roles as "Solvers, that generate solutions, and Reflectors, that verify correctness, assign weights, and provide natural language feedback."[^w1] A Solver writes a reasoning chain for the problem. A Reflector checks the Solvers' answers, gives each one a weight, and writes feedback on what to fix.[^w2]

The roles run in rounds. In each round the Solvers propose independently and the Reflectors assess and weigh those proposals.[^w3] A model orchestrator, itself an LLM, collects the Reflectors' responses, summarises the feedback, and poses questions back to the Solvers so they can refine their reasoning.[^w4][^w11] The weights also feed the aggregation. The paper's post-processing step, a modified [[dawid-skene-annotator-model]], incorporates "the joint error of both" Solvers and Reflectors when it picks a final answer across rounds.[^w5]

The motivation is a mismatch of skills. The paper's introduction observes that "agents with diverse abilities may excel at solving tasks but not at critiquing (or vice versa)."[^w6] A debate that asks every agent to both solve and critique assumes a balance that heterogeneous models do not have (my inference from the passage). The same passage names a second cost: "involving all agents in debate can generate a quadratic number of messages."[^w6][^w10] The partition is the paper's answer to both concerns, so the role split is a design for skill placement and for message count together.

The paper's conclusions state the result in these terms: "segregating agents into roles, as in WISE, enables a more effective division of abilities."[^w7] The measured gain sits in the main comparison, where WISE is "surpassing RECONCILE by 6.1% under the same setup."[^w8] RECONCILE is a debate in which agents are placed in a debate and "report their confidence in their proposed solutions."[^w12] Every agent there both answers and critiques, so the comparison is the closest thing in the text to a role-split versus no-role-split contrast, though it is not a controlled one.

## Limits

- The split is never isolated in the parts of the paper read here. The 6.1% gain over RECONCILE compares whole systems. Roles, reflector weights, the orchestrator and the Dawid-Skene aggregation all differ at once. The appendix ablations were not read in full, so a role-only comparison may exist there and was not checked (my reading).
- Reflector weights are only as good as the Reflector's calibration. The paper says modern MLLMs "tend to be overly confident," and that is the reason it gives for distrusting agents' self-reported confidence.[^w9] A Reflector that is confidently wrong would get a large weight. The paper's aggregation handles this through error estimates, not by fixing the Reflector (my inference from the text, not tested here).
- The orchestrator is an LLM. The split therefore depends on another model's judgement about which Solver to question and what to ask. The cost of that judgement is not measured separately here (my inference).
- The evidence is zero-shot vision-and-language problems: SMART-840, VisualPuzzles, EvoChart-QA and a generated SMART-840++ set. No open-ended reasoning task, and no setting without images, was tested for the role split.

## Related

- [[generate-then-verify-candidate-pipeline]] — the same generator-then-checker shape on candidate lists; the Reflector here also weights votes and feeds back across rounds.
- [[dawid-skene-annotator-model]] — the reliability model the paper uses to weight Solvers and Reflectors in aggregation.
- [[role-differentiated-parallel-elicitation]] — fixed roles asked in parallel, where the user picks among the outputs instead of an aggregator weighing them.
- [[disagreement-retention-in-debate]] — another answer to the message cost of full debate: choosing which responses to broadcast.

[^w1]: arxiv-2512-02405 — "Solvers, that generate solutions, and Reflectors, that verify"
[^w2]: arxiv-2512-02405 — "Solvers generate reasoning chains to tackle the problem, while Reflectors"
[^w3]: arxiv-2512-02405 — "Solvers independently propose solutions, Reflectors assess"
[^w4]: arxiv-2512-02405 — "we introduce a model orchestrator (itself an LLM)"
[^w5]: arxiv-2512-02405 — "incorporating the joint error of both"
[^w6]: arxiv-2512-02405 — "solving tasks but not at critiquing (or vice versa)"
[^w7]: arxiv-2512-02405 — "enables a more effective division of abilities"
[^w8]: arxiv-2512-02405 — "surpassing RECONCILE by 6.1% under the same setup"
[^w9]: arxiv-2512-02405 — "tend to be overly confident"
[^w10]: arxiv-2512-02405 — "involving all agents in debate can generate a quadratic number"
[^w11]: arxiv-2512-02405 — "summarizes feedback, and formulates actionable"
[^w12]: arxiv-2512-02405 — "report their confidence in their proposed solutions"
