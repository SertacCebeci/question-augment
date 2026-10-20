---
description: "In retrieval-augmented generation, repeated samples can agree on a wrong answer because every sample conditions on the same empty or wrong retrieved state, so agreement hides the error."
aliases: ["retrieval lock-in", "absence lock-in", "presence lock-in", "silent error in RAG"]
sources: ["doi-10-48550-arxiv-2606-22728"]
---
# Retrieval-state lock-in

A confidence score that reads agreement among sampled answers as reliability assumes the samples are independent draws of the error. In a retrieval-augmented pipeline they may not be. The paper's definition: a silent error for which "repeated samples condition on the same defective retrieval state."[^c1] The retriever returns a state, the generator samples answers conditioned on that state, and if the state is the same in every draw, the sampling has no way to show that the state was wrong. The answers agree because the error is stable, not because it is right.[^c2]

The worked case is a question about which pharaoh the temple in front of the Osireion honours. The gold answer is Seti I, but the retriever anchors to Ramesses II, the pharaoh of an adjacent temple. "Sample the answer five times and it returns Ramesses II every time," with zero disagreement and a coherent graph trace.[^c3] A black-box estimator that reads agreement as confidence sees nothing to flag. Only the evidence check fires, because "retrieved passages contradict the confident answer."[^c4]

The paper names two variants, and both count as lock-in for the same reason: "the fixed retrieval state, empty or wrong, is what defeats sampling."[^c5] In absence lock-in the retriever returns no usable state and the model answers from parametric memory. In presence lock-in the retriever returns a coherent but wrong neighbourhood. The observable signature is a silent error: a wrong answer with zero answer-state dispersion across the samples. At five samples per question, "errors carry zero answer dispersion, so agreement has nothing to rank," which the paper reports as 42% of errors in its knowledge-graph pipeline and 59% in its dense-retrieval pipeline.[^c6] The share varies with the dataset, from 8% to 55% in the paper's six snapshots, so the footprint is a property of the setting and not a constant.[^c7]

The mechanism, in my reading of the paper's factorisation, is this. If the retrieval state is nearly deterministic given the question, then the answers are drawn from a nearly fixed conditional, and the generator's sampling temperature cannot spread them. The spread that agreement-based scores measure is then close to zero whether the answer is right or wrong. This is my inference from the structure, not a result the paper states as such.

## Limits

The silent-error rate is a signature, not a proof. The paper says so directly: "silent-error rates are an upper bound on lock-in prevalence."[^c8] Parametric overconfidence, benchmark ambiguity and answer normalisation leave the same footprint. The paper separates lock-in from parametric overconfidence despite adequate retrieval, which "can look similar at the answer surface, but it is not lock-in."[^c9] The dispersion floor is also implementation-defined: "floor is implementation-defined" on the encoder and the epsilon used.[^c10]

The evidence is one inspectable system, OntoGraphRAG, across six snapshots. The strict stress run that isolates absence is engineered: the result reflects "engineered absence of retrieval, not graph structure alone."[^c11] The paper's clinical stress run shows that every silent error there is an empty-retrieval row, which says that the absence variant dominates that setting, not that presence is rare.[^c12]

Presence lock-in is the harder case. There "the answer surface and the route observable are both silent, leaving only evidence-level checks."[^c13] The paper's audit of the seven rows that no non-answer check flagged found mostly confounders. It did not confirm deep presence lock-in: "confirming that deceptive type needs the crosspassage" entailment replay, and that replay was not run.[^c14]

Not tested here: whether varying the retrieval itself (a different query, a different seed for the retriever) breaks the lock. My inference is that it would, since the lock depends on the state being the same across draws, but the paper does not run that intervention.

## Related

- [[confidently-wrong-low-entropy-regime]] — another blind spot of sample-based confidence: some hallucinations have near-zero entropy, and the remedy there is a probe rather than a state check.
- [[majority-vote-mode-certificate]] — the agreement estimator whose independence assumption lock-in breaks; the mode-margin guarantee needs draws that are not tied to one shared state.
- [[retrieval-state-drift]] — a search agent whose filters drift while the field values look right; the same shape of wrong retrieval state, seen without the surface showing it, in another setting.
- [[pipeline-object-confidence]] — the split of a RAG run into answer, evidence and retrieval state, which is what makes lock-in visible at all.

[^c1]: doi-10-48550-arxiv-2606-22728 — "repeated samples condition on the same defective retrieval state"
[^c2]: doi-10-48550-arxiv-2606-22728 — "the error is stable"
[^c3]: doi-10-48550-arxiv-2606-22728 — "Sample the answer five times and it returns Ramesses II every"
[^c4]: doi-10-48550-arxiv-2606-22728 — "retrieved passages contradict the confident answer"
[^c5]: doi-10-48550-arxiv-2606-22728 — "the fixed retrieval state, empty or wrong, is what defeats"
[^c6]: doi-10-48550-arxiv-2606-22728 — "errors carry zero answer dispersion, so agreement has nothing to rank"
[^c7]: doi-10-48550-arxiv-2606-22728 — "8% on the clinical domain (RealMedQA) to 55%"
[^c8]: doi-10-48550-arxiv-2606-22728 — "silent-error rates are an upper bound on lock-in prevalence"
[^c9]: doi-10-48550-arxiv-2606-22728 — "similar at the answer surface, but it is not lock-in"
[^c10]: doi-10-48550-arxiv-2606-22728 — "floor is implementation-defined"
[^c11]: doi-10-48550-arxiv-2606-22728 — "engineered absence of retrieval, not graph structure alone"
[^c12]: doi-10-48550-arxiv-2606-22728 — "Every silent error in the strict clinical run is an empty-retrieval"
[^c13]: doi-10-48550-arxiv-2606-22728 — "surface and the route observable are both silent, leaving only"
[^c14]: doi-10-48550-arxiv-2606-22728 — "confirming that deceptive type needs the crosspassage"
