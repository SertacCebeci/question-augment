---
description: "Multi-turn degradation is argued to be an intent gap, not a capability gap; rewriting the vague context into an explicit instruction using the user's history recovers about 20 points."
aliases: ["intent mismatch in multi-turn conversation", "Mediator-Assistant architecture", "intent alignment gap"]
sources: ["arxiv-2602-07338"]
---
# History-conditioned intent reconstruction

In the "Lost in Conversation" setup, a fully specified instruction is split into shards revealed over turns, and models lose roughly 30% of performance against the single-turn version.[^c1] The prior reading blames unreliability. This work argues the cause is an intent alignment gap: the user's utterance is a lossy, many-to-one compression of the intent, so the intent stays uncertain given the context alone.[^c2]

## The argument

When the missing constraints are absent from the context, a frozen model falls back on its pretraining prior and solves for the intent of the "average user".[^c3] The authors argue that scaling only sharpens the fit to that average, so the gap to the specific individual stays as a constant penalty.[^c4] Their support is a reanalysis of the earlier benchmark: relative degradation stays near 60% across model sizes and families.[^c5] A model such as DeepSeek-V3.2-Thinking also stays degraded, which the authors take to mean reasoning cannot fill an information vacuum.[^c6] The entropy argument is the authors' own framing, not a proof in the formal sense, and the constancy across models is a reanalysis, not a controlled test.

## The intervention

A Mediator sits before the execution Assistant. It reads the accumulated context and a per-user set of experiences, and outputs a fully specified instruction that the Assistant then answers.[^c7] The experiences come from a Refiner that compares a failed trajectory with a successful one for the same task, drawn from the user's past reformulation attempts, and distils explicit rules; no weights are updated.[^c8] A rule example in the figure is "Ignore AI responses unless the user approves", which targets the failure where a fragmentary continuation is read as confirmation of the model's earlier guess.

## What was measured

- Gains are about 20 points in average performance and 15 points in reliability across backbones; for the reasoning model the gain is 21.1%.[^c9]
- Reliability rises with performance, so the earlier variance is attributed to intent ambiguity rather than sampling noise.[^c10]
- Remembering is not resolving: on GPT-4o-mini, Mem0 raises the sharded average only from 53.6% to 56.5%, summarization to 54.7%, the Mediator to 73.9%, against 86.9% for the full single-turn instruction.[^c11]
- Putting raw contrastive pairs in the prompt matches accuracy but costs 3.6x the tokens of the distilled rules.[^c12]

For asking and answering, the claim is that the information to answer is often present in the history; what is missing is a statement of how the user means it to apply now. Making that statement explicit, before answering, does work that more model capacity does not.

## Limits

- Evidence comes from one benchmark family with simulated passive users; the authors say its user logic is "relatively homogeneous".[^c13]
- The Refiner is few-shot and heuristic, coarse-grained; per-user personalization beyond the benchmark was not tested.
- The reconstruction uses past successful and failed trajectories of the same task instance; whether this works for a new user or task with no history is not shown (my inference from the design).
- The "scaling cannot help" claim rests on a conceptual entropy argument plus reanalysis; no scaling experiment isolates it.
- It does not compare against asking the user a clarifying question; the authors set that aside as conflicting with expectations of quick provisional answers.

## Related

- [[contextual-inertia]] — another account of why multi-turn answers hold onto a wrong earlier reading
- [[underspecified-question-eager-answering]] — the model's habit of answering from an assumed reading rather than asking
- [[query-to-question-reformulation]] — rewriting a vague input into an explicit one before answering
- [[ambiguity-versus-incapability-routing]] — separating missing information from missing ability

[^c1]: arxiv-2602-07338 — "revealing a substantial performance degradation of approximately 30%"
[^c2]: arxiv-2602-07338 — "the mapping from intent to utterance is many-to-one"
[^c3]: arxiv-2602-07338 — "a frozen LLM Pθ tends to revert to its training priors"
[^c4]: arxiv-2602-07338 — "rendering the ambiguity strictly unresolvable via scaling alone"
[^c5]: arxiv-2602-07338 — "the relative performance degradation between fully specified and underspecified settings remains remarkably constant (approximately 60%)"
[^c6]: arxiv-2602-07338 — "it cannot “reason” its way out of an information vacuum"
[^c7]: arxiv-2602-07338 — "The Assistant A then generates the response based on this low-entropy input"
[^c8]: arxiv-2602-07338 — "enabling the system to bridge the alignment gap and adapt to individual user behaviors without the need for weight updates"
[^c9]: arxiv-2602-07338 — "our approach secures a 21.1% increase"
[^c10]: arxiv-2602-07338 — "the previously observed instability stemmed primarily from intent ambiguity rather than intrinsic model stochasticity"
[^c11]: arxiv-2602-07338 — "w/ Mem0 yields only marginal gains over the baseline (53.6% → 56.5%)"
[^c12]: arxiv-2602-07338 — "it consumes 3.6× more tokens"
[^c13]: arxiv-2602-07338 — "the multi-turn settings in current benchmarks exhibit relatively homogeneous user logic"
