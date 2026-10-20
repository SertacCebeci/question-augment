---
description: "Searching prompts by decoding from an LLM prior tilted by a classifier on a text-to-image model's activations keeps prompts natural while steering them toward a chosen bias."
aliases: ["bias-guided prompt search", "BGPS", "classifier-steered prompt decoding", "prior-anchored failure-prompt search"]
sources: ["arxiv-2512-08724"]
---
# Language-prior-anchored prompt search

A prompt search can run against a target without optimizing the prompt's words directly. Here the search decodes text from a language model and lets a score read from the target steer which continuations survive. The paper's instance targets a text-to-image diffusion model: the search "automatically generates prompts that aim to maximize the presence of biases in the generated images."[^c1]

The objective sums two terms. The first is the language model's prior over the prompt, which the paper says "regularizes against degenerate and unnatural text or text that does not respect the instructions."[^c2] The second is the probability that the generated image carries a chosen attribute, and "The second term favours prompts that lead to biased generations."[^c3] The language model is instructed to produce attribute-neutral prompts, so it supplies a picture of what a plausible prompt looks like before any target signal is added. The paper uses Mistral-7B-v0.2 for this role.[^c4] A weight λ sets the trade-off: it "controls the relative influence of the classifier and LLM scores."[^c5]

The target signal is not read from a finished image by a separate vision model. It is a linear head trained on the generator's own activations: the paper uses "linear classification heads that are pre-trained on activations from the middle layer of Stable Diffusion 1.5 UNet." The score is an average over diffusion noise, because prompts are judged "by their average tendency to generate biased outputs across multiple generations."[^c6] A single lucky sample therefore does not decide a prompt.

Decoding is beam search with an expansion factor. Plain beam search is deterministic, and the paper notes that it "is unfortunately deterministic, which does not let us sample different biased prompts."[^c7] The paper adds extra expansion and samples "the first token from the full LLM logits distribution,"[^c20] then keeps the top-scoring beams under the joint objective. Mechanically, the language model proposes continuations, the attribute head reweights them, and the surviving prompt is one whose prior and target score are both high.

The reason to route the search through a language prior shows up against a gradient-based baseline. The paper's framing is that "gradient-based prompt optimization discovers high-bias regions but produces unreadable text."[^c8] In the comparison, the hard-prompt method PEZ "produces unnatural prompts with very high perplexity" and "frequently reveals the attribute of interest."[^c9][^c10] Naturalness is measured by GPT-2 perplexity, "using a different language model than the one we used for our method, specifically GPT-2."[^c11]

For the asker, the mechanism is this: a failure-triggering input can be searched for inside the set of inputs a language model finds plausible, while the failure signal is read from the system under test's internals rather than from a curated test set. The paper's motivation for this is that curated evaluation "may exhibit balanced performance on curated benchmarks while concealing residual biases triggered by contextual cues."[^c12]

Relation to tilting: the objective is a log-prior plus λ times a log-likelihood term, the same exponential-tilt shape as in [[consensus-reward-tilting]], with the generator's attribute probability in the place of a majority-agreement reward. What survives the transfer is the shape: the prior is kept, the reward reweights it, and λ sets how far the search may leave the prior. What does not survive is the closed-form optimum. The paper does not derive a tilted distribution, and it decodes by beam search rather than sampling from a tilt (my inference from the text).

## Limits

- Naturalness is judged by GPT-2 perplexity and by how often the attribute appears in images. No human rating of the prompts is reported in the text read, so "natural-sounding" rests on those two numbers.
- The attribute set is small. "Our method uses a limited number of attributes to represent gender and race attributes."[^c13] The study is binary (male/female, white/black): "we constrained our study to male-female or white-black."[^c14]
- The classifier and the language model both carry their own biases. "Both of these models can and do influence the generation of the prompts."[^c15] A discovered prompt is therefore partly a product of the prior and the probe, and the measured frequency is not the generator's bias alone.
- Attribute-revealing prompts are removed before measurement, "we remove the prompts that disclose the value of the attribute of interest."[^c16] That filter is applied with an LLM, and its error rate is not reported in the text read (my inference). It decides which prompts count.
- The method needs grey-box access, the paper's term for models whose intermediate activations can be read.[^c19] A closed generator that exposes no activations cannot supply the attribute term.
- The main experiments cover SD 1.5 and two debiased variants; the newer models appear in an appendix, where "we present experiments with four newer diffusion TTI models," on gender only.[^c17]
- The paper shows that discovered prompts reveal biases. It does not show that mitigation improves when they are used. The suggestion that "Biases discovered by BGPS can then be added to the training set of different mitigation methods" is not tested here.[^c18]

## Related

- [[consensus-reward-tilting]] — the same log-linear form, prior times a reward; there the reward is agreement with a majority, here the probability of an attribute in another model's output.
- [[evolutionary-prompt-search]] — also searches wording against a target's score, but treats the target as a black box and recombines a population instead of decoding from an LLM prior.
- [[minimal-edit-prompt-attack]] — searches wording for a change in a model's answer; here the objective is a distribution over an attribute, not a flipped answer.
- [[mean-difference-steering-vector]] — also reads a direction in a model's hidden states; here a linear head is trained as a classifier and used as a score, not added back as a vector.

[^c1]: arxiv-2512-08724 — "we introduce Bias-Guided Prompt Search (BGPS), a framework that automatically generates prompts that aim to maximize the presence of biases in the generated images"
[^c2]: arxiv-2512-08724 — "regularizes against degenerate and unnatural text or text that does not respect the instructions"
[^c3]: arxiv-2512-08724 — "The second term favours prompts that lead to biased generations"
[^c4]: arxiv-2512-08724 — "We use Mistral-7B-v0.2 as the default language model prior for prompt generation"
[^c5]: arxiv-2512-08724 — "controls the relative influence of the classifier and LLM scores"
[^c6]: arxiv-2512-08724 — "by their average tendency to generate biased outputs across multiple generations"
[^c7]: arxiv-2512-08724 — "is unfortunately deterministic, which does not let us sample different biased prompts"
[^c8]: arxiv-2512-08724 — "gradient-based prompt optimization discovers high-bias regions but produces unreadable text"
[^c9]: arxiv-2512-08724 — "produces unnatural prompts with very high perplexity"
[^c10]: arxiv-2512-08724 — "while it frequently reveals the attribute of interest"
[^c11]: arxiv-2512-08724 — "using a different language model than the one we used for our method, specifically GPT-2"
[^c12]: arxiv-2512-08724 — "may exhibit balanced performance on curated benchmarks while concealing residual biases triggered by contextual cues"
[^c13]: arxiv-2512-08724 — "Our method uses a limited number of attributes to represent gender and race attributes"
[^c14]: arxiv-2512-08724 — "we constrained our study to male-female"
[^c15]: arxiv-2512-08724 — "Both of these models can and do influence the generation of the prompts"
[^c16]: arxiv-2512-08724 — "we remove the prompts that disclose the value of the attribute of interest"
[^c17]: arxiv-2512-08724 — "we present experiments with four newer diffusion TTI models"
[^c18]: arxiv-2512-08724 — "Biases discovered by BGPS can then be added to the training set of different mitigation methods"
[^c19]: arxiv-2512-08724 — "be applied to models with grey-box access (intermediate activations)"
[^c20]: arxiv-2512-08724 — "we sample the first token from the full LLM logits distribution"
