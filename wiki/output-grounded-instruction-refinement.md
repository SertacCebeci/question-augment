---
description: "A rewrite of an instruction made after scoring the output it produced, and reissued in a loop, beat a rewrite made from the source alone on one image-editing benchmark."
aliases: ["think-while-edit", "critique-refine-repeat loop", "multi-turn instruction refinement"]
sources: ["arxiv-2512-05965"]
---
# Output-grounded instruction refinement

A request sent to a generator can be rewritten at two points. It can be rewritten before the generator runs, from the source and the request alone. Or it can be rewritten after a critic has looked at what the generator produced. The image-editing study reads the second as a distinct mechanism and calls it Think-while-Edit. A multimodal thinker takes the source image, the original instruction and the previous edited image, and returns a score, a reasoning trace and a refined instruction. The editor then runs again on the refined instruction. The loop is described as one in which "the Thinker evaluates the editing result (Critique), refines the instruction based on identified deficiencies (Refine), and resubmits it to the editor for regeneration".[^c1]

The stated reason for putting the critique first is that a rewrite needs the failure in view. In the authors' words, "the model must first critique the previous output" before it writes the refined instruction, so that the new instruction is grounded in what the image actually shows.[^c2]

The ablation separates the two timings. On GEdit-Bench-EN, with FLUX.1 Kontext as the editor, the single-pass baseline scores 6.18 on the overall measure. A think-before-edit rewrite, made from the source image alone, raises it to 6.82. The think-while-edit loop raises it to 7.19.[^c3][^c4][^c5][^c6] The authors add that a think-before step placed in front of the loop lowers the result to 7.06, and they hypothesize that "the initial Think before Edit introduces a bias" in the first round.[^c7][^c8]

The loop also has a turn cap. Raising the maximum number of turns from two to eight moved the overall score from 6.95 to 7.30, with 7.13 at four turns and 7.16 at six.[^c9][^c10] The cap is also a stopping rule in the trained system: the thinker is used so that refinement is triggered "only when the" predicted score falls below a threshold.[^c11]

Two design choices carry the mechanism. First, the critique and the rewrite are produced together, in one output. The authors say a single expert "struggles to maintain high performance" when asked to refine and to score at once, which is why their data pipeline first had an expert issue refinements and a separate scorer rate them, and why the trained model then does both "in a single forward pass".[^c12][^c13] Second, the reinforcement signal for a rewrite is a difference, not a level. The rewrite is rewarded when it "successfully prompted the Editor to produce a better image than the previous step", judged by the same expert on the before and after images.[^c14]

What transfers, in my reading and not as the paper's claim, is the timing. A reformulation made after seeing an answer that failed a check has a different input from one made before any answer exists. The paper's evidence is about image generation, where the failure can be seen and scored by a model. Whether a question's failure can be read the same way is not tested here.

## Limits

- One task family. The gains are for instruction-following in image editing. The text read has no question-asking or question-answering run.
- The critic is also the teacher. The critique score and the training labels both come from GPT-4.1 "as the critic expert".[^c15] The text read does not say whether the benchmark scores use a different judge.
- Gains are uneven across benchmarks. On ImgEdit-Bench the trained loop moved Qwen-Image-Edit "from 4.36 to 4.37", which is no measurable gain.[^c16]
- The main ablations use one editor and one benchmark. The think-before and think-while comparison in the parts read is on FLUX.1 Kontext and GEdit-Bench-EN only.[^c4]
- The turn curve rises at every tested cap up to eight. The paper does not show where it stops rising. Whether this loop peaks as a judged explanation does is open; see [[refinement-quality-peak]].
- Expert swaps give four points. Replacing the expert changes the overall score to 7.19 (GPT-4.1), 7.11 (Gemini 2.5 Pro), 6.80 (Doubao 1.5) and 7.05 (GPT-4o). The authors call the performance "directly and positively correlated" with expert capability.[^c17][^c18] Four points on one benchmark support an ordering, not a law.
- No cost is reported in the parts read. Each turn is one editor run and one thinker call, so the cost grows with the cap, but the paper gives no latency or price figure. (my inference)

## Related

- [[intrinsic-self-correction-convergence]] — self-correction with no external feedback settles over rounds; here the critique reads the actual output, which is a different input to the same kind of loop
- [[refinement-quality-peak]] — judged self-revision of an explanation peaks and falls; this image loop rose over the tested turn caps
- [[iterated-transformation-regime]] — the same kind of iterated rewrite treated as a dynamical system; this paper does not measure whether its loop settles
- [[stage-specific-elicitation]] — feedback placed at each decision stage rather than after the artifact; the same timing question in another setting
- [[feedback-timing-error-derailment]] — when feedback helps depends on where early errors would propagate

[^c1]: arxiv-2512-05965 — "the Thinker evaluates the editing result (Critique), refines the instruction based on identified deficiencies (Refine), and resubmits it to the editor for regeneration"
[^c2]: arxiv-2512-05965 — "the model must first critique the previous output"
[^c3]: arxiv-2512-05965 — "Ablation on GEdit-Bench-EN with Thinking Paradigm"
[^c4]: arxiv-2512-05965 — "Think before Edit provides a noticeable improvement but"
[^c5]: arxiv-2512-05965 — "is consistently outperformed by Think while Edit."
[^c6]: arxiv-2512-05965 — "using only the source image"
[^c7]: arxiv-2512-05965 — "We hypothesize that the initial Think before Edit introduces a bias"
[^c8]: arxiv-2512-05965 — "Think before Edit provides a noticeable improvement but"
[^c9]: arxiv-2512-05965 — "Ablation of turn number on GEdit-Bench-EN"
[^c10]: arxiv-2512-05965 — "We observe a clear and consistent performance scaling as we increase the maximum number of"
[^c11]: arxiv-2512-05965 — "trigger refinement only when the"
[^c12]: arxiv-2512-05965 — "that a single expert struggles to maintain high performance"
[^c13]: arxiv-2512-05965 — "EditThinker performs both tasks in a single forward pass."
[^c14]: arxiv-2512-05965 — "successfully prompted the Editor to produce a better image"
[^c15]: arxiv-2512-05965 — "as the critic expert (E) to evaluate the resulting image"
[^c16]: arxiv-2512-05965 — "Qwen-Image-Edit from 4.36 to 4.37"
[^c17]: arxiv-2512-05965 — "performance is directly and positively correlated with the"
[^c18]: arxiv-2512-05965 — "Ablation on GEdit-Bench-EN with Expert Model in"
