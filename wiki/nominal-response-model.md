---
description: "For items with more than two options, the nominal response model applies a softmax over linear ability terms; under uniform guessing among wrong options it reduces to a shifted 2PL."
aliases: ["NRM", "nominal model"]
sources: ["arxiv-2601-02580"]
---
# Nominal response model

The two-parameter logistic gives a probability for a yes-or-no response. Once an item offers n options, the natural extension is to give every option its own linear term in ability and take a softmax over all of them. The paper states the ansatz this way: "is the result of the softmax operator applied to a collection of n linear functions of θ".[^n1] Each option v_i carries a slope a_i and a location b_i, and the probability of choosing v_i is its exponentiated term divided by the sum over all options. The paper names this generalization "known as the Nominal Response Model (NRM)".[^n2]

The mechanism is that each option has its own curve. A distractor's probability can rise or fall with ability on its own terms, which a single logistic cannot express. The probability of the keyed answer read from the NRM is therefore a share among all options, not a logistic in θ.

**Reduction to the two-parameter form.** In general the NRM does not collapse to one curve: "a response being correct is not generally equivalent to an equation of the form (1)".[^n3] It does collapse under one assumption, the special case in which "the other options are chosen with equal probability".[^n4] The paper states the resulting correspondence "under the assumption that testtakers choose uniformly at random from the remaining options when incorrect".[^n5] The correct-answer probability then becomes a logistic with a shifted difficulty, and the paper's equation (4) gives the two-parameter discrimination as the option's a and the difficulty as b plus log(n − 1) over a.[^n6]

My reading of that shift: with n = 2 the shift is zero, and each added wrong option adds log(n − 1) to the offset, divided by the discrimination. Under the uniform assumption, an item with more options therefore reads as harder on the two-parameter scale, even when the underlying option terms are the same.

**Use in the paper.** The BEA 2024 data had no student responses, so the uniform assumption was the only route: "the uniform randomness of incorrect choices was assumed to utilize the correspondence in equation (4)".[^n7] The NRM also serves as a smoothing device when responses are available. Fitting a softmax to label-conditioned response counts, rather than taking the raw ratio, avoids the problem that "this quantity can be a bad estimate with very few observations associated with a particular label".[^n8] The fitted model "represents a smooth version of the empirical observed" proportions.[^n9]

## Limits

- The reduction is an assumption, not a result. Real wrong options are not equally likely, and the note on [[distractor-strength-reward-signal]] measures exactly this unevenness in a different setting. Under unequal attractiveness the single-logistic reading of an item is biased (my inference, not tested in the paper).
- The paper's BEA results rest on the uniform assumption, not on observed student choices, so they check the assumed mapping only against the benchmark's own difficulty labels.
- The option-count shift means items with different numbers of options land on different two-parameter scales unless the shift is removed. The paper does not discuss this; it follows from equation (4) as I read it.
- The reduction keeps only the keyed option's terms; the slopes of the distractors are discarded when the model is collapsed.

## Related

- [[item-characteristic-curve]] — the two-parameter form that the NRM reduces to under uniform guessing
- [[simulated-respondent-icc]] — trains an LLM to match a softmax of the NRM's kind over answer tokens
- [[distractor-strength-reward-signal]] — measures the uneven attractiveness of wrong options that the uniform reduction assumes away

[^n1]: arxiv-2601-02580 — "is the result of the softmax operator applied to a collection of n linear functions of θ"
[^n2]: arxiv-2601-02580 — "known as the Nominal Response Model (NRM)"
[^n3]: arxiv-2601-02580 — "a response being correct is not generally equivalent to an equation of the form (1)"
[^n4]: arxiv-2601-02580 — "the other options are chosen with equal probability"
[^n5]: arxiv-2601-02580 — "choose uniformly at random from the remaining options when incorrect"
[^n6]: arxiv-2601-02580
[^n7]: arxiv-2601-02580 — "the uniform randomness of incorrect choices was assumed to utilize the correspondence in equation (4)"
[^n8]: arxiv-2601-02580 — "this quantity can be a bad estimate with very few observations associated with a particular label"
[^n9]: arxiv-2601-02580 — "represents a smooth version of the empirical observed"
