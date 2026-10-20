---
description: "Whether passages contain what an answer requires can be judged from the question and passages alone, before any generator runs; a local scorer ranks sufficient evidence above insufficient."
aliases: ["RINSE", "answer-free sufficiency scoring", "pre-generation sufficiency check", "evidence sufficiency before generation"]
sources: ["doi-10-48550-arxiv-2609-37469"]
---
# Pre-generation evidence sufficiency

A set of retrieved passages can be judged sufficient for a question without generating an answer. The judgment reads only the question and the passages, and asks whether they contain the information a complete answer needs, "including any intermediate facts, before generation begins."[^c1] The claim behind this is that sufficiency is a property of the pair, not of the model that will read it: "whether a set of passages answers a question is a property of" the question and its retrieved passages.[^c2] A generator-free check can run before the generator is called, and it does not need weights tied to one model.

The scorer built on this idea, RINSE, sums three readers that never produce an answer. A content reader checks whether every part of the question is covered: "The content reader measures whether every local part of the question is supported somewhere in the evidence."[^c3] A span reader asks whether some passage contains an answer-like span: "The span reader asks whether any passage contains text that an" extractive QA model prefers to its no-answer option.[^c3b] A latent reader is a frozen 1.5B model that reads the top five passages together, and "The latent reader captures evidence that becomes informative only when passages are read together."[^c4] Each raw score is corrected for evidence-set size and standardised, and "the three are summed with equal weights."[^c5] The weights are fixed rather than tuned per dataset, because the best single reader changes from one dataset to the next.

What was measured. On constructed sufficient and insufficient pairs from six datasets, scored by pairwise accuracy (chance 0.5), RINSE averages 0.837 against 0.746 for Self-RAG, the strongest of ten prior methods.[^c6] A frontier model asked the sufficiency question through an API scores 0.784 on the same pairs. "Asked directly whether the evidence suffices, a local 1.5B model" scores 0.540, so the same question asked of a small local model does little, while the reader-based decomposition does much more.[^c7] On passages returned by real retrievers (BM25 and e5-base-v2, top five), RINSE averages 0.813 against 0.674 for the best prior method.[^c8] The median latency is 36.5 ms per record on one A100, which the authors compare with the 92 to 855 ms median of the twelve short generations they timed; "less than the median time of any of the 12 short generations in" that table.[^c9] The output is a ranking, and "RINSE outputs a ranking score", so a deployment must still choose a threshold for answer, abstain or retrieve more.[^c10]

The contrast with generator-side signals is the main reason the answer-free design matters. Methods that read a generated answer are the ones that fail on NeoQA, where the evidence is invented and the generator cannot have memorised the answers: "Methods that read a generated answer fail on NeoQA," with all four such methods between 0.503 and 0.520.[^c11]

## Limits

The evaluation uses constructed contrasts (substitution, deletion, question swap), and the paper's own cue audit shows that naive constructions leak. After controls, an evidence-only classifier still scores 0.743 on HotpotQA, so the audit has not shown that the sufficiency signal is free of other surface cues.[^c12] The span reader is trained once on Natural Questions, and the latent reader depends on a 1.5B backbone and a direction fitted on other families; neither is shown to transfer to a different domain or a different backbone.

The dataset profile is uneven. RINSE's weakest dataset, SQuAD 2.0, scores 0.684, while the other local methods fall to 0.644 or lower on at least one dataset.[^c13] On NeoQA the content reader alone scores above the full sum, so the equal-weight sum is not the best choice on every dataset.[^c14]

The sufficiency label is itself the dataset's annotation (the gold supporting passages), not a judgment of whether a generator would answer correctly. My inference, not the paper's claim: a passage set can be annotated sufficient and still lead a particular generator astray, and this scorer does not measure that.

The paper does not test thresholds in deployment, a generator-in-the-loop setting, or whether the ranking helps a downstream abstention policy. Its cost claim is for one GPU and one batch setup.

## Related

- [[evidence-insufficiency-regimes]] — the three failure modes the three readers are built to catch
- [[relevance-completeness-divergence]] — relevance scores also fail to track whether an answer is complete, in a different domain
- [[dac-cross-agent-abstention-reward]] — argues sufficiency should depend on the generator; this paper argues the opposite and tests it
- [[search-induced-abstention-degradation]] — generators keep answering when the retrieved text does not say unknowable
- [[structured-gap-sufficiency-judge]] — a distilled LLM judge that makes the same sufficiency call inside an iterative loop
- [[sufficiency-gated-imagination]] — gating extra evidence on a sufficiency judgment, the same decision used to stop or continue
- [[sufficient-statistic]] — the statistical sense of "sufficient"; not the same concept

[^c1]: doi-10-48550-arxiv-2609-37469 — "information needed to derive a complete answer, including any intermediate facts, before generation begins"
[^c2]: doi-10-48550-arxiv-2609-37469 — "whether a set of passages answers a question is a property of"
[^c3]: doi-10-48550-arxiv-2609-37469 — "The content reader measures whether every local part of the question"
[^c3b]: doi-10-48550-arxiv-2609-37469 — "The span reader asks whether any passage contains text that an"
[^c4]: doi-10-48550-arxiv-2609-37469 — "The latent reader captures evidence that becomes informative"
[^c5]: doi-10-48550-arxiv-2609-37469 — "the three are summed with equal weights"
[^c6]: doi-10-48550-arxiv-2609-37469 — "Averaged over six datasets, RINSE scores 0.837, ahead of all 10 prior methods"
[^c7]: doi-10-48550-arxiv-2609-37469 — "Asked directly whether the evidence suffices, a local 1.5B model"
[^c8]: doi-10-48550-arxiv-2609-37469 — "On evidence returned by real retrievers, RINSE scores 0.813, against 0.674 for the"
[^c9]: doi-10-48550-arxiv-2609-37469 — "less than the median time of any of the 12 short generations in"
[^c10]: doi-10-48550-arxiv-2609-37469 — "RINSE outputs a ranking score"
[^c11]: doi-10-48550-arxiv-2609-37469 — "Methods that read a generated answer fail on NeoQA"
[^c12]: doi-10-48550-arxiv-2609-37469 — "The evidence-only classifier still scores 0.743"
[^c13]: doi-10-48550-arxiv-2609-37469 — "its weakest dataset scores 0.684, while every other local method drops to 0.644"
[^c14]: doi-10-48550-arxiv-2609-37469 — "above the full sum (0.773)"
