---
description: "An answerer that disclaims on the whole may not assert on a part in the same report — local credibility contradicts the global non-answer — while further negatives stay obligatory."
aliases: ["piecemeal-opinion prohibition", "no piecemeal opinions", "prohibition of partial assurance under a disclaimer"]
sources: ["iaasb-2015-isa705", "pcaob-2017"]
---
# Piecemeal-opinion prohibition

> "I don't know about the whole, but this part is fine" is inadmissible: the
> auditing standards forbid any unmodified opinion on a part once the opinion
> on the whole is a disclaimer or adverse, and strip out everything else in the
> report that would lend the whole credibility — while keeping every further
> *negative* finding mandatory. The global non-answer has a direction.

## Definition / Mechanism

**The rule.** ISA 705 (Revised), para. 15: when the auditor expresses an adverse opinion or disclaims an opinion on the financial statements as a whole, the report shall not also include an unmodified opinion, under the same reporting framework, on a single financial statement or on specific elements, accounts or items; to do so "would contradict the auditor's adverse opinion or disclaimer of opinion on the financial statements as a whole".[^c1]

The US standard names the forbidden object: "Piecemeal opinions (expressions of opinion as to certain identified items in financial statements) should not be expressed" under a disclaimer or adverse opinion "because piecemeal opinions tend to overshadow or contradict" it (PCAOB AS 3105, .48).[^c2]

**The rule reaches beyond opinions.** Under a disclaimer the report must also drop the statement that the evidence obtained is sufficient and appropriate (para. 26); and, unless law requires it, the Key Audit Matters section (para. 29), because communicating matters other than the one causing the disclaimer "may suggest that the financial statements as a whole are more credible in relation to those matters than would be appropriate" and "would be inconsistent with the disclaimer" (A26).[^c3]

AS 3105 applies the same logic to the description of work done: under a [[scope-limitation]] disclaimer the auditor "should not identify the procedures that were performed", as "to do so may tend to overshadow the disclaimer" (AS 3105 .45).[^c4]

**The asymmetry.** The prohibition runs one way. Even under an adverse opinion or a disclaimer, the auditor *shall* describe the reasons for any other matters that would themselves have required a modification, and their effects (para. 27; A24: a disclaimer on one matter "does not justify the omission" of other identified matters).[^c5]

**What is not a contradiction (A16).** An unmodified opinion under one framework beside an adverse opinion on the same statements under a different framework; and a disclaimer on results of operations and cash flows beside an unmodified opinion on financial position (the opening-balances case, ISA 510) — "In this case, the auditor has not expressed a disclaimer of opinion on the financial statements as a whole."[^c6]

This wiki's reading of para. 15 with A16: the unit the prohibition protects is *the whole under one framework* — parts may carry different opinions as long as no opinion on the whole has been withheld or reversed. The standard gives the escape hatches, not this unit.[^c9]

## Known as

| Field | Name there | Relation |
|---|---|---|
| IAASB (ISA 705 Revised, para. 15) | no name; the requirement and its "would contradict" rationale | exact |
| PCAOB / US practice (AS 3105 .48, from AU 508) | piecemeal opinions (the prohibited object) | exact — same prohibition, rationale "overshadow or contradict" |

[^c7]

Not this concept: the **qualified opinion** — a scoped exception inside an unmodified whole — is the *permitted* direction of composition and belongs to [[modified-opinion-matrix]]; the **Key Audit Matters** section (ISA 701) is one of the things the rule removes, not the rule.

## Why it matters

The wiki's [[abstention]] is a selection function $g(x) \in \{0,1\}$ evaluated per input; nothing in it says what the answerer may say about $x'$ once it has abstained on $x$, and a report that abstains on the whole and answers on the parts is simply a different coverage. ISA 705 says the composition is *not* free: a non-answer on the whole (a) forbids every local assertion that would lend the whole credibility — sub-opinions, the [[sufficient-statistic|sufficiency]] statement, the list of procedures, the key-matters section — and (b) keeps every further local *negative* obligatory. That is all the standards assert. The conjecture [[scoped-exception-commitment]] takes it further, as this wiki's own step: "I don't know" as a scoped object with a direction, checked for consistency after the cells of the matrix are chosen, not before.[^c10]

## Transfer

| | |
|---|---|
| In its home field | one report, one reporting framework, a fixed whole (the financial statements) whose parts (statements, accounts, items) are enumerable, and a user who reads the report as a single assurance |
| Here | an answer to a question whose "whole" is the question and whose parts are its sub-questions or axes; the reader is the asker |
| What survives | the direction: a global non-answer forbids local positive assertions and obliges local negative ones; the extension from opinions to *anything that lends credibility* (evidence statements, procedure lists) |
| What does not | the "same framework" escape hatch has no analogue unless the question fixes a framework; the enumerability of parts — an open-ended answer has no account list — so which local assertions "overshadow" the disclaimer is a judgement the standard makes by structure and an answerer must make by hand |

[^c8]

## Limits

- The standards give the rationale as *contradiction* and *overshadowing* — a claim about how users read a report — and measure neither; no study of whether readers of a disclaimer are in fact misled by a partial assertion was read.
- The AS 3105 quotations (c2 at .48, c4 at .45, the PCAOB row of c7) are unverified against an archived text extract as of this pass — pcaob-2017 `[?]` at claim level, corroborated only by the live PCAOB page. The name "piecemeal opinions" and the extension to the procedure list rest on them; the ISA 705 claims stand without them.
- The rule presupposes that the whole is a declared unit. For an answerer, whether a sub-question's answer "lends credibility" to the whole depends on a decomposition the asker may not have supplied; the note's transfer of the direction assumes one exists.
- A16's escape hatches (different framework; opening balances) show the prohibition is on *the same whole under the same framework*, so it does not forbid all coexistence of a non-answer and an answer; the headline claim and the unit in c9 are bounded by that qualification.

## Related

[[modified-opinion-matrix]] · [[abstention]] · [[scoped-exception-commitment]] · [[evidence-to-recommendation-framework]] · [[scope-limitation]]

[^c1]: iaasb-2015-isa705 — "the financial statements as a whole, the auditor’s report shall not also include an unmodified"
[^c2]: pcaob-2017 — "Piecemeal opinions (expressions of opinion as to certain identified items in financial statements) should not be expressed when the auditor has disclaimed an opinion or has expressed an adverse opinion on the financial statements taken as a whole because piecemeal opinions tend to overshadow or contradict a disclaimer of opinion or an adverse opinion."
[^c3]: iaasb-2015-isa705 — "When the auditor disclaims an opinion on the financial statements, the auditor’s report shall not"
[^c4]: pcaob-2017 — "The auditor should not identify the procedures that were performed nor include the paragraph describing the characteristics of an audit (that is, the scope paragraph of the auditor's standard report); to do so may tend to overshadow the disclaimer."
[^c5]: iaasb-2015-isa705 — "Even if the auditor has expressed an adverse opinion or disclaimed an opinion on the financial"
[^c6]: iaasb-2015-isa705 — "opinion on the same financial statements under a different financial reporting framework."
[^c7]: iaasb-2015-isa705 — "unmodified opinion in the same report in these circumstances would contradict the auditor’s"
[^c8]: iaasb-2015-isa705 — "the financial statements as a whole, the auditor’s report shall not also include an unmodified"
[^c9]: iaasb-2015-isa705 — "the financial statements as a whole, the auditor’s report shall not also include an unmodified"
[^c10]: iaasb-2015-isa705 — "unmodified opinion in the same report in these circumstances would contradict the auditor’s"
