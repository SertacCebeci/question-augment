---
description: "A logistic probe on frozen hidden states that scores any token set, such as a line, by max-pooling down-projected states; labelled spans train it and the generator is untouched."
aliases: ["enhanced probe", "set-query probe", "arbitrary-span probe", "max-pooled latent probe"]
sources: ["arxiv-2512-24560"]
---
# Span max-pooled probe

A linear probe reads a concept off a model's hidden states by fitting a small readout on labelled examples. The variant here is built for spans. The work wanted "set queries over multiple tokens (such as those within a line)," since the label is about a line or a patch, not one token.[^p1]

## Mechanism

The generator is not modified. "As our technique does not modify the underlying transformer model, we can precompute and cache the embeddings and fit on these cached embeddings."[^p2] Each token's hidden state from a chosen layer is projected down to a small vector (32 dimensions in the reported configuration).[^p22] To score a set of tokens, "we aggregate the down-projected vectors by Max Pooling," and "then pass this aggregated vector, through logistic regression to predict a class for the query."[^p3][^p4] Because the pooling is over any chosen subset, one pass over the generated program yields scores for tokens, lines and the whole program. The authors summarize the design as one that "allows for expressive queries with minimal overhead and requiring no modifications to the generative model."[^p5]

The layer matters. "We find that LAST layer does indeed have the worst typical BSS and calibration."[^p6] The authors' best-calibrated choice was a middle layer: "MIDDLE achieves the best typical ECE (and possible generalization)," though slightly worse on skill.[^p7] Their hypothesis, which they do not test directly, is that "middle layers might be more abstract, and (we hypothesize) perhaps better capture the" model's local uncertainty.[^p8]

The probe can be small. The authors "find that probes with even a small supervision 0.5B parameter supervision model can achieve" useful calibration on code from much larger generators, and the 0.5B model can be "competent probes of code generated with models over 10x-100x the size."[^p9][^p10] This is the note's main reason to care: oversight can run on a model much smaller than the one it watches. In the reported numbers the generator choice matters most: "We find the most critical design choice is which model MUT is selected to embed for BSS."[^p11] Down-projection size, pooling style and the attention variant change results less: "We find these model design choices to have low effect" on calibration.[^p12]

## Results

For GPT-4o the raw line-level skill is 0.17 and token-level 0.13; rescaling raises these slightly, to 0.19 and 0.14.[^p13][^p21] For Qwen2.5 Code 7B, probing its own embeddings, the skill is 0.33.[^p14] The authors' overall summary: "Probing can work, but might need specific data."[^p15]

## Limits

- Labels are needed, in quantity. The method works when a labelled set of spans exists; the authors' own observation is that probing "might need specific data." The label source is the minimal-patch construction, with its own approximations (see [[minimal-patch-edit-label]]).
- Overfitting is a real risk. The protocol has no clean held-out set, and the authors flag that this "creates potential risk that results reflect overfitting, in particular for high bias techniques like" probing.[^p16]
- The generators are not frontier models: "but not quite frontier models at the time of the study in early/mid 2025."[^p17]
- White-box access is required. "This is readily obtained with open-source models; some closed-source models block access to model confidence."[^p18] For a closed generator the method is unavailable, and a smaller open model would have to stand in for it.
- Transfer is weaker. Higher layers and combined representations generalize worse to other domains: "We find that when using higher layers or the shifted/combined representation there is degraded" transfer.[^p19] On natural-language hallucinations, the code-trained probe is "much weaker than testing in-domain on code."[^p20]
- The layer result is one configuration's sweep. The authors call their chosen setting "a sensible configuration that appears robust" rather than the optimum, so reported figures are not maxima.[^p23]

## Related

- [[internal-prober]] — the general latent-probe concept; this note is a span-query variant of it.
- localized-calibration — the calibration these span scores are evaluated on.
- [[sample-diff-retention-confidence]] — the black-box route to a token score, with no access to hidden states.

[^p1]: arxiv-2512-24560 — "We wished to support set queries over multiple tokens (such as those within a line)."
[^p2]: arxiv-2512-24560 — "As our technique does not modify the underlying transformer model, we can precompute and cache the embeddings"
[^p3]: arxiv-2512-24560 — "we aggregate the down-projected vectors by Max Pooling."
[^p4]: arxiv-2512-24560 — "then pass this aggregated vector, through logistic regression to predict a class for the query."
[^p5]: arxiv-2512-24560 — "This design allows for expressive queries with minimal overhead and requiring no modifications to the"
[^p6]: arxiv-2512-24560 — "We find that LAST layer does indeed have the worst typical BSS and calibration."
[^p7]: arxiv-2512-24560 — "MIDDLE achieves the best typical ECE (and possible generalization),"
[^p8]: arxiv-2512-24560 — "might be more abstract, and (we hypothesize) perhaps better capture the"
[^p9]: arxiv-2512-24560 — "probes with even a small supervision 0.5B parameter supervision model can achieve"
[^p10]: arxiv-2512-24560 — "can be competent probes of code generated with models over 10x-100x the size."
[^p11]: arxiv-2512-24560 — "We find the most critical design choice is which model MUT is selected to embed for BSS."
[^p12]: arxiv-2512-24560 — "We find these model design choices to have low effect"
[^p13]: arxiv-2512-24560 — "observe raw skill scores of 0.17 at the line level and 0.13 at the token level"
[^p14]: arxiv-2512-24560 — "For Qwen2.5 Code 7B, we observe a skill score of 0.33 with an"
[^p15]: arxiv-2512-24560 — "Probing can work, but might need specific data."
[^p16]: arxiv-2512-24560 — "creates potential risk that results reflect overfitting, in particular for high bias techniques like"
[^p17]: arxiv-2512-24560 — "but not quite frontier models at the time of the study in early/mid 2025."
[^p18]: arxiv-2512-24560 — "This is readily obtained with open-source models; some closed-source models block access to model confidence."
[^p19]: arxiv-2512-24560 — "We find that when using higher layers or the shifted/combined representation there is degraded"
[^p20]: arxiv-2512-24560 — "While the calibration is much weaker than testing in-domain on code,"
[^p21]: arxiv-2512-24560 — "With rescaling these improve slightly to 0.19 and 0.14 respectively."
[^p22]: arxiv-2512-24560 — "a configuration of middle layer embedding, max pooling, 32 downprojection size, and Brier score loss."
[^p23]: arxiv-2512-24560 — "a sensible configuration that appears robust to other parameters."
