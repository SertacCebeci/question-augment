---
description: "Restating the original question, pinned in view, with every new observation counters drift in long agentic search; removing it costs accuracy, less so after fine-tuning."
aliases: ["intent injection", "query re-anchoring", "query pinning"]
sources: ["doi-10-48550-arxiv-2604-09508"]
---
# Intent re-anchoring

In a long chain of search steps, each retrieved result enters the context and pushes earlier material out of view. The original question is among the things that get buried. Intent re-anchoring is the counter: the question is kept in the window the model reads, and it is restated alongside each new observation, so the next step is chosen against the question and not against the most recent result.

The VISOR system for agentic visual retrieval-augmented generation implements this in two parts. The original query is "persistently pinned at the top, ensuring that all cross-page findings" gathered so far stay visible at every turn.[^c1] Separately, every system-returned observation carries an Intent Injection prompt, and "This prompt explicitly restates the original" query and points the model back to its accumulated findings instead of letting it reason from scratch.[^c2] The target is a failure the authors describe as the agent's "attention drifts away from the original query," so that retrievals and actions "progressively deviate from user intent."[^c3]

The effect is measured by ablation, on a 7B backbone: "ablation studies are conducted using Qwen2.5-VL-7B backbone on" the benchmarks.[^c4] Without Intent Injection the model "lacks explicit query re-anchoring at each interaction turn," and "This leads to a noticeable performance drop on both benchmarks."[^c5] The gap shrinks after fine-tuning, which the authors read as Intent Injection being "an architectural inductive bias that guides untrained models toward query-aligned" reasoning, still giving "a consistent (though reduced) benefit in fine-tuned settings."[^c6]

The mechanism, as far as it can be stated from the paper, is placement: the question is kept in the text the model attends to on each turn rather than left to be recalled from earlier context. Whether a person who re-reads their own question partway through a long investigation gets the same benefit is not tested; that transfer is my inference.

## Limits

- Everything measured here is one system, VISOR, evaluated on ViDoSeek, SlideVQA and MMLongBench: "Extensive experiments on ViDoSeek, SlideVQA, and MMLongBench" are the paper's test sets.[^c7] No human asker or answerer was studied.
- The ablation removes Intent Injection together with an evidence space and a sliding window. My reading is that the paper credits the modules jointly, so the share due to re-anchoring alone is not cleanly separated, though the removal of the query restatement is reported on its own.
- The gap "narrows" after fine-tuning but does not vanish. A model trained to keep its query in view may gain little from being reminded of it; the paper does not test that boundary further.
- The paper's related claim concerns a different object. When building training trajectories, the authors kept the original question in searches because a reformulated query "may omit key details from the original question due to intent drift."[^c8] That is about the search queries an agent emits, not about restating the question to the model. The two are separate, and the note keeps them apart.
- Intent stated in a prompt can also pull output away from the evidence, not toward it. The hallucination study in [[non-monotonic-prompt-pressure-hallucination]] shows a model aligning its output with "the suggestive or coercive intent embedded in the user prompt." Re-anchoring helps only when the anchored question is the right one; the paper does not address a wrong anchor.

## Related

- [[query-discipline]] — the same drift seen across a chain of queries: successive queries that repeat or pivot predict accuracy there, while here the question itself is what has to stay in view.
- [[non-monotonic-prompt-pressure-hallucination]] — the opposite risk of prompt-stated intent: it can pull the answer off the evidence instead of keeping it on the question.

[^c1]: doi-10-48550-arxiv-2604-09508 — "persistently pinned at the top, ensuring that all cross-page findings"
[^c2]: doi-10-48550-arxiv-2604-09508 — "This prompt explicitly restates the original"
[^c3]: doi-10-48550-arxiv-2604-09508 — "attention drifts away from the original query"
[^c4]: doi-10-48550-arxiv-2604-09508 — "ablation studies are conducted using Qwen2.5-VL-7B backbone on"
[^c5]: doi-10-48550-arxiv-2604-09508 — "This leads to a noticeable performance drop on both benchmarks"
[^c6]: doi-10-48550-arxiv-2604-09508 — "inductive bias that guides untrained models toward query-aligned"
[^c7]: doi-10-48550-arxiv-2604-09508 — "Extensive experiments on ViDoSeek, SlideVQA, and MMLongBench"
[^c8]: doi-10-48550-arxiv-2604-09508 — "may omit key details from the original question due to intent drift"
