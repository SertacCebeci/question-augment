---
description: "Asked to answer as people with different demographic profiles, an LLM often gives one fixed stance on a survey item, so conditioning on the respondent does not move the answer."
aliases: ["unified viewpoint collapse", "viewpoint fixation under persona conditioning", "demographic insensitivity in LLM survey simulation"]
sources: ["arxiv-2512-06874", "arxiv-2512-11827"]
---
# Demographic-conditioning insensitivity

When a language model is told to answer a survey item as a person with a given sex, birth decade, religion and so on, the answer can stay the same whatever profile it is given. Yu, Zhou, Zhao and Wen report this on World Values Survey items: the models "tend to maintain fixed viewpoints across varying demographic features."[^c1] In their manual analysis, the claims the model generated for a question "agree with the survey question, even when prompted with varying demographic profiles," and the authors say this "occurs in 50% of the survey questions tested."[^c2][^c3]

The fixity is a property of the stance, not of noise. For a question on government video surveillance, the models "consistently produce affirmative claims across all demographic groups."[^c4] Direct prompting and chain-of-thought prompting, the two baselines, are read the same way: they "tend to reflect a unified viewpoint, even when provided with diverse demographic features."[^c5] The demographic line is in the prompt, and the answer does not follow it.

The authors attribute the fixity to alignment training, without testing that link. Reinforcement learning from human feedback "significantly helps align LLMs with widely accepted moral values," but it "also fundamentally limits their ability to simulate users whose viewpoints diverge from these norms."[^c6] The mechanism, then, is that a stance learned as the norm is reproduced for a respondent who holds another one. Their claim is that the model keeps the norm across profiles, not that it lacks the information about the profile.

This is distinct from the spread problem in [[simulated-respondent-variance-deficit]]. That note measures how much answers vary across respondents within one item. Here the question is whether the profile moves the stance at all. The two can come apart: an item can show a reasonable spread across a sample while its answers are still fixed by something other than the profile. The paper does not measure the cross-respondent variance of its items, so the two findings are not compared on one object.

A second setting points the same way. In a comparison of residents' greenspace judgments with three multimodal models, each model was prompted either as a generic citizen or as the socio-demographic profile of the actual respondent. The two conditions differed little: the authors conclude that adding the profile "does not meaningfully influence the models' evaluations."[^c13] The contrast they draw is with text-only work, where "user profiling can influence responses."[^c14] The profile there was socio-demographic, not the respondent's own answers, so that paper does not test the richer person-level content that [[narrative-over-demographic-persona-conditioning]] found to move answers. Their reading is that the judgments come from the image rather than from the asker (the authors' inference, not a tested cause).

## Limits

- Small and specific: 16 items from three domains, 100 sampled individuals.[^c7] The 50% figure comes from a manual analysis of the questions tested, not from a sample of all survey items.
- Fixity varies by domain. Diverse claims could be elicited for "all questions in the religion domain," while the authors report that "inherent biases limit diversity for some questions."[^c8] The insensitivity is not a single property of the model across topics.
- Three models: GPT-4o-mini, Llama 4 and Qwen 3. The paper "did not include reasoning models such as OpenAI O3, Deepseek," so whether reasoning changes the fixity is not known from this work.[^c9]
- The RLHF explanation is a hypothesis. The authors "did not explore fine-tuning or RLHF" and say only that they "hypothesize that simple post-training approaches cannot tackle these limitations."[^c10][^c12]
- Fixity is not the same as inaccuracy, and the paper's accuracy results are weak on their own: "None of the approaches provide accurate user" simulations.[^c11] A stance that does not move with the profile is one way to fail; the paper does not separate it from others.

## Related

- [[simulated-respondent-variance-deficit]] — the spread across respondents within an item, a different measure of the same simulation
- [[narrative-over-demographic-persona-conditioning]] — which person-level content moves simulated answers at all; demographics alone moved them little there too
- accuracy-distribution-dissociation — the same paper's finding that a wider answer distribution does not bring accuracy with it

[^c1]: arxiv-2512-06874 — "tend to maintain fixed viewpoints across varying demographic features"
[^c2]: arxiv-2512-06874 — "even when prompted with varying demographic profiles"
[^c3]: arxiv-2512-06874 — "this pattern occurs in 50% of the survey"
[^c4]: arxiv-2512-06874 — "the models consistently produce affirmative claims"
[^c5]: arxiv-2512-06874 — "tend to reflect a unified viewpoint, even when"
[^c6]: arxiv-2512-06874 — "also fundamentally limits their ability to simulate"
[^c7]: arxiv-2512-06874 — "a total of 16 questions"
[^c8]: arxiv-2512-06874 — "all questions in the religion domain"
[^c9]: arxiv-2512-06874 — "reasoning models such as OpenAI O3, Deepseek"
[^c10]: arxiv-2512-06874 — "we did not explore fine-tuning or RLHF"
[^c11]: arxiv-2512-06874 — "None of the approaches provide accurate user"
[^c12]: arxiv-2512-06874 — "post-training approaches cannot tackle these limitations"
[^c13]: arxiv-2512-11827 — "suggesting that adding sociodemographic context to the prompts does not meaningfully influence the models' evaluations."
[^c14]: arxiv-2512-11827 — "Unlike findings from text-only LLM research where user profiling can influence responses"
