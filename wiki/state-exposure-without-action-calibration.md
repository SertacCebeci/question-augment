---
description: "Adding a retrieval controller's own state (query profile, trace hints) to its prompt makes trajectories easier to inspect but lowers ranking unless the action policy is calibrated."
aliases: ["TraceBound", "profile and trace conditioning", "trace-conditioned controller prompt"]
sources: ["doi-10-48550-arxiv-2607-24800"]
---
# State exposure without action calibration

An adaptive retrieval agent picks, at each step, among a few actions: run a global search, expand a node's neighbourhood, or emit the final answers. Its prompt holds the query, the tool descriptions and the observations so far. The intervention studied here adds two kinds of text to that prompt. The first is a compact query profile, written before the first call, with a predicted answer type, query facets, relation hints and retrieval risks. The second is a short trace hint, written after an observable symptom such as a repeated call, an empty neighbourhood or a spent budget. The hints are deliberately weak: "The trace hint is not an oracle."[^c1] It cannot tell whether a retrieved node is correct, and it summarises only what the controller can observe.

The finding is that this exposure makes the process easier to read without making the answer list better. The graph, the tools, the gold labels and the ranking metrics are held fixed, so only the controller's context and its logging change. Under open-weight Qwen3 controllers the combined agent does worse than the unconditioned one. In the validation ablation the unconditioned agent at a 12-step budget reaches the best average MRR of .4087, while "the complete TraceBound agent obtains .3141 at 12 steps."[^c2] On the held-out subset every paired delta is negative, and on MAG "TraceBound reduces MRR from .7711 to .4974."[^c3] The authors state the result in one sentence: "profile and trace conditioning make trajectories easier to analyze, but they do not improve final ranking in this implementation."[^c4] The profile-only and trace-only variants also fall below the baseline, "showing that the degradation is not caused by only one component."[^c14]

The mechanism they propose concerns the policy, not the wording. The profile and hints change which action the controller takes in a given state, and the paper's design statement is that signals of this kind, "injected into a retrieval controller without a calibrated action policy, they may change the trajectory without improving the ranked answer list."[^c5] The object that matters is "the conditional distribution over actions, not the mere presence of a trace string."[^c6] A hint that says a call repeated and an anchor should change is an instruction only to a controller that already knows when an anchor change pays. The text does not show that such knowledge is absent in the tested controllers, but nothing in the paper shows it present. This reading is my inference, not the paper's wording. It is the same point as [[calibration]] applied to actions rather than to confidence.

The process counters are what localise the loss. Each trajectory is logged as global calls, neighbourhood calls, zero-result calls, repeated calls and budget used, and these are paired with the ranking of the same query. The paper finds that "repeated calls and zero-result calls are associated with substantially larger negative rank deltas."[^c7] The counters are read from trajectories only, and the ranking only from the final list, so the two are kept apart by design.

A cap on interaction length is the obvious alternative, and the paper tests it with "a lower step budget and tighter caps on global and neighborhood" calls.[^c33] Its abstract reports that stricter budgets "shorten trajectories without repairing the policy."[^c8] The body states the same as "a stricter budget reduces trajectory length without recovering accuracy."[^c9] A cap therefore changes how long the controller keeps searching but not which nodes it searches for, which matches the paper's view that the failure is in action selection. The paper frames the transferable lesson as this: "thinking before retrieval" must be evaluated as a control problem over action selection, not as a prompt-format change.[^c10]

The same pattern appears in the wider prompt literature. [[task-conditional-prompt-gain]] records that a prompting strategy can help one stage of a workflow and hurt another. Here the sign was negative in every graph, budget and model that was run, so the effect is not a sign flip across tasks but a consistent loss.

## Limits

- The authors caution that the result holds "in this implementation." The controllers are open-weight Qwen3 models (14B for the validation ablation, 30B-A3B for the held-out subset), with no closed model tested. The paper says "We avoid training or test-set tuning," so the controllers were never trained to use the hints, and a trained action policy is exactly the untested case.[^c11]
- The profile is not a user state. "Our experiments do not introduce real user profiles; the profile in TraceBound is query-derived."[^c12] The paper is motivated by personalised retrieval, but no personal signal is tested.
- Sample sizes are modest. "The validation ablation uses 100 examples per graph."[^c13] The held-out subset is about 300 queries per graph with one controller.
- The budget result is read here from the abstract and the description of the probe. The probe's own table was not read in this pass, so the size of the budget effect is not stated in this note.
- The paper is a single-author workshop paper: it is "Accepted at the Failure Modes in Agentic AI (FAGEN) Workshop at ICML 2026."[^c15] Its claims are about one ARK-style code path on STaRK, and its failure is not shown to hold for other retrieval agents.
- Whether a dialogue for asking or answering questions has a comparable action set, with stops and probes that a hint could mis-steer, is not tested here. That transfer is my inference.

## Related

- [[calibration]] — the same requirement on confidence scores; here it is required of the action choice.
- [[stop-continue-criteria-in-retrieval-loops]] — hard step and token budgets as the usual stop rule, the budget side of the same finding.
- [[trajectory-graph-process-metrics]] — process counters read from an action log, the instrumentation this paper pairs with rank deltas.
- [[online-trajectory-monitoring-intervention]] — a monitor that returns a diagnostic message and also suppresses or rolls back the step; my reading is that the message alone, as prompt text, is the part this paper finds insufficient.
- [[task-conditional-prompt-gain]] — prompt strategies whose effect depends on the task.

[^c1]: doi-10-48550-arxiv-2607-24800 — "The trace hint is not an oracle."
[^c2]: doi-10-48550-arxiv-2607-24800 — "the complete TraceBound agent obtains .3141 at 12 steps"
[^c3]: doi-10-48550-arxiv-2607-24800 — "On MAG, the most severe case, TraceBound reduces MRR from .7711 to .4974."
[^c4]: doi-10-48550-arxiv-2607-24800 — "profile and trace conditioning make trajectories easier to analyze, but they do not improve final ranking in this implementation"
[^c5]: doi-10-48550-arxiv-2607-24800 — "if profile-like signals are injected into a retrieval controller without a calibrated action policy, they may change the trajectory without improving the ranked answer list"
[^c6]: doi-10-48550-arxiv-2607-24800 — "the important object is the conditional distribution over actions, not the mere presence of a trace string"
[^c7]: doi-10-48550-arxiv-2607-24800 — "repeated calls and zero-result calls are associated with substantially larger negative rank deltas"
[^c8]: doi-10-48550-arxiv-2607-24800 — "stricter interaction budgets shorten trajectories without repairing the policy"
[^c9]: doi-10-48550-arxiv-2607-24800 — "a stricter budget reduces trajectory length without recovering accuracy"
[^c10]: doi-10-48550-arxiv-2607-24800 — "must be evaluated as a control problem over action selection, not as a prompt-format change"
[^c11]: doi-10-48550-arxiv-2607-24800 — "We avoid training or test-set tuning"
[^c12]: doi-10-48550-arxiv-2607-24800 — "Our experiments do not introduce real user profiles; the profile in TraceBound is query-derived"
[^c13]: doi-10-48550-arxiv-2607-24800 — "The validation ablation uses 100 examples per graph"
[^c14]: doi-10-48550-arxiv-2607-24800 — "showing that the degradation is not caused by only one component"
[^c15]: doi-10-48550-arxiv-2607-24800 — "Accepted at the Failure Modes in Agentic AI (FAGEN) Workshop at ICML 2026"
[^c33]: doi-10-48550-arxiv-2607-24800 — "a lower step budget and tighter caps on global and neighborhood"
