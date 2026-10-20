---
description: "A video-model hallucination is judged against either the video (faithfulness) or verifiable world knowledge (factuality); an answer can pass one basis and fail the other."
aliases: ["faithfulness versus factuality hallucination", "video-grounded versus knowledge-grounded hallucination", "evidence-basis taxonomy of hallucination"]
sources: ["doi-10-48550-arxiv-2603-11481"]
---
# Evidentiary basis of hallucination

A hallucination is an output that fails some check, and the check is not defined until one says what the output must agree with. INFACT takes that choice as its organising axis. Its taxonomy is built "by the evidentiary basis required for verification, where faithfulness requires alignment with visual content and factuality necessitates consistency with world knowledge."[^c1] The abstract puts the two in one sentence: outputs "that contradict either video evidence (faithfulness) or verifiable world knowledge (factuality)."[^c2]

The two bases are different kinds of check. A faithfulness hallucination "contradict[s] explicit visual evidence in the video";[^c3] a factuality hallucination contradicts world knowledge, and the authors restrict that side to claims that can be settled: "We restrict factuality to objectively verifiable knowledge and explicitly exclude subjective or ambiguous claims."[^c4] Factuality items are then split by the knowledge they need: Domain Knowledge (Know-WHAT), Procedural Knowledge (Know-HOW) and Physical Knowledge (Know-WHY).[^c5]

The split changes what a question can test. A question about what happens in the clip is settled, in principle, by the frames. A question about which festival is shown, or whether a sequence of steps is possible, is settled by knowledge that the frames only prompt. A wrong answer therefore has two possible explanations, a perception failure or a knowledge failure, and an accuracy figure that merges the two cannot say which occurred. The authors' motivation is that the existing literature is lopsided: benchmarks "predominantly focus on faithfulness hallucinations,"[^c6] and factuality hallucinations requiring verifiable world knowledge are "much less explored."[^c7]

What survives the transfer out of video: the axis is the source a claim answers to. Whatever the model is, a question-writer who wants to know whether a wrong answer came from looking or from knowing has to build items on both bases and score them apart. This is my inference from the paper's design, not a result it reports.

"Faithfulness" here does not mean the faithfulness of stated reasoning studied in chain-of-thought work, where the question is whether an explanation reflects what drove the answer (see [[verbalization-incompleteness-versus-unfaithfulness]] and [[supported-faithfulness-score]]). In INFACT the question is whether the answer agrees with the video. The two senses should be kept apart when reading either literature.

## Limits

- The partition is the authors'. Three faithfulness levels and three factuality categories are their construction; the sections read do not test whether another partition gives the same picture.
- Factuality is restricted to objectively verifiable claims by design. The basis split says nothing about contested, subjective or value-laden claims, which the benchmark leaves out.
- The labels rest on source benchmarks (MVBench, Video-MME, TOMATO, CityGuesser-style data, synthetic videos), an LLM-ensemble filter and human-in-the-loop verification.[^c8] The text read reports no agreement statistic for the human check.
- The paper shows that the two bases are scored separately. It does not show that they have separate causes inside a model; the separation is in the measurement.
- Tested only on video-language models. Whether the same two-basis split is useful for text-only models is not shown here.

## Related

- [[structural-versus-parametric-evidence]] — the same question of which source an answer rests on, in retrieval and tool settings
- [[clean-noisy-semantic-gap-entropy]] — a video-VLM hallucination detector, the detection side of the same audit
- [[text-modality-dominance]] — which input modality an omni-model's answer rests on when that input is corrupted

[^c1]: doi-10-48550-arxiv-2603-11481 — "We categorize hallucinations by the evidentiary basis required for verification, where faithfulness requires alignment with visual content and factuality necessitates consistency with world knowledge."
[^c2]: doi-10-48550-arxiv-2603-11481 — "outputs that contradict either video evidence (faithfulness) or verifiable world knowledge (factuality)"
[^c3]: doi-10-48550-arxiv-2603-11481 — "Faithfulness hallucinations occur when model outputs contradict explicit visual evidence in the video."
[^c4]: doi-10-48550-arxiv-2603-11481 — "We restrict factuality to objectively verifiable knowledge and explicitly exclude subjective or ambiguous claims."
[^c5]: doi-10-48550-arxiv-2603-11481 — "Factuality items require consistency with world knowledge and cover Domain Knowledge (Know-WHAT)"
[^c6]: doi-10-48550-arxiv-2603-11481 — "predominantly focus on faithfulness hallucinations"
[^c7]: doi-10-48550-arxiv-2603-11481 — "whereas factuality hallucinations requiring verifiable world knowledge are much less explored"
[^c8]: doi-10-48550-arxiv-2603-11481 — "a human-in-the-loop verification stage is further conducted"
