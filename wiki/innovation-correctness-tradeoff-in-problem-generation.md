---
description: "Fine-tuning an LLM on existing problems raised the novelty of generated math problems while lowering their correctness, because SFT teaches design patterns, not reasoning (the 'innovation curse')."
aliases: ["innovation curse", "innovation-correctness conflict"]
sources: ["arxiv-2601-11792", "arxiv-2512-23601"]
---
# Innovation-correctness tradeoff in problem generation

In innovative mathematical problem generation, the authors observed that after supervised fine-tuning (SFT) of the base model, the innovation of the generated problems improved while their correctness declined. They name this the "Innovation Curse".[^c1]

## Mechanism claimed

The paper's explanation is that SFT lets the model learn existing problem-design paradigms rather than strengthen logical reasoning, which is set mainly in pre-training. The model then combines problem elements to look innovative without ensuring mathematical rigor.[^c2] In the ablation, the base-model trajectory shows correctness falling as innovation rises across training stages.[^c3]

A later group relative policy optimization (GRPO) stage recovered correctness for most configurations, with innovation sometimes slightly lower. The authors read this as distributional adjustment and trade-off optimization between the two.[^c4]

## Mitigation reported

The authors do not remove the conflict by training alone. They add a multi-role loop (sampler, generator, evaluator) in which the generated problem is checked and revised, so that correctness is restored through iterative self-assessment and external expert feedback. They report that this keeps innovation high while correctness stays competitive (my paraphrase of their summary; see the conclusion).[^c5] In pairwise Elo comparisons, the expert-mode system had the top innovation Elo among closed-source models while ranking second on correctness.[^c6]

## Limits

- The tradeoff is shown in one domain (Chinese high school math), one base-model family and one dataset the authors built; no claim here that it holds for other question types.
- "Innovation" and "correctness" are scored by LLM judges and Elo comparisons, not by human experts alone; the causal account (SFT teaches patterns, not reasoning) is the authors' interpretation, not isolated by an intervention.
- The mitigation bundles several changes (difficulty encoding, distillation, GRPO), so which part restores correctness is not separated cleanly here.
- A contrasting result exists in another setting. A prompt-level divergent-then-convergent split, applied to programming-task generation with no fine-tuning, produced tasks that expert evaluators rated higher on the utility-related submetrics than chain-of-thought tasks.[^c7] The tradeoff described above is therefore a property of the SFT route in this study, not a general law of diversity against correctness. The programming study is a different domain and a different mechanism, and it does not measure novelty against correctness on the same scale as the math study.

## Related

- [[calibrated-question-generation]] — generation quality control against a target
- [[idea-then-verify-question-generation]] — generate-then-verify pattern like the evaluator loop
- [[question-generativity]] — novelty of generated questions

[^c1]: arxiv-2601-11792 — "This phenomenon reveals an inherent conflict between correctness and innovation in MPG tasks,"
[^c2]: arxiv-2601-11792 — "This conflict arises because SFT enables the model to learn existing problem design paradigms rather than enhance logical"
[^c3]: arxiv-2601-11792 — "correctness declined while innovation improved throughout training"
[^c4]: arxiv-2601-11792 — "This suggests that the GRPO stage prompted the model"
[^c5]: arxiv-2601-11792 — "Experimental results demonstrate that the framework effectively mitigates the innovation curse through multi-role collaboration."
[^c6]: arxiv-2601-11792 — "Most significantly, Ours-E dominated the Innovation"
[^c7]: arxiv-2512-23601 — "were judged higher than those from C OT on the utility-related submetrics"
