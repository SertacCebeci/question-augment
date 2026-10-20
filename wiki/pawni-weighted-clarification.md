---
description: "An eight-agent pipeline whose Architect agent orders clarification questions by the weight of matching best-practice patterns, tested in an N=4 EEG/NASA-TLX pilot."
aliases: ["PAWNI", "Prompt Architecture Wizard using Neural Intelligence"]
sources: ["sankar-2026"]
---
# PAWNI weighted clarification

> Front-load a fixed budget of clarifying questions, and spend it on the
> best-practice elements the pipeline is most confident matter, first.

## Definition / Mechanism

PAWNI (Prompt Architecture Wizard using Neural Intelligence) is an
eight-agent sequential pipeline — Sentinel, Scout, Architect, Forge, Judge,
Mirror, Scribe, Cipher — that turns an unstructured request into a
structured prompt before any answer is generated. Sentinel classifies the
task and Scout retrieves domain best-practice knowledge as weighted
"pattern points" (weight incremented whenever a newly-fetched point matches
an existing one above 0.82 cosine similarity). The Architect agent is the
questioner: it compares the cleaned request against an 18-element
completeness framework, generates roughly nine multiple-choice questions
per turn, and orders them by the weight of the best-practice pattern each
question would resolve, so elements confirmed across many prior
invocations are asked about before less-established ones.[^c1]

This is a selection rule for stall 2 that is neither information-theoretic
nor value-of-information: the ranking key is accumulated cross-session
confirmation frequency of a best-practice pattern, not an [[entropy]] or
utility computed for this instance.[^c2]

## Findings

Within-subjects pilot, N = 4, four domain-diverse complex tasks, comparing
unaided ("naive") LLM interaction against PAWNI-assisted formulation.
Prompt structural completeness (10-item blind-rated checklist) rose from a
naive mean of 42% to a PAWNI mean of 91% (Cohen's d = 9.69), and outputs
were rated higher on every one of six quality dimensions.[^c3]

On NASA-TLX, overall subjective workload fell from a group mean of 39.6 to
21.7 (45% reduction, d = 2.60) and every one of the four participants
reported lower workload with PAWNI; all five demand subscales dropped, most
on Mental Demand (47.5→27.5, d = 1.73) and Effort (45.0→26.3, d = 1.27).
Three of four participants also showed a lower EEG frontal-theta/parietal-alpha
ratio (a cognitive-load index) under PAWNI; the fourth showed an increase,
which the authors attribute to engaged processing on an unfamiliar topic
rather than burden.[^c4]

## Known as

| Field | Name there | Match |
|---|---|---|
| AI systems | PAWNI | exact |
| AI systems | Prompt Architecture Wizard using Neural Intelligence | exact — the acronym's expansion |

## Why it matters

The Architect's ordering rule is a third answer to "which axis first,"
alongside entropy drop ([[mutual-information]]) and [[expected-utility|expected utility]]
([[value-of-information]]): rank by how often a candidate element has been
confirmed as a best practice across past sessions, not by a quantity
computed fresh each time. It is a frequentist prior over which elements of
$W$ usually matter for this task type, substituting for a within-session
information computation.

## Transfer

| | |
|---|---|
| In cognitive neuroscience / ergonomics | frontal theta / parietal alpha power ratio is used as an index of working-memory load during a task |
| Here | it is read off during multi-turn clarification Q&A to compare cognitive load between an unaided and an assisted asking condition |
| What survives | the direction of the metric — lower theta/alpha reads as lower load — and its use as a second, objective channel alongside self-report |
| What does not | any population-normed threshold for what counts as "high" load; with N=4 and one participant moving the opposite direction, the paper reports the ratio as convergent evidence with NASA-TLX, not as a validated standalone measurement |

[^c5]

## Limits

- N = 4, a pilot, not a powered study; the paper itself reports Wilcoxon
  p = 0.125 as "the minimum achievable with N=4 when all pairs show the
  same direction" — the effect sizes are large but the sample cannot
  support a significance claim.
- The weighted-pattern ordering has not been compared against an
  entropy- or utility-based ordering on the same tasks; the pilot compares
  PAWNI's whole pipeline against unaided prompting, not this selection
  rule against alternative selection rules.
- Four domain-diverse tasks chosen by the authors; no claim about which
  task types the weighting transfers to.

## Related

[[mutual-information]] · [[value-of-information]] · [[multi-agent-clarification]] · [[question-budgets]] · [[expected-information-gain]]

[^c1]: sankar-2026 — "The system comprises eight sequentially orchestrated agents that transform an ambiguous, unstructured user prompt into a comprehensive structured prompt through multiple processing stages"
[^c2]: sankar-2026 — "High-weight points (confirmed across many invocations) receive a three-star confidence indicator, enabling the Architect to prioritize them in its questioning strategy."
[^c3]: sankar-2026
[^c4]: sankar-2026 — "All four participants reported lower workload with PAWNI, with the group mean decreasing from 39.6 to 21.7—a 45% reduction"
[^c5]: sankar-2026 — "To assess convergent validity between objective (EEG) and subjective (NASA-TLX) measures of cognitive load, we examined both within-participant change scores and raw value correlations."
