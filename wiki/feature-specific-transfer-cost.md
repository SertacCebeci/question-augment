---
description: "Transfer cost depends on which feature changes: a learned puzzle strategy moved freely to new digit sets but took a transient accuracy and speed hit when the house type switched."
aliases: ["feature-axis transfer cost", "shift-specific generalization cost"]
sources: ["doi-10-48550-arxiv-2107-06994"]
---
# Feature-specific transfer cost

A strategy learned on one set of cases can be tested on cases that differ from it along one feature at a time. The point of the design is that the cost of the shift, if any, is attributed to the feature that moved. In the hidden single study, the tutorial and practice puzzles shared one house type, one house index, one goal cell and one digit set. The test puzzles were built by changing those features, so that "the puzzles differed from the tutorial and practice puzzles along the four features."[^f1]

The two results that matter here are different in kind. Changing the digit set produced "no detectable change in accuracy or reaction time." Changing the house type produced "a small initial drop in accuracy as well as a pronounced initial slowing" of response.[^f2] The first is a null on a shift the learner might have been expected to find hard, since the digits were new. The second is a cost that is visible in both accuracy and time, but that fades over the test trials.

The authors read the digit result as learners treating digits as "freely assignable" to the roles the puzzle gives them. Those roles were the two digits that each occur three times outside the target house, and these could be used whether or not a particular digit had been seen in that role.[^f3] The house result is harder to interpret. One reading is that the strategy was partly bound to rows or columns, so the switch required remapping the display onto the abstract roles. The other is that a strategy specific to the first house type was carried over by analogy to the orthogonal one.[^f4]

A smaller effect came from the target cell. Participants "were slightly slowed by a switch of the target cell used in practice to a different cell in the grid," which the authors connect to an attentional bias toward that cell that persisted through the test.[^f5]

For asking and answering, the note says the question "does it generalize" has no single answer. It has one answer per axis of change, and the axes can differ in whether they cost accuracy, cost time, or cost nothing that the measures detect.

## Limits

- A null is not a zero. "No detectable change" in accuracy or reaction time with the sample size used does not establish that digit-set transfer is free.
- The house-type cost is measured on one switch, row to column, in one task. Other orientation or structure changes were not tested.
- The authors say it is hard to tell from the data whether the strategy was abstract at its base. Both the remapping reading and the analogy reading fit the same measured drop.
- The cell-index slowing is small, and the attentional-bias explanation is the authors' conjecture.
- Accuracy and reaction time were recorded per trial on a single attempt, with feedback only on correctness during the test phase.

## Related

- [[monotone-strategy-class-acquisition]] — the strategy classes that a shifted test would have to preserve or lose
- strategy-articulation-transfer — the transfer measured here is the one that articulation was compared with
- [[ood-confounded-removal-evaluation]] — another case where a shift check can mislead, here because the shift confounds the feature being tested
- [[proof-depth-decline-under-shift]] — a decline under a different kind of shift, depth of the reasoning chain rather than a feature of the input

[^f1]: doi-10-48550-arxiv-2107-06994 — "differed from the tutorial and practice puzzles along the four features"
[^f2]: doi-10-48550-arxiv-2107-06994 — "generalization from one set of digits to another produced no detectable change in accuracy or reaction time"
[^f3]: doi-10-48550-arxiv-2107-06994 — "participants engaged with the digits in each puzzle as freely assignable to the various roles of digits within the"
[^f4]: doi-10-48550-arxiv-2107-06994 — "a structure-mapping or analogical reasoning process"
[^f5]: doi-10-48550-arxiv-2107-06994 — "participants were slightly slowed by a switch of the target cell used in practice to a different cell in the grid"
