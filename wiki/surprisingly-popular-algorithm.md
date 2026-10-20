---
description: "Ask each answerer two things — its answer, and what it expects everyone else Prelec, Seung & McCoy (2017), *Nature* 541, 532–535."
aliases: ["SP algorithm", "surprisingly popular voting"]
sources: ["prelec-2017"]
---
# The surprisingly popular algorithm

> Ask each answerer two things — its answer, and what it expects everyone else
> to answer — then take the answer that beats its predicted popularity. Not the
> majority, and provably not the most confident.

## Definition / Mechanism

Prelec, Seung & McCoy (2017), *Nature* 541, 532–535. Each respondent gives a[^s1]
vote and a **prediction of the distribution of votes**. The algorithm selects
the answer whose actual endorsement most exceeds its average predicted
endorsement — "select the answer that is more popular than people predict"
(p. 532). No payments are made; this is a selection rule, not an incentive
scheme.

The mechanism behind it (their Fig. 2): a Bayesian respondent's prediction of
others interpolates between the actual world and the counterfactual one, since
the respondent does not know which world is actual. Predictions therefore
*under-forecast* the answer that holds in the actual world, and the residual —
actual minus predicted — points at it. In their worked example, a large panel
asked "Is Philadelphia the capital of Pennsylvania?" gives a wrong majority
"yes" whose actual frequency falls short of what respondents predicted, while
"no" is surprisingly popular and correct.

Three results are stated in the paper's Supplementary Information and described
in the main text (p. 532):

- **Theorem 1** — a general impossibility: no algorithm based on votes and
  confidences can be correct even for ideal Bayesian respondents. The main text
  gives the counterexample: two biased-coin problems with *identical*
  distributions of votes and confidences and opposite correct answers.
- **Theorem 2** — the SP algorithm "always selects the best answer in light of
  available evidence".
- **Theorem 3** — the extension to multiple choice, and the use of vote
  predictions to identify the respondents placing highest probability on the
  correct answer.

**Measured.** 490 dichotomous items across four content types: three studies of
50 US state-capital questions, one of 80 general-knowledge questions, one of 80
skin-lesion images diagnosed by professional dermatologists, and two of 90
20th-century artworks priced by art professionals and by laypeople. Across all
490 items SP reduced errors by **21.3%** relative to simple majority vote
($P<0.0005$, two-sided matched-pair sign test); on the 290 items where
confidence was also measured, by **35.8%** relative to majority vote
($P<0.001$), **24.2%** relative to confidence-weighted vote ($P=0.0107$) and
**22.2%** relative to taking the answer with the highest average confidence
($P<0.13$). On the state-capital studies SP cut incorrect decisions by 48%; on
the general-knowledge study (the only one run on Mechanical Turk) by 14%
($P=0.031$). In the art domain, where the majority is too conservative, SP
lowers the vote share needed for an "expensive" verdict from 50% to about 25%
and matches the discrimination of the best individual judges.

## Known as

| Name | Field | Relation |
|---|---|---|
| SP algorithm | collective intelligence | exact — the paper's own abbreviation for this rule |
| surprisingly popular voting | computational social choice | close — the same actual-minus-predicted criterion, but studied there as a voting rule over full rankings rather than the dichotomous selection this note defines; no source in `sources:` covers that literature, so identity is not claimed |
| surprisingly popular answer | collective intelligence | **not this concept** — the algorithm's *output* on one question, not the rule |
| meta-prediction / second-order report | forecasting, experimental economics | **not this concept** — the input the rule consumes; the same input feeds [[bayesian-truth-serum]], which scores it instead of aggregating it |
| wisdom of crowds | collective intelligence | **not this concept** — the family of aggregation claims this paper is a counterexample within |

## Why it matters

1. **It refutes confidence as the commitment channel, at the best case.**
   Theorem 1 is about *ideal Bayesian* respondents: the failure of
   confidence-weighted aggregation is not human sloppiness that better
   [[calibration]] would fix. If the asker will pool several answers, asking
   "how sure are you?" is provably not enough and asking "what will others
   say?" is.
2. **The extra question is cheap and needs no resolution.** Like
   [[bayesian-truth-serum]] it runs on a proposition that may never be
   settled — unlike a prediction market, which needs an event to resolve. The
   authors name exactly this as the widening of the application range (p. 534).
3. **It inverts how agreement is read.** [[novice-expert-problem]] treats
   agreement among sources as weak evidence needing an independence check; here
   shared common knowledge is precisely what *biases* the majority ("base rate
   information is factored in repeatedly, once for each respondent", p. 533),
   and the diagnostic quantity is the gap between actual and predicted
   agreement.
4. **It comes with its own detection of when it will not help.** Where the
   predicted vote splits cluster near the actual ones, SP cannot overturn the
   majority — the authors attribute the weak 14% result in Study 2 to 81% of
   its items having predicted splits in the 40–60% interval.

## Transfer

| | |
|---|---|
| **Home field** | dozens of independent human respondents, one discrete-answer question, a common prior and [[bayesian-estimation|Bayesian updating]] on private signals, no payments, answers scored afterwards against a known truth for the purpose of evaluation only |
| **Here** | an asker holding several answers to one question it cannot check, needing to choose one |
| **What survives** | the two-report format; the criterion (actual minus predicted endorsement); and the impossibility result about confidence, which is a statement about the best case and therefore binds any weaker respondent too |
| **What does not** | the guarantee — the authors state the theorems "are theoretical and do not guarantee success in practice, as actual respondents will fall short of ideal" (p. 534); the effect sizes, measured on general knowledge, dermatology and art pricing with panels of dozens; and the independence of respondents, since $N$ samples from one model are not $N$ respondents ([[tree-search-methods]]) |

## Limits

- The claim that a second-order report beats a confidence report rests on
  having a **population** of answerers whose predictions of one another carry
  information. With one answerer there is no surprisingly popular answer at
  all, and this note supplies nothing for that case.
- This note defines the rule for a **single dichotomous choice** (with the
  multiple-choice extension of Theorem 3). Any extension of the criterion
  beyond that — to full rankings, as the phrase "surprisingly popular voting"
  is used in computational social choice — is uncited here and outside what
  the note's claims cover.
- The three theorems live in the Supplementary Information, which this note has
  not read; they are cited as described in the main text (p. 532), and the
  numbering is the paper's own.
- The 22.2% advantage over max-confidence voting is reported at $P<0.13$ and is
  not significant at the .05 level.
- The authors' own simulation bounds the power: with individuals correct 75% of
  the time and majority voting at 86%, 50 problems and $n=30$ respondents give
  SP a significant advantage in only 40% of simulated studies. A small panel
  will usually not show the effect even where it exists.
- SP is not manipulation-proof: the authors note a respondent can favour an
  option by submitting a dishonest low vote prediction for it, and point at
  [[bayesian-truth-serum]] for the incentive layer.
- The whole method is bounded by the respondents' evidence: "if the available
  evidence is incomplete or misleading, the answer that best fits the evidence
  may be incorrect" (p. 534).

## Related

[[bayesian-truth-serum]] · [[peer-prediction]] · [[novice-expert-problem]] · [[calibration]] · [[tree-search-methods]] · [[uninformative-equilibrium]]

[^s1]: prelec-2017
