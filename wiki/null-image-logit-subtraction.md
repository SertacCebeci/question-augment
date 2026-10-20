---
description: "Decoding with a blank image as a language-only pass, then subtracting its next-token distribution from the real-image one, pushes down what the question alone would produce at generation time."
aliases: ["visual contrastive decoding", "contrastive decoding with a blank image", "language prior elimination", "blank-image contrastive decoding"]
sources: ["arxiv-2512-19070", "arxiv-2512-01922"]
---
# Null-image logit subtraction

A vision-language model answers from two inputs at once, the image and the question text. To see how much of an answer comes from the text alone, the same question can be asked with a blank image in place of the photograph. The paper under this note uses that null pass inside generation rather than only as a diagnostic: at each decoding step the output distribution given the blank image is subtracted from the distribution given the real image, so that what the question alone would produce is pushed down.[^c1]

Concretely, the two next-token distributions come from the same prefix, one conditioned on image and question, one on a blank image and the same question. The paper combines them as (1+α) times the image logits minus α times the blank-image logits, with α a weighting factor.[^c2] The blank pass is described as letting the model "degrade into a simple" language-only model, in which the query alone can elicit hallucinations from language priors.[^c3] The mechanism is therefore a contrast between two conditionings of one model, not a second model and not a trained correction. The paper's own framing is that this is contrastive decoding with a blank image.

The motivation is a phenomenon the authors call "Decoding Inertia". Changing an opening phrase, "In this picture," to "On the road," on a small-car image raised the output for "car"; the authors then ran the two prompts on a blank image, and "car" still rose when "road" appeared, which they read as over-reliance on language priors.[^c4] They attribute this to frequent co-occurrence of objects in training data, a cause they assert rather than test in the text.[^c5] For someone formulating questions the observation is the relevant part: the wording of the question, with no change to the picture, moved the probability of an object the image may not contain.

The paper reports that the combined method, which also uses segmented sub-images, outperforms recent decoding methods and baselines "across multiple hallucination benchmark tests".[^c6] Those comparisons are on object-existence benchmarks with several LVLMs; the reported numbers are not reproduced in this note.

A related variant keeps the subtraction and changes the contrasting input. In a medical vision-language method the contrast comes from the same image with visual tokens masked by a sparsity mask, not from a blank image, and the masked-token embeddings are passed through the language-model head alone, so that no second decoder pass is run.[^c9] The image masking rate is a separate setting from the token sparsity rate; the paper sets it to 0.5 for image tokens.[^c10] What carries over from the blank-image case is the subtraction of a null-input distribution. What does not obviously carry over is the claim of a full second forward pass: a head-level contrast is a different object from a blank-image decoder pass, and the text read here does not test whether the two agree (my inference).

## Limits

- The subtraction removes whatever the blank image produces. It does not show that the removed part is hallucination rather than a correct prior: a common object in a common setting is often present, so the blank-image contrast can also suppress right answers (my inference; the text does not measure it).
- A blank image is itself an unusual input. Part of what is subtracted may come from blankness rather than from priors alone (my inference).
- α is a free weight. The text says "The hyperparameter α is set in the range" of values it reports, so the gains depend on a setting chosen against benchmarks, not derived from the mechanism.[^c7]
- "Decoding Inertia" rests on one illustrative image and one blank-image check, shown in a figure. No count across items is given here, so it is a case, not a measured rate.
- The method needs the blank-image pass at every decoding step, so it roughly doubles the forward passes per token (my reading of the equation); it needs access to logits and does not apply to models that expose only sampled text.
- The authors scope their work to image-text crossmodal alignment and leave video and 3D open: "Our current research focuses on crossmodal alignment between images and text".[^c8]

## Related

- [[counterfactual-image-grounding-audit]] — the same blank-image probe used as a diagnostic of visual dependence, where this note uses it inside the decoder
- [[evidence-gain-hallucination-score]] — the image-removal contrast as a log-probability score, not as a correction at decode time
- [[parametric-suppression]] — contrasting context and null passes to locate where the prior takes over inside the network
- [[text-modality-dominance]] — reliance on text over other evidence, the failure that the blank pass is meant to expose
- [[visual-token-sparsification-hallucination]] — the masked-token contrast of a medical method, where the contrasting input is the image with pruned visual tokens rather than a blank image
- [[attention-sink]] — the same method's separate reweighting of over-attended tokens, which acts on attention rather than on the output logits

[^c1]: arxiv-2512-19070 — "we perform contrastive decoding (Wang et al., 2024) by subtracting the output distribution"
[^c2]: arxiv-2512-19070 — "of the blank image vn from the output distribution"
[^c3]: arxiv-2512-19070 — "elicit hallucinations based solely on language priors"
[^c4]: arxiv-2512-19070 — "entity also increased substantially"
[^c5]: arxiv-2512-19070 — "which may be due to the frequent co-occurrence of"
[^c6]: arxiv-2512-19070 — "methods and baselines across multiple hallucination benchmark tests"
[^c7]: arxiv-2512-19070 — "The hyperparameter α is set in the range"
[^c8]: arxiv-2512-19070 — "Our current research focuses on crossmodal alignment between images and text"
[^c9]: arxiv-2512-01922 — "coding head ϕ of the language model, hence avoiding the"
[^c10]: arxiv-2512-01922 — "the image masking sparsity rate is set to 0.5"
