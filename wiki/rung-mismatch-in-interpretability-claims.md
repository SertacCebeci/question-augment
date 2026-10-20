---
description: "Interpretability evidence mostly sits on rungs L1-L2 of Pearl's ladder while the claims drawn (this feature is the concept, this circuit is the mechanism) need L3; matching rung to claim is the check."
aliases: ["causal ladder claim-evidence mismatch", "claim-evidence rung gap", "estimand-first interpretability"]
sources: ["arxiv-2602-16698"]
---
# Rung mismatch in interpretability claims

A claim is a question in disguise, and each question belongs to one rung of Pearl's causal ladder: associational (does A correlate with B), interventional (does changing A change B), or counterfactual (for this input, would changing A have changed B).[^c1] The position paper holds that higher rungs need stronger evidence: evidence at one rung does not license claims at the next.[^c2]

## Mechanism

Before measuring, one names the estimand, "the precise quantity a method targets". A probe targets decodability, an associational estimand. That differs from the effect on output of perturbing the decoded concept, an intervention-effect estimand.[^c3] The mismatch arises when evidence from one rung is reported in the language of another. The authors say that "purely associational evidence (L1) is often reported in the language of counterfactual or interventional claims (L3/L2)".[^c4]

Worked on refusal, each rung has a licence and a limit:

- L1: refusal is decodable from this layer. It does not license "the model represents refusal here".[^c5]
- L2: intervening here changes refusal under tested conditions. It does not license "this is the refusal mechanism" or generalisation to novel jailbreaks.[^c6]
- L3: for this forward pass, the intervention would have caused refusal. It does not license generalisation to other inputs without a structural model.[^c7]

Identifiability is a second, separate check. The right rung does not by itself pin down an answer, because the evidence may fit several hypotheses. A correlation is consistent with A causing B and equally with a confounder causing both; interventions can separate these and association cannot.[^c8] The estimand is identifiable up to an equivalence class when it is constant within the class and varies across classes. Estimating it then fixes the class but not the hypothesis inside it.[^c9]

Applied to methods, the paper's Table 1 reads: a sparse autoencoder's sparse basis is L1 evidence and describes a basis without establishing uniqueness; an auto-interpretability description that predicts held-out activation is L1 and leaves the causal role unconfirmed; circuit ablation is L2, an effect for the chosen ablation and not a unique localisation.[^c10] The claims people want from these (unique concepts, semantic assignment, causal attribution) are L3. Auto-interp scores are reported to reach high values even on random structure.[^c11]

The route the authors propose to close the gap is causal representation learning, which seeks assumptions under which latents are recovered up to a simple equivalence class such as permutation and rescaling, typically from observations under multiple interventions.[^c12] If natural perturbations always move two concepts together, the identified quantity will not separate them.[^c13]

## Limits

- It is a position paper. The ladder mapping is argued and tabulated; this slice shows no measurement of how often mismatches occur or of how much they cost.
- I read only the opening of the text (about the first 400 of 3,444 lines). The diagnostic framework, the affordance argument and the later sections are not covered here.
- Whether CRL assumptions hold for real LLM activations is called "the practical question" by the authors, not settled.[^c14]
- Transfer to question asking and answering is my inference, not the paper's: a question names its estimand and rung, and an answer should state which rung its evidence reaches.

## Related

- [[claim-evidence-reasoning]] — a scaffold for tying a claim to evidence by reasoning; this note says which evidence a claim of a given kind needs.
- [[prerequisite-gated-decodability]] — decodability is an L1 result; whether it implies use needs an interventional test.
- [[knowledge-verbalization-dissociation]] — another case where what is readable differs from what is acted on.

[^c1]: arxiv-2602-16698 — "Query: Does A correlate with B?"
[^c2]: arxiv-2602-16698 — "L(k) evidence does not license L(k+1) claims"
[^c3]: arxiv-2602-16698 — "a probe targets decodability of a concept (an associational estimand)"
[^c4]: arxiv-2602-16698 — "purely associational evidence"
[^c5]: arxiv-2602-16698 — "Refusal is decodable from this layer."
[^c6]: arxiv-2602-16698 — "Intervening here changes refusal under"
[^c7]: arxiv-2602-16698 — "For this forward pass, the intervention"
[^c8]: arxiv-2602-16698 — "Interventional"
[^c9]: arxiv-2602-16698 — "estimating the estimand determines the class, but not the hypothesis within it."
[^c10]: arxiv-2602-16698 — "An intervention effect for the chosen"
[^c11]: arxiv-2602-16698 — "auto-interp scores can attain high values even on random structure"
[^c12]: arxiv-2602-16698 — "Typically, identifiability requires"
[^c13]: arxiv-2602-16698 — "the identified quantities will not reflect sentiment or topic"
[^c14]: arxiv-2602-16698 — "The practical question is whether"
