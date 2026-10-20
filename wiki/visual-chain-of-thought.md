---
description: "Text-only chain of thought cannot revisit the images it reasons over; inserting tool-made visual observations (re-sampled frames, marked objects) into the chain helps on spatial and video tasks."
aliases: ["visual chains of thought", "thinking with images", "visual thinking trajectories", "visual thoughts from tools"]
sources: ["arxiv-2511-19261"]
---
# Visual chain of thought

A text-only chain of thought reasons over the input it was given and cannot change what it looks at. The LAST paper locates the failure there: text-only CoT "ignores the rich and continuous visual world"[^c1], and most vision-language models "can only generate text tokens, which prevents them from naturally producing visual reasoning steps."[^c2] The proposal is to put visual observations inside the chain. Its key idea is to "explicitly incorporate visual tokens into the reasoning process, forming visual chains of thought"; since the model cannot emit pixels, the visual tokens come from external tools, such as object tracking and grounding.[^c3]

The mechanism is a loop of text steps and tool calls. The model writes a thought and names a tool; the tool returns a visual observation, which goes back into the context; the model continues from it. The paper's Figure 1 gives the clearest case. A text-only chain "cannot see the basket due to missing frames between the second and third sampled frames"[^c4]. The visual chain first calls frame selection to re-sample the video, then grounding to locate the objects, and "achieves the correct solution by building intermediate visual trajectories."[^c5] The loop is therefore a way of re-presenting parts of the input at the point where the reasoning needs them, not a second pass over the same fixed frames.

The paper also measured design choices within the tools. For object tracking, the observation is a mark, not a mask: "simply adding marks achieves the best performance", and the authors attribute the failure of whole-object masks to the fact that "using the whole mask occludes visual content."[^c6][^c7] So the observation is judged by whether it keeps the scene visible as well as by whether it carries the object. For frame selection the stated reason is that models "are confused by irrelevant context"[^c8], which makes choosing which frames re-enter the chain a step of its own.

What was measured. In the comparison of thinking modes, the authors report that text-only CoT "degrades performance on some benchmarks, e.g., EgoSchema and NExT-QA."[^c9] On EgoSchema the visual chain scores "85.4 vs. 62.7" for text CoT.[^c10] Against the untouched GPT-4o baseline the visual chain "achieves 15.8% improvement on EgoSchema" with eight frames.[^c11] For the fine-tuned Qwen2.5-VL-7B model, the training data include visual trajectories built only for questions the text chain could not solve: the pipeline uses "visual tools to solve questions that can not solved by text CoT."[^c12] The ablation reports that "training data with visual thinking trajectories will significantly improve the performance of the base" model.[^c13] Multi-turn use beat single-turn use: "multi-turn mode gets significant gains compared" with single-turn.[^c14] Most questions needed "one or two tools to be solved."[^c15]

Cost. The chain trades text for pixels: "LAST uses more visual tokens, while text-only CoT uses more text tokens."[^c16] The authors report that the average added latency against the base model "is less than 1 second" on their serving setup.[^c17]

## Limits

The contrast is visual observations against text, but the read text does not show a text chain given the same tool outputs written out as words. Without that control, a gain could come from the extra information a tracker or depth model supplies, not from the visual form of the observation. The paper names its own tools: "we use SAM2 to identify and follow the movement of the object c in a visual sequence."[^c18] That is an outside model, so the zero-shot result is not free of extra inputs in the sense the paper's framing suggests. This is my inference from the sections read.

The fine-tuning data are selected. Visual trajectories were built for questions text CoT failed, so the training set over-represents the cases where a text chain breaks. Whether the gains carry over to questions text CoT already solves is not shown in the slices read.

The benchmarks are spatial and video question answering (ScanQA, SQA3D, VSI-Bench, EgoSchema, NExT-QA, LVBench), run on a few base models (GPT-4o zero-shot, Qwen2.5-VL-7B fine-tuned). The slices read do not test tasks outside those benchmarks, or a model that was not trained on the tool traces.

The paper reports which tools are used and how often, not whether each observation was needed. In the slices read there is no run that drops the visual observation while keeping the same call pattern, so the claim that the observations themselves carry the effect is not tested here.

The chain costs visual tokens and calls. The latency figure is a single hardware setup. The paper's own accounting says the chain uses "more visual tokens," and its gains are reported per benchmark, not per question.

A prior line of "thinking with images" work injected visual information in a similar way on 2D images, and this paper's stated shift is to "3D space and videos"[^c19]. Whether the same loop behaves the same on 2D images is not established by this paper's spatial results.

## Related

- [[tool-integrated-reasoning]] — the same pause, call and re-entry loop, but what re-enters is an image or frame here, not code output or a text summary.
- [[latent-visual-thought]] — the other route to visual steps inside a reasoning chain: latent tokens trained to match sketches, with no tool and no pixels. This note's chain re-presents pixels through tools instead.
- [[visual-forgetting-during-reasoning]] — attention to input images falls as a chain lengthens, and a tool call that re-presents an image restores it. My inference: this is one measured reason a chain benefits from re-presenting the image rather than relying on earlier text.
- [[convergence-ceiling-dissociation]] — another comparison of a visual chain against a language chain, where the visual one trains faster but reaches no higher ceiling; the two notes disagree on what visual steps buy.

[^c1]: arxiv-2511-19261 — "ignores the rich and continuous visual world"
[^c2]: arxiv-2511-19261 — "can only generate text tokens, which prevents them from naturally producing visual reasoning steps"
[^c3]: arxiv-2511-19261 — "explicitly incorporate visual tokens into the reasoning process, forming visual chains of thought"
[^c4]: arxiv-2511-19261 — "cannot see the basket due to missing frames between the second and third sampled frames"
[^c5]: arxiv-2511-19261 — "LAST achieves the correct solution by building intermediate visual trajectories"
[^c6]: arxiv-2511-19261 — "simply adding marks achieves the best performance"
[^c7]: arxiv-2511-19261 — "using the whole mask occludes visual content"
[^c8]: arxiv-2511-19261 — "are confused by irrelevant context"
[^c9]: arxiv-2511-19261 — "text-only CoT [84] degrades performance on some benchmarks, e.g., EgoSchema [50] and NExT-QA [89]"
[^c10]: arxiv-2511-19261 — "85.4 vs. 62.7 on EgoSchema"
[^c11]: arxiv-2511-19261 — "it achieves 15.8% improvement on EgoSchema"
[^c12]: arxiv-2511-19261 — "visual tools to solve questions that can not solved by text CoT"
[^c13]: arxiv-2511-19261 — "training data with visual thinking trajectories will significantly improve the performance of the base"
[^c14]: arxiv-2511-19261 — "multi-turn mode gets significant gains compared"
[^c15]: arxiv-2511-19261 — "or two tools to be solved"
[^c16]: arxiv-2511-19261 — "visual tokens, while text-only CoT uses more text tokens"
[^c17]: arxiv-2511-19261 — "is less than 1 second"
[^c18]: arxiv-2511-19261 — "we use SAM2 to identify and follow the movement of the object c in a visual sequence"
[^c19]: arxiv-2511-19261 — "visual information into the thinking process"
