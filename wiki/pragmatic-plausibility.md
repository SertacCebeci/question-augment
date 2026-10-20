---
description: "Confidence at the pragmatic level is measurable without a pragmatic **Gabsdil & Lemon (ACL 2004)** classify each of the 10-best recognition hypotheses for a user utterance as accept / clarify / rej…"
aliases: ["pragmatic plausibility features", "dialogue-context confidence features", "DIAL features"]
sources: ["gabsdil-2004"]
---
# Pragmatic plausibility

> Confidence at the pragmatic level is measurable without a pragmatic
> probability: count the referring expressions the answerer could not resolve
> and the task conflicts the reading implies, and feed those counts to the
> accept / clarify / reject decision.

## Definition / Mechanism

**Gabsdil & Lemon (ACL 2004)** classify each of the 10-best recognition[^s1]
hypotheses for a user utterance as accept / clarify / reject / ignore, then
pick one action for the whole utterance under the fixed preference ordering
**accept > clarify > reject > ignore**. Each hypothesis is a 20-dimensional
feature vector in four groups:

| Group | Features | What it measures |
|---|---|---|
| Recognition — REC (6) | nbestRank, hypothesisLength, confidence, confidenceZScore, confidence-StandardDeviation, minWordConfidence | the recogniser's own score |
| Utterance — UTT (3) | minAmp, meanAmp, RMS-amp | acoustic; included mainly to detect crosstalk |
| **Dialogue — DIAL (9)** | currentDM, currentCommand, mostActiveNode, DMBigramFrequency, qaMatch, aqMatch, **#unresolvedNPs, #unresolvedPronouns, #uniqueIndefinites** | whether the reading coheres with the discourse |
| **Task — TASK (2)** | **taskConflict, #taskConstraintConflict** | whether the reading's intention conflicts with an active task |

