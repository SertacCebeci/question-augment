---
description: "Recourse minimises the worst-case cost over every cost function still consistent with a subject's pairwise preferences, so the action hedges what the subject has not revealed."
aliases: ["cost-adaptive recourse", "ReAP", "worst-case cost recourse", "preference-robust recourse"]
sources: ["doi-10-48550-arxiv-2402-15073"]
---
# Cost-robust recourse

Algorithmic recourse proposes a cheap action that reverses an unfavourable
classification.[^c1] Its cost is the crux. Most methods assume the cost is known
in full: they generate recourse "under the assumption of complete knowledge
about the cost function."[^c2] The recommended action is then only as good as a
guess at what this subject finds effortful, and two people with identical
attributes can have different preferences that the attributes do not record.

Cost-robust recourse drops the point guess. The subject's cost is taken to be
a Mahalanobis form, $c(x,x_0) = (x-x_0)^\top A_0 (x-x_0)$, with an unknown
symmetric positive-definite $A_0$.[^c3] The source motivates this form by a
linear-quadratic control argument and by a linear Gaussian structural model,
in which $A_0$ corresponds to the precision matrix of the deviation.[^c4]
Pairwise questions ("which of these two recourses do you prefer to implement?")
each give a linear inequality on $A_0$: a preference for $x_i$ over $x_j$
requires $\langle A_0, M_{ij}\rangle \le \varepsilon$, with $M_{ij}$ built from
the two recourses and $x_0$, and a margin $\varepsilon$ for judgement error.[^c5]
The intersection of these half-spaces with the normalisation $A \preceq I$ is a
convex confidence set $U_P$ of cost matrices consistent with the answers so far.
Nothing outside $U_P$ is treated as possible.

The recourse is then chosen against that set rather than against one matrix.
In the gradient-based version the objective is a validity loss plus $\lambda$
times the worst case over the set, $\max_{A\in U_P} (x-x_0)^\top A (x-x_0)$. The
$\lambda$ "balances the trade-off between the validity and the (worst-case)
cost."[^c6] The graph-based version does the same over paths: edge weights are
costs under a worst-case matrix and the recourse is the path with the lowest
worst-case cost. The source says this is a min-max problem and that it borrows
the idea from robust optimisation: "as a min-max optimization problem. Looking
at the worst-case situation can eliminate any bad"[^c7] route.

The point estimate the set is reduced to is the Chebyshev center of $U_P$,
a question-selection object treated in [[chebyshev-center-query-selection]].
With no questions asked, the paper's reference cost is the squared Euclidean
distance, "between x and x0 , which DiCE and Wachter directly optimize."[^c8]
So the method contains the standard counterfactual objective as its zero-question
case, and the questions move it away from that case.

## What was measured

The experiments use simulated subjects. Ground-truth matrices are generated, and
the answers come from them. With five questions, the gradient-based method
"outperforms the baselines regarding the recourse cost."[^c9] More specifically,
it had validity similar to Wachter's and was at "lower cost in three out of four
datasets."[^c10] On the graph side, the worst-case objective compared with the
centre-only version gave path lengths that "are only marginally higher than the
alternative, highlighting" the method's effectiveness.[^c11] Read this as a cost
of the robust choice being small, not as a demonstration that the worst case
lowers cost. The comparison reported in that passage is of path lengths.

## Limits

- The answers are simulated and the cost metric is the one the method assumes.
  The table's cost is computed in that same family: "We compute the cost as the
  Mahalanobis distance described in Section 6.2."[^c12] A method that assumes a
  Mahalanobis cost will look good under a Mahalanobis evaluation; no
  independent human cost is measured.
- Inconsistent answers break the set. If the subject's preferences form a
  cycle, $U_P$ is empty: "In this case, the set UP becomes empty, and finding a
  Chebyshev center A⋆c is impossible." The fix tolerates a fraction of violated
  answers and needs a binary semidefinite program that the paper says standard
  solvers do not support.[^c13]
- The margin $\varepsilon$ and the normalisation $A \preceq I$ are modelling
  choices. The set, and so the worst case, depends on them. The sections read
  do not test a human's actual margin.
- The worst case is conservative by construction: it prices in every cost the
  answers have not excluded, not the most likely one. Whether that conservatism
  costs much in a real interaction is not measured in the sections read.
- Validity is a classifier property; the robust cost does not make an action
  causally effective. A feature change the model can be moved by need not
  change the outcome in the world; that is the gap treated in
  [[counterfactual-explanation-recourse-gap]], and this method does not close it.

## Related

- [[chebyshev-center-query-selection]] — the question rule that shrinks $U_P$
  and supplies the center used as the point estimate
- [[counterfactual-explanation-recourse-gap]] — the causal gap: a nearest
  counterfactual can miss the outcome under feature dependence; here the gap is
  about the cost, not the causal graph
- [[individual-actionability-constraints]] — the same person-specific cost,
  elicited beforehand as constraints; here it is elicited by comparisons during
  the process
- [[separation-oracle-preference-elicitation]] — the same cut-and-shrink geometry
  for a linear reward, without a recourse step
- [[counterfactual-explanation]] — the explanation this recourse turns into an
  action

[^c1]: doi-10-48550-arxiv-2402-15073 — "Algorithmic recourse recommends a cost-efficient action to a subject to reverse an unfavorable machine learning classification decision."
[^c2]: doi-10-48550-arxiv-2402-15073 — "under the assumption of complete knowledge about the cost function."
[^c3]: doi-10-48550-arxiv-2402-15073 — "The subject x0 has a Mahalanobis cost function of the form"
[^c4]: doi-10-48550-arxiv-2402-15073 — "matrix of the deviation under linear Gaussian structural equation assumption."
[^c5]: doi-10-48550-arxiv-2402-15073 — "to model possible error in the judgment of the subject and to accommodate the"
[^c6]: doi-10-48550-arxiv-2402-15073 — "which balances the trade-off between the validity and the (worst-case) cost, we can generate"
[^c7]: doi-10-48550-arxiv-2402-15073 — "as a min-max optimization problem. Looking at the worst-case situation can eliminate any bad"
[^c8]: doi-10-48550-arxiv-2402-15073 — "between x and x0 , which DiCE and Wachter directly optimize."
[^c9]: doi-10-48550-arxiv-2402-15073 — "outperforms the baselines regarding the recourse cost."
[^c10]: doi-10-48550-arxiv-2402-15073 — "lower cost in three out of four datasets."
[^c11]: doi-10-48550-arxiv-2402-15073 — "are only marginally higher than the alternative, highlighting"
[^c12]: doi-10-48550-arxiv-2402-15073 — "We compute the cost as the Mahalanobis distance described in Section 6.2."
[^c13]: doi-10-48550-arxiv-2402-15073 — "In this case, the set UP becomes empty, and finding a Chebyshev center A⋆c is impossible."
