---
description: "Membership queries let a learner choose the points it is labelled on; in the testable setting they cannot speed learning beyond what random labelled examples already allow."
aliases: ["membership query access", "MQ learning", "query access to the labelling function"]
sources: ["arxiv-2512-02279"]
---
# Membership queries

In the membership-query model the learner gets labelled examples drawn i.i.d. from a distribution over inputs, and it may also choose any point and receive that point's label. The learner "may also query any point x" and receive its label f(x).[^c1] The difference from passive learning is that the learner decides where its information comes from, not only how much of it there is.

Queries help in one setting and not another. Under a standard cryptographic assumption, "membership queries can speed up agnostic learning in the distribution-specific setting," while in the distribution-free setting every class learnable with queries is learnable from random examples.[^c2] The paper's examples are on the uniform distribution over the hypercube. For k-juntas the query algorithm is fast, while a statistical-query lower bound of n^Ω(k) applies to sample-only learners; and if learning sparse parities with noise is hard, one "cannot hope to do better than this bound with random examples."[^c3] The paper's reading of the query algorithms in this family is that they "use membership queries only to estimate statistical properties of the unknown function."[^c4]

The main result concerns the testable model, where the learner must also refuse on distributions that lack a property (see [[testable-learning]]). There, the paper states that "membership queries cannot decrease the time complexity of testable learning algorithms beyond" the complexity of sample-only distribution-specific learning.[^c5] The argument is a reduction that answers each query with a random function, so the learner's queries become samples: "Instead we have to answer queries, so we will answer them randomly."[^c6] The learner's training and test sets are then filtered to the points where the sampled label agrees with that function, and the remaining distribution is what the learner sees. This is a reduction from refutation, which separates correlated labels from noise, so a query-based testable learner yields a sample-based refutation algorithm.[^c12]

The paper also defines a restricted class, which it calls statistical membership-query algorithms: "those that use membership queries only to sample from particular distributions over the input" domain.[^c7] Influence estimation and statistical queries over large subcubes fall in this class. For this class the paper proves that a testable learner implies a small SQ dimension, "the SQ dimension of C with respect to D is at most poly(t)," where t is the learner's running time.[^c8] Combined with known SQ dimension lower bounds, the efficient query learners in this class cannot be made testable.[^c13]

Reading for questions (my inference, not the paper's, which is about learning): choosing which points to ask about is a real advantage when the answer need not be gated by a test of the input distribution. Once the answer must be committed only when the input region is checkable, the advantage of choosing the query points does not survive, at least in the statistical class the paper covers.

## Limits

- The result is a lower bound for MQ-SQ algorithms. The paper states that the bound holds "without introducing non-statistical use of membership queries," so a learner that uses queries in other ways is not covered.[^c9]
- The reduction works only when no degenerate query is made, that is, a query whose distribution is a single point: "Our reduction for MQ-SQ algorithms only works when no such queries" are made.[^c10] The theorem also requires the number of queries to be o(poly(d)) for SQ dimension d, and a norm bound on the query distributions.
- Whether sample-only testable learning is as hard as query-based testable learning is a conjecture, not a result.[^c11]
- Everything is theoretical and for boolean concept classes over finite domains; the paper runs no experiment, and its examples are the uniform distribution on the hypercube.
- The non-testability conclusion depends on known SQ dimension lower bounds for the classes named; a class with no such bound is not addressed by this result.

## Related

- [[testable-learning]] — the model in which the query result is stated; the query access is added to its soundness and completeness contract.
- [[distribution-knowledge-gap-in-abstention]] — a sample-side gap: there too the learner's knowledge of the distribution changes what abstaining costs, though no queries are involved.

[^c1]: arxiv-2512-02279 — "may also query any point x"
[^c2]: arxiv-2512-02279 — "membership queries can speed up agnostic learning in the distribution-specific setting"
[^c3]: arxiv-2512-02279 — "hope to do better than this bound with random examples."
[^c4]: arxiv-2512-02279 — "use membership queries only to estimate statistical properties of the unknown function."
[^c5]: arxiv-2512-02279 — "membership queries cannot decrease the time complexity of testable learning algorithms beyond"
[^c6]: arxiv-2512-02279 — "Instead we have to answer queries, so we will answer them randomly."
[^c7]: arxiv-2512-02279 — "those that use membership queries only to sample from particular distributions over the input"
[^c8]: arxiv-2512-02279 — "distribution D by an MQ-SQ algorithm, then the SQ dimension of C with respect to D is at most"
[^c9]: arxiv-2512-02279 — "without introducing non-statistical use of membership"
[^c10]: arxiv-2512-02279 — "Our reduction for MQ-SQ algorithms only works when no such queries"
[^c11]: arxiv-2512-02279 — "If a concept class C is agnostically testably learnable with queries in time t over"
[^c12]: arxiv-2512-02279 — "if a class is efficiently testably-learnable, then it is efficiently"
[^c13]: arxiv-2512-02279 — "lower bounds, our results imply that these efficient membership query learners cannot be made"
