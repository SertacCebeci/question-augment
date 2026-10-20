---
description: "[[entropy|Entropy]] is the floor under expected code length — and, through the **Assumptions**: source symbols drawn from a **known** distribution $p$ over a finite alphabet; a **binary,"
aliases: ["Shannon's first theorem", "noiseless coding theorem"]
sources: ["shannon-1948", "mcmillan-1956", "cover-2006"]
---
# Source coding theorem

> [[entropy|Entropy]] is the floor under expected code length — and, through the
> prefix-code reading of questioning, under the expected number of questions.

## Theorem (Shannon, 1948)

**Assumptions**: source symbols drawn from a **known** distribution $p$ over a[^s1][^s2][^s3]
finite alphabet; a **binary, uniquely decodable** code (a prefix code in the
usual construction); $L$ the **expected codeword length per symbol**.

$$H(X) \leq L < H(X) + 1 \qquad \text{bits per symbol}$$

- **The left inequality holds for every** uniquely decodable binary code of a
  known $p$. Kraft's inequality gives it for prefix codes; McMillan (1956,
  *IRE Trans. Inf. Theory* IT-2(4):115–116) showed the same inequality is
  implied by unique decipherability alone, so the floor cannot be evaded by
  dropping the prefix property (modern statement: Cover & Thomas 2006, ch. 5).
- **The right inequality is a construction, not a property of every lossless
  code.** Shannon–Fano lengths $\lceil \log_2 1/p_i \rceil$ attain it, and
  [[huffman-coding]] is optimal among prefix codes, hence at least as good. An
  arbitrary lossless code can be arbitrarily longer than $H+1$.
- The $+1$ is *per symbol*: coding blocks of $n$ symbols together brings it to
  $H + 1/n$. The gap is an artefact of symbol-by-symbol coding, not of the
  bound.

## Known as

| Field | Name there | Same thing? |
|---|---|---|
| Information theory | Shannon's first theorem | exact — the ordinal names this result against the channel coding theorem, Shannon's second |
| Information theory | noiseless coding theorem | exact — names the same statement by its assumption (a noiseless channel / lossless code) |

**Not this concept.** The *channel* coding theorem bounds rate against channel
capacity, a different quantity over a different object; and the lossy
counterpart (Shannon 1959) replaces the entropy floor with a rate–distortion
function — see [[rate-distortion-theory]].

## What this note contributes to question counting

The equivalence *strategy $=$ prefix code, expected question count $=$ expected
code length* is established in [[twenty-questions]] and is not restated here.
Shannon proves the **coding** statement; the reading below is this wiki's
inference from it, under the assumptions in `## Limits` (binary questions,
noiseless answers, arbitrary askable subsets, known prior):

$$\mathbb{E}[\#\text{questions}] \;\geq\; H(X) \qquad \text{(derived, not Shannon's statement)}$$

That is all this note carries into stall 7: a **floor**. If what is to be
pinned down carries 200 bits of entropy, no strategy of that kind averages
fewer than 200 binary questions. The achievability half is the other note's
business, and it needs both the distribution and the freedom to name any
subset.

## The arithmetic of the floor (illustrative)

The numbers here are chosen to show how the bound scales; **no source in this
note measures the entropy of any real inquiry.**

A choice among $k$ equally likely options carries $\log_2 k$ bits, and
independent choices add ([[chain-rule]]). So *if* a design carried fifty
independent 8-way choices, that is $50 \times 3 = 150$ bits, hence at least
150 binary questions on average.

The mechanism, not the number: the floor grows **linearly** in the count of
independent choices and only **logarithmically** in their arity, so arity is
the cheap dimension and independence is the expensive one. Dependence between
choices lowers $H$ and with it the floor; nothing lowers the cost below $H$.

## Crucial caveat — a floor is not a target

Reaching $H$ requires every answer to carry close to a full bit. If questions
repeat one another, $I(X;Y_i \mid Y_{<i}) \approx 0$: the count rises while the
entropy stalls. A large number of questions asked is therefore evidence of
nothing on its own — the bound constrains the *minimum*, and says nothing about
what any actual sequence achieves.

## Transfer

| | In its home field | Here |
|---|---|---|
| Source | symbols from a known distribution over a finite alphabet | the unknown to be pinned down, under a prior the asker does not know |
| Code | a binary uniquely decodable code; expected length per symbol | a sequence of yes/no questions; expected count |
| What survives | the floor $\mathbb{E}[\#\text{questions}] \geq H$, and the fact that redundant questions add count without lowering $H$ | |
| What does not | the $H+1$ half, which is a construction over a *known* $p$ with arbitrary askable subsets; the per-symbol blocking argument, since an inquiry is not a repeated draw; any concrete number | |

## Limits

- Everything above assumes binary, noiseless answers and a **known**
  distribution. Drop the known distribution and only the floor's *form*
  survives, since $H$ is then unmeasured; drop noiselessness and the floor
  itself changes ([[rate-distortion-theory]] and the noisy variants).
- Shannon's statement is about per-symbol coding of a source. Treating one
  inquiry as one draw from a known prior is an idealisation the theorem does
  not license; the note's question-count reading inherits that idealisation.
- The worked arithmetic is hypothetical. This wiki has no source counting
  independent decisions in any real design, so the floor is an argument form,
  not a measurement.

## Related

[[entropy]] · [[huffman-coding]] · [[twenty-questions]] · [[chain-rule]] · [[rate-distortion-theory]]

[^s1]: shannon-1948
[^s2]: mcmillan-1956
[^s3]: cover-2006
