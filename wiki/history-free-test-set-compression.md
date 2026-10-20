---
description: "Picks a representative evaluation subset from raw test items alone, using a domain-tuned model's embeddings and clustering, so no history of other models' scores is needed."
aliases: ["history-free test set compression", "cold-start benchmark compression", "test set compression"]
sources: ["arxiv-2601-03272"]
---
# History-free test set compression

A benchmark's items can be cut to a fraction of their number without any record of how models scored on them. The method has three steps. First, a base LLM is fully fine-tuned on a small domain set, here 3GPP telecom QA, so that it comes to "internalize task-relevant semantics" of that domain.[^c1] Second, each raw test question is passed through the tuned model with a domain system prompt, and the last hidden state is L2-normalized as the item's embedding. Third, the embeddings are clustered with K-means (K = 100); each cluster is split into five equal-width distance bands from its centroid, and 10% of items are sampled from each band, so that "typical" core items and "challenging" boundary items both survive.[^c2]

The input is item text, not model outcomes, because of the cold-start case. Earlier compressors such as tinyBenchmarks and metabench "propose compressing existing benchmarks into smaller, more informative subsets"[^c3], but they need "the performance profiles of numerous pre-existing models on the full benchmark."[^c4] A new domain or a new model has no such profiles. Here the selection uses geometry alone; the model's knowledge enters only through the fine-tuned embeddings. The abstract claims this "reduc[es] evaluation cost by over 90% while preserving high fidelity."[^c5]

What was measured: on the 3GPP test split (109,043 items, Qwen3-1.7B tuned on the training split), the 10% subset was compared with the full set across "five distinct large language models (LLMs)."[^c6] For the base model, the tuned-embedding subset gave 0.5505 against 0.54 on the full set (+1.94%), while the un-tuned-embedding subset gave 0.5303 (-1.80%).[^c7] For the fine-tuned model, the tuned-embedding subset gave 0.7252 against 0.7134, while the un-tuned-embedding subset gave 0.7772, a stated bias of +8.94%.[^c8] The conclusion reports a Spearman correlation of 0.98 between subset and full rankings.[^c9]

So the thing that changes how a benchmark is built is the choice of what to keep: a stratified draw in a task-tuned embedding space, instead of a random draw or a draw that needs old model scores. The fidelity is a result on this benchmark at this ratio, not a general rule.

## Limits

- The comparator is clustering with un-tuned embeddings. The text also calls it "random baseline sampling"[^c10], but no random draw appears in the table, so the gain is shown against one specific alternative, not against chance.
- One domain (3GPP telecom QA), one base model family (Qwen3-1.7B), five evaluated models. No second benchmark is reported in the sections read.
- The Spearman 0.98 appears only in the conclusion. The experiment section gives per-model accuracies; I did not find a rank table there (my reading).
- The text says the tuned subset is "just 1.65% below the fullset result"[^c11], but 0.7252 is above 0.7134 and the table's Δ column carries no sign. The direction of that result is unclear as written.
- No repeated draws or seed spread are reported in what I read. A 1–2% gap from one subset draw is weak evidence that one sampler beats another; see [[minimum-detectable-effect]] for the resolution a subset-versus-full gap must exceed.
- The 10% ratio comes from the redundancy diagnostic (see [[cluster-geometry-redundancy-diagnostic]]); other ratios are not tested for fidelity in the sections read.
- The contamination use is a proposal, not a measurement: "A significant performance drop on Tgen versus Tcomp signals potential test-set contamination."[^c12]

## Related

- [[cluster-geometry-redundancy-diagnostic]] — the "Dataset X-ray" step that sets how hard the cut is
- [[difficulty-enriched-item-sampling]] — sampling items by a reference model's failures confounds cross-model scores; this method uses no model outcomes, but it does not show the subset's difficulty matches the full set beyond rank agreement
- [[questioning-diversity]] — a per-item embedding redundancy score for generated questions; the benchmark-level analogue is the clustering here

[^c1]: arxiv-2601-03272 — "to internalize task-relevant semantics"
[^c2]: arxiv-2601-03272 — "five equal-sized distance intervals from the centroid and sampled 10% of the samples from each interval"
[^c3]: arxiv-2601-03272 — "propose compressing existing benchmarks into smaller, more informative subsets"
[^c4]: arxiv-2601-03272 — "the performance profiles of numerous pre-existing models on the"
[^c5]: arxiv-2601-03272 — "reducing evaluation cost by over 90% while preserving high fidelity"
[^c6]: arxiv-2601-03272 — "across five distinct large language models (LLMs)"
[^c7]: arxiv-2601-03272 — "SFT Sampling improves accuracy from 0.5400 to"
[^c8]: arxiv-2601-03272 — "baseline sampling introduces a large positive bias of +8.94%"
[^c9]: arxiv-2601-03272 — "rankings with a Spearman correlation of 0.98"
[^c10]: arxiv-2601-03272 — "random baseline sampling"
[^c11]: arxiv-2601-03272 — "just 1.65% below the fullset result"
[^c12]: arxiv-2601-03272 — "A significant performance drop on Tgen versus Tcomp signals potential test-set contamination"
