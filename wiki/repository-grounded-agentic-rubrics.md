---
description: "Letting an agent explore the codebase before writing a checklist yields specific, gradable criteria; scoring patches without execution beat baselines, and dropping exploration cost 1.4-4.0 points."
aliases: ["Agentic Rubrics", "contextual rubric verifier", "execution-free rubric verification"]
sources: ["arxiv-2601-04171", "doi-10-48550-arxiv-2606-01091"]
---
# Repository-grounded agentic rubrics

A verifier for code patches usually either runs tests (grounded in the repository but costly: per-instance sandbox setup, sparse or brittle signals) or judges the patch without running it (cheap, but shallow and uninterpretable). Agentic Rubrics take a third route: an expert agent first uses search and file-view tools on the repository and the issue text, and writes a rubric of explicit criteria. Each candidate patch is then graded against that rubric by a judge, with no code executed.[^c1] The rubric is organized along four axes (File Change, Spec Alignment, Integrity, Runtime), and the patch score is the share of criteria satisfied.[^c2]

## Why exploration matters

The question of *what to check* is answered with evidence from the codebase instead of from the problem statement alone. Rubrics written from the issue text are described as "often under-specified because they lack repository-specific context".[^c3] In the ablation, the same model (Sonnet-4.5) wrote rubrics without repository access. Non-agentic items were high-level ("touches the right code path"), which "increases ambiguity and can lead to false positives", whereas agentic items named concrete files, classes and methods. Removing access reduced Best@16 by 4.0 points on Qwen3-32B rollouts and 1.4 points on Qwen3-Coder-30B-A3B rollouts.[^c4] A parallel construction for open-ended reinforcement learning replaces the repository with multi-turn web search: DR-Rubric writes an evidence trace first, and its rubric constraints are traceable to that trace.[^c10]

## What was measured

- Under parallel test-time scaling (best-of-K) on SWE-Bench Verified, scores were 54.2% on Qwen3-Coder-30B-A3B and 40.6% on Qwen3-32B, at least 3.5 points above the strongest baseline in the comparison set.[^c5]
- Writer capability matters: frontier coding models reached about 54% Best@16, open coding models about 45%, a non-coding agentic model about 43%. Stronger models also wrote more criteria per instance (Sonnet-4.5 averaged over 20), which the authors suggest gives finer-grained separation of candidates.[^c6]
- Judge capability matters little: GPT-5-mini scored 52.6 and GPT-5 high reasoning 55.0 on the same rubrics, which the authors attribute to criteria being self-contained and atomic.[^c7]
- Distillation: fine-tuning Qwen3-32B on 2,000 Sonnet-4.5 rubric-writing trajectories beat fine-tuning it as a YES/NO patch classifier, suggesting the structured, context-grounded rubric is a more trainable objective.[^c8]
- Rubrics also flagged concerns that tests miss: when rubric scores are low, 54% of failures were judged high-utility (missed root cause, missing edge cases), including over half of the rejections of patches that pass ground-truth tests.[^c9]

## Limits

- Evaluated on one benchmark family (SWE-Bench Verified) with a few policy models; whether grounding helps outside code, where "the repository" has no analogue, was not tested.
- The grounding gain is modest and uneven (1.4 vs 4.0 points), and the ablation used one writer model.
- That rubric rejections of test-passing patches are "plausible under-tested issues" is an analysis of sampled cases, not proof they are real defects.
- Rubric writing needs an agentic scaffold and a strong model, so the cost saving over execution is not unconditional; the authors report parse and scaffold success rates separately.
- My inference, untested here: the point carries to question asking only as an analogy (explore context before deciding what to ask or check).

## Related

- [[rubric-formation-gap]] — the same bottleneck (writing the criteria) seen in judging, with human rubrics as the reference
- [[proxy-verified-rubric-transferability]] — another way to assess rubric quality
- [[llm-judge-biases]] — surface cues that execution-free judging is prone to
- [[bootstrap-rubric-generation]] — the evidence-first rubric writer, where the policy being trained replaces the external writer

[^c1]: arxiv-2601-04171 — "an expert agent interacts with the repository to create a context-grounded rubric checklist, and candidate patches are then scored against it without requiring test execution"
[^c2]: arxiv-2601-04171 — "organized along four rubric axes (File Change, Spec Alignment, Integrity, Runtime)"
[^c3]: arxiv-2601-04171 — "rubrics written from the problem statement alone are often under-specified"
[^c4]: arxiv-2601-04171 — "reduces B EST @16 by 4.0 points on Qwen3-32B rollouts and 1.4 points on Qwen3-Coder-30B-A3B"
[^c5]: arxiv-2601-04171 — "with at least a +3.5 percentage-point gain over"
[^c6]: arxiv-2601-04171 — "Rubric-agent capability matters: stronger frontier models generate more granular rubrics"
[^c7]: arxiv-2601-04171 — "judge model capability has a small but non-trivial effect on performance"
[^c8]: arxiv-2601-04171 — "the agentic rubric generator substantially outperforms the patch-classifier verifier"
[^c9]: arxiv-2601-04171 — "over half of these rejections (54%) flag plausible under-tested issues"
[^c10]: doi-10-48550-arxiv-2606-01091 — "Crucially, constraints are not heuristically authored but are traceable to specific elements in Sp"
