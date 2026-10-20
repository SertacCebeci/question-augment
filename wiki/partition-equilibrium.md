---
description: "When the answerer's interest differs from the asker's, the *finest* answer Crawford & Sobel (1982), *Econometrica* 50(6), 1431–1451."
aliases: ["Crawford–Sobel partition equilibrium", "interval equilibrium", "cheap-talk partition equilibrium", "N(b) bound"]
sources: ["crawford-1982", "kono-2021"]
---
# Partition equilibrium

> When the answerer's interest differs from the asker's, the *finest* answer
> that can be given is capped by that difference — before any question about
> the answerer's evidence is asked.

## Definition / Mechanism

Crawford & Sobel (1982), *Econometrica* 50(6), 1431–1451. A Sender observes[^s1][^s2]
a state $m \in [0,1]$ with density $f$ and sends a **costless** message; a
Receiver hears it and takes an action $y$. Utilities $U^S(y,m,b)$ and
$U^R(y,m)$; the scalar $b$ measures how far the Sender's preferred action sits
from the Receiver's. Nothing is verifiable and lying is free.

**Lemma 1 (p. 1436).** If the Sender's ideal action differs from the
Receiver's at every state, the set of actions induced in equilibrium is
**finite** and its elements are separated by some $\epsilon > 0$.

**Theorem 1 (p. 1437).** Every equilibrium is essentially a **partition
equilibrium**: $[0,1]$ is cut at $0 = a_0 < \dots < a_N = 1$ and the Sender
reports only which interval contains $m$. Boundaries satisfy an *arbitrage
condition* — the type sitting on a boundary is exactly indifferent between the
two actions its two neighbouring messages induce. There is a positive integer
$N(b)$ — the paper's notation for the ceiling on the number of cells — such
that an equilibrium of every size $1 \le N \le N(b)$ exists, and **no
equilibrium has more than $N(b)$ cells**.

**Corollary 1 (p. 1440).** Under a stated condition on preferences, $N(b) = 1$:
the only equilibrium is the uninformative one.

**The worked example (pp. 1440–41)**, $f$ uniform on $[0,1]$,
$U^S = -(y - (m+b))^2$, $U^R = -(y-m)^2$:

```text
N(b) = largest integer i with  2 i (i-1) b < 1
cell widths     a_i - a_{i-1} = 1/N + 2b(2i - N - 1)      (eq. 24)
b = 1/20   ->   N(b) = 3, cells [0, 2/15], (2/15, 7/15], (7/15, 1]
b > 1/4    ->   N(b) = 1, only the uninformative equilibrium survives
sigma^2_m = the expected residual variance of the state m given the
            equilibrium message — the loss the partition's own coarseness
            imposes, not the prior variance of m; it is zero only if the
            message reveals m exactly
ex ante         EU^R = -sigma^2_m ,  EU^S = -(sigma^2_m + b^2)
```

Since the Receiver acts on $E[m \mid \text{message}]$, its whole loss is that
residual variance; the Sender bears the same term plus the constant $b^2$ it
can never remove by talking.

## Known as

| Name | Field | Relation |
|---|---|---|
| Crawford–Sobel partition equilibrium | information economics | exact |
| interval equilibrium | information economics, political economy | exact — the cells are intervals of the state |
| $N(b)$ bound | information economics | close — the paper's notation for the *cardinality ceiling*, one component of Theorem 1; the equilibrium object is the interval form together with the bound, so this name is not identity |
| babbling equilibrium | information economics | **not this concept** — it is the $N = 1$ member of the family, always present; the family is not named after it |
| cheap talk | information economics | **not this concept** — the class of games with costless unverifiable messages; partition equilibrium is one result about one such game |
| strategic information transmission | information economics | **not this concept** — the research programme the 1982 paper opened |

## Why it matters

1. **A ceiling that exists before the evidence question.** The Sender in the
   example knows $m$ *exactly* and still cannot deliver more than $N(b)$
   distinguishable answers. Every other row of Commitment treats how
   far to commit as a function of what the answerer knows and how well it is
   scored; this one supplies a bound that is a function of misalignment alone.
