---
description: "Score a candidate not by its distance from the truth — which is not For a problem with data $d$ and a candidate answer $\\tilde{x}$,"
aliases: ["backward error"]
sources: ["higham-2002", "oettli-1964", "rigal-1967", "wilkinson-1961"]
---
# Backward error

> Score a candidate not by its distance from the truth — which is not
> available — but by the smallest change to the *data* that would make the
> candidate exactly right. Computable from the record and the candidate
> alone; the truth never enters.

## Definition

For a problem with data $d$ and a candidate answer $\tilde{x}$, the[^s1][^s2][^s3][^s4]
**backward error** of $\tilde{x}$ is the size of the smallest perturbation
$\Delta d$ such that $\tilde{x}$ is the exact answer to the problem with data
$d + \Delta d$. The **forward error** is $\|\tilde{x} - x\|$ against the true
$x$; it needs $x$, the backward error does not.

Wilkinson (1961) established the stance for direct methods of matrix
inversion: rather than bound how far the computed inverse is from the true
one, show that the computed result is the exact result for a matrix within a
stated distance of the one given, and let that distance be the measure of
the computation. The two explicit formulas for linear systems, with residual
$r = b - A\tilde{x}$:

| Perturbation measured | Backward error of $\tilde{x}$ | Established by |
|---|---|---|
| normwise, $\|\Delta A\| \le \eta\|A\|$, $\|\Delta b\| \le \eta\|b\|$ | $\eta(\tilde{x}) = \dfrac{\|r\|}{\|A\|\,\|\tilde{x}\| + \|b\|}$ | Rigal & Gaches (1967) |
| componentwise, $|\Delta A| \le \omega E$, $|\Delta b| \le \omega f$ | $\omega(\tilde{x}) = \max_i \dfrac{|r_i|}{(E|\tilde{x}| + f)_i}$ | Oettli & Prager (1964) — `oettli-prager-theorem` (draft dropped) |

Both are the residual, normalised by the tolerance available at that
residual (Higham 2002, ch. 7, states both in this form). A candidate with
backward error $\le 1$ in the componentwise measure is the exact solution of
a system inside the stated tolerances: the data, as recorded, **cannot
distinguish it from the truth**.

The forward error is then bounded by the backward error times a
**condition number** of the problem — a property of the data $A$, not of
the candidate or the algorithm (Higham 2002, ch. 7). Small backward error
with a large forward error is the signature of an ill-conditioned problem,
not a bad answer.

## Known as

| Field | Name there | exact / close | Why |
|---|---|---|---|
| Numerical linear algebra | backward error | exact | the quantity defined above |
| Numerical linear algebra | normwise backward error; componentwise backward error | **not aliases** | two *instances* of the definition under two measures of perturbation size; the literature reports them as different numbers for the same candidate, and Higham gives them separate theorems |
| Numerical analysis | backward error analysis | **not this concept** | Wilkinson's method for analysing an *algorithm* — showing what it computes is exact for nearby data; the quantity here is what that analysis bounds |
| Numerical analysis | residual | **not this concept** | the raw $b - A\tilde{x}$; backward error is the residual divided by the tolerance available to absorb it |
| Numerical analysis | forward error | **not this concept** | the dual: distance to the truth, which needs the truth |

## Why it matters

Distillation already has acceptance tests that need no truth:
[[version-space]] accepts a hypothesis when it is consistent with every
example, [[backbone-of-a-formula]] fixes a literal when the formula alone
forces it, [[canonical-implication-basis]] is read off the incidence. Each
is **exact and binary** — a candidate is consistent or it is not, at zero
tolerance — and the tests that do grade candidates ($H \approx 0$, the MAP
world) need the truth or a declared relevance variable. Backward error is
the **graded, truth-free** form: a number, residual over the imprecision the
record itself declares, that consumes the tolerances the record carries and
needs neither the truth, nor a relevance variable, nor a hypothesis
language. Its $\le 1$ level is where the graded test recovers the binary
one — the candidate is exact for *some* record inside the tolerances, so the
record cannot distinguish it from the truth — and above 1 it says by how
much the record would have to move. The test is an inequality over the
record and the candidate, so it is checkable by the asker without a second
source.

The condition-number bound relocates a question. How much world-uncertainty
a given answer imprecision buys is fixed by the **question set**
($A$ — which directions the constraints pin down and which they leave nearly
free), not by the answers; an asker choosing questions is choosing that
conditioning. No source read here applies this to question selection; it is
logged as a gap.

## Transfer

| | |
|---|---|
| In its home field | a computed solution to a problem with numeric data, where the true solution is unknowable but the data are known to a stated precision, and algorithms are judged by the perturbation they are equivalent to |
| Here | a candidate world, or a distillate, judged against a record of accepted answers each carrying a declared tolerance |
| What survives | the reversal — evaluate in data space, where the tolerance is known, rather than in world space, where the truth is not; the residual-over-tolerance form of the score; and the separation of the candidate's fit (backward error) from the record's sensitivity (conditioning) |
| What does not | the closed forms: $\eta$ and $\omega$ are exact only for linear equations, and a nonlinear or categorical answer has no residual to normalise until a model of "how wrong" is declared; the norms and the entrywise tolerances, which nothing in an inquiry supplies; and the condition-number arithmetic, which needs $A$ written out |

## Limits

- The quantity is defined relative to a **declared measure of perturbation
  size** — normwise, componentwise, structured; different measures give
  different numbers for the same candidate, and the choice is the asker's.
- A small backward error certifies that the candidate is *indistinguishable*
  from the truth by the record; it does not certify that the record is
  adequate, and a record that pins nothing down gives every candidate a small
  backward error.
- The contrast with the map's exact tests holds only where the record
  carries tolerances: at zero tolerance the componentwise backward error is
  $0$ or $+\infty$ and the test collapses to the same consistent/inconsistent
  bit as version-space consistency, adding nothing.
- Wilkinson (1961) was read for its stance through its abstract and Higham's
  account; the formulas are cited to Rigal & Gaches (1967) and Oettli &
  Prager (1964) as Higham (2002) attributes them, and the condition-number
  bound is cited to Higham's chapter rather than to a numbered theorem.
- The analogy to [[metamorphic-probes]] — both evaluate a candidate without
  an oracle — is the wiki's: metamorphic relations test a *system* by
  relations between outputs, backward error tests a *candidate* by
  perturbation of inputs, and they share no formalism.

## Related

`oettli-prager-theorem` (draft dropped) · `noise-floor-of-w` (draft dropped) · [[metamorphic-probes]] · [[version-space]] · [[bayesian-estimation]]

[^s1]: higham-2002
[^s2]: oettli-1964
[^s3]: rigal-1967
[^s4]: wilkinson-1961
