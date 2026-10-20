---
description: "One name for a mechanism and for the family it started. The members differ on The rows are estimators of one quantity — the mutual information between an answerer's report and a peer's — under diff…"
aliases: ["peer prediction", "peer prediction mechanism", "information elicitation without verification", "elicitation without ground truth"]
sources: ["dasgupta-2013", "gao-2014", "miller-2005", "prelec-2004", "prelec-2017", "shnayder-2016", "witkowski-2012"]
---
# Peer prediction

> One name for a mechanism and for the family it started. The members differ on
> what the scorer must know, on how many answerers the theorem needs, and on
> whether truth merely *is* an equilibrium or is the best-paying one — and each
> of those decides whether an asker can use it at all.

## The name and what it covers

| Object | The rule | What the scorer must know | The truthfulness property | Member note |
|---|---|---|---|---|
| **The peer-prediction method** (Miller, Resnick & Zeckhauser 2005) | score one agent's signal report with a proper scoring rule applied to the posterior it implies over a *reference* agent's report | the common prior **and** the conditional signal distributions — known to the mechanism | honest reporting is a Nash equilibrium; incentive compatible for any $n \ge 2$ | none yet — queued; the variant with a language model in the prior's seat is [[generative-peer-prediction]] |
| **Bayesian truth serum** (Prelec 2004) | information report + prediction report; pay for answers more common than collectively predicted | nothing — the prior is shared by the agents but need not be known to the mechanism | strictly Bayes–Nash IC as $n \to \infty$; provably fails at $n = 3$ | [[bayesian-truth-serum]] |
| **Robust BTS** (Witkowski & Parkes 2012) | shadow-posterior report built from a reference agent, scored by the binary quadratic rule | nothing about the prior | strict IC for every $n \ge 3$ and *ex post* individually rational; binary signals only | none yet — queued |
| **Multi-task mechanisms** (Dasgupta & Ghosh 2013; Shnayder, Agarwal, Frongillo & Parkes 2016) | reward agreement with a reference agent across *many* tasks, minus a statistic that cancels blind agreement | nothing; the needed correlations are estimated from the reports themselves | *strongly truthful* / *informed truthful* — no strategy profile pays more than truth, and truth strictly beats every uninformed strategy | [[correlated-agreement]] |
| **Surprisingly popular** (Prelec, Seung & McCoy 2017) | take the answer whose endorsement exceeds its predicted endorsement | nothing | **not an incentive property at all** — an aggregation rule with no payments, measured by accuracy | [[surprisingly-popular-algorithm]] |

The rows are estimators of one quantity — the [[mutual-information|mutual information]] between an[^s1][^s2][^s3][^s4][^s5][^s6][^s7]
answerer's report and a peer's — under different budgets; that reading is
Kong & Schoenebeck's and is the object of [[mutual-information-paradigm]].

## The differences are measured, not verbal

Four quantities separate the rows, and each is reported by the papers
themselves rather than inferred here:

- **The smallest population for which the theorem holds** — $n \ge 2$ for the
  2005 method, $n \to \infty$ for BTS, $n \ge 3$ for RBTS. Witkowski & Parkes
  (2012) prove BTS is neither incentive compatible nor interim individually
  rational at $n = 3$; in their example truth earns $-0.450$ where a misreport
  earns $+0.298$. Reading the five rows against a three-answerer panel — this
  note's own tally, not a claim from any cited paper — the BTS row is provably
  out at that size; the RBTS row is the only one with a theorem *at* $n = 3$;
  the 2005 method has a theorem from $n \ge 2$ but is blocked instead by its
  prior requirement; and the remaining two rows are not indexed by $n$ at all,
  the multi-task mechanisms being indexed by number of tasks and the
  surprisingly popular rule carrying no incentive theorem at any $n$.
- **What the scorer must know.** The 2005 method requires the mechanism to hold
  the prior and the conditional signal distributions; the later members do not.
  This is the difference between a mechanism an asker can deploy on a novel
  question and one it cannot.
- **One task or many.** BTS and the 2005 method score a single question; the
  multi-task mechanisms need each answerer to answer many, and buy their
  stronger property with that.
- **Whether truth is *an* equilibrium or the *best-paying* one.** This is not a
  refinement: it is the axis the only controlled experiment on the family turned
  on. Gao et al. (2014) found the truthful equilibrium was never focal, and that
  making the uninformative equilibria unattractive still produced zero truthful
  games — see [[uninformative-equilibrium]].

Filing these as one concept would let an asker inherit RBTS's small-$n$
guarantee while running BTS's formula, or read the multi-task family's
strong truthfulness into a single-question score. The bare name licenses
exactly that substitution.

## Known as

| Name | Field | Relation |
|---|---|---|
| peer prediction | mechanism design | ambiguous — Witkowski & Parkes (2012) use it on one page both for "the *peer prediction method* (Miller, Resnick, and Zeckhauser 2005)" and for "the first peer prediction mechanism that does not rely on knowledge of the common prior" |
| peer prediction mechanism | mechanism design | ambiguous in the same way, and one step worse — it reads as a singular object while naming either the 2005 method (row 1) or any member of the family; a claim carrying this name resolves to a definite mechanism only when the source's $n$ and prior requirement are given with it |
| information elicitation without verification | mechanism design | close — the unambiguous name for the *family*; it names the problem rather than any rule, and excludes nothing that belongs |
| elicitation without ground truth | mechanism design | close — Shnayder et al.'s (2016) phrasing of the same problem, "settings without any objective ground truth against which to score reports"; names the family by what is missing rather than by what is done, and is the phrase under which the family reaches Source |
| output agreement | human computation | **not this concept** — paying two agents for matching answers (the ESP game) has no correction for blind agreement, which is the term the multi-task mechanisms subtract |
| proper scoring rule | statistics, forecasting | **not this concept** — the ingredient several members apply to an *implied posterior*; propriety is a property of a rule scored against a realised outcome, and the whole family exists because no outcome is realised |

## Limits

- **The partition above is this wiki's reading**, assembled from five papers;
  no cited source offers a taxonomy of the name. If the reading is wrong, the
  four measured differences still stand — they are each reported by their own
  paper.
- The three-answerer tally in the first bullet is this note's arithmetic over
  the table, and it inherits the table's provenance: it is only as good as the
  rows drawn from abstracts.
- Only three rows now rest on works read in full here (BTS via Witkowski &
  Parkes 2012, the SP algorithm, and the multi-task row via Shnayder et al.
  2016). The Miller/Resnick/Zeckhauser and Dasgupta/Ghosh rows rest on those
  papers' abstracts and on later papers' restatements; their exact conditions
  are not stated here and their theorem numbers are deliberately not cited.
- The table lists mechanisms, not deployments. Whether any of them elicits
  truth from a real answerer is a separate question with one data point
  ([[uninformative-equilibrium]]), and that data point is about a sixth
  mechanism (Jurca & Faltings 2009) not listed above.

## Related

[[bayesian-truth-serum]] · [[surprisingly-popular-algorithm]] · [[uninformative-equilibrium]] · [[mutual-information-paradigm]] · [[correlated-agreement]] · Commitment

[^s1]: dasgupta-2013
[^s2]: gao-2014
[^s3]: miller-2005
[^s4]: prelec-2004
[^s5]: prelec-2017
[^s6]: shnayder-2016
[^s7]: witkowski-2012
