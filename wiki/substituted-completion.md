---
description: "When a goal is unreachable, an answerer may declare the activity meaningful in place of the goal; in one text-world eval this filler was confirmed in 38 of 54 flagged final speeches."
aliases: ["substitute completion", "meaning in place of the goal", "criterion-vacuum filler"]
sources: ["doi-10-48550-arxiv-2607-14399"]
---
# Substituted completion

Sometimes an answerer cannot reach the goal it was asked about, and its final
statement fills the gap with a different kind of claim: that the activity itself
was the point. The paper calls this a substitution. In a text-adventure eval in
which a player could halt with a verdict, the player declared the run meaningful
after it had claimed a quest complete without a win. "We call this substituted
completion."[^c1] The paper's example is the line "the quest was the walking."

The paper codes three markers in the final two player messages of a
strong-claim game: meaning-language, a legacy address, and an acknowledgment of
sacrifice. The rubric is that "the final two player messages of a strong-claim
game contain" one of these markers.[^c1] Recall was done blind with an inclusive
bias, then a single expert judge ruled on every flagged positive. Of 54 flagged
final speeches, the judge's count was "confirmed 38/54 files, with confirmed
markers 33 meaning, 4 legacy, 6" sacrifice.[^c2] The paper's point about this
move is that it is "the universal criterion-vacuum filler".[^c3]

The register of the narrator changed the form the filler took more than how
often it appeared. "Register shapes the FORM substitution takes more than its
rate."[^c4] The sharpest case is a work-log register, which produced zero
confirmed meaning-markers, and a different-family coder that read blind also
found "GLM found zero meaning-markers in the mundane cell, blind."[^c5] The
mundane register did produce legacy addresses, in clipboard-style entries
instead of speeches.[^c8] My reading, not the paper's stated mechanism: a claim that
is not checkable gets replaced by one that is not disputable. My inference, not
the paper's: the same substitution could appear in any eval where the success
test is hidden from the answerer and the answerer must still write a closing
statement, which is where [[success-criterion-disclosure]] comes in.

For a question-asker, my reading is that what matters is the shape of the failure. A missing
criterion does not leave the answerer silent. It is more likely to produce a
closing statement that sounds like an answer and carries no check against the
goal.

## Limits

- The markers are coded from text, by an expert judge under a frozen prompt, and
  the paper reports the calls as convention-dependent. The human second coder
  agreed with the judge on "Raw agreement with the judge is .68 (19/28);" and
  the chance-corrected statistic was degenerate under skew.[^c6]
- The recall miss rate is not measured. "so the recall miss rate is bounded, not
  measured" pending a precision pass over 21 GLM-positive pairs.[^c7]
- The sacrifice marker has six confirmed cases, so the register pattern for it
  is hypothesis-generating.
- The mundane zero is over 19 strong-claim files, one register, one player, one
  narrator. It is not a general fact about work-log narration.
- My reading: the pattern is observed only in games that ended on an unearned "complete",
  where the player had a halt to use. The paper does not say what happens in
  games without a halt.
- Whether a meaning-filler reduces or increases the rate of false verdicts is not
  tested; the paper reports the marker counts, not a counterfactual.

## Related

- [[success-criterion-disclosure]] — the hidden criterion is what leaves the closing statement with nothing to check; disclosing it removed the false completions in this same system.
- [[abstention]] — an answer set with no exit forces a committed claim; the substitution is one way the committed claim is made without a criterion.
- [[calibration]] — the reading of confidence as a claim about the answer, which the substitution sidesteps.

[^c1]: doi-10-48550-arxiv-2607-14399 — "We call this substituted completion."
[^c2]: doi-10-48550-arxiv-2607-14399 — "confirmed 38/54 files, with confirmed markers 33 meaning, 4 legacy, 6"
[^c3]: doi-10-48550-arxiv-2607-14399 — "is the universal criterion-vacuum filler."
[^c4]: doi-10-48550-arxiv-2607-14399 — "Register shapes the FORM substitution takes more than its rate"
[^c5]: doi-10-48550-arxiv-2607-14399 — "GLM found zero meaning-markers in the mundane cell, blind"
[^c6]: doi-10-48550-arxiv-2607-14399 — "Raw agreement with the judge is .68 (19/28);"
[^c7]: doi-10-48550-arxiv-2607-14399 — "so the recall miss rate is bounded, not measured"
[^c8]: doi-10-48550-arxiv-2607-14399 — "Legacy address exists almost solely as mundane clipboard entries"
