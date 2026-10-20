---
description: "Ranks candidate diagnostic tests by summing graph-edge-derived feature value over the tests they verify, divided by 1 plus monetary cost times invasiveness."
aliases: ["Cost-Sensitive Action Planning", "test utility U(τ)", "GraphDx test selection"]
sources: ["arxiv-2607-15280"]
---
# Graph-edge-weighted test utility

> A discriminative-value proxy read off a knowledge graph's edge weights, spent on the test that returns the most of it per dollar.

## Definition / Mechanism

Tan et al. (2026)'s GraphDx scores the next diagnostic action in two steps, both computed
deterministically from a pre-built graph rather than from a neural
forward pass. First, every unobserved feature (symptom or sign) gets a
discriminative-value score restricted to the top-K current candidate
diseases D_top: the weighted sum, over those diseases, of the disease's
current confidence times the feature's typicality edge weight, plus a
variance term across candidates:

> "V (f) = Σ_{d∈Dtop} |S(d)| · |w(d, f)| + α · Var_{d∈Dtop}(w(d, f))"[^c1]

The first term favors a feature tied to high-confidence diseases; the
variance term favors a feature whose typicality differs sharply across
the candidates — a feature every candidate shares equally cannot
separate them. Second, every candidate test τ (which can verify one or
more features) gets a utility by summing the value of the features it
verifies, weighted by a discrete verification-effectiveness factor
η(f, τ), and dividing by one plus the product of the test's monetary
cost and an invasiveness multiplier:

> "U(τ) = [Σ_{f∈Verifies(τ)} V(f) · η(f, τ)] / (1 + cτ · ιτ)"[^c2]

The agent orders the test with the highest U(τ). The denominator is
additive-smoothed (the `+1`) so a free, non-invasive test is never
divided toward infinity, and an expensive or invasive one is
discounted rather than excluded outright. The authors present this as
a deliberately cheap substitute for full Bayesian value-of-information:
"While full Bayesian Value of Information (VoI) calculation is
computationally prohibitive for real-time interaction, we implement a
heuristic utility function that approximates information gain via
feature variance and relevance."[^c3]

The edge weights `w(d, f)` that feed V(f) are themselves not raw LLM
probabilities but a quantized typicality — each feature-disease pair is
bucketed by the extracting LLM into one of five discrete levels
(Hallmark, Common, Rare, Impossible, and their negatives), "acting as a
low-pass filter, stabilizing the reasoning process against minor
probability fluctuations in LLM generation." This quantization is what
makes V(f) and U(τ) deterministic and reproducible given a fixed graph,
in contrast to a neural agent re-deriving relevance from scratch each
turn.

## Why it matters

This is a concrete instance of turning "which test to order next" into
an arithmetic ranking that a symbolic engine, not the LLM, computes and
hands to the LLM as a constraint. Ordering by U(τ) rather than letting
an LLM decide directly is credited with suppressing "defensive
medicine" — ordering expensive tests to compensate for reasoning
uncertainty: "the average cost drops from \$1062 to \$537... attributed
to the utility-based active planning module, which effectively
suppresses the 'defensive medicine' behavior." Across two datasets
and three LLM backbones, replacing free-form LLM test ordering with
this scoring rule raised diagnostic success rates from 50–68% to
79–93% while cutting test costs 20–54%.[^c5]

## Limits

The scoring rule is a heuristic proxy for information gain, not a
calibrated one: it substitutes graph edge weight and cross-candidate
variance for a real information-theoretic quantity, and its accuracy
is bounded by how well the quantized typicality buckets approximate
true diagnostic likelihoods. It also depends entirely on the
underlying knowledge graph's coverage — the paper's own limitations
note that "the quality of MDKG is limited by the medical knowledge
reserve of the LLM used for graph construction... If the base model
has knowledge blind spots, the graph may miss key nodes or edges,"
which would silently miss both a discriminative feature and any test
that verifies it. The two hyperparameters (α weighting the variance
term, and the discrete η(f, τ) effectiveness levels) are not derived
from data; how they were set is not established in the extract
(unverified).

## Related

- [[value-of-information]] — the Bayesian ideal this utility is a cheap, deterministic proxy for.
- [[expected-information-gain]] — the information-theoretic quantity U(τ) approximates without computing it.
- [[candidate-anchored-rarity-policy]] — another catalogue/graph-weighted score for ranking the next diagnostic question, without the explicit cost-invasiveness denominator.
- [[exam-cost-reward]] — prices the same defensive-medicine problem through an RL reward instead of a deterministic ranking rule.

[^c1]: arxiv-2607-15280
[^c2]: arxiv-2607-15280
[^c3]: arxiv-2607-15280
[^c5]: arxiv-2607-15280 — "GraphDx improves diagnostic success rates from 50–68% to 79–93% while reducing test costs by 20–54%"
