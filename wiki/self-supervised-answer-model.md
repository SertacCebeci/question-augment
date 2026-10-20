---
description: "An answer-likelihood model for a question-asking agent trained with no human-labelled question-answer pairs, by pairing each target with questions derived from it (yes) and from other items (no)."
aliases: ["amortized answer model", "self-supervised answer classifier", "self-labelled answerer simulator"]
sources: ["white-2021"]
---
# Self-supervised answer model

> A stand-in for a ground-truth answerer, trained without any human answer:
> label a question-target pair "yes" if the question was derived from that
> target and "no" if it was derived from another, then fit a classifier on
> that pseudo-label ([[white-2021|White, Poesia, Hawkins, Sadigh & Goodman
> 2021]]).

## Mechanism

An [[expected-information-gain|EIG]]-based question selector needs
$p(a\mid q, y)$ — how a target $y$ would be answered given question $q$ —
for every candidate before any real answer exists. Lacking a ground-truth
answerer or labelled question-answer data, the model manufactures training
pairs: a candidate question generated *from* image $y$ (via caption
decomposition) is paired with $y$ itself as a "yes" example; the same
question paired with a *different* image is a "no" example. A logistic
classifier is fit on CNN/RNN embeddings of the image and the question with
cross-[[entropy]] loss, reaching 94% accuracy against a held-out, manually
labelled set of (image, question) pairs. The same classifier serves two
roles once trained: it supplies $p(a\mid q,y)$ inside the EIG computation
before a question is asked, and — after a real answer arrives — it supplies
$p(a\mid x_t, q, y)$ for the Bayes-rule belief update.[^c4]

## Why it matters

This is the piece that makes the generation method's "no supervised
question-answer data" claim literally true: the paper needs an answer
*likelihood*, and every prior open-domain approach it cites either trains
end-to-end on annotated question sets (Yao et al. 2018; Das et al. 2017) or
retrieves/ranks against a labelled corpus (Kumar and Black, 2020; de Vries
et al., 2017). Building the likelihood from the same generative process that
produced the candidate questions — target vs. non-target pairing — removes
that dependency and is transferable to any domain where a captioner (or any
generator that can be run "in reverse" over other items) exists.[^c5]

## Limits

- The label is a heuristic, not ground truth: a question derived from image
  A can coincidentally also be true of image B, giving a mislabelled "no"
  pair. The paper reports this only as "a minority of the training data,"
  with no measured rate, so the classifier's 94% figure is against
  manually-checked pairs, not against the noisy pairs it was trained on.
- Demonstrated for polar (yes/no) answers only; the wh-question variant
  needed a different output head (a distribution over a vocabulary) and is
  reported as a preliminary, smaller-scale extension.
- Assumes the same process that generates candidate questions (caption
  decomposition) can also generate informative negative pairings; a domain
  without a comparable "other items exist and differ" structure has no
  obvious analogue of the negative-pairing trick.
- Trained and evaluated on Shapeworld and MS COCO only; no test against a
  real human answerer's response *distribution* (only against manually
  labelled yes/no pairs and, separately, live human play).

## Related

[[self-supervised-clarification-question-generation]] · [[expected-information-gain]] · [[twenty-questions]]

[^c4]: white-2021 — "We introduced a self-supervision objective by either pairing target images with questions derived from them (‘yes’ answers) or with questions derived from other images (‘no’ answers)."
[^c5]: white-2021 — "This approach is heavily data-driven, requiring large annotated training sets of questions under different goals and contexts."
