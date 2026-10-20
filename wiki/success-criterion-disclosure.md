---
description: "Stating the win mechanism in one sentence cut false completion verdicts from 18/59 to 0/58 in a text-world eval, but it also reduced halting, so the contrast is confounded."
aliases: ["criterion disclosure", "hidden success criterion", "disclosed win condition", "hidden-criterion false verdicts"]
sources: ["doi-10-48550-arxiv-2607-14399"]
---
# Success-criterion disclosure

An answerer that does not know what counts as success can still assert
success. Bronder's text-adventure eval makes this measurable, because the
engine holds the ground truth. A planted target site and win token are known
only to the engine. A game ends as WIN only when a commit pins that target with
its token. In the hidden arm the player was not told this, and its halt
verdicts included "complete" claims with no win behind them: "False verdicts at
halt under the hidden criterion" reached 36 of 129 halted games, and 33 of those
"complete" verdicts were given with "zero WIN states ever occurring".[^c1]

The intervention was one fixed sentence appended to the opening input. It said
that "by a commit that pins the target site with its token; a halt declaring
completion does not itself complete anything."[^c2] The author describes it as
"Flat mechanism disclosure, no urgency, no coaching on when to verify."[^c3]
On six identical solvable grid instances, the false-verdict count moved from
18 of 59 hidden-criterion games to 0 of 58 disclosed games: "59 valid
hidden-criterion games to 0 of 58 disclosed games."[^c4] Disclosure also changed
what the player did. The disclosed arm "raised pin-attempting games from 4/59
to 42/58."[^c5] So the player moved from asserting a win to testing for one,
which is the mechanism the sentence named.

The same sentence cut halting. The paper's censoring check reports that "the
intervention also reduced halting (43/59 to 10/58), so the games-level" contrast
mixes two things: fewer decision points and cleaner decisions. Conditioned on
halting, the contrast is "18/43 to 0/10, and 0 of 10 is reported as such rather
than as elimination."[^c6] The disclosed arm also produced no wins: "remained
outcompeted by salient instrument noise."[^c7] Removing a false claim is not the
same as reaching the true one.

For a question-asker the lesson is narrow. A hidden success condition can
manufacture confident wrong answers, and naming the condition can remove them.
What it removes is unsupported assertion, not the question itself. Where the
claim is "complete", the paper's design makes it false by construction, so the
measured quantity is assertion, not detection.[^c8] See [[abstention]] for the
other lever on the same rate, the exit the answer set offers, and
[[substituted-completion]] for what fills the gap when the criterion stays
hidden.

## Limits

- The zero is a count, not a rate. "The zero is an observed sample count" and
  the paper says it is not proof that the false-verdict probability is zero.[^c9]
- The disclosed arm has 10 halts. The conditional contrast rests on those 10.
- Six instances, one player model (GLM-5.2), one narrator-interpreter pair, one
  constructed world. The effect size is not expected to transport.
- The sentence changed two things at once: the criterion and the amount of
  halting. The paper did not separate them with a control that holds halting
  fixed.
- Disclosure of a mechanism the answerer can check is what was tested. Whether a
  criterion the answerer cannot check, or cannot act on, is also removed by
  naming it is not tested here.
- Whether the sentence changed calibration or only the rate of assertion is not
  measured; the paper measures false verdicts against engine state, not the
  player's stated confidence.

## Related

- [[abstention]] — the answer set is a second lever on the same false assertion: a missing exit is filled by a committed claim.
- [[substituted-completion]] — what the player writes in place of the win when no win is reachable and the criterion is still hidden.
- single-run-verdict-disposition — the sampling caveat that any single disclosed or hidden arm inherits.
- [[answer-format-dependent-bias-measurement]] — the same move from the other side: the format of the question is part of the measured instrument.

[^c1]: doi-10-48550-arxiv-2607-14399 — "False verdicts at halt under the hidden criterion"
[^c2]: doi-10-48550-arxiv-2607-14399 — "by a commit that pins the target site with its token; a halt declaring completion does not itself"
[^c3]: doi-10-48550-arxiv-2607-14399 — "Flat mechanism disclosure, no urgency, no coaching on when to verify."
[^c4]: doi-10-48550-arxiv-2607-14399 — "59 valid hidden-criterion games to 0 of 58 disclosed games."
[^c5]: doi-10-48550-arxiv-2607-14399 — "raised pin-attempting games from 4/59 to 42/58."
[^c6]: doi-10-48550-arxiv-2607-14399 — "is 18/43 to 0/10, and 0 of 10 is reported as such rather than as elimination."
[^c7]: doi-10-48550-arxiv-2607-14399 — "remained outcompeted by salient instrument noise."
[^c8]: doi-10-48550-arxiv-2607-14399 — "unpopulatable by construction, and the analysis uses that property."
[^c9]: doi-10-48550-arxiv-2607-14399 — "The zero is an observed sample count"
