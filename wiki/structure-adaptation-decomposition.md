---
description: "In a budgeted intake benchmark, fixed clinical ordering captures most recovery gain over random asking; online adaptation captures the rest, concentrated under low-disclosure patients."
aliases: []
sources: ["arxiv-2604-22067"]
---
# Structure-adaptation decomposition

> Most of the gain from picking a good question order comes from having an
> order at all; the rest comes from changing it when the source won't talk.

## Definition / Mechanism

Gui et al. (2026) pose psychiatric intake as selecting,
each turn, one question from a fixed bank of N = 655 clinician-authored
questions to recover K = 10 binary target fields within T = 20 turns, and
compare three [[question-budgets|budgeted]] policies: uniform-random
selection, a clinically-ordered fixed form (domain priority, per-domain caps,
safety screening first), and an LLM-guided policy that samples up to 40
unanswered candidates per turn and has an LLM pick the one most likely to
recover new information, conditioned on the dialogue history and the
still-unrecovered fields.

Pooled over 300 sessions (4 synthetic patients × 5 behavioral conditions × 5
runs), the three policies decompose the recovery gain into two additive
components: "Random reaches 51.7%±19.6% mean accuracy, while form-based
reaches 84.8%±15.8% and LLM-guided reaches 95.4%±8.1%. The 33.1 percentage
point gap between random and form-based indicates that clinical structure
accounts for most of the gain, while the additional 10.6 point gap between
form-based and LLM-guided reflects the value of adapting to patient responses
in real time."[^c1]

The two components are not uniform across conditions: the adaptation term is
where the fixed form fails. "Across the first four conditions, the clinically
ordered form remains relatively close to the adaptive LLM policy. Under
Guarded + Concise, however, the LLM–form gap expands to 29 percentage points,
showing that adaptation matters most when patients do not quickly reveal
target fields." The mechanism is a difference in how the two policies
handle a non-answer: "the form strategy asks one question per topic and then
moves on, whereas the LLM policy can respond to deflections by re-asking or
switching to a better-targeted follow-up."[^c3]

A separate cut of the same transcripts localizes where each policy's
shortfall sits. Extraction precision is near-ceiling and nearly flat across
policies (98.4%–99.4%), while coverage — whether a field's value was elicited
at all — is what drives the accuracy gap: "Precision remains uniformly high
across all three strategies... Instead, the main challenge is whether the
interview strategy reaches the right topics and elicits the relevant
information within the available interaction budget." So the ordering of
questions, not the interpretation of answers, is the load-bearing part of the
task.

## Why it matters

This separates two things a designer of a budgeted-asking system usually
conflates into "the policy is smarter": having *any* principled order over a
large candidate set, versus reacting to what came back. The first is cheap
(a static priority list) and recovers most of the ceiling when the source is
forthcoming. The second is what a non-adaptive order cannot buy, and its
value concentrates exactly where a fixed one-question-per-topic pass fails —
guarded, terse, non-disclosing sources. A system tuned only to the average
case can look adaptation-free almost for free; the case for online selection
has to be made on the hard tail, not the pooled mean.

## Limits

Measured on synthetic patients (GPT-4o-simulated, from 4 authored profiles),
not real intake transcripts, so the accuracy numbers are benchmark artifacts,
not clinical-performance estimates. The question bank reflects a single
institution's workflow and only 10 binary targets, chosen because they were
tractable to grade automatically — subjective targets (affect, chief
complaint) are excluded. The same LLM family (GPT-4o) drives the patient
simulator, the selector and the post-session judge, so shared biases between
"ask," "answer" and "grade" cannot be ruled out; and the low-disclosure
advantage is unverified against a human clinician baseline, which the
benchmark does not yet include.

## Related

- [[question-budgets]] — the fixed 20-turn budget this decomposition is
  measured under.
- [[topic-coverage-tracking]] — the same coverage-vs-interpretation split,
  named as a tracking mechanism rather than measured as a policy gap.
- [[expected-information-gain]] — the criterion the LLM-guided policy
  approximates informally ("most likely to recover new information")
  without computing it.
- [[bayesian-experimental-design]] — the framework this task instantiates:
  select the next measurement under a budget to maximize recovery of
  unknown targets.
- [[clarification-timing-decay]] — a parallel account of why re-asking or
  reframing after a non-answer outperforms moving on.

[^c1]: arxiv-2604-22067 — "Random reaches 51.7%±19.6% mean accuracy, while form-based reaches 84.8%±15.8% and LLM-guided reaches 95.4%±8.1%. The 33.1 percentage point gap between random and form-based indicates that clinical structure accounts for most of the gain, while the additional 10.6 point gap between form-based and LLM-guided reflects the value of adapting to patient responses in real time."
[^c3]: arxiv-2604-22067 — "the form strategy asks one question per topic and then moves on, whereas the LLM policy can respond to deflections by re-asking or switching to a better-targeted follow-up."
