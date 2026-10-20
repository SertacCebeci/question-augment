---
description: "The informativeness of a comparison query depends on the environment it is posed in; searching environment parameters by Bayesian optimisation beats random environments for reward learning."
aliases: ["environment design for preference learning", "bilevel environment and query optimisation"]
sources: ["arxiv-2603-08531"]
---
# Environment design for query informativeness

A question's value is not a property of the question alone. In preference learning the environment fixes which trajectories are feasible and which features they show, so the same learner can ask only weak questions in a poor setting.[^c1] CRED treats environment parameters theta (terrain types, obstacle placement, object configuration) as a variable to optimise alongside the query.[^c2]

## Mechanism

The problem is bilevel: the outer loop chooses theta, the inner loop finds the most informative trajectory pair feasible under theta, with information gain F as the shared objective.[^c3] Because F is not differentiable in theta, a Gaussian-process model with an upper-confidence-bound acquisition (see [[upper-confidence-bound-index]]) proposes environments; each proposal runs the inner generator ([[belief-sample-counterfactual-query-synthesis]]) and feeds back its information gain.[^c4] The bilevel split is chosen for tractability, since the feasible set depends on theta; a joint single-level optimisation is possible in principle but expensive.[^c5]

## Measured

Domain randomisation (random theta, same number of environments as Bayesian optimisation evaluates) underperformed CRED in all variants except random rollouts in Navigation, which the authors attribute to that variant lacking a goal-reaching constraint and so reaching more diverse features.[^c6] Yet in the user study those random-environment trajectories were harder for participants to interpret.[^c7] Applying environment design to the mean-belief baseline (MBP-ED) alone also fell short of full CRED, so the gain needs both components.[^c8]

The point for questioners: diversity that raises simulated information gain can lower the answerer's ability to judge, so informativeness to the learner and answerability for the person are distinct and can diverge (my reading of the two results).

## Limits

- The environment must be controllable by the asker; for questions about a fixed real-world situation this does not apply.
- Tested on three simulated domains and two physical-robot tasks with linear rewards and a uniform prior.
- Bayesian optimisation uses library defaults; sensitivity to the budget was not reported in what I read.
- The interpretability cost of random environments is shown by questionnaire in 25 participants, not isolated causally.

## Related

- [[belief-sample-counterfactual-query-synthesis]] — the inner loop generating queries within a chosen environment
- [[upper-confidence-bound-index]] — the acquisition rule choosing which environment to try
- [[volume-removal]] — another query-scoring criterion, set in a fixed environment
- [[query-by-committee]] — selecting by hypothesis disagreement

[^c1]: arxiv-2603-08531 — "the informativeness of a preference query depends not just on the trajectories, but also on"
[^c2]: arxiv-2603-08531 — "These parameters capture aspects of the environment such as terrain types, obstacle placements, or"
[^c3]: arxiv-2603-08531 — "The outer optimization"
[^c4]: arxiv-2603-08531 — "which models"
[^c5]: arxiv-2603-08531 — "which is more tractable in practice."
[^c6]: arxiv-2603-08531 — "(with the exception of RR-DR in Navigation), highlighting"
[^c7]: arxiv-2603-08531 — "shows that RR-DR trajectories are harder"
[^c8]: arxiv-2603-08531 — "applying environment design to the mean-belief policy baseline."
