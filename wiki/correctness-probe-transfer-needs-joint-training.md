---
description: "A correctness probe trained on one dataset transfers near chance because the direction is misoriented, not absent; joint multi-dataset training restores 0.73-0.91 AUC on instruction-tuned models."
aliases: ["cross-domain probe transfer", "orthogonal truth directions"]
sources: ["arxiv-2602-08159", "doi-10-48550-arxiv-2406-05328", "doi-10-48550-arxiv-2609-10739", "arxiv-2512-20578"]
---
# Correctness-probe transfer needs joint training

A correctness subspace that is clean in one dataset is not thereby transferable. A probe fit on TruthfulQA alone scores 0.39-0.66 AUC on SciQ, CSQA and FEVER.[^c1] The failure is one of orientation: refitting natively on each dataset recovers a decodable signal in-domain everywhere.[^c2] HaluEval is the sharp case: a TruthfulQA probe scores 0.18-0.47 (below chance) yet native refitting gives 0.99, and the two directions are nearly orthogonal (|cos θ| = 0.08).[^c3] Below-chance is the signature of a direction present but pointed elsewhere.

## The fix and its bound

Constraining the subspace with several datasets (leave-one-out joint training) lifts transfer on instruction-tuned models, e.g. Mistral-7B +42/+33pp; GPT-2 base models gain only +0.3 to +5.2pp.[^c4] Model class and scale are confounded in the grid, so the boundary is a limit on the recipe, not on capacity.[^c5] Probes also do not transfer between models: a GPT-2 probe on GPT-2-Medium reaches 0.59 and the reverse is chance; what is shared is the structure of the encoding, not probe parameters.[^c6] A different result comes from a head that reads whole generation traces, not one final-token state. Trained on a Qwen3 1.7B backbone, it is applied without refitting to its 4B and 8B siblings, and on math reasoning it scores 0.93 AUROC, which is "nearly matching the 0.96 achieved by a" head trained on the target model itself.[^c9][^c10] The paper says the transfer "is most effective when models" share a generation style, and that it works less well from thinking models to instruct models.[^c11] My inference: this is transfer within one model family and one readout, so it does not overturn the between-model failure above; whether it holds across families is not tested in the paper.

## For asking and answering

My inference: a verifier calibrated on one question type should not be trusted on another type; its score is evidence only within the distribution that fixed its direction.

## Limits

Causal validation is in-distribution; cross-distribution causal transfer is untested. Teacher-forced setting only. Five instruction-tuned models; HaluEval excluded from averages.

## Related

- [[misconception-regime-output-confidence-failure]] — the same paper's regime result.
- [[pre-generation-success-probe]] — a probe whose labels are likewise model- and policy-specific.
- [[accuracy-masks-selective-reliability]] — in-domain scores overstating reliability.
- [[cross-model-domain-adaptation-probe]] — for a non-factuality probe on question representations, unlabeled alignment carried it across four LLMs, with the source probe adapted rather than refit on target labels.[^c7]
- [[perfect-aliasing]] — a candidate mechanism for the sign failure here: when the fitting labels cannot separate two targets, a fitted direction can read the wrong one, and a below-chance score does not say which (my inference from the paper's identity, not its claim about this setting).[^c8]

[^c1]: arxiv-2602-08159 — "A probe fit on TruthfulQA alone transfers close"
[^c2]: arxiv-2602-08159 — "The failure is one of orientation, not of absence."
[^c3]: arxiv-2602-08159 — "essentially orthogonal (| cos θ| = 0.08)"
[^c4]: arxiv-2602-08159 — "The gain is bounded by"
[^c5]: arxiv-2602-08159 — "model class and scale are confounded in our"
[^c6]: arxiv-2602-08159 — "What is shared across"
[^c7]: doi-10-48550-arxiv-2406-05328 — "(MMD loss with linear kernel), the cross-LLM FacLens can work much better in the target domain,"
[^c8]: doi-10-48550-arxiv-2609-10739 — "the protocol offers no way to tell which they measured."
[^c9]: arxiv-2512-20578 — "it achieves 0.93"
[^c10]: arxiv-2512-20578 — "nearly matching the 0.96 achieved by a"
[^c11]: arxiv-2512-20578 — "this transfer is most effective when models"
