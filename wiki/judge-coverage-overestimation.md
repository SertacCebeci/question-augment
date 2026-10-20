---
description: "LLM judges rate reasoning chains as largely complete even when 70% of middle steps are deleted, treating surface coherence as completeness; their ranking of completeness tracks truth only weakly."
aliases: ["coverage score inflation", "completeness overestimation by judges"]
sources: ["arxiv-2603-05167"]
---
# Judge coverage overestimation

Coverage asks whether the essential intermediate inferences are present in a reasoning chain. In C2-Faith, steps are deleted from verified chains at controlled rates (up to 70% of middle steps), and judges score completeness on a 0-4 rubric; reference scores come from GPT-4.1 given the original chain and the removed steps.[^c1]

## What was found

All three judges were too generous: even at the highest deletion level the mean coverage score stayed near 3.0.[^c2] Their ordering of which chains are more complete only weakly tracked the reference, and DeepSeek-V3.1 was essentially uncorrelated at 10-30% deletion; o4-mini was most consistent and tied GPT-4.1 at the top deletion level (rho = 0.331).[^c3] The authors' explanation is that coverage requires global reasoning over the whole chain, while causality can be checked locally, and that judges "treat surface coherence as evidence of completeness".[^c4] They recommend using coverage scores as a triage signal, combined with step-level auditing or multi-judge agreement, not as a strict threshold.[^c5]

For asking and answering: a fluent answer that skips steps is not penalized by the judge, so a missing-premise or skipped-inference defect is the kind that goes unnoticed.

## Limits

- The reference is itself a GPT-4.1 judgement with extra information, not a human label.
- Deletions are random steps from math chains; whether judges notice deletions of central versus peripheral steps was not separated here.
- The coherence explanation is the authors' interpretation, not tested by intervention.
- Three judges, one dataset.

## Related

- [[cot-judge-detection-localization-gap]] — the companion causal-faithfulness result from the same benchmark
- [[judge-master-key-false-positives]] — judges accepting form in place of content
- [[correct-answer-trap]] — rewards that miss what the answer lacks

[^c1]: arxiv-2603-05167 — "Reference scores are produced by GPT-4.1 under the same rubric, but with access to the original complete CoT and explicitly removed steps."
[^c2]: arxiv-2603-05167 — "For coverage, all judges are too generous, even at high deletion (70% of middle steps removed), mean coverage scores remain around 3.0."
[^c3]: arxiv-2603-05167 — "DeepSeek-V3.1 is essentially uncorrelated at low deletion (10–30%)."
[^c4]: arxiv-2603-05167 — "judges treat surface coherence as evidence of completeness"
[^c5]: arxiv-2603-05167 — "Coverage scores are therefore best used as a triage signal rather than a strict threshold"
