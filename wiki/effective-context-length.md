---
description: "Advertised context windows overstate usable capacity: accuracy near 80% at 32K tokens falls at 128K and 200K, unevenly across models, so context must be measured at the size used."
aliases: ["effective context length", "usable context", "context length claims", "context window utilization"]
sources: ["arxiv-2601-08847", "arxiv-2512-12989", "arxiv-2512-02445"]
---
# Effective context length

A model's advertised context window is a vendor claim about how much text it accepts, not a measure of how much of that text it uses. RIKER tests the gap directly by putting the whole corpus in the prompt and asking questions about it at several sizes: "We evaluate 33 models at 32K context, 24 models at 128K context, and 11 models at 200K context".[^c1] The paper's framing is that "Models frequently advertise 128K or 200K token context windows", and that "these claims overstate usable capacity".[^c2]

The measured drop is concrete. "Top-tier models achieve over 80% accuracy at 32K tokens", but the drop at longer sizes is uneven. Among the top-tier models, "Top-tier models (Qwen3, GLM-4.5 family) lose 10-16% accuracy from 32K to 200K", while "Llama models degrade 13 - 23% from 32K to 128K", which the paper calls consistently worse than other families. The worst case is a collapse: "GLM-4.6 collapses from 70.9% accuracy at 128K to 26.6% at 200K", even though the model nominally supports both lengths.[^c3]

The paper's conclusion is a distinction between two quantities: "marketed context length should not be conflated with effective context length".[^c4] The effective length is a property of the model on a task, measured at the size that will be used. A specification does not supply it.

The same logic reaches agents, where the size that matters includes the history the agent keeps. In a coding-migration study, reducing only one model's served window from 128K to 32K, with the same weights and budgets, "lowers full passes from 36/40 to 4/40 across the two conditions"; the authors explain that "Retained history competes with the next response for the context window".[^c8][^c9] The window the model is served with is therefore part of what an agent result measures. The aggregation tier degrades faster, so the effective length for multi-document questions can be shorter than the one for single-document extraction; this links to [[aggregation-extraction-gap]].[^c5]

Padding that carries no evidence also degrades agents. In an AgentHarm extension with up to 200K tokens of padding, models advertised at 1M to 2M tokens "degrade severely already at 100K tokens" on benign and harmful tasks alike.[^c11] Placement changed the rate: "placing padding before the task description slows" degradation relative to placing it after, and the authors offer the attention-distance account as what "likely occurs", not as something they measured.[^c12][^c13] The kind of padding also mattered, with a reported order of "higher scores for non-relevant padding, followed by relevant padding, then random, and finally multi-task" padding.[^c14] My inference from these results is that a single effective length per model understates the case: where the instruction sits and what fills the context both move the number. The mechanism behind the placement effect is the paper's conjecture.

## Limits

The agent-side ablation changes one model's served window and nothing else, and its authors say it does not establish the "minimum context needed to solve the task".[^c10] It is one model on one task, and the other configurations in that study differ in quantization, sampling and engine, so no general window threshold follows.

The architecture tested is pure context-stuffing. The paper says that "Future work will test retrieval-augmented generation and agentic retrieval patterns", so the effective length under retrieval is not measured here.[^c6]

Coverage shrinks as the context grows (33 models at 32K, 24 at 128K, 11 at 200K), so the comparison at 200K rests on a different and smaller set. The paper accepts this: "as fewer models support longer contexts" is, it says, itself a finding, but it weakens any claim about the 200K column as a population estimate.

The threshold of "significant degradation beyond 32K" is the paper's summary of a table, not a fitted breakpoint. The 32K results also contain an anomaly, which the authors attribute to measurement: "The 32K anomaly is most likely a test measurement limitation".[^c7] Some models are simply absent at 200K for architectural reasons. The effective length here is a per-model, per-task result on one synthetic enterprise corpus, not a law.

The results also sit uneasily with a different measurement. The sibling note [[context-cost-accuracy-decoupling]] reports accuracy holding under padding for several models. The two results measure different things, padding with irrelevant text versus a multi-document task over a fixed corpus, and reconciling them is my inference, not something either paper does.

## Related

- [[aggregation-extraction-gap]] — the multi-document questions that degrade faster as context grows.
- [[context-cost-accuracy-decoupling]] — the padding result that the RIKER degradation must be reconciled with.
- [[dispersed-evidence-retrieval-collapse]] — retrieval over a whole corpus, the alternative that the paper leaves untested.
- [[padding-refusal-drift]] — the same long-context agent runs read through refusal rates, which move in opposite directions across models.

[^c1]: arxiv-2601-08847 — "We evaluate 33 models at 32K context, 24 models at 128K context, and 11 models at 200K context"
[^c2]: arxiv-2601-08847 — "Models frequently advertise 128K or 200K token context windows"
[^c3]: arxiv-2601-08847 — "GLM-4.6 collapses from 70.9% accuracy at 128K to 26.6% at 200K"
[^c4]: arxiv-2601-08847 — "marketed context length should not be conflated with effective context length"
[^c5]: arxiv-2601-08847 — "Aggregation degrades faster with context"
[^c6]: arxiv-2601-08847 — "Future work will test retrieval-augmented generation and agentic retrieval patterns"
[^c7]: arxiv-2601-08847 — "The 32K anomaly is most likely a test measurement limitation"
[^c8]: arxiv-2512-12989 — "lowers full passes from 36/40 to 4/40 across the two conditions"
[^c9]: arxiv-2512-12989 — "Retained history competes with the next response for the context window"
[^c10]: arxiv-2512-12989 — "minimum context needed to solve the task"
[^c11]: arxiv-2512-02445 — "degrade severely already at 100K tokens"
[^c12]: arxiv-2512-02445 — "placing padding before the task description slows"
[^c13]: arxiv-2512-02445 — "This likely occurs"
[^c14]: arxiv-2512-02445 — "higher scores for non-relevant padding, followed by relevant padding, then random, and finally multi-task"
