---
description: "A verifier-free stopping signal: how much the policy's own log-probabilities shift when a rubric is placed in context, which tracks reference-panel reward and peaks where that reward peaks."
aliases: ["self-gap", "verifier-free rubric diagnostic", "rubric-conditioned log-probability gap", "self-internalization diagnostic"]
sources: ["doi-10-48550-arxiv-2605-12474"]
---
# Self-internalization gap

Checking whether an RL policy is still improving normally takes an external judge. The self-internalization gap tries to read the same signal from the policy itself. The idea: a policy that has absorbed a rubric should assign nearly the same probability to its own responses whether or not the rubric is in its context. The gap measures how far apart those two distributions still are.[^c1]

Concretely, for each evaluation prompt the policy draws K = 10 responses under the rubric-conditioned context (the rubric placed in the system prompt). Each response is then scored under both contexts, the rubric-conditioned one and the prompt-only one used in RL training, and the per-token average log-probabilities are compared. The gap is the length-normalized difference, averaged over the evaluation set.[^c2] By construction it is at most zero in expectation, so its negative is a Monte Carlo estimate of the forward KL from the rubric-conditioned distribution to the prompt-only one. A gap near zero means the prompt-only distribution has come to resemble the rubric-conditioned one, which the paper reads as internalization of the rubric.[^c3]

The gap is a diagnostic, not a reward. The paper's use of it is as a stopping signal. Under weak training verifiers the gap peaks mid-training and then plateaus or reverses, and its argmax falls near the peak of the reference reward; the training verifier's own reward, by contrast, keeps rising to the final checkpoint.[^c4] The within-run Pearson correlation with the reference reward "lies in r ∈ [0.91, 0.97] over the full training trajectory" across the four main runs.[^c5] So a practitioner who cannot afford the panel can, in these runs, see from the policy's own log-probabilities roughly when the proxy has stopped tracking quality. The paper states the result plainly: "Self-gap recovers the same stopping signal as the panel-based metric without requiring an external panel."[^c6]

## Limits

- The paper's claim is "in our experiments," on four main runs (medical and science, two weak and two strong verifiers) plus the 14B and 32B policies in the medical weak-verifier setting. The gap's behaviour under other rubrics, other domains, or other stopping rules is not shown.
- The correlation is within each run over the trajectory. It says the gap moves with the reference reward; it does not show that the gap can predict the reference reward's level in a new run without the panel.
- The gap could close for a trivial reason: RL can push the policy toward longer, rubric-shaped outputs whose per-token log-probability is dominated by repeated structure. The paper addresses this with a length check, and reports that "Appendix G.3 rules out a response-length-driven explanation." I did not read that appendix; I cite the main-text claim only.
- The rubric-conditioned reference is itself a policy whose quality could drift. The paper reports that "the rubric-conditioned reference does not degrade during training" (Appendix G.1, cited as stated in the main text), but this rests on one policy family.
- The gap measures agreement between two contexts of one model. A policy can internalize a rubric's wording and still be exploiting it, so a small gap does not rule out verifier exploitation. The paper pairs it with the exploitation rate for that reason ("the former localizes criterion-level verifier errors, while the latter provides a policy-level stopping diagnostic").[^c7]

## Related

- [[verifier-exploitation-rate]] — the panel-based measure this gap is meant to stand in for; the two are complementary, not interchangeable
- [[rubric-aware-on-policy-self-distillation]] — a rubric-conditioned teacher scoring a rubric-free student's rollouts, the same conditioning used to move a rubric into weights; here the conditioned and unconditioned log-probabilities are compared rather than distilled
- [[pairwise-advantage-validity-stopping]] — another stopping rule for self-reward training that needs no external anchor, though it uses a human-verified holdout rather than the policy's own log-probabilities
- [[reward-overoptimization]] — the general pattern of a proxy that keeps rising while quality falls, which the stopping signal is meant to detect

[^c1]: doi-10-48550-arxiv-2605-12474 — "a verifier-free diagnostic based on policy log-probabilities, which tracks reference-verifier quality"
[^c2]: doi-10-48550-arxiv-2605-12474 — "The self-internalization gap is the length-normalized log-prob difference"
[^c3]: doi-10-48550-arxiv-2605-12474 — "indicate that the prompt-only distribution has come to resemble the rubric-conditioned one"
[^c4]: doi-10-48550-arxiv-2605-12474 — "under both weak verifiers ∆(t) peaks mid-training and then plateaus or reverses,"
[^c5]: doi-10-48550-arxiv-2605-12474 — "lies in r ∈ [0.91, 0.97] over the full training trajectory"
[^c6]: doi-10-48550-arxiv-2605-12474 — "same stopping signal as the panel-based metric without requiring an external panel"
[^c7]: doi-10-48550-arxiv-2605-12474 — "the former localizes criterion-level verifier errors, while the latter provides a policy-level stopping diagnostic"
