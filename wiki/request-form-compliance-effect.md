---
description: "How a harmful request is phrased (declarative, consultative or imperative) shifts how often multimodal models comply, though the direction the one paper reports is stated inconsistently."
aliases: ["inquiry type effect", "prompt style and compliance", "request tone effect on attack success"]
sources: ["arxiv-2512-06589"]
---
# Request form and compliance

A request has a grammatical and pragmatic form as well as a content. The same harmful subject can be asked as a statement of fact, as a question seeking advice, or as a direct command. The benchmark OmniSafeBench-MM treats this form as a variable in its own right. It sorts its prompts into "consultative, imperative, and declarative" inquiry types, and says each sample "is categorized by inquiry type ... reflecting real user interaction patterns with MLLMs."[^c1] Its stated reason is that earlier datasets "overlook the type of risk prompts, for example whether the attack prompt is consultative, instructive, or deceptive."[^c2]

The text prompts were produced by asking GPT-4o for risk-related prompts in each form.[^c3] The form was then used as a factor in the outcome. The main figure compares attack success rate across the three styles for each attack method, and a logistic regression is fitted with style, attack method and model type as predictors of attack success.[^c4]

The measured direction is where the paper contradicts itself. The figure caption says "Consultative prompts consistently trigger higher" attack success across several attacks.[^c5] The supplementary text says the opposite about tone: "The instructive tone produces consistently higher ASR," which it reads as the imperative style inducing more compliance.[^c6] Both cannot be the full story at once, and the parts of the text read here do not reconcile them. What survives is the narrower claim that the grammatical form of the request moves the outcome, measured across several attacks and models.

The mechanism is not established. A plausible reading is that a command and a request for advice ask the answerer for different things, so the form changes how the demand is parsed. That is my inference; the paper reports the effect and does not test why it occurs.

## Limits

- The direction is inconsistent within the paper (consultative highest in the caption, instructive highest in the appendix text). Until that is settled, the note records the effect, not a ranking of forms.
- Style is one factor among attack method, model and risk category, and the parts read do not report the regression coefficients, so the size of the style effect relative to the others is not shown here.
- The outcome is attack success, a score built on a judge's reading of the response. The same limits apply as for any composite success rate.
- The effect is shown for multimodal models with image-paired prompts. Text-only prompts and human askers are not tested in what was read.
- Whether the forms differ in content as well as in grammar was not checked in the parts read; a difference in topic would confound the comparison.

## Related

- [[monopolar-question]] — the declarative form as a question that proposes its own answer; it is the form in which a request carries its premise
- [[prompt-content-over-surface-form]] — there surface form had little effect on classification accuracy; here form moves unsafe compliance, so the two findings measure different outcomes and do not contradict each other
- [[script-level-obfuscation]] — another rewrite that keeps the intent and changes the outcome, at the level of script rather than grammar
- [[short-form-check-blindness-to-open-ended-bias]] — another case where the question format decides which defect becomes visible

[^c1]: arxiv-2512-06589 — "Each sample is categorized by inquiry type, including consultative, imperative, and declarative, reflecting"
[^c2]: arxiv-2512-06589 — "they overlook the type of risk prompts, for example whether the attack prompt is consultative, instructive,"
[^c3]: arxiv-2512-06589 — "to synthesize risk-related text prompts with consultative, imperative, and declarative"
[^c4]: arxiv-2512-06589 — "quantify the effect of style, attack method, and model type"
[^c5]: arxiv-2512-06589 — "Consultative prompts consistently trigger higher"
[^c6]: arxiv-2512-06589 — "The instructive tone produces consistently higher ASR,"
