---
description: "Equal bits of entropy reduction can differ entirely in bearing on action; more answering capacity raises the rate of uncertainty reduction but does not choose which questions are worth asking."
aliases: ["rate is not direction", "bearing of a question", "directional knowledge"]
sources: ["arxiv-2603-06630"]
---
# Entropy versus bearing on action

Shannon mutual information measures how much a question's answer reduces uncertainty, I(Q;X) = H(X) - H(X|Q). The paper argues this is insufficient for choosing questions: "entropy reduction is not the same as directional knowledge."[^c1] Ten bits about tomorrow's weather and ten bits about which treatment extends a patient's life carry identical entropy but differ in their bearing on action, a term the authors take from Cox's logic of inquiry, where the bearing of a question measures its relevance to an outstanding issue.[^c2]

## The claim

Knowledge relevant to action is reduced uncertainty about the consequences of interventions, not about what will be observed. Expanding answering capacity increases how fast uncertainty is reduced; "rate is not direction."[^c3] Which question to ask needs a model linking information to consequences, a causal structure the token-generating process does not itself supply.[^c4]

## Agency, as the paper defines it

The capacity to formulate high-bearing questions, update beliefs coherently, act when probability models are incomplete, and preserve adaptability across regime change.[^c5] Under structural uncertainty (unknown, shifting models) the authors recommend iterative, option-preserving inquiry over static optimization, since irreversible actions collapse branches of future possibilities. This is argued, not tested.

## Limits

- A conceptual argument; no experiment or benchmark measures bearing, and the paper does not define a computable bearing score.
- Cox's logic of inquiry is cited, not derived; the claim that it "uniquely determines" ordering by expected information gain is asserted in passing.
- Expected information gain already ranks questions within a fixed model; the paper's point concerns uncertainty about the model itself, which it leaves informal.

## Related

- [[physical-question-budget]] — the count of questions this note says is not enough to choose among them.
- [[value-of-information]] — decision-relevance of an answer, the closest formal counterpart to bearing.
- [[reversibility]] — option-preserving versus irreversible actions.
- [[question-budgets]] — budgets by source of answer.

[^c1]: arxiv-2603-06630 — "entropy reduction is not the same as directional knowledge."
[^c2]: arxiv-2603-06630 — "The “bearing” of a question on an"
[^c3]: arxiv-2603-06630 — "rate is not direction."
[^c4]: arxiv-2603-06630 — "which questions to ask requires a model connecting information to consequences—"
[^c5]: arxiv-2603-06630 — "Formulate high-bearing questions,"
