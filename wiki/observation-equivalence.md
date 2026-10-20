---
description: "Online RL is causal because the learner observes every cause of its own actions, so no latent confounder ties actions to rewards and conditional probabilities equal interventional ones."
aliases: ["observation-equivalent policies", "observational equivalence"]
sources: ["doi-10-48550-arxiv-2403-04221"]
---
# Observation-equivalence

A policy is a map from the observations it conditions on to actions. Two
policies are observation-equivalent when the behavioural policy that generated
the data and the learned policy condition on the same observation signal. An RL
setting "satisfies observation-equivalence if the behavioral and the learned
policy are based on the same observation signal."[^c1] The causal point is that
the observation signal causes a policy's decisions, so two policies share their
causes only if they share their observations.[^c2]

The mechanism is confounding. A latent variable confounds an action and a
reward when it causes both and the learner does not observe it. The paper's
sports example makes this concrete: "Thus Player Health is a common cause of the
action and reward."[^c3] A coach who does not see player health therefore reads
shots and goals through a confounder. "Because of the confounder, conditional
probabilities generally do not correctly estimate" the causal effect of an
action.[^c4]

Observation-equivalence removes the latent parent of the action. The chain in
the paper runs: observation-equivalence implies that "every cause of the observed
actions is observed by the learning agent," so "Actions and rewards are therefore
not confounded by a latent variable."[^c5] Together with temporal ordering, the
paper's main proposition is that "given observation-equivalence and temporal
ordering, causal effects and what-if counterfactuals" coincide with conditional
probabilities.[^c6] Temporal ordering carries its own half of the argument:
"causes do not succeed effects temporally."[^c7]

Why online learning meets the condition. The agent "is transparent to itself, the
agent is aware of the causes of its own actions," so the causes of its actions
"are therefore accessible to the learning agent in online learning."[^c8] The
argument covers exploration too. In the paper's epsilon-greedy example the
behaviour policy differs from the current policy, yet "both are based on the same
observations."[^c9] The paper adds that "this conclusion applies to both on-policy
and off-policy learning."[^c10]

Online learning is not the only route. The paper states that "The online setting
is sufficient but not necessary for observation-equivalence."[^c11] On-policy
learning, where the behavioural and learned policies are the same, is another
sufficient condition.[^c12] Complete observability is a third: "Under complete
observability, the learning agent has access to the same observations as" the
behavioural agent.[^c13]

Where it fails. The paper's conclusion is that "causal effects differ from
conditional probabilities in the offline off-policy RL setting with partial"
observability.[^c14] There the learner "does not have access to all the causes of
the decisions made by the behavioral agent," and the action-reward pair can be
confounded from the learner's side.[^c15]

## Limits

- The result is stated for discrete variables: "Throughout the paper we assume
  that random variables are discrete."[^c16]
- The support is theorems and worked examples. "We support this conclusion with
  theorems based on causality theory."[^c17] The text read here reports no
  measurement of how large the conditional-versus-interventional gap is in an
  actual trained agent.
- The self-transparency premise is an assumption about the agent, not a test of
  it. If the learner's logged observation omits a variable that drives both its
  exploratory actions and the reward, the condition fails. The paper's
  epsilon-greedy case only shows that exploration noise that does not touch the
  reward is harmless (my reading, not the paper's claim).
- Observation-equivalence concerns confounding by latent variables only. It says
  nothing about other bias sources, such as a logging process that drops
  observations or a reward that is measured with error.

## Related

- [[hindsight-counterfactual]] — the same paper's split: under this condition
  what-if counterfactuals reduce to conditionals, hindsight ones do not.
- [[coverage-separation-offline-online]] — another offline/online split, drawn in
  terms of data coverage rather than confounding.
- [[action-sufficient-compression]] — shares the phrase "action sufficiency" with
  the paper's chain but is a different object: a policy-equivalence quotient of
  support states, not a condition on observed causes.
- [[common-support-positivity]] — the usual adjustment-side condition that a
  confounder stratum must contain every treatment arm; a separate requirement from
  the one here.

[^c1]: doi-10-48550-arxiv-2403-04221 — "the behavioral and the learned policy are based on the same observation signal"
[^c2]: doi-10-48550-arxiv-2403-04221 — "observation signal causes their decisions"
[^c3]: doi-10-48550-arxiv-2403-04221 — "Thus Player Health is a common cause of the action and reward."
[^c4]: doi-10-48550-arxiv-2403-04221 — "Because of the confounder, conditional probabilities generally do not correctly estimate"
[^c5]: doi-10-48550-arxiv-2403-04221 — "Actions and rewards are therefore not confounded by a latent variable"
[^c6]: doi-10-48550-arxiv-2403-04221 — "given observation-equivalence and temporal ordering, causal effects and what-if counterfactuals"
[^c7]: doi-10-48550-arxiv-2403-04221 — "causes do not succeed effects temporally."
[^c8]: doi-10-48550-arxiv-2403-04221 — "are therefore accessible to the learning agent in online learning"
[^c9]: doi-10-48550-arxiv-2403-04221 — "both are based on the same observations."
[^c10]: doi-10-48550-arxiv-2403-04221 — "this conclusion applies to both on-policy and off-policy learning"
[^c11]: doi-10-48550-arxiv-2403-04221 — "The online setting is sufficient but not necessary for observation-equivalence."
[^c12]: doi-10-48550-arxiv-2403-04221 — "the behavioral and the learned policy are the same, so they are observation-equivalent"
[^c13]: doi-10-48550-arxiv-2403-04221 — "Under complete observability, the learning agent has access to the same observations as"
[^c14]: doi-10-48550-arxiv-2403-04221 — "is that causal effects differ from conditional probabilities in the offline off-policy RL setting with partial"
[^c15]: doi-10-48550-arxiv-2403-04221 — "When the learning agent does not have access to all the causes of the decisions made by the behavioral agent"
[^c16]: doi-10-48550-arxiv-2403-04221 — "Throughout the paper we assume that random variables are discrete."
[^c17]: doi-10-48550-arxiv-2403-04221 — "We support this conclusion with theorems based on causality theory"
