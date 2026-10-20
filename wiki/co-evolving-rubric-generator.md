---
description: "A rubric generator trained in the same RL step as the policy, rewarded for the spread of scores its criteria give candidate answers, so the evaluation tracks the policy's gains."
aliases: ["adversarial rubric co-evolution", "rubric generator co-evolution", "discrimination-rewarded rubric generator"]
sources: ["doi-10-48550-arxiv-2606-23038", "doi-10-48550-arxiv-2605-03871"]
---
# Co-evolving rubric generator

A static rubric is a fixed list of weighted criteria, each judged met or unmet for every answer. Its scores are informative early in reinforcement learning and flatten later: as the policy improves, the same criteria are met by more and more answers, and the reward stops separating them. The paper's wording is that the rubrics "become progressively saturated: increasingly many" responses satisfy them.[^c1]

A co-evolving rubric generator is a second model, trained beside the policy, that writes a new rubric set for each query at every training step. The evaluation is then itself a moving target rather than a reference fixed before training.

## Mechanism

The policy and the rubric generator are two low-rank adapters on one shared backbone (Qwen3-4B and Qwen3-8B in the experiments), each with its own optimizer. The backbone is first warm-started by supervised fine-tuning on responses from a stronger model.[^c2] In each step the policy samples M candidate answers and the generator samples N rubric sets. A judge model scores every answer against every rubric set, which fills an M × N score matrix.

The policy's reward for an answer is its average normalized score across the N rubric sets. Averaging over several independently generated rubric sets is the paper's defence against the noise of any single rubric.[^c3]

The generator's reward is a weighted sum of four terms. The discrimination term is the standard deviation of one rubric set's scores across the M answers, so a rubric that scores every answer alike earns nothing. A near-zero value, the paper says, "signals that the rubrics cannot distinguish response quality".[^c4] The diversity term is the mean pairwise cosine distance between criterion embeddings. The alignment term is a judge's similarity score between the generated rubric and a preconstructed human rubric. The constructiveness term is the average score gain on the human rubric when the policy revises its answers under the generated rubric.[^c5]

Both adapters are updated with GRPO inside the same step, on the same query batch. The paper's claim is that each side trains against the other's most recent behaviour, which "enabling real-time co-adaptation" distinguishes from earlier schemes that revised rubrics at epoch granularity.[^c6] The discrimination term is where the adversarial pressure sits: the generator is rewarded for criteria that expose the policy's remaining gaps, and the authors describe the result as an "auto-curriculum over evaluation standards."[^c7] The alignment and constructiveness terms exist to stop that pressure from producing arbitrary criteria or reward hacking.[^c8]

## What was measured

Training uses HealthBench, with 4,000 standard-difficulty examples for training and the 1,000 Hard cases held out for testing.[^c9] Against static and dynamic rubric-RL baselines, the authors report that EvoRubrics "consistently improves policy performance across in-domain and OOD evaluations."[^c10] The learned generator is also used as a reward model for preference ranking on RubricBench.[^c11]

The ablation removes reward terms one at a time on Qwen3-4B. The paper's reading is that "All reward components are important, with discriminativeness serving as the core signal."[^c12] A fully self-supervised variant, which drops the alignment term and needs no preconstructed rubrics, is reported to keep "meaningful gains" from the co-evolution alone.[^c13]

What survives the move from this RL setting to asking and answering is one idea: an evaluation is worth what it can separate among the candidates currently being produced, measured against those candidates rather than against a fixed reference. What does not survive is the paper's own yardstick, which is the policy's score on rubric-based benchmarks. Whether the rubrics are valid for a human reader is a separate question that this mechanism does not answer.

A different instance of the same co-evolution appears in EvoLM, where one Qwen3-8B model plays both roles and the generator learns from preference pairs the policy builds from its own outputs, with no human rubric and no proprietary model. Its comparison is the useful part. Training the generator and policy alternately gave a policy average of 69.3%, against 68.3% for sequential training, even though the sequential generator scored higher on static rubric accuracy: "despite sequential training achieving higher static rubric."[^c18] The authors read the gap as a matter of adaptation: "Downstream policy quality depends on how well rubrics adapt to the evolving policy distribution."[^c19] The two papers agree that the evaluation has to move with the policy. They differ on the reward. Here the generator is paid for the spread of scores; in EvoLM it is paid for the judge's ability to rank self-generated pairs (see [[temporal-contrast-preference-pairs]]).

