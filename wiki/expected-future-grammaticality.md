---
description: "The lookahead term that a schema-masked decoder silently replaces with a Let $P$ be the answerer's distribution over strings and $G$ the asker's grammar."
aliases: ["expected future grammaticality", "EFG"]
sources: ["park-2024"]
---
# Expected future grammaticality

> The lookahead term that a schema-masked decoder silently replaces with a
> yes/no test — and the reason the *rate* at which each admissible answer
> comes back is a property of the schema, not of the answerer.

## Definition / Mechanism

Let $P$ be the answerer's distribution over strings and $G$ the asker's[^s1]
grammar. The answer the asker believes it is getting is the conditional

$$Q^{P,G}(w) \;\propto\; P(w)\cdot \mathbb{1}[w \in L(G)].$$

Park, Wang, Berg-Kirkpatrick, Polikarpova & D'Antoni (NeurIPS 2024) write the
left-to-right factorisation of that conditional:

$$Q^{P,G}(w_i \mid w_{1:i-1}) \;\propto\; P(w_i \mid w_{1:i-1})\cdot c(w_{1:i}),$$

where $c(w_{1:i})$ — the **expected future grammaticality** of a prefix — is
the probability that a continuation sampled from $P$ out of that prefix ends
inside $L(G)$.

[[constrained-decoding]] does not compute $c$. It substitutes the indicator
$\mathbb{1}[w_{1:i} \in L_{\text{prefix}}(G)]$: every prefix that *could* be
completed grammatically is treated as equally likely to be. The two coincide
only when all live prefixes have equal expected future grammaticality, and in
general the masked sampler therefore "distorts the LLM's learned language
distribution" (Park et al. 2024). Their example: a model that ends a binary
string with 1 about 90% of the time, put under a grammar whose one
0-branch leads to a single low-probability string, ends with a 1 only about
30% of the time under masking — once a prefix is committed it cannot be
withdrawn.

Their algorithm ASAp (adaptive sampling with approximate expected futures)
reuses earlier samples to tighten an estimate $\tilde c$ of $c$. In the arXiv
version, Theorem 1 states that the estimate is a sound over-approximation,
$\tilde c_S(w_{1:i}) \ge c(w_{1:i})$, and Theorem 2 that as the number of
samples grows it converges in probability to $c$ on grammatical prefixes — so
the sampler converges to $Q^{P,G}$ while every sample stays grammatical.

## Known as

| Field | Name there | Relation |
|---|---|---|
| LLM decoding (Park et al. 2024) | expected future grammaticality, EFG | exact — the quantity $c(\cdot)$ defined above |
| LLM decoding (Park et al. 2024) | grammar-aligned decoding, GAD | **not this concept** — the name of the decoding *problem* (sample from $Q^{P,G}$); this note names the quantity that problem turns on |
| LLM decoding (Park et al. 2024) | ASAp | **not this concept** — one algorithm that estimates $c$; the identity above holds whatever estimates it |

## Transfer

| | |
|---|---|
| **In its home field** | Probability: sampling from $P$ conditioned on an event $A$. Rejection sampling does it exactly — draw, discard non-members — at expected cost $1/P(A)$. |
| **Here** | An answerer that must emit its reply left to right in one pass, where a prefix cannot be un-sampled, so the conditioning must be pushed into each step. |
| **What survives** | The identity: the exact conditional needs a lookahead factor, and any per-step filter without one defines a *different* distribution over the same admissible set. |
| **What does not** | The rejection-sampling guarantee, and with it any finite-time correctness. ASAp is an anytime over-approximation: before convergence its distribution is neither $P$ nor $Q^{P,G}$, and the authors report benchmarks where "even after 2,000 iterations the [[kl-divergence|KL divergence]] barely improves". |

## Why it matters

Stall 5 asks whether what came back is a constraint. What Park et al. establish
is about the distribution the masked decoder samples from: the *frequency* with
which a given cell of the asker's partition comes back is jointly determined by
the answerer and the shape of the grammar, and they measure that divergence from
$Q^{P,G}$ on grammars, not the behaviour of any downstream estimator.

— *this wiki's corollary*: any procedure that reads a distribution off repeated
constrained samples (majority voting, self-consistency, "the model said X in 8
of 10 runs", [[semantic-entropy]] computed over masked generations) is therefore
reading the grammar as well as the model, and its input is biased in a direction
the identity fixes and a magnitude nobody cited here has measured. The estimate
$c$ is also the first per-answer number in this wiki that quantifies how much the
instrument contributed; what to do with it is
[[constrained-answer-attribution]].

## Limits

- No cited work measures the size of the bias that masking induces in a
  sampled-uncertainty estimate (semantic entropy, self-consistency, majority
  voting). The *direction* follows from Park et al.'s identity — the sample
  frequencies are those of the masked sampler, not of $P$ conditioned on $G$ —
  but the magnitude is unmeasured, and whether it changes any such estimate's
  decision is an open question, not a finding of this note.
- The distortion is a claim about the *distribution*, not about accuracy. It
  matters only if the asker cares which admissible answer arrives and how
  often. Park et al. themselves report that correcting it "has no strong
  effect on solving downstream tasks" — evidence that the cost of the
  distortion is often invisible to a task metric.
- The whole account takes $P$ as the reference the asker wants. When the
  grammar encodes something the answerer does not know, moving mass toward the
  grammar is a gain, and "distortion" is the wrong word for it.
- The convergence is asymptotic and, on the authors' own benchmarks, slow;
  ASAp must also retain previous samples to update the estimate, so the
  correction has a memory cost that grows with sampling.
- The theorem numbers are those of the arXiv version of the paper.

## Related

[[constrained-decoding]] · [[structured-output]] · [[constrained-answer-attribution]] · [[semantic-entropy]] · [[surprisal]]

[^s1]: park-2024
