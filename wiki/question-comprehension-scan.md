---
description: "A computational scan of the question text alone returns flagged problem Graesser, Wiemer-Hastings, Kreuz, Wiemer-Hastings & Marquis (2000) built QUAID; Graesser, Cai,"
aliases: ["QUAID", "Question Understanding Aid"]
sources: ["graesser-2000", "graesser-2006", "yan-2012"]
---
# Question comprehension scan

> A computational scan of the question text alone returns flagged problem
> classes — and the flagging threshold is reported to have been chosen to
> maximise agreement with human language experts. If that is so, "the
> detector works" means an operating point against a declared criterion, not
> a precision against a truth.

## Definition / Mechanism

Graesser, Wiemer-Hastings, Kreuz, Wiemer-Hastings & Marquis (2000) built[^s1][^s2][^s3]
QUAID; Graesser, Cai, Louwerse & Daniel (2006) published it as a web
facility. The user enters the question, any accompanying context and the
answer alternatives; the system returns flags. Five classes are reported (of
nine the design targets):

```text
unfamiliar technical term        word the respondent will not know
vague or imprecise relative term "often", "usually", "large"
ambiguous noun phrase            referent not fixed
complex syntax                   parse load
working-memory overload          too much to hold while answering
```

The modules are computational-linguistic — lexical frequency and familiarity
norms, part-of-speech and syntactic analysis, counts over the question's
structure — not a hand-maintained list of banned constructions.

**How the flag threshold was set.** The full text of graesser-2000 is
reported to describe varying candidate thresholds and taking the value that
maximises the correlation with language experts' ratings of whether a given
question contains that problem. That full text was not read for this note and
the procedure is carried here as unverified (see Limits). What the abstract
does report is the scan's performance *against the expert corpus*: hit rate,
false-alarm rate, d′, recall and precision. On either reading the detector is
scored relative to a human criterion rather than against a ground truth about
respondents.

## Why it matters

1. The fork-marker list this wiki proposes in [[ambiguity-taxonomy]] —
   ambiguous pronouns, quantifiers, underspecified verbs, baseless
   comparatives, hedges — is the same kind of object, and QUAID is its
   measured precedent: a surface scan from question text to problem classes,
   needing no answerer and no trial run.
2. It shows what an "operational check" of that kind delivers — and this
   point is **this note's inference, not a finding in the sources**. QUAID
   does report hit rate, false-alarm rate, d′, recall and precision; every
   one of them is scored against the language-expert corpus. Nothing in the
   sources read here scores a flag against measured respondent behaviour, and
   the reading that no such labelling was available is this wiki's, not the
   authors'. The consequence, if it holds, is that the criterion is part of
   the check: a flag means "the experts would likely call this a problem",
   not "the respondent will mis-answer".
3. The ceiling is the criterion's own [[calibration|reliability]]. In Yan, Kreuter & Tourangeau (2012) the median correlation between the four
   questionnaire-design experts on item quality was .360, and agreement among
   the compared methods on the *kind* of problem found was r = .86 for
   recall problems, −.09 for comprehension and −.33 for judgment/reporting —
   comprehension, the class this scan is fitted to, being the one on which
   the methods agree least.
4. Its five classes are properties of the text alone, so it covers the
   comprehension stage of [[survey-response-model]] and nothing else. Whether
   a question is leading, or carries a false premise, is out of its range.

## Known as

| Field | Name there | Relation |
|---|---|---|
| Survey methodology / psycholinguistics | QUAID, Question Understanding Aid | exact — the program implementing the scan |
| Not this concept | question comprehensibility | the property scanned for, not the scan |
| Not this concept | formal appraisal (QAS-99) | a human coder applying a fixed problem-code checklist; same output type, different instrument, and it is not threshold-fitted |
| Not this concept | predicted quality ([[survey-quality-predictor]]) | returns a variance decomposition from format codes, not flags from text |

## Transfer

| | |
|---|---|
| **In its home field** | standardised English survey items read by lay respondents, scanned by a methodologist before fielding; the criterion is a panel of language experts rating the same items |
| **Here** | an agent scanning its own drafted question before sending it, with no panel available |
| **What survives** | the object type — question text in, flagged classes out, no answerer required — and the calibration logic: a flag threshold is an operating point, so a scan that does not name its criterion is not a check ([[roc-curve]]) |
| **What does not** | the criterion itself (no expert panel exists for an agent's ad-hoc question, so the threshold cannot be re-fitted the same way), the English lexical norms the modules rest on, and any claim of coverage — comprehension is one family of defect among several |

## Limits

- graesser-2000 is **[?] for the threshold-fitting procedure**: only its
  abstract was read, and the abstract does not contain the procedure
  (maximise correlation with expert ratings) — it reports hit rate,
  false-alarm rate, d′, recall and precision against the expert corpus. The
  five problem classes are confirmed from the abstract; the fitting procedure
  is not, and is reported here as coming from the full text, which was not
  read. If it is wrong, point 2 of *Why it matters* survives anyway, since the
  reported performance figures are themselves scored against the expert
  criterion.
- Only the abstracts of graesser-2000 and graesser-2006 were read; the hit
  and false-alarm rates are not reproduced as numbers here.
- Apart from the expert-vs-SQP r = .608, the yan-2012 figures used above —
  median inter-expert correlation .360 and the problem-type agreement
  .86 / −.09 / −.33 — were not independently confirmed by the verifier and
  are taken from the paper as reported.
- A threshold fitted to maximise correlation with experts cannot make the
  scan better than the experts, and the experts' agreement with each other is
  low (yan-2012). This bounds the check without saying where the bound is.
- Nothing here licenses the fork-marker list in [[ambiguity-taxonomy]]: the
  two scans share a shape, not a validation. Importing the shape does not
  import an operating point.
- The nine-class design and the five reported classes come from the source's
  own description; this note has no independent evidence that the five are the
  ones that matter for an agent's questions rather than for survey items.

## Related

[[ambiguity-taxonomy]] · [[question-evaluation-method]] · [[survey-quality-predictor]] · [[survey-response-model]] · [[roc-curve]] · [[metamorphic-probes]]

[^s1]: graesser-2000
[^s2]: graesser-2006
[^s3]: yan-2012
