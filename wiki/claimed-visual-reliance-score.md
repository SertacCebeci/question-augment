---
description: "A text-only score of how much a reasoning trace claims to rest on visual evidence, given by an LLM judge; it reads what the reasoning says, not what the model attended to."
aliases: ["Video Attention Score", "VAS", "visual-reliance score", "claimed visual grounding score"]
sources: ["arxiv-2511-23478"]
---
# Claimed visual reliance score

A reasoning trace can cite the picture and still lean on what the model already knows. Video-R2 measures the gap between how a trace reads and what it draws on, by scoring the trace text itself.[^c1] The Video Attention Score (VAS) is an LLM-as-a-judge rating: "We employ an LLM-as-a-Judge framework, where a language model evaluates the reasoning trace based on predefined guidelines and assigns a visual-reliance score between 0 and 10, later normalized to the range [0, 1]."[^c2][^c3] The judge looks at explicit mentions of visual entities, spatial or temporal relations, and causal statements tied to observed actions.[^c4] A dataset's VAS is the mean of the per-sample scores.

The score is deliberately independent of the model's internals. The paper shows token-wise attention to video tokens as a picture, but says those distributions "serve only as a visualization of the internal model behavior and are not used to compute VAS."[^c10] The score is therefore a claim-level quantity: it measures reliance as the trace presents it, and it is defined so that a model's attention cannot move it directly. The authors motivate the measure with the failure they see in current thinking models: "the reasoning often sounds coherent but fails to correspond either" to the answer or to the visual evidence.[^c11]

The paper uses VAS alongside Think–Answer Consistency, as two axes of reasoning quality. TAC asks whether the conclusion matches the answer; VAS asks how visual the reasoning is. Together they are described as "a two-axis evaluation of reasoning quality".[^c12] See [[think-answer-consistency]] for the first axis.

The measured movements show the score responding to training. Timestamp-aware SFT raised VAS from 44.3 to 69.7 over the CoT baseline; GRPO on the final answer lowered it, "and VAS (69.7 → 61.5)"; adding the temporal reward raised it again, "and VAS shows a notable increase from 61.5 to 69.9."[^c7][^c8] These are the paper's numbers on its own benchmark mix. They show the score can move, in the direction the authors expect, under different training recipes. They do not show that the score tracks visual use.

## Limits

- The score is a claim, not a check. The paper says so: VAS "evaluates claimed rather than verified reliance on video evidence."[^c6] A trace that names objects and timestamps it never used scores high on the cues the judge is given. My inference from the cue list; the paper does not test this case in the text I read.
- It is judge-dependent. The reliance score is produced by a language model under a guideline prompt that the paper puts in an appendix. The text I read reports an ablation of "the stability of the proposed VAS metric using" different judges,[^c9] but I did not read that result, so I cannot say how much the number moves with the judge.
- The trained target and the metric overlap. The temporal reward rewards timestamps that match reference reasoning, and VAS rewards visible mention of visual entities and temporal relations. A rise in VAS after that reward is partly the reward doing what it is shaped to do (my inference). The metric is not independent of the training signal here.
- Attention is not measured. The attention figure in the paper is illustrative, and the paper does not report a correlation between VAS and attention mass. Whether the two agree is untested in the text read.
- Visual dependence is not the same as visual correctness. A high score says the trace talks about the video; it does not say the talk is right. Accuracy and a localization check would be needed for that, as in [[grounding-answer-dual-axis-audit]].

## Related

- [[cot-hallucination-trap]] — a language-prior rationale that a plausibility score cannot separate from a grounded one; VAS is a visual-reliance reading of the same trap
- [[counterfactual-image-grounding-audit]] — tests reliance by changing the image and watching the output; VAS only reads what the text says, the contrast being verified against claimed reliance
- [[think-answer-consistency]] — the consistency axis the paper pairs with VAS
- [[grounding-answer-dual-axis-audit]] — crosses measured evidence localization with answer correctness, rather than scoring a trace's self-description
- [[llm-judge-biases]] — the judge here is an LLM, so known judge biases apply to the score
- [[text-modality-dominance]] — heavier reliance on text, measured by corrupting the input rather than reading the reasoning

[^c1]: arxiv-2511-23478 — "rely on visual information rather than on textual patterns"
[^c2]: arxiv-2511-23478 — "We employ an LLM-as-a-Judge framework, where a language model evaluates the reasoning trace"
[^c3]: arxiv-2511-23478 — "score between 0 and 10, later normalized to the range [0, 1]."
[^c4]: arxiv-2511-23478 — "The LLM-judge considers cues such as explicit mentions"
[^c5]: arxiv-2511-23478 — "VAS is independent of attention weights and provides a complementary, text-based"
[^c6]: arxiv-2511-23478 — "evaluates claimed rather than verified reliance on video evidence"
[^c7]: arxiv-2511-23478 — "with TAC increasing from 55.5 to 96.8 and VAS from 44.3 to 69.7"
[^c8]: arxiv-2511-23478 — "and VAS shows a notable increase from 61.5 to 69.9"
[^c9]: arxiv-2511-23478 — "the stability of the proposed VAS metric using"
[^c10]: arxiv-2511-23478 — "the token-wise attention distributions shown in Fig. 1 serve"
[^c11]: arxiv-2511-23478 — "the reasoning often sounds coherent but fails to correspond either"
[^c12]: arxiv-2511-23478 — "TAC and VAS together form a two-axis"
