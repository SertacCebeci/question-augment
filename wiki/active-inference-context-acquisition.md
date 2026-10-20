---
description: "A bilevel expected-free-energy objective for an agent choosing a context action versus acting now, collapsing to information-gain-per-cost when observations are deterministic."
aliases: ["active inference for context acquisition", "AIF-Context", "expected free energy minimization"]
sources: ["dutta-2026"]
---
# Active inference as context acquisition

> Score a candidate context action by how much it is expected to reduce
> decision-relevant uncertainty, not by whether it looks like a reasonable
> question.

## The bilevel objective (Dutta, Ramachandran & Sra, 2026)

An agent holds a belief $q_t(x)$ over a latent task state $x$ (intent,
missing constraint, best prompt). For a candidate action $a$ — a clarifying
question, a retrieval, a tool call, or acting now — an **inner** step forms
the posterior $q_t(x\mid o,a)$ that a hypothetical observation $o$ would
produce; an **outer** step scores $a$ by expected free energy $G_t(a)$,
summing an expected-risk term and an expected-KL-change-in-belief term, and
picks the action that minimizes it.[^c1]

Under an exact inner update, the KL term is exactly the [[mutual-information|mutual information]]
$I_{q_t}(x;o\mid a)$, and if the preference over observations $p^\star$ is
constant, minimizing $G_t$ is the same optimization as maximizing that
mutual information: $a^\star\in\arg\min_a G_t(a) \iff a^\star\in\arg\max_a
I_{q_t}(x;o\mid a)$ (Proposition 3.1).[^c2]

## The cost-weighted stopping rule (Proposition 3.3)

With cost $c(a)>0$ per action and a linear penalty $\lambda c(a)$, an
information-gathering action is worthwhile exactly when its information gain
exceeds its priced cost: $I_{q_t}(x;o\mid a) > \lambda c(a)$; among worthwhile
actions the best one maximizes $I_{q_t}(x;o\mid a) - \lambda c(a)$, i.e. a
budget spent greedily ranks actions by information gained per unit cost.[^c3]

## Bayes-risk value of context (Theorem 3.4)

For a terminal decision problem with Bayes risk $R(q)=\min_d
\mathbb{E}_{x\sim q}\ell(d,x)$, an action $a$ beats acting now exactly when
the expected risk reduction exceeds its cost: $R(q_t) -
\mathbb{E}_{o}[R(q_t(\cdot\mid o,a))] > \lambda c(a)$. When the terminal loss
is logarithmic, $R(q)=H(q)$ and the left side collapses to the same mutual
information $I_{q_t}(x;o\mid a)$.[^c4]

## Known as

| Field | Name there | Relation |
|---|---|---|
| Active inference / cognitive science (Friston et al. 2017; Parr & Friston 2019) | active inference | close — this note is the paper's one-step, deterministic-observation bilevel reduction, not the full generative-model neuroscience formalism (no proprioception, no hierarchical generative model) |
| This paper (Dutta, Ramachandran & Sra 2026) | AIF-Context / context acquisition | exact |

## Transfer

| | |
|---|---|
| **Home field** | Active inference (Friston et al. 2017): an agent minimizes expected free energy over a full generative model of states, observations, and policies, including an [[efe-planning-as-variational-inference|ambiguity]] term $H(o\mid x,a)$ |
| **Here** | An AI agent choosing among clarifying questions, retrievals, tool calls, and acting now, with a scalar token/latency cost per action |
| **What survives** | The bilevel structure (inner belief update, outer action score) and the exact reduction to expected-information-gain-per-cost under deterministic, noiseless observation models (Propositions 3.1, 3.3) |
| **What does not** | The ambiguity term $H(o\mid x,a)$, which the paper sets to zero for deterministic OQA — so the full active-inference decomposition is untested here; nor does the reduction hold once observations are noisy or the agent's own question changes what "the same $x$" means |

## Limits

- The equivalence to expected information gain (Proposition 3.1) requires an
  exact inner posterior and a **constant** preference $p^\star(o)$ over
  observations; with a non-constant preference the risk term does not drop
  out and $G_t$ diverges from pure information gain.
- Proposition 3.3's stopping rule is myopic (one-step lookahead), the same
  limit noted for [[expected-information-gain]] and [[value-of-information]].
- Theorem 3.4 generalizes [[value-of-information]] from a decision-specific
  loss to any Bayes risk, but the paper's own OQA instantiation only
  exercises the logarithmic-loss ([[entropy]]) special case — the general
  finite-loss form is stated, not benchmarked.
- All empirical validation is on the deterministic OQA benchmark and two
  token-budgeted prompting case studies; it does not test the framework
  against noisy or adversarial answers.

## Related

[[expected-information-gain]] · [[value-of-information]] · [[optimal-question-asking]] · [[mutual-information]] · [[bounded-rationality]]

[^c1]: dutta-2026 — "An outer step then chooses the action that minimizes expected free energy, including risk, epistemic value, and cost."
[^c2]: dutta-2026
[^c3]: dutta-2026 — "an information-gathering action is worthwhile exactly when Iqt ( x; o | a) > λc( a). (12) Among worthwhile actions, the optimal one maximizes Iqt ( x; o | a) − λc( a)."
[^c4]: dutta-2026
