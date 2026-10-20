---
description: "Manipulative information uptake scores a decision against the option authorized evidence alone supports, so injected content that displaces that evidence counts as failure, true or not."
aliases: ["MIU", "decision integrity under injected content", "manipulated-evidence uptake"]
sources: ["doi-10-48550-arxiv-2609-34714"]
---
# Manipulative information uptake

The intake half of agent loyalty. An agent acting for a principal receives input from an opponent, and that input "may mix legitimate and manipulative" content.[^c2] Huang et al. require the agent to "resist Manipulative Information Uptake" (MIU), which they state as decision integrity: the agent's decisions must stay grounded in the principal's authorized information, not in content outside that scope.[^c1][^c3]

The measurement starts from a reference decision. For a task with user constraints, preferences, authorized sources S and a set of decision options, the gold decision d* is the option the value function picks from the clean context and authorized material only, "the gold-standard decision under authorized information alone."[^c4] An agent is then scored on whether its chosen option still matches d* when a manipulated context has been added. Under this requirement "the decision must match what authorized evidence" supports, whatever else the context contains.[^c5]

The reward has two parts. A correctness term D is 1 when the chosen option equals d*. A grounding term F "measures per-claim citation support from" clean, authorized evidence for the rationale the agent prints.[^c6] The MIU reward is R = −1 + (2 − η)·D + η·F, with η = 0.5 in the main setting. The paper's hierarchy is that it "enforces the hierarchy R=1 (correct and faithful) > R=0.5 (correct but unfaithful)," with incorrect decisions at R ≤ −0.5.[^c7] The grounding term is there because a correct answer can be reached through unauthorized reasoning: it "flags cases where a correct decision is reached through ungrounded or unauthorized reasoning."[^c8] Accuracy alone is therefore not taken as evidence of loyalty.

Training splits the same way. "The decision signal is a deterministic correctness measure," a string match against the precomputed baseline, "avoiding judge-induced evaluation variance."[^c9][^c10] Only faithfulness uses a judge, which asks "whether the agent's stated reasons rely on authorized clean evidence rather than manipulative evidence."[^c11] The paper reports that "Faithfulness is more tractable than decision accuracy under adversarial training."[^c12]

## Limits

- MIU measures a relation to authorized evidence, not the truth of what the opponent says. The paper is explicit: "MIU measures whether a decision rests on authorized evidence rather than whether" external claims are true.[^c13] A decision that follows a true but unauthorized claim is scored as a failure. Whether that is the right norm for a principal who would want the truth used is a question the text does not settle.
- The grounding term checks claims one at a time. "F evaluates each printed claim in isolation against its cited evidence," so a set of individually supported claims that together mislead is not caught by F. The paper says "D provides that verdict," leaving the overall warrant to the decision term.[^c14][^c15]
- The manipulations are fixed in advance. "MIU uses static manipulated contexts," so training never includes an opponent that adapts its injected content to the agent's replies.[^c16] The text I read does not test adaptive manipulation. That gap is my inference from the design, not a reported result.
- The faithfulness judge is a model. A separate model "provides EIL utility/leakage and MIU faithfulness," so the grounding scores inherit that judge's errors.[^c17]
- The out-of-distribution claim rests on "under a single-seed design."[^c18] The main trained configuration is averaged over three seeds, but "the Claude Haiku 4.5 configuration uses a single seed."[^c19] The MIU gains should be read as one training recipe on one benchmark, not as a general property of decision integrity.

## Related

- [[exploitable-information-leakage]] — the disclosure half of agent loyalty. EIL governs what leaves the agent; MIU governs what enters its decision.
- [[compensatory-leakage]] — a different unauthorized reversal. There a lower-priority score overturns an earlier criterion inside one decision rule; here the overturning input comes from outside the agent, and the test is authorization rather than priority order. The two share only the shape of a decision that a non-authorized input can flip.

[^c1]: doi-10-48550-arxiv-2609-34714 — "resist Manipulative Information Uptake"
[^c2]: doi-10-48550-arxiv-2609-34714 — "which may mix legitimate and manipulative"
[^c3]: doi-10-48550-arxiv-2609-34714 — "Decision integrity: A"
[^c4]: doi-10-48550-arxiv-2609-34714 — "the gold-standard decision under authorized information alone"
[^c5]: doi-10-48550-arxiv-2609-34714 — "the decision must match what authorized evidence"
[^c6]: doi-10-48550-arxiv-2609-34714 — "measures per-claim citation support from"
[^c7]: doi-10-48550-arxiv-2609-34714 — "enforces the hierarchy R=1 (correct and faithful) > R=0.5 (correct but unfaithful)"
[^c8]: doi-10-48550-arxiv-2609-34714 — "flags cases where a correct decision is reached through ungrounded or unauthorized reasoning"
[^c9]: doi-10-48550-arxiv-2609-34714 — "The decision signal is a deterministic correctness measure"
[^c10]: doi-10-48550-arxiv-2609-34714 — "avoiding judge-induced evaluation variance"
[^c11]: doi-10-48550-arxiv-2609-34714 — "rely on authorized clean evidence rather than manipulative evidence"
[^c12]: doi-10-48550-arxiv-2609-34714 — "Faithfulness is more tractable than decision accuracy under adversarial training"
[^c13]: doi-10-48550-arxiv-2609-34714 — "MIU measures whether a decision rests on authorized evidence rather than whether"
[^c14]: doi-10-48550-arxiv-2609-34714 — "F evaluates each printed claim in isolation against its cited evidence"
[^c15]: doi-10-48550-arxiv-2609-34714 — "D provides that verdict"
[^c16]: doi-10-48550-arxiv-2609-34714 — "MIU uses static manipulated contexts"
[^c17]: doi-10-48550-arxiv-2609-34714 — "provides EIL utility/leakage and MIU faithfulness"
[^c18]: doi-10-48550-arxiv-2609-34714 — "under a single-seed design"
[^c19]: doi-10-48550-arxiv-2609-34714 — "the Claude Haiku 4.5 configuration uses a single seed"
