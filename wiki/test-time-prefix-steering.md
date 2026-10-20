---
description: "Prepending a few learned continuous vectors to a frozen LLM's input, tuned on unlabelled test data to minimise output entropy, is reported to lift math accuracy without changing any weight."
aliases: ["TTSV", "test-time steering vectors", "Model Whispering", "input-prefix test-time adaptation"]
sources: ["arxiv-2512-04748"]
---
# Test-time prefix steering

A short run of continuous vectors, placed in front of a model's input embeddings, can be optimised on unlabelled test inputs while every weight of the model stays frozen. The vectors are the only trainable object. Their loss is the entropy of the model's own output distributions: the paper averages token-level entropy "across all non-padding generated tokens within" a mini-batch, and gradients reach only the prefix.[^t1] No answer key enters the objective. The paper calls the prefix a Test-Time Steering Vector (TTSV). The augmented input is the prefix followed by the embedded input, and the frozen model generates from that.[^t2] After optimisation the prefix is fixed, and "these optimized steering vectors are used for all samples in the test set."[^t3]

The premise is that confidence and competence go together on a task: "model proficient in a specific task should exhibit high certainty in its predictions," so lower output entropy is read as a sign that the model has found the part of its existing knowledge that fits the task.[^t4] The method does not teach a new skill. It searches for an input signal that moves the model into a more deterministic state it already has access to. The paper's contrast is with training methods, which are used "to embed new and task-specific knowledge into the trainable components."[^t5]

Where the intervention enters is part of the claim. The prefix takes part in attention in every layer. In a first-layer analysis that ignores position encoding, the output at each content position is a mix of its original output and one bias direction, fixed by the prefix, with the mixing weight set by the attention paid to the prefix.[^t6] The paper then argues that the shift grows through depth: "the magnitude of the activation shift induced by TTSV increases with network depth."[^t7] The depth claim is supported by a t-SNE plot of final-layer activations, not by a derivation.

Reported effects, all from the paper's own tables and text. On Qwen2.5-Math-7B the mean-token-entropy prefix lifts MATH500 "from 51.00% to 74.40%."[^t8] Averaged over four math sets, the gain is "an average absolute improvement of +17.22%, which corresponds to a" relative gain of 55.95%, and the paper states this "surpasses the +14.08% average gain from EM", the full-parameter entropy-minimisation baseline.[^t9] On the thinking-mode Qwen3-4B it reports "a 16.22% relative gain on the Qwen3-4B reasoning model" on MATH500.[^t10] On LLaMA-3.1-8B "the gains from both methods were modest."[^t11] Against the parameter-efficient SLOT method the prefix is ahead on the Qwen2.5-Math sizes in the paper's table, and in a per-sample variant "even in this setting, TTSV still outperforms SLOT."[^t12]

Two properties are set against the full-parameter baseline. Training does not degrade late: the accuracy curve for the prefix "does not exhibit the performance degradation at later training stages observed in EM."[^t13] The prefix length has a non-monotonic effect: "the relationship between TTSV length and performance is non-monotonic," with "L = 20 yielding the best results" among {1, 5, 10, 20, 40} on one model.[^t24][^t25] A single vector "provides a substantial improvement over the baseline."[^t14] A prefix trained on one distribution also helps on others: a vector trained on MATH500 "always yields substantial performance gains over" the baseline on the other sets, and one such transfer "surpasses the 22.8% from the ID-TTSV" trained on the target itself.[^t15]

## Limits

