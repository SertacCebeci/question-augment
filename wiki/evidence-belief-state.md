---
description: "A retrieval controller can keep one persistent evidence state over six belief dimensions, updated each step, and choose its next action from the whole state rather than from one signal."
aliases: ["persistent evidence state", "evidence-state fragmentation"]
sources: ["doi-10-48550-arxiv-2609-39139"]
---
# Persistent evidence belief state

Multi-step retrieval needs more than a relevance score. After each search a controller must judge whether the evidence it already holds is enough to answer, whether that evidence can be trusted, and whether another search would add anything. Adaptive RAG methods supply these judgments as separate signals (confidence, relevance, support, retrieval quality), each often used as its own trigger. The paper's diagnosis is that this "makes it difficult to preserve a coherent evidence state across a trajectory", and it names the result evidence-state fragmentation.[^c1]

The remedy is to keep one state that persists across steps. "Before making a decision, BeliefRAG computes" a set of diagnostics on the retained evidence: relevance, support, conflict, uncertainty, gap, novelty and cost.[^c2] These are converted into six belief dimensions: sufficiency, reliability, conflict, uncertainty, gap and cost.[^c3] Five of them are inferred, since "for each inferred dimension, the complete diagnostic vector is mapped to an instantaneous belief."[^c4] Cost is not inferred. It is the fraction of the token budget already spent.

The state is not overwritten by each observation. The new estimate is blended with the previous belief in logit space, because "one verifier call can be noisy" and a single reading should not replace the belief.[^c5] The paper motivates the construction by partially observable decision problems, where the usual move is "maintaining a belief over information that cannot be observed directly".[^c6] My reading is that the update in its equation 5 is a smoothed average of logits, not a Bayesian filter over a latent variable. What carries over from that field is the premise that the evidence condition is hidden and must be estimated. The formal update does not carry over.

The state drives an ordered set of rules rather than a single score. Correction comes first: high conflict or low reliability triggers verification, pruning, query rewriting and replacement retrieval. "Correction is not simply deletion", because removing weak passages without new retrieval can leave the question less answerable. Next comes answering, if the answer gate passes (see calibrated-answerability-gate). Then another retrieval is issued only if its estimated chance of making the evidence answerable clears a minimum. Rewriting follows when novelty is low. Stopping and abstention come last. The abstention rule is conjunctive: "not an abstention rule: uncertainty must be combined with evidence insufficiency and low acquisition value."[^c7] So [[abstention]] here means that the evidence is insufficient and no useful acquisition remains, not that confidence is low.

What was measured. On six QA benchmarks with gpt-oss-120b the controller reaches mean token F1 0.572 at 3.89k tokens per question, against 0.555 for fixed iterative retrieval, and it does so with 39% fewer tokens.[^c8] The paper reports the same pattern on Qwen3-32B.[^c9] Its ablations attribute the gain mainly to corrective re-retrieval rather than to pruning: "main gains come from corrective re-retrieval".[^c10]

The dimensions overlap. "The joint state reaches AUC 0.816, compared with" 0.761 for the strongest single dimension, uncertainty, and the paper finds that "several belief dimensions are redundant".[^c11][^c12] Sufficiency and reliability are reported as "well calibrated, with ECE values of 0.039 and 0.045".[^c13] The paper says its dimension analysis gives "interpretation and association" rather than causal evidence for each dimension.[^c14] The one intervention it runs acts on the separate answerability score, not on the sufficiency dimension.

## Limits

- One author, one preprint, and a shared harness built by the author. The paper's own limitations include "lexical retrieval, only n = 100 questions" in some analyses.[^c15]
- The controller is not trained with reinforcement learning. "The controller is non-RL; only the sufficiency and" retrieval-value estimates are fitted from data.[^c16] The thresholds are defaults, and the paper says that "experiment-specific selected values" are reported separately, so the operating points were chosen per experiment.
- The baselines Self-RAG and RL-Search are "common-harness mechanism variants rather than full reproductions", so the comparison is between mechanisms in one harness, not between published systems.[^c17]
- Source shift is a stated boundary: the same decision signal can be invalidated when the evidence source changes, even after calibration.[^c18]
- The belief dimensions are not shown to be individually decision-relevant by intervention. The claims about their use rest on association and on the ablations listed above.

## Related

- calibrated-answerability-gate — the answer rule inside this state, and why its threshold needs a calibrated score.
- [[evidence-gap-state]] — a tracked evidence and gap state in a memory-based loop. Here gap is one of six dimensions, not the whole state.
- [[stop-continue-criteria-in-retrieval-loops]] — the stop families; a state-based stop like this one is rare in that corpus.
- [[uncertainty-guided-retrieval-triggering]] — uncertainty as a trigger for retrieval. Here uncertainty counts toward abstention only together with insufficiency.
- [[belief-augmented-generation]] — a "belief state" built from sampled answers, not from retrieved evidence. Same word, different object.

[^c1]: doi-10-48550-arxiv-2609-39139 — "Existing methods often use such signals as separate triggers, making it difficult to preserve a coherent evidence state across a trajectory"
[^c2]: doi-10-48550-arxiv-2609-39139 — "Before making a decision, BeliefRAG computes"
[^c3]: doi-10-48550-arxiv-2609-39139 — "observations update six operational belief dimensions: sufficiency, reliability, conflict, uncertainty,"
[^c4]: doi-10-48550-arxiv-2609-39139 — "For each inferred dimension, the complete diagnostic vector is mapped to an instantaneous belief."
[^c5]: doi-10-48550-arxiv-2609-39139 — "Because one verifier call can be noisy"
[^c6]: doi-10-48550-arxiv-2609-39139 — "maintaining a belief over information that cannot be observed directly"
[^c7]: doi-10-48550-arxiv-2609-39139 — "not an abstention rule: uncertainty must be combined with evidence insufficiency and low acquisition value"
[^c8]: doi-10-48550-arxiv-2609-39139 — "token F1 0.572 with 3.89k tokens per question, outperforming fixed Iterative RAG at 0.555 F1 while"
[^c9]: doi-10-48550-arxiv-2609-39139 — "The same quality–cost pattern transfers to Qwen3-32B"
[^c10]: doi-10-48550-arxiv-2609-39139 — "main gains come from corrective re-retrieval"
[^c11]: doi-10-48550-arxiv-2609-39139 — "The joint state reaches AUC 0.816, compared with"
[^c12]: doi-10-48550-arxiv-2609-39139 — "several belief dimensions are redundant"
[^c13]: doi-10-48550-arxiv-2609-39139 — "sufficiency and reliability are well calibrated, with ECE values of 0.039 and 0.045"
[^c14]: doi-10-48550-arxiv-2609-39139 — "These results establish interpretation and association for the belief dimensions"
[^c15]: doi-10-48550-arxiv-2609-39139 — "include lexical retrieval, only n = 100 questions"
[^c16]: doi-10-48550-arxiv-2609-39139 — "The controller is non-RL; only the sufficiency and"
[^c17]: doi-10-48550-arxiv-2609-39139 — "are common-harness mechanism variants rather than full reproductions"
[^c18]: doi-10-48550-arxiv-2609-39139 — "source shift can still invalidate the same decision signal"
