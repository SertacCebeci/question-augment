---
description: "Chaining a diversity-based acquisition function before an uncertainty-based one shrinks the pool the costly scorer sees, cutting query cost and labels; domain-dependent."
aliases: ["series structure", "sieve acquisition", "aggregated acquisition functions"]
sources: ["arxiv-2602-07440"]
---
# Series-aggregated acquisition

Active learning splits acquisition functions into representativity-based ones, which "effectively explore the dataset but do not prioritize boundary decisions", and uncertainty-based ones, which "focus on refining boundary decisions already identified by the neural network".[^c1] Jung et al. (2026) combine them rather than inventing a new score. In the series structure two functions are applied one after the other, each shrinking the pool for the next: a sieve with layers.[^c2]

## Mechanism

A subsample factor kappa >= 1 gives the first function an enlarged budget kappa*b; the second function then picks the final b from that subpool: D1 = a1(pool, kappa*b), D* = a2(D1, b).[^c3] Because the pool is much larger than kappa*b, the second function costs little on top of the first.[^c3]

The cost argument is concrete. BALD needs N_MC-dropout forward passes per pool item, K-Centers only one. Running BALD after K-Centers needs |pool| + N_MC*b passes, far fewer than N_MC*|pool|.[^c4] So the chain can be cheaper than the expensive scorer alone, while a parallel or hybrid combination (all functions over the whole pool) cannot.

Measured effect: K-Centers then BALD reached 80% accuracy on CIFAR-10 in 9 fewer acquisition rounds than BALD alone, 7200 labels, about 12% of the dataset; the conclusion reports almost half the acquisition cost.[^c5] Successes over 12 repetitions rose from 2 to 6.[^c4]

Two other findings from the same paper. Alternation (random, annealed, or feedback-driven switching between functions each round) with BALD and BADGE gave win rates above 50%, attributed to their complementary spaces, weight versus prediction.[^c6] Top-K selection in parallel-ranked structures amplifies batch redundancy, which series filtering mitigates.[^c6]

## Limits

The benefit is domain-dependent: Series K-Centers then BALD won above 50% on CIFAR-10/100 but only 9% on the noisy PTB-XL ECG data, where early embeddings are unreliable.[^c6] The authors say the best combination depends on dataset, architecture and constituent principles, not a one-size-fits-all rule.[^c7] Gains were shown for image and ECG classification with neural networks; transfer to question selection by language models is my inference, not tested. Energy is treated as proportional to execution time, not measured directly. Series BADGE then K-Centers gave no significant gain.

## Related

- [[exploit-explore-union-selection]] — a parallel union of exploit and explore rankings, versus the sequential sieve here.
- [[ball-coverage-acquisition]] — a coverage-style acquisition of the kind used as the first stage.
- [[expected-information-gain]] — the uncertainty-style score such chains refine with.
- [[cost-energy-scale-calibration]] — cost of acquisition itself as a consideration.

[^c1]: arxiv-2602-07440 — "representativity-based acquisition functions effectively explore the dataset but do not prioritize boundary decisions"
[^c2]: arxiv-2602-07440 — "reducing the pool of data on which the next acquisition"
[^c3]: arxiv-2602-07440 — "the cost of using this second acquisition function on top"
[^c4]: arxiv-2602-07440 — "forward passes. Applying BALD on top of K-Centers"
[^c5]: arxiv-2602-07440 — "this represents 12% of the total available samples"
[^c6]: arxiv-2602-07440 — "consistently achieve winning rates above 50% across"
[^c7]: arxiv-2602-07440 — "rather than on a"
