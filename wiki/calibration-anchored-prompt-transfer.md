---
description: "Prompts can be carried across models by a mapping fitted on tasks where both models' best prompts were found, then applied to unseen tasks with only the source prompt in hand."
aliases: ["PromptBridge", "anchor-task prompt mapping", "model-adaptive prompt transfer", "cross-model prompt mapping"]
sources: ["arxiv-2512-01420"]
---
# Calibration-anchored prompt transfer

If a prompt does not carry over between models, one option is to learn the correspondence between the two models' prompts instead of re-optimizing for every task and model. The PromptBridge paper does this in two stages. The first is calibration: "requires only a small set of alignment tasks for calibration."[^a1] For each alignment task, the best prompt for the source model and the best prompt for the target model are both found by a search, and the pair is kept as an anchor. The second stage is transfer. The anchors are analyzed by a capable language model, which "distills the consistent prompt-level adjustments required" when moving prompts from the source model to the target model.[^a2] The distilled output is a natural-language description, not a trained weight matrix: "This distilled summary constitutes the transferable knowledge, describing how task-optimal prompts for the source model" should be reworded for the target.[^a3]

At test time the anchors are not needed again for the new task. For an unseen task, the source-model prompt is the only input, and "given a source-model prompt, this mapping directly produces an optimized prompt for the target model."[^a4] The mapping is applied in context, so no training happens on the new task. The paper calls the approach training-free.

The measured effect is relative to direct transfer, not to re-optimization. On SWE-Bench the paper reports that "PromptBridge yields a 27.39% improvement on SWE-Bench" over direct transfer to the target model o3.[^a5] Its summary claim is that PromptBridge "consistently reduces the transfer gap and maintains or improves performance while substantially" lowering migration overhead.[^a6] The stated goal is to approximate, as closely as possible, "the performance of the true task-optimal target-model prompt."[^a7]

The concept can be separated into three parts that a reader can ask about separately. First, the anchor pairs: they must exist for both models on a set of tasks. Second, the mapping: a description of how the source-model prompts differ from the target-model prompts across those tasks. Third, the application: an in-context rewrite of a new source prompt, with no access to evaluation data for the new task.[^a8] The paper's contribution is the combination, and the text I read does not isolate the value of each part.

## Limits

The anchors are themselves search results. The calibration step that finds each anchor prompt is an evolutionary search guided by evaluation and reflection, described as "an evaluation-guided, reflection-driven, island-based prompt search."[^a9] The transferred mapping therefore inherits whatever the search misses: a weak anchor makes a weak mapping, and the paper does not report how the mapping degrades when anchors are poor (my inference).

Coverage is stated as a limit by the authors: "Our transfer effects are learned from standard tasks and model families; coverage" may be weaker where "may diminish for niche domains or rapidly updated model APIs."[^a10] An unseen task far from the alignment tasks, or a model whose API changes after calibration, is outside what the text establishes.

Cost is not removed. "Prompt evolution incurs nontrivial" compute.[^a11] The method saves the per-task re-optimization but still pays for the anchor search on each source–target pair, which the paper presents as an amortized cost. Whether the amortization pays off at a given number of tasks is not measured in the text I read.

The scope is instructions only. The paper "currently focuses on optimizing instructions alone, omitting exemplar or" few-shot demonstration optimization.[^a12] A prompt whose effect lives in its examples may not be transferred this way, and the text gives no evidence either way.

The reported gains are on code and agentic benchmarks. The 27.39% figure is from a single transfer direction shown in the introduction. I did not read the ablations, so claims about which component matters most are not checked here.

## Related

- [[model-drifting]] — the gap this mapping is meant to close; the anchor pairs are the paper's measurement of that gap on alignment tasks.
- [[evolutionary-prompt-search]] — the search that produces each anchor prompt in this paper is a reflective, island-based variant of the same family of population search.
- [[model-prompt-matching-bias]] — ensembling over several prompts and backbones is another response to the same mismatch: aggregate across readers rather than map one reader's prompt onto another.

[^a1]: arxiv-2512-01420 — "requires only a small set of alignment tasks for calibration"
[^a2]: arxiv-2512-01420 — "distills the consistent prompt-level adjustments required"
[^a3]: arxiv-2512-01420 — "This distilled summary constitutes the transferable knowledge, describing how task-optimal prompts for the source model"
[^a4]: arxiv-2512-01420 — "given a source-model prompt, this mapping directly produces an optimized prompt for the target model"
[^a5]: arxiv-2512-01420 — "PromptBridge yields a 27.39% improvement on SWE-Bench"
[^a6]: arxiv-2512-01420 — "consistently reduces the transfer gap and maintains or improves performance while substantially"
[^a7]: arxiv-2512-01420 — "the performance of the true task-optimal target-model prompt"
[^a8]: arxiv-2512-01420 — "transformation is applied to unseen tasks"
[^a9]: arxiv-2512-01420 — "an evaluation-guided, reflection-driven, island-based prompt search"
[^a10]: arxiv-2512-01420 — "Our transfer effects are learned from standard tasks and model families; coverage may diminish for niche domains or rapidly updated model APIs."
[^a11]: arxiv-2512-01420 — "Prompt evolution incurs nontrivial"
[^a12]: arxiv-2512-01420 — "PromptBridge currently focuses on optimizing instructions alone, omitting exemplar or"
