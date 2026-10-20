---
description: "Terminal-reward RL on elicitation collapses per-criterion labels into one scalar and learns static questions; learning criterion correlations offline then doing Bayes online keeps adaptivity."
aliases: ["factored supervision", "offline structure learning plus online Bayesian elicitation", "Pep"]
sources: ["arxiv-2602-15012"]
---
# Factored versus entangled supervision in elicitation

When the training data holds a complete preference profile per user, there are two ways to learn how to ask. Train a questioning policy end to end against a terminal reward (entangled), or learn the correlations among criteria directly from the per-criterion labels (factored) and select questions by Bayesian inference at run time. Bose et al. (2026) argue the second keeps what the first throws away.

## Mechanism

The setting is a routing problem: a task can have 20–30 preference dimensions, a given user cares about 2–4, and which ones depends on who is asking.[^c1] Preferences are correlated across dimensions, so one answer updates beliefs about many unasked criteria.[^c2]

RL's reward is sparse and terminal: only the final response is scored after T questions, so the agent must solve credit assignment across all T decisions.[^c3] The authors report the consequence: the trained policy converges to static question sequences, with 0% adaptivity on AIME.[^c4] The same datasets contain dense per-criterion labels, which the scalar reward discards.[^c5]

Pep instead learns a structured world model offline from complete profiles, with latent user embeddings. Online, it keeps a posterior over the embedding, updates it by Bayes' rule after each answer, picks questions that maximize information gain about the whole profile, and predicts the unasked criteria.[^c6] The belief model can be Bayesian linear regression, about 10K parameters against 8B for the RL baselines.[^c7]

Measured results: 80.8% alignment against 68.5% for RL, with 3–5x fewer interactions; adaptivity (how often different answers lead to a different next question) of 39–62% against 0–28% for RL.[^c8] Adaptivity alone is not the point. CollabLLM reached 28–44% adaptivity but only 20–26% alignment, because it cycled through generic topics. Changing questions helps only if the change uses learned preference structure.[^c9] The RL policy's adaptivity tracked how much criteria overlapped across samples: with high overlap it could memorize fixed sequences, with low overlap it fell below the population average.[^c10]

## Limits

- Needs complete preference profiles for offline training. Without them the factored signal does not exist, and the contrast with RL is moot.
- The evidence is four reasoning domains with a rubric-judged alignment score (PrefAlign) and simulated profiles. Real users are untested here.
- The RL baselines' failure is attributed to the reward structure by the authors. My reading is that the comparison also differs in model class and data use, so the causal attribution to credit assignment alone is not isolated.
- Claims about the Bayesian linear model's sufficiency may not carry to tasks whose criteria are not shared in a correlated latent space.

## Related

- [[population-prior-mining]] — another offline population prior for starting elicitation
- [[competence-aware-credit-assignment]] — credit assignment across turns, the problem Pep sidesteps
- [[cold-start-value-of-information]] — value of asking when no user history exists
- [[cross-type-eig]] — information-gain question selection over a prior
- [[investigative-question-grpo-training]] — RL-trained questioning, the contrasted approach

[^c1]: arxiv-2602-15012 — "individual users care about only 2–4 of these, and which 2–4 depends on who is asking"
[^c2]: arxiv-2602-15012 — "because observing one preference updates beliefs about many"
[^c3]: arxiv-2602-15012 — "the agent must solve credit assignment across all T sequential decisions"
[^c4]: arxiv-2602-15012 — "achieving 0% adaptivity"
[^c5]: arxiv-2602-15012 — "its training signal collapses factored supervision into a single scalar"
[^c6]: arxiv-2602-15012 — "we maintain a posterior over their latent"
[^c7]: arxiv-2602-15012 — "Pep achieves this with ∼10K parameters (Bayesian linear regression)"
[^c8]: arxiv-2602-15012 — "Pep changes its follow-up question 39–62% of the time versus 0–28%"
[^c9]: arxiv-2602-15012 — "changing questions is not sufficient"
[^c10]: arxiv-2602-15012 — "High overlap enables learning fixed"
