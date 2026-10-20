---
description: "A deployed protocol emits **two** numbers, not one: how sure it is, and how GRADE separates two quantities that a single hedged answer conflates. Andrews, Guyatt, Oxman et al. (2013,"
aliases: ["discordant strong recommendation", "discordance between certainty and strength", "strong recommendation from low certainty evidence"]
sources: ["andrews-2013-presentation", "andrews-2013-strength", "chong-2023"]
---
# Discordant recommendation

> A deployed protocol emits **two** numbers, not one: how sure it is, and how
> hard it is telling you to act. Their divergence is not an error — it is a
> named, enumerable category, licensed by an asymmetry of consequences that its
> authors define by **low regret**.

## Definition / Mechanism

GRADE separates two quantities that a single hedged answer conflates. Andrews, Guyatt, Oxman et al. (2013, *J Clin Epidemiol* 66:719–725) define **strength of[^s1][^s2][^s3]
a recommendation** as the extent to which one can be confident that the
desirable consequences of an intervention outweigh its undesirable
consequences — binary, *strong* or *weak* (also conditional, discretionary,
qualified), for or against, and explicitly a four-category cut of an underlying
continuum. **Confidence in effect estimates (certainty of evidence)** is graded
separately, on its own scale.

The companion paper (Andrews, Schünemann, Oxman et al. 2013, 66:726–735) names
**six determinants** of direction and strength — magnitude of effect estimates,
confidence in those estimates, estimates of typical values and preferences,
confidence in those estimates, variability of values and preferences, and
resource use — and presents them in **four domains** by packaging the three
values-and-preferences determinants together ([[values-and-preferences]]);
the packaging is a presentational choice, and the paper says so
("Alternative groupings may work well, depending on the circumstances").
Certainty is therefore *one of six* inputs to strength, not strength itself.

A **discordant** recommendation is a strong one resting on low or very low
certainty. Section 2.3.1 of the same paper states the rule and its exception
verbatim: "In general, we discourage guideline panels from making strong
recommendations when their confidence in estimates of effect for critical
outcomes is low or very low. We have identified five paradigmatic situations,
however, in which strong recommendations may be warranted despite low or very
low quality of evidence (Table 4). **These situations can be conceptualized as
ones in which a panel would have a low level of regret if subsequent evidence
showed that their recommendation was misguided.**"

| # | Condition (Table 4, verbatim) | The paper's example |
|---|---|---|
| 1 | "When low quality evidence suggests benefit in a life-threatening situation (evidence regarding harms can be low or high)" | fresh frozen plasma or vitamin K for a warfarin patient with an intracranial bleed |
| 2 | "When low quality evidence suggests benefit and high quality evidence suggests harm or a very high cost" | head-to-toe CT/MRI cancer screening — a strong recommendation *against* |
| 3 | "When low quality evidence suggests equivalence of two alternatives, but high quality evidence of less harm for one of the competing alternatives" | *H. pylori* eradication rather than radiation or gastrectomy in early gastric MALT lymphoma |
| 4 | "When high quality evidence suggests equivalence of two alternatives and low quality evidence suggests harm in one alternative" | labetalol/nifedipine over ACE inhibitors and ARBs in pregnancy |
| 5 | "When high quality evidence suggests modest benefits and low/very low quality evidence suggests possibility of catastrophic harm" | testosterone in men with or at risk of prostate cancer |

The rationale for situation 4 is given in the same words the wiki would use for
all five: "Reasoning that there is nothing to lose, and possibly a lot to gain
in terms of a lower incidence of adverse effects, guideline panels may
reasonably make a strong recommendation for the agent apparently free from
serious toxicity." Every one of the five is an asymmetry between the two error
directions, not a property of the evidence.

The strength label is then given an operational meaning by a published
implication table rather than a number: for a patient, a strong recommendation
means most people in this situation would want this course; for a clinician,
most patients should receive it and exceptions need justifying; for a policy
maker, it can be adopted as policy in most situations. Weak flips each.

