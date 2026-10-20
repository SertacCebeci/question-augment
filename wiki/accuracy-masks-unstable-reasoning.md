---
description: "Crossing correctness with internal stability splits answers into four modes; most correct answers can be lucky guesses and about 9% of outputs are stable but wrong, which accuracy alone hides."
aliases: ["silent failure rate", "lucky guess mode", "depth-accuracy paradox"]
sources: ["arxiv-2603-03475", "arxiv-2512-00552"]
---
# Accuracy masks unstable reasoning

A single accuracy number averages over answers reached by different internal routes. The paper classifies each answer by two things: whether it is correct, and whether an internal stability score S(q) reaches 0.65. That gives four modes: correct and stable, incorrect and stable ("silent failure"), incorrect and unstable, and correct and unstable ("lucky guess"). The silent failure rate is the share of all problems in the second mode.[^c1]

## What was measured

Qwen2.5-Math-7B was run on 500 GSM8K problems and reached 61% accuracy. Of the correct answers, 18.4% came from stable, faithful reasoning and 81.6% from computationally inconsistent pathways.[^c2] Over all predictions the split was 11.2% correct and stable, 49.8% lucky guesses, 30.2% incorrect and unstable, and 8.8% silent failures (44 cases), roughly 1 in 11 to 12 predictions that are confident yet wrong.[^c3]

Stability here is the cosine similarity of hidden activations across independent forward passes, combined with alignment and depth-efficiency terms into a composite fidelity F. Only about 20% of responses met the strict criteria F at least 0.60, S at least 0.65, E at least 0.60.[^c4] Mean per-sample stability across passes was high (cosine about 0.96 or more), so the S that varies is between problems, not within one.[^c5]

## Two related observations

Scaling did not move accuracy. The 1.5B and 7B models both scored 61.0%, though the 7B had deeper activations (0.514 against 0.479) and lower entropy.[^c6] Explicit chain of thought raised accuracy from 58.5% to 68.5% while depth differed by only 0.01, which the authors read as better alignment, not deeper computation.[^c7] Reasoning depth itself correlated with correctness at about zero (r = 0.03), and more reasoning steps predicted lower accuracy (r = -0.27).[^c8]

Fidelity correlated weakly negatively with binary correctness (r = -0.21), yet fidelity separated correct from incorrect with AUROC 0.78; the authors call the negative correlation a threshold artifact.[^c9] So the same score can look inverse or predictive depending on how it is summarized.

A different diagnostic reaches a similar conclusion from another side. On a 600M-parameter model, answer accuracy above 70% sat beside a low forward-backward consistency score.[^c12] The paper reads accuracy as masking "fundamental failures in logical computation".[^c11] The two papers measure different things, so I read them as one lesson, not one result; that reading is my inference. The reverse-pass test is described in [[bidirectional-reasoning-consistency]].

## What it means for asking and answering

A reader or asker who sees a confident, correct answer cannot infer that the route was sound; and a stable, confident answer can still be wrong. Checking correctness and checking route consistency are separate questions. This is my inference, not a result of the paper.

## Limits

- Only 500 GSM8K items (about 6%), one model family, one run; the authors say the scaling result needs the full benchmark.[^c10]
- The 0.65 threshold and the F, S, E metrics have no formal foundation (the authors admit this) and the "silent failure" label depends on S being a proxy for confidence, which is not output confidence in the usual sense.
- Stability is measured across forward passes of the same model; the paper reports high within-problem similarity, so what "unstable" means mechanistically is unclear. The causal-layer findings (middle layers matter under noise, late layers have large activations) were not tied to the failure modes.
- The 81.6% figure counts "unfaithful" by the paper's own composite metric; it is not shown that those answers were produced by guessing.
- Correlation of fidelity with correctness was negative on the binary reading; the reconciliation by AUROC is the authors' interpretation.

## Related

- [[confidently-wrong-low-entropy-regime]] — another case where a confidence-like signal fails to separate errors from correct answers
- [[semantic-entropy]] — a dispersion score whose consistency-equals-reliability assumption this note's silent failures also test

[^c1]: arxiv-2603-03475 — "High SFR indicates the model produces confident yet incorrect outputs—a critical safety concern for"
[^c2]: arxiv-2603-03475 — "18.4% of correct predictions result from stable, faithful reasoning (56 cases),"
[^c3]: arxiv-2603-03475 — "8.8% are Silent Failures (incorrect with stable reasoning, 44 cases)."
[^c4]: arxiv-2603-03475 — "However, only 20% of responses satisfy our strict faithfulness criteria (F ≥ 0.60, S ≥ 0.65, E ≥"
[^c5]: arxiv-2603-03475 — "Individual forward passes show high per-sample stability with cosine similarity ≈ 0.96+."
[^c6]: arxiv-2603-03475 — "Despite a 4.7× parameter difference, both achieve identical 61.0% accuracy."
[^c7]: arxiv-2603-03475 — "Explicit CoT improves accuracy by ten percentage points (58.5% → 68.5%), yet internal signatures"
[^c8]: arxiv-2603-03475 — "Similarly, more reasoning steps predict lower accuracy (r = −0.27, p < 0.001)."
[^c9]: arxiv-2603-03475 — "Higher fidelity robustly predicts correctness when analyzed continuously (AUROC ="
[^c10]: arxiv-2603-03475 — "Scaling law conclusions should be validated on the complete benchmark before generalizing."
[^c11]: arxiv-2512-00552 — "masking fundamental failures in logical computation"
[^c12]: arxiv-2512-00552 — "while the model achieves reasonable answer accuracy (70%+), it demonstrates poor backward consistency (15%)"
