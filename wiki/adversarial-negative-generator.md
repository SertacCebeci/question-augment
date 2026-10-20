---
description: "A generator rewarded for step errors that fool a process reward model, while the model is rewarded for catching them, makes the negatives harden as the verifier learns."
aliases: ["APRM", "adversarially trained process reward model", "generator-verifier adversarial game", "co-evolving hard-negative generator"]
sources: ["arxiv-2511-22888"]
---
# Adversarial negative generator

A step-level verifier learns from the wrong steps it is shown, so the source of those wrong steps sets which errors it can catch. In the adversarially trained process reward model (APRM), the wrong steps come from a second model that is trained against the verifier. A Generator takes a correct step and perturbs it into an incorrect one. Its reward is one-sided: "It is rewarded +1 for generating an incorrect reasoning step that successfully"[^a1] deceives the verifier. It is penalised for leaving a correct step uncorrupted, and it gets nothing when the verifier catches the error. The Reward Model is paid for agreement with the oracle label: "The PRM is rewarded for accurate classifications."[^a2] Both players are updated by reinforcement learning, so each round the generator's errors move toward the verifier's current blind spots. The paper states the aim in one line: "This interaction yields progressively harder negatives for R".[^a3]

The contrast is with fixed training data, which the paper calls a limit because "they provide a fixed error distribution that cannot adapt to more nuanced errors."[^a4] A second defect it names is in synthetic step data, which rests on the "assumption that correct final answers imply correct intermediate steps."[^a5] The worked example is a cancellation that is invalid at one point yet gives the right final answer, and the authors say adversarial training exposes PRMs to "errors that lead to correct final answer, which static rollouts are not able to."[^a6] My reading is that the fixed-distribution limit and the final-answer assumption are different defects, and the example shows the loop catching only the second kind.

Whether a generated step counts as wrong is decided by an oracle, not by a model. The oracle "uses non-LLM metrics, such as cosine similarity, entity matching (nouns and numbers)," judged against a reference solution.[^a7] The generator's reward therefore depends on that oracle's label. A generated step is "incorrect" as far as the oracle says so.

The game is written as general-sum, with each player's utility penalised by a KL term toward its initial policy and given an entropy bonus. The regularisation is motivated by stability: "standard gradient methods often exhibit undesirable behaviors such as cycling" in non-monotone games.[^a8] The equilibrium is a stationary point, "rather than a mini-max saddle point."[^a9] Under the regularised utilities the paper proves that an equilibrium exists (by Glicksberg's theorem) and that optimistic gradient descent-ascent converges to it linearly, for "game described by the regularized utility functions (Section 2.2) algorithms such as Optimistic".[^a17] These are results about the game over policy distributions. The paper itself notes that policy-space convexity "is different from convexity in the parameter space of a neural model".[^a10]

Measured results are on math and science benchmarks. Averaged over benchmarks and solvers, the paper reports that APRM "improves solver accuracy by +3.4 pp relative to" the strongest trained PRM baseline.[^a11] On the out-of-distribution JeeBench the margin is larger: "where APRM outperforms ReST-MCTS by +5.3 pp".[^a12] When the PRM is the reward for RL on Gemma-3-12B, the paper reports "outperforming outcome-based RL by +6.8 pp on MATH500."[^a13]

## Limits

- The paper does not claim to reach the equilibrium it proves exists: "Nor do we claim in this paper that we are able to find the Nash equilibrium."[^a14] The convergence result is for the regularised game. The accuracy gains are not evidence that the trained weights sit at an equilibrium.
- The generator finds only the errors it can write. The failure cases are theorem-precondition errors, such as applying the Alternating Series Test to a sequence that does not alternate, and the authors "hypothesize that G struggles to generate adversarial negatives that specifically target theorem preconditions".[^a15] They attribute this possibly to backbone size, which was not tested beyond the scaling runs.
- The oracle that labels generated steps is heuristic. I did not read its appendix, so how often it mislabels a generated step is not established here. Any error in the oracle becomes a training error for the verifier.
- The SciBench margin is small: "On GPT-OSS-20B, APRM reaches 63.0% accuracy versus 61.8% for ReST-MCTS".[^a16] The benchmark gains are averages over a few models and benchmarks; no per-benchmark variance is reported in the parts I read.
- The equilibrium vocabulary (Nash, saddle point, GAN) is imported from game theory and GAN training. What survives the transfer is the pressure of an adaptive generator on the verifier. What does not transfer is the convergence guarantee, which is proved in policy space and not for the neural weights.
- The verifier and generator are of the same family in the scaling runs, and all results use the authors' own baselines at matched test-time compute. An independent replication was not part of this reading.

## Related

- [[counterfactual-hard-negative]] — a static, LLM-written negative for preference data; the adversarial generator instead rewrites its negatives as the verifier changes.
- [[controlled-error-injection]] — fixed edits whose error location is known by construction; here the location is not fixed because the generator is trained against the verifier.
- [[process-reward-model-hackability]] — a policy that exploits a PRM without being trained to; APRM applies the same pressure on purpose, during training, to a generator rather than a policy (my inference).
- [[sound-verifier-self-play]] — self-play in which a sound formal checker gates the data; the APRM label comes from a heuristic oracle, not a proof.
- [[process-outcome-consistency-verification]] — another response to right answers reached through wrong steps, by checking derivation consistency rather than generating negatives.

[^a1]: arxiv-2511-22888 — "It is rewarded +1 for generating an incorrect reasoning step that successfully"
[^a2]: arxiv-2511-22888 — "The PRM is rewarded for accurate classifications."
[^a3]: arxiv-2511-22888 — "This interaction yields progressively harder negatives for R"
[^a4]: arxiv-2511-22888 — "they provide a fixed error distribution that cannot adapt to more nuanced errors"
[^a5]: arxiv-2511-22888 — "assumption that correct final answers imply correct intermediate steps"
[^a6]: arxiv-2511-22888 — "errors that lead to correct final answer, which static rollouts are not able to"
[^a7]: arxiv-2511-22888 — "that uses non-LLM metrics, such as cosine similarity, entity matching (nouns and numbers),"
[^a8]: arxiv-2511-22888 — "standard gradient methods often exhibit undesirable behaviors such as cycling"
[^a9]: arxiv-2511-22888 — "rather than a mini-max saddle point"
[^a10]: arxiv-2511-22888 — "This is different from convexity in the parameter space of a neural model"
[^a11]: arxiv-2511-22888 — "benchmarks and four solver models, APRM improves solver accuracy by +3.4 pp relative to"
[^a12]: arxiv-2511-22888 — "where APRM outperforms ReST-MCTS by +5.3 pp"
[^a13]: arxiv-2511-22888 — "outperforming outcome-based RL by +6.8 pp on MATH500"
[^a14]: arxiv-2511-22888 — "Nor do we claim in this paper that we are able to find the Nash equilibrium."
[^a15]: arxiv-2511-22888 — "generate adversarial negatives that specifically target theorem preconditions"
[^a16]: arxiv-2511-22888 — "On GPT-OSS-20B, APRM reaches 63.0% accuracy versus 61.8% for ReST-MCTS"
[^a17]: arxiv-2511-22888 — "game described by the regularized utility functions (Section 2.2) algorithms such as Optimistic"
