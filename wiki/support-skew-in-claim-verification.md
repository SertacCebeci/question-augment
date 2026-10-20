---
description: "Verifiers asked whether a figure supports a claim lean toward supported: they catch only the obviously wrong claims, so a single balanced score hides which way they fail."
aliases: ["supported-label bias", "support bias in claim verification", "affirmation skew in verifiers"]
sources: ["doi-10-48550-arxiv-2506-04585", "arxiv-2511-23101", "arxiv-2511-22929", "arxiv-2511-22275"]
---
# Support skew in claim verification

A claim verifier has three possible answers: supported, neutral, contradicted. On a balanced set, an aggregate F1 hides the direction in which the verifier errs. The MuSciClaims results show one direction clearly. The paper says that "models have a strong bias towards recognizing most of the claims as supported."[^s1] It ties the bias to the subtle cases: the models are "biased towards judging claims as supported, likely misunderstanding nuanced perturbations."[^s2]

The per-class pattern is a split. On the supported class, models "attain high recall and low precision."[^s3] On the other two classes the pattern reverses: "models have low recall and high precision."[^s4] Read together, a verifier of this kind rarely withholds the supported label, and when it does reject a claim, the rejection is often right. The paper's own gloss is that "models only identify the most obviously wrong claims" as neutral or contradicted.[^s5] A contradiction is caught when the perturbation is blatant and passes as supported when it is subtle, which is the case the benchmark was built to test.

Reasoning before judging does not remove the skew. The paper finds that "Reasoning before judging helps models slightly"[^s6], and that "the gains are rather small."[^s7] The lean is a standing default of the verdict, not a result of skipping the reasoning step.

A lean of the same direction shows up in a different task. In zero-shot prediction of binary Big Five trait presence from text, a prompt enriched with trait descriptions was found to move the verdicts toward presence: "Complex prompts systematically increase recall for the positive class, biasing predictions toward trait presence."[^s10] The paper reports this as a shift in class balance under a changed prompt, not as a verifier's default, and it does not test a cause. The lean is a property of the prompt as much as of the model here, which the verifier case does not show. See [[class-wise-recall-diagnostic]] for the per-class reading that exposes it.

The construction of the classes matters for reading the skew. The neutral class is made by pairing "each claim with an unassociated figure from the same paper."[^s8] A neutral claim can be rejected by topical mismatch alone, so low recall on that class is a strong sign that the verifier does not read the figure at the level of the claim. This is my reading, not the paper's claim.

The same affirmative default appears when a vision-language model is asked presence questions about artworks. Asked whether an artwork involves an emotion, or uses a symbol to show one, the models "answer almost always affirmatively, even" when the answer is wrong.[^s11] The authors place this with the confirmation or position bias known from LLMs, which they say the VLMs "consistently exhibit", and they say it applies most to the presence questions.[^s12][^s13] The affirmation then widens the terms: "they are forced to interpret the terms" emotion and symbol very broadly, so an affirmed presence is filled with whatever reading the model can supply.[^s14] This is the authors' account of a yes-default on yes/no probes. The sections read do not separate the affirmation from the widening by intervention, and the paper does not score the default against labels. The two cases share a direction, not a task: a verdict of supported in one, a presence of an emotion in the other.

A yes-default also appears on a keyed, binary judgement item in a conversational benchmark. RecToM asks whether a dialogue strategy will be effective, and the paper reports that its models "perform below random guess, indicating a systematic distortion driven by preference-conforming bias."[^s15] The yes rate is the sharper measure: the paper reads the models as showing "a strong default toward affirmative responses regardless of ground truth", with a prediction rate of "yes" near 93%.[^s16] The item has an answer key, so the default can be scored, which the open-ended sycophancy measures elsewhere in this wiki cannot. The mechanism is not tested; the paper's explanation is the preference-conforming bias quoted above.

## Limits

- The bias is the authors' reading of score patterns. The "likely misunderstanding nuanced perturbations" explanation is a hypothesis; no experiment in the text I read separates it from other causes.
- The classes are balanced by construction (505 supported, 505 contradicted, 505 neutral). Real claim streams are not balanced, and the skew's effect on a field with a different base rate of supported claims is not measured here.
- The paper suggests that analysing confidence may show more than the verdict: "may provide more insight."[^s9] It does not run that analysis, so the skew is measured as a verdict pattern only.
- I read the summary text and the reported patterns, not every row of the per-class table. The statement covers the models the paper reports as showing the pattern and the default prompt; it is not a claim about every row.
- The RecToM yes-rate is one benchmark's judgement items, where the strategy under judgement is assigned at random: the paper says "a strategy is randomly specified".[^s17] Whether the yes-default is a model property or partly a property of how such items are built is not separated here.

## Related

- [[llm-judge-biases]] — position and verbosity biases in judges; an order effect, where this is a prior over the label.
- [[default-tone-skew]] — a standing lean in replies under a neutral instruction; the same kind of default, here on a verdict label.
- [[challenge-type-dissociation-in-capitulation]] — models give up answers under explicit challenge; the support lean is present before any challenge.
- [[text-prior-over-visual-evidence]] — a fluent text prior can displace the figure; a support default may be one such prior, which this paper does not test.
- [[cross-modal-aggregation-gap]] — the same benchmark's finding that a joint answer does not beat one channel; a second way the figure is under-used.
- [[class-wise-recall-diagnostic]] — why a balanced aggregate score hides a directional lean; the per-class reading this note relies on.
- [[conventional-symbol-versus-expressive-feature]] — the affirmative default on symbol presence questions, where the widened term is "symbol".
- [[concrete-cue-grounding]] — the same kind of default is weakest where the image gives concrete cues to answer from.

[^s1]: doi-10-48550-arxiv-2506-04585 — "models have a strong bias towards recognizing most of the claims as supported"
[^s2]: doi-10-48550-arxiv-2506-04585 — "biased towards judging claims as supported, likely misunderstanding nuanced perturbations"
[^s3]: doi-10-48550-arxiv-2506-04585 — "Models attain high recall and low precision on"
[^s4]: doi-10-48550-arxiv-2506-04585 — "models have low recall and high precision"
[^s5]: doi-10-48550-arxiv-2506-04585 — "models only identify the most obviously wrong claims"
[^s6]: doi-10-48550-arxiv-2506-04585 — "Reasoning before judging helps models slightly"
[^s7]: doi-10-48550-arxiv-2506-04585 — "the gains are rather small"
[^s8]: doi-10-48550-arxiv-2506-04585 — "we pair each claim with an unassociated figure from the same paper"
[^s9]: doi-10-48550-arxiv-2506-04585 — "may provide more insight"
[^s10]: arxiv-2511-23101 — "Complex prompts systematically increase recall for the positive class, biasing predictions toward trait presence."
[^s11]: arxiv-2511-22929 — "answer almost always affirmatively, even"
[^s12]: arxiv-2511-22929 — "Like LLMs, the VLMs consistently exhibit"
[^s13]: arxiv-2511-22929 — "This applies in particular to Qs 3 and 7"
[^s14]: arxiv-2511-22929 — "they are forced to interpret the terms"
[^s15]: arxiv-2511-22275 — "perform below random guess, indicating a systematic distortion driven by preference-conforming bias"
[^s16]: arxiv-2511-22275 — "indicating a strong default toward affirmative responses regardless of ground truth"
[^s17]: arxiv-2511-22275 — "a strategy is randomly specified"
