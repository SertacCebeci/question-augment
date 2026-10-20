---
description: "In RL for search agents, a prompt that forces explicit reasoning before each decision led to longer rollouts, a surge in think tags and training collapse; a direct-decision prompt was more stable."
aliases: ["Slow Thinking template collapse", "Fast Thinking template", "think-tag surge before collapse"]
sources: ["doi-10-48550-arxiv-2602-19526"]
---
# Reasoning-length training collapse

The prompt used in RL training decides how much explicit reasoning each rollout contains, and that amount can destabilize training. The work compares two prompt templates for a Search-R1-style agent. The Slow Thinking template, from the prior work, requires the model to reason inside think tags before its search and answer decisions. The Fast Thinking template asks for the search and answer decisions directly. The authors find that "Fast Thinking template exhibits more stable training dynamics, whereas Slow" training is "more likely to lead to training collapse".[^c1]

The mechanism they report runs through the length and structure of rollouts. Before collapse, the Slow-template runs "consistently produce longer responses than those with the Fast Thinking template", and there is "a marked jump around the collapse point".[^c2] In the same phase, the model begins to produce several think segments before one search or answer: "prior to collapse, we observe that the model begins to generate multiple <think> segments before a single" decision.[^c3] The authors tie this repeated-think pattern to the collapse itself, which is the point where the logged score falls.

In accuracy the switch gave a gain on the same setup: "improving overall correctness from 0.403 to 0.422 on" the benchmark average, with the Fast template ahead.[^c4] The authors' summary of the prompt dimension is general: "The longer the explicit reasoning length, the worse the accuracy and training" stability.[^c5]

## Limits

- The main analysis is on Qwen2.5-7B: "perform the analysis using Qwen2.5-7B" is the stated default, and the other model size is checked separately.[^c6] Only two templates were compared, and both are the authors' own variants of a fixed template family.
- The think-tag surge is observed before collapse. That is a temporal association in the training logs; the text does not establish that the surge causes the collapse rather than appearing alongside it.
- The result concerns stability in RL training. It says nothing about whether less reasoning helps accuracy on tasks where reasoning matters at inference; the Fast template may be the right choice for search-and-answer tasks and the wrong one elsewhere.
- The paper's own account is that the Slow template "encourages reasoning expansion for rewards, undermining training stability".[^c7] That is a claim about this training setup and this retriever (E5 over 2018 Wikipedia, top-3), not about reasoning length in general.

## Related

- [[moderate-adaptive-reasoning-length]] — at inference, longer reasoning lowered accuracy on theory-of-mind tasks and a length cap helped; the same direction, measured in a different setting and with no training
- [[answer-avoidance-collapse]] — the other collapse in this paper, caused by withheld answers rather than by long reasoning

[^c1]: doi-10-48550-arxiv-2602-19526 — "Fast Thinking template exhibits more stable training dynamics, whereas Slow"
[^c2]: doi-10-48550-arxiv-2602-19526 — "Thinking template consistently produce longer responses than those with the Fast Thinking template"
[^c3]: doi-10-48550-arxiv-2602-19526 — "prior to collapse, we observe that the model begins to generate multiple <think> segments before a single"
[^c4]: doi-10-48550-arxiv-2602-19526 — "improving overall correctness from 0.403 to 0.422 on"
[^c5]: doi-10-48550-arxiv-2602-19526 — "The longer the explicit reasoning length, the worse the accuracy and training"
[^c6]: doi-10-48550-arxiv-2602-19526 — "perform the analysis using Qwen2.5-7B"
[^c7]: doi-10-48550-arxiv-2602-19526 — "encourages reasoning expansion for rewards, undermining training stability"
