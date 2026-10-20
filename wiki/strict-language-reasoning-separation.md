---
description: "Confine the LLM to parsing and verbalizing; a separate deterministic Bayesian module alone tracks the posterior, picks the next question by EIG, and sets the abstention threshold."
aliases: ["MoBayes", "strict separation", "language-reasoning decoupling"]
sources: ["arxiv-2604-20022"]
---
# Strict language–reasoning separation

> The LLM handles only language; a deterministic Bayesian module handles all probabilistic reasoning, question selection and abstention.

## Definition / Mechanism

A conversational decision-support system (introduced as MoBayes,
Kesmen et al. (2026)) is split into two components
that communicate only through structured evidence triples `(feature,
value, confidence)`: a **language module** (an LLM) that parses the
human's utterances into these triples and verbalizes whichever question
the other module chose, and a **reasoning module** — a deterministic,
non-neural statistical engine — that owns the posterior belief over
hypotheses, picks the next question, and decides when to stop or defer.
[^c1]

The reasoning module maintains a posterior over a fixed hypothesis set
and, at each turn, decides whether to terminate.
[^c2]

It queries the unasked feature of highest [[expected-information-gain]]
under a naive-Bayes factorisation, the standard myopic Bayes-optimal
policy, and commits or abstains once the posterior confidence crosses a
tunable threshold within a fixed turn budget.
[^c3]

The LLM never sees the posterior and cannot alter which question is
asked or when the system stops — the boundary is enforced by the
interface, not by instruction. Because the knowledge base (priors and
per-feature likelihoods) is external to the LLM's weights, adapting the
system to a new population is a data swap, not a fine-tune: the language
module is untouched and no case data is ever embedded in it.

## Why it matters

The separation is offered as an alternative to two failure modes: classical
structured CDS systems, which reason well but force clinicians into rigid,
pre-coded input, and end-to-end LLM diagnosticians, which converse fluently
but entangle question choice, stopping and diagnosis inside one generative
model with no formal posterior or calibrated abstention. A controlled
ablation isolates that the advantage is architectural rather than merely
informational: holding the knowledge source fixed — even eliciting it once
from the *same* frontier LLM that would otherwise reason turn-by-turn —
the version that reasons through the external Bayesian module still
outperforms the version where the LLM stays inside the decision loop.
[^c4]

The architectural origin of the advantage is confirmed in a control
setting where both systems draw their clinical knowledge from the same
frontier LLM, yet the separated system still wins — evidence that where
question-selection and stopping logic *live* (inside vs. outside the
language model) is itself a lever on performance, independent of what
the system knows.
[^c5]

## Limits

- Demonstrated only for a naive-Bayes factorisation over a closed,
  enumerable hypothesis set (diseases × discrete features); the paper
  notes richer factorisations (tree-augmented naive Bayes, noisy-OR,
  sum-product networks) "plug in without altering belief representation,
  EIG, or abstention" but at higher inference cost — this generalisation
  is not itself tested here.
- Closed-world: the system can only reach conclusions the knowledge base
  encodes, and it cannot exploit evidence the human volunteers outside the
  question actually asked — an ability an end-to-end LLM has by reading
  the whole conversation.
- Evaluated on simulated patients (LLM personas, PatientSim), not real
  clinical dialogue; how well the parser's structured-triple extraction
  holds up against messier real input is **unverified**.
- The EIG question-selection step itself is not novel (myopic Bayes-optimal
  feature choice is classical); the note's claim is about the modular
  boundary, not about a new selection rule.

## Related

- [[expected-information-gain]]
- [[bayesian-experimental-design]]
- [[compound-ai-systems]]
- [[gated-answerability-rule]]
- [[communication-policy]]

[^c1]: arxiv-2604-20022 — "We introduce MoBayes, a modular Bayesian framework that separates language from probabilistic reasoning. The LLM acts as a conversational interface, parsing patient interactions into structured observations and verbalizing questions selected by the Bayesian module."
[^c2]: arxiv-2604-20022
[^c3]: arxiv-2604-20022 — "At each turn the Bayesian module queries the unasked feature with the highest expected information gain (EIG), the standard myopic Bayes-optimal policy."
[^c4]: arxiv-2604-20022 — "Architectural attribution and selective control. Controlled comparisons with shared knowledge sources, including KBs elicited entirely from the same frontier LLM (§5.3), show that gains are architectural, not informational: the LLM is more usefully elicited once into a tabular KB and reasoned over by the Bayesian engine than invoked turn-by-turn as the reasoner."
[^c5]: arxiv-2604-20022 — "The architectural origin of the advantage is supported by control setting in which M O BAYES and the standalone doctor draw clinical knowledge from the same frontier LLM, yet M O BAYES still outperforms the standalone system."
