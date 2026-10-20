---
description: "Decomposing multi-turn QA into an ask-vs-answer clarification policy and post-clarification answering shows fine-tuning fixes the former fast but leaves the latter the main bottleneck."
aliases: ["post-clarification answering bottleneck"]
sources: ["su-2026-clarification"]
---
# Post-clarification answering bottleneck

> After a system correctly decides to ask a clarifying question, producing
> the right final answer once the user has replied is a harder, separately
> measured failure than the ask-vs-answer decision itself.

## Definition / Mechanism

Su & Healey (2026) decompose multi-turn
under-specified QA into two components: a **clarification policy**, which
decides whether the next action should be to ask a clarifying question or
answer directly, and **post-clarification answering**, which produces the
correct final answer once the missing information has been supplied. They
report a metric — final-answer accuracy conditioned on the model having
taken the correct action — that isolates the second component from the
first.[^c1]

On PACIFIC (Deng et al., 2022, a multi-turn financial QA benchmark with
naturally occurring ambiguous and unambiguous turns), supervised
fine-tuning of Llama-3-8B-Instruct and Qwen2.5-7B-Instruct raises action
accuracy on ambiguous turns from near zero to 0.68 (Llama) and 0.71 (Qwen),
while accuracy on turns that should be answered directly drops by at most
0.02.[^c2]

Conditioned on taking the correct action, final-answer accuracy on
ambiguous turns after fine-tuning remains low and clearly below the
unconditional gain in action accuracy: 0.28 vs. an unconditional Final Acc
of 0.19 for Llama, 0.18 vs. 0.13 for Qwen. The paper's own reading: the
remaining bottleneck is not deciding whether to clarify, but correctly
combining the user's disambiguating reply with the dialogue context to
answer.[^c3]

Two additional interventions tested by the same paper do not close the
gap: varying the amount or composition of synthetic clarification-turn
augmentation gives only modest, quickly-saturating gains, and appending
GPT-4o-generated reasoning traces to each turn does not solve the
bottleneck and can degrade performance.[^c4]

## Why it matters

The literature on this stall largely optimizes the ask-vs-answer decision
(when to stop asking and commit to an answer). This result measures the
two halves of that pipeline separately and finds the second half —
turning a given answer into the right final output — absorbs most of the
remaining error once the first half is fixed by ordinary fine-tuning. A
procedure that only tunes its stopping rule, without separately checking
whether it correctly uses what it is told, is optimizing the smaller of
the two gaps.

## Limits

- Single benchmark (PACIFIC), financial domain, questions grounded in
  tables with extractive or calculation-based answers; the paper's own
  limitations section flags that findings may not generalize to
  open-ended generative tasks.[^c5]
- Two models only (Llama-3-8B-Instruct, Qwen2.5-7B-Instruct), one
  fine-tuning recipe (full-parameter SFT); user replies and final-answer
  correctness are both judged by GPT-4o rather than humans.
- The claim rests on a single conditional metric (Final Acc cond.); it
  does not decompose *why* post-clarification answering fails (wrong
  clarifying question asked vs. correct question but misused reply).

## Related

[[multi-turn-clarification-plateau]] · [[clarification-benchmarks]] · [[value-of-information]]

[^c1]: su-2026-clarification — "a clarification policy, which decides whether to ask a clarifying question or answer directly, and post-clarification answering, which produces the correct final answer once the missing information is provided"
[^c2]: su-2026-clarification — "After SFT, action accuracy on ambiguous turns rises to 0.68 for LLaMA and 0.71 for Qwen, while accuracy on unambiguous turns remains high, decreasing by only 0.01 and 0.02, respectively."
[^c3]: su-2026-clarification — "On ambiguous turns, however, Final Acc (cond.) remains noticeably higher than Final Acc after SFT: 0.28 vs. 0.19 for LLaMA and 0.18 vs. 0.13 for Qwen."
[^c4]: su-2026-clarification — "We find that synthetic turn augmentation provides only modest gains and quickly saturates, varying the clarification rate has limited impact, and results are broadly consistent across different augmentation models. We also find that naive reasoning trace augmentation does not solve the bottleneck and can even degrade performance."
[^c5]: su-2026-clarification — "Our experiments are conducted exclusively on PACIFIC, a financial-domain benchmark whose questions are grounded primarily in tables and support mostly extractive or calculation-based answers. As a result, our findings may not directly generalize to other domains or to more open-ended generative tasks"
