---
description: "An instruction layer between user prompt and image model fills unspecified attributes with demographic defaults; removing it weakens gender association in the text embedding."
aliases: ["system prompt bias propagation", "default system prompt", "language-side demographic conditioning", "instruction-conditioned text processing"]
sources: ["arxiv-2512-04981"]
---
# Intermediary instruction default fill

In a text-to-image system whose prompt passes through a language model before the image generator, the user's words are not the only thing that conditions the image. A built-in instruction sits in between and tells the model how to interpret and expand the prompt. The paper writes the text embedding as a function of both the user prompt and that default instruction, and finds that these instructions "strongly influence text embeddings".[^c1] The image is then generated from the embedding, not from the words the user typed.

## The mechanism

Where the user leaves an attribute open, the intermediary fills it. For an underspecified prompt such as "A botanist", the authors say the model "may inadvertently fill in missing visual details according to its demographic priors based on LLM self-reasoning".[^c2] The fill is made by a layer the asker did not write and usually cannot see. It becomes visible only when the intermediary's output is decoded or the image is inspected.

## How it was measured

The measurements are on neutral occupational prompts, with and without the default instruction.

First, in the embedding space: removing the instruction "consistently weakens gender associations in the embedding space".[^c3] The change is not a loss of meaning. The paper notes that "reduction is not explained by a loss of semantic" fidelity, since cosine similarity to the original prompt embedding stays comparable in both conditions.[^c4] So the instruction moves the demographic direction of an otherwise neutral representation.

Second, in decoded text: the intermediate text produced from neutral prompts contains gendered terms and demographic descriptors, and removing the instruction substantially reduces them. The authors put it as "system-prompt conditioning can transform neutral user inputs into biased language-side representations".[^c5]

Third, in the image: decoded text and generated images agree on demographic attributes in 64% of occupational prompts.[^c6] The authors read this as the instruction acting as "a bias propagation pathway from language-side processing to visual outputs".[^c7] The 64% is a correspondence across prompts, not an intervention on one slot, so "propagation" is the authors' reading of it.

## What transfers, and what the intervention shows

The structure is an open slot, an intermediary that holds priors, and a probe that reads the intermediary's output. For asking, the point is that the same underspecified request can be completed differently by a layer the asker never sees, so a question left open is not left neutral.

The paper's own remedies are informative here. Rewriting the user prompt to add specificity ("A doctor" becomes "A healthcare professional in diverse settings") "can improve alignment through added specificity" but "does not reliably mitigate demographic bias" while the instruction stays the same.[^c8][^c9] Changing the intermediary worked better. The proposed method, FairPro, generates a fairness-aware instruction per input by LLM self-reasoning and "substantially reduces demographic disparities", a fixed fairness instruction did less, and "a fixed fairness prompt is not sufficient".[^c10][^c11] The second result matters for the transfer: one static guideline is not enough, the intervention has to depend on the particular prompt.

A fair caution from the same paper: removing the default instruction "reduces demographic bias, but could weaken prompt enrichment and instruction following".[^c12] The fill and the enrichment come from the same mechanism. The authors also report that as prompts grow more complex, "prompt adherence can amplify demographic disparities in generated outputs".[^c13] Better fit to the prompt and more skew can rise together, so neither can be read as a sign of the other.

My inference, not the paper's claim: the same slot-filling structure is plausible wherever a model rewrites or expands a question before answering. The paper does not test this. It measures image demographics, not answers to questions.

## Limits

- The study is text-to-image only: eight recent T2I models and a 1,024-prompt benchmark, with occupational prompts at the core.[^c17] No text question-answering or chat answerer was measured.
- The demographic measure uses discrete categories, three gender and seven ethnicity. The authors say this "cannot fully reflect the diversity and fluidity of realworld identities".[^c14]
- The fairness reference is a uniform distribution, and the authors say "what constitutes an appropriate fair distribution is context-dependent and" remains open.[^c15]
- FairPro is test-time and leaves the model unchanged, so it "does not remove biases encoded in" the generative model itself.[^c16]
- The propagation claim rests on correlation (64% agreement) and on removing the whole instruction, not on editing the fill of a single attribute. Whether the fill is causal for the image is the authors' reading.
- Nothing here shows that an asker can prevent the fill by stating attributes explicitly. The rewriting baseline tested one pattern of added specificity only.

## Related

- [[identity-neutral-query-rewriting]] — there a user-side identity cue was stripped from the question; here a user-side rewrite left the intermediary's fill in place, so the two bound each other.
- [[underspecified-question-eager-answering]] — the same filling of an absent detail by an assumed reading, measured in dialogue rather than in images.
- [[attribute-pinning-in-prompt]] — explicit mapping of attributes into the prompt, the asker-side counterpart to leaving a slot open for an intermediary.
- [[debiasing-utility-overcorrection]] — debiasing judged on both bias and fit to the input, the same two-sided measure used here.
- [[demographic-conditioned-mirage]] — demographic descriptors shaping what a model outputs instead of the evidence it is given.

[^c1]: arxiv-2512-04981 — "these instructions strongly influence text embeddings"
[^c2]: arxiv-2512-04981 — "the model may inadvertently fill in missing visual details according to its demographic"
[^c3]: arxiv-2512-04981 — "the system prompt consistently weakens gender associations in the embedding space"
[^c4]: arxiv-2512-04981 — "reduction is not explained by a loss of semantic"
[^c5]: arxiv-2512-04981 — "conditioning can transform neutral user inputs into biased language-side representations"
[^c6]: arxiv-2512-04981 — "decoded text and generated images exhibit 64% agreement in"
[^c7]: arxiv-2512-04981 — "suggesting that system prompts act as a bias propagation pathway"
[^c8]: arxiv-2512-04981 — "does not reliably mitigate demographic bias"
[^c9]: arxiv-2512-04981 — "can improve alignment through added specificity"
[^c10]: arxiv-2512-04981 — "substantially reduces demographic disparities"
[^c11]: arxiv-2512-04981 — "a fixed fairness prompt is not sufficient"
[^c12]: arxiv-2512-04981 — "could weaken prompt enrichment and instruction following"
[^c13]: arxiv-2512-04981 — "prompt adherence can amplify demographic disparities in generated outputs"
[^c14]: arxiv-2512-04981 — "cannot fully reflect the diversity and fluidity of realworld identities"
[^c15]: arxiv-2512-04981 — "what constitutes an appropriate fair distribution is context-dependent and"
[^c16]: arxiv-2512-04981 — "does not remove biases encoded in"
[^c17]: arxiv-2512-04981 — "Evaluations on eight recent T2I models show that LLM-based systems consistently"
