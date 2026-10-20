---
description: "The canonical form of the question-asking problem. The bridge between Bob picks an object from a finite set according to a distribution $\\mu$ that both players know;"
aliases: ["20 questions", "prefix-code equivalence"]
sources: ["shannon-1948", "huffman-1952", "dagan-2017", "filmus-2021"]
---
# Twenty questions

> The canonical form of the question-asking problem. The bridge between
> [[entropy]] and question count.

## The game

Bob picks an object from a finite set according to a distribution $\mu$ that[^s1][^s2][^s3][^s4]
both players know; Alice identifies it with yes/no questions, each of which may
name an **arbitrary** subset. Alice minimises the expected number of questions.

## Core result

Alice's strategy is equivalent to a **prefix code**: the codeword of an object
is the sequence of answers along its root-to-leaf path, so expected question
count *is* expected code length. Two named results then apply verbatim to the
game — this correspondence is the stated premise of the modern literature on it
(Dagan, Filmus, Gabizon & Moran 2017 §1; Filmus & Mehalel 2021 §1):

- **Shannon (1948)**, the source coding theorem, gives the bracket
  $$H(\mu) \leq \mathbb{E}[\#\text{questions}] < H(\mu) + 1$$
  — the lower bound unbeatable, the upper achievable. Carrier:
  [[source-coding-theorem]].
- **Huffman (1952)** gives the optimum inside that bracket: his construction
  yields the minimum-expected-length prefix code for a known $\mu$, hence the
  optimal strategy. Carrier: [[huffman-coding]].

Question count and entropy are therefore the same quantity to within one
question — under the assumptions in `## Limits`, not outside them.

## Known as

| Field | Name there | Same thing? |
|---|---|---|
| Recreational / combinatorial search | 20 questions | exact — the same game; the version here is the distributional one, with $\mu$ given |
| Information theory | prefix-code equivalence | close — names the theorem this note states (strategies $\leftrightarrow$ prefix codes), not the game it is stated about |

**Not this concept.** *Bisection search* / binary search is a strategy over an
**ordered** domain that halves the index range; its guarantee is
$\lceil \log_2 n \rceil$ questions in the worst case whatever $\mu$ is, while
the object here is expected cost under a known $\mu$, whose optimum is
Huffman's tree — not balanced when $\mu$ is skewed. Different definition,
different measured quantity: see [[optimal-decision-tree]] and
[[generalized-binary-search]].

## The shape of a good question

Every question should split the probability mass **in half**:

```text
Good question:  P(yes) ≈ 0.5   →  1 bit gained
Bad question:   P(yes) ≈ 0.95  →  0.29 bits gained
```

*Inference of this wiki, not part of the theorem:* this wiki reads the
*constraint-seeking vs hypothesis-scanning* distinction ([[constraint-seeking]],
which comes from developmental work on children's questioning, not from coding
theory) as the same rule seen from cognitive science. "X or Y?" splits the
[[possible-worlds|hypothesis space]]; "Is it B?" tests one hypothesis, and if $P(B)$ is small it
teaches almost nothing.

The caveat is the same either way: if $P(B)$ is already near $0.5$, asking
directly is optimal. The rule is not "ask constraint-seeking questions" but
**"split the mass"**.

## Restricted question sets

What if Alice may use only questions from a fixed set $\mathcal{Q}$ of subsets?

- **Dagan, Filmus, Gabizon & Moran (2017)**: comparison ("$x < c$?") and
  equality ("$x = c$?") queries alone come within a small additive constant of
  the Huffman optimum, and a set of $O(r\,n^{1/r})$ questions attains expected
  cost at most $H(\mu) + r$. The price of restriction is redundancy, and it is
  a function of the set's **size**.
- **Filmus & Mehalel (2021)** quantify the size that preserves *exact*
  optimality for every $\mu$. With $q(n)$ the smallest such set over $n$
  objects, their Theorem 1.1 gives $q(n) = 2^{-G(\beta)n \pm o(n)}$ for
  $n = \beta \cdot 2^k$, $\beta \in [1,2)$, with $2^{-G(\beta)} < 1.25$ for
  $\beta \neq 1.25$ — refining Dagan et al.'s $1.25^{n+o(n)}$, and generalised
  to $d$-ary questions.

So the result is not that "the optimum drifts away from $H+1$": exact
optimality for all $\mu$ costs an exponential but sub-$2^n$ question set, and
accepting $r$ extra questions buys a polynomially small one.

*Inference of this wiki, not a result of either paper:* the questions askable
in a natural language are a restricted set of a different kind — not chosen for
optimality, not closed under complement or intersection, and not indexed by
size. No bound above applies to it, so the $r$ a real interrogative repertoire
pays is unknown. That an inquiry needs far more questions than the entropy of
what it settles is *consistent* with restriction, but neither paper licenses a
number.

## Transfer

| | In its home field | Here |
|---|---|---|
| Question | an arbitrary subset of the object set | one natural-language interrogative, which can denote only some partitions of $W$ ([[question-as-partition]]) |
| $\mu$ | known to both players, fixed | unknown, estimated by the asker, shifting as answers arrive |
| What survives | the count $\geq H(\mu)$, and "split the mass" as the local rule for choosing the next question | |
| What does not | the $H+1$ achievability, the optimality of Huffman, and any concrete question count, once the askable set is restricted | |

## Limits

- Binary, noiseless, arbitrary-subset questions over a **known** $\mu$. Drop
  any one of the three and only the $H$ lower bound survives.
- Reading "split the mass" as the constraint-seeking rule is this wiki's
  inference, not Shannon's or Huffman's result: the work behind
  [[constraint-seeking]] classifies question types, it does not measure bits.
- The natural-language paragraph above is this wiki's extrapolation. Dagan et
  al. and Filmus & Mehalel bound cost against the **size** of a permitted
  question set, never against its expressibility, and no source here measures
  the askable set of a language.
- "Split the mass in half" needs the mass to be estimable — see
  [[calibration]].

## Related

[[entropy]] · [[huffman-coding]] · [[source-coding-theorem]] · [[optimal-decision-tree]] · [[constraint-seeking]] · [[renyi-ulam-problem]]

[^s1]: shannon-1948
[^s2]: huffman-1952
[^s3]: dagan-2017
[^s4]: filmus-2021
