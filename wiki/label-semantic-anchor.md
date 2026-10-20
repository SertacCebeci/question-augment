---
description: "Pretrained label meanings (POS, NEG) resist few-shot inversion: with flipped demonstrations, 1–12B models never answer correctly under the inverted mapping, so the override rate is zero."
aliases: ["semantic anchor", "semantic anchors", "semantic override rate", "semantic override"]
sources: ["arxiv-2511-21038", "arxiv-2511-21752"]
---
# Label semantic anchor

A label word in a few-shot prompt is not a neutral symbol. POS, NEG, ENTAILMENT and their kin arrive with meanings the model acquired in pretraining, and the question is whether labelled demonstrations can overwrite those meanings. The test the paper uses is inversion: take demonstrations whose labels are systematically swapped (for sentiment, POS and NEG exchanged; for NLI, a cycle ENTAILMENT → NEUTRAL → CONTRADICTION → ENTAILMENT) and see whether the model comes to apply the inverted rule.[^c1] The pretrained meaning of a label token is what the paper calls a semantic anchor: a constraint that a prompt can adjust but, at these scales, not replace.

The measured quantity is the semantic override rate. It is the probability that a prediction is both correct under the true label and consistent with the inverted mapping, under inverted demonstrations.[^c2] The rate separates two things a plain accuracy score runs together. A model can follow the demonstrated labels without being right, and it can be right without following them. The override rate counts only the case where both hold, which is the case that would show a model had learned an anti-semantic classifier.

The result is that the case does not occur. Across eight tasks and eight open-source models of 1–12B parameters, the paper finds that inverted demonstrations do not yield a coherent anti-semantic classifier: "models cannot learn coherent anti-semantic classifiers".[^c3] The override rate is not small but zero: "the semantic override rate is zero, not near-zero".[^c4] In the sentiment tasks roughly half of predictions match the demonstrated, wrong labels, yet "No examples simultaneously satisfy both the true label and the inverted mapping."[^c5] The paper's reading is that the model is pulled between two constraints and satisfies neither well: "The model cannot reconcile conflicting constraints (demonstrated mappings versus semantic priors), producing incoherent outputs that satisfy neither."[^c6]

The same anchor is what makes natural demonstrations work. With correct labels, accuracy rises and the predictions stay coupled to the zero-shot behaviour; the paper reads ICL as adjusting "how inputs project onto stable semantic directions learned during pre-training" rather than redefining them.[^c7] Its summary is that "The semantic anchors encoded in tokens like POS, NEG, and ENTAILMENT form rigid constraints that few-shot prompting cannot overcome."[^c8]

Two further observations place the anchor in time. The failure grows with the number of inverted examples: "each additional inverted example strengthens the contradiction between demonstrated and" the pretrained semantics.[^c9] And the paper situates its result against earlier work in which flipped labels were followed only at large scale: "requires massive scale: GPT-3 can eventually flip labels,".[^c10]

A reading for asking, which is mine and not the paper's: a question that tries to make a familiar word mean its opposite is working against the word's pretrained meaning, and the paper's numbers suggest that the answerer will keep the familiar meaning even when the context states the reverse. Whether the same holds for a context that defines a term explicitly, rather than through labelled examples, the paper does not test.

## Limits

- The override rate is defined for binary tasks. The paper says it evaluates "the semantic override rate for binary tasks."[^c11] The headline claim covers all eight tasks, but the zero-rate measurement is on the binary subset, and the NLI tasks are three-way.
- The shots tested are few: one to eight demonstrations, with five seeds. The claim is about the few-shot regime, not many-shot prompting; the paper's related-work section cites a many-shot study that "showed that even many-shot regimes (hundreds of examples) struggle with semantic override".[^c12]
- The scale is 1–12B. The paper's conclusion is explicitly open on this: "test whether this constraint is specific to semantically loaded labels" is left to future work, so arbitrary symbol-to-concept mappings are not shown to behave the same way.
- The "geometric interpretation" of rigid label regions in the representation manifold is offered as a suggestion: "our results suggest a geometric interpretation." No geometry is measured here.
- The result is in tension with another wiki note. [[anchoring-strength]] reports that two in-context examples redefining a sign flipped frontier models on arithmetic. That is a different task, a different scale, and a redefinition rather than a label inversion, so the two results are not reconciled by this paper.
- The paper measures prediction behaviour on classification benchmarks with greedy decoding. It does not test generation, open-ended answers, or whether the zero rate reflects an internal representation.
- Arbitrary label words are not settled by this paper. In a defence setting, [[alias-label-remapping]] reports that some models partly learn unrelated alias pairs from a few examples, and that for unaligned pairs "Regression Counts dominate" for nearly all models.[^c13][^c14] That is new assignment of words, not inversion of a familiar one, so it does not contradict the zero override rate; it shows that the boundary of the anchor claim is not yet mapped.

## Related

- [[anchoring-strength]] — a scalar competition between in-context cues and a prior; its frontier flips are the contrasting case noted under Limits.
- [[demonstration-label-consistency]] — the share of demonstrations carrying the query's label; inversion sets that share against the truth, which is where the override rate lives.
- [[icl-alignment-decomposition]] — the three-way agreement measure that isolates the override rate as a joint term.
- [[alias-label-remapping]] — the same question in a defence setting: arbitrary label words taught by a few examples, where the aligned/unaligned split decides whether the new mapping helps.

[^c1]: arxiv-2511-21038 — "Inverted demonstrations apply a permutation"
[^c2]: arxiv-2511-21038
[^c3]: arxiv-2511-21038 — "models cannot learn coherent anti-semantic classifiers"
[^c4]: arxiv-2511-21038 — "the semantic override rate is zero, not near-zero"
[^c5]: arxiv-2511-21038 — "No examples simultaneously satisfy both the true label and the inverted mapping."
[^c6]: arxiv-2511-21038 — "The model cannot reconcile conflicting constraints (demonstrated mappings versus semantic priors), producing"
[^c7]: arxiv-2511-21038 — "ICL primarily adjusts how inputs project onto stable"
[^c8]: arxiv-2511-21038 — "The semantic anchors encoded in tokens like POS, NEG, and ENTAILMENT form"
[^c9]: arxiv-2511-21038 — "each additional inverted example strengthens the contradiction between demonstrated and"
[^c10]: arxiv-2511-21038 — "requires massive scale: GPT-3 can eventually flip labels,"
[^c11]: arxiv-2511-21038 — "We evaluate the three alignment metrics plus the semantic override rate for binary tasks."
[^c12]: arxiv-2511-21038 — "showed that even many-shot regimes (hundreds of examples) struggle with semantic override"
[^c13]: arxiv-2511-21752 — "suggesting that it can partially adapt to this alias"
[^c14]: arxiv-2511-21752 — "Regression Counts dominate"
