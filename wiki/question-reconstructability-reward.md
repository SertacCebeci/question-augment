---
description: "Score a search trajectory by whether the original question can be reconstructed from it, masked of lexical shortcuts — informativeness without a gold answer."
aliases: ["Cycle-Consistent Search", "CCS", "cycle-consistency reward", "reconstructability reward"]
sources: ["arxiv-2604-12967", "arxiv-2512-11986", "arxiv-2511-23151"]
---
# Question-reconstructability reward

> A trajectory is informative exactly to the degree that the original question
> can be recovered from it — so recoverability, not a gold answer, is the
> reward.

## Definition / Mechanism

An, Yuan, Lee, Hsieh & Min (2026) train a search agent
without ground-truth answers by treating a search trajectory as a channel: a
question $q$ produces a trajectory $\tau$ (search actions and observations),
and the trajectory's quality is judged by how well a frozen reconstructor
$P_\phi$ can recover $q$ from it. "If $\tau$ contains the necessary and
sufficient evidence to resolve $q$, it should be possible to reconstruct $q$
solely from $\tau$. Formally, this establishes a cycle $q \to \tau \to
\hat q$, where the closeness between $q$ and $\hat q$ serves as a proxy for
the quality of the intermediate representation $\tau$, independent of
external supervision."[^c1]

The objective is cast as mutual information between the question and the
trajectory, $I(Q; T_\theta) = H(Q) - H(Q\mid T_\theta)$; since $H(Q)$ is fixed,
maximizing it reduces to maximizing $\mathbb E[\log P(q\mid\tau)]$, approximated
with the trained reconstructor.[^c2]

**Informativeness is not read off the raw trajectory.** A trajectory can
"encode $q$ into the action sequence through trivial lexical copying (e.g.,
by repeating the question in a search query or partially restating it in the
final response for context), allowing the reconstructor to recover $q$
without relying on the search results." The authors call this *information
leakage*: the reconstructor scores the channel, not the evidence, unless the
channel is first stripped of the shortcut. They apply a bottleneck $\psi =
\psi_{mask}\circ\psi_{trace}$ before reconstruction: $\psi_{trace}$ drops the
final answer step, and $\psi_{mask}$ replaces named entities in search
queries with generic type tags (e.g. "Burj Khalifa" → `[LOC]`), leaving
observations unmasked. "This operation substantially reduces the direct
lexical channel from actions to the question, forcing reconstruction to
resolve masked content primarily from evidence in $o_t$ rather than from
copied words in $a_t$."[^c4]

The reward for trajectory $\tau_i$ is the semantic similarity between $q$ and
the reconstruction $\hat q_i \sim P_\phi(\cdot\mid\psi(\tau_i))$, cosine
similarity of sentence embeddings, used as a GRPO group-relative advantage
with no separate critic and no gold answer anywhere in the loop.[^c5]

An ablation isolates what the bottleneck buys: reconstructing from the
unmasked trajectory (lexical shortcuts intact) scores 0.545–0.561 average,
reconstructing from observations alone scores 0.584, and the full masked-action
design scores 0.606 — "masked actions contribute more than simply removing
lexical leakage: they preserve useful structural intent that helps the
reconstructor interpret the observations within a specific investigative
context."[^c6]

## Why it matters

This is a way to judge whether an evidence-gathering process actually
constrains the unknown *without a labeled answer to check against*: adequacy
is operationalized as "can the question be recovered," and the informativeness
signal survives being turned into a trainable reward. The reported effect is
large enough to matter in practice — CCS "achieves performance comparable to
supervised methods while consistently outperforming competing methods without
gold supervision," on some backbones surpassing the gold-supervised baseline
outright.[^c7]

The same objective appears on a safety context rather than a search trajectory. In the ContextLens work, a generator is rewarded when a frozen decoder can rebuild the original prompt from its snippet and a partially visible prompt, and the authors describe the snippet as "the context snippet is considered as a high-bandwidth latent representation of the prompt."[^c9] Two details differ from the search case. The bottleneck is a segment, not a lexical mask: the prompt is split at a random point and only the longer part is shown to the decoder, as the rebuild target. The leakage control is a check, not a mask: because a generator can learn to copy the prompt into its snippet, the reward is set to 0 when the snippet contains the larger segment, so the authors "check whether the larger segment appears in the context snippet."[^c10] The reconstruction term is one part of a reward that also scores safety, and the ablation reports that removing the decoder term hurts most: "auto-encoder structure is essential for producing informative contexts that translate into improved safety performance."[^c11] See [[transferable-context-snippet]] for the design this term sits in.

