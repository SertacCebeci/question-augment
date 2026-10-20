---
description: "In Llama-3-8B, retrieved context lowers measured social bias across 13 types, while adding chain-of-thought on top raises it again: accuracy and fairness move apart."
aliases: ["RAG fairness-accuracy tradeoff", "CoT bias amplification in RAG"]
sources: ["arxiv-2602-09442"]
---
# RAG bias reduction versus CoT bias increase

Parihar and Cheng compare bias scores of one model before and after retrieval augmentation, holding the rest of a standard RAG pipeline fixed so that the retrieval effect can be isolated. Their headline result is that standard RAG "generally reduces social bias across multiple bias evaluation datasets and metrics, retrieval datasets, LLMs, task types, and bias types".[^c1] In one table, 9 of 10 bias types fall, and the reduction holds for both retrieval corpora (WikiText-103 and C4).[^c2]

Their proposed mechanism is correlational. Before RAG, bias scores correlate negatively with female-oriented content and neutral or positive regard in the response (for example -0.52 for gender-female and -0.54 for neutral regard). The authors read this as diverse external context diluting stereotype-driven completions.[^c3]

Adding chain-of-thought reverses the direction. "RAG with CoT produces higher bias scores across both WikiText-103 and C4 retrieval databases."[^c4] CoT also strengthens the correlation between bias and toxicity (0.59 versus 0.14 before RAG). The authors interpret this as explicit step-by-step justification reinforcing stereotypical associations, in contrast to RAG, which "dilutes biases through contextual diversity".[^c5] The RAG benefit does not vanish under CoT. Regard-negative correlation falls from 0.51 to 0.29 after retrieval even with CoT on.[^c6] The paper frames the combination as a fairness-accuracy tradeoff: CoT raises accuracy and bias together.[^c7]

For someone asking or answering, the claim is that adding more context and adding more deliberation are separate levers on bias, with opposite signs in this setting, and that an accuracy gain from reasoning cannot be taken as evidence of fairer answers.

## Limits

- The demonstration model is a single 8B model (Llama-3-8B-Instruct), a second 7B model is reported in an appendix, and all experiments are "single run", so there are no variance estimates.[^c8]
- The mechanism is correlational (Pearson correlations between bias scores and response metrics). Nothing intervenes to show that diversity of context causes the reduction. The explanation is the authors' reading, not a tested cause.
- One dataset (SCW) shows a weaker, mixed effect: some types such as disability, nationality and socioeconomic status increased after RAG.[^c9]
- Corpora are generic (WikiText-103, C4), not adversarially biased. Earlier work cited in the paper found RAG can propagate bias from retrieved documents, so the reduction should not be assumed for biased corpora.
- Whether CoT raises bias because of reasoning itself or because of the prompt format was not separated.

## Related

- [[correctness-non-bias-utility-trilemma]] — a different, conjectural tension between correctness and non-bias; this note is an empirical accuracy-bias divergence
- [[parametric-knowledge-gates-retrieval-noise-damage]] — another case where retrieval effects depend on what the model already holds
- [[cot-reasoning-faithfulness-by-truncation]] — how the same paper checks that the CoT reflects the retrieved evidence

[^c1]: arxiv-2602-09442 — "Standard RAG generally reduces social bias across multiple"
[^c2]: arxiv-2602-09442 — "observe a reduction in the bias score (highlighted) in 9 out of 10 bias types"
[^c3]: arxiv-2602-09442 — "The Before RAG condition reveals strong negative correlations between bias scores and key dimensions: gender-female (-0.52), regard-neutral (-0.54), and"
[^c4]: arxiv-2602-09442 — "RAG with CoT produces higher bias scores across both WikiText-103 and"
[^c5]: arxiv-2602-09442 — "Unlike standard RAG, which dilutes biases through contextual diversity"
[^c6]: arxiv-2602-09442 — "regard-negative correlations decrease from 0.51 to 0.29 for WikiText-103 and 0.18 for C4"
[^c7]: arxiv-2602-09442 — "underscoring the fairness-accuracy tradeoff where increased correctness may"
[^c8]: arxiv-2602-09442 — "We conduct extensive experiments (all single run) using the demonstration model"
[^c9]: arxiv-2602-09442 — "socioeconomic status actually saw an increase in bias after applying RAG"
