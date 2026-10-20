---
description: "A model that checks its own output with the parameters that produced it shares one noise source between generator and verifier; self-correction then needs a large shared signal-to-noise ratio."
aliases: ["diagonal GVU", "self-verification noise barrier", "shared-noise self-correction barrier", "monolithic self-improvement barrier"]
sources: ["arxiv-2512-02731"]
---
# Hallucination barrier

Take the generator-verifier-updater loop of [[verifier-noise-self-improvement-condition]] in its diagonal form: one model supplies the generator, the verifier and the updater, and the roles differ only by prompt or interface. The paper writes this as G = V = U, which it calls the diagonal regime.[^c1] It describes the wiring as "Diagonal GVU is maximally entangled": the same parameters decide what is proposed, how it is judged, and which updates are admitted.[^c2]

The paper's Corollary 4.2 gives the consequence. If the verifier is the model "simply asks itself" whether its output is correct, then "typically ρ ≈ 1 and σV ≈ σG", so the two noises are equal.[^c3][^c4] The sufficient condition then "reduces, up to constants, to a requirement that the shared SNR be large."[^c5] The paper adds that "this inequality is rarely satisfied when SNRdiag is modest," and that in that regime the expected gain is close to zero or negative, and "the flow tends toward mode collapse or a" noisy random walk.[^c6][^c7]

The mechanism is a shared noise term. In a general loop the verifier adds its own noise to the generator's, and the expected gain has to clear both. In the diagonal loop the two are the same process: "generation and verification inherit the same noise," so the verifier cannot supply the low-variance signal that the generator lacks.[^c8] The paper reads this as the reason naive self-correction does not reach sustained gains: "This helps explain the empirical failure of naive self-correction."[^c9] The point is about which noise can be lowered without copying the generator, not about which role is noisier in principle. The paper notes that the generator "is often intrinsically high-entropy," so it is easier to raise the verifier's SNR by external structure, ensembles or oracles, "even though the sufficient condition (4) itself is symmetric in the two SNRs."[^c10][^c11]

The paper's one in-model escape is a "cold" verifier: the same weights sampled at a lower temperature. In "a stylized Gaussian-noise model where the stochasticity of each role scales" with its temperature, the verifier's variance becomes a small fraction of the generator's when the verifier's temperature is much lower.[^c12] The paper says this "should be read not as a theorem about real networks," and it offers the model as a lens on why strict low-temperature judge prompts help in practice: "interface asymmetries can induce a spectral advantage for verification."[^c13][^c14]

For questioning, the consequence is my reading, not the paper's (the paper does not discuss questions). A model asked to check whether its own question is well posed, using the same weights and the same sampling, is a diagonal loop. On this reading that check adds little signal beyond the generator's own noise unless it is made lower-variance by a different interface, a separate judge, or an external reference. Whether any real question-asking system falls on one side of this line is not measured here.

## Limits

- Theory and a parametric remark, with no experiment. The paper's statements that the barrier is "rarely satisfied" and that self-correction "typically fails" come with no measured threshold or frequency.
- The corollary follows from a sufficient condition. Failing a sufficient condition does not show that the expected gain is negative; the paper's "close to zero or negative" is a description of the regime, not a bound.
- The corollary assumes ρ ≈ 1 and σV ≈ σG. A same-weights judge with a systematic bias changes both terms, and the paper does not analyse that case. The framework takes the noise to be zero-mean, so a judge that is wrong in one direction lies outside the condition (see [[verifier-noise-self-improvement-condition]]).
- The cold-verifier model is stylized. The paper does not measure the variance ratio on any network, and temperature is one source of variance among several.
- The paper does not separate "mode collapse" from "noisy random walk" as the failure mode.
- The link between this barrier and the intrinsic self-correction results in the wiki is an explanation offered by the paper, not a test. None of those measured studies is re-examined here.

## Related

- [[verifier-noise-self-improvement-condition]] — the general condition this note specialises; diagonal GVU is the case where the generator's and the verifier's noise are the same
- [[intrinsic-self-correction-convergence]] — repeated self-correction with no outside feedback converges; the barrier gives a noise-based reason that convergence need not be a gain (my reading; the two works do not discuss each other)
- [[same-model-self-verification-conditional-confidence]] — a same-model check that helps on one benchmark and not another; the barrier predicts when a shared-noise check is weak, and this paper does not test that prediction
- [[population-search-under-noisy-verifier]] — a noisy verifier made usable by sampling many candidates; the barrier is about noise the verifier shares with the generator, which more samples do not by themselves separate (my reading)

[^c1]: arxiv-2512-02731 — "Gθ = Vθ = Uθ = Mθ"
[^c2]: arxiv-2512-02731 — "Diagonal GVU is maximally entangled"
[^c3]: arxiv-2512-02731 — "the model simply asks itself"
[^c4]: arxiv-2512-02731 — "then typically ρ ≈ 1 and σV ≈ σG"
[^c5]: arxiv-2512-02731 — "to a requirement that the shared SNR be large"
[^c6]: arxiv-2512-02731 — "this inequality is rarely satisfied when SNRdiag is modest"
[^c7]: arxiv-2512-02731 — "the flow tends toward mode collapse or a"
[^c8]: arxiv-2512-02731 — "generation and verification inherit the same noise"
[^c9]: arxiv-2512-02731 — "This helps explain the empirical failure of naive self-correction"
[^c10]: arxiv-2512-02731 — "the generator is often intrinsically high-entropy"
[^c11]: arxiv-2512-02731 — "the sufficient condition (4) itself is symmetric in the two SNRs"
[^c12]: arxiv-2512-02731 — "In a stylized Gaussian-noise model where the stochasticity of each role scales"
[^c13]: arxiv-2512-02731 — "This should be read not as a theorem about real networks"
[^c14]: arxiv-2512-02731 — "interface asymmetries can induce a spectral advantage for verification"