This note's object is the **bolded class across both groups** — the counts
that score a reading at the two stages the recogniser cannot score — not
either feature group as the paper packages it. *Reference*: how many definite
NPs and pronouns in this hypothesis cannot be resolved in the current
Information State ("the car" when no car was mentioned), and how many
indefinites have a unique referent in the domain. *Intention*: whether the
current and previous utterance form a valid question–answer pair (qaMatch,
aqMatch, in DIAL), and whether the command expressed has preconditions
conflicting with a task already active (`take_off` while altitude $\neq 0$ —
taskConflict, #taskConstraintConflict, in TASK). The paper's ablation is by
group, so the two stages are measured together with their group-mates and
never separately.

**What each group buys.** On 303 utterances from the WITAS UAV
command-and-control system (6 subjects, 30 dialogues), leave-one-out, TiMBL at
default settings, three-class accuracy / weighted f-score (Table 2): baseline
65.68 / 61.81 → REC 67.66 / 67.51 → REC+UTT 68.98 / 68.32 → REC+UTT+DIAL
77.56 / 77.59 → REC+UTT+DIAL+TASK 77.89 / 77.91. So of the **12.2 accuracy
points** the four groups add at default settings, the nine dialogue-context
features account for **8.6**, the recogniser's own six for 2.0, the three
acoustic features for 1.3, and the two task features for 0.3. Parameter
optimisation over 40 settings adds a further 8.3 points, to 86.14 / 86.39 —
what the authors report as a 25% weighted f-score improvement over the
baseline — against an oracle ceiling of 94.06 / 94.17.

**The middle region is priced.** The baseline accepted 233 utterances at
21.51% WER; the tuned classifier accepted 169 at 4.05% WER, and among them 159
correct against the baseline's 154. Accepting a quarter fewer utterances cut
the error rate of what was accepted about fivefold while raising the number of
correct accepts.

## Known as

| Name | Field | Relation |
|---|---|---|
| pragmatic plausibility, pragmatic plausibility features | spoken dialogue systems | exact — the authors' own term for the pragmatic-level evidence a reading is wrong, spanning the discourse-level and task-level counts alike |
| dialogue-context confidence features, DIAL features | spoken dialogue systems | close — the nine dialogue-context features: the larger part of this class (8.6 of the 8.9 points the two groups add together) but not the two task-level ones, which this note also counts and which the paper measures separately at 0.3 |
| task-level features, TASK features | spoken dialogue systems | close — the other part: taskConflict and #taskConstraintConflict, the intention-stage half of this class, measured apart from DIAL and adding almost nothing on this domain |
| confidence annotation | spoken dialogue systems | *not* this concept — a per-concept probability updated across turns and scored by its calibration, not a per-utterance four-way action decision |
| context-sensitive speech recognition | ASR | *not* this concept — the grammar-switching baseline this work is measured against |
| concept accuracy / semantic confidence | ASR evaluation | close — the quantity the 50% WER cut stands proxy for; the authors say they would have thresholded on it had scores been available |

## Why it matters

1. **A stage with no probability can still have a confidence.** The answerer
   needs no error model for reference resolution: the *count of what it failed
   to resolve* is a deterministic read of its own information state, and the
   group holding those counts carries about two thirds of the total gain here,
   against 1.3 points for the microphone and 2.0 for the recogniser's own
   scores.
2. **The combination rule can be learned instead of derived.** Where
   [[clarification-request]] leaves "combine in some principled way" open and
   [[decision-theoretic-grounding]] answers with a Bayesian network plus
   utilities, this answers with a supervised classifier over stage features and
   a fixed preference ordering — no calibrated probability anywhere in the loop.
3. **The three-region strategy has a measurable cost.** The accept/clarify
   boundary is not free: fewer accepts, cleaner accepts. This wiki reads that
   trade as the same shape as the coverage–risk trade in [[abstention]], made
   concrete on a comprehension decision rather than a prediction — see
   *Limits*; the correspondence is ours, not the authors'.
4. **The two stages of this class are not worth the same.** Task-level
   features added 0.3 points where discourse-level features added 8.6. On this
   domain, intention conflict was nearly redundant given reference failure —
   which is why the two halves of the class are named apart in *Known as*
   rather than treated as one label.

## Transfer

| | |
|---|---|
| **Home field** | a multimodal command-and-control spoken dialogue system with a hand-written semantic grammar, an Information State (dialogue move tree, active node list, salience list) and a 10-best recogniser |
| **Here** | any answerer scoring its own reading of one received question before committing |
| **What survives** | the *class* of feature — unresolved referring expressions and precondition conflicts as observable evidence that a reading is wrong; learning the accept/clarify/reject rule rather than deriving thresholds; the preference ordering as tie-breaker |
| **What does not** | the features themselves, computable only because the information state is a structured symbolic record; the acoustic and crosstalk groups; the n-best list, which a free-text answerer does not have unless it constructs alternative readings deliberately |

## Limits

- 303 utterances, 6 subjects, one domain, one grammar. Point 1 claims this
  feature class *was* informative here, not that unresolved-reference counts
  transfer as a confidence signal to open-domain answering.
- **The class this note names is not the unit the paper ablates.** DIAL also
  contains four discourse-state features (currentDM, currentCommand,
  mostActiveNode, DMBigramFrequency) that are not reference counts, so the 8.6
  points are an upper bound on what the reference-stage counts contributed, and
  the 0.3 for TASK is the only figure isolating the intention stage.
- **The split is learner-dependent.** With RIPPER on the same data the
  dialogue group adds only 2.3 points (72.61 → 74.92) while REC alone already
  reaches 69.31; the "almost 10%" jump is TiMBL's. The 8.6-point figure is a
  property of one learner's fit, not of the features alone, and no ablation
  isolates any single feature.
- The 86.14% figure includes parameter optimisation, which accounts for 8.3 of
  the 20.5 points separating it from the baseline; attributing that range to
  feature groups would double-count the tuning.
- **The coverage–risk correspondence in point 3 is this wiki's framing.**
  Gabsdil & Lemon compute no risk–coverage curve; the two accept/WER figures
  are two operating points. It is recorded as `equivalence.analogy`.
- **The clarify class is a proxy**, defined by a 50% word-error-rate cut
  adopted because concept-accuracy scores were unavailable — not by evidence
  that clarification would have succeeded. The authors state the system did not
  support clarification dialogue, so the four-class annotation is of
  theoretical interest; point 3's figures come from the three-class comparison,
  which does not depend on it.
- Two simplifying assumptions the authors flag as possibly too strong: an
  utterance counts as correctly recognised only if its logical form equals the
  transcription's, and an out-of-grammar utterance is assumed unhandleable.
- The outputs are decisions, not calibrated probabilities; nothing here
  licenses reading a pragmatic-plausibility score as a probability of correct
  comprehension ([[calibration]]).
- The improvement is against a grammar-switching baseline in the same system,
  not against a well-tuned fixed rejection threshold.

## Related

[[clarification-request]] · [[decision-theoretic-grounding]] · [[abstention]] · [[calibration]] · [[third-position-repair]] · [[uncertainty-decomposition]]

[^s1]: gabsdil-2004
