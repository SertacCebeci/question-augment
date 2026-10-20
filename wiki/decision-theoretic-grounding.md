---
description: "The answerer does not hold one confidence in \"understanding\". It holds a **Paek & Horvitz (UAI 2000)** build the Quartet architecture on four levels of analysis taken from Clark (1996): Two modules…"
aliases: ["decision-theoretic grounding"]
sources: ["paek-2000"]
---
# Decision-theoretic grounding

> The answerer does not hold one confidence in "understanding". It holds a
> probability distribution over *which level of understanding failed*, and
> picks its repair by [[expected-utility|expected utility]] over that distribution.

## Definition / Mechanism

**Paek & Horvitz (UAI 2000)** build the Quartet architecture on four levels of[^s1]
analysis taken from Clark (1996):

| Level | The speaker $S$ | The listener $L$ |
|---|---|---|
| channel | executes a behaviour $\beta$ | attends to $\beta$ |
| signal | presents $\beta$ as a signal $\sigma$ | identifies $\sigma$ |
| intention | signals a proposition $p$ | recognises $p$ |
| conversation | proposes a joint activity $\alpha$ | considers and takes it up |

Two modules carry the levels — a *Maintenance Module* (channel, signal) and an
*Intention Module* — and a *Conversation Control* sits over both. Each is a
temporal Bayesian network over variables the system cannot observe. In the
Maintenance Module a "Maintenance Status" node fuses channel fidelity, signal
identification and its own previous time slice; in the Conversation Control a
"Grounding Status" node produces a distribution over five states: OKAY,
CHANNEL FAILURE, SIGNAL FAILURE, INTENTION FAILURE, CONVERSATION FAILURE.

**The output is a diagnosis, not a score.** The system then takes the action of
highest expected utility given the distributions over Grounding Status and
Activity Goal. The action space is a decomposed set of grounding strategies:
no repair (do the conditionally relevant action, assume the speech was
overheard and ignore it, wait for more information, acknowledge); display
confusion to elicit user-initiated repair; confirm understanding or seek
clarification — *in a general way, or naming the level that failed*; declare
the intention before acting; or a combination of repairs. Utilities are
elicited from users rather than assumed.

**Two refinements matter.** [[value-of-information|Value-of-information]] analysis chooses which
further evidence to observe before repairing — exact VOI would require every
observation sequence, so greedy VOI is used. And the Conversation Control
monitors its own modules: if the Intention Module keeps reporting high
confidence in the user's goal while the Maintenance Module reports concern and
the user keeps correcting the system, it lowers its estimate of that module's
[[calibration|reliability]] and the utility of assuming a goal.

## Known as

The mechanism has one name. The rows below record names that travel *with* it
in the literature and are **not** alternate labels for it — they are its parts,
its host system, or the process it models; none of them belongs in `aliases`.

| Name | Field | Relation |
|---|---|---|
| decision-theoretic grounding | dialogue systems, HCI | exact — this concept |
| Grounding Status | dialogue systems | *not* this concept — one node inside the mechanism, a five-state distribution; the mechanism is that distribution *plus* the expected-utility choice over repairs |
| Quartet architecture | dialogue systems | *not* this concept — Paek & Horvitz's implementing system, a proper superset: it also contains parser, ASR and vision components that are not part of the decision rule |
| grounding | psycholinguistics (Clark & Schaefer 1987) | *not* this concept — the interactional process being modelled, not a decision rule |
| grounding criterion | dialogue systems | *not* this concept — Paek & Horvitz's separate definition of when mutual understanding is *sufficient* |

## Why it matters

1. **It supplies the combination rule [[clarification-request]] names as open.**
   Schlangen (2004) asks for a confidence at every guessed stage and combines
   them "in some principled way (for example a weighted average)". Four years
   earlier this line combines them as a Bayesian network whose output is a
   distribution over *which* level failed — not a scalar, so nothing has to be
   averaged.
2. **The thresholds dissolve.** There are no cut points between reject,
   confirm and accept: there is an argmax of expected utility over a repair
   action set. Where a threshold would sit is then a consequence of the
   utilities, and the utilities are elicited, not derived.
3. **The repair can name its own level.** Because the diagnosis is
   level-indexed, "I'm not sure that I heard you correctly; did you want a
   shuttle?" is available as a distinct action from a general clarification —
   this is what makes a typed clarification request computable rather than
   merely classifiable after the fact.
4. **Confidence about confidence.** The meta-level readjustment gives an
   answerer a way to detect that one of its own stage confidences is
   systematically wrong, without ground truth on the individual turn.

## Transfer

| | |
|---|---|
| **Home field** | multimodal spoken dialogue: co-present user, ASR with a large trigram model, a syntactic parser, a face-pose tracker, a system that must act continuously |
| **Here** | any answerer holding one received question and choosing among answer, answer-and-check, typed ask-back, and wait |
| **What survives** | diagnosing comprehension as a distribution over failure levels rather than one confidence; selecting the repair by expected utility instead of thresholding; using VOI to decide what to observe before repairing; recalibrating a stage whose confidence keeps disagreeing with outcomes |
| **What does not** | the channel and signal levels, which have no analogue for a text-only answerer — the four-level net degenerates to the two that carry propositional content; the hand-crafted network structure, which is domain-specific; the elicited utilities, which are task- and user-specific and have no task-agnostic form |

## Limits

- The pairing of this architecture with the hole Schlangen leaves is **this
  wiki's**: Paek & Horvitz predate him and do not address a combination rule
  for stage confidences; Schlangen does not cite this solution.
- The networks were **initially hand-crafted** from variables the authors
  judged significant, with learning of parameters and structure from user data
  described as ongoing. The level diagnosis is only as good as those priors.
- The paper's evidence is illustrative runtime traces from two prototypes
  (Presenter, the Bayesian Receptionist). It reports no accuracy for the level
  diagnosis and no comparison against a thresholding baseline, so point 2 is a
  claim about the form of the decision, not about its performance.
- The mechanism requires a utility function. The paper cites companion work
  for eliciting it rather than supplying one, so an answerer that cannot price
  a misunderstanding cannot run this.
- Intention-level evidence in the demonstrations comes from a syntactic parse
  and logical form over recognised speech; that confidence therefore inherits
  parser error, and no separate confidence for the conversation level is
  reported.

## Related

[[clarification-request]] · [[value-of-information]] · [[expected-utility]] · [[uncertainty-decomposition]] · [[abstention]]

[^s1]: paek-2000
