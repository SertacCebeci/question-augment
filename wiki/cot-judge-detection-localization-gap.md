---
description: "LLM judges flag that a reasoning chain has a broken step far more often than they name which step; the raw detection rate overstates ability because false positives on clean chains are high."
aliases: ["detection-attribution gap in process judging", "causal step localization gap"]
sources: ["arxiv-2603-05167"]
---
# CoT judge detection-localization gap

In C2-Faith, one step in the middle of a human-verified chain (PRM800K) is replaced by an LLM-written, logically inconsistent rewrite, so the error position is known. Three judges (GPT-4.1, DeepSeek-V3.1, o4-mini) are then asked whether an error exists and, in a second task, which step it is.

## What was measured

Detection is much easier than attribution. Detection rates were 89.3%, 88.4% and 94.2%, but exact-match step localization was 57.6%, 55.8% and 68.0%: gaps of 31.7, 32.6 and 26.2 points.[^c1] The authors summarize that "pinpointing the wrong step is far harder than just noticing that something is wrong."[^c2]

Raw detection is also inflated by false alarms. On the unperturbed full chains, the localization prompt flagged an error in 54.9% (GPT-4.1), 49.3% (DeepSeek-V3.1) and 40.4% (o4-mini) of perfect chains.[^c3] In the binary task DeepSeek-V3.1 had the highest detection (94.7%) but flagged 29.6% of correct chains, nearly three times GPT-4.1 (11.4%) and o4-mini (10.4%). Net discrimination (detect minus false-positive rate) reversed the ranking: o4-mini 81.6%, DeepSeek last at 65.1%.[^c4]

Rankings flip across tasks: binary detection DS > o4 > GPT, localization o4 > GPT > DS. DeepSeek was most accurate when it did detect an error (detected-only MAE 1.45) but least often exact.[^c5] So "which judge is best" has no task-free answer.

## Why it matters for asking and answering

A judge that says "something is wrong" gives a signal that cannot be acted on without a location, and its yes-rate alone says little about discrimination. My inference: any evaluation of an answerer's reasoning should report the false-alarm rate on clean items and the localization accuracy, not detection alone.

## Limits

- Only math chains from one dataset, only single-step injections placed in the middle 30-90% of the chain, only three judges.
- Errors are LLM-generated negations, which may differ in kind from naturally occurring errors.
- The mechanism for the gap is not isolated; the authors' account (local entailment versus global attribution) is interpretive.
- Whether prompt design, not capability, drives the high false-positive rate in the localization task was not separated.

## Related

- [[ambiguity-detection-localization-gap]] — the same detect-but-cannot-locate shape, for ambiguity in questions
- [[judge-master-key-false-positives]] — another case where a judge's yes-rate misleads
- [[hint-adherence-without-acknowledgement]] — unfaithful reasoning that such judges are meant to catch

[^c1]: arxiv-2603-05167 — "GPT-4.1 (89.3% vs. 57.6%, gap = 31.7 pp),"
[^c2]: arxiv-2603-05167 — "pinpointing the wrong step is far harder than just noticing that something is wrong."
[^c3]: arxiv-2603-05167 — "GPT-4.1 flags 54.9%, DeepSeek-V3.1 flags 49.3%, and o4-mini"
[^c4]: arxiv-2603-05167 — "also flags 29.6% of correct steps as unfaithful,"
[^c5]: arxiv-2603-05167 — "Model rankings flip from Exp 1 to Exp 2."
