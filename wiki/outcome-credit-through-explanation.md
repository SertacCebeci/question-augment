---
description: "Routing a decision-label reward through a reasoning, explanation, then prediction trajectory credits the explanation without gold explanations, only through the decision it helps produce."
aliases: ["trajectory-level outcome reward", "explanation credit via final-label reward", "reasoning-explanation-prediction credit"]
sources: ["arxiv-2601-04208"]
---
# Outcome credit through explanation

In a model that writes a reasoning trace, then an explanation, then a prediction, a reward on the prediction can be made to reach the explanation. LEXMA arranges this on purpose. The design applies "rewards for correct decisions" to the whole trajectory, so the explanation is part of what gets reinforced.[^c1] The authors expect this to "encourage explanations that highlight case factors associated with accurate predictions and improves predictive performance."[^c2] The explanation has no target of its own. It is shaped only through the label that is conditioned on it.

The mechanism is a placement, not an added term. The explanation sits between the reasoning and the prediction, so the gradient from the prediction passes back through it. The paper gives the reason as "since correctness depends on how reasoning and explanation shape the final label."[^c3] The training uses group sampling: several complete trajectories are drawn per case, each is scored 1 if its predicted label is correct, and the scores are compared within the group. An explanation that tends to co-occur with correct labels is reinforced, and one that co-occurs with wrong labels is not. That is a claim about what the update does, which is my reading of the setup, not a measured effect.

The design also states an ordering of objectives. The paper says that "a necessary condition for this objective is that the underlying decision is correct."[^c4] Explanation quality is thus a second goal that sits on top of decision correctness, and it is not allowed to replace it.

The contrast is with a process reward that scores the explanation directly. [[rationale-aware-reward]] adds a term that checks the reasoning against a gold reference span, so it needs a reference for each training item. The trajectory route needs only decision labels. The paper's reward for these runs "depend only on" ground-truth decisions and rule-based metrics.[^c5] What is traded is a direct check on the explanation for a signal that is cheaper to obtain.

The motivation is the failure this placement is meant to address. An LLM that predicts and then narrates its prediction "can produce fluent but unfaithful" rationales.[^c6] Putting the explanation before the prediction makes it an input to the label in the training design. Whether it is a causal input at inference is a different question, and the text I read does not test it.

## Limits

- The explanation is not scored for faithfulness. The support for "explanations that highlight case factors" comes from loan professionals' ratings of risk relevance, decision appropriateness and explainability, not from a check that the explanation names the features the model used (my reading).
- Credit flows only through the label. An explanation that is wrong but co-occurs with a correct label is reinforced the same way as a sound one, and the design cannot tell them apart (my inference).
- No comparison with a separate explanation objective is in the text I read. So whether trajectory credit does better than a direct explanation reward, or the reverse, is not shown.
- The task is binary (approve or deny) on one dataset with one model. With more labels or softer outcomes, the group comparison may carry less signal (my inference).
- Whether the prediction depends causally on the explanation at inference was not measured, so "the explanation drives the decision" is a training-time story here.

## Related

- [[rationale-aware-reward]] — a process reward on the reasoning that needs a gold reference span; the contrast with this route
- [[group-relative-advantage]] — the group baseline that compares the sampled trajectories
- [[verbalization-incompleteness-versus-unfaithfulness]] — what a verbalized reason can and cannot show about the computation behind a decision
- [[decision-fixed-audience-adaptation]] — the audience split that a trajectory-trained explanation is then adapted to
- [[rule-based-style-reward]] — the style-side reward that runs alongside this decision-side one

[^c1]: arxiv-2601-04208 — "rewards for correct decisions are applied to the entire"
[^c2]: arxiv-2601-04208 — "case factors associated with accurate predictions and improves predictive performance"
[^c3]: arxiv-2601-04208 — "on how reasoning and explanation shape the final label"
[^c4]: arxiv-2601-04208 — "A necessary condition for this objective is that the underlying decision is correct."
[^c5]: arxiv-2601-04208 — "rewards that depend only on"
[^c6]: arxiv-2601-04208 — "can produce fluent but unfaithful"
