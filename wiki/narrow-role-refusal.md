---
description: "A role the model is not qualified for can make it refuse: an out-of-domain expert persona made Gemini 2.5 Flash decline on about 10 of 25 trials per question on GPQA Diamond."
aliases: ["role-induced refusal", "out-of-domain persona refusal", "expertise disclaimer refusal"]
sources: ["arxiv-2512-05858"]
---
# Narrow role refusal

A role instruction can change whether a model answers at all, not only how confidently it answers. In the Wharton study, the "Unrelated Expert" condition gave a model an expert persona in a field far from the question: a physics expert answering a biology item, for example. For Gemini 2.5 Flash on GPQA Diamond, the model "refuses to answer an average of 10.56 out of the 25 trials per question."[^c1] The refusals were not silent. The model typically said "that it lacks the relevant expertise," or that it "cannot, in good conscience" select an answer.[^c2]

The authors read this as the main reason the off-domain conditions depressed measured accuracy: "This refusal-driven behavior substantially depresses measured accuracy."[^c3] The same mechanism appeared in weaker form in the sibling model: "Gemini 2.0 Flash exhibits similar, but less extreme, behavior in some Physics and Chemistry conditions."[^c4] The paper calls this "a notable failure mode" of the domain-mismatched expert conditions, and it states the general lesson: "role instructions that are too narrow can cause models to under-utilize their actual knowledge."[^c5] [^c6]

The distinction matters for scoring. A refusal is a third output, not a wrong answer: it is neither right nor wrong on the item, and a benchmark that counts it as incorrect measures the role's disclaimer rather than the model's knowledge. This is the reason the rebuttal in [[expert-persona-confidence-amplification]] asks that invalid outputs be separated from wrong answers. The general notion that "I don't know" is a legitimate answer, not a weak one, is treated in [[abstention]]. The role-induced case differs in its trigger: it is caused by a stated lack of expertise in the prompt, not by what the model could determine about the question. That reading is mine, not the paper's; the paper does not separate the two causes.

## Limits

- The refusal rate is reported for one model, in one condition, on one benchmark. The Gemini 2.0 Flash behaviour is described as "less extreme," without a count in the text I read.
- The paper says refusal "substantially depresses measured accuracy," but the accuracy tables are not decomposed here into refusals and wrong answers. How much of the off-domain drop is refusal, and how much is error, is not established by what I read.
- "Under-utilize their actual knowledge" is asserted, not tested. No knowledge probe was run that would show the model could have answered correctly when it declined.
- Whether the refusal is a flaw or a calibrated response to a real mismatch is open. The authors treat it as a failure mode; the study does not test an in-domain or disclaimed alternative that would tell the two apart.
- Only Gemini models in this study showed the pattern. Other providers' models were not tested for role-induced refusal in these runs.

## Related

- [[abstention]] — "I don't know" as a deliberate output; this note is one trigger for it that is not uncertainty
- [[expert-persona-accuracy-null]] — the same off-domain conditions, where the accuracy null partly hides refusals
- [[low-knowledge-persona-accuracy-cost]] — the other way a role degrades answers, by lowering accuracy instead of withholding answers

[^c1]: arxiv-2512-05858 — "the model refuses to answer an average of 10.56 out of the 25 trials per question"
[^c2]: arxiv-2512-05858 — "typically asserting that it lacks the relevant expertise or"
[^c3]: arxiv-2512-05858 — "This refusal-driven behavior substantially depresses measured accuracy"
[^c4]: arxiv-2512-05858 — "Gemini 2.0 Flash exhibits similar, but less extreme, behavior in some Physics and"
[^c5]: arxiv-2512-05858 — "A notable failure mode emerges from the domain-mismatched expert conditions in the Gemini"
[^c6]: arxiv-2512-05858 — "role instructions that are too narrow can cause models to"
