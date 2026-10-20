---
description: "Traces are merged into a shared-prefix tree and disputed only at nodes with two or more children, comparing each branch's next steps under the shared context, not whole answers."
aliases: ["critical divergence point", "CDP", "decision-critical divergence"]
sources: ["doi-10-48550-arxiv-2602-09341"]
---
# Critical divergence point

Reasoning traces from several agents often share a common opening. If the traces are merged into one tree, a shared opening becomes a single path, and a node with two or more children is the place where the traces actually part ways. The auditing paper calls such a node a Critical Divergence Point (CDP): a node $u$ is marked "when it has at least two children."[^c1] Agreements become shared prefixes and disagreements become explicit branch points, so the dispute is localised rather than spread across whole traces.[^c2]

At each CDP the adjudicator receives a divergence packet. The packet holds the shared path from the root to the node, and for each child the next few steps along that branch together with the agents whose traces pass through it. The paper states its purpose plainly: "This packet focuses the Auditor on the immediate logical consequence of the divergence, rather than downstream verbosity or full-trace noise."[^c3] Agent support is carried along but is not treated as evidence: "Support frequency is not treated by the local Auditor as direct evidence of correctness."[^c4]

The adjudicator scores the competing branches on a rubric covering factual accuracy, logical soundness, constraint adherence, assumption validity and trace hygiene, and returns one branch.[^c5] Traversal runs from the root and the Auditor is invoked at each CDP, so the chosen branch sets the path for everything below it. The paper keeps an optional beam because a wrong early choice is hard to undo: "a single early mis-adjudication can irreversibly prune the correct lineage."[^c6]

The mechanism therefore changes the unit of disagreement. It is a point in a tree, and the decision there compares the evidence on each side of the split rather than counting the agents on each side. The count is not discarded altogether: it survives as a fallback.

**What transfers (my inference).** Any setting in which chains of steps share prefixes has a split point that can be located and checked. The paper's gain depends on that split being at a step the adjudicator can actually assess. Where steps are free text with no checkable content, the same tree exists but the comparison at the node has less to hold onto.

## Limits

- The reported gains are for the full pipeline: tree, Auditor and preference training together. The sections read here do not isolate the localisation step from the Auditor's accuracy. The claim that localisation is what helps rests on the paper's argument and its two-branch toy proposition, not on a separate measurement in the sections read (my reading).
- A divergence packet holds only the next few representative steps: each branch contributes "the next $\ell_v \le k$ representative step texts."[^c7] A disagreement that appears later, or a shared prefix that is already wrong, lies outside the packet (my inference).
- The tree is built from "representative step texts on the path" to the node.[^c8] Deciding that two steps are the same step is a judgement, and the tree is only as good as that merging (my inference).
- Late disagreement is not always resolved locally. When surviving lineages still disagree at the end, the paper falls back to counting: the system "falls back to the majority-supported candidate as a conservative default."[^c9] So a count still has the last word in the hard cases.
- The paper's own scope note applies here too: the method "should not be expected to improve every instance or every multi-agent system" (see [[confabulation-consensus]] for the same quote in context).

## Related

- [[confabulation-consensus]] — the failure this localisation is meant to avoid; whole-answer counting is what it replaces
- [[disagreement-retention-in-debate]] — also routes attention to where agents disagree rather than to how many agree; there the selection is of messages, here it is of the decision point
- [[cot-judge-detection-localization-gap]] — judges flag a broken chain more often than they name the broken step; a divergence packet needs exactly the naming that gap says is missing

[^c1]: doi-10-48550-arxiv-2602-09341 — "when it has at least two children"
[^c2]: doi-10-48550-arxiv-2602-09341 — "agreements form shared prefixes and disagreements become explicit branch points"
[^c3]: doi-10-48550-arxiv-2602-09341 — "This packet focuses the Auditor on the immediate logical consequence of the divergence, rather than downstream verbosity or full-trace noise."
[^c4]: doi-10-48550-arxiv-2602-09341 — "Support frequency is not treated by the local Auditor as direct evidence of correctness"
[^c5]: doi-10-48550-arxiv-2602-09341
[^c6]: doi-10-48550-arxiv-2602-09341 — "a single early mis-adjudication can irreversibly prune the correct lineage"
[^c7]: doi-10-48550-arxiv-2602-09341 — "truncated earlier if another CDP is reached"
[^c8]: doi-10-48550-arxiv-2602-09341 — "sequence of representative step texts on the path"
[^c9]: doi-10-48550-arxiv-2602-09341 — "falls back to the majority-supported candidate as a conservative default"
