---
description: "A drafted question's expected measurement error is predicted from its coded Saris & Gallhofer (2007) define two quantities for an item and then estimate them from the item's *form*: ```text reliabi…"
aliases: ["SQP", "predicted measurement quality"]
sources: ["saris-2007", "yan-2012"]
---
# Survey quality predictor

> A drafted question's expected measurement error is predicted from its coded
> formal characteristics alone, by a regression fitted over a meta-analysis of
> multitrait–multimethod experiments. It is the only check in its family
> that returns a number before anyone has been asked anything.

## Definition / Mechanism

Saris & Gallhofer (2007) define two quantities for an item and then estimate[^s1][^s2]
them from the item's *form*:

```text
reliability  = 1 - (random error variance / total variance)
quality      = proportion of observed variance explained by the latent
               construct      ( = reliability x validity )
```

Both are identified by the **multitrait–multimethod** design: measure several
traits by several methods, and decompose the observed correlations into true
score, method effect and random error. Saris & Gallhofer pooled such
experiments — 87 of them, the count as reported by yan-2012; the primary
source was not read — coded the questions in them on formal characteristics:
the formulation of the request, the number of response categories, whether the
categories are labelled, the range offered, the presence of a don't-know
branch, position in the instrument, mode — and regressed the MTMM estimates
on those codes. The fitted regression is the predictor: code a *new*
question's characteristics, get predicted [[calibration|reliability]], validity, method effect
and quality (yan-2012, reporting the program used in their study).

What this makes checkable at formulation time: **how much of the answer will
be the world and how much the instrument**, estimated from the question's
shape rather than from a trial run.

## Why it matters

1. It refutes the assumption that a finished question can only be evaluated
   by asking it. The predicted quantity is a variance decomposition, but the
   input is text and format codes.
2. The response format is part of the question. Most of the carrying
   characteristics are properties of the offered answer set, not of the stem —
   which is a statement about where measurement error was found to sit.
3. It gives a non-checklist form for a formulation check: a **fitted function
   from codeable features to expected error**, whose coefficients can be wrong
   and can be re-estimated, rather than a list of forbidden constructions
   whose warrant is consensus.
4. Its verdicts are not authoritative. In the only head-to-head comparison
   read here, SQP's predicted quality correlated $r = .608$ ($n = 15$,
   $p < .05$) with four experts' *badness* ratings — significant in the
   direction opposite to the one expected (yan-2012).

## Known as

| Field | Name there | Relation |
|---|---|---|
| Survey methodology | SQP / survey quality predictor | exact — the fitted prediction procedure this note is about, and the program distributing it |
| Survey methodology | predicted measurement quality | close — the quantity the procedure returns, named on its own; the procedure also returns predicted reliability, validity and method effect |
| Not this concept | MTMM | the experimental design the coefficients were fitted on, not a name for the predictor |
| Not this concept | question evaluation method ([[question-evaluation-method]]) | the family this is one member of |

## Transfer

| | |
|---|---|
| **In its home field** | closed-ended survey items with fixed response scales, put to hundreds of respondents; the predicted quantity is a variance decomposition identified only over a sample and only relative to a named trait |
| **Here** | one agent wording one question to one answerer, usually without a response scale, usually once |
| **What survives** | the form of the check — expected measurement error as a *learned* function of codeable features of wording and answer format, revisable against data; and the consequence that changing the offered answer set changes the question |
| **What does not** | the coefficients and the coding frame (fitted on scaled attitude and fact items; an open dialogue turn has no response scale to code), and the criterion itself — reliability and validity are defined over repeated administrations, which a one-shot ask does not have |

## Limits

- Quality is defined **relative to an assumed latent construct** the item is
  meant to measure. A question with no declared construct has no quality in
  this sense: the check presupposes that the axis (stall 1) and its selection
  (stall 2) are already settled, and says nothing about whether the right
  question is being asked.
- Saris & Gallhofer's book was not read directly for this note. Everything
  this note says about the predictor's basis — the meta-analysis of MTMM
  experiments, the definitions of reliability and quality, and the count of
  87 experiments — comes from yan-2012's account of the program they used.
  The count of 87 is **unconfirmed against the primary text** [?] and may not
  describe the version of the program in current use; nothing in the note's
  argument depends on its exact value, only on the basis being a fitted
  meta-analysis.
- One comparison against expert judgement, on 15 items, went the wrong way.
  That is evidence about the pair, not about which of the two is wrong — see
  [[question-evaluation-method]].
- Nothing in the predictor addresses presupposition, false premises, or
  suggestive wording ([[presupposition-accommodation]],
  [[false-premise-question]]). It scores the item as a *measuring
  instrument*, not the question as a *move*.

## Related

[[question-evaluation-method]] · [[survey-response-model]] · [[question-comprehension-scan]] · [[question-as-partition]] · [[calibration]]

[^s1]: saris-2007
[^s2]: yan-2012
