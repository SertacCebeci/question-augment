---
description: "When a reasoner re-consults its visual source mid-chain is a timing decision that accuracy reward does not teach; tying lookups to uncertainty markers in the text beat plain RL on four benchmarks."
aliases: ["when-to-look", "perception timing", "strategic perception", "think longer, see less"]
sources: ["arxiv-2512-17227"]
---
# Strategic perception timing

A reasoner that holds an image can go back to it at many points in a chain. Which part of the image to consult is one question; when to consult it is another. Yang et al. treat the second as a separate skill, one that training does not supply by default. Their starting observation is that long chains erode the source: "models increasingly lose visual grounding, ultimately defaulting to degenerate solutions."[^c1] They attribute this to the reward. Standard reinforcement learning on answer accuracy "not explicitly penalize[s] visual disengagement," so a policy can reach the answer with little looking.[^c2] The paper's name for the phenomenon is "think longer, see less."[^c15]

The concept is that the timing of a look is a policy variable. It can be learned from the state of the reasoning rather than fixed in advance. Fixed placement is the alternative the paper rejects. Supervised training on looks inserted at teacher-chosen positions teaches the structure of grounded reasoning, but the resulting model "merely imitates the fixed perception schedule of the teacher, lacking strategic" autonomy.[^c13] In their ablation, the grounded-data SFT alone "provides no average gain" over the text-only cold start, and the paper reads this as the same point: "teaching perceptual structure without strategic timing" can hurt reasoning fluency.[^c16][^c12]

## How the timing is rewarded

The work adds a reward term on the looks themselves, separate from the answer reward. Each look is paired with the sentence just before it. The reward asks whether that sentence carries a marker of cognitive uncertainty or re-examination, the kind of word that signals "wait," "verify," or a change of step. The paper states the coupling as "coupling perceptual actions to linguistic markers" of uncertainty.[^c3] The score is the share of looks anchored to such a sentence: "is then defined as the proportion of perception actions that are anchored to a preceding pivotal."[^c4] The keyword list is hand-built: "we curate a comprehensive lexicon of reasoning-pivotal keywords."[^c6]

A raw share can be gamed, so the paper caps how much of the coupling counts. The authors note that rewarding the share alone could give "a degenerate policy that overfits to these keywords."[^c5] The cap is a regularizer on the excess coupling above a set ratio.

What the concept is, apart from this recipe, is the separation of two decisions: what the looks show, and when they happen. The paper's own numbers say the second is what the accuracy reward misses. On four benchmarks ("MathVista MathVision WeMath MathVerse Avg."[^c7]), plain RL from the same cold-start checkpoint gained about "averaging +2.6 points."[^c8] Adding the timing reward gave "(+5.3 over Cold Start)."[^c9] The gain is largest on the two visual benchmarks: "pronounced on MathVision and MathVerse, benchmarks."[^c10] The authors conclude that "conventional rewards cannot effectively teach strategic perception timing."[^c11]

## Limits

- The decay itself is taken from prior work and from the paper's framing. In the sections read, the paper does not measure how grounding falls with chain length, so "think longer, see less" is a premise of the work rather than a result of it.
- The timing signal is a proxy. The authors "operationalize the hypothesis that strategic perception should" follow metacognitive signals.[^c14] Whether the markers track uncertainty, rather than merely co-occurring with looks, is not tested in the text read.
- The lexicon is hand-curated, and the full list sits in the supplementary material, which was not read. Whether a different lexicon gives the same gain is not shown.
- Every result is for a multimodal model trained with RL on math and diagram benchmarks. The gains are single averages, and no spread across seeds is reported in the sections read. Nothing here concerns human askers or answerers.
- The reward is one of several components, and the ablation changes only the timing term against the same cold start. Its effect on the other components was not isolated.

On the answerer's side, the same question can be put to a person: at which step should one return to the source? That transfer is my inference. The paper does not test it, and a model's chain and a reader's reasoning differ in ways the text does not address.

## Related

- [[cot-hallucination-trap]] — reasoning decouples from the image when grounding is weak; this note concerns when the grounding is re-entered during the chain, the timing side of that decoupling.
- [[sufficiency-gated-imagination]] — also gates when to call a visual resource, but to generate new views rather than to re-consult the view already given.
- [[question-conditioned-evidence-acquisition]] — asks, each turn, what visual evidence the question still needs; the same timing question, asked at each step of an agent's loop.

[^c1]: arxiv-2512-17227 — "models increasingly lose visual grounding, ultimately defaulting to degenerate solutions"
[^c2]: arxiv-2512-17227 — "not explicitly penalize visual disengagement"
[^c3]: arxiv-2512-17227 — "coupling perceptual actions to linguistic markers"
[^c4]: arxiv-2512-17227 — "is then defined as the proportion of perception actions that are anchored to a preceding pivotal"
[^c5]: arxiv-2512-17227 — "that overfits to these keywords"
[^c6]: arxiv-2512-17227 — "we curate a comprehensive lexicon of reasoning-pivotal keywords"
[^c7]: arxiv-2512-17227 — "MathVista MathVision WeMath MathVerse Avg."
[^c8]: arxiv-2512-17227 — "averaging +2.6 points"
[^c9]: arxiv-2512-17227 — "(+5.3 over Cold Start)"
[^c10]: arxiv-2512-17227 — "pronounced on MathVision and MathVerse, benchmarks"
[^c11]: arxiv-2512-17227 — "cannot effectively teach strategic perception timing"
[^c12]: arxiv-2512-17227 — "teaching perceptual structure without strategic timing"
[^c13]: arxiv-2512-17227 — "fixed perception schedule of the teacher, lacking strategic"
[^c14]: arxiv-2512-17227 — "operationalize the hypothesis that strategic perception should"
[^c15]: arxiv-2512-17227 — "think longer, see less"
[^c16]: arxiv-2512-17227 — "PG-CoT data alone provides no"
