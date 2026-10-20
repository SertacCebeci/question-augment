---
description: "In Gemma 3 27B, verbal confidence is computed while the answer is written, cached at the first post-answer token, and retrieved at verbalization; it is not a log-probability readout."
aliases: ["cached retrieval hypothesis", "post-answer newline confidence cache", "PANL confidence representation"]
sources: ["arxiv-2603-17839"]
---
# Verbal confidence as cached retrieval

When an LLM is asked "how confident are you?", two mechanisms are possible. Under a just-in-time (JIT) account, nothing confidence-related happens until the question arrives; the model integrates question and answer at the last prompt token. Under cached retrieval, confidence is computed automatically as the answer is produced, stored at an answer-adjacent position, and read out later.[^c1] Kumaran et al. (2026) test both in Gemma 3 27B (TriviaQA, BigMath, MMLU), with replications in Qwen 2.5 7B and Magistral Small 24B, and find cached retrieval.

## The pathway

The cache site is the first post-answer position (the newline after the answer, "PANL"). Verbalization happens at the final prompt token before the confidence ("CC").

- **No JIT computation at CC.** Blocking attention from CC to question and answer tokens changed outputs about as often as the control: "CC does not compute confidence from scratch."[^c2]
- **CC reads from PANL.** With a minimal numeric prompt that removes intermediate template tokens, blocking CC to PANL disrupted outputs: "CC retrieves confidence information from PANL."[^c3] With the long categorical prompt this edge showed no effect. The authors attribute that to redundant routing through the more than a hundred template tokens in the prompt.[^c4]
- **PANL reads from answer tokens.** Blocking PANL's attention to answer tokens had its effect about 6-8 layers earlier than the CC-to-PANL effect (layers 22-28 against 30-36), which gives the order answer tokens, then PANL, then CC.[^c5]
- **Causal specificity.** Swapping PANL activations between a high- and a low-confidence trial shifted the recipient's reported confidence in the donor's direction, beyond the disruption seen in same-confidence swaps. These swaps "produce systematic directional shifts in confidence—decreasing" or increasing it.[^c6] This argues that PANL carries confidence, not just answer content. Steering, patching and noising at PANL also modulate reports (see the paper's figures), and confidence is decodable from PANL at earlier layers than from CC.[^c7]

## Not a log-probability readout

The answer-colon token, whose residual stream directly produces the first answer token, is the natural site for a first-order readout. Interventions there were inert: steering, patching and noising "all produced null effects, indistinguishable from the PANL+1 control position, while the same".[^c8] Linear decoding at that token gave R2 near 0.2 against about 0.75 at PANL.[^c8]

Variance partitioning agrees. Six log-probability indices combined explained 10.0% of the variance in verbal confidence, whereas a probe on PANL activations at layer 40 gave "activation at L40 explained 38.0% variance."[^c9] The authors read this as a second-order, answer-quality evaluation, parallel to the neuroscience distinction between confidence read from the decision variable and confidence from a separate evaluation.[^c1] Calibration of the studied model was moderate (ECE 0.12, AUROC 0.71 for Gemma).[^c10]

## Limits

- Mostly short-answer, no-chain-of-thought settings on three open models. The authors state that this simplification is what makes tracing possible, so whether the pathway holds with long reasoning is untested here. Magistral gave similar localization, but only in summary.
- Mean ablation at PANL only partly disrupted reports. Encoding is distributed or redundant, and PANL is not the only path.[^c11]
- "Richer than log-probabilities" rests on six chosen log-prob indices and a ridge probe. A different uncertainty feature, such as sampling consistency, could explain the unique variance. The second-order reading is the authors' interpretation, not a direct test.
- Information is decodable at positions where intervention has no behavioral effect, so probing alone does not show use.[^c12]
- All authors work at the lab that makes Gemma; one tested model is theirs.
- The prompt format changed which edges mattered, so the pathway is prompt-sensitive.

## Related

- [[verbal-confidence-commit-readiness-dissociation]] — behavioral evidence that verbal confidence carries signal beyond log-probabilities; this note gives a candidate internal substrate
- [[reasoning-contamination-of-verbalized-confidence]] — what changes when confidence is verbalized after chain-of-thought rather than from cached state
- [[verbal-probability-expressions]] — how verbal confidence terms map to numbers once produced

[^c1]: arxiv-2603-17839 — "Under the cached retrieval hypothesis, however, confidence is computed automatically as"
[^c2]: arxiv-2603-17839 — "CC does not compute confidence from scratch."
[^c3]: arxiv-2603-17839 — "CC retrieves confidence information from PANL."
[^c4]: arxiv-2603-17839 — "rather than via a direct pathway (see §D for details)."
[^c5]: arxiv-2603-17839 — "consistent with a sequential information"
[^c6]: arxiv-2603-17839 — "produce systematic directional shifts in confidence—decreasing"
[^c7]: arxiv-2603-17839 — "Consistent with the cached retrieval hypothesis, information about both correctness and confidence magnitude is"
[^c8]: arxiv-2603-17839 — "and noising at AC all produced null effects, indistinguishable from the PANL+1 control position, while the same"
[^c9]: arxiv-2603-17839 — "activation at L40 explained 38.0% variance."
[^c10]: arxiv-2603-17839 — "calibrated (ECE = 0.12, AUROC = 0.71), and used both ends"
[^c11]: arxiv-2603-17839 — "rather than complete disruption may reflect either the distributed nature of confidence encoding across layers—such"
[^c12]: arxiv-2603-17839 — "This is consistent with previous studies showing information may be present in networks"
