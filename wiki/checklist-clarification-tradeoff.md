---
description: "A controlled comparison across three LLMs and four task types found upfront checklist-structured prompts beat interactive clarifying-question prompts on rubric quality, at under half the turns."
aliases: ["structured prompting"]
sources: ["ghosh-2026"]
---
# Checklist–clarification tradeoff

> Restructuring a prompt with a fixed checklist before sending it beat
> asking the model to interactively clarify it, on both output quality and
> interaction cost, in a small controlled comparison.

## The comparison

Ghosh, Polach & Sow (2026) tested three prompt conditions —
a raw prompt, a checklist-improved prompt (rewritten to add Roles/Rules,
Context, and Answer Format), and a clarifying-question prompt (the model
asks 1–3 questions before answering) — across four task types
(summarization, planning, explanation, coding) and three LLM systems
(ChatGPT, Claude, Grok), scoring each output 0–8 on a rubric of task
completion, correctness, compliance and clarity.

Checklist prompts scored highest (mean 7.50/8) and used the fewest tokens;
raw prompts scored lowest (5.67/8); clarifying-question prompts improved
over raw (6.67/8) but needed roughly double the turns of the other two
conditions (1.96 vs. 1.00 mean turns to acceptance) to get there.[^c1]

The authors' own hypothesis test makes the ordering explicit: the
prediction that clarifying questions would beat both other conditions
(H2) was only partially supported, and the prediction that both
structured conditions would reduce interaction effort relative to raw
(H3) held for the checklist but not for the clarifying-question
condition.[^c2]

The pattern was not uniform across models: ChatGPT and Grok scored
highest under the checklist condition, but Claude scored slightly higher
under the clarifying-question condition; Grok showed the widest
checklist-over-clarifying gap, with several trials where the clarifying
questions were on-topic but the final answer still drifted from the
original task.[^c3]

## Limits

- This note's ordering claim rests on one small-scale study: four fixed
  task prompts, three models, one human operator per model doing the
  scoring, with no inter-rater [[calibration|reliability]] check across operators and no
  blinding — acceptance was "based on the evaluator's judgment rather
  than an external user study."
- The checklist's three components (Roles/Rules, Context, Answer Format)
  were tested only as a bundle; the paper explicitly leaves their
  individual contributions to future ablation work, so this note cannot
  say which part of the checklist does the work.
- Interaction cost is measured by turns-to-acceptance and token count,
  not wall-clock time or a real user's tolerance for waiting through a
  clarification exchange.
- The clarifying-question condition was capped at 1–3 questions per task
  by the study design, not chosen adaptively by the model; a policy
  allowed more turns, or one trained to ask better questions, could shift
  the comparison.

## Related

[[clarification-benchmarks]] · [[question-budgets]] · [[value-of-information]]

[^c1]: ghosh-2026 — "Table III shows that checklist prompts achieved the highest mean rubric score, 7.50 out of 8, while also using the fewest average tokens. Raw prompts had the lowest mean score, 5.67 out of 8, and the highest average token use. Clarifying prompts improved over raw prompts, with a mean score of 6.67 out of 8, but required almost twice as many turns on average."
[^c2]: ghosh-2026 — "These results support H1: checklist-improved prompts produced higher-quality outputs than raw prompts. H2 was only partially supported. Clarifying-question prompts improved over raw prompts, but they did not outperform checklist-improved prompts overall. H3 was supported for checklist prompts but not for clarifying-question prompts."
[^c3]: ghosh-2026 — "ChatGPT and Grok achieved their highest mean scores with checklist prompts, while Claude achieved a slightly higher mean score with clarifying prompts. However, checklist prompts still required fewer turns overall. Grok showed the clearest gap between checklist and clarifying prompts; in several Grok trials, the clarifying questions were relevant, but the final answers sometimes strayed from the original task."
