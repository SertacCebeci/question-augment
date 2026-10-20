---
description: "A decoding-time logit correction that pushes the user's next-token distribution toward context or memory only where the two branches diverge, scaled by each source's reliability."
aliases: ["JSD-gated logit correction", "branch-conflict activation gate", "signed logit arbitration", "reliability-scaled token correction"]
sources: ["doi-10-48550-arxiv-2608-16515"]
---
# Conflict-gated logit correction

Some decoding-time methods add a fixed bias to a chosen token set. The mechanism here is different: it keeps the user's next-token distribution as the base and multiplies it by a ratio between two alternative sources, with the exponent set at each step. The sources are a context branch and a memory branch, each a separate next-token distribution computed from a different prompt. The paper's implementation uses a support snippet from the retrieved passage for the context branch, "we instantiate it with a support snippet selected from" the context, and an ensemble of closed-book prompt variants for the memory branch.[^c1][^c2]

## The three steps

The correction is computed in three steps, each of which can switch it off.

First, activation. At each decoding step the method measures how far the context and memory branches disagree, using the Jensen-Shannon divergence between the two distributions. "We therefore measure distributional conflict at step t between" the branches,[^c3] over a renormalised top-K set rather than the full vocabulary, as the paper's efficiency choice.[^c11] The divergence is converted to a soft gate with two thresholds and a sharpness, "with τlow = 0.10, τhigh = 0.35, and γ = 2.0."[^c4] Below the lower threshold the gate is closed, so two branches that agree leave the user distribution alone. Between the thresholds the gate opens gradually: the paper describes the gate as one that "gradually activates intervention as source conflict increases."[^c5]

Second, direction. Conditioned on activation, the sign of the coefficient is set by two signals: the instruction mode, which encodes how far the user wants context trusted, and an entropy-based confidence for each branch. Confidence is one minus the normalised entropy of the branch's top-K distribution, so a concentrated branch scores high. The paper's summary is that "Thus, IGD intervenes only under source conflict, chooses the" direction from intent and branch confidence.[^c6] A positive coefficient favours the context branch, a negative one the memory branch.

Third, reliability scaling. The magnitude is rescaled by how well the favoured source is supported. For context, the support score combines how much the selected snippet supports the context answer with the snippet's evidential quality. For memory, it is the answer consistency across the closed-book prompt variants. The purpose, in the paper's words, is that it "prevents confident but poorly supported context from exerting excessive" influence,[^c7] and similarly keeps unstable memory predictions from overriding context.

The update is a ratio, not an additive bias. As I read the paper's equation, the user distribution is multiplied by the context-to-memory ratio raised to the coefficient, then renormalised. Positive coefficients move mass toward tokens the context branch prefers; negative ones move it toward tokens the memory branch prefers. (My reading of the equation, not a quoted claim.)

## What the ablation says

On Qwen2.5-14B, the paper removes each component in turn. The largest drop comes from removing the correction itself: "Removing token-level correction causes the largest degradation, reducing" truth-mode factual accuracy sharply, and the paper's reading is that token-level correction is the main steering mechanism, not a memory-side add-on.[^c8][^c9] Strict-mode factual context accuracy also falls, "from 90.1 to 83.1,"[^c10] which is the sign that the same mechanism is doing work in the context direction too.

## Limits

- Most of the constants are chosen by the authors: the gate thresholds, the sharpness, the reliability floors, the top-K size. The slices of the paper I read do not include a sweep of the gate thresholds; the only sensitivity reported is for the mode prior and the strength of the correction. (My reading.)
- The divergence is computed over a renormalised top-K set, "rather than the full vocabulary we use K = 16."[^c11] Conflicts that sit in the tail of the distribution are invisible to the gate by construction.
- It needs next-token distributions from several passes: the user branch, the context branch, and the closed-book memory variants. The method as described therefore requires access to logits; a black-box API that returns only text cannot run it. (My inference from the design.)
- The memory side is only as good as the closed-book model. The paper notes that memory-side correction is "naturally limited" by what the model can recover without the context, so the gate cannot create a correct memory answer that is absent.
- The reliability scaling reads the snippet's support by a lexical localizer and a judge; the paper reports that swapping in a stronger localizer did not improve results, so the scaling's behaviour depends on which snippets it is fed rather than on snippet quality in general.[^c12] (The paper's own finding, in its discussion of a stronger localizer.)
- Everything is measured on short-form QA with alias matching, on the paper's own setup.

## Related

- [[intent-conditioned-source-arbitration]] — the intent-level policy that sets the direction this correction takes
- [[context-fidelity-boosting]] — an always-on additive bias on source-supported tokens, scaled by a divergence from the context-free distribution; it has no memory branch, no gate and no intent input (my comparison)
- [[null-image-logit-subtraction]] — another decoding-time contrast of a main pass against a prior-only pass, by subtraction and without a gate
- [[parametric-suppression]] — the layer-level account of why memory can hold an answer that the final output loses, which is the situation the memory branch is built to exploit (my inference)

[^c1]: doi-10-48550-arxiv-2608-16515 — "we instantiate it with a support snippet selected from"
[^c2]: doi-10-48550-arxiv-2608-16515 — "implement the memory branch as an ensemble of M prompt"
[^c3]: doi-10-48550-arxiv-2608-16515 — "We therefore measure distributional conflict at step t between"
[^c4]: doi-10-48550-arxiv-2608-16515 — "with τlow = 0.10, τhigh = 0.35, and γ = 2.0."
[^c5]: doi-10-48550-arxiv-2608-16515 — "gradually activates intervention as source conflict increases."
[^c6]: doi-10-48550-arxiv-2608-16515 — "Thus, IGD intervenes only under source conflict, chooses the"
[^c7]: doi-10-48550-arxiv-2608-16515 — "confident but poorly supported context from exerting excessive"
[^c8]: doi-10-48550-arxiv-2608-16515 — "Removing token-level correction causes the largest degradation, reducing"
[^c9]: doi-10-48550-arxiv-2608-16515 — "indicates that token-level correction is not merely a memory"
[^c10]: doi-10-48550-arxiv-2608-16515 — "strict-mode factual context accuracy from 90.1 to 83.1."
[^c11]: doi-10-48550-arxiv-2608-16515 — "rather than the full vocabulary we use K = 16."
[^c12]: doi-10-48550-arxiv-2608-16515 — "IGD does not only need a snippet that is semantically"