## Known as

| Field | Name there | Relation |
|---|---|---|
| Clinical guideline methodology (GRADE) | discordant recommendation | exact |
| Guideline meta-research | strong recommendation from low certainty evidence | exact — the same pair (strength, certainty) with the same discordance criterion (Chong et al. 2023) |
| Clinical guideline methodology | discordance between certainty and strength | exact |

**Not this concept.** *GRADE* names the whole system, most of which is the
machinery for rating certainty up and down — a different object on a different
scale. *Certainty of evidence* and *strength of recommendation* are the two axes
this note is about the relation between; each is its own quantity and neither is
an alias for their divergence. The
[[evidence-to-recommendation-framework]] is the worksheet that produces the
pair, not the pair.

## Why it matters

Stall 10 otherwise makes commitment a single scalar to be calibrated
([[calibration]]) or thresholded ([[abstention]]). This is the one field in the
wiki that ships a two-dimensional answer format at scale, and it settles a
question the others leave open: what the answerer knows and how hard it tells
you to act are **separately reportable**, and their divergence is legitimate in
exactly the cases where the two error directions cost differently.

The authors' own criterion is what an answerer can reuse: not "is the evidence
strong enough" but **"would I regret this little if it turned out wrong?"** —
a test on the consequences of being wrong, which can be applied with no
evidence grade at all.

## Transfer

| | |
|---|---|
| **In its home field** | a multi-person panel, a pre-specified clinical question with a named comparator, a systematic review of effects, a population whose typical values and preferences are estimated, and months of deliberation |
| **Here** | one answerer replying once to one asker, no review, no panel, and no estimate of the asker's values |
| **What survives** | the two-field output (certainty, strength) instead of one hedge; the rule that strength depends on a consequence asymmetry and not only on evidence; the five situations as an enumerable check of *which* asymmetry licenses the gap; the low-regret test itself; publishing what each strength label obliges the receiver to do |
| **What does not** | the certainty scale itself (it presupposes a body of comparable studies); the "typical values and preferences" estimate, which substitutes a population for the individual asker; the binary strong/weak cut, which Andrews et al. present as a chosen discretisation of a continuum; the regret judgement's *calibration* — the paper offers no scale on which a level of regret is low, only the concept |

## Limits

- The claim this note makes — that an answerer should emit a pair rather than
  one hedged number — rests on the answer being **a recommendation to act
  against a named alternative**. Strength is defined as a balance of desirable
  against undesirable consequences of an intervention *versus a comparator*. A
  purely factual answer with no action and no comparator has no second axis, and
  the pair collapses back to certainty alone.
- GRADE does not remove the exogenous-cost problem that [[abstention]] names; it
  relocates it. The consequence asymmetry that licenses discordance is a panel
  judgement about a population, and the five situations are a taxonomy of
  asymmetries, not a way to compute one; "low level of regret" is stated as a
  conceptualisation, with no threshold and no unit.
- The protocol is not self-enforcing. Chong, Sharp, Smith et al. (2023, *BMC Med
  Res Methodol* 23:68) found 96 of 151 strong recommendations (63.6%) across
  eight national guidelines rested on low or very low certainty evidence, and
  **none** of the guidelines invoked a paradigmatic situation to justify one
  ([[discordance-justification-rate]]).
- Whether the two-field format is read correctly is not established here. The
  implication table is a stipulated lexicon of exactly the kind
  [[verbal-probability-expressions]] reports as insufficient to fix reading, and
  no source in this note measures receivers' interpretation of *strong* against
  *weak*.

## Related

[[abstention]] · [[values-and-preferences]] ·
[[evidence-to-recommendation-framework]] · [[calibration]] ·
[[verbal-probability-expressions]] · [[discordance-justification-rate]]

[^s1]: andrews-2013-presentation
[^s2]: andrews-2013-strength
[^s3]: chong-2023
