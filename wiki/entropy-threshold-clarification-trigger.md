---
description: "Ask a clarification question whenever predictive entropy over an attribute crosses a fixed threshold, targeting the highest-entropy item; this beats imitating human ask-timing on task success."
aliases: []
sources: ["testoni-2024"]
---
# Entropy-threshold clarification trigger

QDrawer, a Drawer agent for the CoDraw task, decides whether to ask a
clarification question by comparing its own predictive [[entropy]] against a
fixed threshold: if the entropy over the size attribute labels (small,
medium, or large) exceeds a given threshold, QDrawer generates a
clarification question targeting a maximum number of 2 cliparts (i.e., the
ones with the highest entropy). The threshold both selects *which* item to
ask about (the highest-entropy clipart) and *whether* to ask at all —
lowering it raises the number of questions per dialogue (Table 2: 57.1% of
dialogues get at least one question at θ=1.1, versus 96.6% at θ=0.3).[^c1]

Compared against a baseline "Decider" module trained on the turns at which
*human* Drawer players asked (a supervised imitation of human ask-timing,
reaching only 0.35 Average Precision at predicting those turns — see
[[human-model-uncertainty-dissociation]]) and against asking at random or
human-matched turns, the entropy-threshold trigger wins on task success:
the uncertainty-driven QDrawer outperforms the baselines to a large
extent: up to 87.3% size accuracy and 3.40 similarity score.[^c2]

Asking also measurably improves the [[calibration]] of the model's own
uncertainty (Expected Calibration Error 0.10 to 0.05, Brier score 0.36 to
0.28, Silent Drawer versus QDrawer at θ=0.3).

## Transfer

| | |
|---|---|
| Home field | Information theory — entropy as an uncertainty measure over a discrete distribution |
| Here | A per-turn scalar trigger for a dialogue agent's clarification decision: ask when entropy over an attribute's label distribution exceeds a fixed threshold, targeting the highest-entropy item |
| What survives | The monotonic relationship the paper exploits operationally: lowering the threshold strictly increases both the number of questions asked and downstream task accuracy (Table 1-2) |
| What does not | Any claim that the entropy threshold tracks a *human* asking policy — [[human-model-uncertainty-dissociation]] shows the same entropy signal predicts human ask-timing only weakly (AP 0.188), so the trigger's success is a task-success argument, not evidence it reproduces human question timing |

## Limits

Demonstrated only for one attribute (size) with a template-based question
generator that guarantees a correct answer; the paper's own extension to
orientation is noted but only sketched (footnote 8: adding orientation
raises similarity score to 3.46). The threshold is hand-set per experiment,
not learned or tied to a decision-theoretic [[value-of-information|value of information]]; no
comparison is offered against an EIG- or VoI-based trigger.

## Related

[[human-model-uncertainty-dissociation]], [[expected-information-gain]],
[[value-of-information]], [[semantic-entropy]]

[^c1]: testoni-2024
[^c2]: testoni-2024 — "the uncertainty-driven QDrawer outperforms the baselines to a large extent: up to 87.3% size accuracy and 3.40 similarity score."
