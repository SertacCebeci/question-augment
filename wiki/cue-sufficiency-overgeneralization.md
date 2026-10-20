---
description: "Vision-language models take plausible persuasive cues in an image as sufficient evidence of persuasiveness and over-predict it; framing the cues as auxiliary, not decisive, reduces the error."
aliases: ["recall-oriented bias", "persuasive-cue overgeneralization", "false positives from persuasion-relevant cues", "cue presence as verdict"]
sources: ["arxiv-2511-17036"]
---
# Cue-sufficiency overgeneralization

A binary judgment can fail in a specific way: the judge finds a cue that the target relation plausibly depends on, and reads its presence as the answer. Park and Kim test this on vision-language models (VLMs) with 562 image-message pairs from the Personalized Visual Persuasion dataset, kept where the raters agreed. These are "clearly separable persuasive (High) and nonpersuasive (Low) binary cases with almost-perfect" agreement.[^c1] On the question of whether an image persuasively supports a target message, the models do not split the cases evenly. They "tend to over-predict persuasiveness, revealing a pronounced recall-oriented" bias.[^c2] They reach near-perfect recall, and the price is inflated false positives. The name in the aliases, recall-oriented bias, is the symptom. The mechanism is the step from cue to verdict.

The false positives show where the step happens. The paper's key object cue, the presence of an object the message is about, "reliably separates human judgments yet also contributes to VLM false positives."[^c3] Among items that humans labelled Low, the models predict High when such a cue is present. The authors read this as the models mistaking the cue for proof: "these results indicate that VLMs often mistake plausible persuasive visual cues for sufficient evidence of persuasiveness, rather than evaluating whether those cues genuinely support the target message."[^c4] The cue is real and relevant, so the judge is not hallucinating it. What is missing is a criterion for when the cue should count.

The bias is not a fixed setting. Its size depends on how the cue is presented. The authors give the models VPF knowledge "as context-dependent auxiliary cues and not prescribing any fixed effect on the persuasive judgment."[^c5] Making the factors explicit in this framed way "can mitigate the recall-oriented bias by discouraging models from treating" persuasion-relevant cues as decisive.[^c6] The same cue given without framing does not help: "This indicates that direct cue specification, without contextual framing," stays insufficient, and the F1 drops in the paper's table.[^c7] The authors' reading is that "VLMs still lack a stable criterion" for when a cue should count as evidence.[^c8]

Explicit reasoning does not repair the step. Plain chain-of-thought gives mixed effects, and when the model reasons over an explicit key object cue, "the recall-oriented bias can be amplified."[^c9] Reasoning makes the cue more salient to the answer without making it conditional on the message. This is why the paper treats the problem as one of integration rather than of perception, and why the note on persuasive-integration-bottleneck is its companion.

My inference, not the paper's claim: the same shape should show up wherever a judge is asked a yes-or-no question about a relation and the cue that usually supports the relation is visible. The paper tests only visual persuasion, so the transfer is untested here.

## Limits

- The sample is the high-agreement subset. The authors say it "comprises persuasive and nonpersuasive cases that are relatively clear to viewers."[^c10] Behaviour on ambiguous pairs is not in the main analysis. The appendix reports that the pattern persists under "progressively broader agreement levels" and "diverse model scales, families, and reasoning variants."[^c11] Those checks are the paper's, and I did not read their numbers.
- "Mistake a cue for sufficient evidence" is the authors' reading of an association. Cue presence goes with false positives among Low items, and framing changes the rate. Neither isolates an internal cause. My inference: a judge that is more sensitive to cue presence would show the same pattern without any reasoning about sufficiency.
- The reasoning and injection tests focus on the key object cue: "VPF-guided interventions, focusing on key object" cues.[^c12] The other VPFs were tested only in the injection setting. Whether framing rescues every factor is not established.
- Framing reduces the bias but does not remove it. The paper reports the bias as persisting under framing in some settings and does not claim a cure. Treat the framing effect as a sensitivity, not a fix.

## Related

- [[visible-cue-judgment-bias]] — a neighbouring mechanism: a model's judgment follows what the image shows. Here the shown cue is not the problem; it is the jump from the cue to the verdict.
- persuasive-integration-bottleneck — the rationale-level account of why explicit reasoning does not stop the over-prediction.
- [[cot-hallucination-trap]] — when visual grounding is weak, reasoning follows a language prior; the explicit-cue result is a related case where reasoning amplifies the error it was meant to fix.
- [[element-level-entailment-verification]] — cites the affirmative bias of yes-or-no visual questions, the same family of error on the answer side.
- [[bias-controlled-metacognitive-sensitivity]] — yes-bias in a model's self-report, a different measurement of a related tilt toward affirmation.

[^c1]: arxiv-2511-17036 — "clearly separable persuasive (High) and nonpersuasive (Low) binary cases with almost-perfect"
[^c2]: arxiv-2511-17036 — "they tend to over-predict persuasiveness, revealing a pronounced recall-oriented"
[^c3]: arxiv-2511-17036 — "reliably separates human judgments yet also contributes to VLM false positives"
[^c4]: arxiv-2511-17036 — "these results indicate that VLMs often mistake plausible persuasive visual cues for sufficient evidence"
[^c5]: arxiv-2511-17036 — "context-dependent auxiliary cues and not prescribing any fixed effect on the persuasive judgment"
[^c6]: arxiv-2511-17036 — "can mitigate the recall-oriented bias by discouraging models from treating"
[^c7]: arxiv-2511-17036 — "This indicates that direct cue specification, without contextual framing,"
[^c8]: arxiv-2511-17036 — "VLMs still lack a stable criterion"
[^c9]: arxiv-2511-17036 — "with explicit key object cues, the recall-oriented"
[^c10]: arxiv-2511-17036 — "Hence, this subset comprises persuasive and nonpersuasive cases that are relatively clear to viewers"
[^c11]: arxiv-2511-17036 — "Across progressively broader agreement levels (with at least minimal annotator agreement) and diverse model scales,"
[^c12]: arxiv-2511-17036 — "focusing on key object"
