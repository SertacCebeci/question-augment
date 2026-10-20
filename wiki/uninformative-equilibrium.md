---
description: "[[gao-2014|Gao, Mao, Chen & Adams (2014)]] report — citing two results this wiki has not"
aliases: ["uninformative equilibria"]
sources: ["gao-2014"]
---
# Uninformative equilibrium

> Gao, Mao, Chen & Adams (2014) report — citing two results this wiki has not
> read [?] — that every score for an unverifiable answer has a second
> equilibrium in which answerers report the same thing whatever they saw. In
> their own controlled experiment that is the equilibrium the players found,
> and paying nothing produced more truth than any payment rule tested.

## Definition / Mechanism

In a peer-prediction game ([[peer-prediction]]) an **uninformative[^s1]
equilibrium** is a strategy profile in which each agent's report is independent
of its private signal — everyone always reports the same answer — which is a
Nash equilibrium of the very game whose truthful profile the mechanism was
designed to support. Gao, Mao, Chen & Adams (2014) report that such equilibria
are unavoidable in general, citing Jurca & Faltings (2009) and Waggoner & Chen
(2013).

**The experiment.** Gao et al., EC'14, 507–524: the first controlled online
experiment of a peer-prediction mechanism. Over 3000 unique Mechanical Turk
workers, each participating once, played the Jurca & Faltings (2009) mechanism
as a real-time, repeated, multiplayer game under a "trick or treat" cover story
that made the common-knowledge assumptions concrete; strategies were inferred
with a hidden Markov model. Five treatments (3–4 players, 20–30 rounds,
103–411 games each) varied only the payment rule, with a fixed prior
$\Pr(A)=0.5$, $\Pr(\text{MM}\mid A)=0.2$, $\Pr(\text{MM}\mid B)=0.7$.

| Treatment | Payment rule | What happened |
|---|---|---|
| 1 | uninformative "MM" profile pays the maximum $1.50 | a majority of games coordinated on it; with T2, more than 1/3 of all games converged to a symmetric uninformative equilibrium |
| 2 | symmetric — the two uninformative profiles pay the same | players coordinated on "GB" instead; exit surveys show the coordination was deliberate |
| 3 | 4-player rule with **no** symmetric uninformative equilibrium | fewer than 5% of games reached an asymmetric one — and **not a single game converged to the truthful equilibrium**, though 20% of players were truthful throughout; 11% of games reached the mixed-strategy equilibrium |
| 4 | uninformative profiles made to pay very little (0.15 vs 0.50 truthful) | under 2% of games reached "MM", none "GB", **no game reached the truthful equilibrium**; 16% of players truthful throughout; 26% adopted "MM" by the end |
| 5 | **no peer prediction** — a flat 0.90 per round | **two-thirds of players reported truthfully for the entire game**, with no incentive to do so |

The authors' conclusion: "a failure of peer prediction mechanisms in
incentivizing truthful reports… players are generally truthful in the absence
of economic incentives", and peer prediction "may be harmful in scenarios where
the cost of being truthful is similar to that of acting strategically".

## Known as

| Name | Field | Relation |
|---|---|---|
| uninformative equilibria | mechanism design | exact — the standard plural for the object |
| symmetric coordinating equilibrium | experimental economics | close — Gao et al.'s term for the symmetric members ("MM", "GB"); the asymmetric coordinating profiles ($x$MM$y$GB) are equally uninformative and are not symmetric, so the name covers a strictly narrower object than this note |
| babbling equilibrium | information economics | **not this concept** — the uninformative equilibrium of a cheap-talk *sending* game with no payments, where nothing is scored; see [[partition-equilibrium]] |
| collusion | mechanism design | **not this concept** — a colluding group can also coordinate on an *informative* lie; Jurca & Faltings's collusion-resistance is a different property |

## Why it matters

1. **It is the refutation the commitment stall needed.** Scoring an answerer's
   commitment against its peers is the one mechanism on Commitment that
   needs no resolution ([[bayesian-truth-serum]]). This is the only measurement
   of whether it works: in the two payment treatments with a reported
   per-player rate, 20% (T3) and 16% (T4) of players were truthful throughout
   against two-thirds in the unpaid control, and the authors read the four
   payment rules together as "a failure of peer prediction mechanisms in
   incentivizing truthful reports".
2. **"Truth is an equilibrium" is the wrong property to design for.** The
   experiment separates existence from focality: T3 and T4 removed or
   impoverished the uninformative equilibria and still produced zero truthful
   games. Deterring the bad equilibrium is not the same intervention as making
   the good one attractive — which is why the strongly-truthful family (truth
   pays *best* of all equilibria) is a different design point.
3. **The unpaid control beat every paid rule.** Two-thirds truthful under a
   flat payment against 16–20% under the mechanism gives a directly derivable
   rule: do not attach a peer score to an answer that is cheap to give
   honestly, because the score is what prompts the search for a strategy.
4. **The failure was inside the mechanism's own assumptions.** The cover story
   was written to make the common prior and conditional independence hold and
   was quiz-gated; participants demonstrably understood the prior — the exit
   surveys show they used it to pick which uninformative answer to coordinate
   on.

## Transfer

| | |
|---|---|
| **Home field** | a repeated, real-time game among 3–4 anonymous online workers with a small known prior, cash payments of $0.10–$1.50 per round, no communication, and a cost of honest reporting near zero |
| **Here** | an asker deciding whether to score an answerer's commitment against other answerers when the answer cannot be checked |
| **What survives** | the separation of *existence* from *focality* for a truthful equilibrium; the finding that removing the attractive coordination does not create truth; and the direction of the unpaid control's advantage |
| **What does not** | the magnitudes, which are specific to one mechanism (Jurca & Faltings 2009), one prior and 3–4 players; and the setting's near-zero cost of honesty — the authors explicitly leave open whether peer prediction works where truthful reporting is much costlier than acting strategically |

## Limits

- The claim above — that a peer score degrades commitment — rests on honest
  reporting being *cheap* in this task. The authors name that as the likely
  cause and say the mechanisms "may be better suited for scenarios where
  behaving truthfully is much more costly than acting strategically".
- Per-player truthfulness is reported for T3, T4 and the control only; T1 and
  T2 are reported as coordination on an uninformative profile, without a rate
  comparable to the control. The comparison in *Why it matters* is therefore
  two payment rules against one control, plus the authors' own reading of all
  four.
- One mechanism was tested, not the family: Jurca & Faltings (2009), with the
  prior known to the mechanism. [[bayesian-truth-serum]] and the multi-task
  mechanisms were not run, so this is evidence about the family's weakest
  property, not a measurement of each member.
- Fixed groups played repeatedly, so the repeated game has equilibria the
  one-shot stage game does not; the authors name this as a limit and propose
  re-matching players each round.
- Participants were US Mechanical Turk workers with >95% approval who passed a
  comprehension quiz and could enter once; 4% of games were excluded for
  disconnections.
- The general unavoidability of uninformative equilibria is *reported* by Gao
  et al. citing Jurca & Faltings (2009) and Waggoner & Chen (2013); neither
  primary has been read or verified by this wiki [?].

## Related

[[peer-prediction]] · [[bayesian-truth-serum]] · [[surprisingly-popular-algorithm]] · [[partition-equilibrium]] · [[preference-signal-against-asking]] · [[outcome-feedback]]

[^s1]: gao-2014
