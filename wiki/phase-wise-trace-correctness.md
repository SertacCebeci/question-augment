---
description: "Scoring a reasoning trace stage by stage against the scene's ground truth locates where a model's reasoning breaks, which a right-or-wrong grade on the final answer cannot show."
aliases: ["phase-wise reasoning correctness", "stage-wise trace evaluation", "phase-wise LLM-as-a-judge scoring"]
sources: ["arxiv-2512-02340"]
---
# Phase-wise trace correctness

A reasoning trace on a multi-view question can be graded at its final answer, or at each stage it passes through. Only the second locates a failure. In ReMindView-Bench the stages are set by the instruction: the model follows a template whose stages include "(2) alignment of frame-level spatial relationship", after a description of each view and before query-specific reasoning and a final decision.[^c1]

Each stage is then scored by a panel of LLMs against a reference built from the renderer's metadata. The score is a "score of reasoning correctness based on the consistency between spatial relationship in view graphs" and the trace's claims.[^c2] The view graphs are the reference: nodes are objects or viewpoints, edges are spatial relations, and all visible entities are placed so that they are "views are represented within a unified relational structure".[^c3]

The stage scores show where the trace fails. The first stage "achieves the highest percentage of correctness",[^c4] and "such correctness drops considerably in later phases".[^c5] The same pattern holds for wrong final answers: "descriptions remain relatively robust but later reasoning" collapses.[^c6] A wrong answer can therefore carry sound perception and fail at integration. A final-answer grade records that as one failure and does not say which. The authors summarize it as "VLMs remain reliable in early perceptual encoding but degrade sharply in later inferential stages".[^c7]

The same stages are also used for a latent reading. The paper measures entropy "by computing the mean and variance of token-level" logit entropy within each phase,[^c8] and reports that "correct reasoning maintains substantially lower entropy".[^c9] So the stage serves as the unit for a confidence reading as well as for correctness. The text read does not compare the stage-wise judge scores with the stage-wise entropy directly.

My inference, not the paper's claim: this turns an evaluation of a trace into the question of which premise broke, which is the question an asker needs answered before a wrong answer can be repaired. The paper does not measure whether a repair guided by the stage score works.

## Limits

- The judge is an LLM given ground-truth metadata. The paper averages a panel of judges, and the text read gives no human check or agreement figure for the stage scores.
- The stage table covers one family: "Phase-wise reasoning correctness of Qwen2.5-VL family".[^c10] The paper adds that "Larger VLMs demonstrate slower performance decay and higher phase stability",[^c11] so the shape of decay is shown across scale within that family only.
- The four stages are the authors' decomposition, drawn from Johnson-Laird's theory of mental models, and they are applied as an instruction. A model not prompted in these stages may fail at other points, and the stage score would then not locate its failure. The text does not test this.
- The entropy result is a separation between correct and incorrect traces within phases. The text read gives no calibration on held-out items.

## Related

- [[staged-perception-decomposition]] — staging inside one output as a format that helps the model; here the stages are an axis for grading a trace after generation.
- [[object-grounded-trace-scoring]] — scores a visual trace by which objects it names; this note scores by which relational stage is right.
- [[first-token-entropy]] — a one-position entropy readout; the paper instead averages token-level entropy within each reasoning stage.
- [[object-centric-view-centric-spatial-pattern]] — the same benchmark's scene organization, which changes what the stages have to carry.

[^c1]: arxiv-2512-02340 — "(2) alignment of frame-level spatial relationship"
[^c2]: arxiv-2512-02340 — "score of reasoning correctness based on the consistency between spatial relationship in view graphs"
[^c3]: arxiv-2512-02340 — "views are represented within a unified relational structure"
[^c4]: arxiv-2512-02340 — "achieves the highest percentage of correctness"
[^c5]: arxiv-2512-02340 — "such correctness drops considerably in later phases"
[^c6]: arxiv-2512-02340 — "descriptions remain relatively robust but later reasoning"
[^c7]: arxiv-2512-02340 — "VLMs remain reliable in early perceptual encoding but degrade sharply in later inferential stages"
[^c8]: arxiv-2512-02340 — "by computing the mean and variance of token-level"
[^c9]: arxiv-2512-02340 — "correct reasoning maintains substantially lower entropy"
[^c10]: arxiv-2512-02340 — "Phase-wise reasoning correctness of Qwen2.5-VL family"
[^c11]: arxiv-2512-02340 — "Larger VLMs demonstrate slower performance decay and higher phase stability"
