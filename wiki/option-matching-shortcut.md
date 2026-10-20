---
description: "Showing multiple-choice options lets reasoning models match candidates instead of deducing; removing options raised their ToM accuracy markedly (R1 0.549 to 0.691) while a non-reasoning model fell."
aliases: ["option anchoring in reasoning", "choice-level shortcut", "option-level shortcut"]
sources: ["arxiv-2602-10625", "arxiv-2512-16978", "arxiv-2512-01274", "arxiv-2511-20086", "arxiv-2511-17405"]
---
# Option-matching shortcut

When a question comes with explicit answer candidates, a reasoning model can stop deducing from the story and instead search for superficial justifications for each candidate. The study modified the HiToM theory-of-mind benchmark by removing the multiple-choice candidates, so models had to extract the answer directly; HiToM was chosen because its answers are extractive and can be scored open-ended.[^c1]

Measured effect: with options removed, reasoning models improved substantially. DeepSeek-R1 went from 0.549 to 0.691 and Qwen3-8B in reasoning mode from 0.481 to 0.629, whereas the non-reasoning Qwen3-8B dropped from 0.557 to 0.510.[^c2] The authors read this as options short-circuiting deduction so that reasoning models anchor on shallow overlaps, while non-reasoning baselines rely on choice-level signals and lose them when options go.[^c3]

Qualitatively, with options present reasoning models "abandon linear deduction" and run a chaotic search for justifications; without options the same model on the same question shows structured deductive thinking.[^c4] The paper's takeaway is that explicit options lead to shortcuts that prioritize superficial matching over deduction.[^c5]

For asking: the form of the question (closed candidates versus open) changes which process produces the answer, not only how it is scored. This reading is mine; the paper measured only accuracy and trace behavior.

The shortcut also shows up in long-video question answering, where the same comparison is run by removing the options. On Video-MME the authors re-evaluated models with the options removed and answers forced open-ended; the monolithic omni-models lost 13.6 to 18.7 points.[^c6][^c7] The agent that answers from retrieved evidence rather than choosing from a list hardly moved, and the authors read the gap as comprehension rather than option-matching.[^c8] This is a different domain and a different measure (accuracy drop on video, not reasoning traces on theory of mind), so it points the same way without testing the same mechanism.

A benchmark built against this route. SUPERChem (arxiv-2512-01274) treats closed options as a route to back-solving and designs its multiple-choice items to block it. It states that the problems were reformulated to prevent solving by working backwards from the options; some items ask for an intermediate quantity instead of a full answer, and "benchmark includes up to 26 options for some problems" so that "This dramatically lowers the probability" of a lucky pick.[^c9][^c10][^c11] The paper reports no ablation of these choices, so it does not show that they remove the match-to-candidate shortcut; the design is its stated intent. Its answers are scored by accuracy plus a fidelity measure of the reasoning, see [[reasoning-path-fidelity]].

A prompting route keeps the options on the page and asks for something else of them. BiasPrompting first asks for a supporting reasoning for each option, "treating each as if it were correct," and only then asks for a choice from the set of reasonings (see [[per-option-elaboration]]).[^c12] The paper reports accuracy gains on commonsense multiple-choice sets, not a test of the match-to-candidate mechanism itself; whether per-option elaboration reduces the shortcut that the HiToM study measures is open (my inference).

The same channel shows up at the level of benchmark scores. ReVeL states that the options "may leak exploitable signals, which makes the accuracy metrics unreliable."[^c13] On the questions that remain answerable without options, models "achieve consistently lower accuracy than" the multiple-choice format, and the authors read the gap as models using option information they do not have the knowledge to supply.[^c14][^c15] The measure is accuracy, not reasoning traces, so it does not separate option matching from the cue-reading in [[answer-option-surface-cue]]; the two are different routes to an inflated score.

## Limits

Tested on one benchmark (HiToM) with a handful of models; open-source models only for the intervention that follows (Think-to-Match). The paper attributes the gain to a shortcut from trace inspection of examples, not a controlled causal test; open-ended scoring may also differ in difficulty in ways not separated here. Whether the effect holds outside theory of mind is not shown. The video re-run is one paper on Video-MME and WorldSense, and its agent is a different system from the monolithic models, so the answer-format effect is not separated from architecture there.[^c8]

## Related

- [[reasoning-shortcut]] — shortcuts in reasoning generally
- [[format-induced-answer-collapse]] — answer format altering answer quality
- [[planning-theory-of-mind-elicitation-gap]] — theory-of-mind elicitation in LLMs
- [[reasoning-trap]] — reasoning effort can hurt

[^c1]: arxiv-2602-10625 — "we modified the HiToM benchmark by removing multiple-choice candidates, requiring models to extract answers directly."
[^c2]: arxiv-2602-10625 — "DeepSeek-R1 surges from 0.549 to 0.691, and Qwen3-8B-Reasoning improves from 0.481 to 0.629."
[^c3]: arxiv-2602-10625 — "explicit candidates shortcircuit deduction, causing reasoning models to anchor on shallow overlaps."
[^c4]: arxiv-2602-10625 — "reasoning models often abandon linear deduction, instead engaging in a chaotic search to find superficial justifications for potential choices."
[^c5]: arxiv-2602-10625 — "Explicit options lead to shortcuts in reasoning, causing models to prioritize superficial matching over deduction."
[^c6]: arxiv-2512-16978 — "the options removed, forcing open-ended answers"
[^c7]: arxiv-2512-16978 — "Qwen3-Omni-Instruct 18.7 pts, and Qwen3Omni-Thinking 13.6 pts"
[^c8]: arxiv-2512-16978 — "LongShOTAgent, which generates answers from retrieved evidence"
[^c9]: arxiv-2512-01274 — "the problems were reformulated to prevent solving by working backwards from"
[^c10]: arxiv-2512-01274 — "benchmark includes up to 26 options for some problems"
[^c11]: arxiv-2512-01274 — "This dramatically lowers the probability"
[^c12]: arxiv-2511-20086 — "treating each as if it were correct"
[^c13]: arxiv-2511-17405 — "the options may leak exploitable signals, which makes the accuracy metrics unreliable"
[^c14]: arxiv-2511-17405 — "models achieve consistently lower accuracy than"
[^c15]: arxiv-2511-17405 — "it is often utilizing the information embedded in the option set even when it does not actually have"
