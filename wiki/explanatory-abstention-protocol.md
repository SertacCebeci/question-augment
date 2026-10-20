---
description: "A framework where a sub-agent's abstention returns a labeled failure category and rationale to its coordinator, for clarification, rerouting, or fallback instead of a refusal."
aliases: ["EARS", "Explanatory Abstention for Reliable Sub-Agent Modeling", "explanatory abstention protocol"]
sources: ["xie-2026-ears"]
---
# Explanatory abstention protocol (EARS)

> In a centralized multi-agent system, a sub-agent that cannot answer does not
> silently refuse or hallucinate — it returns a structured failure state that
> the coordinator can act on, turning "I can't" into a signal the asker's side
> of the system can route on.

## Definition / Mechanism

EARS targets a centralized coordinator–sub-agent architecture: a coordinator
routes a user request to a lightweight, domain-specialized sub-agent, which
either answers or must abstain. Two stages produce the behaviour. First, an
offline [[calibration]] stage: human annotators label a seed set of interactions
under a four-category taxonomy, then an ensemble of three LLM-as-a-Judge
models (from three different providers) is calibrated against that seed set
by iteratively revising its instructions until its category-prediction
accuracy clears a threshold and stops improving. Second, an online data
flywheel: the calibrated judge ensemble labels large-scale production
interactions (accepting a label only on unanimous agreement across judges),
and that curated data supervised-fine-tunes the sub-agent to emit, instead of
a best-effort answer, one of four structured [[abstention]] outputs with a
written rationale: Ambiguous Query (intent not determinable), Insufficient
Input (intent clear, execution needs more information), Missing Capability
(the sub-agent does not support the requested function), or Misrouting (a
different sub-agent should handle it).[^c1]

The fine-tuned sub-agent is redeployed, its new interactions re-enter the
labeling pipeline, and the cycle repeats.[^c2]

Deployed on a production e-commerce business-intelligence sub-agent, this
raised the sub-agent's overall response pass rate from 68.5% to 78.9% (a
15.2% relative gain) over a baseline sub-agent trained without abstention
data.[^c3]

## Why it matters

The mechanism answers a question this wiki treats as two of the answerer's
stalls at once. It is the sub-agent's move on "how much to commit, and how to
say the rest" (stall 10): instead of forcing an answer under capability
constraints it does not have, the sub-agent commits to a category-labeled
non-answer with a rationale. And it feeds stall 4, "who answers" — a
Misrouting label is itself a routing signal, handing the coordinator grounds
to send the request to a different sub-agent rather than treating the
sub-agent's silence or hallucination as the final word.

## Limits

The claim rests on one deployment: a single centralized coordinator/sub-agent
architecture, one domain (shop business-intelligence queries with a
SQL-like DSL), and one taxonomy of four failure categories chosen by the
authors, not derived from a general theory of what a sub-agent can fail at.
The training signal itself depends on a calibrated multi-judge ensemble whose
highest-precision setting (unanimous four-judge agreement) costs roughly
20x a single judge call, so the method's quality is bought with labeling
cost that is not free to reproduce elsewhere. The measured gain is also
uneven across the two query types evaluated: segmentation semantic
correctness rose sharply (61.9% to 82.7%) while analytics semantic
correctness was flat to slightly negative (75.1% to 75.0%), so "improves MAS
reliability" is not uniform across sub-agent capabilities even within this
one deployment. [xie-2026-ears] is a single arXiv report (2026), not yet
independently replicated.

## Related

[[abstention]] · [[informed-abstention-framework]] · [[dac-cross-agent-abstention-reward]] · [[clarification-request]]

[^c1]: xie-2026-ears — "we present EARS (Explanatory Abstention for Reliable Sub-Agent Modeling), a production-oriented framework that reframes sub-agent abstention as an inter-agent communication protocol: a sub-agent does not merely abstain, but exposes an actionable failure state to the coordinator."
[^c2]: xie-2026-ears — "The updated sub-agent is finally redeployed into the multi-agent system, forming an online data flywheel for iterative improvement."
[^c3]: xie-2026-ears — "EARS improves the overall response pass rate from 68.5% to 78.9%, demonstrating that sub-agent-side explanatory abstention improves MAS reliability."
