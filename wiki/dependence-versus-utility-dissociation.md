---
description: "A trained policy can encode history in every scenario yet need it for performance in under half; detecting use is not detecting necessity, so high returns do not show the reasoning was required."
aliases: ["history dependence versus history utility", "reactive shortcut in Dec-POMDP benchmarks"]
sources: ["arxiv-2602-20804"]
---
# Dependence versus utility dissociation

In a cooperative multi-agent benchmark framed as a Dec-POMDP, success is usually read as evidence that agents did the hard part: using history to infer hidden state and coordinating from local information. The audit of 37 scenarios (MPE, SMAX, Overcooked, Hanabi, MaBrax) separates two things that are normally conflated. The first is dependence: whether a trained policy's actions carry information about its past. The second is utility: whether removing memory costs performance.[^c1]

Measured result: an information-theoretic history-dependence score exceeded its permutation null in all 37 scenarios, yet memory-based policies beat reactive ones significantly in only 43.2% (16/37).[^c2] The authors read much of the dependence as redundant: policies track past information that offers no functional advantage over the current observation.[^c3] Hanabi, a canonical partially observable task, shows no significant memory gap under the baselines tested.[^c4]

The decision rule requires both a significant performance gap (one-tailed Wilcoxon signed-rank, p < 0.05) and a history-use score above its permutation baseline. The second criterion is there to confirm that the advantage reflects use of history rather than confounders such as optimisation dynamics.[^c5]

A second dissociation: hidden environment state and hidden teammate information are separate drivers of difficulty. The private-information-flow probe fired in 20% of Overcooked V1 layouts (fully observable) and 82% of V2 layouts, where hidden teammate information was added by design, so the probe recovered the designers' intent.[^c6] Coordination likewise splits into synchronous action coupling and directed temporal influence, which dissociate across suites; only MPE satisfied every criterion in every scenario.[^c7]

The consequence for question and answer design (my inference, not the paper's claim): a correct or high-scoring answer is weak evidence of the capacity a task is meant to test unless the task is built so that a cheaper strategy fails. The paper's own prescription is that decision-relevant information be available only through history so reactive policies are insufficient.[^c8]

## Limits

- Verdicts describe policies learned by IPPO and MAPPO under current training, not the environments' intrinsic requirements; the paper says these reflect dependencies induced by the policy rather than strict environment requirements.[^c9] A better learner might use memory where baselines did not.
- Aggregation is deliberately conservative (maximum over agents and configurations), so "absent" means absent everywhere tested.
- The analogy to human or LLM question answering is mine and untested here.
- Synchronous coupling is flagged as possibly brittle; it signals coordination but not robustness.

## Related

- [[model-dependent-benchmark-difficulty]] — difficulty also depends on who is being tested, not only on the task
- [[verification-over-invention]] — success on a task can mask which ability was exercised
- [[multi-agent-process-verification-unreliability]] — multi-agent setting where outcome signals mislead

[^c1]: arxiv-2602-20804 — "High returns can mask a failure to learn the underlying coordination challenge, as agents may exploit reactive shortcuts"
[^c2]: arxiv-2602-20804 — "history dependence rarely translates to history utility—while all learned policies encode some history dependence, only 43% actually need memory to achieve high returns"
[^c3]: arxiv-2602-20804 — "policies learn to track past information that offers no functional advantage over current observations"
[^c4]: arxiv-2602-20804 — "Despite being a canonical partially observable task, the memory–reactive gap is not significant"
[^c5]: arxiv-2602-20804 — "this advantage reflects active use of history rather than other confounding factors, such as optimisation dynamics"
[^c6]: arxiv-2602-20804 — "PIF recovers the design intentions of the environment authors"
[^c7]: arxiv-2602-20804 — "MPE stands out as the only suite where every scenario demands both coordination forms"
[^c8]: arxiv-2602-20804 — "environments should ensure decision-relevant information is exclusively available through history, rendering reactive policies insufficient"
[^c9]: arxiv-2602-20804 — "these reflect dependencies induced by the policy rather than strict environment requirements"
