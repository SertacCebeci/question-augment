---
description: "Draft an answer without retrieval, score its length-normalized negative log-likelihood, and retrieve only above a threshold; on low-uncertainty queries retrieval lowers accuracy."
aliases: ["UGT", "decide-then-retrieve triggering", "generation-uncertainty retrieval gate"]
sources: ["arxiv-2601-03908", "arxiv-2512-19134", "arxiv-2512-11935", "doi-10-48550-arxiv-2607-25600", "doi-10-48550-arxiv-2505-04253"]
---
# Uncertainty-guided retrieval triggering

In the Decide Then Retrieve (DTR) framework the answerer first writes an answer from its own parametric knowledge. It then scores that answer with the normalized negative log-likelihood of its tokens, u = -(1/T) log P(answer | query), which "can be computed directly from next-token probabilities".[^c1] A query whose u falls at or under a threshold keeps the no-retrieval answer. Only queries above it trigger retrieval. No classifier is trained, so the gate is tied to the generator that will answer, not to a separately trained router.[^c2]

## What was measured

- Over HotpotQA and NaturalQA with Qwen2.5 generators, exact match of no-retrieval answers falls monotonically as the threshold rises, while the share of queries under the threshold rises. So u ranks queries by how reliable the model's own answer is, and the threshold sets how many may bypass retrieval.[^c3]
- Retrieval is not neutral for confident queries. When uncertainty is low, activating retrieval lowers accuracy relative to no retrieval. As uncertainty rises, the gain from retrieving rises steadily, "showing that retrieval becomes increasingly helpful when parametric knowledge is insufficient".[^c4] This is the paper's account of why always-retrieving RAG adds noise on easy questions.
- Scale changes the curve. The 72B model gains more slowly because of its parametric strength. The 32B model gains most, which the authors attribute to a balance between parametric knowledge and robustness to retrieval noise.[^c5]
- Against an LLM-as-judge trigger, a 7B judge "rarely triggers retrieval", giving results near the no-retrieval baseline, while a 72B judge triggers often yet stays below DTR. The authors read this as an advantage of the uncertainty signal over judge-based decisions.[^c6]
- The threshold is a dial: smaller values trigger more often with slightly better scores on reasoning-heavy sets; larger values retrieve less with marginal accuracy loss.[^c7]
- The gate can read a verbalized confidence instead of token likelihood, for APIs that expose no token probabilities. The paper adopts it for that reason: "Because none of the evaluated endpoints exposes usable" token probabilities, so verbalized confidence is the signal it has.[^c15] A single probe returns "a compact JSON object containing a provisional answer, verbalized confidence", and retrieval fires when that confidence falls below a threshold chosen on validation data and frozen before test.[^c16] Across three model families the confidence is "associated with final F1 across all three model families".[^c17] Its uncertainty "shows a positive but modest association with retrieval benefit", with AUROC 0.628 for predicting a positive retrieval gain.[^c18] This is a relabelling of the same gate with a different signal, not a new mechanism; the token-likelihood results above do not transfer to it without the paper's evidence.

The same gate question arises when the source is a database tool rather than retrieved text. In the AGAPI materials platform, on defective supercells and hypothetical compositions outside the model's training distribution, the answer without tools is far worse: "the tool-free baseline collapses to MAE = 1.86 eV" on the first set, and "versus tool-free MAE = 1.25 eV" on the second, against about 0.003 eV with tools.[^c11][^c12] On canonical properties the sign reverses for three of five properties, where tool augmentation raised error against experiment. The authors conclude that "Agentic systems therefore should not blindly invoke tools for every query."[^c13] The tool-augmented figures on those hard sets are on the diagonal by construction, which the authors call "a property of the circular ground-truth choice", so they do not independently measure accuracy; the tool-free side carries the evidence.[^c14]

Ablating the gate alone gives scores that are "comparable or slightly lower", so the measured benefit is largely saved retrievals plus a modest accuracy gain, not a large accuracy jump.[^c8]

## Limits

- The authors say the gate "relies on the quality of uncertainty estimates derived from token probabilities, which may vary across decoding strategies or model families".[^c9]
- Token likelihood measures confidence, not correctness. A confidently wrong answer gets u low and never reaches retrieval; the paper does not quantify this failure. Elsewhere in the wiki raw likelihood confidence is reported as a weak discriminator in some domains, so transfer is open.
- Evidence is five open-domain QA sets with Wikipedia (HotpotQA with its own corpus); nothing on long-form answers, private corpora or temporal facts where parametric knowledge is stale yet fluent. That case is my inference, not tested.
- The threshold is set per deployment; the paper offers no rule for choosing it.
- It needs a full drafting pass before the decision, adding latency whenever retrieval is triggered.
- A rival gate reads the pre-training corpus instead of the model. QuCo-RAG argues that model-internal signals "are fundamentally unreliable because LLMs are typically ill-calibrated"; its [[corpus-statistics-retrieval-trigger]] reports its gains over internal-signal methods on OLMo-2 with a full corpus index. That paper does not test the single-draft likelihood gate described above, so setting the two side by side is my inference, not a result.[^c10]
- The verbalized score ranks better than it estimates. The paper calls it "more useful as an" ordinal signal, not a probability: "ordinal routing signal than as a calibrated estimate of correctness or retrieval benefit".[^c19] Its calibration error is large, with ECE5 "(ECE5 = 0.426–0.528)" across the three families.[^c20]
- The probe trades tokens for passages. The paper finds the method is "retrieval-saving" but its extra call means that "increases total token usage by 28.2%, revealing a trade-off" against always retrieving.[^c21]
- The benefit is not uniform: the paper reports it weakens "when confidence values cluster near the routing threshold".[^c22]
- The evidence is a controlled setting. The paper lists "the controlled TF–IDF corpus, unmatched execution paths" among its main limitations, so a sparse local index was tested, not open-domain search.[^c23]

