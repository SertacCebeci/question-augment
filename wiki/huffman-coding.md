---
description: "The construction that provably orders a fixed set of alternatives by Take the two lowest-probability symbols, merge them into one node of summed probability, repeat until one node remains;"
aliases: ["Huffman code", "minimum-redundancy code", "optimal prefix code"]
sources: ["huffman-1952", "shannon-1948"]
---
# Huffman coding

> The construction that provably orders a fixed set of alternatives by
> probability. Its ordering logic transfers to question order; its optimality
> does not.

## Algorithm (Huffman, 1952)

Take the two lowest-probability symbols, merge them into one node of summed[^s1][^s2]
probability, repeat until one node remains; the tree read root-to-leaf gives
the codewords. Huffman (1952, *Proc. IRE* 40(9):1098–1101) proved this
construction **minimises expected code length among all prefix codes** for
symbol-by-symbol coding of a known distribution. A lemma of the same proof is
the ordering fact used below: in an optimal code, $p_i > p_j$ implies
$\ell_i \le \ell_j$ — **the heavier symbol never gets the longer codeword**.

The [[entropy]] bracket is Shannon's (1948), not Huffman's:

$$H(X) \leq L_{\text{Huffman}} < H(X)+1$$

The lower bound is the [[source-coding-theorem]]; the upper follows because
Huffman is no worse than the Shannon–Fano code with lengths
$\lceil \log_2 1/p_i \rceil$.

## Known as

| Field | Name there | Same thing? |
|---|---|---|
| Information theory | Huffman code | exact — the tree this algorithm outputs |
| Information theory | minimum-redundancy code | exact — Huffman's own term in the 1952 title |
| Coding theory | optimal prefix code | close — the class of length-minimising prefix codes; Huffman's output is one member, and optimal codes are not unique |

## [[twenty-questions]] correspondence

Each branch of the tree is a binary question, each leaf an answer, and the
average depth is the expected number of questions.

## Ordering: what the theorem says, and what it does not

Huffman's rule is **shortest path to the heaviest mass** — sort by
probability, not by balance. This is *not* the same criterion as
[[generalized-binary-search]], which picks the test splitting the remaining
probability mass most **evenly**. The two coincide only in the uniform case;
under a skewed prior Huffman spends its first branch separating the single
heaviest world, while an even split would cut the mass in half. Any
prescription for question order has to choose between them.

*Inference of this wiki, not Huffman's result:* if a questioner's prior over
$W$ is fixed and skewed, the Huffman ordering says to spend early questions on
the heaviest region rather than on the most balanced cut. This wiki has no
source establishing that this carries to live inquiry, where the prior is not
fixed.

## But Huffman is offline

Huffman knows the whole distribution in advance. In a live inquiry the
distribution changes as answers arrive — so the live counterpart is
[[optimal-decision-tree]] and its greedy approximation.

## Transfer

| | In its home field | Here |
|---|---|---|
| Object | a symbol drawn from a known, fixed distribution over a finite alphabet | a world in $W$ under a prior |
| Structure | a codeword; expected code length in bits | a question sequence; expected number of questions |
| What survives | heavier mass gets the shorter path, and tree depth reads directly as question count | |
| What does not | the optimality proof — the inquiry distribution is unknown and shifts as answers arrive; the within-one-bit guarantee; and the assumption that answers are binary and error-free | |

## Limits

- The optimality claim above holds only under Huffman's own conditions: a
  known, fixed distribution, a finite alphabet, symbol-by-symbol prefix
  coding. Outside them nothing in this note is proved.
- Within one bit of $H$ per symbol; that gap is not tight when symbols can be
  blocked together.
- "Heaviest mass first" maps probability to importance. Those differ: a rare
  decision can carry the whole design ([[value-of-information]]).

## Related

[[twenty-questions]] · [[source-coding-theorem]] · [[optimal-decision-tree]] · [[generalized-binary-search]] · [[value-of-information]]

[^s1]: huffman-1952
[^s2]: shannon-1948
