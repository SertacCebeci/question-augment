---
description: "A logic-only process reward model picks confidently flawed trajectories as best-of-N grows and falls below majority voting; adding an evidence-grounding check keeps it stable."
aliases: ["logic-only PRM reranking", "best-of-N drift under a process reward", "reranking blind spot of general PRMs", "grounding-blind trajectory selection"]
sources: ["doi-10-48550-arxiv-2609-01658"]
---
# Logic-only reranking drift

When a model samples many reasoning trajectories and a process reward model (PRM) picks one, the picker's blind spots decide whether a larger candidate pool helps. In retrieval-augmented QA the measured pattern is that a PRM judging only logical coherence stops helping as the pool grows, while a PRM that also checks the retrieved evidence keeps helping.

The comparison draws 128 trajectories per question, for 500 questions from PopQA, HotpotQA and 2WikiMultiHopQA, from Qwen2.5-7B-Instruct.[^b1] Majority voting (MV) is the baseline that "ignores PRM scores". Weighted majority voting (WMV) weights each candidate by its minimum step score. Best-of-N (BoN) takes the single top-scored trajectory. Under BoN, two general-purpose PRMs, VersaPRM and a math-trained PRM, "degrade as K increases", and they "frequently" fall "below the MV baseline" on all three sets.[^b2][^b3]

The authors' explanation is about what these scorers do not check: "Because they evaluate logical coherence without verifying factual grounding," they give high scores to plausible but unsupported paths. As the pool grows, "BoN increasingly selects these confidently flawed trajectories."[^b4][^b5] The mechanism in one line: selection takes the argmax over more candidates, so a scorer with a systematic blind spot hands the choice to the blind spot more often as N rises.[^b5] That last step is my reading, not a result the paper isolates.

The grounded PRM is the contrast. Under WMV its F1 "consistently improves" as the pool grows.[^b6] At K = 128 with WMV it is ahead of majority voting on all three sets, "outperforming both MV (43.9 / 54.6 / 49.2)" on 2WikiMultiHopQA, HotpotQA and PopQA.[^b7] Under BoN it "remains stable as K grows, performing comparably" to MV on two sets, and is "substantially outperforming it on HotpotQA".[^b8][^b9]

## Limits

- One generator (Qwen2.5-7B-Instruct), three QA sets, 500 questions each. MuSiQue and the other benchmarks are not in this experiment, so the drift is not shown there.
- Only two general PRMs are compared. The math-trained one was trained on mathematics, so its failure in retrieval QA may come from domain shift as much as from a missing grounding check. The experiment does not separate the two.
- The explanation (confidently flawed hallucinations) is the authors' reading. The text I read does not count hallucinated selections directly.
- The grounded PRM's advantage under BoN is not uniform. It is comparable to MV on two sets and clearly ahead only on HotpotQA.
- Whether a logic-only scorer drifts in a domain without retrieval is not tested here. The claim is about scorers judging steps that interleave reasoning with retrieved text.

## Related

- [[evidence-grounded-step-reward]] — the same grounding check, used to build training pairs as well as to rerank.
- [[process-reward-model-hackability]] — another way a step scorer's high scores come apart from correctness, here through style edits rather than missing evidence.

[^b1]: doi-10-48550-arxiv-2609-01658 — "We sample 128 reasoning trajectories"
[^b2]: doi-10-48550-arxiv-2609-01658 — "majority voting (MV), which ignores PRM scores"
[^b3]: doi-10-48550-arxiv-2609-01658 — "both VersaPRM and MathPRM degrade as K increases, frequently falling below the MV baseline"
[^b4]: doi-10-48550-arxiv-2609-01658 — "Because they evaluate logical coherence without verifying factual grounding"
[^b5]: doi-10-48550-arxiv-2609-01658 — "BoN increasingly selects these confidently flawed trajectories"
[^b6]: doi-10-48550-arxiv-2609-01658 — "our PRM consistently improves F1"
[^b7]: doi-10-48550-arxiv-2609-01658 — "outperforming both MV (43.9 / 54.6 / 49.2)"
[^b8]: doi-10-48550-arxiv-2609-01658 — "our PRM remains stable as K grows, performing comparably"
[^b9]: doi-10-48550-arxiv-2609-01658 — "substantially outperforming it on HotpotQA"
