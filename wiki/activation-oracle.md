---
description: "A model trained to answer arbitrary questions about injected LLM activations, in natural language, recovers facts absent from its input text, such as knowledge only fine-tuning put in the weights."
aliases: ["LatentQA", "activation verbalizer", "activation verbalization", "latent question answering", "AO"]
sources: ["arxiv-2512-15674"]
---
# Activation oracle

An activation oracle (AO) is a language model that receives two kinds of input at once: ordinary text, and one or more activation vectors taken from a target LLM. It is trained to answer natural-language questions about those vectors.[^c1] The target's activations are placed into placeholder tokens of the oracle prompt, together with the layer number and the question, so the oracle reads the question and the injected state in the same forward pass.

The injection is a steering-style addition. After an early layer, the hidden state at each placeholder is changed by adding a vector whose length equals the original hidden state's length, pointing in the direction of the injected activation. "This normmatching ensures that activations of varying provenance are automatically scaled to a consistent magnitude."[^c2] The authors chose addition over replacement: "we add rather than replace because we observed that direct replacement caused excessive growth of the activation norm during training."[^c3]

The name LatentQA is the older term for the general task (Pan et al.). The AO is a generalist version of it, trained on three kinds of data: a system-prompt question-answering set taken from Pan et al., seven binary classification tasks turned into yes/no questions over activations near the end of a sequence,[^c4] and a self-supervised context prediction task (see [[self-supervised-context-prediction]]). The training set is about one million examples, and each oracle is trained on activations from its own base instruct model and then applied to fine-tuned variants of that model without further training.[^c5]

What the work measured. On three secret-keeping auditing games (Taboo, User Gender, and a secret side constraint), the oracle is given activations from prompts that never mention the secret and is asked one direct question. The authors report that "we achieve 21% accuracy on Taboo secret-keeping compared to just 4% for the best" interpretability baseline; on the side-constraint task the gain is smaller, "such as achieving 59% versus 52% accuracy".[^c6] In a model-diffing setting, the oracle receives the activation difference between a base and a fine-tuned model, with one fixed open-ended prompt and no per-task tuning; the prior baseline (ADL) needed tuning. On the rubric used, "Both methods obtain an average score of 2/5."[^c7] On PersonaQA, where a fine-tuned model is shown only a persona's name, accuracy rose "from about 5% for the base model to approximately 14%" with the full mixture.[^c8]

The mechanism claim is narrow. The oracle answers about content present in the activations and absent from the text; the authors read the gain as extraction of "some signal from information that exists only in the model" (its weights).[^c17] The worry it is tested against is that such a model merely inverts the input text. A PersonaQA prompt contains only the persona's name, so text inversion has little to recover.[^c9] For the wiki's purposes the transferable point is that an answer can come from a source other than the text being asked about (my reading).

## Limits

The paper studies self-application: its oracles explain the activations of the model they were trained on.[^c10] Their answers are not calibrated. The authors note the oracle is not trained to express uncertainty, so it produces an answer even when confidence is low.[^c11] On hallucination detection, the authors found that simple prompting baselines did well, so the activation route did not clearly beat them on that task.[^c15]

The evaluation is narrow. The authors say their evaluation "focuses primarily on auditing game benchmarks," and their fine-tunes are narrow: "Our experiments use narrow fine-tunes that modify" the base model along few dimensions, so realistic post-trained systems were not tested.[^c16][^c12] On PersonaQA the absolute accuracy of the open models stays low, and for the Claude model the configurations are within error of each other.[^c13] The authors say the approach trades mechanistic understanding for a question-answer interface, and that "it sacrifices the ability to drill down into mechanisms" that other methods offer.[^c14][^c18]

[^c15]: arxiv-2512-15674 — "baselines achieve strong performance on hallucination detection in practice"
[^c16]: arxiv-2512-15674 — "Our evaluation focuses primarily on auditing game benchmarks"
[^c17]: arxiv-2512-15674 — "some signal from information that exists only in the model"
[^c18]: arxiv-2512-15674 — "it sacrifices the ability to drill down into mechanisms"

## Related

- [[mean-difference-steering-vector]] — the injection is an addition to a hidden state like steering, but the injected vector is a raw activation, not a contrast direction.
- [[verbalization-incompleteness-versus-unfaithfulness]] — both ask what a model's own state says beyond what it states in text; here the answer is read from activations rather than from the chain of thought.
- [[probe-revealed-hidden-influence]] — a second route to information the model does not state, by asking after the fact.
- [[nonlinear-hidden-state-probe]] — a trained readout of hidden states for one fixed label; an AO takes free-form questions instead.

[^c1]: arxiv-2512-15674 — "to answer arbitrary natural-language questions about LLM activations"
[^c2]: arxiv-2512-15674 — "This normmatching ensures that activations of varying provenance are automatically scaled to a consistent"
[^c3]: arxiv-2512-15674 — "we add rather than replace because we observed that direct replacement caused excessive growth of"
[^c4]: arxiv-2512-15674 — "We adapt 7 existing binary classification tasks into natural language yes/no"
[^c5]: arxiv-2512-15674 — "trained on activations from its base instruct model and applied to audit either that same model or"
[^c6]: arxiv-2512-15674 — "we achieve 21% accuracy on Taboo secret-keeping compared to just 4% for the best"
[^c7]: arxiv-2512-15674 — "Both methods obtain an average score of 2/5"
[^c8]: arxiv-2512-15674 — "accuracy increases from about 5% for the base model to approximately 14%"
[^c9]: arxiv-2512-15674 — "The input text contains only the persona"
[^c10]: arxiv-2512-15674 — "We focus on a model explaining its own"
[^c11]: arxiv-2512-15674 — "trained to express uncertainty, it will frequently produce an answer even when confidence is low"
[^c12]: arxiv-2512-15674 — "Our experiments use narrow fine-tunes that modify"
[^c13]: arxiv-2512-15674 — "though all training configurations perform within error of each other"
[^c14]: arxiv-2512-15674 — "Activation Oracles trade mechanistic understanding for simpler"
