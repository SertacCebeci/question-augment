---
description: "Asking what would have happened under another action after seeing the outcome needs a causal model; even in online RL, where what-if counterfactuals reduce to conditionals, it does not."
aliases: ["hindsight query"]
sources: ["doi-10-48550-arxiv-2403-04221"]
---
# Hindsight counterfactual

A counterfactual question asks what would have followed had an agent chosen
differently. The paper separates two versions. "A what-if query concerns the
results of deviating from an action taken."[^c1] A hindsight query adds the
outcome that was actually observed, so it asks the same question after the fact.
Its example from a sports domain is "I failed to score. What if I had taken"
a shot instead of making a pass.[^c2]

In the paper's notation, the what-if level conditions on the state and the
alternative action, while the hindsight level adds the realised reward to the
conditioning set. (This is my reading of the Table 1 notation, which is garbled
in the text.) The two levels sit on a four-level causal hierarchy that the paper
builds on Pearl's three levels: the hierarchy is "A four-level causal hierarchy,
which refines" Pearl's association, intervention and counterfactual levels.[^c3]

The mechanism the paper establishes is a difference in what conditioning can
do. What-if counterfactuals can be computed from conditional probabilities under
observation-equivalence and temporal ordering. Hindsight counterfactuals cannot:
"Our analysis indicates that in online RL, what-if counterfactuals can be
evaluated using conditional probabilities, whereas hindsight counterfactuals
require a causal model beyond conditional probabilities, even in online RL."[^c4]
The short form is "hindsight counterfactuals cannot be reduced to conditional
probabilities, even in online RL."[^c5]

The condition that rescues the what-if level, observation-equivalence, is
therefore not enough for the hindsight level. Online learning removes the
latent-confounder route to bias, but the realised reward still has to be
explained through a model of the environment rather than read off a table of
conditionals. A conjecture of mine, not the paper's: the realised reward carries
information about latent state that the counterfactual reward also depends on,
and a conditional over observed history has no slot for that update. The text I
read states the result without this proof; the proof sits in the section on
hindsight counterfactuals, which I did not read.

## Limits

- The claim is for the paper's setting: discrete variables throughout, and the
  causal model is a dynamic decision network the paper defines.[^c6]
- The text establishes that a causal model is needed, not how to estimate one.
  It reports no experiment that estimates a hindsight counterfactual from data.
- The four-level split is the paper's refinement of Pearl's three levels. Whether
  the what-if and hindsight levels are the right cut is a modelling choice the
  text argues for, not a fact the literature fixes.
- The sports example is a tutorial illustration with binary variables, not a
  measured case.

## Related

- [[observation-equivalence]] — the condition under which what-if counterfactuals
  reduce to conditionals; hindsight counterfactuals are not covered by it.
- [[backtracking-counterfactual]] — a different dispute about counterfactuals, on
  whether upstream causes may change when a variable is set; the what-if and
  hindsight split does not settle it.
- [[potential-outcome-counterfactual-semantics]] — when a counterfactual
  probability is unique and point-identified; the route to asking whether a
  hindsight query is identified.
- [[rung-stratified-causal-accuracy]] — scoring a model on Pearl's rungs; the
  paper's four levels would give a finer axis for the same kind of test.

[^c1]: doi-10-48550-arxiv-2403-04221 — "A what-if query concerns the results of deviating from an action taken"
[^c2]: doi-10-48550-arxiv-2403-04221 — "I failed to score. What if I had taken"
[^c3]: doi-10-48550-arxiv-2403-04221 — "A four-level causal hierarchy, which refines"
[^c4]: doi-10-48550-arxiv-2403-04221 — "evaluated using conditional probabilities, whereas hindsight counterfactuals require a causal model beyond"
[^c5]: doi-10-48550-arxiv-2403-04221 — "hindsight counterfactuals cannot be reduced to conditional probabilities, even in online RL."
[^c6]: doi-10-48550-arxiv-2403-04221 — "Throughout the paper we assume that random variables are discrete."
