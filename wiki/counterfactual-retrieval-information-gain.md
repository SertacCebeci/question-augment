---
description: "A search step is scored by how far its retrieved documents raise the policy's gold-answer log-probability above a random-document baseline, giving query-level credit with no extra labels."
aliases: ["IG reward for search steps", "retrieval-grounded process reward", "counterfactual retrieval gain", "step-level information gain for search"]
sources: ["doi-10-48550-arxiv-2604-15148", "arxiv-2511-19314"]
---
# Counterfactual retrieval information gain

> A search query is judged by what its documents do to the model's confidence in the answer, compared with what random documents would do.

## Mechanism

Liang et al. (2026) score each search step t of a rollout by comparing two versions of the same context. The real context is the whole trajectory up to and including step t, with that step's actual retrieved documents and refinement. The counterfactual contexts keep everything before step t and replace only the (documents, refinement) pair at step t, with pairs "drawn from randomly selected search steps of other questions in the same training batch".[^c1] The score is the log-probability of the gold answer under the real context minus the average of the same log-probability over the N counterfactual contexts (the paper uses N = 3).

The log-probability is length-normalized over the answer tokens, so values are in nats per answer token and comparable across answers of different length.[^c2] Only the short gold-answer tokens are scored, not new sequences, and the N+1 variants share one batched forward pass. The authors report that this adds "an approximately 6.4% increase" to per-step wall-clock time relative to the trajectory-level baseline.[^c3]

The baseline is random documents, not an empty context. The authors reject the empty context because "real and empty contexts differ not only in informativeness but also in length and positional structure", which introduces "a systematic bias unrelated to retrieval quality".[^c4] Random documents from the batch keep the length and structure of a real retrieval while removing its topical relevance, so the difference is meant to isolate what the retrieval contributed.[^c5] They state that "Figure 3 confirms that the empty baseline performs worst" among the baselines they compared.[^c6]

## What it credits

The premise is that, with a fixed retriever, "the quality of a search query is directly reflected in the documents it retrieves".[^c7] A step's score is therefore read as a property of the query that produced those documents. Because the score does not depend on whether the final answer is correct, it stays informative when every rollout fails. The authors contrast this with trajectory-level rewards: when all trajectories fail, "the trajectory-level advantages become approximately zero, yielding nearly no gradient signal".[^c8]

The closest prior signal the authors name is IGPO, which uses "the temporal difference in gold-answer log-probability between consecutive turns". They argue that this "conflates reasoning, querying, and retrieval within each turn rather than isolating query quality".[^c9] The counterfactual baseline is what separates the retrieval's share: the comparison is against the same step with its retrieval swapped, not against the previous turn (this contrast is my reading of the two definitions). Unlike step-level methods that need annotated sub-questions, the signal needs no labels beyond the QA pair; the authors describe it as "signal via counterfactual comparison, using only standard QA pairs".[^c10]

On seven QA benchmarks with Qwen2.5-3B, the authors report that "Both IG-Search variants (Base and Instruct) achieve an average EM of 0.430".[^c11] The reported gain over the strongest trajectory-level baseline is 1.6 points on average.

## Transfer from information theory

The name borrows from information theory, but the authors say the quantity is not that one: Eq. 2 "is not a Shannon information gain but shares the same sign convention".[^c12] What survives the transfer is the sign convention, positive when the real documents raise confidence in the gold answer relative to uninformative retrieval, and the framing that a retrieval is worth what it moves belief in a known target. What does not survive is any entropy reduction, so the score cannot be read as bounding the information a query gathers. The authors also note that such log-probability differences "inherently exhibit high variance and heavy-tailed distributions".[^c13] That is why the score is passed through the stabilization step described in [[signed-process-reward-stabilization]].

The same family appears in clarification: [[information-gain-reward]] scores a question by the shift in teacher-forced log-likelihood of a known goal, against a prior belief rather than against random retrieval. The two share the target-likelihood device and differ in the baseline. A broader relation to [[expected-information-gain]] and [[mutual-information]] is my inference, since the paper does not claim it.

## A second estimator, from rollouts

PRInTS (arxiv-2511-19314) targets the same quantity, a step's information gain, but measures it another way. Its gain is "the change in mean answer accuracy before and after the step", estimated with Monte Carlo rollouts.[^c17] The estimate is an accuracy difference over sampled continuations, not a log-probability difference against retrieved documents. On my reading, it therefore needs no random-document baseline; the paper does not discuss that contrast. The rollouts are annotation: they produce labels "to estimate information gain scores and construct preference trajectory step pairs", and a trained scorer predicts the gain at test time.[^c18] At test time the scorer ranks n candidate next steps, "selecting the step expected to yield the greatest information gain".[^c19]

## Limits

