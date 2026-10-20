---
description: "Bayesian model reduction scores a reduced model's evidence from the full model's posterior and prior counts alone, so rival structures are compared after the data are in, with no refitting."
aliases: ["BMR", "post hoc Bayesian model selection", "Bayesian model selection by reduction"]
sources: ["arxiv-2512-21129"]
---
# Bayesian model reduction

Bayesian model reduction (BMR) gives the evidence of a *reduced* model from
the posterior and prior of its *full* (parent) model, without refitting the
data.[^c1] A reduced model is the parent with some parameters pinned, in the
paper's implementation by shrinking the corresponding Dirichlet counts to zero
or a small value.[^c14] Its posterior is not estimated afresh: it is read off
the parent posterior, "the posterior that would obtain under the reduced
model".[^c2] For Dirichlet (categorical) parameters the change in log marginal
likelihood between the two models is then an explicit function of three count
vectors: the posterior counts, the prior counts, and the reduced prior counts.[^c3]
The result is a closed form in the counts and the beta function, so each
candidate is scored by arithmetic on counts already accumulated.

## Selection by reduction

Given a set of candidate reduced models, the paper treats the model index as a
random variable and places a flat prior over the set, so that the prior over
parameters becomes a Bayesian model average over the candidates.[^c4] Each
candidate's posterior probability then follows from its reduced evidence, and
evidence accumulates model by model as data arrive. The average is kept until
one model dominates. The paper's threshold is a log odds ratio of 16 natural
units, which makes the leading model at least exp(16) times likelier than any
alternative; past that point "the Bayesian model average becomes Bayesian model
selection".[^c5] The number 16 is the authors' choice, not a derived quantity.

In the paper this is applied to a three-ball task in which the agent must find
which likelihood mapping (a rule) generates feedback, out of 81 candidates.
The commitment is a stopping decision on the model posterior: once it is
taken, the agent acts on the selected rule.

## Limits

- **Post hoc.** The paper states that "selection is a post-hoc process that is
  enacted after sufficient data have been accumulated."[^c6] It separates this
  from inference over models: "This is distinct from inferring the model per
  se."[^c7] The appendix treats the post-hoc update as an approximation to
  continual structure learning, via Jensen's inequality (my reading of the
  appendix; the approximation is not tested in the text). The practical benefit
  the paper names is that "a post hoc scheme means one does not have to entertain
  multiple models during active inference and learning."[^c8]
- **Commitment can be premature.** "Clearly, this does not guarantee that" the
  selected model is the best model.[^c9] In the 64 simulated games one
  application was premature: "was applied prematurely", and the wrong model was
  kept.[^c10] The paper concludes that "there is always a possibility of jumping
  to conclusions," even at a stringent threshold.[^c11]
- **Only the models supplied.** BMR ranks the candidates it is given and cannot
  find a rule outside them. The paper says "an outstanding issue is the
  elaboration of alternative models", and that the model space "effectively
  implements hyperpriors over hypothetical rules."[^c12][^c13] Building the
  candidate set is a separate problem the text does not solve.
- **Shrinkage is a choice.** Reduction is implemented by setting counts to
  near zero, "one simply applies shrinkage priors by setting Dirichlet counts
  to" zero or a small value; the value and the threshold are free settings.[^c14]
- **Scope of the text.** The results are numerical, on one discrete partially
  observed task. The text reports no timing against refitting and no
  comparison with other model-selection methods; the claim that BMR is fast
  rests on the closed form alone (my reading).

## Related

- [[structure-information-gain]] — uses the reduced-model posteriors to score
  which observation would best separate the candidate structures.
- [[expected-information-gain]] — the parameter-level information gain that
  BMR's post-hoc selection sits beside; the same functional, different index.
- [[bayesian-estimation]] — the parameter posterior updates that BMR reuses
  without refitting.
- [[stopping-rules]] — the log-odds threshold is a commitment rule: stop
  comparing and act on the leading model (my reading).

[^c1]: arxiv-2512-21129 — "and efficient form of Bayesian model selection that allows one to evaluate the evidence"
[^c2]: arxiv-2512-21129 — "the posterior that would obtain under the reduced model"
[^c3]: arxiv-2512-21129 — "the change in log marginal likelihood can"
[^c4]: arxiv-2512-21129 — "the model m becomes a random variable, over which we can"
[^c5]: arxiv-2512-21129 — "If we use a threshold of 16 natural units,"
[^c6]: arxiv-2512-21129 — "selection is a post-hoc process that is enacted after sufficient data"
[^c7]: arxiv-2512-21129 — "This is distinct from inferring the model per se."
[^c8]: arxiv-2512-21129 — "a post hoc scheme means one does not have to entertain"
[^c9]: arxiv-2512-21129 — "Clearly, this does not guarantee that"
[^c10]: arxiv-2512-21129 — "was applied prematurely"
[^c11]: arxiv-2512-21129 — "there is always a possibility of jumping to conclusions"
[^c12]: arxiv-2512-21129 — "An outstanding issue is the elaboration of alternative models"
[^c13]: arxiv-2512-21129 — "effectively implements hyperpriors over hypothetical rules"
[^c14]: arxiv-2512-21129 — "one simply applies shrinkage priors by setting Dirichlet counts to"
