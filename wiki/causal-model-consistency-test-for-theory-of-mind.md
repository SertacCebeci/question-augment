---
description: "A model has a theory of mind only if its mental-state model is coherent, abstract and consistent; GPT-4o passed coherence but failed cross-domain transfer and prediction-inference reciprocity."
aliases: ["coherence abstractness consistency", "ContainerWorld MovieWorld", "forward-inverse model consistency", "cognitively-grounded ToM evaluation"]
sources: ["arxiv-2602-12150"]
---
# Causal-model consistency test for theory of mind

Benchmarks that score a model against human answers cannot tell social proficiency from a theory of mind (ToM). The authors define ToM as a theory: a unified causal model of how mental states generate behavior, which must be coherent, abstract and consistent.[^c1] They test each property separately, and deliberately do not require the model's ToM to be human-like.

## The three properties and their tests

**Coherence.** Action predictions should follow a systematic combination of costs, desires and beliefs. In ContainerWorld (a character chooses a near box or a far basket, with beliefs, desires and fruit contents enumerated, 9 x 3 x 9 tuples) GPT-4o's next-token action distribution was compared with a rule-based HumanToM model and ablations that drop beliefs, desires or cost.[^c2] GPT-4o agreed most with HumanToM, even though a cost-only model would already be right most of the time (85% of human-like predictions are "box"). The authors read this as some core principles being followed.[^c3]

**Abstractness.** The same causal model should apply across surface domains. MovieWorld maps every ContainerWorld tuple one-to-one onto a film-festival choice (5-minute versus 90-minute screening, cost as time instead of effort).[^c4] Agreement with the candidate models fell, and GPT-4o's ContainerWorld action distribution did not reliably predict its MovieWorld one (r = .48).[^c5] For mental-state inferences, only belief inference transferred (r = .78); joint inference was weak (r = .39) and desire inference very weak (r = .18).[^c6]

**Consistency.** The forward model (mental states to action) and the inverse model (action to mental states) should be one model. Two checks: a "Bayesian evaluation" correlating GPT-4o's inferences with the Bayesian inversion of its own forward model, and a more generous "validity evaluation" asking whether an inferred mental state, fed to the forward model, reproduces the observed action.[^c7] GPT-4o failed to reach ceiling on both in both domains, so its predictions and its inferences are not drawn from one causal model.[^c8]

## Why this separates the two readings

Success on one task (coherence) coexisted with failure when the logic was relabeled and when predicting and explaining were required to agree. The authors' inference is that proficiency arises without a unified causal model, and that LLMs may build narrow, domain-specific models instead.[^c9] For asking and answering, the transferable point is that agreement between a model's answer to a question and its answer to the inverse question is a checkable property, independent of any ground truth. (This reading is mine.)

## Limits

- Only one model (GPT-4o, May 2024 snapshot, default temperature) and two tiny, fully enumerated paradigms were tested; the authors say generality to other LLMs is open and merely expected.[^c10]
- Probabilities are next-token distributions from a JSON-constrained prompt; that these equal the model's "confidence" is an assumption, and the cost change between paradigms (effort versus time) may itself explain the attenuation, as the authors concede.[^c11]
- No ceiling or human baseline is reported for the cross-domain correlations; "at or near ceiling" is a stipulated criterion, not a measured human value.
- Fragile belief-only transfer (r = .78) is left unexplained.
- Whether the Bayesian-inversion criterion is a fair demand of an LLM is questioned by the authors themselves, hence the validity metric.[^c12]

## Related

- [[planning-theory-of-mind-elicitation-gap]] — another argument that static ToM benchmarks can be passed without a causal model
- [[perturbed-false-belief-robustness]] — fragility of ToM success under task perturbation
- [[tom-uncertainty-score]] — a different ToM measurement for LLMs

[^c1]: arxiv-2602-12150 — "Critically, since"
[^c2]: arxiv-2602-12150 — "we generated all possible tuples of beliefs"
[^c3]: arxiv-2602-12150 — "it appears that GPT-4o follows some core principles of action"
[^c4]: arxiv-2602-12150 — "Since every behavior in ContainerWorld has a corresponding"
[^c5]: arxiv-2602-12150 — "ContainerWorld does not"
[^c6]: arxiv-2602-12150 — "we find that only beliefs are able to reliably predict"
[^c7]: arxiv-2602-12150 — "Crucially, this metric requires that a mental-state inference,"
[^c8]: arxiv-2602-12150 — "Taken together, these"
[^c9]: arxiv-2602-12150 — "LLMs, however, seem to achieve their social proficiency"
[^c10]: arxiv-2602-12150 — "One limitation of the current investigation is that we only"
[^c11]: arxiv-2602-12150 — "This likely stems from the change in cost representation –"
[^c12]: arxiv-2602-12150 — "Since this may not be the case, we also"
