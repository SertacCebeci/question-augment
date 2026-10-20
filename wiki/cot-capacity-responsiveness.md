---
description: "Structured chain of thought helps code generation most in small models: GPT-3.5 gains about 15 points over zero-shot, while GPT-5 loses 1.36 points; naive zero-shot CoT can cost accuracy too."
aliases: ["capacity-dependent CoT", "CoT responsiveness by model size", "scale-dependent chain-of-thought benefit"]
sources: ["arxiv-2512-09679", "arxiv-2512-05277"]
---
# Capacity-dependent chain-of-thought responsiveness

A chain of thought (CoT) written before the code is not a fixed gain. The same structured prompt moves Pass@1 by different amounts depending on the model that receives it. The paper's own abstract states the dependence in one line: "CoT benefits depend on language type systems and model capacity."[^c1]

The measured pattern is in the structured-CoT comparison against the zero-shot baseline. The small proprietary model gains most: "GPT-3.5: SCoT provides +15.09% over Zero-Shot".[^c2] The open models in the 7B to 480B range gain a few points each: Qwen2.5-7B gains +1.83% and Qwen2.5-32B gains +4.87%, and the paper lists comparable gains for Qwen3-30B and Qwen3-480B. The largest model in the study does not gain: "GPT-5 shows minimal benefit even from high-quality reasoning," with SCoT at -1.36% against zero-shot.[^c3]

The paper's explanation for the frontier case is that "frontier models have internalized reasoning patterns and derive limited marginal utility" from external guidance.[^c4] That is an interpretation. The text does not test whether GPT-5 has internalized anything; it reports only the accuracy differences.

The same direction shows up in the paper's asymmetric-outcome analysis, which compares larger and smaller models under identical structured prompts. There, "Larger models succeed in about two-thirds of asymmetric cases," and the authors call the capacity effect non-monotonic, adding that "excessive capacity can introduce reasoning drift."[^c5][^c10][^c6] So the relation is not a simple increase in benefit with size. Moderate scaling helps the decoding of reasoning, and past some point the extra capacity can produce a different failure.

Unguided reasoning sits at the low end of the same axis. The abstract says "naive Zero-Shot CoT can even degrade performance,"[^c7] and the paper attributes the degradation to hallucinated reasoning: "unguided self-generated reasoning often degrades performance."[^c8]

A video version of the pattern appears in the TAD driving benchmark. Scene-CoT writes a reasoning trace for each short segment and lets an LLM answer from the traces. The paper says it "provides modest gains over the baselines for smaller" generalist models.[^c11] For larger models, the paper finds that "SceneCoT does not offer additional gains."[^c12] The authors offer a hypothesis: larger VLMs "produce internal representations better suited for temporal QA than an explicit CoT-based" description.[^c13] That is their suggestion, not a test.

## Limits

- Capacity is a label, not a measurement. The pairs are GPT-3.5 against GPT-5, Qwen2.5-7B against 32B, and Qwen3-30B against 480B. The paper says "Each pair shares identical architecture, training objectives, and instruction format,"[^c9] but the text does not document that for the proprietary pair. Within a pair the model is not isolated from its vendor, its training data or its release date, so the curve over size is a curve over these six systems, not a dose-response in capacity.
- The mid-size gains are small. HumanEval has 164 problems, so one problem is about 0.61 Pass@1 points (my arithmetic). Gains of 1 to 5 points are of the order of a few problems, and the text read here reports no variance across runs.
- The frontier explanation (internalized reasoning) is the paper's suggestion and is untested.
- Each number is one prompt family (three-shot structured CoT) on one set of benchmarks. Whether a different template moves the crossover is not shown.
- Non-monotonicity is stated in the asymmetric analysis; the SCoT-versus-zero-shot table does not by itself establish a peak.

## Related

- [[reasoning-quality-over-structure]] — within one fixed template, the generator's quality moves accuracy; the quality gap is largest where capacity is smallest.
- [[capacity-dependent-evidence-modality]] — the same capacity-dependent pattern for the input modality; there too the capacity axis is a label rather than a measurement.
- [[abstention-option-uncertainty-inflation]] — a second setting where chain of thought does little for a strong model, here on abstention in medical QA.
- [[moderate-adaptive-reasoning-length]] — light chain of thought helped non-reasoning models on a different benchmark, a gain of the same sign for the smaller models.

[^c1]: arxiv-2512-09679 — "CoT benefits depend on language type systems and model capacity"
[^c2]: arxiv-2512-09679 — "GPT-3.5: SCoT provides +15.09% over Zero-Shot"
[^c3]: arxiv-2512-09679 — "GPT-5 shows minimal benefit even from high-quality reasoning"
[^c4]: arxiv-2512-09679 — "frontier models have internalized reasoning patterns and derive limited marginal utility"
[^c5]: arxiv-2512-09679 — "Larger models succeed in about two-thirds of asymmetric cases"
[^c6]: arxiv-2512-09679 — "excessive capacity can introduce reasoning drift"
[^c7]: arxiv-2512-09679 — "naive Zero-Shot CoT can even degrade performance"
[^c8]: arxiv-2512-09679 — "unguided self-generated reasoning often degrades performance"
[^c9]: arxiv-2512-09679 — "Each pair shares identical architecture, training objectives, and instruction format"
[^c10]: arxiv-2512-09679 — "capacity effects are non-monotonic"
[^c11]: arxiv-2512-05277 — "provides modest gains over the baselines for smaller"
[^c12]: arxiv-2512-05277 — "SceneCoT does not offer additional gains"
[^c13]: arxiv-2512-05277 — "better suited for temporal QA than an explicit CoT-based"