A reconstruction term also appears in video temporal grounding, applied to the query rather than to a trajectory. Jung et al. (2025) add a term that is zero when the query is relevant. When the query is irrelevant to the video, the term "encourages the model to reconstruct the intended relevant query" from the video and the mismatched query, and scores the similarity between the rebuilt query and the original.[^c12] The reconstruction is therefore a comparison step: the model must find the mismatch to rebuild the query it should have been given. The term is applied only to irrelevant queries, and it is not a measure of whether the evidence covers the question; it measures whether the model can see what was changed. In the authors' ablation it added to F1 and explanation scores while keeping grounding accuracy, and the authors read this as "reconstructing the original relevant query enhances" fine-grained understanding.[^c13] The ablation was run on one benchmark: "All ablation studies and discussions are" conducted on HI-ActivityNet.[^c14] For the query side of the same logic, see [[hard-irrelevant-query]].

## Limits

- The proxy needs a second trained model — the reconstructor — and its own
  failure modes (miscalibration, its own shortcuts) are not characterized
  beyond the one leakage channel the authors control for (lexical copying);
  other reconstructor biases are unverified.
- The bottleneck removes two specific leakage channels (final response,
  entity-bearing actions); the authors do not claim it removes all shortcut
  paths, only that it beats not bottlenecking at all.
- Demonstrated only for knowledge-intensive, multi-hop question answering
  with a search-tool agent; the authors state the formulation "is developed
  in the context of knowledge-intensive question answering, where search
  trajectories can often be viewed as informative representations of user
  intent," and mark extension to "broader agentic settings" as future work,
  not shown here.[^c8]
- Reconstruction quality is a proxy, not identity: a trajectory could score
  well by supporting a plausible-but-wrong reconstruction if the
  reconstructor itself is fooled — the paper does not measure this failure
  mode directly.
- The safety setting uses a verbatim-segment check against copying. A snippet that paraphrases the prompt would pass that check while still leaking it, and the paper does not test paraphrase copying (my inference, not the paper's claim).

## Related

- [[mutual-information-paradigm]]
- [[conditional-entropy]]
- [[information-bottleneck]]
- [[expected-information-gain]]
- [[semantic-entropy]]
- [[transferable-context-snippet]] — the safety-context version of this reward: a generator's snippet is scored by how well a frozen decoder rebuilds the prompt from it
- [[hard-irrelevant-query]] — the query-side setting in which the video grounding paper's reconstruction term is applied

[^c1]: arxiv-2604-12967
[^c2]: arxiv-2604-12967 — "I(Q; Tθ ) = H(Q) − H(Q | Tθ )."
[^c4]: arxiv-2604-12967 — "This operation substantially reduces the direct lexical channel from actions to the question, forcing reconstruction to resolve masked content primarily from evidence in ot rather than from copied words in at ."
[^c5]: arxiv-2604-12967
[^c6]: arxiv-2604-12967 — "masked actions contribute more than simply removing lexical leakage: they preserve useful structural intent that helps the reconstructor interpret the observations within a specific investigative context."
[^c7]: arxiv-2604-12967 — "CCS achieves performance comparable to supervised methods while consistently outperforming competing methods without gold supervision."
[^c8]: arxiv-2604-12967 — "our formulation is developed in the context of knowledge-intensive question answering, where search trajectories can often be viewed as informative representations of user intent. Extending this idea to broader agentic settings remains an important direction for future work."
[^c9]: arxiv-2512-11986 — "the context snippet is considered as a high-bandwidth latent representation of the prompt"
[^c10]: arxiv-2512-11986 — "check whether the larger segment appears in the context snippet"
[^c11]: arxiv-2512-11986 — "auto-encoder structure is essential for producing informative contexts that translate into improved safety performance"
[^c12]: arxiv-2511-23151 — "encourages the model to reconstruct the intended relevant query"
[^c13]: arxiv-2511-23151 — "reconstructing the original relevant query enhances"
[^c14]: arxiv-2511-23151 — "All ablation studies and discussions are"
