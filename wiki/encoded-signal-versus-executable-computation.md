---
description: "A probe can recover a problem feature from an LLM's hidden states where direct querying fails, because the states hold a statistical signal of the feature, not the procedure that computes it."
aliases: ["encoded signal versus computation", "statistical signal versus executable computation", "decodable but not computed"]
sources: ["arxiv-2512-13374"]
---
# Encoded signal versus executable computation

A frozen LLM can carry a feature of a combinatorial optimization instance in its hidden states and still fail to return that feature when asked. Da Ros, Di Gaspero and Roitero test five "open-weight models from 3B to 120B parameters across the Llama instruct" and gpt-oss families on four problems, and read the same instance-level features two ways.[^c8] Direct querying reads a number from the generated output. Probing trains a regressor on the hidden states. The two readouts come apart in a patterned way. Direct querying recovers feature values "reliably only when they can be read off the input with little or no computation"[^c1], and the abstract puts the same split as "a limited ability to recover features explicitly, particularly those requiring structured computation."[^c2] The probe decodes the same features with lower error, most of all on the harder complexity groups.

The authors name what the probe reads. It is "an encoded statistical signal and an executable computation."[^c3] On their reading, the hidden state "captures statistical regularities of the input–feature relation without instantiating a procedure that computes the feature exactly."[^c4] The feature is defined by a deterministic procedure that maps the raw instance to a value. The model's written output only approximates that procedure, while the probe recovers a regularity that is correlated with the feature. So a successful probe shows that the feature is available in the state. It does not show that the forward pass runs the computation that defines the feature. The authors keep to this descriptive reading: they "deliberately avoid interpreting this dissociation as direct evidence either for or against model comprehension."[^c5]

Scale moves the two readouts differently. Explicit retrieval improves with model size, but it does not reach handcrafted extraction. The null rate on features rises in parallel, and larger models become "more likely to abstain on features where the answer requires actual computation."[^c6] The probe's accuracy is roughly constant across sizes, "comparable accuracy across model sizes."[^c7] So in this range scale narrows the error of the answers the model commits to, and widens the set of features it declines to answer, while the encoded signal stays where it was.

For asking and answering with a model as the instrument, the consequence is this. A feature the model cannot state is not thereby absent from its states. A stated number that needs computation is the least reliable part of the reply, because the reply may be an approximation of a procedure the forward pass did not run. The question "can the model say X" and the question "does its state carry X" are different, and the gap between them is widest where X has to be computed rather than read off a pattern. This extends [[prompt-probe-capacity-gap]], which measured the same readout split for time-series labels. A label there is a recognizable pattern, while here the target is a quantity defined by an algorithm. The dissociation is also the one found for solvability in [[knowledge-verbalization-dissociation]], where the hidden state holds a fact and generation follows a different direction.

My inference, not the paper's: the axis that separates the two cases is how much computation the feature needs. The paper groups features by complexity but does not isolate computation depth from other sources of difficulty, so the axis is read from its groups and not tested as such.

## Limits

- Four problems, five models and a stratified 5% subset of the benchmark. The claim is about these settings, not about LLMs in general.
- The scaling claims rest on a fit across five models, so the trend between sizes is a few points, not a curve (my inference).
- Decodable is not used. A probe shows what the state makes available, not whether generation uses it. This is the limit that [[prompt-probe-capacity-gap]] states for its own probes, and it applies here too.
- The probe is a regressor on pooled hidden states. A different probe could read more or less of the same signal, and the paper does not test a nonlinear alternative for this comparison.
- The paper is explicit that it does not settle whether the separation means comprehension or its absence. Calling the probed quantity a "signal" is the authors' term and carries no claim about mechanism.

## Related

- [[prompt-probe-capacity-gap]] — the same readout split for time-series labels, where the target is a pattern rather than a computed value
- [[knowledge-verbalization-dissociation]] — the same asymmetry as a linear direction for unsolvability
- [[output-accuracy-format-gap]] — what a null from a failed output structure hides, which the abstention-versus-failure split here also bears on
- [[internal-prober]] — a probe on hidden states used as a predictor, the use this work makes of the probe in algorithm selection

[^c1]: arxiv-2512-13374 — "reliably only when they can be read off the input with little or no computation"
[^c2]: arxiv-2512-13374 — "a limited ability to recover features explicitly, particularly those requiring structured computation"
[^c3]: arxiv-2512-13374 — "an encoded statistical signal and an executable computation"
[^c4]: arxiv-2512-13374 — "without instantiating a procedure that computes the feature exactly"
[^c5]: arxiv-2512-13374 — "We deliberately avoid interpreting this dissociation as direct evidence either for or against model comprehension"
[^c6]: arxiv-2512-13374 — "more likely to abstain on features where the answer requires actual computation"
[^c7]: arxiv-2512-13374 — "comparable accuracy across model sizes"
[^c8]: arxiv-2512-13374 — "open-weight models from 3B to 120B parameters across the Llama instruct"
