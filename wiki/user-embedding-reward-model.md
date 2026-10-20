---
description: "A reward model with one learned embedding per user ID, trained jointly on preference pairs, reaches 80.45% held-out preference accuracy against 69.25% for an off-the-shelf model."
aliases: ["PRMU", "personalization reward model with user embeddings", "user-ID embedding reward model", "learnable user embedding reward"]
sources: ["doi-10-48550-arxiv-2509-23140"]
---
# User-embedding reward model

A reward model scores a candidate response. A personalized one needs to know whose response it is judging, and this design gives it that knowledge through a trainable vector per user. The architecture starts from a general reward model, and "PRMU incorporates learnable user embeddings Eu to capture individual preferences."[^c1] A user ID is first mapped to its embedding, which then enters the score together with the query, the profile, the reasoning chain and the answer.[^c2] The embedding table is not frozen: "the user embeddings E are jointly optimized by minimizing the Bradley-Terry" preference loss, together with the base model's weights.[^c3]

What the embedding can learn depends on the pairs it is trained on. One preference set "contrasts responses generated with a user profile (preferred)" against responses generated without the profile, so the pair teaches the scorer to value use of the profile.[^c4] A second set "contains pairs of personalized responses where preference is determined by correctness or ROUGE", so it teaches discrimination between personalized outputs by quality.[^c5] Both are built by the authors, at about 10k pairs each.

On a held-out set of such pairs, the full model reaches 80.45%, and the paper says it is "achieves the best accuracy (80.45%), substantially outperforming an off-the-shelf reward model" at 69.25%.[^c6] Two ablation statements bear on the embedding's share. Training on the personalization pairs without any user information already improves on the untrained model in the paper's LaMP ablation, "yields improvements across all metrics".[^c7] Adding the embedding gives the best variant, and "PRMU consistently outperforms all other variants".[^c8] These ablation rows are a downstream LaMP comparison, not a held-out preference-accuracy comparison, so the 80.45% figure and the ablation are different evidence.

Inside the composite RL reward the term is weighted lightly. The weights "prioritize logical correctness over personalization to prevent factuality degradation and reward hacking."[^c9] So the user-aware signal is a minor term beside the format, correctness and tag terms, by the authors' design.

The transferable part is the idea of a user-indexed latent that a reward can read, fitted from preference pairs in which the profile is the variable. What does not transfer on the evidence read is any claim about users outside the training pairs: the text does not describe how a user absent from the preference data is scored (my reading: an ID-indexed table has no entry for a new user). Compare the Bayesian route in [[factored-versus-entangled-supervision]], where a latent user vector is a posterior updated online from answers rather than a point estimate fitted offline per ID.

## Limits

- The authors measure "the standalone preference prediction accuracy of PRMU variants on a held-out set."[^c10] The text does not say whether held-out users also appear in training, so the 80.45% does not establish performance on new users.
- Privacy: "The use of learnable user embeddings and deep personalization introduces potential privacy concerns regarding user data retention and the risk of reinforcing existing user biases or creating echo chambers."[^c11] The paper names the risk and calls for further research; it does not measure it.
- The "personal" in the pairs is what the two preference sets encode: whether the profile was used, and whether one response scores higher on correctness or ROUGE. Preferences a user has not expressed in those forms are not tested.
- The term is weighted at γ = 0.2 in the composite reward, and the paper's sensitivity analysis varies these weights only within a reasonable range. Whether the embedding would matter more under a different weighting is not tested.
- Results are reported on LaMP, LongLaMP, PGraphRAG and one self-constructed set. The paper does not compare the embedding with explicit rubric-based scoring of the same profile.

## Related

- [[personal-rubric-reward-gap]] — the same reward-model problem, handled by reading explicit rubrics from the profile instead of learning a user vector
- [[factored-versus-entangled-supervision]] — a latent user embedding there is a posterior updated online from answers; here it is a point estimate fitted offline per ID
- [[personalization-privacy-tradeoff]] — the privacy cost of personalization, which the paper raises specifically for learnable user embeddings

[^c1]: doi-10-48550-arxiv-2509-23140 — "PRMU incorporates learnable user embeddings Eu"
[^c2]: doi-10-48550-arxiv-2509-23140 — "first maps a user ID idu to its corresponding embedding"
[^c3]: doi-10-48550-arxiv-2509-23140 — "the user embeddings E are jointly optimized by minimizing the Bradley-Terry"
[^c4]: doi-10-48550-arxiv-2509-23140 — "contrasts responses generated with a user profile (preferred)"
[^c5]: doi-10-48550-arxiv-2509-23140 — "contains pairs of personalized responses where preference is determined by correctness or ROUGE"
[^c6]: doi-10-48550-arxiv-2509-23140 — "achieves the best accuracy (80.45%), substantially outperforming an off-the-shelf reward model"
[^c7]: doi-10-48550-arxiv-2509-23140 — "yields improvements across all metrics"
[^c8]: doi-10-48550-arxiv-2509-23140 — "PRMU consistently outperforms all other variants"
[^c9]: doi-10-48550-arxiv-2509-23140 — "prioritize logical correctness over personalization"
[^c10]: doi-10-48550-arxiv-2509-23140 — "We evaluate the standalone preference prediction accuracy of PRMU variants on a held-out set"
[^c11]: doi-10-48550-arxiv-2509-23140 — "The use of learnable user embeddings and deep personalization introduces potential privacy concerns"
