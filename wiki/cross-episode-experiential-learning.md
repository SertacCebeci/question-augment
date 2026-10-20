---
description: "Across-episode experiential learning reuses what past interactions revealed about shared latent preferences to shape later questions; frontier LLM agents learn within a dialogue, not across."
aliases: ["experiential learning", "in-context experiential learning", "across-episode adaptation", "cross-episode learning of questioning strategy"]
sources: ["arxiv-2511-22130"]
---
# Cross-episode experiential learning

Experiential learning, in the sense the paper takes from Silver and Sutton, is the ability to act better in a new task because of what earlier tasks revealed: "we refer to this ability as experiential learning."[^c1] The concept is about information-gathering under uncertainty. An agent that does not yet know a customer's taste must ask; which questions are worth asking depends on how tastes are distributed over the population the agent serves. The paper's example is blunt: in a market where tastes concentrate on a few clusters, "a small number of well-chosen questions" can separate them, while in a niche market "the same broad questions are uninformative."[^c2] The optimal questioning policy is therefore a function of a distribution that is rarely known in advance, and the agent has to infer it from its own experience: "preference distribution dictates how the agent should act under uncertainty."[^c3]

Two levels of learning are kept apart. Within an episode, the agent resolves uncertainty as answers arrive across turns. Across episodes, it refines the strategy it uses to start the next episode, by inferring the structure the episodes share. In the paper's product-recommendation setting an episode is one shopping session, "from initial inquiry to final recommendation," and the paper says this whole interaction "constitutes an episode."[^c4] The feedback at the end of the episode, a rating, a regret or free text, is the carrier of information about the episode's latent factor, and the agent's history includes earlier episodes' turns and feedback. The paper's stated requirement is that "A performant recommender must learn across users and products and improve based on experience."[^c5]

The measured result is a dissociation. In the paper's benchmark, regret is "the main metric of merit for the recommendation," scored against the best product in the choice set.[^c6] Frontier models do reduce their in-dialogue uncertainty: the paper's caption for one model says "GPT-5.4 exhibits within-dialogue learning across turns, but does not improve across" episodes.[^c7] Across ten episodes and 40 seeds, "no models exhibit episode-over-episode improvements."[^c8] The number of questions also stays flat: "the number of questions asked generally remains the same for most models."[^c9] The authors read this as "proactive information gathering as a major deficiency in the behavior patterns of SOTA models."[^c10] Their confidence estimates do not repair the gap either: the paper says the in-context experience "does not reliably improve uncertainty estimates."[^c11]

The paper also constructs trajectories in which, by its account, the agent does improve: regret falls across episodes, and "the ideal trajectories ask progressively fewer questions over episodes."[^c12] These are not an agent's achieved behaviour; they are a witness that the information needed for across-episode gains exists in the interactions, which the paper frames as "a witness to shared information that agents could have leveraged."[^c13]

## What transfers

The transferable part is a separation of two capacities that an evaluation can run together: solving the task in front of you, and changing how you approach the next task from the distribution of tasks you have seen. A system can score well on the first and show nothing on the second. The distinction also says what a question is worth: its information value depends on the belief the asker holds, and across episodes that belief is precisely the prior over latent preferences, so a question that is informative in one population can be idle in another. [[expected-information-gain]] gives the value of a question under a given belief; this concept says the belief itself has to be learned across tasks, and that is the part the paper finds missing.

What does not transfer directly is the benchmark. The customers are simulated, and the paper states that the design favours learnability over realism: "it exposes consistent latent structure that the recommender can learn from interactions."[^c14] Whether the same dissociation holds for real users, or for questioning in a domain without a fixed scoring function, the paper does not test.

## Limits

- The customers are LLM personas. "Users are simulated by a LLM (GPT-4o) prompted to respond" to the agent's questions.[^c15] The authors say "we do not expect the simulated customers to reflect real users."[^c16] The regret target is itself an LLM score, "an average of the scores generated using two models: GPT-4o and Gemini-1.5-Pro."[^c17]
- The headline comparison is one setting in the main text: "over 10 episodes across 40 random seeds under setting (a), using Free-form Text" feedback, for three frontier models. The other settings, models and feedback types are reported in an appendix I did not read in full.
- The ideal trajectories are hand-selected. The authors run five repetitions and "pick one high-quality trajectory that" "contains questions that target meaningful aspects of the persona."[^c18][^c19] The selection uses knowledge of the persona, so the witness shows that good questions exist for that persona; it does not show that a policy could find them without it.
- The paper does not explore training. It says "This work also does not explore training methods to instill experiential learning," so nothing here shows whether a trained memory, a fine-tuned policy or a prompt would close the gap.[^c20]
- The word "experiential" is used here for an in-context capacity measured over a stream of tasks. It is not the name of a memory mechanism. [[contrastive-experiential-memory]] uses the same word for a text bank built from RL trajectories; the two do not share a method.

## Related

- [[preference-elicitation-gap]] — a signal can be present in an implicit channel and still go unused; the paper's ideal trajectories make the same split between signal present and signal used.
- [[expected-information-gain]] — the value of a question under a belief; across-episode learning is the claim that the belief's prior has to be learned.
- [[calibration]] — the confidence an agent attaches to its recommendation, which the paper finds does not improve across episodes.
- [[contrastive-experiential-memory]] — a different use of "experiential": a trained text memory from contrasting trajectories, which this paper does not test as a fix.

[^c1]: arxiv-2511-22130 — "we refer to this ability as experiential learning"
[^c2]: arxiv-2511-22130 — "the same broad questions are uninformative"
[^c3]: arxiv-2511-22130 — "preference distribution dictates how the agent should act under uncertainty"
[^c4]: arxiv-2511-22130 — "constitutes an episode"
[^c5]: arxiv-2511-22130 — "A performant recommender must learn across users and products and improve based on experience"
[^c6]: arxiv-2511-22130 — "The main metric of merit for the recommendation is the regret"
[^c7]: arxiv-2511-22130 — "GPT-5.4 exhibits within-dialogue learning across turns, but does not improve across"
[^c8]: arxiv-2511-22130 — "no models exhibit episode-over-episode improvements"
[^c9]: arxiv-2511-22130 — "the number of questions asked generally remains the same for most models"
[^c10]: arxiv-2511-22130 — "proactive information gathering as a major deficiency in the behavior patterns of SOTA models"
[^c11]: arxiv-2511-22130 — "suggesting that in-context experience does not reliably improve uncertainty estimates"
[^c12]: arxiv-2511-22130 — "The ideal trajectories ask progressively fewer questions over episodes"
[^c13]: arxiv-2511-22130 — "Their existence serves as a witness to shared information that agents could have leveraged"
[^c14]: arxiv-2511-22130 — "it exposes consistent latent structure that the recommender can learn from interactions"
[^c15]: arxiv-2511-22130 — "Users are simulated by a LLM (GPT-4o) prompted to respond"
[^c16]: arxiv-2511-22130 — "we do not expect the simulated customers to reflect real users"
[^c17]: arxiv-2511-22130 — "an average of the scores generated using two models: GPT-4o and Gemini-1.5-Pro"
[^c18]: arxiv-2511-22130 — "Out of the 5 repetitions, we pick one high-quality trajectory that"
[^c19]: arxiv-2511-22130 — "contains questions that target meaningful aspects of the persona"
[^c20]: arxiv-2511-22130 — "This work also does not explore training methods to instill experiential learning"
