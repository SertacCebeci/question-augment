---
description: "An interview agent selects its next elicitation question by scoring and re-ranking domain-ontology slots against dialogue context, then prunes branches the stakeholder has closed off."
aliases: ["OntoAgent", "ontology-guided interview", "ScoreOnto", "ReRankOnto", "GatePrune"]
sources: ["jin-2026-chat"]
---
# Ontology-guided elicitation agent

> A method for choosing which requirement to ask about next: score every
> unexplored node of a domain ontology against the dialogue so far, re-rank
> after every turn, and prune the branches the stakeholder has closed off.

## Definition / Mechanism

OntoAgent runs a multi-turn interview against a pre-built **experience
ontology** — a three-level tree of aspects, dimensions and slots (see
[[requirements-experience-ontology]]) — using four operations at each turn:
**ParseUser** interprets the stakeholder's last answer as an aspect- or
dimension-level confirmation/rejection; **ScoreOnto** assigns each ontology
node an initial priority from its semantic relevance to the stakeholder's
opening description, before any dialogue feedback exists; **ReRankOnto**
re-scores the remaining candidate slots after every turn against the
updated dialogue history, so the priority order tracks what has just been
learned rather than staying fixed; **GatePrune** removes a whole aspect
branch once N consecutive questions under it produce no new requirement,
and removes a single dimension's slots the instant the stakeholder rejects
that dimension outright. The highest-priority surviving slot is then
combined with the dialogue history to generate the next question
(`QuestionGen`). Selection is a fixed-tree scored traversal, not a fixed
question order or a one-shot free-form LLM chat.[^c1]

On 101 web-application requirements scenarios (ReqElicitGym), OntoAgent
reached an Implicit Requirement Elicitation ratio (IRE) of 0.69 against a
0.52 best baseline (+33% relative) and a [[turn-discounted-key-question-rate|Turn-discounted Key Question Rate]]
(TKQR) of 0.59 against a 0.49 best baseline (+21% relative); an ablation
that adds the ontology, then ScoreOnto, then ReRankOnto, then GatePrune to
a bare LLM shows the ontology alone carrying the largest single jump (IRE
0.13 → 0.41), with ScoreOnto and ReRankOnto adding further, smaller gains
on top.[^c2]

## Why it matters

This is a concrete instance of "which axis first" (stall 2) run as a
scored-and-re-ranked traversal of a pre-declared structure rather than a
recomputed information-theoretic criterion at every step: the ontology
substitutes for an explicit value function, and GatePrune substitutes for a
stopping rule (stall 7) triggered by a run of uninformative answers rather
than a posterior threshold.

## Limits

The ablation isolates each component's contribution only on this one
domain (web-application requirements) and one ontology; the paper reports
no comparison against an explicit information-theoretic scoring rule (e.g.
[[expected-information-gain]]) on the same task, so whether ScoreOnto/
ReRankOnto's ranking approximates an [[entropy]]-drop criterion or departs from
it is not established here — only that adding them beats not adding them.
GatePrune's pruning threshold N is a tuned hyperparameter, not a derived
stopping bound. [?] no independent replication found.[^c3]

## Related

[[requirements-experience-ontology]] · [[expected-information-gain]] · [[optimal-decision-tree]] · Selection

[^c1]: jin-2026-chat
[^c2]: jin-2026-chat — "OntoAgent achieves an IRE of 0.69, outperforming all baselines. The strongest baseline (i.e., Mistake-guided Prompting) reaches 0.52. Compared with it, OntoAgent gain a relative improvement by 33%"
[^c3]: jin-2026-chat — "Aspect-level GatePrune is triggered when no new requirements are elicited after N consecutive inquiries under the same aspect."
