---
description: "Yes/no search for one of $n$ known candidates against an answerer allowed at Rényi (1961) defined the two-player game: $A$ thinks of something, $B$ finds it by yes/no questions,"
aliases: ["Ulam's game", "liar game", "twenty questions with lies", "Ulam–Rényi game"]
sources: ["renyi-1961", "ulam-1976", "berlekamp-1964", "rivest-1980", "pelc-2002"]
---
# Rényi–Ulam problem

> Yes/no search for one of $n$ known candidates against an answerer allowed at
> most $\ell$ lies — what the lie budget costs in extra questions. Its reading
> as a model of an agent answering its own questions is this wiki's, not the
> literature's.

## Problem

Rényi (1961) defined the two-player game: $A$ thinks of something, $B$ finds it[^s1][^s2][^s3][^s4][^s5]
by yes/no questions, and a proportion of the answers is wrong. Ulam (1976,
*Adventures of a Mathematician*, p. 281) independently posed the fixed-budget
version — a number below one million, [[twenty-questions|twenty questions]], "now suppose one were
allowed to lie once or twice". Pelc's survey (2002) established the joint
attribution and the name; most of the literature before it says "Ulam's game".

The object of this note is the **fixed lie budget**: at most $\ell$ of the
answers are wrong, chosen adversarially, and the asker sees every prior answer.

## The result

For **comparison questions** ("is the unknown smaller than $a$?") over
$\{0,\dots,n-1\}$ with at most $\ell$ lies, Rivest, Meyer, Kleitman, Winklmann
and Spencer (1980) proved that the minimum worst-case length of the asker's
strategy is

$$\log_2 n + \ell\log_2\log_2 n + O(\ell\log \ell).$$

Noise enters as an **additive term, not a multiplicative factor**: the lie
budget buys back $\ell\log_2\log_2 n$ questions on top of the $\log_2 n$ that
noiseless search needs. For arbitrary yes/no questions the benchmark is
instead Berlekamp's counting ("volume") lower bound on how many answer
sequences can still identify a candidate; exact optimal lengths are known only
for small $\ell$ (Pelc 2002, §3).

## Berlekamp's connection

Berlekamp (1964 PhD thesis; published version in *Error-Correcting Codes*,
Wiley 1968) studied block coding for a binary symmetric channel with
**noiseless delayless feedback**. Pelc (2002, §1) states the equivalence in
both directions: a questioning strategy that always finds the object in at
most $n$ queries under $\le \ell$ errors *is* an adaptive $\ell$-error-correcting
code of length $n$, and conversely. Answers are the channel's bits, lies are
channel errors, and the asker's sight of prior answers is the feedback link.
Pelc records the boundary too: this equivalence holds for a fixed upper bound
on corrupted bits, and **fails** when the limitation is a per-bit error
probability.

## Known as

| Field | Name there | Match |
|---|---|---|
| Combinatorics / CS, most papers since the 1980s | Ulam's game, Ulam's problem | exact |
| Combinatorics, after Cicalese & Vaccaro (1998–99) | Rényi–Ulam game, Ulam–Rényi game | exact |
| Recreational / puzzle literature | twenty questions with lies | exact |
| Coding theory | adaptive $\ell$-error-correcting code (block coding with noiseless feedback) | close — the same optimisation stated over codes rather than over a game (Pelc 2002, §1) |

**Not this concept.** Rényi's 1961 formulation assumed a *probability* of
erroneous answers, not a bounded count; Pelc (2002, §5) surveys the
probabilistic branch — random errors, bounded error fraction, the linearly
bounded liar — as separate games with different optimal lengths. They are
different objects, not aliases of this one.

## Why it matters — and what this wiki infers

What the theorem gives the asker at stall 4 is a price list: over an
**enumerated** candidate set, an answerer with a **bounded adversarial** lie
budget is not a broken source, it is a source with a surcharge, and the
surcharge is additive.

**Conjecture (this wiki).** Nothing in Rényi–Ulam concerns language models.
This wiki's inference is that *if* an agent's self-answer errors were bounded
in number and non-systematic, and the candidate set enumerated, then wrong
self-answers would not collapse $|W| \to 1$; they would raise the question
count by an additive term, and the design consequence would be to budget a few
redundant re-asks rather than to stop self-answering. The antecedent is the
whole load: no lie budget $\ell$ is known for a model, and an answerer that
errs *systematically* — always drifting the same way — falls outside the model
entirely, where the theorem offers nothing.

## Transfer

| Row | |
|---|---|
| In its home field | combinatorial search / block coding with noiseless feedback: $n$ known candidates, yes–no or comparison questions, an adversary with at most $\ell$ lies, every prior answer visible to the asker |
| Here | an asker re-questioning an unreliable source — including an agent answering its own questions — over a candidate set it has written down |
| What survives | the shape of the cost: redundancy against bounded error is additive ($\ell\log_2\log_2 n$ beside $\log_2 n$), so unreliable answers are paid for with extra questions rather than a restart, and the lower bound says how much of that redundancy is unavoidable |
| What does not | the budget is an adversarial count fixed in advance, not a probability or a correlated drift — Pelc (2002) shows the coding equivalence itself fails under a per-bit error probability. With no known $\ell$, no enumerated $W$, and free-text answers that are not bits, the formula yields no question count here |

## Limits

- The quoted formula is Rivest et al. (1980) for **comparison questions** over
  an ordered set. It is not the general yes/no result, and quoting it as such
  overstates what is proved.
- It is asymptotic in $n$; the $O(\ell\log\ell)$ term hides what dominates at
  small $n$.
- Lies are bounded in number and adversarial; systematic error is outside the
  model, and this note claims nothing there.
- `berlekamp-1964` is **unverified** in this wiki (`[?]`) — the entry names
  Berlekamp's 1964 MIT thesis, while what is checked here is Pelc's (2002)
  citation of the published version and Pelc's own statement of the
  equivalence. Attribution to Berlekamp rests on that.
- The self-answering paragraph is this wiki's conjecture with no source; its
  precondition — a bounded, non-systematic error budget for a model — is
  unestablished, and [[semantic-entropy]] measures error rates, not budgets.

## Related

[[twenty-questions]] · [[channel-capacity]] · [[data-processing-inequality]] · [[semantic-entropy]] · [[generalized-binary-search]]

[^s1]: renyi-1961
[^s2]: ulam-1976
[^s3]: berlekamp-1964
[^s4]: rivest-1980
[^s5]: pelc-2002
