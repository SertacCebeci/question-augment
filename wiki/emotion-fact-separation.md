---
description: "Affect in a patient narrative can carry into the medical summary; a probe scores how well LLMs separate emotional expression from clinical fact, and failures are linked to overtreatment."
aliases: ["emotion deconvolution", "fact-emotion separation", "toxic accumulation"]
sources: ["arxiv-2512-11544"]
---
# Emotion-fact separation

A clinical narrative mixes two kinds of content: objective facts (what happened, how long, what was forgotten) and subjective emotion (anxiety, fear, self-deprecation, complaint). Emotion-fact separation is the ability to pull the facts out and leave the affect behind. Shen et al. give it a probe group of its own, and they describe the capacity as "strip away subjective emotions (anxiety, fear) and extract objective medical" content.[^b1] The reason they give is that affect carried into the output costs the reader time and may distort the decision that follows.[^b2]

The probe is concrete. A complaint is written in strong, figurative emotional language, and the model is asked to separate the objective facts from the subjective emotions. The gold standard for one case lists the fact as "Recent significant short-term memory decline, evidenced by forgetting work appointments", and lists the emotions separately, as frustration, anxiety and self-deprecation.[^b3] The rubric scores "0 points (Precise separation)" for an answer that isolates the fact and summarizes the emotion without redundancy, and higher scores for incomplete extraction or for confusing the two sides.[^b4] Probes are built to "penetrate strong emotions wrapped in metaphor, irony, or cultural idioms".[^b5]

Results are reported as averages on the same inverse scale, where lower is better. Qwen "demonstrated a significant advantage in emotional immunity (average score = 0.75)".[^b6] GPT-4o and DeepSeek 3.1 showed "clear emotional sensitivity (average scores of 1.75)", "frequently mixing irrelevant emotional descriptions into the output".[^b7] So the same narrative produced clean facts from one model and an affect-laden summary from another. The paper reads model rankings as a "non-linear capability distribution", so this skill need not track general ability; whether it does is not tested here (my reading).[^b11]

The paper's claim about harm goes further than the score. Contaminated output "not only increases the clinician's cognitive load but can also lead to unnecessary medical intervention".[^b8] The authors name the mechanism "toxic accumulation" and write that failures "may also lead to unnecessary overtreatment due to emotional amplification".[^b9] That link is their reasoning, not something the probes measure: the rubric scores the content of the summary, and no treatment decision is scored.

The same affect can also work on the other side of the exchange. [[distress-conditioned-question-decline]] reports that a model's probing questions decline when the user is distressed; here the question is about what the model keeps when it answers. Emotional interference is also one of the secondary materials the paper counts toward [[information-steatosis]], so an affect-laden answer can fail as steatosis as well as on fact separation.

## Limits

- Four models and twenty probes, with text-only input: "the probes were limited to text form".[^b10] Nothing here tests emotion in speech, where tone carries affect that text does not.
- The probes are heavy on figurative emotion by design, so the average may overstate what plain patient text produces. Whether ordinary complaints cause the same contamination is not established by these probes (my inference).
- The overtreatment claim is the authors' reasoning, not a measured outcome. No clinical decision was scored, so the step from a contaminated summary to an unnecessary intervention is untested.
- The boundary between an "emotional" and a "factual" word is judged by two clinicians against a rubric. Where a feeling is also a symptom, such as weakness, a rater's call decides which side it is on.

## Related

- [[information-steatosis]] — emotional interference is one of the secondary materials that counts as steatosis; the two scores can move together but are separate rubric dimensions.
- [[distress-conditioned-question-decline]] — the same affect on the user's side changes what a model asks; this note is about what it keeps in the answer.

[^b1]: arxiv-2512-11544 — "strip away subjective emotions (anxiety, fear) and extract objective medical"
[^b2]: arxiv-2512-11544 — "it not only increases the clinician's cognitive load but can also lead to unnecessary medical intervention"
[^b3]: arxiv-2512-11544 — "Recent significant short-term memory decline, evidenced by forgetting work appointments"
[^b4]: arxiv-2512-11544 — "0 points (Precise separation)"
[^b5]: arxiv-2512-11544 — "penetrate strong emotions wrapped in metaphor, irony, or cultural idioms"
[^b6]: arxiv-2512-11544 — "Qwen demonstrated a significant advantage in emotional immunity (average score = 0.75)"
[^b7]: arxiv-2512-11544 — "frequently mixing irrelevant emotional descriptions into the output"
[^b8]: arxiv-2512-11544 — "it not only increases the clinician's cognitive load but can also lead to unnecessary medical intervention"
[^b9]: arxiv-2512-11544 — "may also lead to unnecessary overtreatment due to emotional amplification"
[^b10]: arxiv-2512-11544 — "the probes were limited to text form"
[^b11]: arxiv-2512-11544 — "non-linear capability distribution"
