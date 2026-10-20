---
description: "A latent concept is the moral orientation an input activates inside the model; under repeated self-correction instructions that activation converges and is pushed by immoral instructions."
aliases: ["latent concept", "activated latent concept", "concept activation by instruction"]
sources: ["doi-10-48550-arxiv-2406-02378"]
---
# Latent concept activation

A latent concept is the hidden orientation a text carries without stating it. The paper defines it as "moral orientation within an input sentence," such as toxicity or an implied stereotype: "One example is the surgeon asked the nurse a question, he ..., wherein the statement expresses an implicit gender stereotype that surgeons should be male."[^c1] The authors take the notion from the mechanistic reading of in-context learning, where "activated by instructions" latent concepts are "a critical signal" for what a model outputs.[^c2] The claim being tested is that a self-correction instruction activates a concept in the model, and that the activated concept is what moves the model's uncertainty.[^c3]

The concept is measured with a linear probe, not read from the output. For toxicity, the authors train a one-layer classifier on the Jigsaw data and "use the weight dimension of the classifier corresponding to non-toxicity as the probing vector," then take a score "measuring its similarity to the hidden states across all layers and averaging the results."[^c4] For social stereotypes, which are "not explicitly stated in language but are implicitly embedded within it," they build biased statements instead.[^c5] The reading at each round is therefore a similarity between hidden states and a fixed direction, averaged over layers.

Two properties are reported. The first is convergence: "the activation of negative concepts, such as stereotypes in QA tasks and toxicity in generation tasks, eventually converges after several rounds."[^c6] The second is irreversibility, which the authors test by injecting immoral instructions at fixed rounds. Their finding is that "once an immoral instruction is introduced, the activated concept immediately becomes significantly more" toxic, "even if only moral instructions were applied in previous rounds."[^c7] Moral instructions, read the other way, keep the concept at non-toxicity. The authors summarise the direction as "immoral instructions drive the activated concept towards toxicity, while moral instructions guide it towards" non-toxicity.[^c8]

The link to uncertainty is a prediction task. Two rounds are sampled from a trajectory, the change in concept is the input, and a logistic regression predicts whether uncertainty rose or fell. The authors report that "The model achieves an average accuracy of 83.18%, with a variance of 0.00024."[^c9] From this they conclude that "the concept activated through self-correction instructions is a strong driving force for the change in model uncertainty."[^c10] The concept is therefore the variable linked, by this test, to the uncertainty drop in [[intrinsic-self-correction-convergence]].

## Limits

- The concept is whatever the probe picks out. The text does not show that the toxicity probe reads a moral orientation rather than surface vocabulary or a dataset artefact (my inference).
- The probe is trained on one dataset for one concept. The stereotype measure uses constructed biased statements, not natural text, so the two concepts are measured by different routes.
- The result is contested. The paper notes that [29] "empirically demonstrates that intrinsic moral self-correction is superficial, as it does not significantly alter immorality in hidden states."[^c11] The present work reads the same kind of hidden-state measure as showing movement, so the two readings disagree on what the probe shows.
- The simulation predicts the sign of an uncertainty change, not its size, and it is a correlation. A classifier that does well at predicting direction does not establish that the concept causes the change. The authors' causal claim rests on their Equation 1 together with this test.
- The irreversibility test uses one direction of injection, immoral instructions at rounds 2, 5 and 8. It shows immoral instructions move the concept; the moral side is shown as convergence, not as a symmetric intervention.
- The paper's Bayesian framing is taken from earlier work on in-context learning, with its assumptions carried over. How that framing applies to instruction-only prompts is the authors' extension, not a separate test.

## Related

- [[intrinsic-self-correction-convergence]] — the uncertainty and calibration trajectory this concept is said to drive.
- [[in-context-learning-as-label-propagation]] — the same latent-concept term from the Bayesian reading of in-context learning, where it is used to explain demonstrations rather than instructions.
- [[calibration]] — the calibration error that the concept-driven uncertainty drop is said to reduce.

[^c1]: doi-10-48550-arxiv-2406-02378 — "One example is the surgeon asked the nurse a question, he"
[^c2]: doi-10-48550-arxiv-2406-02378 — "activated by instructions have been proven to be a critical signal in the mechanistic understanding"
[^c3]: doi-10-48550-arxiv-2406-02378 — "we show that through multi-round intrinsic self-correction, latent concepts are activated, which reduces model uncertainty"
[^c4]: doi-10-48550-arxiv-2406-02378 — "use the weight dimension of the classifier corresponding to non-toxicity as"
[^c5]: doi-10-48550-arxiv-2406-02378 — "Since social stereotypes are not explicitly stated in language but are implicitly embedded within it"
[^c6]: doi-10-48550-arxiv-2406-02378 — "eventually converges after several rounds"
[^c7]: doi-10-48550-arxiv-2406-02378 — "once an immoral instruction is introduced, the activated concept immediately becomes significantly more"
[^c8]: doi-10-48550-arxiv-2406-02378 — "instructions drive the activated concept towards toxicity, while moral instructions guide it towards"
[^c9]: doi-10-48550-arxiv-2406-02378 — "The model achieves an average accuracy of 83.18%, with a variance of 0.00024"
[^c10]: doi-10-48550-arxiv-2406-02378 — "concept activated through self-correction instructions is a strong driving force for the change in model"
[^c11]: doi-10-48550-arxiv-2406-02378 — "intrinsic moral self-correction is superficial, as it does not significantly alter immorality in hidden states"
