---
description: "A committed answer carries an assumption about what the receiver wants, at Andrews, Schünemann, Oxman et al. (2013, *J Clin Epidemiol* 66:726–735,"
aliases: ["typical values and preferences", "relative preferences for outcomes"]
sources: ["andrews-2013-strength", "devereaux-2001"]
---
# Values and preferences

> A committed answer carries an assumption about what the receiver wants, at
> what exchange rate. GRADE makes that assumption a **declared, separately
> judged field** — and makes the *spread* of it across receivers a reason to
> commit less, independently of the evidence.

## Definition / Mechanism

Andrews, Schünemann, Oxman et al. (2013, *J Clin Epidemiol* 66:726–735, Box 1)[^s1][^s2]
define the term: "Values and preferences is an overarching term that includes
patients' perspectives, beliefs, expectations, and goals for health and life.
More precisely, they refer to the processes that individuals use in considering
the potential benefits, harms, costs, limitations, and inconvenience of the
management options in relation to one another." The paper's own gloss is
narrower and more usable, and it is that narrower quantity — not the overarching
term — that this note is about: the **typical values that patients — or a
population — apply to those outcomes**, "otherwise conceptualized as the
relative preferences for those outcomes", together with the spread of those
values across the population.

Three of GRADE's six determinants of a recommendation's direction and strength
are about this one thing: the estimate of typical values and preferences,
confidence in that estimate, and **variability** of values and preferences. The
paper packages the three into one of four decision domains, with a single
judgement to record: *are you confident about the typical values and
preferences, and are they similar across the target population?* (Table 3). That
packaging — the worksheet slot that bundles estimate, confidence and variability
into one recorded Yes/No with a written reason — belongs to
[[evidence-to-recommendation-framework]]; what follows here is the quantity the
slot records.

Three mechanisms follow.

1. **An exchange rate, stated.** "Maximal explicitness requires quantification."
   The example given is the ninth American College of Chest Physicians
   antithrombotic panel, which "specified that they considered typical patients
   would value preventing one stroke equivalent to avoiding three serious
   gastrointestinal bleeds" — a ratio between two outcome types, published
   alongside the recommendation.
2. **Dispersion lowers strength.** Table 1: "The greater the variability in
   values and preferences, or uncertainty in values and preferences, the more
   likely a weak recommendation is warranted." The reason given is not
   epistemic: "To the extent large variability exists, it is less likely that a
   single recommendation would apply uniformly across all patients, and the
   right course of action is likely to differ between patients." Where
   variability drives the decision, the answer should additionally carry
   "descriptions of how varying values and preferences will determine the
   optimal decision".
3. **Whose values, declared.** "Panels should explicitly state the perspective
   they are taking, particularly when they are not taking a patient-centered
   perspective" — patient, public health, or payer, each of which can reverse
   the recommendation; the paper's cost illustration is a year of one drug
   costing the equivalent of one nurse's salary in the United States, four in
   Poland and twenty in China.

Dispersion is measurable, not assumed. Andrews et al. report Devereaux, Anderson, Gardner et al. (2001, *BMJ* 323:1218–1222) as finding that most
atrial-fibrillation patients would accept a 22% bleeding risk to reduce their
stroke risk by 8%, while "a few patients were ready to accept only a small risk
of bleeding" for the same reduction — one population, one question, two
incompatible optimal actions.

## Known as

| Field | Name there | Relation |
|---|---|---|
| Evidence-based medicine (GRADE) | values and preferences | close — Box 1's overarching term is strictly wider: it also covers beliefs, expectations, goals for health and life, and the deliberation process individuals use; this note is the narrower quantity a panel records, typical relative preferences over outcomes with a spread |
| Evidence-based medicine (GRADE) | typical values and preferences | exact — the estimate the panel records for the domain |
| Evidence-based medicine (GRADE) | relative preferences for outcomes | exact — the paper's own alternative phrasing of the same quantity |
| Decision analysis | utility / disutility over outcomes | close — same role in fixing how hard to commit, different definition: a cardinal function over outcomes recovered from one decision maker's lottery choices ([[expected-utility]]), where this is a panel's asserted estimate of a population's typical trade-offs plus its published spread |

**Not this concept.** The *values and preferences domain* is not another name for
this quantity: it is the Table 3 slot that bundles three determinants — the
estimate, confidence in the estimate, and its variability — into one recorded
judgement, and it belongs to [[evidence-to-recommendation-framework]]. *Patient
preference* in shared decision making is one individual's choice in one
consultation, measured by what that person picks; the object here is a
population estimate with a dispersion attached. *Confidence in effect estimates*
is the other domain entirely — how well the outcomes are known, not how they are
valued.

## Why it matters

Stall 10's other notes treat commitment as a function of the answerer's
epistemic state: calibrate it ([[calibration]]), threshold it ([[abstention]]),
or split it in two when the consequences are asymmetric
([[discordant-recommendation]]). This note names a reason to commit less that
survives **perfect knowledge of the world**: if the recipients of one answer
value the outcomes differently from each other, no single committed answer is
right for all of them, and the correct response is a weaker commitment plus an
explicit statement of which values would flip it. That converts "who is asking"
from a comprehension problem (stall 9) into a quantity the answerer must
estimate, publish, and be judged on.

It also supplies the missing unit for [[expected-utility]]'s complaint that a
utility function must be elicited before any decision-theoretic score exists:
GRADE's answer is that the utility is not elicited but *asserted as typical, in
public, as a ratio between named outcomes*, and that its spread is reported
beside it.

## Transfer

| | |
|---|---|
| **In its home field** | a guideline panel choosing between named management strategies for a defined patient population, with (ideally) systematic reviews of values studies, patient-group consultation, and a written domain judgement |
| **Here** | an answerer replying to askers it cannot interview, whose goals it must guess, and whose spread it can only estimate from the class of askers the question comes from |
| **What survives** | the exchange rate between outcome types as a publishable object; the rule that dispersion of receivers' values caps how hard an answer may push; the requirement to state whose perspective was taken; the instruction to describe *which* values would change the answer instead of averaging over them |
| **What does not** | the empirical base — systematic reviews of values studies exist for few questions and none for an arbitrary asker; and the population frame itself: for a single identified asker dispersion is zero, so the mechanism yields nothing and is replaced by asking the person |

## Limits

- The claim this note makes — that commitment should fall as the recipients'
  values disperse — assumes the answer is **broadcast to a population** the
  answerer cannot query. It gives no guidance for a one-to-one exchange, where
  the cheaper move is a clarifying question ([[clarification-request]]), and it
  is silent on how to pick the population whose spread counts.
- GRADE states a direction, not a function: "the more likely a weak
  recommendation is warranted" has no threshold, no unit and no rule for
  combining this domain with the other three — the paper's abstract says panels
  "must use judgment in integrating these factors".
- The estimate is usually weak at source, by the authors' own admission: less
  well-resourced panels "must rely on unsystematic reviews of the available
  literature and their clinical experience", and "how well such estimates
  correspond to true typical values and preferences is likely, in any particular
  situation, to be uncertain".
- The Devereaux figures (22% / 8%) are quoted here from Andrews et al.'s summary
  of that study; the primary paper was confirmed to exist and match its citation
  but its full text was not read here [?], so treat the numbers as the
  guideline authors' reading of it.

## Related

[[discordant-recommendation]] · [[evidence-to-recommendation-framework]] ·
[[expected-utility]] · [[abstention]] · [[clarification-request]] ·
Commitment

[^s1]: andrews-2013-strength
[^s2]: devereaux-2001
