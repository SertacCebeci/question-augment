---
description: "A token trained into a reasoning trace and emitted at the step where the state looks unreliable gives an intervention point that one end-of-answer confidence number cannot localize."
aliases: ["<uncertain> marker", "during-reasoning self-assessment", "mid-trace uncertainty token", "reasoning-time uncertainty signal"]
sources: ["doi-10-48550-arxiv-2604-05306"]
---
# In-stream uncertainty marker

A model can be trained to emit a dedicated token inside its own reasoning, at the step where the current state appears unreliable, so the flag arrives while the trace is still open.[^c1] The point is timing. A confidence written after the answer summarizes the whole response in one number, and that number cannot say where the risk entered: "identify which step caused the risk" is the thing a scalar cannot do.[^c2] By the time the score is computed the answer is already fixed. A marker placed in the trace is a candidate control point that a downstream component can act on before the answer is committed.

The marker is shaped by reinforcement learning with a reward that ranks four outcomes: correct without a flag, correct with a flag, wrong with a flag, and wrong without a flag, in that order from highest to lowest.[^c3] By my reading of that ordering, flagging costs little when the answer is wrong and something when it is right: a flagged wrong answer scores above a silent wrong one, and a flagged correct answer scores below a silent correct one. The paper's concrete values follow that order, 5.0, 3.5, 0.0 and a negative value for silent failure, and the first three are stated in the text.[^c4]

At inference the emitted marker does not, by itself, trigger anything. Each occurrence is treated as a candidate, and "a lightweight hidden-state probe decides whether retrieval should actually be triggered."[^c5] The mechanism therefore has two parts: an emitted token in the output, and a state read from the hidden activations around its first occurrence. The probe is trained to predict final-answer wrongness.[^c6]

The reported effects are these. Emissions are spread through the response: they are "distributed across the full range of response positions, not clustered near the end."[^c7] Across six factual reasoning datasets the paper reports that the model trained this way improves macro-average answer accuracy "from 17.67% to 28.53%".[^c8] The more specific figure concerns retrieval: the pipeline gated by the marker sends wrong dev answers to retrieval, "covering 88.2% of failures, whereas the base pipeline" covers only 15.1%, by the paper's count of 128 of 848.[^c9] The authors summarize the marker as "a high-recall reasoning-time signal."[^c10]

The contrast with the end-of-answer confidence is the paper's own framing. The end-of-answer number suits trust-or-abstain decisions on the whole answer; the in-stream marker suits decisions that must be made before the answer is committed. The two are not presented as substitutes.

## Limits

- Scope. The work tests factual QA and adaptive retrieval with one marker. "We study factual QA and adaptive retrieval with a single during-reasoning marker."[^c11] Whether the same holds for coding or multi-turn agents is not tested; the paper says those settings "may require richer feedback and multiple specialized markers."[^c12]
- Recall, not precision. The headline numbers measure how many wrong answers are flagged. The cost of flagging correct answers is not the headline. The only pressure against over-flagging visible in the reward is the gap between 5.0 and 3.5 for correct answers. Whether that keeps the flag rate in check is my inference from the reward, not a result measured here.
- The probe is supporting evidence. "We keep the probe as supporting evidence rather than a separate contribution."[^c13] So the claim that the marker exposes a usable internal state rests on a secondary result.
- Timing is not isolated. The paper compares two designs, end-of-answer and in-stream, and attributes the gains to the training of each. It does not show that the mid-trace position itself, as opposed to the reward and the instruction, produces the accuracy gain. This is my reading.
- The reward and the instruction to emit the marker define what counts as a flag. Changing either changes the emission rate and position, and the text reports those effects only through its appendix ablations, not through the main claim.

## Related

- [[confidence-triggered-reflection]] — a low-confidence reading during decoding triggers a self-review; here the trigger is a token the model learns to emit, not a readout of token probabilities.
- [[log-score-verbalized-confidence-reward]] — the end-of-answer counterpart: a number after the answer, trained with a proper scoring rule.
- [[uncertainty-guided-retrieval-triggering]] — retrieval gating from the answer's likelihood, with no signal placed inside the trace.
- [[calibration]] — the property the end-of-answer number is trained toward; the in-trace marker is shaped by the reward ordering above rather than by calibration.

[^c1]: doi-10-48550-arxiv-2604-05306 — "we train the model to emit the explicit marker <uncertain> whenever it encounters such"
[^c2]: doi-10-48550-arxiv-2604-05306 — "identify which step caused the risk"
[^c3]: doi-10-48550-arxiv-2604-05306 — "r(correct, no emit) > r(correct, emit) > r(wrong, emit) > r(wrong, no emit)"
[^c4]: doi-10-48550-arxiv-2604-05306 — "with concrete values 5.0 > 3.5 > 0.0"
[^c5]: doi-10-48550-arxiv-2604-05306 — "a lightweight hidden-state probe decides whether retrieval should actually be triggered"
[^c6]: doi-10-48550-arxiv-2604-05306 — "predicts final-answer wrongness, with the strongest signal"
[^c7]: doi-10-48550-arxiv-2604-05306 — "across the full range of response positions, not clustered near the end"
[^c8]: doi-10-48550-arxiv-2604-05306 — "improves macro-average answer accuracy from 17.67% to 28.53%"
[^c9]: doi-10-48550-arxiv-2604-05306 — "covering 88.2% of failures, whereas the base pipeline"
[^c10]: doi-10-48550-arxiv-2604-05306 — "marker functions as a high-recall reasoning-time signal"
[^c11]: doi-10-48550-arxiv-2604-05306 — "We study factual QA and adaptive retrieval with a single during-reasoning marker"
[^c12]: doi-10-48550-arxiv-2604-05306 — "may require richer feedback and multiple specialized markers"
[^c13]: doi-10-48550-arxiv-2604-05306 — "We keep the probe as supporting evidence rather than a separate contribution"
