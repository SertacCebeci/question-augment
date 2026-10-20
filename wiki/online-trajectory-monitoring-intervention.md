---
description: "A monitor reads an agent's partial trajectory mid-run, flags loops, stagnation or skipped phases, and returns a diagnostic message; oscillation fell over 90% in one study."
aliases: ["online process monitoring", "diagnostic-message intervention", "trajectory monitor with rollback", "online monitoring and intervention"]
sources: ["arxiv-2512-02393"]
---
# Online trajectory monitoring with diagnostic intervention

A postmortem analysis of a trajectory says what went wrong after the run has ended.[^d16] The alternative keeps the same graph under construction during the run. "Online process-centric analysis requires incremental construction of Graphectory" and Langutory, and at each step the monitor checks the partial structure for plan compliance and for inefficiency signals.[^d1] The signals are four heuristics, each of which "can potentially (but not necessarily) indicate an inefficient or regressive behavior": a large loop, a mismatch between temporal and structural edges, a long stay in one phase, and a failed outcome.[^d2] The authors state that the heuristics are not fixed to the design: "more heuristics or even specific inefficiency patterns can be added later."[^d3]

Each signal leads to a different intervention. "For plan violation and oscillation cases, the intervention component suppresses the current step," dropping its thought-action-observation and returning only a diagnostic message. For a plan violation, such as submitting a patch before validating it, the paper says the intervention "may block the most recent action that triggered the intervention and revert" the trajectory, so the agent can refine its strategy.[^d4][^d14] An inefficiency signal is handled differently. There is no rollback, "since the history of taken actions may be required for reasoning about the steps given" the message.[^d5] The message is a template, for instance "A repeating cycle of actions" followed by a request to summarise the failing behaviour and choose one decisive next step.[^d15]

The implementation was on SWE-agent. From 153 problematic trajectories, "This yielded 86 reproducible problematic trajectories (out of 153)," kept only where the issues "persisted in at least two runs."[^d6] Under monitoring, the authors report that the setting "substantially reduce[s] oscillatory behavior across all models (by over 90%)," shortens trajectories, and raises resolution by "6.9% to 23.5% on studied instances."[^d7] The overhead is small by the authors' measure, "less than 10 milliseconds" in the setting studied.[^d8]

On my reading, the mechanism is a rule over a growing graph, not a model of the agent's beliefs. The rule responds to the shape of the path (a loop repeating without progress, or several steps with no edit) and tells the agent what the shape means. Whether that changes what the agent believes is a separate question the paper leaves to the outcome measure.

## Limits

- The gains are measured only on instances that were already problematic. The vanilla baseline counted an instance as resolved "only if all reproducible runs" resolved it, a stricter criterion than the monitored runs faced.[^d9]
- The heuristics signal inefficiency only potentially, and the thresholds are set by hand. The stagnation rule fires after "spending at least 5 steps in navigation without any edit."[^d10]
- Plan compliance improved less than oscillation did: "is improved as well, although to a lesser extent compared to oscillatory behavior."[^d11] Agents may judge the task finished and skip validation: "they might still submit a patch without validation, despite" being told to test.[^d12]
- Only one framework was re-executed: "We re-executed SWE-agent with integrated online monitoring and intervention (OMI setting)."[^d13] Other agents, and other kinds of monitor, are not tested.
- The monitor needs discrete actions and a phase plan. Whether a question-asking or answering dialogue has either is my inference, not shown here.

## Related

- [[trajectory-graph-process-metrics]] — the graph and metrics this monitor reads; there they are read after the run, here during it
- [[intermediate-action-feedback]] — also acts on intermediate steps, but its signal is a proposed action, not a pattern in the path
- [[self-reinforcing-repetition-loop]] — the decoding-level loop that the oscillation rule catches at the level of the trajectory
- [[watchdog-outcome-escalation]] — a bounded retry-or-escalate policy on an execution outcome; a physical-system counterpart to a rule-based monitor

[^d1]: arxiv-2512-02393 — "requires incremental construction of Graphectory"
[^d2]: arxiv-2512-02393 — "We identify a series of heuristics that can potentially (but not necessarily) indicate an inefficient or"
[^d3]: arxiv-2512-02393 — "The heuristics are orthogonal to our design, i.e., more heuristics or even specific inefficiency patterns can be added later"
[^d4]: arxiv-2512-02393 — "For plan violation and oscillation cases, the intervention component suppresses the current step"
[^d5]: arxiv-2512-02393 — "rollback, since the history of taken actions may be required for reasoning about the steps given"
[^d6]: arxiv-2512-02393 — "This yielded 86 reproducible problematic trajectories (out of 153)"
[^d7]: arxiv-2512-02393 — "substantially reduce oscillatory behavior across all models (by over 90%)"
[^d8]: arxiv-2512-02393 — "less than 10 milliseconds"
[^d9]: arxiv-2512-02393 — "Under the vanilla setting, an instance is considered resolved only if all reproducible runs"
[^d10]: arxiv-2512-02393 — "spending at least 5 steps in navigation without any edit"
[^d11]: arxiv-2512-02393 — "is improved as well, although to a lesser extent compared to oscillatory behavior"
[^d12]: arxiv-2512-02393 — "they might still submit a patch without validation, despite"
[^d13]: arxiv-2512-02393 — "We re-executed SWE-agent with integrated online monitoring and intervention (OMI setting)"
[^d14]: arxiv-2512-02393 — "interventions may block the most recent action that triggered the intervention and revert"
[^d15]: arxiv-2512-02393 — "A repeating cycle of actions is detected"
[^d16]: arxiv-2512-02393 — "when performed postmortem at the end of the trajectory"
