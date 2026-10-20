---
description: "An open-domain polar-question generator that derives candidates from an image captioner's output and ranks them by expected information gain, with no labelled question-answer data at all."
aliases: ["open-domain clarification question generation", "caption-derived question generation", "White et al. question generator"]
sources: ["white-2021"]
---
# Self-supervised clarification question generation

> A visually grounded polar-question generator that needs no supervised
> question-answer pairs at all: candidates come from an off-the-shelf image
> captioner, and selection is [[expected-information-gain|EIG]] estimated
> from a self-labelled answer model ([[white-2021|White, Poesia, Hawkins,
> Sadigh & Goodman 2021]]).

## Mechanism

At each turn the model does three things: generate candidates, select one by
EIG, update beliefs. **Generation** needs no question examples: a pretrained
image captioner produces candidate captions for each image in the context,
a constituency parse (Berkeley Neural Parser) is taken over each caption,
and every noun-phrase subtree is rewritten into a polar question ("Are there
<NP>?"), yielding on average ten candidates per caption. **Selection** scores
each candidate $q$ by $\mathrm{EIG}(y,a;q,x_t)$ — the drop in [[entropy]] of the
belief over which image $y$ is the target, marginalised over the possible
answers $a$ — and picks the arg-max. The likelihood $p(a\mid q,y)$ needed for
that expectation comes from a logistic classifier trained with
self-supervision: pairing a target image with questions derived *from it*
gives "yes" labels, pairing it with questions derived from *other* images
gives "no" labels, no human answer is ever collected for training (94%
accuracy against held-out manually labelled pairs). **Belief update** is a
Bayes-rule multiply of this same likelihood against the running belief.[^c1]

## Why it matters

In a [[twenty-questions|20-questions]] game (up to 20 turns, a context of $k$ images, one
privately indicated as the target), the full model beats a random-question
baseline and a "ask the whole caption" baseline on both a synthetic dataset
(Shapeworld) and MS COCO, and only slightly under-performs an
oracle binary-search baseline that halves the image set by fiat rather than
posing a real question. With human answerers on 10-image MS COCO games, win
rate rose from 10.0% before any question to 75.5% after questioning (mean
6.39 questions); with an initial free-text description and 25-image
contexts, from 58.5% to 75.0% (mean 7.24 questions).[^c2]

The result the map's EIG row does not otherwise carry: EIG is normally
presented as a criterion for *ranking a given candidate set* — this paper
shows the candidate set itself can be produced with zero labelled
question-answer data, only an off-the-shelf captioner and a generic parser,
because the answer likelihood the EIG computation needs is obtainable by
self-supervision rather than annotation.[^c3]

## Transfer

| | |
|---|---|
| **Home field** | image captioning and constituency parsing (computational linguistics / vision-language grounding) |
| **Here** | the captioner's output is not consumed as a caption but decomposed into a candidate pool of polar questions for an EIG selector |
| **What survives** | the pre-answer EIG selection logic is unchanged — arg-max over a fixed candidate set scored by expected entropy drop under a learned answer likelihood |
| **What does not** | the parse-to-question templates are English-specific and tied to constituency-parse quality; extension past polar to wh-questions is reported only as a preliminary result (a single-word-answer variant, +3% at 20 questions on MS COCO), not validated at the scale of the polar-question results |

## Limits

- Evaluated on two visual domains only (Shapeworld, MS COCO), against
  synthetic and 40–41 Mechanical Turk answerers per experiment; no test
  outside visually grounded reference games.
- The self-supervised answer labels are occasionally wrong: a "no"-labelled
  pair can coincidentally be true of the image (a question derived from a
  different image can still apply), and the paper reports this only as "a
  minority of the training data," not a measured rate.
- The candidate pool is capped by what a captioner plus NP-decomposition
  produces; an axis the captioner never mentions cannot become a question,
  the same invisibility [[expected-information-gain]] names for any
  unmodelled axis.
- The gap between the model and the oracle binary-search baseline is larger
  on MS COCO than on Shapeworld; the paper attributes this to the difficulty
  of finding attributes that cleanly split a random set of natural images,
  not to a flaw in the EIG computation itself.

## Related

[[expected-information-gain]] · [[question-asking-as-program-generation]] · [[twenty-questions]] · [[self-supervised-answer-model]] · [[generalized-binary-search]]

[^c1]: white-2021 — "Our model uses an expected information gain objective to derive informative questions from an off-the-shelf image captioner without requiring any supervised question-answer data."
[^c2]: white-2021
[^c3]: white-2021 — "Our key contribution is a lightweight method to ground question semantics in the open image domain without observing question examples."
