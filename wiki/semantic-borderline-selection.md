---
description: "Examples are picked at the edge of a written definition, as a language model reads it, not where a classifier's probability sits near 0.5; the paper argues VLM probabilities are uncalibrated."
aliases: ["semantic borderline retrieval", "borderline image retrieval", "language-boundary example selection"]
sources: ["arxiv-2512-10821"]
---
# Semantic borderline selection

When a person is asked to label examples so that a classifier can be sharpened, the usual choice is uncertainty sampling: show the examples the classifier is least sure about. The work states what that choice amounts to for a binary classifier: uncertainty sampling "selects samples with prediction probabilities near 0.5".[^c1] Its own selection rule moves the boundary out of the classifier's probability and into the wording of the definition. Borderline images are those "near the natural-language decision boundary implied by" the current definition, "as judged by LLM/VLM reasoning rather than by model confidence".[^c2]

The authors give two reasons. First, a vision–language model here is "a generative model rather than a dedicated discriminative model", which makes margin-based sampling "ill-defined".[^c3] Second, a generative model's confidence may not track human ambiguity: such a model "may assign high confidence to cases that humans find" ambiguous.[^c4] The selected examples are meant to "stress-test the current definition along one interpretable dimension".[^c5]

The mechanism is concrete. An LLM writes borderline queries from the current definition, and each query retrieves a pool of candidate images, and near-duplicates are removed.[^c11] The images are embedded and grouped into clusters by sparse dictionary codes. A multi-armed bandit with an upper-confidence rule chooses which cluster the user sees next, and it favours clusters where "the model disagrees with users" or where feedback has been most informative.[^c6] Within a chosen cluster, a VLM writes a one-sentence summary of each image's ambiguity, and a batch is kept only if the summaries form a tight cluster, so that "batch centers on a single coherent ambiguity dimension".[^c7] The language model is used to propose and to describe, not to pick the final images alone. The authors note that prompting an LLM directly for borderline images "may overlook idiosyncratic user preferences, hallucinate" visual descriptions.[^c8]

## Limits

- No measured comparison with uncertainty sampling is reported. The authors say their "evaluation does not isolate the contributions of individual components", including the retrieval module, so the gain is not attributed to the selection rule.[^c9]
- The calibration premise is asserted with citations, not measured here. The paper says that "VLM predictions are often uncalibrated with human understanding" and cites other work for it.[^c10] No calibration of the model used is shown.
- The selection depends on an LLM's reading of the boundary. Queries and summaries can drift from what the target dataset contains, which is why the paper adds retrieval and clustering. How often that drift occurs is not reported.
- The bandit reward is a proxy, given as an example: "fraction of classifier errors corrected" or the amount of feedback.[^c12] Whether it tracks the user's understanding is not tested.
- The study uses one concept domain (healthy food and similar subjective visual concepts), one generative model, and sessions with non-experts. Transfer to text or to other domains is not shown.
- My inference, not the paper's: a boundary drawn in words can be borderline for the wording while being clear to the person who wrote it. The note has no evidence either way.

## Related

- [[concept-deliberation]] — the process this selection serves; the cases shown are chosen to make the user revise the definition.
- [[positive-first-most-ambiguous-selection]] — the uncertainty-sampling family this note departs from; that rule also works from classifier scores near 0.5, under rare-positive imbalance.
- [[expected-information-gain]] — the information-maximising ideal that uncertainty sampling approximates; the work does not measure its selection against it.
- [[ambiguity-taxonomy]] — a vague term admits borderline cases; this note is about choosing examples at such a boundary.

[^c1]: arxiv-2512-10821 — "which for binary classification is equivalent to selecting samples with"
[^c2]: arxiv-2512-10821 — "as judged by LLM/VLM reasoning rather than by model confidence"
[^c3]: arxiv-2512-10821 — "rather than a dedicated discriminative model, making classical margin-based sampling ill-defined"
[^c4]: arxiv-2512-10821 — "may assign high confidence to cases that humans find"
[^c5]: arxiv-2512-10821 — "stress-test the current definition along one interpretable dimension"
[^c6]: arxiv-2512-10821 — "This directs user attention to clusters where the model disagrees with users"
[^c7]: arxiv-2512-10821 — "batch centers on a single coherent ambiguity dimension"
[^c8]: arxiv-2512-10821 — "may overlook idiosyncratic user preferences, hallucinate"
[^c9]: arxiv-2512-10821 — "Our evaluation does not isolate the contributions of individual components"
[^c10]: arxiv-2512-10821 — "often uncalibrated with human understanding"
[^c11]: arxiv-2512-10821 — "prioritizing surfacing a broader pool of borderline cases"
[^c12]: arxiv-2512-10821 — "fraction of classifier errors corrected"