- The evidence is mostly mathematical. The one non-mathematical benchmark is included "to assess the generalization of our method beyond the mathematical domain," and it is a single graduate-level science set.[^t16]
- Four models are tested, all at or under about 8B parameters in the base family, plus one reasoning model. The paper's breadth claim rests on that set.[^t17]
- The baselines are EM and SLOT, described as "two representative test-time adaptation methods."[^t18] Test-time reinforcement learning is cited in the introduction but not benchmarked in the sections read.
- The objective is a proxy. The paper's own warning is that entropy minimisation "can push the model into a state of over-confidence, leading to" overly deterministic reasoning.[^t19] The paper argues that freezing the weights guards against this, but the reported measure is accuracy; no calibration or confidence-versus-correctness measure appears in the sections read. Whether a lower-entropy answer is more often correct is an assumption carried by the premise above, not a result the paper tests.
- The paper lists "the exploration of alternative or combined objective functions" as an open question.[^t20]
- The length ablation is one model on one benchmark: "The effect of TTSV length on the accuracy of" Qwen2.5-Math-1.5B on MATH500.[^t21] The best length is not established beyond that setting.
- The theory covers only the first attention layer and "ignoring position encoding."[^t22] The growth with depth is shown on one t-SNE figure over "20 problems sampled from Minerva Math," which is an illustration rather than a test.[^t23]
- The tables give single values. The sections read report no spread across seeds, so the size of the smaller gains (for example on LLaMA-3.1-8B) is not bounded by the paper. (My inference from the sections read.)
- The per-sample variant trades away the one-prefix-for-all-items advantage. The paper notes that SLOT's per-sample approach costs "inference latency due to per-sample optimization." A per-sample prefix pays the same optimisation cost per item, and the paper does not price that. (My inference.)

## Related

- [[entropy]] — the quantity minimised; the objective is the mean of this over generated tokens, not over a label set.
- [[mean-difference-steering-vector]] — an activation-space offset built from labelled prompt pairs and added at one layer; the prefix here is an input-side vector tuned without labels, so the two act at different points.
- [[query-only-test-time-training]] — another test-time adaptation that leaves most of the model fixed and updates a small part of it; it changes query projections, not the input.
- [[consensus-reward-tilting]] — the test-time reinforcement-learning family (TTRL) that the paper cites as a parameter-changing baseline; its pseudo-label is a majority answer, where the prefix uses entropy.
- [[compress-and-merge-soft-prompt]] — learned soft prompts for a frozen LLM, trained to compress documents, not to lower output entropy at test time.
- [[confidently-wrong-low-entropy-regime]] — the blind spot of low-entropy scores; a prefix tuned to lower entropy inherits it, and the paper does not test for it.

[^t1]: arxiv-2512-04748 — "across all non-padding generated tokens within"
[^t2]: arxiv-2512-04748 — "creating an augmented input"
[^t3]: arxiv-2512-04748 — "these optimized steering vectors are used for all samples in the test set"
[^t4]: arxiv-2512-04748 — "model proficient in a specific task should exhibit high certainty in its predictions"
[^t5]: arxiv-2512-04748 — "to embed new and task-specific knowledge into the trainable"
[^t6]: arxiv-2512-04748 — "ignoring position encoding"
[^t7]: arxiv-2512-04748 — "increases with network depth"
[^t8]: arxiv-2512-04748 — "lifting its score from 51.00% to 74.40%"
[^t9]: arxiv-2512-04748 — "This result surpasses the +14.08% average gain from EM."
[^t10]: arxiv-2512-04748 — "a 16.22% relative gain on the Qwen3-4B reasoning model"
[^t11]: arxiv-2512-04748 — "the gains from both methods were modest"
[^t12]: arxiv-2512-04748 — "even in this setting, TTSV still outperforms SLOT"
[^t13]: arxiv-2512-04748 — "does not exhibit the performance degradation at later training stages observed in EM"
[^t14]: arxiv-2512-04748 — "provides a substantial improvement over the baseline"
[^t15]: arxiv-2512-04748 — "which surpasses the 22.8% from the ID-TTSV"
[^t16]: arxiv-2512-04748 — "To assess the generalization of our method beyond the mathematical domain"
[^t17]: arxiv-2512-04748 — "models from both the Qwen and LLaMA series"
[^t18]: arxiv-2512-04748 — "We benchmark our method against two representative test-time adaptation methods"
[^t19]: arxiv-2512-04748 — "push the model into a state of over-confidence, leading to"
[^t20]: arxiv-2512-04748 — "the exploration of alternative or combined objective functions"
[^t21]: arxiv-2512-04748 — "The effect of TTSV length on the accuracy of"
[^t22]: arxiv-2512-04748 — "ignoring position encoding"
[^t23]: arxiv-2512-04748 — "on 20 problems sampled from Minerva Math"
[^t24]: arxiv-2512-04748 — "the relationship between TTSV length and performance is non-monotonic"
[^t25]: arxiv-2512-04748 — "L = 20 yielding the best results"
