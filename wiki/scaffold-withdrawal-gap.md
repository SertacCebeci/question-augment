---
description: "Multimodal model accuracy falls as cues and step-by-step guidance are withdrawn from zero-shot to agentic evaluation; the drop measures dependence on prompt scaffolding."
aliases: ["autonomy gap", "guidance-withdrawal gap", "zero-shot to agentic gap"]
sources: ["arxiv-2512-16250"]
---
# Scaffold withdrawal gap

A question put to a model can arrive with its answer path already laid out: the relevant cues pointed at, the steps named, the tools mentioned. The same question can also arrive bare. Chowdhury et al. measure the difference by running one benchmark under three protocols that differ in how much of that structure the model receives. "It evaluates MLLMs across three modes zero-shot, guided, and agentic and six task families."[^c1]

The levels are ordered by how much the prompt carries. In zero-shot evaluation the model gets only the input: "It receives only the raw video and the question as input."[^c2] Guided evaluation adds perceptual aids, "the model receives auxiliary perceptual cues such as pre-computed face crops," together with instructions on using them. The authors describe this as "an assisted agent with external signals but limited autonomy."[^c3][^c4] Agentic evaluation removes the instructions: "The most challenging regime removes all explicit hints about tool availability or intermediate steps."[^c5] The external modules stay available at runtime, but the model "must discover and invoke them implicitly through its own reasoning."[^c6]

The mechanism the gap isolates is what a model loses when the question stops carrying the path. The reported decline is monotone: "Model accuracy and reasoning coherence consistently drop as autonomy"[^c7] moves from zero-shot to agentic. It is not uniform across tasks. Audio-visual summarization, speaker temporal grounding and cross-modal narrative linking "exhibit the steepest performance decline from guided to autonomous modes," while "next-speaker prediction and speaker association remain more stable."[^c8][^c9]

Guided scores are the most flattering. The paper reports that models such as GPT-4o and Qwen3-Omni "perform competitively in guided" settings, but their "reasoning quality, turn attribution, and temporal flow degrade sharply without instructions."[^c10][^c11] A score read under guidance can therefore report what the model does with the path supplied, not what it does when it must find the path itself. The authors read the pattern as a dependence: "prompt scaffolding currently substitutes for robust multimodal representations."[^c12] That is their interpretation of the decline across modes; the modes were not varied one factor at a time to test it.

For asking, the gradient says that the amount of structure a question carries changes the measured ability. For answering, the same question may be answered well with its path given and poorly without it.

The gap is cross-sectional: it compares protocols at one time. [[reinforced-scaffold-fading]] studies a designed decay of scaffolding toward learner independence over a schedule. [[scaffolding-collapse]] is the reverse failure, a tutor that abandons its guidance under pressure and gives the answer. [[chain-of-inquiry-scaffolding-effect]] shows that an ordered chain of questions adds gain; the gradient here is what remains when that kind of structure is absent. [[agent-autonomy-as-complexity-frontier]] varies task size at fixed guidance, while this note varies guidance at a fixed task.

## Limits

- One benchmark, AMUSE, in one arXiv preprint by its own authors ("arXiv:2512.16250v1 [cs.AI] 18 Dec 2025").[^c13] The clips are 10 to 50 seconds of multi-person conversations such as talk shows, interviews and podcasts.[^c14] Nothing here transfers the gradient to other domains or to text-only tasks.
- The three modes differ in more than cue support. Guided prompts carry structured metadata and step-by-step instructions, and agentic mode also places tool invocation on the model. The gap therefore mixes the loss of supplied information with the loss of a skill, deciding which tool to call and when. The paper does not separate the two (my observation).
- A monotone decline with less input is what one expects with or without a representational dependence. The gradient alone cannot tell missing information from missing representation, so "substitutes for robust representations" is a reading, not a measured cause.
- The closed-source edge is reported only for zero-shot and guided conditions: "counterparts in subjective and objective metrics under zero-shot and guided conditions."[^c15] Whether the gap is smaller for the strongest models under agentic evaluation is not shown here.
- The metrics mix BLEU, METEOR, CIDEr and a GPT-based judge. A gap in these scores is not the same as a gap in whether an answer is correct.

## Related

- [[reinforced-scaffold-fading]] — a scheduled decay of scaffolding toward independence; this note's gap is the unscheduled, between-protocol version
- [[scaffolding-collapse]] — the reverse failure, where guidance is dropped under pressure and the answer is given
- [[chain-of-inquiry-scaffolding-effect]] — structure added by question order; the gradient is what remains without it
- [[tool-use-robustness-gap]] — agentic mode depends on tool outputs, and corrupted tool responses lower accuracy across nearly all tested pairs
- [[agent-autonomy-as-complexity-frontier]] — autonomy measured against task complexity, at fixed guidance

[^c1]: arxiv-2512-16250 — "It evaluates MLLMs across three modes zero-shot, guided, and agentic and six task families"
[^c2]: arxiv-2512-16250 — "It receives only the raw video and the question as input."
[^c3]: arxiv-2512-16250 — "the model receives auxiliary perceptual cues such as pre-computed face crops"
[^c4]: arxiv-2512-16250 — "an assisted agent with external signals but limited autonomy"
[^c5]: arxiv-2512-16250 — "The most challenging regime removes all explicit hints about tool availability or intermediate steps."
[^c6]: arxiv-2512-16250 — "model must discover and invoke them implicitly through its own reasoning"
[^c7]: arxiv-2512-16250 — "Model accuracy and reasoning coherence consistently drop as autonomy"
[^c8]: arxiv-2512-16250 — "exhibit the steepest performance decline from guided to autonomous modes"
[^c9]: arxiv-2512-16250 — "next-speaker prediction and speaker association remain more stable"
[^c10]: arxiv-2512-16250 — "While models such as GPT-4o and Qwen3-Omni perform competitively in guided"
[^c11]: arxiv-2512-16250 — "their reasoning quality, turn attribution, and temporal flow degrade sharply without instructions"
[^c12]: arxiv-2512-16250 — "prompt scaffolding currently substitutes for robust multimodal representations"
[^c13]: arxiv-2512-16250 — "arXiv:2512.16250v1 [cs.AI] 18 Dec 2025"
[^c14]: arxiv-2512-16250 — "multi-person conversations such as talk shows, interviews, and podcasts etc."
[^c15]: arxiv-2512-16250 — "counterparts in subjective and objective metrics under zero-shot and guided conditions"
