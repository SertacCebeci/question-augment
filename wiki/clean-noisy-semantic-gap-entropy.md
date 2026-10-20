---
description: "Semantic entropy sharpened by the shift between clean and visually degraded answer clusters detects video-VLM hallucination better than clean-only uncertainty, but at only moderate AUC."
aliases: ["VASE", "Vision-Amplified Semantic Entropy", "perturbation-gap semantic entropy"]
sources: ["arxiv-2601-08557"]
---
# Clean-noisy semantic gap entropy

Plain [[semantic-entropy]] samples several answers to one input, clusters them by meaning, and takes entropy over cluster probability mass. For video question answering this uses only the clean clip. VideoHEDGE adds a second sample set: answers to perturbed variants of the clip (fewer frames, lower resolution, photometric shifts). Both sets are clustered into the same semantic hypotheses, giving a clean distribution s_clean and a noisy distribution s_noisy over clusters.

**The score (VASE).** The clean distribution is pushed away from the noisy one before the entropy is taken: VASE = SE(softmax(s_clean + α(s_clean − s_noisy))), with α = 1.[^c1] Clusters whose mass changes under degradation are accentuated. The score is therefore high only when the model's beliefs are both spread out and unstable under input change.[^c2] The two comparison scores use clean samples only. SE is the entropy of the clean cluster distribution. RadFlag is the fraction of clean samples that leave the baseline answer's cluster.[^c3]

**What was measured.** On three 7B video-VLMs (Qwen2VL, Qwen2.5-VL and a SoccerChat-finetuned model), the paper reports that VASE had the highest ROC-AUC against adjudicator-provided hallucination labels, most clearly at larger distortion budgets, while SE and RadFlag often sat near chance.[^c4] Increasing the number of distortions from 1 to 10 generally raised VASE, though not monotonically.[^c5]

**Coupling of budget and scale.** Adding distortions enlarges the noisy pool and the clean sampling budget is raised in proportion. All three metrics are therefore functions of both sampling scale and perturbation strength, and trends over either one cannot be separated.[^c6]

**Clustering backend.** Embedding-based clustering gave detection quality close to NLI clustering. NLI GPU time passed 1,000 s at nine distortions, against 12 to 135 s for embeddings, so the authors call embeddings the only practical option for large perturbation budgets.[^c7]

## Limits

- The absolute level is modest: VASE configurations lie in the 0.57 to 0.67 AUC range, and the baselines are near 0.5 in many cells. It is a better signal, not a reliable detector.[^c8]
- Evidence is one domain (soccer clips, short event labels and short QA) and three 7B models. Whether the gap helps on long free-form answers is untested.
- The label is an adjudicator's judgment, not ground truth.
- α was fixed at 1 following prior work and not tuned here. The claim that the gain comes from the gap, not from the larger sample, is confounded by the coupled budget (above); I do not think the paper isolates it.
- The embedding-versus-NLI parity is uneven: NLI was clearly better in some cells (Qwen2-VL EventClassification, 0.577 against 0.470), and no systematic winner was found.[^c9]

## Related

- [[semantic-entropy]] — the clean-only base that VASE modifies.
- [[evidence-gain-hallucination-score]] — another method that reports VASE as a baseline and beats it in medical VQA.
- [[answer-stability-abstention]] — also reads instability of answers under changed input as a reliability signal.
- [[pseudo-ensemble]] — perturbed inputs standing in for an ensemble of models.
- [[entropy]] — the quantity over clusters.

[^c1]: arxiv-2601-08557 — "with a scaling factor 𝛼 controlling sensitivity to the clean–noisy semantic"
[^c2]: arxiv-2601-08557 — "VASE is high when the model’s semantic beliefs are both uncertain"
[^c3]: arxiv-2601-08557 — "3.3.3 RadFlag. RadFlag measures how often high-temperature"
[^c4]: arxiv-2601-08557 — "VASE consistently achieves the highest ROC-AUC, especially at larger distortion budgets, while SE and RadFlag often operate near chance."
[^c5]: arxiv-2601-08557 — "even though the progression is not strictly monotonic."
[^c6]: arxiv-2601-08557 — "functions of both sampling scale and perturbation strength"
[^c7]: arxiv-2601-08557 — "this makes embedding-based clustering the only practical option for large perturbation budgets,"
[^c8]: arxiv-2601-08557 — "VASE configurations lie in the moderate 0.57–0.67 range"
[^c9]: arxiv-2601-08557 — "also cases where NLI is noticeably better (e.g., Qwen2-VL EventClassification, 0.577 vs. 0.470), but there is no systematic advantage"
