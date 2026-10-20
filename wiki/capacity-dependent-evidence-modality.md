---
description: "Converting a figure or table to text before retrieval beats retrieving its page image for a mid-size generator, while page-image retrieval closes the gap with a frontier one."
aliases: ["capacity-aware MM-RAG", "modality-converting versus OCR-free retrieval", "pipeline choice is capacity-dependent", "convert-or-retrieve-page choice"]
sources: ["arxiv-2512-16802"]
---
# Capacity-dependent evidence modality

In multimodal retrieval-augmented generation, a figure or table can reach the generator in two forms. It can be converted to text before indexing, so that a parser and a summariser do the interpretation inside the pipeline. Or the whole page can be indexed as an image, and the generator does the reading at answer time. Kocbek et al. set these up as two paradigms and find that which one works better depends on the generator. Their abstract puts it in one sentence: "Pipeline choice is capacity-dependent."[^c1]

The numbers come from a 120-question multiple-choice benchmark on glycobiology, built from 25 papers. With Gemma-3-27B-IT, text and multi-modal augmentation outperformed OCR-free retrieval, at 0.722 to 0.740 against 0.510 average accuracy.[^c2] With GPT-4o the order narrows: Multi-modal reached 0.808, Text 0.782 and ColPali 0.745, and the authors judge that "within-model differences were small."[^c3] Their conclusion names the pattern directly: "We found a clear capacity-dependent pattern."[^c4] Across the GPT-5 family, the three visual retrievers (ColPali, ColQwen, ColFlor) "were statistically indistinguishable," so the retriever mattered less than the generator's scale.[^c5]

The mechanism the authors give concerns where the reading happens. "Modality-converting pipelines interpret earlier (via OCR/layout analysis and summarization)," while visual retrievers leave the interpretation to the LLM, which reads the retrieved page images.[^c6] A weak reader can therefore receive the right page and still fail. In their words, "the system can retrieve the right page but the generator" cannot read it reliably. With GPT-4o, "the gap closes and ColPali becomes competitive."[^c7] The design lesson they draw is that "conversion to text lowers the burden" on the generator, which is why conversion is the safer default when capacity is limited.[^c8]

The same claim can be stated as a question about the pair: for this generator, is the cost of reading the evidence lower in the pipeline or at answer time? The paper's own version is that conversion "interpret[s] earlier" and visual retrieval "interpret[s] later," and the crossover is where the generator can carry the later reading. My reading, not the paper's: the variable that moves the crossover is the reader's ability to read a page image, and the model family is only a proxy for it.

## Limits

- The benchmark is small and narrow. The authors say so themselves: "The benchmark is small," and it is "focused on glycobiology." The item mix is skewed toward easy cases, which leaves the medium and hard strata exploratory.[^c9]
- "Capacity" is never measured. It is a label on a few models, and Gemma-3-27B-IT differs from the GPT-4o and GPT-5 models in vendor, training and size at once. The data show an ordering over these models, not a dose-response in reader ability. Whether a single property of the generator drives the crossover is not tested.
- Only one open-source model was analysed in depth: "We analyzed one open-source model." The authors name the gap: "future work should span a wider" range of open VLMs.[^c10][^c11]
- The frontier side is thinner than the mid-size side. The GPT-5 comparison ranks visual retrievers against each other, and in the part I read, text RAG and multi-modal conversion were not re-run on GPT-5. The claim that the gap closes at frontier scale rests on GPT-4o, where the margins are about six points on 120 items, each configuration run 5 times.
- Retrieval quality says little here. Retrieval precision at 5 "was uniformly low with only modest variation," because each question draws on a single source article, so any extra returned document counts as a false positive.[^c12]
- Only multiple-choice accuracy is reported: "we reported multiple-choice accuracy," so whether the generator used the retrieved evidence faithfully is not measured.[^c13]
- The advice to "argue for capacity-aware MM-RAG design" and to "Choose capacity-aware designs" is the authors' recommendation, drawn from one domain. It is not a general result about multimodal retrieval.[^c14][^c15]

## Related

- [[page-image-evidence-unit]] — the page as the retrieval unit, with no text-chunk baseline; this work runs that baseline and shows that the ranking depends on the generator
- [[retrieval-utilization-gap]] — a retrieval that surfaces the evidence but is not used; the page-image route exposes this failure in a weak reader
- [[perception-context-tradeoff]] — raw visual input against question-agnostic text; there the text route loses detail for a strong agent, here conversion helps a weak reader, and the two agree only if reader capacity is the hidden variable (my inference)
- [[ue-method-scale-dependence]] — another best-method choice that switches with model scale, here in uncertainty estimation rather than retrieval
- [[capacity-dependent-format-tax]] — the same capacity dependence for an output schema instead of an input modality

[^c1]: arxiv-2512-16802 — "Pipeline choice is capacity-dependent"
[^c2]: arxiv-2512-16802 — "Text and Multi-modal augmentation outperformed OCR-free"
[^c3]: arxiv-2512-16802 — "within-model differences were small"
[^c4]: arxiv-2512-16802 — "We found a clear capacity-dependent pattern"
[^c5]: arxiv-2512-16802 — "statistically indistinguishable"
[^c6]: arxiv-2512-16802 — "Modality-converting pipelines interpret earlier"
[^c7]: arxiv-2512-16802 — "the gap closes and ColPali becomes competitive"
[^c8]: arxiv-2512-16802 — "conversion to text lowers the burden"
[^c9]: arxiv-2512-16802 — "The benchmark is small"
[^c10]: arxiv-2512-16802 — "We analyzed one open-source model"
[^c11]: arxiv-2512-16802 — "future work should span a wider"
[^c12]: arxiv-2512-16802 — "was uniformly low with only modest variation"
[^c13]: arxiv-2512-16802 — "we reported multiple-choice accuracy"
[^c14]: arxiv-2512-16802 — "argue for capacity-aware MM-RAG design"
[^c15]: arxiv-2512-16802 — "Choose capacity-aware designs"
