---
description: "A testable learner may refuse: it outputs a hypothesis only when the data distribution has a checkable property, and any hypothesis it outputs must be near-optimal."
aliases: ["testable agnostic learning", "testable learning model", "testably learnable", "TL-Q"]
sources: ["arxiv-2512-02279"]
---
# Testable learning

A testable learner is allowed to refuse, and the refusal is part of its contract. It receives i.i.d. samples from an unknown distribution D over inputs and labels, and it outputs either a hypothesis h or the symbol ⊥. Two guarantees bind it. Soundness: whenever it outputs a hypothesis, that hypothesis is near-optimal for the concept class, with high probability.[^c2] Completeness: when D has the desired property, the learner must not refuse; it "outputs a hypothesis (instead of ⊥) with high probability."[^c3]

The property is the lever. Plain distribution-specific learning promises a competitive hypothesis only when the distribution has some property, and says nothing otherwise: "if the distribution does not satisfy the property, then the behavior of the learner is" undefined.[^c4] The testable model replaces that undefined region with an explicit output. The learner combines a distribution-specific learner with a tester for the property, and "may output a hypothesis or it may reject" the distribution.[^c5]
The model is worth having because it can be efficient where distribution-free learning is not. The paper notes that "there are efficient algorithms for testable learning in cases where distribution-free learning cannot be done efficiently."[^c6] Its main line of argument reduces through refutation: the paper gives "a general reduction from sample-based refutation of boolean concept classes" to testable learning with queries.[^c7] Refutation asks the converse question, whether the labels look correlated with some concept in the class or look like noise, and the reduction turns a testable learner into such a distinguisher.

Reading for questions and answers (my inference, not the paper's, which is about learning only): a testable answerer commits only on inputs it can check belong to a region, and is held to the accuracy of that commitment there. The gate sits on the distribution of inputs, not on the confidence of a single answer. This is the same object that [[distribution-knowledge-gap-in-abstention]] studies in a stream: there, knowing the distribution changes the price of abstaining, and the learner cannot tell which items it should abstain on. A testable learner moves that question into an explicit test that runs before any answer is committed. Whether that test is cheap enough to matter for language answering is not something this paper addresses.

## Limits

- The guarantees are stated over a family F of distributions, and the results are for specified families and concept classes. Nothing here says what the right property is for a given task.
- The paper proves lower bounds on testable learning with queries. It does not give a new efficient testable learner, and it does not run any experiment.
- Soundness and completeness are stated with constants c and ε and failure probability δ; the bounds are relative to the best concept in the class (opt), so a hypothesis can be far from the truth when the class itself is a poor fit.
- The semi-agnostic variant, where the error bound is O(opt) + ε instead of opt + ε, is only partly connected to the paper's reduction. "It is an open question for future work to resolve the connection between" semi-agnostic testable learning with queries and semi-agnostic learning.[^c8]
- Whether sample-only testable learning reduces to query-based testable learning is open; the paper states it as a conjecture, not a result.[^c9]

## Related

- [[membership-queries]] — the query-access variant of this model; queries do not speed testable learning beyond samples.
- [[distribution-knowledge-gap-in-abstention]] — the stream version of the same question: what knowing the distribution buys an abstaining learner.
- [[abstention]] — refusal as an output; testable learning gates the refusal on the distribution rather than on the answer.

[^c1]: arxiv-2512-02279 — "the learner must output a hypothesis whenever the data distribution satisfies a desired property,"
[^c2]: arxiv-2512-02279 — "If the learner outputs a hypothesis h, then with high probability"
[^c3]: arxiv-2512-02279 — "hypothesis (instead of ⊥) with high probability."
[^c4]: arxiv-2512-02279 — "if the distribution does not satisfy the property, then the behavior of the learner is"
[^c5]: arxiv-2512-02279 — "It may output a hypothesis or it may reject"
[^c6]: arxiv-2512-02279 — "algorithms for testable learning in cases where distribution-free learning cannot be done efficiently."
[^c7]: arxiv-2512-02279 — "We give a general reduction from sample-based refutation of boolean concept classes"
[^c8]: arxiv-2512-02279 — "It is an open question for future work to resolve the connection between"
[^c9]: arxiv-2512-02279 — "we do not resolve the strongest, most natural question on the power of membership queries: whether"
