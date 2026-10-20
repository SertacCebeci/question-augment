---
description: "Having a policy write candidate user intents in a tag before answering, with reward on the answer only, makes the inferred intent matter: swapping it out lowers personalized scores."
aliases: ["intent-tag reasoning", "latent-intent rollout", "intent-conditioned thinking before personalized answer"]
sources: ["doi-10-48550-arxiv-2605-12645", "arxiv-2512-20458"]
---
# Latent intent before answer

A single question often underdetermines what the asker needs. "Should I change my job?" may come from someone who wants a decision framework or someone who wants help diagnosing burnout. The IAP framework treats the unstated goal as an intermediate object the model must produce before it answers. The rollout has a fixed tag structure: a first thinking block, then a numbered list of candidate intents inside an intent tag, then a second thinking block that "explicitly conditioning on the inferred intents to plan the" answer, then the answer in its own tag.[^c1]

The intents are not gold labels. Each one is described as "a plausible hidden motivation or need."[^c2] Nothing checks them directly. Reward is computed only on the final answer, so the intent list is trained indirectly: a list that leads to a better-scored answer is reinforced. The paper states this design choice directly: "This design enables IAP to learn intent-aware generation without requiring gold intent labels."[^c3] A length penalty applies to intent segments longer than a threshold L. Its purpose is not stated beyond that; my reading is that it discourages padding the list with many weak guesses.

The evidence that the intent step carries weight is an intervention on the trained model. Holding the policy fixed, the authors replace the intent it inferred with no intent, a random intent from the same LaMP-QA category, or a random intent from another category. The selected intent gives the highest personalized score for every model, and the paper's summary is that "removing intent leads to large drops, and random intents also perform far below the selected-intent setting."[^c4] So the answer depends on the intent it was conditioned on: the paper reports drops for both no intent and random intent, with the selected intent best. The count of intents matters too: answer quality "declines as the number of inferred intents increases."[^c5]

The mechanism is a latent variable made explicit in the generation. The model is not asked to classify the user into a fixed taxonomy; it writes free-text hypotheses and then conditions on them. The transferable part is the separation of inference (which intents are plausible) from generation (answer given intents), with reward applied only to the second.

A structurally similar step appears in a search agent, Laser, where intent refinement is the first action of the planning stage. The output is "the refined and structured user intent, which is a JSON data,"[^c8] with a refined goal and a list of constraints. The motivation given is that "refining the intent and extracting explicit constraints enables the agent to establish a clearer objective."[^c6] Removing that action gives "a clear performance drop, highlighting the importance of explicit intent interpretation."[^c7] The Laser intent is stored in the [[context-register]] and read by later steps. The paper reports the effect of removing the step, not of swapping in a wrong intent as the IAP authors do, so it is weaker evidence that the content of the intent matters. Whether the search-QA drop and the personalized-answer drop share a mechanism is not tested here. (My inference.)

## Limits

- The paper does not evaluate the intent list itself. Its claim that "the inferred <intent> captures" the user's goal rests on the drop in answer score under substitution, not on a comparison with human-written intents. A high answer score could follow from intents that are merely useful conditioning text.
- The ablation swaps intents at inference time for a model trained with its own intents. It does not train a model on random intents, so it shows reliance on the intent at test time, not what training on wrong intents would do.
- Answer quality is scored by an LLM judge against per-question rubric aspects (LaMP-QA), so the notion of a good intent is tied to that rubric. Questions without rubrics, or with several equally valid goals, are not tested.
- The paper is single-turn by design. Its motivation is that multi-turn history is often unavailable; it does not measure how the intent step compares with a model that does have the history.
- The contrast with intent-free answers is a separate reward term ([[intent-free-contrastive-reward]]). The ablations in the paper vary the intent and the contrast term separately, so their joint contribution is not isolated.
- The intent-count result is reported as a trend across three buckets (1–2, 3–4, 5+). The bucket sizes and the number of questions per bucket are not part of the text I read, so the size of the trend is not established.

## Related

- [[intent-free-contrastive-reward]] — the reward term that compares each trained answer against the same model's intent-free answer
- [[intent-aware-response-strategy]] — routes a tutoring query into one of five fixed pedagogical intents; the fixed-taxonomy alternative this method avoids
- [[implicit-predictive-intent]] — finds intent recognition to be the bottleneck in a different setting, where the intent is also implicit
- [[permutation-consistency-training]] — another RL setup where the reward is computed on a final output rather than on an intermediate step
- [[context-register]] — Laser's refined-intent slot, a structured intent kept in a state store and read by later search steps

[^c1]: doi-10-48550-arxiv-2605-12645 — "explicitly conditioning on the inferred intents to plan the"
[^c2]: doi-10-48550-arxiv-2605-12645 — "a plausible hidden motivation or need."
[^c3]: doi-10-48550-arxiv-2605-12645 — "This design enables IAP to learn intent-aware generation without requiring gold intent labels."
[^c4]: doi-10-48550-arxiv-2605-12645 — "leads to large drops, and random intents also perform far below the selected-intent setting."
[^c5]: doi-10-48550-arxiv-2605-12645 — "declines as the number of inferred intents increases."
[^c6]: arxiv-2512-20458 — "refining the intent and extracting explicit constraints enables the agent to establish a clearer objective"
[^c7]: arxiv-2512-20458 — "show a clear performance drop, highlighting the importance of explicit intent interpretation"
[^c8]: arxiv-2512-20458 — "the refined and structured user intent, which is a JSON data"
