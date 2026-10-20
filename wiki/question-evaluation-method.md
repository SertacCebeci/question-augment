---
description: "One name, seven instruments. Run on the same drafted questions they rank The first four run **before anyone is asked anything**; the last three need an administration. That split,"
aliases: ["question evaluation", "questionnaire pretesting", "question appraisal"]
sources: ["graesser-2006", "presser-1994", "saris-2007", "yan-2012"]
---
# Question evaluation method

> One name, seven instruments. Run on the same drafted questions they rank
> them differently, and two of the significant correlations between them run
> the *wrong* way — so "the question was checked" does not say what was
> checked.

## The name and what it covers

| Instrument | What it reads | What it needs | Member note |
|---|---|---|---|
| **Expert review** | judgements of questionnaire-design specialists on a draft | a panel, or individual reviewers | none yet |
| **Formal appraisal** (QAS-99, Willis & Lessler 1999) | 26 yes/no checks under 8 headings — reading, instructions, clarity, assumptions, knowledge/memory, sensitivity/bias, response categories, other — applied per question | a coder trained on the form | none yet |
| **Automated comprehension scan** (QUAID) | computational-linguistic features of the question text | nothing but the text | [[question-comprehension-scan]] |
| **Predicted quality** (SQP) | coded formal characteristics, through a fitted regression | the coding | [[survey-quality-predictor]] |
| **Cognitive interview** | respondents' verbalisations while answering the draft | respondents | none yet |
| **Behaviour coding** | coded interviewer/respondent behaviour in a live administration | a fielded survey | none yet |
| **Latent-class error rate** | statistical misclassification from three indicators of one construct | many respondents, several items | none yet |

The first four run **before anyone is asked anything**; the last three need an[^s1][^s2][^s3][^s4]
administration. That split, not the family name, is what an agent choosing a
check has to decide on.

## The differences are measured, not verbal

Yan, Kreuter & Tourangeau (2012) ran five of these on the same 15 items (five
triplets measuring one construct each, with one member of every triplet
deliberately written worse). Correlations across the 15 items, their Table 5:

```text
expert rating   vs LCA misclassification      r =  .526 *   agreement
cognitive int.  vs validity coefficient       r = -.560 *   agreement
cognitive int.  vs validity ratio             r = -.715 *   agreement
LCA             vs cognitive interview        r = -.570 *   WRONG SIGN
expert rating   vs SQP predicted quality      r =  .608 *   WRONG SIGN
                                              (* p < .05, n = 15)
```

The last two are significant *and* opposite to the direction the authors
expected: the items experts rated worse were the ones SQP predicted better.
Only the cognitive interviews caught the deliberately damaged item in the
first triplet, and no method caught it in the second.

**Within** a method the agreement is not higher. Pairwise correlations among
three cognitive interviewers' problem rates ran .143 to .326; the median
correlation among the four experts was .360. On the *kind* of problem found,
the methods agreed on recall problems (r = .86) and not at all on
comprehension (−.09) or judgment/reporting (−.33). Presser & Blair (1994) had
already found the methods differed in which problems they found and how
consistently they repeated across trials of the same method.

Rothgeb, Willis & Forsyth (2005) separated the instrument from the
organisation running it: 83 items, three techniques × three organisations in
a balanced design. Mean problem score per item (0–3): expert review 1.55,
QAS 2.93, cognitive interviews 1.46. The QAS flagged a problem on 97.7% of
its opportunities — so nearly every item failed it, and the ceiling left its
scores with too little variance to correlate with anything. Expert review
against cognitive interviewing correlated .27 (p < .02). Across
organisations, item scores correlated .34–.38 and kappas averaged about .3.

The conclusion Yan et al. draw: until it is known which method yields valid
results, it is unwise to rely on any one of them.

## Known as

| Field | Name there | Relation |
|---|---|---|
| Survey methodology | question evaluation method | exact — the family name |
| Survey methodology | questionnaire pretesting | close — pretesting names *when* it is done and includes the workflow this note excludes, while question evaluation names the instrument; three members here need a live administration rather than a pre-field trial. Kept in `aliases` as the field's loose usage, not as identity |
| Not this concept | item-writing guidelines ([[item-writing-guidelines]]) | rules for *producing* a question, not a procedure for appraising a finished one |
| Not this concept | question quality | the predicted or estimated quantity, not the instrument that produces it |

## Limits

- The inventory lists the instruments the three cited comparison studies
  actually ran. The family is at least this large, not exactly seven.
- The divergence claim rests mainly on one study with n = 15 items drawn from
  two non-probability web panels; correlations on 15 points are wide, and
  Yan et al. present them as indications, not estimates.
- The disagreement measured is disagreement in **rank order within a triplet
  of items measuring one construct**. No study cited here establishes which
  instrument is right — two of the five compared ([[calibration|reliability]], validity) are
  themselves members of the family being compared, so there is no external
  criterion in it.
- Every member is defined over standardised items with fixed response formats
  put to many respondents. Three of the seven cannot run at all on one
  question asked once, so the family is not a menu this wiki can pick from
  freely; only the first four survive the setting.
- The QAS-99 manual (`willis-1999`) was not read directly; the description of
  its 8 headings and 26 checks follows Rothgeb et al.'s account of the form
  they administered.
- This note holds the bare name. It does not say that a check is worthless —
  it says an unnamed check is uninterpretable.

## Related

[[question-comprehension-scan]] · [[survey-quality-predictor]] · [[item-writing-guidelines]] · [[survey-response-model]] · [[ambiguity-taxonomy]] · [[roc-curve]]

[^s1]: graesser-2006
[^s2]: presser-1994
[^s3]: saris-2007
[^s4]: yan-2012