- The score needs the gold answer at training time. The authors say it "derives signal from the policy's own generation probabilities conditioned on the gold answer".[^c14] It is a training signal, not a grader that can be applied at deployment.
- For questions the policy already answers from parametric memory, the score tracks memory rather than the query. The authors say "IG does not faithfully reflect query quality" in that case, and add a dead zone for it.[^c15]
- The counterfactuals are drawn from the same batch, so the baseline depends on batch composition. The paper does not, in the parts read, measure how much the score moves with batch composition; this concern is my inference.
- The evidence is one retriever (E5-base-v2), one Wikipedia dump, training on NQ and HotpotQA, and two model sizes. On Bamboogle, GiGPO leads "(0.641 vs. 0.424, on 125 questions)", so small benchmark splits carry wide uncertainty.[^c16]
- The counterfactual-baseline ablation (RQ3), the component ablations, the hyperparameter sensitivity and the three-seed significance rerun in Appendix C were not read in this pass. The statement that the random baseline beats an empty one rests on the authors' Figure 3 remark, which was not checked.
- Selecting by predicted gain over-favours exploration when many candidates are drawn. In PRInTS, best-of-n gains rise with n and then fall at n = 16: "performance declines at n = 16".[^c20] The authors attribute this to a larger pool making it "increasingly prone to" steps that look informative, so "the agent abandons shorter, successful trajectories".[^c21] The scaling figure is labelled as one model (Tongyi DeepResearch-30B-A3B) while the text names Qwen3-32B for the same experiment; the paper does not resolve this.

## Related

- [[query-token-advantage-modulation]] — how this per-step score enters the GRPO advantage, on query tokens only
- [[signed-process-reward-stabilization]] — the dead zone, negative scaling and clipping applied before the score is used
- [[information-gain-reward]] — the clarification analogue: a log-likelihood shift against a prior, not against random retrieval
- [[intermediate-query-quality-credit]] — grades each query by novelty and a judge's usefulness, not by the answer likelihood it enables
- [[sequence-likelihood-confidence]] — the answer log-probability that the score differences are taken over
- [[competence-aware-credit-assignment]] — other credit assignment across steps of an agent
- [[rolling-trajectory-summary]] — the bounded running summary a step scorer reads in PRInTS, the rollout-estimated gain's evaluator

[^c1]: doi-10-48550-arxiv-2604-15148 — "pairs drawn from randomly selected search steps of other questions in the same training batch"
[^c2]: doi-10-48550-arxiv-2604-15148 — "The log-probability of the gold answer is computed as the length-normalized sum of per-token log-probabilities"
[^c3]: doi-10-48550-arxiv-2604-15148 — "introducing only an approximately 6.4% increase in"
[^c4]: doi-10-48550-arxiv-2604-15148 — "introducing a systematic bias unrelated to retrieval quality"
[^c5]: doi-10-48550-arxiv-2604-15148 — "while removing its topical relevance, so that IGt isolates the informational contribution"
[^c6]: doi-10-48550-arxiv-2604-15148 — "Figure 3 confirms that the empty baseline performs worst"
[^c7]: doi-10-48550-arxiv-2604-15148 — "the quality of a search query is directly reflected in the documents it retrieves"
[^c8]: doi-10-48550-arxiv-2604-15148 — "the trajectory-level advantages become approximately zero, yielding nearly no gradient signal"
[^c9]: doi-10-48550-arxiv-2604-15148 — "conflates reasoning, querying, and retrieval within each turn rather than isolating query quality"
[^c10]: doi-10-48550-arxiv-2604-15148 — "signal via counterfactual comparison, using only standard QA pairs"
[^c11]: doi-10-48550-arxiv-2604-15148 — "Both IG-Search variants (Base and Instruct) achieve an average EM of 0.430"
[^c12]: doi-10-48550-arxiv-2604-15148 — "It is not a Shannon information gain but shares the same sign convention"
[^c13]: doi-10-48550-arxiv-2604-15148 — "inherently exhibit high variance and heavy-tailed distributions"
[^c14]: doi-10-48550-arxiv-2604-15148 — "on the gold answer, requiring neither a separately trained reward model nor intermediate"
[^c15]: doi-10-48550-arxiv-2604-15148 — "For questions the model can answer from parametric knowledge, IG does"
[^c16]: doi-10-48550-arxiv-2604-15148 — "GiGPO leads only on Bamboogle (0.641 vs. 0.424, on 125 questions)"
[^c17]: arxiv-2511-19314 — "as the change in mean answer accuracy before and after the step"
[^c18]: arxiv-2511-19314 — "to estimate information gain scores and construct preference trajectory step pairs"
[^c19]: arxiv-2511-19314 — "selecting the step expected to yield the greatest information gain"
[^c20]: arxiv-2511-19314 — "performance declines at n = 16"
[^c21]: arxiv-2511-19314 — "the agent abandons shorter, successful trajectories and continues exploring until it reaches the maximum step budget"
