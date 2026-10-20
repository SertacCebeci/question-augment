---
description: "Query by committee filters a random input stream by asking only where two sampled hypotheses disagree; positive information gain per query implies exponentially falling prediction error."
aliases: ["QBC", "selective sampling", "committee-based sampling"]
sources: ["freund-1997"]
---
# Query by committee

Query by committee (QBC) is a filter over a stream of candidate questions. Hypotheses are drawn from those still consistent with the answers so far, forming a small committee. The learner asks the oracle for a label only on inputs where the committee members disagree. The work describes it as "a method for filtering informative queries from a random stream of inputs".[^c1] Agreement means the answer is already implied, so the query is skipped. Disagreement marks a question whose answer would remove some of the remaining hypotheses.

## What is proved

The result is conditional. If the two-member committee algorithm achieves information gain with a positive lower bound, then "the prediction error decreases exponentially with the number of queries".[^c2] The information gain is the quantity in [[expected-information-gain]], measured on the space of hypotheses. A guaranteed floor on the gain per asked question therefore gives a rate that passive random sampling does not give. The abstract states that this exponential decrease holds for query learning of perceptrons.[^c3]

The mechanism, in my own reading of the abstract (not a quoted claim): the committee's disagreement is a cheap stand-in for expected information gain. The learner never computes the gain. It only compares two samples from its current belief, which is a sampling version of [[bayesian-experimental-design]].

## Limits

- The text available here is only the abstract and reference list of the paper. The algorithm's details, the proof, and the size of the rate constants were not read, so none of them are asserted here.
- The guarantee depends on the gain lower bound holding. The abstract proves it for perceptrons only. Other hypothesis classes are not covered by what was read.
- The setting is label queries to a noiseless oracle about inputs in a stream. Whether the idea carries over to open-ended natural-language clarification questions is untested here.
- The reference list includes "Query learning can work poorly when a human oracle is used" (Baum and Lang). I only know the title, so I do not claim what it found.

## Related

- [[expected-information-gain]] — the quantity whose positive lower bound drives the exponential rate
- [[bayesian-experimental-design]] — the classical framing that selective sampling approximates
- [[mutual-information]] — the information-theoretic form of the gain per query

[^c1]: freund-1997 — "a method for filtering informative queries from a random stream of inputs"
[^c2]: freund-1997 — "the prediction error decreases exponentially with the number of queries"
[^c3]: freund-1997 — "this exponential decrease holds for query learning of perceptrons"
