---
description: "Ranks candidate design-decision questions by mutual-information co-occurrence mined from a news corpus, filtered by domain-label Jaccard relevance, then asks only the top-k."
aliases: ["PrivacyAkinator prioritization", "co-occurrence-ranked question pool"]
sources: ["arxiv-2605-20206"]
---
# Corpus co-occurrence question ranking

> Which design decision to ask about next is decided offline, before the
> interview starts: by how often that decision co-occurs with others in a
> mined corpus, not by how much it would inform the current developer's
> system.

## Definition / Mechanism

Li et al. (2026)'s PrivacyAkinator keeps a pool of
candidate "design decisions" (key–value privacy choices) mined from 10K
privacy-related news articles. To score two decisions $D_1, D_2$ it computes a corpus-level
mutual-information statistic, $MI(D_1,D_2)=\log\frac{P(D_1\wedge D_2)\times
N}{P(D_1)\times P(D_2)}$, "where $P(D_1 \wedge D_2)$ is the probability of
the two decisions cooccurring, $P(D_1)$ and $P(D_2)$ are their individual
probabilities, and $N$ is the total number of data practices involved."[^c1]

Before scoring, the pool itself is filtered for relevance to the developer's
current node: domain labels are assigned to the current practice and to
every mined practice, and only candidates above a Jaccard-similarity cutoff
survive — "Only data practices with a similarity score above 0.4 are
retained."[^c2]

At each turn, every surviving candidate is ranked by its average
co-occurrence with the decisions already chosen, and only the head of the
list is expanded into a question: "PrivacyAkinator then uses the average
co-occurrence statistics with all prior design choices to rank all design
decisions in the pool. The hypothesis is that design decisions that
frequently co-occur in privacy news or literature are more likely to be
correlated and critical. At each step, PrivacyAkinator generates questions
for the top-$k$ decisions from the ranked list, as expanding too many
decisions would significantly increase computational cost." $k=3$ in the
reported setting.[^c3]

## Why it matters

The ranking never touches the developer's own uncertainty: it is a fixed
prior over which decisions *tend to* matter, computed once from an external
corpus, then reused (and narrowed by domain-relevance) across every session.
This is a cheap substitute for a per-session information-gain computation —
useful exactly when no likelihood model of the current unknown is available,
only a corpus of past co-occurrences. In the reported user study, developers
using the full tool (this ranking plus [[response-triggered-explore-exploit-switching|explore/exploit switching]] and structured
representation) "identified 47% more key decisions in 73% less time
compared to PRAM" — evidence for the pipeline as a whole, not isolated to
the ranking step.[^c4]

## Transfer

| | |
|---|---|
| **Home field** | Information theory / [[bayesian-experimental-design]]: $I(X;Y)$ between the unknown $X$ and a candidate answer $Y$, indexed by design and maximised to choose the next question. |
| **Here** | $MI$ between two *label categories* in a static mined corpus — a correlation prior over which decisions travel together, not an information-gain computation about this developer's system. |
| **What survives** | The log-ratio scoring form and the use of a ranked score to pick a bounded top-$k$ rather than all candidates. |
| **What does not** | Any epistemic reading — no unknown $X$, no answer $Y$, no update from the developer's actual response feeds back into the MI table itself; only averaging with prior *choices* shifts the ranking. |

## Limits

- The corpus is mined from privacy **news**, skewed toward "high-profile,
  media-reported incidents" and geographically toward the US and UK; the
  paper states this "could underrepresent privacy issues more prominent in
  other regions or regulatory environments" — the ranking inherits this
  bias directly, since rarity-in-corpus is conflated with irrelevance.
- $k=3$ and the 0.4 Jaccard cutoff are stated, not ablated in the extract
  read here — unverified whether the ranking's benefit is sensitive to
  either value.
- The 47%/73% result is measured on the whole tool; this note's mechanism
  is not evaluated in isolation.

## Related

[[ontology-guided-elicitation-agent]] · [[mutual-information]] · [[bayesian-experimental-design]] · [[response-triggered-explore-exploit-switching]] · [[expected-information-gain]]

[^c1]: arxiv-2605-20206 — "where P (D 1 ∧ D 2 ) is the probability of the two decisions cooccurring, P (D 1 ) and P (D 2 ) are their individual probabilities, and N is the total number of data practices involved."
[^c2]: arxiv-2605-20206 — "Only data practices with a similarity score above 0.4 are retained."
[^c3]: arxiv-2605-20206 — "PrivacyAkinator then uses the average co-occurrence statistics with all prior design choices to rank all design decisions in the pool. The hypothesis is that design decisions that frequently co-occur in privacy news or literature are more likely to be correlated and critical. At each step, PrivacyAkinator generates questions for the top-k decisions from the ranked list, as expanding too many decisions would significantly increase computational cost."
[^c4]: arxiv-2605-20206 — "developers using PrivacyAkinator identified 47% more key decisions in 73% less time compared to PRAM."
