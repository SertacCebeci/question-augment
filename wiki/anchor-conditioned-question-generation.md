---
description: "A question generator that samples 0 to 5 human-labelled examples per batch as in-context demonstrations; zero examples reverts to ungrounded self-play, and the anchors are meant to damp drift."
aliases: ["few-shot grounded challenger", "anchor-grounded challenger", "human-anchor in-context generation", "k-anchor question generation"]
sources: ["arxiv-2512-02472"]
---
# Anchor-conditioned question generation

A self-play question generator, the Challenger, normally writes its tasks from its own weights alone. The variant here keeps a small pool of human-labelled examples, the anchors, and at each rollout step draws a number k between zero and five of them into the prompt as in-context demonstrations. The rule is stated directly: "the Challenger dynamically samples zero to five anchor examples as in-context example to guide synthetic question generation."[^c1] The count k is part of the design. At k = 0 the generator is the ungrounded self-play setting, and for k above zero "the Challenger is softly guided toward human-consistent reasoning trajectories" while it still produces its own items.[^c2]

The anchors enter a second place, the Challenger's reward. A term measures the cosine similarity between a generated question and the anchor distribution in embedding space, and the paper says this "encourages the Challenger to explore in the vicinity of real human data."[^c3] The rest of the reward pushes toward questions the Solver finds neither trivial nor impossible. The paper describes the target as questions that are "moderately (“medium”) uncertain" and that "lie at the edge of the Solver's current abilities."[^c4] The anchor term and the uncertainty term are separate pressures: one keeps the questions near human-labelled material, the other keeps them at the frontier.

The motivation is two failure modes the paper names for unguided self-play. The first is concept drift: "Without external intervention or guidance, models tend to reinforce their own knowledge bias."[^c5] The second is diversity collapse, where self-generated challenges "converge toward familiar and low-entropy regions of the task space."[^c6] A fixed anchor pool gives the generator a reference that does not move with the model's own output, which is the mechanism the paper proposes against both. The paper's summary is that "R-Few mitigates drift, yielding more stable and controllable co-evolutionary dynamics."[^c7]

One feature separates this from retrieval-style demonstration choice. The k anchors are drawn at random each step, not picked for similarity to the target. The paper does not argue for selection; it treats the pool as a regulariser on the generator's distribution. Compare [[demonstration-label-consistency]], where demonstrations are chosen so that their label share matches the query's. Here the question is not which demonstration best fits, but how much a fixed human prior should weigh on what the generator writes at all. That reading is mine, not the paper's.

Evidence is an ablation on Qwen3-8B-Base. Removing challenger training gives the largest drop of the three components tested (Math 71.0 to 68.0 in the paper's Table 2), and the authors conclude that "disabling challenger training causes the largest degradation."[^c8] The stability claim is supported in the paper by training curves: its Figure 1 caption says the method "delays the performance plateau seen in R-Zero and achieves higher performance."[^c9]

## Limits

- The stability and drift claim rests on curves and on final scores. The text I read does not define drift as a measured quantity; the plateau is used as its proxy. Whether the anchors cause less drift, as opposed to a better-tuned curriculum, is not separated by the ablation, which removes the challenger as a whole rather than only its anchors.
- The ablation is one model at one data ratio, and the gaps are one to three points. The paper itself notes that "math benchmarks exhibit larger performance" variance across methods.[^c10] Small differences in averages need more runs than the text reports.
- The method needs a pool of correct, labelled examples. The anchors are drawn from WebInstruct at 1% to 5% of its 232k items. Without a labelled pool the premise of anchoring is absent, and the paper does not test an unlabelled or synthetic pool. This limit is my inference from the design.
- The abstract compares against General-Reasoner, which was trained on about 20 times more human data. That comparison is of data volume. It does not isolate whether the anchoring mechanism, rather than the data scale of the anchors, accounts for the gain.
- The exact form of the anchor-alignment term is partly garbled in the extracted text, so I have not verified its weighting or normalisation. I have stated only the purpose the paper gives for it.
- Whether random k-sampling beats selected or retrieved demonstrations was not tested in the text I read.

## Related

- [[uncertainty-peaked-challenge-reward]] — the challenger reward shape and the solver's success-band filter that this generator is trained against
- [[pretraining-grounded-rubric-self-play]] — grounds the generator and the grader in one sampled document, not in in-context demonstrations
- [[curriculum-collapse]] — the diversity collapse that anchors are meant to damp; that note addresses it with a cross-iteration coverage reward instead
- [[demonstration-label-consistency]] — how in-context demonstrations are chosen; this generator draws its anchors at random
- [[self-evolving-visual-questioner]] — a different guard on self-generated questions: a frozen rewriter filters them rather than a fixed human pool conditioning them

[^c1]: arxiv-2512-02472 — "the Challenger dynamically samples zero to five anchor examples"
[^c2]: arxiv-2512-02472 — "the Challenger is softly guided toward human-consistent reasoning trajectories"
[^c3]: arxiv-2512-02472 — "This term encourages the Challenger to explore in the vicinity of real human data"
[^c4]: arxiv-2512-02472 — "uncertain questions that lie at the"
[^c5]: arxiv-2512-02472 — "Without external intervention or guidance, models tend to reinforce their own knowledge bias."
[^c6]: arxiv-2512-02472 — "converge toward familiar and low-entropy regions of the task space"
[^c7]: arxiv-2512-02472 — "mitigates drift, yielding more stable and controllable co-evolutionary dynamics"
[^c8]: arxiv-2512-02472 — "disabling challenger training causes the largest degradation"
[^c9]: arxiv-2512-02472 — "the performance plateau seen in R-Zero and achieves higher performance"
[^c10]: arxiv-2512-02472 — "math benchmarks exhibit larger performance"
