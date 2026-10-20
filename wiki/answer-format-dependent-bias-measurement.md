---
description: "The same items given in closed-ended, Likert and open-ended formats yield different measured gender bias and reversed model rankings, because each format elicits a different response behaviour."
aliases: ["answer format effects on bias evaluation", "format-dependent bias scores", "multi-format evaluation"]
sources: ["doi-10-48550-arxiv-2608-17516", "arxiv-2512-19238", "arxiv-2512-03019"]
---
# Answer-format-dependent bias measurement

A bias score is not a property of the model alone; it is a property of the model and the answer format in which the question was posed. Merzlyakova, Padó and Weeber reformatted the same gender-related items from BBQ and OpinionQA into closed-ended, Likert-scaled and open-ended versions and ran three instruction-tuned models (Mistral 7B, Gemma 12B, Llama 8B). They found that "answer format does substantially alter measured outcomes, including reversals in order rankings."[^c1]

## Mechanism: each format elicits a different behaviour

The authors attribute the differences to the response behaviour each format induces: "forced-choice selection, scale-based distributions and refusal in free-text generation."[^c2]

- **Closed-ended**: bias shows up as stereotype-consistent forced choice. It gave the strongest and most consistent stereotypical behaviour across models.[^c3]
- **Likert**: stereotype-consistent and counter-stereotypical answers partly cancel, so net directional bias looks low although a polarisation index shows substantial stereotyping.[^c4] Near-zero ambiguous-context scores coexisted with polarisation, so the scale can mask bias through symmetric polarisation.[^c5]
- **Open-ended**: measured bias falls through selective abstention, where models give non-substantive outputs even where BBQ presupposes a substantive answer.[^c4]

## Consequences for evaluation

- Rankings flip: Mistral 7B goes from the most biased model in the closed-ended format to the least biased in open-ended.[^c6]
- Distributional alignment with humans (OpinionQA) is also format-dependent: Mistral 7B is best on discrete formats but worst on Likert, and Gemma 12B shows the reverse.[^c7]
- Part of the apparent Likert advantage is mechanical (mean-normalisation, per-option averaging, removal of mutual exclusivity), not better opinion modelling.[^c8]
- Closed-ended answer order matters strongly, and no single ordering consistently predicts performance.[^c9]
- The authors' conclusion: using a single format "would draw a different, and potentially misleading, conclusion about which model behaviours exhibit bias."[^c10] They also argue the differences are not solely measurement artefacts.[^c11]

My inference: format should be treated as part of the measurement instrument, so a single-format score supports claims only about that format.

The format can also remove a bias rather than expose one. In pairwise LLM judging the measured bias is positional, not gender-related: the candidate shown first or second wins more often. Forcing a choice pushes order-driven preferences onto one side. Gemini-2.5-flash "favors the first position by 14.58%" when a forced choice is required, and the authors report that allowing a tie "dramatically reduces positional bias for both models".[^c14][^c15] This comes from one experiment on a subset of 336 human-tie pairs, and it is a bias of the judge under one format, not a claim about gender bias in the closed-ended items above.

## Limits

- Three small instruction-tuned models, two datasets and one bias construct (gender); the paper calls its analysis descriptive, so no causal decomposition of format versus model is given.
- Open-ended answers were mapped by annotation; non-matching answers count as refused, so abstention and annotation failure are partly confounded.
- The Likert and open-ended conversions of BBQ were generated and validated by prompting, so conversion quality bounds the comparison.
- Whether the effect holds for larger or frontier models is not tested.
- A binary format sets its own coding rule. In a SocialStigmaQA study, any answer that was not an explicit yes or no was counted as unbiased, "as it did not explicitly contain bias".[^c12] My inference: a model that hedges or declines to pick a side scores as unbiased under that rule, so the same format change that exposes forced-choice bias can also hide it. The authors of that study name the binary requirement itself as a limitation.[^c13] See [[stigma-social-features]].

## Related

- [[format-restriction-effect]] — format effects on answer quality, rather than on bias measurement
- [[survey-response-model]] — the survey-methodology view of format as part of the instrument
- [[elicitation-protocols]] — how the way of asking shapes what is elicited
- [[option-matching-shortcut]] — option-level artefacts in multiple-choice formats

[^c1]: doi-10-48550-arxiv-2608-17516 — "We find that answer format does substantially alter measured outcomes, including reversals in order rankings."
[^c2]: doi-10-48550-arxiv-2608-17516 — "forced-choice selection, scale-based distributions and refusal in free-text generation."
[^c3]: doi-10-48550-arxiv-2608-17516 — "Closed-ended results show the strongest, most"
[^c4]: doi-10-48550-arxiv-2608-17516 — "Open-ended formats reduce measured bias through selective abstention"
[^c5]: doi-10-48550-arxiv-2608-17516 — "Thus, the Likert format may mask stereotypeconsistent behaviour through symmetric polarisation"
[^c6]: doi-10-48550-arxiv-2608-17516 — "Mistral7B shifts from the most biased model in closed-ended to the least biased"
[^c7]: doi-10-48550-arxiv-2608-17516 — "Mistral7B exhibits highest alignment on discrete formats but lowest on"
[^c8]: doi-10-48550-arxiv-2608-17516 — "lower Likert divergence relative"
[^c9]: doi-10-48550-arxiv-2608-17516 — "all models are sensitive to ordering, but no single ordering consistently predicts performance."
[^c10]: doi-10-48550-arxiv-2608-17516 — "Using any single format would"
[^c11]: doi-10-48550-arxiv-2608-17516 — "these differences cannot be attributed solely to measurement artefacts."
[^c12]: arxiv-2512-19238 — "as it did not explicitly contain bias"
[^c13]: arxiv-2512-19238 — "we note the limitation of the binary output requirement within the SocialStigmaQA benchmark"
[^c14]: arxiv-2512-03019 — "first position by 14.58%"
[^c15]: arxiv-2512-03019 — "introduction of this third choice dramatically reduces positional bias for both models"