## Related

- [[parametric-knowledge-gates-retrieval-noise-damage]] — same finding from the other side: noise hurts where parametric knowledge is weak or reliance on evidence is high
- [[self-answerability-flip-threshold]] — another self-knowledge score that predicts when the model defers to retrieved text
- [[sequence-likelihood-confidence]] — evidence that token-probability confidence can be a weak signal
- [[boundary-novelty-retrieve-or-think-gate]] — a different retrieve-or-not gate, based on embedding novelty not likelihood
- [[uncertainty-gated-lm-fallback]] — the same pattern of gating a costlier path by the cheap path's own uncertainty
- [[corpus-statistics-retrieval-trigger]] — the same retrieve-or-not decision, gated by pre-training corpus counts instead of the model's token probabilities
- [[reference-inherited-error-split]] — when the source is a database tool, splits the error of a tool-augmented answer into the agent's share and the database's
- [[route-count-matched-control]] — the random control that asks whether a confidence gate picks better questions than chance at the same retrieval count
- [[calibration]] — the gate uses verbalized confidence as a ranking, not as a probability; the calibration error is what the gate does not rely on
- [[llm-independent-retrieval-gate]] — a rival gate that drops the answerer's uncertainty and reads question and entity features instead; on six QA sets at least one such feature matched the uncertainty methods[^c24]

[^c1]: arxiv-2601-03908 — "This uncertainty score measures the model’s confidence in its own prediction and can be computed"
[^c2]: arxiv-2601-03908 — "training-free and model-agnostic RAG framework"
[^c3]: arxiv-2601-03908 — "indicating that higher uncertainty"
[^c4]: arxiv-2601-03908 — "showing that retrieval becomes increasingly"
[^c5]: arxiv-2601-03908 — "The 72B model exhibits slower gains due to its"
[^c6]: arxiv-2601-03908 — "rarely triggers retrieval, resulting in performance"
[^c7]: arxiv-2601-03908 — "while larger thresholds reduce retrieval frequency with marginal accuracy"
[^c8]: arxiv-2601-03908 — "Removing UGT results in comparable or slightly"
[^c9]: arxiv-2601-03908 — "relies on the quality of uncertainty estimates derived from"
[^c10]: arxiv-2512-19134 — "existing methods rely on model-internal signals (e.g., logits, entropy), which are fundamentally unreliable because LLMs are typically ill-calibrated"
[^c11]: arxiv-2512-11935 — "the tool-free baseline collapses to MAE = 1.86 eV"
[^c12]: arxiv-2512-11935 — "versus tool-free MAE = 1.25 eV"
[^c13]: arxiv-2512-11935 — "Agentic systems therefore should not blindly invoke tools for every query."
[^c14]: arxiv-2512-11935 — "the tool-augmented MAE being on the diagonal in this evaluation is a property of the circular"
[^c15]: doi-10-48550-arxiv-2607-25600 — "Because none of the evaluated endpoints exposes usable"
[^c16]: doi-10-48550-arxiv-2607-25600 — "a compact JSON object containing a provisional answer, verbalized confidence"
[^c17]: doi-10-48550-arxiv-2607-25600 — "associated with final F1 across all three model families"
[^c18]: doi-10-48550-arxiv-2607-25600 — "shows a positive but modest association with retrieval benefit"
[^c19]: doi-10-48550-arxiv-2607-25600 — "ordinal routing signal than as a calibrated estimate of correctness or retrieval benefit"
[^c20]: doi-10-48550-arxiv-2607-25600 — "(ECE5 = 0.426–0.528)"
[^c21]: doi-10-48550-arxiv-2607-25600 — "increases total token usage by 28.2%, revealing a trade-off"
[^c22]: doi-10-48550-arxiv-2607-25600 — "confidence values cluster near the routing threshold"
[^c23]: doi-10-48550-arxiv-2607-25600 — "the controlled TF–IDF corpus, unmatched execution paths"
[^c24]: doi-10-48550-arxiv-2505-04253 — "at least one external feature matches the performance of"
