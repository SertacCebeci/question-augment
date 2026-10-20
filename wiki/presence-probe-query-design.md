---
description: "A query built to detect whether one planted record shaped the output asks for a presence signal, not the record's content, so it can pass defences that block extraction-style injections."
aliases: ["influence-detection query", "canary query template", "membership probe design", "presence query"]
sources: ["arxiv-2512-16059"]
---
# Presence-probe query design

A question put to a model about its own context can have two goals. One is extraction: get the model to reproduce the content. The other is detection: learn whether one record influenced the output at all. The paper states the second as its own aim: "unlike content-extraction attacks, ContextLeak only seeks to" detect "the influence of a single data point on the output."[^c1][^c2] The formulation changes what counts as success. An extraction probe succeeds when the content comes back; a detection probe succeeds when the answer differs with and without one record, even if the content never surfaces.

The paper builds the probe around a target output rather than a reproduction. The canary has an input and a label, and the query asks the model to produce the label for the canary's input. Three templates are used. The input-output template relies on the observation that "LLMs memorize input-output mappings" seen in context.[^c3] The if-then template asks the model "to ask if the LLM has seen the exact canary sequence in context" and then to emit one of two strings.[^c4] A third variant hides the canary's wording and asks for "an incongruous string," for the case where "the attacker aims to extract sensitive information but lacks" knowledge of the data's structure.[^c5]

The choice of target output is part of the formulation. The canary's label is picked to be one the model is unlikely to produce unprompted, "the label that the model has a lesser tendency to output by default."[^c6] A rare target turns a presence check into a measurable event: if the model emits it, the record was probably there. (my inference on why this helps; the paper gives the choice, not a test of alternatives)

The template itself is treated as the thing to optimise. The paper says it treats "the auditing accuracy" as an objective "over a class of query templates," and searches that class with a prompt optimiser.[^c7] The search gave only a small gain over the hand-written templates, which the paper reads as evidence that "the original templates have already been well-optimized."[^c8] So in this setting most of the formulation work is done by picking the right family of probe, not by tuning its wording.

## Limits

- The probe measures influence, not content. It tells an asker that a record mattered, not what the record says. Whether the same probes recover content is not tested in this text; the paper only sets the two aims apart.
- The best template depends on the model. Across models the if-then-explicit and input-output templates "perform consistently well, except for Llama," and the ranking came from one dataset, SubJ classification, "over 100 trials for each attack."[^c9][^c10] Open-ended generation was handled with one recommended pairing, and the paper's own advice for a new task is to start there and optimise.[^c11]
- The paper's claim that these probes get past heuristic defences is the paper's, measured against the defences it chose to build. A monitor that watches for odd target outputs was not among them; whether such a monitor would flag rare-label answers is my open question, not a result here.
- Smaller models showed no gain from the if-then probe as the privacy budget rose, so a probe that works on one model may not transfer. See [[empirical-privacy-auditing]] for that result.

## Related

- [[empirical-privacy-auditing]] — the audit that scores these probes; the probe's accuracy is the audit's input.
- [[llm-red-teaming]] — also a search for inputs that make a model misbehave; the probe's target is a presence signal rather than a failure.
- [[exploitable-information-leakage]] — a leakage score built on reconstruction of content, the contrast case to influence-based detection.

[^c1]: arxiv-2512-16059 — "unlike content-extraction attacks, ContextLeak only seeks to"
[^c2]: arxiv-2512-16059 — "detect the influence of a single data point on the output"
[^c3]: arxiv-2512-16059 — "LLMs memorize input-output mappings"
[^c4]: arxiv-2512-16059 — "ask if the LLM has seen the exact canary sequence in context"
[^c5]: arxiv-2512-16059 — "the attacker aims to extract sensitive information but lacks"
[^c6]: arxiv-2512-16059 — "or the label that the model has a lesser tendency to output by default"
[^c7]: arxiv-2512-16059 — "we treat a as an optimization objective over a class of query templates"
[^c8]: arxiv-2512-16059 — "the original templates have already been well-optimized"
[^c9]: arxiv-2512-16059 — "except for Llama"
[^c10]: arxiv-2512-16059 — "over 100 trials for each attack"
[^c11]: arxiv-2512-16059 — "For open-ended generation, we also suggest"
