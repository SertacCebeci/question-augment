---
description: "Instead of one committed answer, the answerer publishes the **four judgements Table 3 of Andrews, Schünemann, Oxman et al. (2013,"
aliases: ["evidence to recommendation framework", "GRADE evidence to recommendation framework"]
sources: ["alonso-coello-2016", "andrews-2013-strength", "chong-2023", "hershenfeld-2026"]
---
# Evidence-to-recommendation framework

> Instead of one committed answer, the answerer publishes the **four judgements
> the answer is made of** — each a yes/no, each with its written reason and the
> sub-questions that should have decided it. Two answerers who disagree can then
> find *where*.

## Definition / Mechanism

Table 3 of Andrews, Schünemann, Oxman et al. (2013, *J Clin Epidemiol*[^s1][^s2][^s3][^s4]
66:726–735) is a four-column record filled in before the recommendation is
stated: **decision domain | judgement (Yes/No) | reason for judgement |
subdomains influencing judgement**. Each domain is written as a question put to
the panel:

| Domain | The question asked |
|---|---|
| Balance of desirable and undesirable outcomes | "Given the best estimate of typical values and preferences, are you confident that the benefits outweigh the harms and burden or vice versa?" |
| Confidence in estimates of effect (quality of evidence) | "Is there high or moderate quality evidence?" |
| Values and preferences | "Are you confident about the typical values and preferences and are they similar across the target population?" ([[values-and-preferences]]) |
| Resource implications | "Are the resources worth the expected net benefit from following the recommendation?" |

Two further rows close it: **overall strength of recommendation**, and an
**evidence to recommendation synthesis** — a sentence saying how the four
judgements combine into that strength. The fourth column is not decoration: it
lists the subdomains a panel is expected to have considered — baseline risk
similarity across subgroups, magnitude of relative benefits and harms, how much
extrapolation and modelling the estimate required, the source of the typical
values, the method for judging values sufficient, availability, opportunity
cost, and variability in resource requirements across settings.

The payload is what the record does to **disagreement**. Section 3.3 states that
"disagreement between panels is common, and disagreement may be a result of
variability in judgments about the domains or of how panels synthesize those
judgments", and offers the record as the way to tell the two apart. The worked
case is perioperative beta-blockers: one group's synthesis emphasises
heterogeneity in dose and timing across trials (a *confidence* judgement), the
other's emphasises that patients value avoiding a disabling stroke
(~0.5% at 0.5% baseline risk) far above avoiding a largely asymptomatic
myocardial infarction (~1.5% at 5% baseline risk) — a *values* judgement.
Identical evidence, different domain, and the framework names which.

The framework was later elaborated, with added criteria and typed decision
options, as the GRADE **Evidence to Decision (EtD)** framework
(Alonso-Coello, Schünemann, Moberg et al. 2016, *BMJ* 353:i2016).

## Known as

| Field | Name there | Relation |
|---|---|---|
| Evidence-based medicine (GRADE) | evidence to recommendation framework | exact — the caption of Table 3 |
| Evidence-based medicine (GRADE) | GRADE evidence to recommendation framework | exact — the same table with the system named |

**Not this concept.** The **Evidence to Decision (EtD) framework**
(Alonso-Coello et al. 2016) is a larger, later object — it adds criteria this
table does not have (among them equity, acceptability and feasibility) and
covers coverage and public-health decisions, so it is a different instrument
with a different field count, not another name for this one. A **Summary of
Findings table** is the evidence input to this record, not the record. The
[[discordant-recommendation]] is one possible *output* of it.

## Why it matters

Every other commitment note on stall 10 treats the answer's second field as a
scalar — a probability, a coverage level, a strength label. This one makes the
second field **structured**: a fixed schema of judgements the answerer must fill
before committing, in which the reason belongs to a named slot. Three
consequences for an answerer that is not a guideline panel:

- the schema is a **checklist against silent substitution** — it is visible when
  strength was set by the evidence alone and nothing was recorded about who the
  answer is for or what it costs;
- disagreement between two answers becomes **localisable**, so the asker's
  follow-up question can target the domain rather than the conclusion;
- the record is auditable after the fact, but a schema being auditable is not
  evidence that answerers fill it: no audit read here measures completion of a
  Table 3 record at all. Its nearest audited neighbour measures a different
  field of a different object — the rate at which a *discordant* recommendation
  names the licence it claims, which across bodies declaring the same protocol
  runs from 0 of 96 (Chong et al. 2023) to 25 of 33 (Hershenfeld et al. 2026)
  ([[discordance-justification-rate]]).

## Transfer

| | |
|---|---|
| **In its home field** | a panel, an evidence profile already built, a defined population and comparator, and a published table whose readers are guideline users |
| **Here** | one answerer committing to one answer, with the same four slots read as: is the balance of consequences clear, how good is my information, whose goals am I assuming, and what does acting cost |
| **What survives** | the fixed slot list; the separation of *judgement* from *reason for judgement*; the synthesis sentence stating how the slots combined; and the use of the filled record to locate a disagreement in a domain rather than in the conclusion |
| **What does not** | the binary Yes/No per domain, which the paper itself fills with a hypothetical case and never validates; and the assumption that the four slots exhaust the decision — the same paper presents the four-domain packaging as one grouping of six determinants among several that "may work well" |

## Limits

- The claim this note makes — that the record localises disagreement — holds
  only when both answerers use the **same** domain set. Andrews et al. offer the
  four-domain packaging as a presentational choice over six determinants, so two
  records built on different groupings are not comparable slot by slot, and the
  localisation fails exactly where the disagreement is about what the domains
  are.
- Section 3.3 is an argument, not a measurement: no source here shows that
  publishing a filled framework changed agreement between panels or improved any
  recommendation, and none audits whether issued recommendations carry a filled
  record. The beta-blocker case is the authors' reconstruction of a
  disagreement, not a study of it.
- Table 3 is explicitly labelled by its authors as "a hypothetical
  recommendation developed for this article and not intended for clinical
  decision making" — it demonstrates the form, and no filled example in the
  paper is a real decision.
- `chong-2023` and `hershenfeld-2026` are cited here only for the neighbouring
  justification-rate figures; those two audits used different coding schemes
  ([[discordance-justification-rate]] §Limits), so the 0-of-96/25-of-33 contrast
  is not one instrument applied twice and carries no inference about this
  framework's uptake.
- `alonso-coello-2016` is cited only for the later framework's name and
  existence; its text was not read here [?], so nothing in this note describes
  how EtD differs beyond the added criteria its title and abstract name.

## Related

[[discordant-recommendation]] · [[values-and-preferences]] ·
[[discordance-justification-rate]] · [[expected-utility]] · Commitment

[^s1]: alonso-coello-2016
[^s2]: andrews-2013-strength
[^s3]: chong-2023
[^s4]: hershenfeld-2026
