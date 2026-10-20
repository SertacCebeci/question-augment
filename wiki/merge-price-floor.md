---
description: "**This wiki's inference, not a result.** A merge price is evidence of Three steps; the middle two are someone else's. **1."
aliases: ["merge price floor"]
sources: ["paninski-2003", "slonim-1999", "still-2004"]
---
# Merge price floor

> **This wiki's inference, not a result.** A merge price is evidence of
> structure only if it exceeds the amount by which the curve it is read from is
> inflated by sampling. Composing the two sources gives that amount a number —
> about $K_v/(2\ln 2\,N)$ bits per cluster, $\approx 0.09$ bits for forty
> answers coded against five decisions — and turns "look for a jump in the
> cost curve" into a threshold.

## The claim

Three steps; the middle two are someone else's.[^s1][^s2][^s3]

**1. The instrument as it stands has no stopping point.** Slonim & Tishby (1999) price each merge of [[agglomerative-information-bottleneck]] by the
exact information lost, $\delta I_y = I(Z_m;Y) - I(Z_{m-1};Y)$, and read a
*jump* in that per-step loss as the signal that a meaningful $m$ has been
passed — conditioning the reading on the curve being concave, which they state
they observed empirically and did not prove ("if this is always true").
Nothing in the method says how large a jump must be.

**2. The curve is inflated by a fixed amount per cluster.** Still & Bialek (2004) show that for a hard partition of $N$ observations with the relevance
variable binned into $K_v$ bins, the empirical curve carries a leading-order
sampling inflation of $K_v N_c / (2\ln 2\,N)$ bits, linear in the number of
clusters, and that subtracting it gives the curve an interior maximum
(`corrected-information-curve` (draft dropped)).

**3. Therefore (this wiki).** The first difference of that correction is a
**floor on the merge price**:

$$f \;=\; \frac{K_v}{2\ln 2\,N} \ \text{bits}.$$

A step whose price satisfies $\delta I_y < f$ buys less than the curve's own
sampling inflation; the partition above it is not distinguishable from the one
below on this evidence. The stated form of the rule is therefore: **run the
merges and keep the largest $m$ at which the price last rises above $f$** —
equivalently, the argmax over the AIB path of
$I(Z_m;Y) - \frac{K_v}{2\ln2\,N}m$. Only if the price sequence is
non-decreasing does this collapse into the cheaper "merge while
$\delta I_y < f$, stop at the first price above $f$"; that is Slonim &
Tishby's unproven concavity, not something the floor supplies. Report $f$
beside $m$ either way.

What it changes in a derived procedure. With $N = 40$ coded answers and
$K_v = 5$ decision categories, $f \approx 5/(2\ln2\cdot 40) \approx 0.09$ bits.
Every part the distillate keeps must earn 0.09 bits of decision-relevant
information; since the whole table holds at most $H(Y) \le \log_2 5 \approx
2.32$ bits, no more than about 25 parts could ever be justified even if the
empirical curve were exact — and it is not, so the real ceiling is lower.
Still & Bialek's own scaling ($N_c^\* \propto N^{2/3}$ below a few thousand
samples) points at single digits for a forty-answer record. The instruction
that follows is the opposite of the usual one: a small session does not licence
a long specification, and the number of distinct parts is fixed by the size of
the record before anyone reads the transcript.

**What would refute it.** Split one session's answers into halves, build a
table from each, run AIB on both. If merges priced below $f$ agree across the
halves as often as merges priced above it, the floor separates nothing and the
jump heuristic loses nothing by ignoring it.

## Known as

Not a term of art. "Merge price floor" is this wiki's name for the composition
of Slonim & Tishby's per-merge cost with Still & Bialek's per-cluster sampling
inflation; neither paper cites the other's quantity, and the phrase should not
be searched for. Its halves are [[agglomerative-information-bottleneck]] and
`corrected-information-curve` (draft dropped).

`corrected-information-curve` (draft dropped) is the `close` relation and not a second name
for this: $f$ is the first difference of that curve's correction and the two
select the same quantity — how many parts the record supports — by different
definitions. The corrected curve is *maximised over the optimal partition at
each $N_c$*; the floor is a *threshold read locally off one greedy hierarchy's
merge prices*, and the two coincide only when the greedy path is optimal and
the price sequence monotone. The note's structure — a cut displaced by the
uncertainty in the statistic being cut — is [[guarded-threshold]]'s, with the
offset here *derived* rather than declared.

## Transfer

| | |
|---|---|
| **In its home field** | two unrelated quantities: a pairwise merge cost computed on a corpus-sized count table, and a perturbative bias term for the optimal hard partition of $N$ i.i.d. binned observations |
| **Here** | both are read as bits on the same axis, so one becomes a threshold on the other |
| **What survives** | the units and the order of magnitude: $\delta I_y$ and $f$ are both bits of $I(Z;Y)$, both computed from the same $N$ and $K_v$, so the comparison is dimensionally sound and needs no new input |
| **What does not** | the optimality premise. Still & Bialek's inflation is computed for the *best* partition at each $N_c$; AIB's is greedy and provably suboptimal, so the two curves are not the same curve, and nothing in either paper licenses subtracting one's bias from the other's cost |

## Limits

- **This is a conjecture and is typed as one.** No source states it. Slonim &
  Tishby do not correct their curve; Still & Bialek do not run an
  agglomerative algorithm and use only synthetic data.
- **The single-crossing form of the rule assumes a non-decreasing price
  sequence** — Slonim & Tishby's unproven concavity (step 1). AIB selects the
  cheapest *available* pair at each step, and after a merge the recomputed
  pairwise costs can fall, so a price below $f$ may reappear after one above
  it. Where that happens "the first merge above $f$" is neither unique nor the
  argmax of the corrected curve, and only the last-crossing / argmax form
  above is defined. Whether crossings are in fact unique on real tables is
  untested here.
- **The premise mismatch in `## Transfer` is the load-bearing weakness**, not a
  caveat: if AIB's greedy curve is inflated differently from the optimal one,
  $f$ is the wrong number even where the rest of the reasoning holds.
- **The arithmetic example's inputs are invented.** $N = 40$, $K_v = 5$ are
  this note's illustration of a session, not a measured case; no transcript has
  been coded and run here. The $N^{2/3}$ extrapolation carries a constant
  fitted to one synthetic radial distribution and should be read as an order of
  magnitude at best.
- **It inherits the i.i.d. and fixed-binning conditions.** Answers in a session
  are dependent and the coding is chosen after reading the transcript, so $f$
  is a *best case* for the inflation — the same limit
  [[information-estimation-bias]] records for its own bounds.
- **It does not say which error costs more.** [[guarded-threshold]] would have
  the offset signed by the costlier failure; $f$ is symmetric and says nothing
  about whether an over-merged or an under-merged distillate is worse.
- It shares [[distillation-input-debt]]'s unpaid debt: $Y$ is still declared,
  and $K_v$ — the number of decision categories — is exactly the declaration
  whose completeness [[objectives-generation-deficit]] measures at about half.

## Related

[[agglomerative-information-bottleneck]] · `corrected-information-curve` (draft dropped) · [[guarded-threshold]] · [[distillation-input-debt]] · [[information-estimation-bias]] · `retained-information-fraction` (draft dropped)

[^s1]: paninski-2003
[^s2]: slonim-1999
[^s3]: still-2004
