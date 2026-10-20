---
description: "In an evaluation-and-operation chain, a weak early instrument cannot be repaired by later machinery, since each layer trusts what the previous one measured; upstream repair is the costly one."
aliases: ["repair asymmetry", "dependency chain of evidence", "upstream evidence loss", "reliability dependency chain"]
sources: ["doi-10-48550-arxiv-2608-13867"]
---
# Upstream repair asymmetry

Coding-agent reliability is treated here as a chain of evidence obligations rather than a list of parts. Measurement determines whether a difference is credible; grading turns observations into acceptance decisions; containment and recovery determine whether the record survives failure; retrieval determines which evidence reaches the agent; review determines who can challenge a result.[^c1] "Each layer determines what the next may trust."[^c2]

The mechanism is the asymmetry. Errors propagate forward: "A weak measurement can become a confident" grade, a weak grade can admit unsafe work, and an invalid review signal can steer more work toward the wrong configuration. "Downstream confidence cannot repair evidence" lost upstream.[^c3] The text states the asymmetry directly: "Later machinery is often easier to add than the earlier instrument" is to repair, yet "it is evaluated through that earlier instrument."[^c4]

Three examples in the text make the point concrete. "More samples cannot repair a task distribution that excludes production work."[^c5] More judges cannot repair a rubric that experts apply inconsistently. More agents cannot repair a retrieval boundary that treats an empty result as authoritative. Each case adds effort at a layer that inherits the defect.

The consequence for practice is an order of work. Before adding a grader, agent or retrieval stage, one asks which promise the surrounding system makes, which component owns it, what state survives failure, and what experiment would falsify it.[^c6] The text calls the result "a sequence of evidence obligations, not a list of subsystems."[^c7]

The framing is not new. The text cites Osterweil (1987) on software processes as software and Choi and Scacchi (1991) on a software factory as distributed infrastructure. What the monograph adds is the claim that autonomous workers change the failure model: they are nondeterministic, edit persistent code, call external services and can claim completion incorrectly.[^c8]

## Limits

- The asymmetry is an argument, not a measured quantity. The text presents the chain as "an organizing argument" and gives examples; it does not estimate how much more expensive upstream repair is.
- Its practices are "bounded engineering claims rather than universal rules," and their applicability depends on workload, permissions, failure costs and review capacity.[^c9]
- Several results come from repositories of millions to tens of millions of lines; the text says that transfer downward to a small repository "is an assumption to test rather than a default."[^c10]
- My inference: the asymmetry says what cannot be fixed later, not whether an upstream instrument is worth its cost in a given system. A cheap, imperfect early check may still be the right first step.
- The note's chain is the author's ordering of six layers. Other decompositions of the same system are not compared here.

## Related

- [[run-to-run-spread]] — the measurement layer at the head of the chain: one run is one draw
- [[chance-corrected-agreement]] — the grading layer, where agreement can look like validity
- [[repairability-attribution]] — classifying a failure as repairable before it updates a system; this note asks where repair is possible at all

[^c1]: doi-10-48550-arxiv-2608-13867 — "Measurement determines whether a difference"
[^c2]: doi-10-48550-arxiv-2608-13867 — "Each layer determines what the next may trust."
[^c3]: doi-10-48550-arxiv-2608-13867 — "Downstream confidence cannot repair evidence"
[^c4]: doi-10-48550-arxiv-2608-13867 — "Later machinery is often easier to add than the earlier instrument"
[^c5]: doi-10-48550-arxiv-2608-13867 — "More samples cannot repair a task distribution that excludes production work."
[^c6]: doi-10-48550-arxiv-2608-13867 — "what experiment would falsify the guarantee"
[^c7]: doi-10-48550-arxiv-2608-13867 — "The dependency chain is therefore a sequence of evidence obligations, not a list of subsystems."
[^c8]: doi-10-48550-arxiv-2608-13867 — "Autonomous workers change the failure model, not the problem"
[^c9]: doi-10-48550-arxiv-2608-13867 — "Its practices are intended to serve as bounded engineering claims"
[^c10]: doi-10-48550-arxiv-2608-13867 — "is an assumption to test rather"
