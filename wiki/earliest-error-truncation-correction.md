---
description: "A reviewer finds the first wrong step in a reasoning chain, the chain is cut there, and the worker regenerates the tail under a comment; measured gains level off near five rounds."
aliases: ["review-truncate-comment-continue", "progressive correction loop", "prefix-retaining chain-of-thought correction", "earliest-error truncation"]
sources: ["arxiv-2512-22627"]
---
# Earliest-error truncation correction

A chain of reasoning written by a worker model is inspected step by step by a second model, the reviewer. The reviewer finds the earliest step that is wrong, "identifies the earliest incorrect reasoning step, removes" it together with everything after it, and keeps only the verified prefix before it.[^c1] It then writes a comment on what is wrong and points toward a fix. The worker continues the chain from the retained prefix, "Guided by the comments, the worker LLM continues generating new" steps.[^c2]

The cycle is review, truncate, comment, continue. It "is repeated until a predefined maximum number of correction rounds is reached," and the best corrected chain from the rounds is kept as the output of the process.[^c3] The paper selects that best chain by answer correctness or by closeness to the reference answer.[^c11]

The mechanism is built on one premise. The paper argues that time series data, unlike purely textual material, "are inherently verifiable, enabling consistency checking between" the reasoning steps and the input.[^c4] A reviewer can therefore test a step against the numbers it cites, and cutting the chain at that step keeps the checked prefix intact while only the unchecked tail is regenerated. (That the truncation protects the prefix is my reading of the design; the paper does not measure it separately.)

## What was measured

On the TMQA dataset, the paper sweeps the maximum number of correction rounds over 1, 2, 3, 4, 5 and 10.[^c5] At one round the method "already significantly outperforms the no-" review-correction baseline, which is standard chain-of-thought without correction.[^c6] Accuracy keeps rising from one to three rounds. Between three and five it is stable for classification and anomaly detection, and the paper reads this as "the benefit of larger MCR saturates."[^c7] Ten rounds gave a result "even slightly lower" than five.[^c8] The paper's explanation is that long correction rounds "create too many comments," which makes the model answer more conservatively.[^c9]

The quality of the corrected chain depends on both roles. Swapping in a weaker reviewer lowered the student's results, and the paper ties this to reasoning ability: "the reasoning ability of LLMs affects the quality of their corrected CoT."[^c10] A weak worker is worse: when the first chain is wrong, "the later correction process is unable to stop the" student from learning from it.[^c12]

## Limits

The reviewer is given the reference answer. Its input includes "the golden standard answer An , the primitive CoT," and it is instructed not to reveal the answer in its comment, "without revealing any information about the golden" standard answer.[^c13] So the loop uses label information in the review itself. The text does not test whether the same reviewer can localize the first error without the label; that is the question a loop without labels would need answered.

The round sweep was run on one dataset, TMQA; the figure caption names only that set.[^c5] The main comparison is with a no-correction baseline at one round, so the text does not separate the value of the truncation step from the value of the extra generation it allows. The paper also reports no measure of whether the truncation point is the true error. The gap between detecting that a chain is broken and naming the broken step is documented for judges generally, see [[cot-judge-detection-localization-gap]]; this loop depends on the naming step.

The paper's own cost trade-off is stated briefly: "this analysis offers a reasonable trade-off in setting MCR" between performance and computation.[^c14] No cost figures are given in the text.

## Related

- [[corrected-trace-distillation]] — what the corrected chains are used for: training a smaller student that reasons without the reviewer.
- [[cot-judge-detection-localization-gap]] — judges flag broken chains more often than they name the broken step; the truncation point is exactly that naming.
- [[specific-actionable-self-feedback]] — a model's own critique helps a draft only when it is specific; here the critic is a separate model and the revision regenerates only the tail, not the whole answer.
- [[self-repair-anchoring]] — conditioning on a failed attempt can reproduce it; a loop that keeps the verified prefix and regenerates only after the cut is a different way of using the failure (my inference, not tested in the paper).

[^c1]: arxiv-2512-22627 — "identifies the earliest incorrect reasoning step, removes"
[^c2]: arxiv-2512-22627 — "Guided by the comments, the worker LLM continues generating new"
[^c3]: arxiv-2512-22627 — "is repeated until a predefined maximum number of correction rounds is reached."
[^c4]: arxiv-2512-22627 — "time series data are inherently verifiable, enabling consistency checking between"
[^c5]: arxiv-2512-22627 — "on the TMQA dataset"
[^c6]: arxiv-2512-22627 — "T3LLM already significantly outperforms the no-"
[^c7]: arxiv-2512-22627 — "the benefit of larger MCR saturates"
[^c8]: arxiv-2512-22627 — "performance of 10 setting is even slightly lower"
[^c9]: arxiv-2512-22627 — "long correction rounds create too many comments,"
[^c10]: arxiv-2512-22627 — "the reasoning ability of LLMs affects the quality of their corrected CoT"
[^c11]: arxiv-2512-22627 — "answer correctness or proximity to the golden standard answer."
[^c12]: arxiv-2512-22627 — "the later correction process is unable to stop the"
[^c13]: arxiv-2512-22627 — "without revealing any information about the golden"
[^c14]: arxiv-2512-22627 — "this analysis offers a reasonable trade-off in setting MCR"
