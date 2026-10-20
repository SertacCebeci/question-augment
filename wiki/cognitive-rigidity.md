---
description: "Hypothesized cause of overconfidence on multi-solution tasks: reasoning locks early onto one narrow path, read via error correction, new-solution discovery and attention entropy."
aliases: ["cognitive-rigidity hypothesis", "premature convergence on a narrow reasoning path"]
sources: ["arxiv-2512-01725"]
---
# Cognitive rigidity

The cognitive-rigidity hypothesis is the authors' account of why reasoning
overconfidence occurs. It says overconfidence "arises when the reasoning
process prematurely converges on a narrow set of thought paths."[^c1] The
claim concerns a state of the reasoning process, not a single wrong answer:
once a chain has settled on an initial set, it stops looking for
alternatives. The authors name the state directly: "a state where Short-CoT
locks the model into a narrow search space."[^c2]

**Behavioural signature.** Rigidity is read from what a model does when it
is given a chance to revise. Short-CoT shows "extremely low error correction
and new solution discovery rates."[^c3] Even when prompted to reconsider, "the
model is largely unable to identify its previous errors or explore new,
correct paths."[^c4] Long-CoT is "far more capable of self-correction and
discovery."[^c5] These are rates over a fixed ground-truth solution set, so
they count recovered answers, not the model's self-report.

**Internal proxy.** The authors take attention entropy as the internal
measure: "Following Cui et al. [10], we treat attention entropy as a proxy
for internal diversity."[^c6] They compute layer-wise entropy for Qwen3-8B
under Short-CoT and under the lower-overconfidence Long-CoT setting and
describe three phases. In shallow layers the entropies differ and then
converge. In the core reasoning layers (15–30), the lower-overconfidence
paradigm keeps "higher entropy than high-ROC counterparts."[^c7] In deep
layers (about 35) "the trend reverses; high-ROC paradigms" end with greater
entropy. The authors' reading of the reversal is post hoc: "The final
reversal strengthens this interpretation."[^c8]

**Interventions.** Two manipulations are reported as breaking the lock. Extra
reflection rounds: "reflection exposes otherwise overlooked solutions and
thus decreases ROC."[^c9] An exploratory cue appended to a Short-CoT answer,
namely "Wait, there may be other solutions.",[^c10] after which "the added
exploration frees the model from cognitive rigidity and" yields more correct
answers.[^c11] The same cue's effect on overconfidence itself is smaller:
"ROC also drops slightly, as shown in Figure 13 in Appendix."[^c12]

## Limits

- The hypothesis is preliminary by the authors' own description. The
  attention analysis "offers preliminary support for this view."[^c13]
- The proxy is imported. Attention entropy was used as a measure of diversity
  in work on reinforcement-learning entropy, and the paper adopts it for
  reasoning traces. What survives the transfer is a measurable layer pattern.
  What does not is shown here: that entropy spread across attention in a
  layer counts distinct reasoning paths. The paper gives no test linking the
  layer entropy to the solutions a model recovers (my inference).
- One model. The entropy figure is "Attention entropy of Short-CoT vs.
  Long-CoT on Qwen3-8B."[^c14]
- Rigidity is inferred from behaviour and entropy, not manipulated directly.
  The two interventions are the only causal handles, and the cue's effect on
  overconfidence is described as slight.
- The result is on enumeration tasks with bounded solution spaces (see
  [[reasoning-overconfidence]] for the limits of that setting).
- Reading the two results together (my reading): a shift that is imposed from
  outside helps, while the spontaneous shifts measured elsewhere are rare and
  accompany lower accuracy. The two agree that a shift is not automatically
  useful; they differ on whether it helps when induced.

## Related

- [[reasoning-overconfidence]] — the phenomenon this hypothesis is offered to
  explain
- [[retrieval-state-lock-in]] — the retrieval analogue: samples agree on a
  wrong answer because they share one wrong state, a lock-in outside the
  reasoning trace (my reading)
- [[self-repair-anchoring]] — retrying from one's own failed attempt reproduces
  near-identical code, a rigid retry in another setting (my reading)
- [[spontaneous-reasoning-shift-illusion]] — spontaneous mid-trace shifts are
  rare and accompany lower accuracy; the cue here is imposed from outside
- [[entropy-gated-forced-reconsideration]] — an appended reconsideration cue
  gated by token entropy, tested on single-answer math
- [[attention-entropy-ambiguity-signature]] — the same attention-entropy
  measure, read as prompt ambiguity rather than internal diversity

[^c1]: arxiv-2512-01725 — "when the reasoning process prematurely converges on a narrow set of thought paths"
[^c2]: arxiv-2512-01725 — "a state where Short-CoT locks the model into a narrow search space"
[^c3]: arxiv-2512-01725 — "extremely low error correction and new solution discovery rates"
[^c4]: arxiv-2512-01725 — "model is largely unable to identify its previous errors or explore new, correct paths"
[^c5]: arxiv-2512-01725 — "far more capable of self-correction and discovery"
[^c6]: arxiv-2512-01725 — "Following Cui et al. [10], we treat attention entropy as a proxy for internal diversity."
[^c7]: arxiv-2512-01725 — "higher entropy than high-ROC counterparts."
[^c8]: arxiv-2512-01725 — "The final reversal strengthens this interpretation"
[^c9]: arxiv-2512-01725 — "reflection exposes otherwise overlooked solutions and thus decreases ROC"
[^c10]: arxiv-2512-01725 — "Wait, there may be other solutions."
[^c11]: arxiv-2512-01725 — "The added exploration frees the model from cognitive rigidity and"
[^c12]: arxiv-2512-01725 — "ROC also drops slightly, as shown in Figure 13 in Appendix."
[^c13]: arxiv-2512-01725 — "analysis offers preliminary support for this view"
[^c14]: arxiv-2512-01725 — "Attention entropy of Short-CoT vs. Long-CoT on Qwen3-8B"
