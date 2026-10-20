---
description: "An LLM persuader can succeed when a target's mental states are handed to it yet fail when it must elicit them by asking; the gap, not static ToM scores, marks missing planning ToM."
aliases: ["PToM", "planning theory of mind", "revealed-hidden persuasion gap", "MindGames"]
sources: ["arxiv-2602-17045", "arxiv-2511-22275"]
---
# Planning theory of mind elicitation gap

Static, spectatorial theory-of-mind (ToM) benchmarks ask a model to predict what a character will do. The authors argue this can be solved by a heuristic, without a causal model of how mental states produce behavior. They distinguish associative ToM (predictive mappings from cues to behavior), causal ToM (mental states as causes of behavior) and Planning ToM (PToM): using causal ToM in interaction to plan interventions.[^c1]

## The task and the gap

In the MindGames persuasion task, the persuader must get a target to choose one of three policies by strategically revealing information. Success depends on the target's knowledge states and motivational states. Those states are either REVEALED to the persuader or HIDDEN, so that it must inquire about or infer them.[^c2] Because HIDDEN success requires eliciting and using mental-state information, the authors treat above-chance HIDDEN performance as the marker of PToM.[^c3]

With a rational bot as target, o3 succeeded 65% of the time in REVEALED, above the 10% baseline, but 6% in HIDDEN, no better than chance. Humans scored 29% in HIDDEN against o3's 6%, and 22% in REVEALED against o3's 65%.[^c4] The size of the REVEALED-minus-HIDDEN difference was larger for o3 than for humans.[^c5]

## Behavioral signature

In HIDDEN, humans made 6.1 appeals (questions) and 2.5 disclosures per scenario; o3 made 4.7 appeals and 5.3 disclosures. The authors read this as o3 disclosing in a scattershot way, humans more surgically after seeking information.[^c6] When all mental-state information is available, success can come from matching preferences to available facts, which needs no monitoring of whether one knows enough about the target. That is the pattern expected from associative rather than causal ToM.[^c7]

## Persuasion without PToM

In the later experiments, with human targets role-playing the bot or reporting real belief change, o3 outperformed human persuaders, significantly so in REVEALED. The authors infer that effective persuasion can occur without explicit ToM reasoning, for example through rhetorical strategies.[^c8]

For question design: the diagnostic is whether an asker notices what it lacks about the other party and asks for it. Fluent output and good outcomes with a cooperative target do not show this. (This reading is mine.)

## Behavioral prediction as a separate item

RecToM, a benchmark for LLM theory of mind in recommendation dialogue, makes a related complaint from the other side. It says that existing benchmarks "often overlook a critical component of human ToM: behavioral prediction, the ability to use inferred mental states to guide strategic decision-making".[^c11] Its items keep inference and prediction apart: desire, intention and belief questions on one side, and questions on which strategy comes next and whether a strategy is effective on the other. Its authors state that "it is equally important to leverage these inferred states to inform action."[^c12] The items are multiple choice or yes/no over a finished dialogue, so nothing is elicited by asking and the benchmark does not test the gap described above. The two papers agree that inference alone is not the whole of ToM; they do not test the same thing. (This comparison is mine.)

## Limits

- The authors say the behavioral signatures do not uniquely identify a mechanism. Limits in multi-step planning, working memory, epistemic tracking, pragmatic mismatch with a minimally cooperative bot, or classifier noise could explain the same pattern.[^c9]
- The rational bot never volunteers information, so it may disadvantage persuaders that rely on cooperative conversation; external validity is low.[^c10]
- One reasoning model (o3, with o1 replication) was studied; other models and prompts were not established here.
- That o3 persuades "without" PToM is inferred from its HIDDEN failure; it is not a direct measurement of its internal process.

## Related

- [[unindexed-information-seeking]] — information seeking when the needed facts are not given
- [[policy-based-vs-plan-based-epistemic-action]] — planning versus reactive information gathering
- [[rhetorical-intent-direction-divergence]] — rhetorical effects diverging from intent
- [[debate-elicits-sycophancy]] — persuasive interaction effects in LLMs
- [[intention-granularity-gap]] — the same benchmark family's intention items; fine intent labels are far harder than coarse ones

[^c1]: arxiv-2602-17045 — "we call this capacity Planning Theory of Mind (PToM)"
[^c2]: arxiv-2602-17045 — "Success depends on a persuader’s sensitivity to a given target’s knowledge"
[^c3]: arxiv-2602-17045 — "for PToM. For this reason, we treat above-chance performance on the H IDDEN condition as"
[^c4]: arxiv-2602-17045 — "With a human success rate of 29% and a o3 success rate of 6%, humans"
[^c5]: arxiv-2602-17045 — "Finally, the difference in performance between R EVEALED and H IDDEN was significantly larger for o3 than for humans"
[^c6]: arxiv-2602-17045 — "This gives the impression that o3 discloses information"
[^c7]: arxiv-2602-17045 — "Success in R EVEALED can be association-based"
[^c8]: arxiv-2602-17045 — "effective persuasion can occur without explicit ToM reasoning"
[^c9]: arxiv-2602-17045 — "these behavioral signatures do not uniquely identify an underlying mechanism"
[^c10]: arxiv-2602-17045 — "Experiment 1 is limited by its low external validity"
[^c11]: arxiv-2511-22275 — "behavioral prediction, the ability to use inferred mental states to guide strategic decision-making"
[^c12]: arxiv-2511-22275 — "it is equally important to leverage these inferred states to inform action"
