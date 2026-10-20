---
description: "Vision-language models pick too many figure panels, and asking them to localize before judging lowers accuracy; handing them the right panel helps but does not reach the ceiling."
aliases: ["evidence localization", "panel localization failure", "localize-then-judge penalty"]
sources: ["doi-10-48550-arxiv-2506-04585"]
---
# Evidence localization gap

To judge a claim against a multi-panel figure, an answerer has to find which panels bear on the claim before it can weigh them. The MuSciClaims paper treats this as a separate capability, evidence localization. It measures the capability by asking models to name the relevant panels and scoring the names with precision, recall and F1.[^l1] The result is that "VLMs localize poorly to relevant information."[^l2] The errors have one shape. Models do find the right panels, but they include too many: "they do identify the relevant panel(s), but also deem a lot of irrelevant panels to be important."[^l3] Low precision with high recall is over-inclusion, not a miss.

Localization also sits inside the reasoning chain, and putting it there costs accuracy. Asking the model to localize first and then reason does worse than reasoning over the whole figure: "Model performance deteriorates when localizing before reasoning."[^l4] A two-step answer that finds the evidence and then judges it can therefore score below a one-step answer that looks at everything at once.

The hint experiments separate finding from using. Gold panel information helps. Given the relevant panels as text, models "fare much better"; given only the relevant panel as an image, they "improve even further", which the paper reads as removing panel localization errors.[^l5][^l6] The ceiling is still not reached: "But even with perfect localization (i.e., through hints here), there is significant room for improvement."[^l7] Finding the right evidence is necessary for a good verdict and not sufficient.

My reading, not the paper's claim: the two results together suggest that a localization step is a cost as well as a benefit. The localize-then-look ordering that [[coarse-to-fine-evidence-zoom]] uses on video gains there, while the same ordering loses on scientific figures. The text I read does not say whether the loss comes from the extra step, from the prompt, or from the answer format.

## Limits

- The hint experiments run on "a randomly sampled subset (n=101) of class-balanced data points."[^l8] That is a small sample, and no interval is reported in the text I read.
- The gold panels are "automatically extracted annotations about the panels of a figure."[^l9] Localization errors are measured against those annotations, so some of the error may be annotation error. The text I read does not validate the panel labels.
- A hint hands the model the location of the evidence. The gain measures what a located panel is worth to the verdict, not whether models can locate evidence unprompted in deployment.
- The localize-first drop is shown for one prompt format, a separate localization step followed by reasoning. The paper does not test a version that asks for localization inside a single reasoning pass.
- The localization numbers are not broken down by physics, chemistry or biology in the text I read, so a domain-level reading of the gap is not established here. This is my reading of what I read, not a result.

## Related

- [[coarse-to-fine-evidence-zoom]] — localize-then-look answering in video; here the same ordering loses accuracy on figures, which limits its transfer.
- [[visual-evidence-scoring]] — scores localization as one of three sub-scores of a VQA selector's confidence, a use of the same capability as a signal rather than a step.
- [[perception-cognition-gap]] — a figure can be read correctly and still be misinterpreted; the failure here is about which parts to read, not what they mean.
- [[cot-judge-detection-localization-gap]] — a judge that detects a causal step still fails to localize it; a localization failure in process judging, not in figures.

[^l1]: doi-10-48550-arxiv-2506-04585 — "We use precision, recall and F1 to measure how well models identify the correct panels"
[^l2]: doi-10-48550-arxiv-2506-04585 — "VLMs localize poorly to relevant information."
[^l3]: doi-10-48550-arxiv-2506-04585 — "they do identify the relevant panel(s), but also deem a lot of irrelevant panels to be important"
[^l4]: doi-10-48550-arxiv-2506-04585 — "Model performance deteriorates when localizing before reasoning"
[^l5]: doi-10-48550-arxiv-2506-04585 — "they fare much better"
[^l6]: doi-10-48550-arxiv-2506-04585 — "They improve even further"
[^l7]: doi-10-48550-arxiv-2506-04585 — "But even with perfect localization (i.e., through hints here), there is significant room for improvement"
[^l8]: doi-10-48550-arxiv-2506-04585 — "a randomly sampled subset (n=101) of class-balanced data points"
[^l9]: doi-10-48550-arxiv-2506-04585 — "automatically extracted annotations about the panels of a figure"
