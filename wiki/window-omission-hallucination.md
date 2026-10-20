---
description: "A window without the answer can be confidently wrong and win an uncertainty-based aggregation over the window that holds it; weighting windows by the information they add counters this."
aliases: ["fact omission", "fact omission in parallel windows", "uncertainty-driven omission", "missing-evidence window dominance"]
sources: ["doi-10-48550-arxiv-2412-14905"]
---
# Window omission hallucination

In parallel context extension, a window that does not contain the answer does not stay silent. The model still writes a distribution for it, and that distribution enters the aggregate. The paper names the resulting error fact omission: "fact omission refers to windows lacking useful information may disproportionately affect the aggregation function, leading it to omit critical information present in other windows."[^c1] The failure is therefore not that the answer is absent from the prompt. It is that a window with no answer can outweigh the window that has one.

The paper's example makes the mechanism concrete. A question about a grandfather has its facts spread over three documents, and the document that holds the needed link is "useless to answer the question" for the window that lacks it. In that window the model "confidently generate[s]" the word Unknown.[^c2][^c3] The final answer is then wrong, because the aggregation followed the window that said Unknown with high confidence and lost the claim that sat in another window.[^c4] The paper's wording is that the absence of required information "disproportionately influence[s] the aggregation function".[^c5]

Why an uncertainty rule is exposed: the lowest-uncertainty rule keeps the window with the smallest entropy. The paper says that measuring the "uncertainty of the final output distribution can be" heavily influenced by this omission.[^c6][^c7] My reading of the example: a confident Unknown has low entropy, so the rule selects exactly the window that lacks the answer. The paper does not state this step in those words; it follows from the rule and the example.

The repair the paper proposes changes the question asked of each window. Instead of how uncertain a window is, it asks how much the window changes the output relative to having no document. The paper says it measures "the changes of uncertainty" from "the non-document output distribution" to "the with-document output distribution", reflecting "the information increment provided by the retrieved" document.[^c8][^c9] The divergence used is the Kullback-Leibler divergence: "we apply the Kullback-Leibler (KL) divergence to measure the information increment".[^c10] Windows with a higher increment are given priority: "windows with higher information increment".[^c11] A window that is confidently Unknown in the same way as the no-document case then adds nothing, and the window that moves the distribution is preferred.

The paper folds this into the lowest-uncertainty selection as a penalty, with the rejection term from its other component, so the two repairs act together: "we integrate the above two methods as" penalty terms in one selection rule.[^c12] Their ablation finds that "both parts of DePaC are essential for its performance", which is the paper's evidence that the increment term matters.[^c13]

## Limits

- The diagnosis rests on one constructed example with three documents and on an ablation on six information-seeking datasets. The paper also reports how often omission occurs across its tasks in a figure, but the numbers from that figure were not read here.
- The information increment is measured against the model's own no-document distribution. My inference: a window that restates what the model already knows adds little increment even when it is correct and useful. The text read does not test this case, so it is a risk, not a finding.
- The ablation replaces the increment rule with lowest-uncertainty aggregation. It does not compare the increment rule with average aggregation or with a learned weighting, so the claim is about one alternative only.
- The backbone is one 7B model, so the frequency of omission in other models is not measured here.[^c14]
- The paper's own quantities are the ones that define omission. A different definition of "lacking useful information" would change which windows count as omitting.

## Related

- [[parallel-context-extension]] — the merge in which this failure happens; both aggregation rules in that note are exposed to it.
- [[kl-divergence]] — the divergence that measures the increment, here between a with-document and a no-document distribution.
- [[context-aware-negative-training]] — the other failure, fabrication, and the training that targets it; the two repairs are used together.
- [[unanswerable-marking-in-context]] — another response to a gap in the context: marking the unfilled question in the prompt, not reweighting the window that is missing it.

[^c1]: doi-10-48550-arxiv-2412-14905 — "information may disproportionately affect the aggregation function, leading it to omit critical information present in other windows"
[^c2]: doi-10-48550-arxiv-2412-14905 — "Doc3 is useless to answer the question"
[^c3]: doi-10-48550-arxiv-2412-14905 — "makes LLM confidently generate"
[^c4]: doi-10-48550-arxiv-2412-14905 — "further leading to the wrong final answer"
[^c5]: doi-10-48550-arxiv-2412-14905 — "disproportionately influence the aggregation function"
[^c6]: doi-10-48550-arxiv-2412-14905 — "uncertainty of the final output distribution can be"
[^c7]: doi-10-48550-arxiv-2412-14905 — "heavily influenced by fact omission hallucination"
[^c8]: doi-10-48550-arxiv-2412-14905 — "We propose to measure the changes of uncertainty"
[^c9]: doi-10-48550-arxiv-2412-14905 — "information increment provided by the retrieved"
[^c10]: doi-10-48550-arxiv-2412-14905 — "we apply the Kullback-Leibler (KL) divergence to measure the information increment"
[^c11]: doi-10-48550-arxiv-2412-14905 — "windows with higher information increment"
[^c12]: doi-10-48550-arxiv-2412-14905 — "we integrate the above two methods as"
[^c13]: doi-10-48550-arxiv-2412-14905 — "that both parts of DePaC are essential for its performance"
[^c14]: doi-10-48550-arxiv-2412-14905 — "We take Mistral-7B (Jiang et al., 2023a) as the backbone model for all methods by default"
