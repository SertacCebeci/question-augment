---
description: "Second-hop retrieval candidates are scored jointly with the bridge passage the first hop found, s(q,b,c) not s(q,c), so source choice is conditioned on prior evidence."
aliases: ["BridgeRAG", "bridge conditioning", "tripartite judge", "s(q,b,c) scoring"]
sources: ["arxiv-2604-03384"]
---
# Bridge-conditioned retrieval

> The passage the second hop needs is not a property of the query alone —
> it is a property of what the first hop already found.

## Definition / Mechanism

Bacellar (2026) treats multi-hop question answering as
a two-stage source problem: a first-hop passage $b$ (the "bridge") resolves
an intermediate entity, and the second-hop passage $c$ is the one that
answers the question given that entity. Standard dense retrievers score
every candidate by $s(q,c)$, a function of the query alone. BridgeRAG
replaces this with $s(q,b,c)$: after retrieving the top-1 hop-1 passage as
$b$ by cosine similarity, every second-hop candidate is scored jointly
against the query and the bridge by an LLM ("tripartite judge"), rather
than against the query in isolation.[^c2]

The pipeline keeps two objectives separate. *Coverage* is built without the
judge: an LLM extracts $N{=}3$ subject-verb-object queries and two key
entities from $b$, each independently retrieved by nearest-neighbour search
and unioned into a pool of up to 20 candidates. *Ranking* then scores every
pool candidate with $s(q,b,c)$ and fuses the judge score with the
query-similarity score by mapping both to percentile ranks before a convex
combination — so a Gaussian-distributed cosine score and a categorical LLM
score become commensurable before they are combined. The paper formalizes
when conditioning should matter with a chain-disambiguation gap
$\Delta(q,b^*,c) = \mathrm{sim}(q,c) - \mathrm{sim}(q \oplus b^*, c)$:
on *bridge-comparison* queries $\Delta<0$ (the gold second-hop passage is
underranked by the query alone and needs the bridge to surface); on
*single-chain* queries $\Delta \approx 0$ (the query alone already suffices,
and conditioning should not help or hurt).

## Why it matters

The gap predicts a selective, not uniform, effect, and the paper measures
exactly that: bridge conditioning produces a 18.7% top-1 flip-win rate on
parallel-chain queries against 0.6% on single-chain queries, not merely more
churn. Separately, coverage and scoring are shown to be independent
levers: the entity-grounded expansion widens the candidate pool on its own,
while the judge improves ranking over any fixed pool. The general point
for source selection is that routing a request to "who or what is asked
next" can be conditioned on what an earlier step in the same request already
established, not only on the request's original wording — the two do not
have to be scored the same way.

## Limits

The information-theoretic framing the paper uses to motivate selectivity —
entropy of the second-hop gold given the query, mutual information between
gold and bridge — is offered explicitly as "a motivating lens rather than a
formal derived result"; it is not proved, and its predictions hold at the
level of query subtype, not reliably at the whole-dataset level (the
bridge-comparison effect reaches significance on 2WikiMultiHopQA but not on
MuSiQue, p=0.21). The mechanism is also not free of inference cost despite
being "training-free": each query costs three LLM calls (entity extraction,
SVO generation, tripartite judging) and six nearest-neighbour searches, so
the source is still chosen by consulting a model, not by a lookup. Every
experiment is a two-hop, entity-bridged factoid benchmark (MuSiQue,
2WikiMultiHopQA, HotpotQA); whether bridge conditioning transfers to bridges
that are not named entities, or to chains longer than two hops, is
unverified.

## Related

[[retrieval-conditioned-question-selection]], [[constraint-as-information]],
[[value-of-information]], [[self-ask-decomposition]]

[^c2]: arxiv-2604-03384 — "the correct scoring target for second-hop retrieval: relevance of a candidate is not a property of the query alone but of (q, b, c), where"