## Limits

- Training and the main results sit in one domain, medicine. The authors state that "training is primarily conducted in the medical domain," and list legal reasoning, creative writing and scientific QA as untested.[^c14]
- The experiments stop at models of up to 8B parameters, so the performance ceiling at larger scale was not measured.[^c15]
- Generator and policy share one backbone, so they may amplify shared biases or spurious preferences. The authors name this as a risk and do not measure it.[^c16]
- A single judge model scores everything, "used as the judge throughout training and evaluation."[^c17] The paper does not vary the judge, so the reward is only as stable as that judge.
- A spread of scores is not the same as a correct distinction. A rubric that splits answers on an irrelevant feature would score high on discrimination. This is my inference; the alignment and constructiveness terms are the paper's guard against it, and their effect was not isolated beyond the ablation.
- The size of the gains is not stated in this note; the numeric tables were not read in full.
- The EvoLM co-evolution advantage is one point (69.3% against 68.3%) on one 12-benchmark average from one model family. The parts read report no variance across runs, so the gap's stability is untested (my inference).

## Related

- [[rubric-difficulty-evolution]] — the same saturation problem, answered by extending a fixed rubric from reference answers rather than by a generator trained against the policy
- [[pretraining-grounded-rubric-self-play]] — a self-play rubric verifier grounded in a document; it does not co-train the rubric writer with a spread-based reward
- [[reasoning-judge-adversarial-policy]] — a policy exploiting its judge, the failure the alignment term here is meant to block
- [[rubric-complexity-normalized-reward]] — another rubric-based GRPO reward, scaled by rubric size rather than by discrimination

[^c1]: doi-10-48550-arxiv-2606-23038 — "become progressively saturated: increasingly many"
[^c2]: doi-10-48550-arxiv-2606-23038 — "Before co-evolutionary RL, we warm-start the LLMs"
[^c3]: doi-10-48550-arxiv-2606-23038 — "mitigates the noise of any single evaluation rubric."
[^c4]: doi-10-48550-arxiv-2606-23038 — "a near-zero value signals that the rubrics"
[^c5]: doi-10-48550-arxiv-2606-23038 — "Constructiveness reward. Beyond evaluation, effective rubrics should provide actionable guidance"
[^c6]: doi-10-48550-arxiv-2606-23038 — "models train against each other’s most recent behavior, enabling real-time co-adaptation rather than"
[^c7]: doi-10-48550-arxiv-2606-23038 — "auto-curriculum over evaluation standards."
[^c8]: doi-10-48550-arxiv-2606-23038 — "prevent this pressure from drifting into reward hacking or misaligned evaluation."
[^c9]: doi-10-48550-arxiv-2606-23038 — "We use HealthBench (Arora et al., 2025) as"
[^c10]: doi-10-48550-arxiv-2606-23038 — "EvoRubrics consistently improves policy performance across in-domain and OOD evaluations."
[^c11]: doi-10-48550-arxiv-2606-23038 — "preference ranking on RubricBench"
[^c12]: doi-10-48550-arxiv-2606-23038 — "All reward components are important, with discriminativeness serving as the core signal."
[^c13]: doi-10-48550-arxiv-2606-23038 — "even a fully self-supervised variant without any external supervision achieves meaningful gains"
[^c14]: doi-10-48550-arxiv-2606-23038 — "training is primarily conducted in the medical domain."
[^c15]: doi-10-48550-arxiv-2606-23038 — "experiments are limited to models up to 8B parameters."
[^c16]: doi-10-48550-arxiv-2606-23038 — "may amplify shared biases or spurious preferences, especially when both components are trained from the same backbone."
[^c17]: doi-10-48550-arxiv-2606-23038 — "judge throughout training and evaluation."
[^c18]: doi-10-48550-arxiv-2605-03871 — "despite sequential training achieving higher static rubric"
[^c19]: doi-10-48550-arxiv-2605-03871 — "Downstream policy quality depends on how well rubrics"
