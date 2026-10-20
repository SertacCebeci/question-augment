---
description: "Condensing a multi-turn interaction into one LLM-generated natural-language query, used as the retrieval query, outperforms updating an explicit Bayesian posterior over candidates turn by turn."
aliases: ["language posterior", "implicit posterior via re-retrieval"]
sources: ["chi-2024"]
---
# Language posterior

> Represent "what the system currently believes about the target" as a
> sentence, not a distribution — and re-retrieve with it, rather than
> updating a distribution with Bayes' rule.

## Definition / Mechanism

Chi, Lin, Lin & Klein (2024), building CLARINET (see
[[retrieval-conditioned-question-selection]]), compare two ways to fold a
clarification dialogue back into the retriever's belief state after each
answer. The **explicit posterior** updates a distribution over candidates
by Bayes' rule, $p_t(y\mid q_t,a_t)\propto p(q_t,a_t\mid y)\,p_{t-1}(y)$,
estimated per-candidate with a pretrained Flan-T5-base model. The
**language posterior** instead prompts a GPT-3 model to synthesize, from the
whole interaction history, a single natural-language description of what is
known about the target item, and re-runs the retriever with that sentence
as a fresh query — collapsing belief-state tracking into one re-retrieval
step rather than an explicit update rule.[^c1]

With question selection held fixed (random selection from the candidate
pool, in both arms), the language posterior gives significantly higher
retrieval performance than the explicit posterior; the explicit posterior's
MRR on the true item *decreases* with more questions asked, despite more
information nominally being available. The paper attributes this to
robustness: a single turn's answer is out-of-distribution for the retriever
and, under exact [[bayesian-estimation|Bayesian updating]], a misread or noisy answer has an
uncorrectable large effect on the whole distribution, whereas synthesizing a
new query each turn is less sensitive to any one turn's noise.[^c2]

## Why it matters

This is a negative result for the textbook move of maintaining an explicit
posterior over $W$ (stall 2's usual setup: score candidate questions against
a belief distribution and update it exactly). Here the exact update is the
*worse* mechanism empirically, because "exact" does not mean "well-behaved
under a noisy or partial per-turn answer" — the failure mode is the answer
being consumed by a component (a per-candidate likelihood model) that
amplifies its noise, not a flaw in Bayesian updating as such.

## Limits

- Demonstrated in one setting (book retrieval, random question selection
  held fixed in both arms) — the comparison isolates the posterior
  representation, not the interaction with a learned question-selection
  policy; whether the ranking would hold with a different question
  selector or a different retriever/likelihood-estimation pipeline is not
  tested.
- The explicit posterior's likelihood term is itself estimated with a
  pretrained Flan-T5-base model (an approximation of $p(a\mid q,y)$), so the
  comparison is between two approximate mechanisms, not between an exact
  Bayesian filter and a heuristic — the paper does not isolate whether the
  loss belongs to the exact-update *idea* or to this particular likelihood
  estimator.
- Qualitatively noted, not measured: over-representation of the (longer)
  initial query relative to later turn responses in the synthesized
  sentence, an asymmetry the authors flag as future work rather than fix.

## Related

[[retrieval-conditioned-question-selection]] · [[expected-information-gain]] · [[value-of-information]]

[^c1]: chi-2024
[^c2]: chi-2024
