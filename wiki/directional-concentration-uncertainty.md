---
description: "Uncertainty scored as inverse von Mises-Fisher concentration of embeddings of N sampled outputs, replacing semantic-entropy clustering; near SE on short QA, above it on visual QA."
aliases: ["DCU", "vMF concentration uncertainty", "embedding-dispersion uncertainty"]
sources: ["arxiv-2602-13264"]
---
# Directional concentration uncertainty

A sampling-based, black-box uncertainty score that skips the clustering step of [[semantic-entropy]]. Sample N outputs for one input, embed each with a pretrained encoder, and measure how tightly the unit vectors point the same way.

## Mechanism

Each output y_i is mapped by an embedding model and L2-normalised, so it lies on the unit hypersphere.[^c1] The embeddings are modelled with a von Mises-Fisher distribution, which has a mean direction and a concentration parameter kappa. Larger kappa means tighter clustering and smaller kappa means more dispersion.[^c2] The mean direction is the normalised resultant vector. Kappa is found by solving A_d(kappa) = mean resultant length numerically (Newton-Raphson with a bisection fallback). The uncertainty score is the inverse concentration, 1/kappa.[^c3]

The authors' motivation is a structural limit of SE. Clustering needs a narrow notion of semantic equivalence, namely entailment, which works for short answers but not for longer or more complex text or other modalities.[^c4] DCU needs no cluster assignments and no auxiliary entailment model. It only needs an encoder suited to the modality (e5-large-v2 for text, CLIP for the multimodal case).[^c5]

## What was measured

Setup: N = 10 generations per question, LLaMA-2-7B, Mistral-7B and Falcon-7B on TriviaQA, SQuAD and NQ-Open (300 questions each), then LLaVA-1.5-7B and Gemma-3-4B on ScienceQA (150 image questions). Evaluation was AUROC of the uncertainty score against correctness, with bootstrap intervals.[^c6] Correctness on text QA was ROUGE-L F1 above 0.1 for the first answer. On ScienceQA, the first answer was matched to the nearest option by CLIP cosine similarity.

- Text QA: SE is generally slightly higher, with differences inside the bootstrap intervals, and DCU matches or exceeds it in some settings such as Falcon on NQ-Open and SQuAD.[^c7] For example, TriviaQA LLaMA-2 gives DCU 0.61 against SE 0.71 (both with a 0.06-0.07 interval). Falcon on NQ-Open gives 0.75 against 0.67.
- ScienceQA: DCU AUROC was 0.56 (Gemma) and 0.67 (LLaVA), against SE at 0.52 and 0.51.[^c8] The authors read this as a limit of SE outside typical QA benchmarks.[^c9]

My reading, as inference and not a result of the paper: the score treats paraphrase as small angular distance instead of as an equivalence class. So it replaces a hard partition with a soft one that depends on the encoder's geometry.

## Limits

- Small scale. 7B-class open models, N = 10, 150-300 questions, and a single encoder per modality. No encoder ablation is reported in the slices I read.
- The multimodal comparison is on ScienceQA, which is multiple choice. The authors converted it to free-form answers by prompting, and judged correctness with the same CLIP space DCU uses. That plausibly favours DCU, and I flag it as my own concern.
- Absolute multimodal AUROC is weak, and the authors call 0.67 "good, but not acceptable".[^c10]
- Dispersion of embeddings still measures only the model's inconsistency. A consistently wrong answer has high concentration and so low uncertainty, as with SE (see [[confidently-wrong-low-entropy-regime]]).
- Nothing here tests whether embedding distance tracks meaning differences that matter, such as a negation. This is untested.
- The paper's vMF fit with d in the hundreds and N = 10 is statistically thin. This is my observation, not a claim of the paper.

## Related

- [[semantic-entropy]] — the baseline DCU replaces; the same sampling logic, a different dispersion measure.
- [[confidently-wrong-low-entropy-regime]] — the shared blind spot of consistency-based scores.
- [[pseudo-ensemble]] — another use of repeated sampling as a stand-in for an ensemble.

[^c1]: arxiv-2602-13264 — "to ensure they all lie on a unit hypersphere."
[^c2]: arxiv-2602-13264 — "larger values indicating more tightly clustered samples and smaller values indicating greater dispersion."
[^c3]: arxiv-2602-13264 — "We use the inverse concentration, κ−1 , as the uncertainty score, with lower concentration corresponding to higher uncertainty."
[^c4]: arxiv-2602-13264 — "approaches relying on text clustering will struggle to generalize across all language domains."
[^c5]: arxiv-2602-13264 — "uncertainty is computed without discrete cluster assignments or auxiliary semantic matching models."
[^c6]: arxiv-2602-13264 — "we used N = 10 generations with"
[^c7]: arxiv-2602-13264 — "DCU attains AUROC scores that closely match or exceed"
[^c8]: arxiv-2602-13264 — "the AUROC scores for DCU with embeddings are clearly superior to SE especially"
[^c9]: arxiv-2602-13264 — "with poor performance on data and tasks outside the typical"
[^c10]: arxiv-2602-13264 — "good, but not acceptable AUROC levels"
