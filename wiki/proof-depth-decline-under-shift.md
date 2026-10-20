---
description: "Accuracy on first-order deduction falls as the proof chain lengthens, and models trained on shallow chains lose most of it on deeper test chains; in-context learning alone was not enough."
aliases: ["proof-depth generalization", "reasoning-depth extrapolation", "depth-stratified deduction accuracy", "chain-length out-of-distribution decline"]
sources: ["arxiv-2512-10561"]
---
# Proof-depth decline under distribution shift

A deduction problem has a depth: the number of reasoning steps needed to derive the query from the facts and rules. The benchmark behind this work, SimpleLogic, makes depth the controlled variable. "It has 40,000 samples from depths 0 to 7, with 5,000 samples per depth."[^p1] The test sets then move past the training range. The natural-language test "manifests OOD by including deeper (up to 11)" chains, and the random-character test (lexical-cue-ablation) does the same.[^p2] The paper's own summary is that "both datasets manifested OOD by having deeper reasoning steps (8 to 11) than observed in the training data."[^p3]

What the measurement shows is a decline with depth. For fine-tuned models, "in the NL dataset, average accuracy gradually declines" as depth grows, while on the random-character set "in the NNL dataset, it drops sharply from 89% to 50% and then plateaus."[^p4][^p5] So the deepest chains, the ones outside the training range, are where the models are closest to chance. The depth-wise curves are the evidence here; the paper's figures show them for each fine-tuned model.

The same axis separates the architectures. The paper's claim is that the gap between encoder-based and decoder-only models "becomes wider as the reasoning chains in both scenarios become deeper."[^p6] For zero- and few-shot prompting the decline is also present. Most LLMs tested were brittle, and the paper concludes that "ICL alone is not an effective mechanism for causal reasoning."[^p7] Adding shots changed little: "in accuracy when increasing the number of shots from zero to five" was marginal, about half a point on average.[^p8] The exception is GPT-5, which "achieved 100% accuracy in both the NL and NNL" sets, at a cost in latency the paper calls substantial.[^p9]

A reading that the paper does not test directly, and that I hold as my inference: a model that has fit the depths it saw can still fail one step beyond them, because nothing in the training data fixes how the composition continues past the trained range. The depth axis is therefore a way to ask a question of a deduction system, not only a difficulty knob. Asking at depths above the training range shows whether the system composes steps or matches patterns it has seen.

The paper also gives an architectural account. Its hypothesis is that "will allow them to perform more reliable" causal composition under shift for encoders than for decoders, because an encoder layer lets every token see the whole sequence while a decoder reads left to right.[^p10] That account is covered in the Limits.

## Limits

- The depth is synthetic. The facts and rules are templated SimpleLogic clauses with no disjunction, and depth is counted in proof steps. Whether the same decline holds for proofs in open text, with real premises and ambiguous steps, is not tested.
- There is one extrapolation step: training on depths 0 to 7, testing up to 11. The shape of the decline beyond depth 11, or under training on deeper chains, is not measured.
- The architecture comparison is confounded. The fine-tuned models are small (BERT, BART, Flan-T5 Base, a 1.7B Qwen3), and the prompted models are large and varied. The paper's encoder-over-decoder argument is marked as informal: "In this section we provide an informal argument on how encoder layers could have an advantage".[^p11] The paper offers no ablation that holds size and training fixed.
- Prompting was tested with zero shots and up to five. Larger prompt sets, or chain-of-thought prompting of the same models, are not separated here.
- One reasoning model is an outlier. GPT-5 is near perfect at every depth, and the paper hypothesizes that this comes from "immense capacity and built-in chain-of-thought priors". Neither part of that explanation is tested.[^p12]

## Related

- [[local-correctness-without-global-composition]] — the same failure to compose locally correct steps into a correct whole, measured on structured answers rather than proofs
- lexical-cue-ablation — the random-character split, which steepens the depth decline for fine-tuned models
- [[symbolic-grounded-depth-gap]] — a different depth axis: path depth lost when a graph path is realized as text
- [[hop-depth-difficulty-with-entropy-check]] — depth set as a difficulty control for knowledge-graph questions, checked by a probe's entropy
- [[in-context-learning-as-label-propagation]] — a theory of what in-context examples do to the label; it does not address how a prompted model composes a long chain

[^p1]: arxiv-2512-10561 — "It has 40,000 samples from depths 0 to 7, with 5,000 samples per depth."
[^p2]: arxiv-2512-10561 — "manifests OOD by including deeper (up to 11)"
[^p3]: arxiv-2512-10561 — "both datasets manifested OOD by having deeper reasoning steps (8 to 11) than observed in the training data"
[^p4]: arxiv-2512-10561 — "in the NL dataset, average accuracy gradually declines"
[^p5]: arxiv-2512-10561 — "in the NNL dataset, it drops sharply from 89% to 50% and then plateaus"
[^p6]: arxiv-2512-10561 — "wider as the reasoning chains in both scenarios become deeper"
[^p7]: arxiv-2512-10561 — "We thus conclude that ICL alone is not an effective mechanism for causal reasoning."
[^p8]: arxiv-2512-10561 — "in accuracy when increasing the number of shots from zero to five"
[^p9]: arxiv-2512-10561 — "GPT-5 achieved 100% accuracy in both the NL and NNL"
[^p10]: arxiv-2512-10561 — "will allow them to perform more reliable"
[^p11]: arxiv-2512-10561 — "In this section we provide an informal argument on how encoder layers could have an advantage"
[^p12]: arxiv-2512-10561 — "immense capacity and built-in"
