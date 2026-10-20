---
description: "Finding an epsilon-optimal arm among n with probability 1-delta needs on the order of (n/eps^2)log(1/delta) samples for any sampling policy; adaptivity cannot beat this."
aliases: ["PAC multi-armed bandit lower bound", "sample complexity of exploration lower bound", "best-arm identification lower bound"]
sources: ["mannor-2003"]
---
# PAC best-arm sample complexity lower bound

In the PAC multi-armed bandit model, a sampler must output an epsilon-optimal arm among n arms with probability at least 1-delta. Even-Dar et al. showed that a total of O((n/eps^2) log(1/delta)) plays suffice.[^c1] Mannor and Tsitsiklis (2003) supply the matching lower bound, and it holds for any sampling policy.[^c2] So the cost of identifying a good option by sampling scales linearly in the number of options, quadratically in the inverse accuracy, and logarithmically in the inverse confidence. No adaptive allocation, however clever, changes the order.

The bound is also generalized in two directions: to a Bayesian setting, and to the case where the statistics of the arms are known but the identities of the arms are not.[^c3] The second case matters for questioning: knowing what the possible answers look like does not remove the need to sample to find which source gives which.

## Limits

Only the abstract was available in the text I read; the proof, constants, assumptions on reward distributions (the abstract does not state them) and the exact Bayesian statement are not established here. Applying it to asking questions (each question as an arm pull) is my own inference: it assumes independent noisy answers with a fixed gap, which question-asking rarely satisfies.

## Related

- [[thompson-sampling]] — a bandit heuristic whose guarantees this bound limits
- [[one-bit-mean-estimation]] — another result that fixes sample complexity and shows adaptivity cannot help
- [[odds-theorem-lower-bound]] — a lower bound in sequential decision making
- [[plug-in-glr-stopping-rule]] — a stopping rule for sequential identification
- [[information-directed-sampling]] — an adaptive sampler that this bound caps in order

[^c1]: mannor-2003 — "it suffices to play the arms a total of"
[^c2]: mannor-2003 — "Our contribution is a matching lower bound that holds for any"
[^c3]: mannor-2003 — "We also generalize the lower bound to a Bayesian setting"
