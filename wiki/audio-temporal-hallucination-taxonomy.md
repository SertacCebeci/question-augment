---
description: "Four error types for answers about temporal audio: event omission, false event identity, temporal relation error, quantitative temporal error, each naming the grounding it breaks."
aliases: ["audio hallucination taxonomy", "AHA taxonomy", "four-dimension temporal audio hallucination taxonomy"]
sources: ["arxiv-2512-24052"]
---
# Audio temporal hallucination taxonomy

Answers about sound over time can go wrong in four distinct ways. The paper introduces the four as "a four-category taxonomy of hallucinations that captures the dominant and practically actionable errors exhibited by contemporary LALMs."[^t1] Each type is defined by the part of the audio's structure that the answer gets wrong, so that a wrong answer can be scored by what it broke rather than only marked wrong.

- **Event omission.** "The model fails to mention perceptible events present in the audio."[^t2] The paper ties this to "attention bias toward high-energy events":[^t3] a faint sound before a loud one drops out of the answer.
- **False event identity.** The answer either invents an event that is not present, or gives an existing event the wrong label. The paper says both "reflect errors in mapping acoustic evidence to semantic labels."[^t4]
- **Temporal relation error.** The answer gets the relations between events wrong: "it swaps the chronological order, or misstates causal/sequence relations."[^t5] This is the order and causation of events, not their presence.
- **Quantitative temporal error.** The answer errs on "quantitative temporal attributes: incorrect counts of" repeated events, or on which of two events is longer.[^t6] This is counting and duration arithmetic.

The four are tied to question families. The question templates are grouped into explicit temporal ordering, temporal logic and counterfactual reasoning, and "Temporal counting and duration comparison,"[^t7] and "each question qi is associated with one or more hallucination types."[^t8] A type is therefore a property of the question, which says which kind of grounding it probes, and of an answer that fails it. The paper says the taxonomy "aligns closely with the controlled perturbations introduced by our data generation pipeline, enabling precise attribution."[^t9] Because the same taxonomy labels the generated wrong answers and the evaluation items, a per-type error rate is a measure of one specific kind of failure.

The paper reports that the base model fails on all four. It shows "an Omission Rate over 40%"[^t10] for its base model, and says that "Gemini and GPT-4o exceed 74% in Event Omission rates."[^t11] These are rates on the paper's own generated questions, so they describe the taxonomy's items, not general audio use.

## Limits

- The four categories are the authors' selection from failures they observed on their own question set. The text gives no argument that they cover all temporal audio errors; the claim is that they are the dominant and actionable ones. My inference: other failure kinds, such as errors about a sound's source or loudness, fall outside the taxonomy and would be scored as something else or missed.
- The types are assigned by the construction: the question template and the ground-truth caption determine which error is possible. An answer is not classified by an independent reader of the audio. The text I read reports no agreement rate for the type labels.
- The audio is drawn from one corpus, AudioTime, and the generation pipeline works on "caption-level representations that serve as a proxy for acoustic input."[^t12] Whether the four types appear in the same proportions on natural audio is not tested.
- The rates quoted are for models the paper chose to test, one of which it trained. The text does not show that the taxonomy predicts which answers a deployed user would find harmful.

## Related

- [[counterfactual-hard-negative]] — the rejected answers used for training are generated one per type of this taxonomy.
- [[controlled-error-injection]] — another construction that places a known error of a chosen kind, so that the error's type is known by construction.
- [[hallucination-diagnosis-task]] — a separate typed-hallucination framing; the two are not compared in the text read here.

[^t1]: arxiv-2512-24052 — "hallucinations that captures the dominant and practically actionable errors exhibited by contemporary"
[^t2]: arxiv-2512-24052 — "The model fails to mention perceptible events present in the audio"
[^t3]: arxiv-2512-24052 — "attention bias toward high-energy events"
[^t4]: arxiv-2512-24052 — "mapping acoustic evidence to semantic labels"
[^t5]: arxiv-2512-24052 — "it swaps the chronological order, or misstates causal/sequence relations"
[^t6]: arxiv-2512-24052 — "quantitative temporal attributes: incorrect counts of"
[^t7]: arxiv-2512-24052 — "Temporal counting and duration comparison"
[^t8]: arxiv-2512-24052 — "question qi is associated with one or more hallucination types"
[^t9]: arxiv-2512-24052 — "controlled perturbations introduced by our data"
[^t10]: arxiv-2512-24052 — "showing an Omission Rate over 40% and"
[^t11]: arxiv-2512-24052 — "Gemini and GPT-4o exceed 74% in Event Omission rates"
[^t12]: arxiv-2512-24052 — "caption-level representations that serve as a proxy for acoustic input"
