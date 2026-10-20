---
description: "A confidence gate can be fully controlled by its threshold yet fail to track the evidence behind an answer: cutting video frames from 18 to 6 left median confidence at 0.9."
aliases: ["confidence contraction under evidence loss", "epistemic validity of a confidence gate", "evidence-conditioned confidence"]
sources: ["arxiv-2601-00138"]
---
# Evidence sensitivity of confidence

A confidence gate has two properties that are easy to run together. The first is mechanistic. The system accepts an answer only when its confidence reaches a threshold ε, and sweeping ε traces a risk–coverage curve. On NExT-QA with Gemini 2.0 Flash, "Sweeping threshold ε produces smooth risk-coverage tradeoffs, reducing error rates" from 23.6% to 9.4% at 63.7% coverage.[^c1] The gate is set by the designer, not read from the model's own abstain flag: the paper defines abstention "at the system level based solely on a confidence threshold ε, rather than relying" on the model's decision.[^c2]

The second property is evidential: does confidence fall when the evidence behind an answer falls? The test keeps the same frozen questions and changes only the visual input. The degraded condition uses "with degraded visual evidence: only 6 uniformly sampled" frames, against the usual 15–18.[^c3] At a fixed ε = 0.71 the gate's coverage drops from 63.7% to 53.7%, and "conditional risk remains similar (9.4% vs 9.3%)."[^c4] So the gate answers fewer questions, but the error rate of the answers it keeps barely moves.

The confidence itself barely moves either. Median self-reported confidence "remains 0.9 in both regimes despite a 3× reduction" in visual information.[^c5] Set against the size of the cut, the response is small: "a 67% reduction in evidence produces less than 6%" change in confidence.[^c6] Self-reported confidence falls by 3.3% in the paper's matched comparison, and "logprob-derived pmax actually" rises slightly.[^c7]

The logprob signal is built as follows. A separate single-letter call returns log-probabilities for the five option letters; these are renormalised over A–E, and the largest resulting probability is pmax. "By extracting only the A–E logprobs and renormalizing, we obtain a probability" distribution over the answer space, which is the decoder's preference among options rather than a number the model reports.[^c8] The paper uses it as a second instrument, and it fails in the same direction as the self-report.

The practical consequence is that a threshold set on full evidence is not a setting for a weaker evidence regime. The paper says a deployed system "cannot rely on confidence thresholds tuned in-distribution."[^c9] Its summary is blunter: "Confidence does not track information availability."[^c10] The motivation is information-theoretic. If features carry little information about the label, "no classifier can be highly accurate", so justified confidence should be bounded by what the evidence supports.[^c11] The paper's formal object for that bound is the warrant ζ(e), "the Bayes-optimal predictability of a claim given" an evidence view e.[^c12] My reading is that a gate would need a score bounded by the evidence view, not by the answer alone; the paper states the need, not a construction.

The shift also differs in kind from the usual distribution-shift benchmarks. The paper says "our shift is an intervention on information availability."[^c13] A covariate shift changes the inputs while the answer stays recoverable; frame removal can make the answer unrecoverable. That is why the sensitivity of confidence to information is a separate question from its calibration on a new input distribution.

## Limits

- One model and one dataset. "We evaluate a single model (Gemini 2.0 Flash) on a single dataset (NExTQA)."[^c14] Whether another VLM's confidence contracts under the same frame cut, or whether other video domains behave the same way, is not tested.
- Frames are a proxy for information. "Evidence reduction is not semantic information reduction."[^c15] Many NExT-QA items may stay answerable from sparse keyframes, so a 67% cut in frames is not a 67% cut in what a question needs. The paper mentions a temporal ablation as a stronger intervention; I have not read that appendix for this note.
- Self-reported confidence is a text interface. "Self-reported confidence is a behavioral interface that may not reflect the model" token-level decision.[^c16] The logprob run only partly answers this, and it uses a different prompt: "experiment uses a different prompt interface (single-letter response, no JSON structure), absolute" accuracy levels cannot be compared across the two.[^c17] So the paper compares changes within each interface, not levels across them.
- The warrant is not implemented. "These experiments do not estimate a warrant quantity ζ or enforce warrant-based bounds."[^c18] A note that names ζ(e) describes a proposal, not a method that has been shown to work.
- My own caution: a flat median and a flat conditional risk are summary statistics. They do not show that confidence ranks the answers it keeps badly under degradation, and the paper reports no ranking metric for the degraded condition. This is my inference, not the paper's claim.

## Related

- [[abstention]] — the selective-prediction pair and the risk–coverage curve that a threshold gate instantiates. That framework does not ask whether the score under the gate carries evidence information; this note does.
- [[calibration]] — the paper's ECE is computed on accepted predictions. Good calibration in-distribution says nothing about how confidence responds to less evidence.
- [[conformal-prediction]] — the paper contrasts it with its own aim: "conformal methods control marginal risk under exchangeability (or specified relaxations)," [^c19] so its guarantee is marginal, while the warrant is meant to be per-instance.
- [[score-separability]] — the condition under which a threshold raises selective accuracy at all. An evidence shift is one way that separation can move; this extension is mine.

[^c1]: arxiv-2601-00138 — "Sweeping threshold ε produces smooth risk-coverage tradeoffs, reducing error rates"
[^c2]: arxiv-2601-00138 — "We define abstention at the system level based solely on a confidence threshold ε, rather than relying"
[^c3]: arxiv-2601-00138 — "with degraded visual evidence: only 6 uniformly sampled"
[^c4]: arxiv-2601-00138 — "conditional risk remains similar (9.4% vs 9.3%)."
[^c5]: arxiv-2601-00138 — "median self-reported confidence remains 0.9 in both regimes despite a 3× reduction"
[^c6]: arxiv-2601-00138 — "a 67% reduction in evidence produces less than 6%"
[^c7]: arxiv-2601-00138 — "Self-reported confidence drops only 3.3%, and logprob-derived pmax actually"
[^c8]: arxiv-2601-00138 — "By extracting only the A–E logprobs and renormalizing, we obtain a probability"
[^c9]: arxiv-2601-00138 — "cannot rely on confidence thresholds tuned in-distribution."
[^c10]: arxiv-2601-00138 — "Confidence does not track information availability."
[^c11]: arxiv-2601-00138 — "no classifier can be highly accurate"
[^c12]: arxiv-2601-00138 — "the Bayes-optimal predictability of a claim given"
[^c13]: arxiv-2601-00138 — "our shift is an intervention on information availability."
[^c14]: arxiv-2601-00138 — "We evaluate a single model (Gemini 2.0 Flash) on a single dataset (NExTQA)."
[^c15]: arxiv-2601-00138 — "Evidence reduction is not semantic information reduction."
[^c16]: arxiv-2601-00138 — "Self-reported confidence is a behavioral interface that may not reflect the model"
[^c17]: arxiv-2601-00138 — "experiment uses a different prompt interface (single-letter response, no JSON structure), absolute"
[^c18]: arxiv-2601-00138 — "These experiments do not estimate a warrant quantity ζ or enforce warrant-based bounds."
[^c19]: arxiv-2601-00138 — "conformal methods control marginal risk under exchangeability (or specified relaxations),"
