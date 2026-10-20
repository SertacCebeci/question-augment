---
description: "Parallel context extension runs the model on each retrieved window and merges the per-window next-token distributions with an aggregation rule that decides whose evidence wins."
aliases: ["parallel context windows", "PCE", "parallel context extension for RAG", "distribution-level window aggregation"]
sources: ["doi-10-48550-arxiv-2412-14905"]
---
# Parallel context extension

Parallel context extension (PCE) gives a language model more retrieved text than one prompt is meant to hold, without placing every document in one context. Each document goes into its own window together with the question and the answer generated so far. The model is run once per window, and the per-window next-token distributions are merged into one distribution from which the next token is sampled.[^c1] The merge is the whole mechanism: the windows never see each other, and only their output distributions meet at the aggregation step.

The fit with retrieval rests on independence. The paper says "PCE is highly compatible with RAG scenarios" and the reason given is that the retrieved candidates are independent of one another, so each can sit in its own window.[^c2] The authors also state that "The effectiveness of the PCE paradigm is significantly influenced by the design of the aggregation" rule, which makes the aggregation the place where the method is decided.[^c3]

Two aggregation rules are in use. The first is average aggregation, which gives every window the same weight. The paper says this makes the method "unable to seek critical information when applied to RAG", because when only a few documents are relevant, an equal-weight average lets the irrelevant windows dilute the answer.[^c4][^c5] The second is lowest-uncertainty aggregation, which "selects the individual distribution with the lowest uncertainty" and so keeps the window whose output distribution has the smallest entropy.[^c6] The paper credits this with "filtering out highuncertainty windows", but says it "remains a suboptimal solution as it still suffers from the two types" of in-context hallucination.[^c7] That remainder is what the paper's two repairs address.

One further step sits outside the aggregation. Before sampling, the paper subtracts a weighted no-document distribution from the aggregate. My reading of that subtraction is that it removes what the question alone would produce; the paper gives only the formula and the weight. The paper calls this "the calibrated distribution to facilitate generation" and takes the weight from earlier work.[^c8] The no-document distribution is the baseline against which a window's contribution can later be measured.

On cost, the paper states that its own method's "inference time ... increases linearly" with the number of documents, and that the vanilla single-prompt approach grows faster ("time of vanilla approach increases squarely").[^c9][^c10] The per-window structure is what makes the linear claim possible, so it is a property of PCE as a family, not only of the paper's variant. This is my inference from the structure; the paper's measurement concerns its own method.

## Limits

- The paper adopts the output-distribution form of PCE and says that Su et al. "claimed the above two formalizations have similar practical performances" for the output-distribution and hidden-state forms.[^c11] It does not test the hidden-state form itself, so parity between the two is taken from the earlier work.
- Only two aggregation rules are compared as baselines, average and lowest-uncertainty. Other rules, such as learned weights, were not part of the text read.
- Every experiment uses one backbone: "We take Mistral-7B (Jiang et al., 2023a) as the backbone model for all methods by default".[^c12]
- The independence assumption is the paper's premise, not a result. Its own example asks a question whose answer chains facts that may sit in different documents; whether PCE can combine evidence split across windows is not the point the paper measures. My reading: the aggregation is over answer distributions, so a fact that is only meaningful with another window's fact has no path through the merge.

## Related

- [[window-omission-hallucination]] — the failure that survives both aggregation rules above, in which a window without the answer wins the merge.
- [[context-aware-negative-training]] — the repair for the other failure, fabrication, which trains the window model to refuse on irrelevant documents.
- [[sequential-window-reading]] — the other way to read a ranked list of windows: one window at a time, with a stop, rather than a merge over all of them.
- [[kl-divergence]] — the divergence the paper uses to compare a window's distribution with the no-document one.

[^c1]: doi-10-48550-arxiv-2412-14905 — "Subsequently, these individual distributions are aggregated into a single distribution"
[^c2]: doi-10-48550-arxiv-2412-14905 — "PCE is highly compatible with RAG scenarios"
[^c3]: doi-10-48550-arxiv-2412-14905 — "The effectiveness of the PCE paradigm is significantly influenced by the design of the aggregation"
[^c4]: doi-10-48550-arxiv-2412-14905 — "each context window with equal importance"
[^c5]: doi-10-48550-arxiv-2412-14905 — "it unable to seek critical information when applied"
[^c6]: doi-10-48550-arxiv-2412-14905 — "This method selects the individual distribution with the lowest uncertainty"
[^c7]: doi-10-48550-arxiv-2412-14905 — "it remains a suboptimal solution as it still suffers from the two types"
[^c8]: doi-10-48550-arxiv-2412-14905 — "is the calibrated distribution to facilitate generation"
[^c9]: doi-10-48550-arxiv-2412-14905 — "The inference time of DePaC increases linearly"
[^c10]: doi-10-48550-arxiv-2412-14905 — "time of vanilla approach increases squarely"
[^c11]: doi-10-48550-arxiv-2412-14905 — "claimed the above two formalizations have similar practical performances"
[^c12]: doi-10-48550-arxiv-2412-14905 — "We take Mistral-7B (Jiang et al., 2023a) as the backbone model for all methods by default"
