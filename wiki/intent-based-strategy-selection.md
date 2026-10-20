---
description: "A fixed priority order over four detected-intent strategies, keyed to the Toulmin claim→grounds→warrant→rebuttal hierarchy, that selects which pedagogical move a Socratic tutoring agent makes next."
aliases: ["intent-based pedagogical steering", "intent-based strategy selection"]
sources: ["shi-2026-tackling"]
---
# Intent-based strategy selection

> Which axis of a student's argument to interrogate next, decided not by a
> score but by which of four possible intents was just detected and where
> the argument's weakest still-unaddressed component sits in a fixed
> priority chain.

## Definition / Mechanism

LFTutor (Shi et al. (2026)) is a four-step dialogue
tutor for teaching laypeople to recognise logical fallacies: (1) a
disagreement check against a running memory of prior claims, (2) intent
detection, (3) intent-based strategy selection, (4) verified strategy
execution. Step 2 classifies the student's last turn into one or more of
four intents: I1 requests clarification of the flaw, I2 gives a claim with
no supporting evidence, I3 gives evidence with no stated assumption linking
it to the claim, I4 is a complete but flawed argument. Step 3 — the
selection step — maps each intent to one of four strategies (Responding,
Evidence, Assumption, Refutation) and, when more than one intent fires,
breaks the tie by a fixed order that never changes with context: Responding
before Evidence before Assumption before Refutation.[^c1]

The order is not scored by an information criterion; it is stipulated to
match the logical dependency of Toulmin's argument components — a claim
must exist before its grounds can be questioned, grounds before the warrant
linking them, and the warrant before the whole argument is refuted:
"LFTutor selects strategies in the order listed above (i → iv), matching
the priority of components in the Toulmin model ... claims form an
argument's foundation (→Responding), followed by grounds (→Evidence), then
warrants (→Assumption), and finally, rebuttal to a complete argument
(→Refutation)."[^c2]

## Known as

| Field | Name there | Relation |
|---|---|---|
| NLP tutoring agents (Puech et al. 2024, cited but not read here) | intent-based pedagogical steering | close — the general technique this paper names as its source and instantiates with its own four intents and Toulmin ordering |

## Why it matters

An ablation isolates what this selection step buys over a role-playing
baseline with no such structure: "these improvements come from strategy
verification and intent-based strategy selection... Intent-based strategy
selection allows targeted execution of one strategy per turn and dynamic
strategy switch across turns, which helps with Stance Change, Strategy
Fixation, and Unexplained LF Terms."[^c3]

Under the normal-student automatic evaluation, the full framework
"outperforms BASE by up to 53% on average, and up to 85% for individual
metrics. It outperforms BASE W/PROBLEMS by 23% on average, and up to 67%
for individual metrics except Lack of Refutation." Under an
adversarial-student design built to trigger each named failure mode, it
"outperforms BASE W/PROBLEMS by up to 31% on average in all adversarial
student types."[^c4]

For stall 2, this is a case where "which axis first" is answered by a
domain-specific dependency order over a fixed, small menu of moves rather
than by re-scoring candidates at each turn — closer to [[five-whys]]'s
single-track climb than to an [[entropy]]-maximising rule.

## Transfer

| | |
|---|---|
| In its home field | Toulmin's model (informal logic/rhetoric): an argument decomposes into claim, grounds, warrant (and further backing/qualifier/rebuttal), used as a static scheme for *evaluating* a finished argument's structure. |
| Here | The same four-way decomposition is repurposed as a priority order for choosing which unaddressed component to interrogate next in a live, multi-turn dialogue. |
| What survives | The componential split and the intuition that earlier components (claim, grounds) are logically prior to later ones (warrant, rebuttal) — you cannot coherently refute an argument whose claim was never stated. |
| What does not | Any optimality argument: Toulmin's model supplies no weight or score over components, the claim-to-rebuttal order is the authors' stipulation rather than a result derived from or tested against alternative orderings, and the ablation reports the step's aggregate effect, not evidence that this order beats another. |

[^c5]

## Limits

- The 53%/23%/31% figures are aggregate automatic-evaluation gains for the
  whole LFTutor framework over baselines; the ablation names intent-based
  strategy selection as one of two drivers (with strategy verification) but
  does not report a number for selection alone, isolated from verification.
- The fixed priority order is untested against any alternative ordering or
  against a scored/adaptive selection rule (e.g. an information-gain
  criterion); "matches the priority of Toulmin's components" is the
  authors' design rationale, not a measured comparison.
- Evaluated only on logical-fallacy tutoring dialogues (Elec2Deb20 debate
  sentences) with simulated (GPT-4o) and, for one baseline, 20 human
  participants; generalisation to other tutoring domains or to
  non-dialogic asking is untested here.
- `shi-2026-tackling` is a 2026 arXiv preprint, not yet peer-reviewed at
  the time of harvest; unverified `[?]` until the verifier confirms it.

## Related

[[socratic-method]] · [[five-whys]] · [[constraint-seeking]] · [[value-of-information]]

[^c1]: shi-2026-tackling — "Step 3: Intent-based Strategy Selection. Given the detected intents, LFTutor focuses on addressing the student’s reasoning flaws by selecting an appropriate education strategy related to their intent."
[^c2]: shi-2026-tackling — "LFTutor selects strategies in the order listed above (i → iv), matching the priority of components in the Toulmin model (Hitchcock, 2017): claims form an argument’s foundation (→Responding), followed by grounds (→Evidence), then warrants (→Assumption), and finally, rebuttal to a complete argument (→Refutation)."
[^c3]: shi-2026-tackling — "To understand where these improvements come from, we ablate LFTutor’s core design choices (§ 7), which shows that they stem mostly from strategy verification and intent-based strategy selection."
[^c4]: shi-2026-tackling — "With the “normal” student design, LFTutor outperforms BASE by up to 53% on average, and up to 85% for individual metrics. It outperforms BASE W / P ROBLEMS by 23% on average, and up to 67% for individual metrics except Lack of Refutation."
[^c5]: shi-2026-tackling — "LFTutor selects strategies in the order listed above (i → iv), matching the priority of components in the Toulmin model (Hitchcock, 2017)"
