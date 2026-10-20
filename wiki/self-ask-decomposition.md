---
description: "One prompt format in which the model emits an explicit follow-up question Self-ask (Press et al., 2022) is a few-shot prompt that ends with the scaffold *\"Are follow up questions needed here:\"*."
aliases: ["Self-Ask", "question decomposition"]
sources: ["press-2022", "yao-2022", "zhou-2022"]
---
# Self-ask and question decomposition

> One prompt format in which the model emits an explicit follow-up question
> before answering — and the sub-question, once demarcated, can be sent to
> something other than the model.

## Mechanism

Self-ask (Press et al., 2022) is a few-shot prompt that ends with the scaffold[^s1][^s2][^s3]
*"Are follow up questions needed here:"*. The model then emits `Follow up: <sub-question>`
and `Intermediate answer: …` in a loop, deciding itself how many follow-ups to
ask, and closes with `So the final answer is:`.

```text
Main question
  ↓
"Follow up:"  →  sub-question   →  answered by the LM, or by a search engine
  ↓                                 ↓
next "Follow up:"  … until "So the final answer is:"
```

Everything happens in one forward pass of one prompt. Because each sub-question
is a demarcated string, Press et al. (§3.3) stop generation at
`Intermediate answer:`, send the sub-question verbatim to a search API, paste
the result back, and continue — the same prompt, a different **source** for the
sub-answer.

## What was measured

- **Compositionality gap** — the fraction of 2-hop questions answered wrongly
  among those whose sub-questions the model answers correctly. On Compositional
  Celebrities (8.6k automatically generated 2-hop questions) it stays at roughly
  40% across GPT-3 from Ada (0.35B) to Davinci (175B) and across the InstructGPT
  series: it does **not** shrink with scale (Press et al., 2022, Fig. 1).
- **Self-ask vs. chain of thought**, Davinci-002 accuracy (Press et al., 2022,
  Table 1): Bamboogle (125 hand-written 2-hop questions) direct 17.6, chain of
  thought 46.4, self-ask 57.6, self-ask + search engine 60.0; 2WikiMultiHopQA
  29.8 / 30.0 / 40.1; Musique 12.6 / 13.8 / 15.2. The margin over chain of
  thought is ~11 points absolute on Bamboogle and ~0–1 point on the two
  template-generated datasets; routing the sub-questions to a search engine
  supplies the larger remaining gain on 2Wiki (+10).

## Neighbouring mechanisms — not this concept

- **ReAct** (Yao et al., 2022) interleaves free-form reasoning traces with
  *actions* on an environment: search/lookup/finish against a Wikipedia API on
  HotpotQA and FEVER, and physical actions in ALFWorld and WebShop, where it
  beats imitation and RL baselines by 34% and 10% absolute success rate. Its
  unit is a thought–action–observation triple, not an explicit sub-question.
- **Least-to-most** (Zhou et al., 2022) generates the whole list of sub-problems
  in a *separate* prompt pass, then solves them in order; on SCAN with
  code-davinci-002 it reaches ≥99% against 16% for chain of thought. Press et al.
  measure it against self-ask on 2Wiki (Table 2): 29.0 vs 35.5 accuracy, with
  self-ask using fewer generated tokens (569 vs 844).

## Why it matters — stall 4 (source)

What self-ask adds on the source stall is measured, not argued: making the
sub-question an addressable string lets the *same* prompt draw its constraint
from the model's own weights or from an external index, and Press et al. report
the difference that switch makes (Bamboogle 57.6 → 60.0, 2Wiki 30.0 → 40.1).

*Inference (this wiki, not a result of Press, Yao or Zhou):* we read the
sub-question loop as the concrete form of the **agent budget** in
[[question-budgets]] — cheap questions the agent puts to itself or to an index
rather than to the user — and the "ask 10,000 questions" idea as a change of
scale on that budget rather than a new mechanism. The ordering intuition it
shares with [[huffman-coding]] (settle first the decision the others depend on)
is a resemblance this wiki notices, not a formalism imported here: no
coding-theoretic optimality is claimed for sub-question order.

## Known as

| Field | Name there | Kind |
|---|---|---|
| LLM prompting (Press et al., 2022) | Self-Ask | exact — the authors' name for this prompt format |
| LLM prompting, general | question decomposition | close — the *family* (least-to-most, QDMR, decomposed prompting); self-ask is one member and the family's members are measured separately |

Not names for this concept: **ReAct** (Yao et al., 2022) — a reasoning/action
interleaving evaluated on interactive tasks, with no explicit sub-question; and
**least-to-most** (Zhou et al., 2022) — a separate decomposition pass, scored on
different benchmarks and against self-ask itself. An earlier version of this note
carried `ReAct` as an alias; it is a different object.

## Limits

- Evidence base: 2-hop English questions over facts on Wikipedia (Compositional
  Celebrities, Bamboogle, 2Wiki, Musique) with GPT-3-family models up to 175B —
  Press et al. flag both bounds themselves (§6). Decomposition helps when
  sub-answers are retrievable; for a design question there is nothing to retrieve.
- The advantage over chain of thought is large only on Bamboogle and ~zero on the
  template-generated sets, so "decomposition helps" is not established as a
  general effect — only for varied, unseen compositional questions.
- ReAct's numbers come from another evaluation domain (interactive tool use and
  embodied environments). Nothing in them carries over to compositional QA
  without retrieval, or to self-ask's format.
- Equating ReAct's reason–act loop with sub-question emission — the "shared
  lesson" this note used to be built around — is this wiki's reading, not a
  finding of either paper; neither claims it, and the two are measured on
  disjoint benchmarks.
- The agent-budget reading above is inference; [[question-budgets]] is itself a
  framework note with no source behind its numbers.

## Related

[[question-budgets]] · [[chain-rule]] · [[tree-search-methods]] · [[compound-ai-systems]] · [[clarification-request]]

[^s1]: press-2022
[^s2]: yao-2022
[^s3]: zhou-2022
