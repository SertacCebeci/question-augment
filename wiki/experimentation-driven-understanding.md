---
description: "Comprehension of a system can be built by hypothesis, test and revision against its own behaviour, so a failed run corrects a reading that a description alone would keep."
aliases: ["design understanding via experimentation", "DUET", "understanding by experimentation", "experimentation loop"]
sources: ["arxiv-2512-06247"]
---
# Experimentation-driven understanding

A system described only by its text can be read and summarised, but the summary can be wrong in ways the text does not show. The experimentation loop adds a second route to comprehension: the answerer forms a hypothesis about how the system behaves, runs a test against the system through a tool, and uses the logged result to revise the hypothesis before the next test. The paper's own statement of the aim is a methodology for "developing Design Understanding via Experimentation and Testing"; in its setting the system is a hardware design written in SystemVerilog and the tools are a simulator, a formal verifier and a counterexample replicator.[^c1] The authors contrast this with "a one-off readthrough" of the code, and argue that understanding comes "via iterative experimentation using a number of tools."[^c2]

The mechanism is a loop that the agent steers. The agent chooses which experiment to run in each iteration and when to stop, and at the end writes a report of the hypotheses, tests and conclusions.[^c3] The useful property is that a hypothesis can fail in its own test, and the failure carries information. In the worked example, an agent describing a clock-stretching feature wrote a testbench encoding its hypothesis; the hypothesis "proved to be false" in the log, the agent analysed that result, and in later iterations it repaired the testbench and exercised the feature.[^c4] The authors summarise the lesson as "deep design behaviors from simple trial-and-error experimentation."[^c5]

The gain was measured on one design. The authors ran a baseline flow and an experiment-enabled flow on the same round-robin arbiter, with the same design summary and the same ten properties, and the baseline proved three properties while the experimental flow proved six.[^c6] Every property the authors counted as improved used the counterexample replication tool.[^c7] That tool is itself an agent that turns a formal counterexample into a simulation testbench, and it generally takes one to five simulator calls per use.[^c8] The authors read the effect as "the trial-and-error process of counterexample replication seems to produce deeper design understanding."[^c9] On property 1 the first formal attempt was wrong about timing; the replications showed that "behavior of the given property is more complex than originally proposed", and the property was refined and proved.[^c10]

For the asker-answerer transformation, the transferable piece is the structure rather than the hardware: a claim about a system becomes a test whose outcome can overturn the answerer's model before any judgement is made about the answer. Whether a question-asker gains the same from running experiments is my inference; the paper does not test it.

## Limits

- One design, ten properties, one attempt per flow: "Each flow is only given a single attempt to prove each property."[^c11] The text reports no repeated runs, so the size of the gap under variation is not known.
- The "improved" label is the authors' own rule: "we classify a property as having been improved if" a previously unproven or vacuous assertion became proven.[^c12] Two of the four improved cases were plain proofs; the other two were refinements, one of them only partial.
- The starting point is not guaranteed to be sound. The RTL-only design summary "may be incorrect."[^c13]
- Agents cheat in the test: some replications forced outputs to the expected values "instead of only manipulating the inputs."[^c14] The authors observe that such cases still helped understanding; that observation is not isolated by a test.
- The loop depends on the agent choosing to use it. Agents often try the goal first: "the agent will often attempt to achieve" it without the tools.[^c15] Simulation was used far more than formal, and "The formal tool was rarely used".[^c16] The authors suspect better prompting would change this, "though we suspect that with better prompt engineering and few-shot-examples" the formal use could rise, and they did not test it.[^c17]
- The authors expect the method to travel: "it is likely even useful outside of hardware and EDA applications."[^c18] The text does not test that. The text also reports no ablation that separates the experiments from the extra calls and tokens they cost, so the cause of the gain is not isolated.

## Related

- [[hypothesis-conditioned-query-rewriting]] — forms a working answer hypothesis and then searches to confirm or overturn it; here the test is an experiment on the system itself, not a retrieval.
- [[bayesian-experimental-design]] — picks the next experiment by expected utility; the loop here leaves the choice to the agent's judgement, with no criterion stated in the text.
- [[outcome-feedback]] — a returned verdict on an answer; the experiment returns how the system behaves, which can overturn the answerer's model without any judgement of an answer.
- [[availability-gated-branch-selection]] — scores which branch of a tree of experiments to expand by how much of its hypothesis space is still untested.
- [[tool-type-confidence-dichotomy]] — tool use moves an agent's confidence differently by tool kind; the paper's question is comprehension, not confidence.

[^c1]: arxiv-2512-06247 — "developing Design Understanding via Experimentation and Testing"
[^c2]: arxiv-2512-06247 — "via iterative experimentation using a number of tools."
[^c3]: arxiv-2512-06247 — "The AI agent has full control over what experiment it runs in each iteration and when to end experimentation."
[^c4]: arxiv-2512-06247 — "proved to be false."
[^c5]: arxiv-2512-06247 — "deep design behaviors from simple trial-and-error experimentation."
[^c6]: arxiv-2512-06247 — "doubles the number of proven properties to six, over the three proven in the baseline."
[^c7]: arxiv-2512-06247 — "Every improved property used the counterexample replication tool."
[^c8]: arxiv-2512-06247 — "calls (generally 1-5) to the simulation experimentation tool."
[^c9]: arxiv-2512-06247 — "replication seems to produce deeper design understanding."
[^c10]: arxiv-2512-06247 — "behavior of the given property is more complex than originally proposed"
[^c11]: arxiv-2512-06247 — "Each flow is only given a single attempt to prove each property."
[^c12]: arxiv-2512-06247 — "we classify a property as having been improved if"
[^c13]: arxiv-2512-06247 — "As this summary comes only from viewing the RTL, it may be incorrect."
[^c14]: arxiv-2512-06247 — "instead of only manipulating the inputs."
[^c15]: arxiv-2512-06247 — "the agent will often attempt to achieve"
[^c16]: arxiv-2512-06247 — "The formal tool was rarely used"
[^c17]: arxiv-2512-06247 — "though we suspect that with better prompt engineering and few-shot-examples"
[^c18]: arxiv-2512-06247 — "it is likely even useful outside of hardware and EDA applications."
