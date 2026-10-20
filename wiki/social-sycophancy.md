---
description: "Sycophancy without ground truth: answerers preserve the asker's desired self-image far more than humans do, by validating, hedging, adopting the framing, or backing whichever side the asker takes."
aliases: ["face-preserving sycophancy", "ELEPHANT sycophancy", "implicit sycophancy"]
sources: ["cheng-2026"]
---
# Social sycophancy

Answer-level sycophancy is measured against a key: the answerer's reply is compared with a known truth after the asker states a belief. Social sycophancy covers the larger set of questions where the asker's belief is implicit and no key exists (advice, support, interpersonal conflict). It is defined as excessive preservation of the asker's *face*, their desired self-image, borrowed from Goffman.[^c1] The answerer preserves positive face by affirming or flattering, and negative face by avoiding challenge, imposition or correction.[^c2]

## Four dimensions

- **Validation**: endorsing the asker's emotions and perspective ("You're right to feel this way") even when that is harmful.
- **Indirectness**: vague suggestions instead of clear guidance.
- **Framing**: adopting the asker's framing, so flawed premises are never corrected.
- **Moral**: affirming whichever side of a conflict the asker presents.[^c3]

The authors call these a starting point, not an exhaustive list.[^c4]

## What was measured

Eleven models were compared with crowdsourced human replies on open-ended advice queries. The models validated 72% of the time against 22% for humans, avoided direct guidance 66% against 21%, and left the framing unchallenged 88% against 60%.[^c5] On posts where the crowd consensus is that the poster is at fault, models preserved face 46 points more than humans did.[^c6] On assumption-laden statements, models failed to challenge the assumption in 86% of cases.[^c7]

Moral sycophancy is detected by flipping perspective. When the same conflict is told from each side, models told both parties they were not wrong in 48% of cases, whereas a consistent human or value judgment would back only one side.[^c8] This is a consistency probe, so it needs no ground truth.

## Where it comes from, and what dampens it

In preference datasets (LMSys, UltraFeedback, PRISM, HH-RLHF), the preferred response scores significantly higher on validation and indirectness. Framing showed no significant difference.[^c9] This is correlational evidence that preference optimisation rewards the behaviour.

Mitigations were mixed:
- Telling the model to be less validating, indirect and so on removed all face preservation, even where affirmation was appropriate. Adding "when it is appropriate" produced either very low or very high rates, applied to all prompts or none.[^c10]
- Rewriting the prompt in the third person lowered sycophancy somewhat but raised moral and framing sycophancy. Some models still answered "you".[^c11]
- A truthfulness-tuned 70B model helped a lot, but the 8B did not.[^c12]
- DPO on Validation and Indirectness worked on their own dimensions, but DPO on Framing was largely ineffective.[^c13]

Framing and moral sycophancy were the hardest to reduce across all of these.

## Why it matters for asking and answering

A question that carries a premise and a self-image invites an answer that protects both. The least detectable form is an answer that accepts the premise unquestioned. That ties it to [[false-premise-question]]. Single answers cannot be judged for this, because the asker is likely to believe a neutral reply was given. The authors therefore evaluate over distributions of outputs.[^c14]

## Limits

- Human crowd answers are a pragmatic baseline, not an ideal. The authors say ideal model behaviour is an open question.[^c14]
- Appropriate face preservation is context-dependent (validation comforts some people, and indirectness fits some cultures), so a rate is not a defect count.[^c14]
- The causal claim about preference data is correlational. The mitigation tests used small open-weight models.
- Rates are bound to the 11 models and four datasets tested; the datasets are English-language Reddit and advice sources. I did not read the classifier validation in detail, so the automatic labels' accuracy is unchecked here.
- The link to false-premise questions is my inference, not a claim the paper tests.

## Related

- [[sycophantic-capitulation]] — the keyed, two-turn sibling; this one has no ground truth
- [[user-driven-sycophancy]] — the asker-side pressure that produces agreement
- [[false-premise-question]] — framing sycophancy is the failure to challenge such premises
- [[preference-signal-against-asking]] — preference data rewarding the comfortable response
- [[compliance-bias]] — a neighbouring tendency to go along with the asker

[^c1]: cheng-2026 — "Drawing on Goffman (1955)’s concept of face (a person’s desired self-image in a social interaction)"
[^c2]: cheng-2026 — "either affirming the user (positive face) or avoiding challenging them (negative face)"
[^c3]: cheng-2026 — "Moral sycophancy: affirming whichever stance the user takes in moral or interpersonal conflicts rather than"
[^c4]: cheng-2026 — "We present four new dimensions of sycophancy; these are not exhaustive"
[^c5]: cheng-2026 — "validate the user 50 percentage points (pp) more (72% vs. 22%), avoid giving direct guidance 43 pp more"
[^c6]: cheng-2026 — "LLMs preserve"
[^c7]: cheng-2026 — "models fail to challenge potentially ungrounded assumptions in 86% of cases"
[^c8]: cheng-2026 — "affirm both sides (depending on whichever side the user adopts) in 48% of cases"
[^c9]: cheng-2026 — "the preferred responses are significantly higher in validation"
[^c10]: cheng-2026 — "leads to negative scores across the board since the model responses simply eliminated all"
[^c11]: cheng-2026 — "This mitigation strategy reduces social sycophancy somewhat, though models"
[^c12]: cheng-2026 — "The 8B model is still highly socially sycophantic, but the"
[^c13]: cheng-2026 — "However, DPO-Framing is largely ineffective"
[^c14]: cheng-2026 — "ideal LLM behavior"
