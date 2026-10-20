---
description: "LLM code reviewers approved female-authored code 70.6% vs 62.9% despite equal correctness; gender cues in prompts left correctness unchanged but shifted code length and approval, by provider."
aliases: ["gender bias in LLM code review", "author-identity bias in LLM-as-judge", "gendered prompting effects"]
sources: ["doi-10-48550-arxiv-2603-24359"]
---
# Author-cue review bias

A cue about who wrote or prompted a piece of work (here, gender) can leave the quality of what an LLM produces untouched yet change how an LLM evaluator judges it. A pilot study, in three parts, locates the fairness risk in the evaluation step rather than in generation.[^c1]

## What was measured

**Prompts carry a faint trace.** In real-world coding prompts, women used more personal pronouns, more pragmatic markers (hedges via modal verbs) and a higher involved-informational ratio, while men were marginally more direct (p = .051); there were no differences in length, spelling or punctuation.[^c2] Predicting gender from prompt text was hard: RoBERTa reached a weighted F1 of 0.60 in cross-validation and 0.61 on the test set.[^c3] The authors suspect confounds such as experience level, so the cue is weak as a signal.

**Generation was not hurt.** In a controlled user study, unit-test pass rates and code quality (complexity, maintainability, Pylint) were similar between genders.[^c4]

**Review was biased.** When an LLM review bot judged the human-written code, female-authored submissions were approved in 70.6% of review events versus 62.9% for male-authored code (p about 0.008), at comparable correctness. The gap was modest for Anthropic and OpenAI models, larger for Deepseek, and largest, and significant, for Groq's LLaMA models.[^c5]

**Style cues shape the output, not its correctness.** In an LLM-only simulation with male-coded, female-coded, neutral and self-introduction prompts, pass rates clustered at 54-57% with no significant difference. Female-coded prompts yielded longer code with higher maintainability and slightly lower cyclomatic complexity; male-coded and neutral prompts yielded more compact code with higher Pylint scores.[^c6]

**Reviewer persona is provider-dependent.** Gendered reviewer personas (system messages) differed most for Groq and least for Anthropic, where personas responded identically. Female reviewers tended to be stricter for Groq and OpenAI. Only the male persona showed a marginal effect, approving female-coded prompts more often (p = 0.049).[^c7]

## Why it matters for asking and answering

The way a question is phrased carries identity information that can alter the length and style of the answer, and a downstream judge of the answer can then be moved by that cue without any change in correctness. Equal correctness with unequal approval means that approval is not a clean read of quality. This is my inference from the results, not a claim the study tests directly; the authors themselves note that they did not compare against human reviewers, so the gap may or may not diverge from human judgment.[^c8]

## Limits

- Small, mostly young, technically literate, self-selected sample; gender treated mainly as binary (one non-binary and one transgender participant were excluded).[^c9]
- Short programming tasks and a specific set of commercial models at one time; results may not generalize to newer models or complex projects.[^c9]
- Study 3 is LLM-only and uses stereotypically gendered prompt operationalizations; it cannot capture learning or adaptation over time.[^c9]
- Whether the approval gap is bias or alignment with human judgment is untested.
- The mechanism is not isolated: in the human study the code authors differed in more than gender, so the approval gap cannot be attributed to a gender cue in the code itself.

## Related

- [[llm-judge-biases]] — position, verbosity and self-enhancement biases; this adds an author-identity cue and shows size varies by provider
- [[demographic-conditioned-mirage]] — another case where a demographic descriptor, not evidence, steers a model's output
- [[cross-provider-judge-ensemble]] — provider-dependent bias size is the motive for mixing judges
- [[social-sycophancy]] — the answerer adapting to user cues, a neighbouring phenomenon

[^c1]: doi-10-48550-arxiv-2603-24359 — "fairness risks in LLM-assisted programming arise less from generation accuracy than from LLM evaluation"
[^c2]: doi-10-48550-arxiv-2603-24359 — "women used more personal pronouns"
[^c3]: doi-10-48550-arxiv-2603-24359 — "achieving a weighted F1 score of 0.60 during crossvalidation and 0.61 on the test set"
[^c4]: doi-10-48550-arxiv-2603-24359 — "unit-test pass rates and code quality (cyclomatic complexity, maintainability, Pylint"
[^c5]: doi-10-48550-arxiv-2603-24359 — "female-authored submissions were approved in 70.6% of"
[^c6]: doi-10-48550-arxiv-2603-24359 — "Female-coded prompts produced longer code"
[^c7]: doi-10-48550-arxiv-2603-24359 — "Female reviewers tend to be stricter than male reviewers for Groq and OpenAI."
[^c8]: doi-10-48550-arxiv-2603-24359 — "This may contextualize whether observed disparities reflect bias or alignment with human judgment."
[^c9]: doi-10-48550-arxiv-2603-24359 — "our sample sizes are relatively small and demographically limited"
