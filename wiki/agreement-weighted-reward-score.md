---
description: "Scoring a candidate by a softmax-weighted mix of its reward and how many already-selected answers match it moves selection between best-of-n and majority voting by one weight."
aliases: ["agreement-weighted soft score", "reward-agreement interpolation", "best-of-n and majority-vote interpolation", "agreement-modified reward"]
sources: ["arxiv-2512-05542"]
---
# Agreement-weighted reward score

A candidate drawn among several samples can be ranked two ways: by its reward, or by how many other samples give the same final answer. The score described here uses both at once. Over the set S of candidates already selected, each member ℓ gets a softmax weight w_ℓ = exp(β·r_ℓ) / Σ_j exp(β·r_j). The set is then scored by Σ_ℓ w_ℓ · (α·r_ℓ + (1−α)·agree_S(a_ℓ)), where agree_S(a_ℓ) is the fraction of S that gives the same normalized answer as member ℓ, and α ∈ [0, 1] sets the mix. The authors describe the result as "an interpolation between best-of-n and majority voting".[^c1] The reward part "drives selection towards high-reward responses", and the agreement part "acts as a majority vote incentive, prioritizing responses that occur often in S".[^c2]

The endpoints are stated in the text. At α = 0 the rule is agreement alone, "corresponding to majority-style voting".[^c3] With one model and α = 1 it reduces to soft best-of-n, which "recovers standard soft best-of-n for a single model".[^c4] For large β and moderate α the rule "approximates hard best-of-n with an agreement modified reward over a suite of models".[^c5] The experiments use β = 1e5, "which essentially recovers picking an arg max".[^c6] So the softmax is close to a hard pick of the top-reward member of S, and the agreement term is what the score adds. That last reading is my inference from the formula, not the authors' statement.

The score is applied in marginal form. For a tentative candidate, the score is computed over S with that candidate added, not over the candidate alone. The authors tried the simpler per-candidate version and report that it was worse: "this to not work well, and the above score to work much better".[^c7] Their guess is that the marginal form measures what a candidate adds to the set, rather than its own value. The text does not test that guess.

The stated purpose of the agreement term is to damp reward hacking, which the authors say it "can mitigate".[^c8] The evidence they give is indirect. The routed method, which uses this score, shows less degradation than single-model best-of-n as n grows, and the authors say that "the effect is significantly diminished".[^c9] That comparison is between the routed method and single-model baselines. It does not isolate the agreement term from the routing.

## Limits

- Agreement is an exact-match count after normalization: "comparing the normalized answers for exact matches".[^c10] For free-form answers this term has no direct form. The authors name embedding similarity as a possible replacement and do not test it: "one could potentially replace this string-based comparison with embedding similarities".[^c11]
- The mitigation is not isolated. The sections read do not contain the run with the reward term alone on the same suite. The α ablation is cited as showing robustness "as long as α < 1", but that appendix is not in the text read here.
- The authors give no guarantees: "makes it difficult to derive reliable guarantees in practice".[^c12] The agreement term is a vote over the greedy set S, which is built adaptively and is not a set of independent draws. The error bound for majority voting in [[majority-vote-mode-certificate]] is stated for independent samples, so it does not transfer to this score. This is my inference.
- Every result uses one reward model and four 7–8B models. How the score behaves when the reward model is weak or miscalibrated is not tested in the text.

## Related

- [[majority-vote-mode-certificate]] — the α = 0 endpoint is majority voting; that note's error bound assumes independent samples, which the greedy set S does not provide
- [[reward-overoptimization]] — the proxy-rising, true-quality-falling pattern that the agreement term is said to damp
- [[modal-centroid-selection]] — selection among samples with no evaluator at all, the other way to avoid trusting the reward alone
- [[cross-model-best-of-n]] — the routing scheme that uses this score to choose which model's head is committed at each step
- [[test-time-scaling]] — the family whose selection step this score is one design for

[^c1]: arxiv-2512-05542 — "They can be thought of as an interpolation between best-of-n and majority voting"
[^c2]: arxiv-2512-05542 — "a majority vote incentive, prioritizing responses that occur often in S"
[^c3]: arxiv-2512-05542 — "corresponding to majority-style voting"
[^c4]: arxiv-2512-05542 — "recovers standard soft best-of-n for a single model"
[^c5]: arxiv-2512-05542 — "the policy approximates hard best-of-n with an agreement modified reward over a suite of models"
[^c6]: arxiv-2512-05542 — "which essentially recovers picking an arg max"
[^c7]: arxiv-2512-05542 — "this to not work well, and the above score to work much better"
[^c8]: arxiv-2512-05542 — "can mitigate reward hacking"
[^c9]: arxiv-2512-05542 — "the effect is significantly diminished"
[^c10]: arxiv-2512-05542 — "comparing the normalized answers for exact matches"
[^c11]: arxiv-2512-05542 — "one could potentially replace this string-based comparison with embedding similarities"
[^c12]: arxiv-2512-05542 — "makes it difficult to derive reliable guarantees in practice"
