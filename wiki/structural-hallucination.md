---
description: "Hallucination as a consequence of a generator that must always emit a continuation, so reward changes reach only its surface, not the mechanism that produces fabrication."
aliases: ["architectural hallucination", "structural hallucination thesis", "hallucination as architectural inevitability"]
sources: ["arxiv-2512-14801"]
---
# Structural hallucination

Structural hallucination is the claim that fabrication follows from what a generative model is, not from how it was rewarded. The paper sets it against an incentive account. In September 2025 OpenAI "released a widely discussed paper"[^c11] whose account is that hallucinations "arise when models are penalized equally for abstaining and for being incorrect."[^c1] On that account a reward that stops penalising abstention should reduce fabrication. The structural account denies that the choice exists in the first place.

The argument starts from the generator's design. A transformer "has no internal mechanism for withholding output."[^c2] Every query, answerable or not, receives a token sequence, so the behaviour a benchmark calls guessing is not chosen against an alternative: "It simply computes the next token."[^c3] The paper's summary is that hallucination is "a structural consequence of the transformer architecture"[^c4] and not a miscalibration that rewards could fix.

The mechanism it gives runs through the learned space. That space is "a shadow structure formed by linguistic cooccurrence rather than by the structure of the world."[^c5] Where the learned patterns are dense an answer looks accurate; where they are sparse the model interpolates, as described in [[ontological-boundary-condition]]. What makes the thesis structural rather than a claim about data is the absence of an internal signal of ignorance. Abstention is therefore "an epistemic act but a learned linguistic pattern, triggered by contexts that resemble prior abstention cues."[^c6] A reward can teach the pattern to fire more often, but it cannot give the model access to the fact that would tell it when to fire.

The paper's remedy follows from the diagnosis. Refusal has to be produced by something that is not the generator, as in [[externalized-abstention-gate]]. The thesis also concedes what rewards do change: "incentives affect outputs but do not correct the underlying mechanism generating hallucination."[^c7] The dispute is therefore about mechanism, not about whether reward moves refusal rates.

## Limits

- The thesis is argued from architecture. Its empirical support is the Licensing Oracle results of an earlier paper, which the text cites as "empirical confirmation of this diagnosis."[^c8] The thesis is not tested in this text, and the results it relies on come from a validator added to the model, not from a model whose architecture is varied.
- The contrast does not isolate architecture from training. The Oracle experiment compares a transformer alone with a transformer plus an external module. The paper says "The Oracle does not change the model."[^c9] That shows the external module works; it does not vary the training objective with the architecture held fixed. My inference.
- The claim is universal: "No incentive mechanism can modify this structural dependence on pattern completion."[^c10] One trained system in which a reward-side change produces refusal that tracks the model's own correctness would falsify it as stated. The wiki's [[abstention]] note records refusal rising to most of a policy's outputs under a refusal-heavy reward. That moves refusal, which the paper concedes, but it does not show refusal tracking truth; neither the paper nor that note tests the question. My reading.
- "Pseudo-ontology" and "shadow structure" are the paper's metaphors. No embedding geometry is measured in the text. My inference.
- The argument is for a generator trained on next-token prediction. Systems with retrieval or tool use, where a non-generative component already sits in the loop, are outside the scope the paper states. My inference.

## Related

- [[ontological-boundary-condition]] — the place in the learned space where the structural account locates fabrication
- [[externalized-abstention-gate]] — the paper's remedy: a validator outside the generator that is allowed to refuse
- [[abstention]] — refusal as a named output; the structural claim is that the generator cannot produce it from inside
- [[training-density-citation-fabrication-gradient]] — a measured ordering of citation fabrication that the structural account predicts; its density mechanism is inferred, not tested

[^c1]: arxiv-2512-14801 — "arise when models are penalized equally for abstaining and for being incorrect"
[^c2]: arxiv-2512-14801 — "its design has no internal mechanism for withholding output"
[^c3]: arxiv-2512-14801 — "It simply computes the next token."
[^c4]: arxiv-2512-14801 — "a structural consequence of the transformer architecture"
[^c5]: arxiv-2512-14801 — "a shadow structure formed by linguistic cooccurrence rather than by the structure of the world"
[^c6]: arxiv-2512-14801 — "epistemic act but a learned linguistic pattern, triggered by contexts that resemble prior abstention cues"
[^c7]: arxiv-2512-14801 — "incentives affect outputs but do not correct the underlying mechanism generating hallucination"
[^c8]: arxiv-2512-14801 — "empirical confirmation of this diagnosis"
[^c9]: arxiv-2512-14801 — "The Oracle does not change the model."
[^c10]: arxiv-2512-14801 — "No incentive mechanism can modify this structural dependence on pattern completion."
[^c11]: arxiv-2512-14801 — "In September 2025, OpenAI released a widely discussed paper"
