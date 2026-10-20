---
description: "Evaluator-free selection picks, from N sampled outputs, the one at the centroid of the dominant lexical-similarity cluster, generalizing majority vote to open-ended text."
aliases: ["Mode Extraction", "ModeX", "evaluator-free best-of-N", "modal output selection", "graph centroid selection"]
sources: ["arxiv-2601-02535"]
---
# Modal-centroid selection

Given N samples from one prompt, a selector can choose one output without a judge by treating the samples as nodes of a graph. Each edge weight is a lexical similarity: the sum of Jaccard overlaps over unigram, bigram and trigram sets.[^c2] Near-paraphrases are therefore strongly tied and unrelated outputs weakly tied. The graph is cut recursively by its Fiedler vector. A cut is accepted only while its conductance stays below a threshold, which the paper sets to τ = 0.8.[^c6] When the recursion stops, the surviving cluster is searched for the node with the largest weighted degree, and that node is the output.[^c7]

The construction is a soft version of majority voting. For a closed answer set, responses that pick the same option form a clique and the largest clique is the vote.[^c3] Open-ended text has no exact equality, so the paper replaces the clique with a weighted graph and the count with a degree. The premise is that high-quality generations "tend to form coherent clusters in the semantic space," while errors look like sparse outliers.[^c4] The selected output is therefore the modal one, and not, in the paper's words, "the most extreme or longest" response.[^c5] Rejected summaries in the paper's CNN/DailyMail example "often omit important" keywords and repeat themselves.[^c8] That is one example, shown qualitatively.

Two results carry the claim. The first concerns timing: on math with Qwen-7B, high-quality candidates can be told apart from partial generations, "even when less than 50% of the full" trajectory exists.[^c9] This is the basis of the ModeX-Lite variant, which prunes early. The second concerns the baseline: across summarization, code and math, the authors report that "our approaches consistently outperform standard" single- and multi-path baselines,[^c17] and that ModeX exceeds "the gold standard Best-of-N that requires external" evaluators at times.[^c12]

The theory treats the two steps as mode estimation. Theorem 1 says the spectral bipartition separates modes when the distribution is supported on pieces "separated by a region of low density".[^c10] Theorem 2 says the weighted degree "is proportional to the Kernel Density Estimator" of the sample density.[^c11] Read together, the cluster isolates one dominant region and the degree picks the density peak inside it. The paper's own point is that this replaces exact-match counting with continuous density estimation.

## Limits

- The similarity is lexical. The paper concedes the metric "may fail to recognize valid paraphrases" that differ in surface form, and so may reject correct but differently worded outputs.[^c13] Its embedding-based comparison (Table 3) does not show the n-gram version winning every column. By my reading of the table rows, SentenceBERT leads on Rouge-2 and code BLEU.
- The method assumes the most frequent output is correct.[^c14] Where the model has a systematic error, the centroid will reinforce it. The paper calls this a fault of the target model rather than of ModeX, and leaves the mitigation to future work. This is the same failure that majority voting has.
- The consistency theorem is stated in the limit of many samples. The experiments use far fewer, and the Best-of-16 baseline is the reference point.[^c15] Whether the mode is recovered at N = 16 is shown empirically, not proved. This is my inference from the statement.
- Theorem 2 treats cosine or Jaccard scores as a kernel and calls the degree proportional to a density estimate. A similarity score is not a normalized density, and I did not verify the appendix argument that bridges the two. This is my inference, not a result I checked.
- The modal-point argument is about the distribution, but the output is the sample with the highest degree, which is an approximation by construction.[^c16]
- The evidence covers three task families with one model family for the early-pruning figure. Figure 4 is a single model and task.

## Related

- [[verification-weighted-voting]] — the same weakness of plain majority voting: frequent answers can be wrong. Modal-centroid selection inherits the frequency assumption and does not address it.
- [[supervised-cross-model-consensus]] — a learned agreement rule over answers from several models. Modal-centroid selection is unsupervised and uses one model's own samples.
- [[self-consistency-difficulty-score]] — uses the same sample agreement, but as a difficulty signal for question selection, not as a rule for picking an output.

[^c2]: arxiv-2601-02535 — "similarity computed over unigram, bigram, and"
[^c3]: arxiv-2601-02535 — "responses selecting the same choice form a clique"
[^c4]: arxiv-2601-02535 — "tend to form coherent clusters in the semantic space"
[^c5]: arxiv-2601-02535 — "output is often not the most extreme or longest"
[^c6]: arxiv-2601-02535 — "we set the conductance threshold to"
[^c7]: arxiv-2601-02535 — "centroid as the node with the maximum weighted"
[^c8]: arxiv-2601-02535 — "rejected summaries often omit important"
[^c9]: arxiv-2601-02535 — "even when less than 50% of the full"
[^c10]: arxiv-2601-02535 — "separated by a region of low density"
[^c11]: arxiv-2601-02535 — "is proportional to the Kernel Density Estimator"
[^c12]: arxiv-2601-02535 — "the gold standard Best-of-N that requires external"
[^c13]: arxiv-2601-02535 — "metric may fail to recognize valid paraphrases"
[^c14]: arxiv-2601-02535 — "assumption that the most frequent output is correct"
[^c15]: arxiv-2601-02535 — "Best-of-16 (Gold Standard)"
[^c16]: arxiv-2601-02535 — "the generation process draws samples from a"
[^c17]: arxiv-2601-02535 — "our approaches consistently outperform standard"