2. **"I don't know" is an equilibrium, not a failure.** Above $b = 1/4$ in the
   example the uninformative message is the *only* thing the Sender can send
   that the Receiver will read correctly. An answerer refusing to commit is
   therefore not always a defect to be repaired — [[abstention]] would still
   price it, but here the price does not change the outcome.
3. **The ceiling is steep, so buying granularity is expensive.**
   $2N(N-1)b < 1$ makes $N$ grow roughly as $b^{-1/2}$: halving the
   misalignment buys about $\sqrt 2$ more cells, not twice as many. A
   commitment scale finer than a handful of levels needs near-alignment.
4. **Precision is not uniform over the [[possible-worlds|state space]].** Eq. 24 makes cell width
   increase linearly in $i$ when $b > 0$: the answer is finest at one end of
   the range and coarsest at the other. A commitment vocabulary with
   equally-spaced levels ([[verbal-probability-expressions]]) does not match
   the shape the equilibrium has.
5. **Truthfulness is unenforceable, not unwanted.** Crawford & Sobel note
   (p. 1444) that a commitment to tell the truth would raise the Sender's ex
   ante utility from $-(b^2 + \sigma_m^2)$ to $-b^2$. The gain is exactly
   $\sigma_m^2$, the residual variance the coarse partition imposes — positive
   whenever the equilibrium is not fully revealing, which under $b > 0$ it
   never is. So the Sender itself prefers the commitment ex ante, and cannot
   make it inside the game, because the Receiver knows the incentive to lie.
   The remedy this points at is a commitment device, not persuasion or
   instruction.

## Transfer

| | |
|---|---|
| **Home field** | a one-shot two-player Bayesian game; scalar state on $[0,1]$; costless, unverifiable messages with an unbounded message space; both utilities and the bias $b$ common knowledge; a Receiver who acts on rational expectations |
| **Here** | an answerer choosing how finely to commit to an asker whose use of the answer it does not fully share |
| **What survives** | the *form* — a credible commitment scale is a finite set of cells, not a continuum; the existence of an upper bound on the number of cells fixed by misalignment rather than by what the answerer knows; the always-available uninformative option; and the ex ante preference of *both* sides for the finest available scheme |
| **What does not** | the numbers — $2N(N-1)b<1$ and the $b>1/4$ collapse hold only under a uniform prior, quadratic losses and a scalar state. Nor does common knowledge of $b$: an asker who cannot name the answerer's bias is not the Receiver of this model, and no source cited here measures $b$ for any real answerer. Nor does the equilibrium's self-enforcement, which requires the Receiver to decode a coarse message *correctly* rather than take a hedge at face value |

## Limits

- The load-bearing claim above — that a misalignment ceiling constrains
  commitment — rests on the answerer's bias being a **stable preference
  parameter known to the asker**. If $b$ is unknown or unstable, the
  equilibrium concept does not apply as stated and the computed bound is not
  the operative one.
- Theorem 1 gives an upper bound, **not a prediction**: equilibria of every
  size from 1 to $N(b)$ exist simultaneously and the model selects none.
  Crawford & Sobel argue for the $N(b)$ equilibrium by focal-point and ex ante
  Pareto arguments in Sections 4–5; that is a selection argument, not part of
  the theorem.
- The $\sigma_m^2$ in bullet 5 is the residual variance *of the equilibrium
  being compared against*; the size of the gain from a commitment device is
  therefore not a constant but depends on which of the $N(b)$ equilibria is
  played, and the note cannot say which.
- The proof of Theorem 1 in the 1982 paper contains incorrect statements. Kono & Kandori (2021) give a counterexample to a step and a corrected proof; the
  theorem itself stands.
- The $N(b)=3$ at $b=1/20$ and the $b>1/4$ collapse are the Section 4 example,
  not general results.
- Messages here are costless. An answerer whose wrong answers are punished is
  in a different game, and nothing in this note covers it.

## Related

[[abstention]] · [[calibration-training]] · [[sycophantic-capitulation]] · [[question-as-partition]] · [[constraint-as-information]] · [[verbal-probability-expressions]]

[^s1]: crawford-1982
[^s2]: kono-2021
