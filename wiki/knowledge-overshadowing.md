---
description: "In multi-condition queries a dominant condition can suppress another, so the LLM's next query drifts; the least-influential keyphrase, found by embedding noise, marks what to re-supply."
aliases: ["overshadowed knowledge", "condition overshadowing"]
sources: ["arxiv-2601-07260"]
---
# Knowledge overshadowing

When a query carries several conditions, a dominant condition can overshadow the others, so the model overlooks essential information while generating. Zhang et al. (2025) named the phenomenon; ActiShade builds on it.[^c1] Example: for "the famous bridge in the birthplace of Gloria in D Major's composer", the dominant condition "Te Deum in D Major" overshadows "Gloria in D Major". The model then writes a next-round query about Te Deum.[^c2]

## Why it matters for asking

Multi-round retrieval uses LLM-generated text as the next query. If the generated text drops a condition, retrieval returns irrelevant documents. Those documents mislead the next generation, so the error accumulates across rounds.[^c3] The loss is in the question being formed, not in the answer. The problem is sharpest in multi-hop reasoning, where the chain depends on several interrelated conditions.[^c4]

## Detecting it: Gaussian perturbation (GaP)

The detector treats a keyphrase that barely moves the output as underused:

1. Extract candidate keyphrases with SpaCy: named entities and NOUN, ADJ, VERB, PROPN, NUM or ADV tokens, minus stopwords.[^c5]
2. For each keyphrase, add zero-mean Gaussian noise to its token embeddings only, and compare the LLM's output distribution with the unperturbed one.[^c6]
3. Pool the distributions over time and take the cosine similarity. The keyphrase with the highest similarity is declared overshadowed, because perturbing it changed the output least.[^c7]

The earlier detector, CoDA, removes tokens instead. The authors argue that perturbing keeps the query's structure and so the reasoning chain intact.[^c8] In their ablations, CoDA was worse than no detection on MuSiQue and 2WikiMQA, which they attribute to removal disrupting the chain.[^c9] Noise level matters: performance peaked at sigma = 0.1 on Llama-3-8B-Instruct. Larger noise shifts the output for every keyphrase, which erases the contrast between salient and overshadowed ones.[^c10]

## Acting on it

ActiShade retrieves documents relevant to both the query and the overshadowed keyphrase, using a retriever trained to separate positive, semi-positive and negative documents. It then has the LLM write the next query from the retrieved material. The paper reports gains over multi-round baselines on HotpotQA, 2WikiMQA and MuSiQue across several LLMs.[^c11]

## Limits

- The detector's claim, that the highest-similarity keyphrase is the overshadowed one, is the authors' operational definition. It was not validated against human-labelled overshadowed conditions in the slices I read. Insensitivity could also mean the phrase is simply irrelevant (my inference).
- It selects a single keyphrase per query (argmax), so multiple suppressed conditions are not handled.
- It needs white-box access to token embeddings and output distributions, so it does not apply to API-only models.
- Evidence is on three multi-hop QA datasets with a sigma sweep on one model; I did not read the effect sizes.
- The analogy to human question formulation (a speaker dropping a condition) is mine and untested.

## Related

- [[embedding-retriever-position-bias]] — another way retrieval inputs get unevenly weighted, there by position rather than by a dominant condition.

[^c1]: arxiv-2601-07260 — "a phenomenon where dominant conditions can overshadow others, causing the LLM to overlook essential information during generation"
[^c2]: arxiv-2601-07260 — "the dominant condition Te Deum in D Major overshadows the condition Gloria in D Major, causing the LLM to generate next-round query related to Te Deum in D Major"
[^c3]: arxiv-2601-07260 — "such hallucinations lead to irrelevant retrieval and cause error accumulation during the iterative process"
[^c4]: arxiv-2601-07260 — "This phenomenon is particularly problematic in multi-hop reasoning, where the reasoning process relies on multiple interrelated conditions within"
[^c5]: arxiv-2601-07260 — "remove stopwords to reduce noise"
[^c6]: arxiv-2601-07260 — "we inject Gaussian noise into its token embeddings"
[^c7]: arxiv-2601-07260 — "A high similarity score indicates that the perturbation had"
[^c8]: arxiv-2601-07260 — "our GaP preserves the reasoning chain by adding"
[^c9]: arxiv-2601-07260 — "models using CoDA even perform worse than those without knowledge overshadowing detection"
[^c10]: arxiv-2601-07260 — "excessive noise causes"
[^c11]: arxiv-2601-07260 — "ActiShade significantly outperforms the state-of-the-art baselines on three"
