---
description: "Response entropy of a black-box LLM is bimodal over generated questions, so two thresholds separate within- and beyond-knowledge questions with a narrow ambiguous band; an RL questioner probes it."
aliases: ["Knowledge Boundary Discovery", "KBD", "entropy-defined knowledge boundary"]
sources: ["arxiv-2603-21022"]
---
# Bimodal response entropy as a knowledge boundary

Wang and Lu define an answerer's knowledge boundary operationally, by the questions it can and cannot answer: "those the LLM can confidently answer (within-knowledge boundary) and (ii) those it cannot (beyond-knowledge boundary)."[^c1] Confidence is read from the token-level entropy of the target model's response, computed from log-probabilities over the vocabulary.[^c2] No access to internal states is needed; the target is a black box.

## Mechanism

A belief about each question's hidden status (within or beyond) is a sigmoid of the entropy distance to a threshold: P(within | E) = σ(β(E_th − E)).[^c3] The questioner is a Q-learning agent in a partially observable setting: the question is the action, the target's response is the observation, and the reward is the absolute change in entropy between consecutive responses, r = |E_prev − E_current|.[^c4] An episode stops once entropy falls below a threshold, and epsilon-greedy selection mixes random questions (to reach beyond-knowledge gaps) with greedy ones (to refine the within-knowledge area).[^c5] Reward shaping can flip the objective, for example rewarding high entropy to hunt for unanswerable questions.[^c6] In my reading, this is a questioner that treats the answerer as a sensor: each question is chosen for how sharply it moves the answerer's uncertainty, not for its own content.

## What was measured

- Over 2,000 generated responses the entropy histogram has two peaks, at entropy ≤ 40 and ≥ 170; only about 20% fall in the middle, so the ambiguous transition band is narrow.[^c7] The thresholds (40 and 170) were fixed from this distribution for these models.
- As a confidence signal, entropy gave the highest overall self-awareness score (mean of accuracy on answerable items and correct "unknown" rate on unanswerable ones) against min/product/first-token probability, prior and posterior prompts, in-context "I don't know" and verbalized uncertainty, on the KUQ, Sware and Infeasible benchmarks.[^c8]
- Against a random-question baseline and a domain-expert questioner, the RL agent and the experts both drive entropy down to the within-knowledge level, while random questions do not converge in 50 rounds; the agent is slower than the experts.[^c9]
- Generated question sets gave EER and F1 close to the human-built KUQ set across three 7B-class models (for example LLaMA 7B-Chat EER 0.239 vs 0.301, F1 0.725 vs 0.732).[^c10]
- Generated questions were nontrivial: t-SNE of embeddings shows answerable questions in a central cluster, unanswerable ones in a surrounding band, and random questions scattered.[^c11]

Examples of the two classes: a specific historical fact ("What treaty ended the Russo-Persian War?", entropy 26.63) is within; open speculative questions ("Are there limits to human creativity?", 211.29) are beyond.[^c12] This hints that high entropy conflates unknowable-in-principle or open-ended questions with facts the model lacks (my inference).

## Limits

- Evidence comes from three small models (ChatGLM2/3-6B, LLaMA 7B-Chat) with one generator model (GLM-4-9B); the generator is assumed, not shown, to have a wider boundary than the targets.[^c13]
- Raw entropy values (40 and 170) depend on the model, response length and sampling; the bimodality is not shown to transfer to other targets or to calibrated probabilities. Entropy was not checked against ground-truth correctness of the answers on the generated set; "within" means low entropy, which can be confident error (my inference).
- Comparison with human data is by similar EER/F1, not by identical items, so "comparable" is weak; no variance or significance tests appear in the text I read.
- The reward is the absolute entropy change, yet the text also describes it as entropy reduction; the two differ, and the agent could be rewarded for climbing into high-entropy regions.
- Convergence was shown on cumulative reward only.

## Related

- [[information-gain-reward]] — the same idea of paying a questioner for uncertainty reduction, here with entropy change of the answerer's output as the proxy
- [[calibration]] — entropy as a confidence signal competes with probability and verbalized confidence
- [[abstention]] — the unanswerable class is the set where an answerer should decline
- [[selective-abstraction]] — uses the boundary to decide when to answer
- [[boundary-sharpness]] — a benchmark metric of whether abstention tracks the same boundary

[^c1]: arxiv-2603-21022 — "those the LLM can confidently answer (within-knowledge boundary) and (ii) those it"
[^c2]: arxiv-2603-21022 — "This logprob is crucial for calculating the response"
[^c3]: arxiv-2603-21022 — "P (si = within | Ei ) = σ(β(Eth − Ei )),"
[^c4]: arxiv-2603-21022 — "rt = |Eprev − Ecurrent | ,"
[^c5]: arxiv-2603-21022 — "Exploration (ϵ branch) injects stochastic questions that"
[^c6]: arxiv-2603-21022 — "(e.g., rewarding high-entropy responses) and adjusting the"
[^c7]: arxiv-2603-21022 — "Only about 20% of the"
[^c8]: arxiv-2603-21022 — "Entropy consistently achieves the highest Saware on all datasets"
[^c9]: arxiv-2603-21022 — "random questioning"
[^c10]: arxiv-2603-21022 — "validating that our KBDgenerated dataset comparable to human-generated datasets."
[^c11]: arxiv-2603-21022 — "This structure supports the non-triviality of KBD-generated samples."
[^c12]: arxiv-2603-21022 — "Are there limits to human creativity?"
[^c13]: arxiv-2603-21022 — "we assume that GLM-4-9B has a wider"
