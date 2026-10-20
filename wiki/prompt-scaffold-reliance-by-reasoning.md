---
description: "Prompt framing matters for GPT-4 but not for OpenAI o3 or DeepSeek-R1 at fault localization; dropping the novice description cut GPT-4's Top-1 by 38% to 78% across datasets."
aliases: ["prompt scaffold dependence", "framing reliance by reasoning capability"]
sources: ["arxiv-2512-03421"]
---
# Prompt scaffold reliance by reasoning capability

A prompt for a task carries elements that frame it: who is asking, what the answer is for, what form it takes. The question this note addresses is how much the answer depends on each element, and whether that dependence is the same for every answerer. The paper's ablation says it is not. For models with strong reasoning, "prompt engineering has minimal impact".[^c1] For a model the authors call one "that lacks reasoning capabilities", the framing carries the result.[^c2]

The ablation works by removing elements from one designed prompt and measuring the change in Top-1 accuracy. Three models were tested: OpenAI o3 and DeepSeek-R1 as the reasoning side, and GPT-4 as the contrast.[^c3] For GPT-4, the element that mattered most was the novice description. Removing it "leads to the most noticeable performance drop".[^c4] The reported drops range over datasets from 38.36% on BugT to 77.77% on Condefects; on Codeflaws the drop is 42.8%.[^c5] The summary states the split directly: for models with limited modular thinking, "prompt engineering is crucial, especially the novice program prompt".[^c6]

The authors' account of the split is capability: the strong models' "reasoning capabilities" reduce their "reliance on external prompt guidance".[^c7] The mechanism that follows, which the paper does not test, is that a reasoning model can supply for itself the context a framing sentence would give it, so the sentence adds nothing. The same logic would make the framing a point of leverage only for answerers that cannot reconstruct the missing context. That is my inference.

For the wider concept, what carries over is a dependence structure. A formulation that a weaker answerer needs may be redundant for a stronger one, and removing it costs little. The reverse is also implied: a formulation can be cut from the prompt for a strong model and then wrongly removed for a weak one. Which elements fall in which group is not something the paper establishes beyond its three models.

## Limits

- Reasoning capability is confounded with model family, scale and provider. The three models differ in far more than a reasoning mode. The paper does not compare two models that differ only in that respect, so the split cannot be attributed to reasoning alone.
- The "reasoning" grouping is the authors' own classification. The paper names GPT-4 as having "medium reasoning capabilities" and o3 and DeepSeek-R1 as strong; the grading is not measured independently.[^c8]
- The ablation uses 50 programs per dataset, drawn at random because of API cost.[^c9] The per-element drops are therefore estimated from a small base, and the paper gives no interval on them.
- Only one non-reasoning model is ablated. Whether other non-reasoning models depend on the novice description to the same degree is not shown.
- Removal tests whether an element is needed as written. It does not test whether a different framing would replace the novice description. The claim is about the element, not about framing as such.
- The task is fault localization on novice programs, a single domain. Whether the split holds for other tasks is not tested here.

## Related

- [[prompt-content-over-surface-form]] — prompt sensitivity located in informational content rather than in which model reads it; this note adds that the content's weight can change with the reader's capability
- [[option-matching-shortcut]] — reasoning models match options instead of deducing, another way reasoning changes what a prompt's form does
- [[requirement-focused-prompt-training]] — training humans to state complete requirements, the part of a prompt the ablation found crucial for the weaker model

[^c1]: arxiv-2512-03421 — "prompt engineering has minimal impact"
[^c2]: arxiv-2512-03421 — "an LLM that lacks reasoning capabilities"
[^c3]: arxiv-2512-03421 — "included to evaluate the performance of an LLM that lacks reasoning capabilities"
[^c4]: arxiv-2512-03421 — "Its removal leads to the most noticeable performance drop"
[^c5]: arxiv-2512-03421 — "(42.8%), and 5 (38.36%) in Condefects, Codeflaws, and BugT"
[^c6]: arxiv-2512-03421 — "prompt engineering is crucial, especially the novice program prompt"
[^c7]: arxiv-2512-03421 — "This observation likely stems from their intrinsic capabilities"
[^c8]: arxiv-2512-03421 — "For LLMs with medium reasoning capabilities, such as"
[^c9]: arxiv-2512-03421 — "we randomly select 50 program samples from each dataset"
