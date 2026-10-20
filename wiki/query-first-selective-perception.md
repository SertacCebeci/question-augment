---
description: "Let the question decide where to look: a plan of intent-tied segments is made before any frames are encoded, and reasoning and looking alternate until an answer is confident."
aliases: ["reason-then-perceive", "query-driven perception", "query-conditioned selective perception", "intent-guided frame selection", "process-then-reason contrast"]
sources: ["arxiv-2512-09354"]
---
# Query-first selective perception

A model that must answer from a long source can order two steps differently. The usual order is to perceive the whole source first and reason afterwards. The other order takes the question first: it decides which part of the source is worth perceiving, perceives only that part, and then reasons. The Video-QTR paper names the usual order "process-then-reason" and describes it as a paradigm "which analyzes visual streams exhaustively before semantic reasoning."[^q1] Its proposal reverses the order into what it calls "reason-then-perceive", where "perception is actively guided by semantic intent".[^q2]

The mechanism has three parts. A planner, the Reason Temporal Proxy, turns the query into a sequence of temporal intents, each an intent token ("what to look for") paired with an interval ("when the event occurs").[^q3] The paper states the purpose as "These intents guide perception, enabling reasoning-first and" selective perception.[^q4] A perception module then encodes only the frames inside the proposed intervals, so the number of encoded frames K is much smaller than the source length N. The paper adapts the density inside those intervals too: it adapts "the sampling rate based on semantic variance, using denser" sampling where the scene changes.[^q5]

The loop is what makes the order matter. The planner's next intent is conditioned on the query, the accumulated perception memory and the reasoning state; the paper writes this as a function of those three, and says "The LLM refines the next temporal intent" from the hypothesis-evidence consistency of what has been seen.[^q6] A separate answering step reports a confidence score, and the paper uses a high score as the signal to stop searching.[^q7]

The argument against saliency-based selection is the part that carries over. Earlier methods reduce cost "by highlighting salient frames or objects, assuming that visual importance directly correlates with reasoning relevance."[^q8] The paper's position is that these are different things, so selection should follow the question's intent and not visual prominence. In text, the same separation appears as [[salience-relevance-decoupling]]. My reading, not the paper's: for an answerer, the question is the only source of a prior over where the answer lies, and a question-first order is one way to use that prior before the evidence is seen.

What was measured: the abstract reports "reducing input frame consumption by up to 73%" alongside state-of-the-art accuracy on five benchmarks.[^q9] On the MovieChat long-video benchmark the paper reports processing "only 202.39 frames on average" in its on-demand mode.[^q10] In the planner ablation, the paper replaces the planner with a random segment selector and reports the result as "this leads to a 30.4% drop" in total accuracy, concluding that "query-conditioned temporal planning is crucial for efficient long-video understanding."[^q11]

## Limits

- The ablations are on one benchmark. The paper's ablation figure is captioned "Ablation study on MovieChat benchmark."[^q12] Whether the planner's contribution holds on the short-video sets was not shown in the parts read.
- The planner ablation swaps in random segments, not uniform sampling at a matched frame count. The text I read reports no matched-budget uniform baseline, so the 30.4% drop does not separate query-driven choice from any sparse selection at that budget. That separation is my inference, not a result of the paper.
- Frame counts are not matched across methods. The "up to 73%" is a best case over benchmarks, and the 202.39 figure is an average under the method's own stopping rule, set against baselines that used fixed budgets.
- The stop rule rests on the answerer's self-reported confidence. The paper calls a high score "a reliable, data-driven criterion,"[^q13] but the text does not measure how often a high score is wrong. See [[stop-continue-criteria-in-retrieval-loops]].
- The planner is an LLM and the frame encoder is CLIP-based. Whether query-first selection survives a weaker planner, or a question that does not localize in time, is not tested in the text read.
- Choosing where to look before seeing evidence can fail when the choice is hard. A related figure-side result found that localizing before reasoning lowered accuracy; see [[coarse-to-fine-evidence-zoom]].

## Related

- [[coarse-to-fine-evidence-zoom]] — localize-then-zoom in two fixed passes; the same query-conditioned localization, but the grain changes rather than whether to observe at all
- [[on-demand-resolution-zoom]] — the answerer asks for a finer look mid-reasoning; here the planner proposes whole intervals before any look
- [[salience-relevance-decoupling]] — visual or textual prominence versus relevance to the question; the paper's case against saliency-based frame selection
- [[reason-chunking]] — proposition-level looks at a text source, each made after the reasoning step that needs it
- [[query-adaptive-evidence-granularity]] — the grain of evidence is fixed from the question before retrieval; this note is about which evidence is observed at all
- [[stop-continue-criteria-in-retrieval-loops]] — the confidence-based stop as one case of when an iterative loop ends

[^q1]: arxiv-2512-09354 — "analyzes visual streams exhaustively before semantic reasoning."
[^q2]: arxiv-2512-09354 — "where perception is actively guided by semantic intent"
[^q3]: arxiv-2512-09354 — "allowing the LLM to control when and where to observe."
[^q4]: arxiv-2512-09354 — "These intents guide perception, enabling reasoning-first and"
[^q5]: arxiv-2512-09354 — "sampling rate based on semantic variance, using denser"
[^q6]: arxiv-2512-09354 — "The LLM refines the next temporal intent"
[^q7]: arxiv-2512-09354 — "a high confidence score provides a reliable, data-driven criterion"
[^q8]: arxiv-2512-09354 — "reduce costs by highlighting salient frames or objects, assuming that visual importance directly correlates with reasoning relevance"
[^q9]: arxiv-2512-09354 — "reducing input frame consumption by up to 73%"
[^q10]: arxiv-2512-09354 — "processing only 202.39 frames on average"
[^q11]: arxiv-2512-09354 — "this leads to a 30.4% drop"
[^q12]: arxiv-2512-09354 — "Ablation study on MovieChat benchmark"
[^q13]: arxiv-2512-09354 — "a high confidence score provides a reliable, data-driven criterion"
