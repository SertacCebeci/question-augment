---
description: "Stating a coding task's input-output constraints and core algorithm with its time complexity before writing code, as a separate intermediate, beat six prompting baselines on harder benchmarks."
aliases: ["intention chain-of-thought", "ICoT", "Specification and Idea", "intention abstraction in code generation", "previewing stage (Blueprint2Code)"]
sources: ["arxiv-2512-14048", "doi-10-3389-frai-2025-1660912"]
---
# Intention abstraction

Before writing code, a model is asked to state two things about the task. A Specification fixes the input and output constraints. An Idea names the core algorithmic logic and estimates its time complexity.[^c1] The code is then written conditioned on that pair, not on the problem text alone. The paper calls the pair Intention Chain-of-Thought (ICoT), a structure that "explicitly models the task intention using a specification-and-idea structure".[^c3] Its motivation is a separation the authors take from classic problem solving, "separating task comprehension from solution design".[^c2] The intention is written text that the code stage reads, so the structure is visible and can be compared with the code it produces.

The mechanism has two stages. In the first, the model "is prompted with the input problem to generate a diverse set" of candidate intentions, each a Specification and an Idea decoded jointly, and the decoding "leverages stochastic decoding techniques (e.g., nucleus sampling)".[^c4][^c5] In the second, each intention is used to produce one program by greedy decoding, with the code stage "guiding code generation aligned with the task" conditioned on both the problem and that intention.[^c6] The sampled set therefore carries several candidate algorithms, and each is turned into one program. The authors say the route "guides the model from explicit modeling of task requirements to core algorithmic design".[^c7] Their worked example is a same-characters check, where the stated idea (build a set, compare the sets, cost O(m + n)) becomes a one-line set comparison.[^c7]

What was measured. Over three models and six code benchmarks, the paper reports that "ICoT consistently outperforms six prompting baselines" on the harder ones.[^c8] The ablations were run with one model, DeepSeek-V3-671B, on six benchmarks, and show each stage carrying weight.[^c9] Removing the Specification stage "reduces Pass@1 from 92.07% to" 88.17% on HumanEval.[^c10] On McEval, "removing the Idea stage leads" to a drop from 67.20% to 59.20%.[^c11]

The concept sits beside two other things the wiki holds. The intention here is written text, not the hidden state read before the first token, which is a different object in [[pre-collapse-intention-state]]. The structure is an expensive branch: the router that decides which problems get it is [[complexity-tiered-strategy-routing]], and in this paper the routing label comes from a prompted classifier. A stage diagnosis that places failure in requirement recovery, [[implicit-requirement-recovery-bottleneck]], is the step the Specification stage targets. That last link is my reading; the paper does not cite the diagnosis.

A second paper puts the same split into a multi-agent code pipeline, as a previewing stage placed before any plan or code. Its Previewing Agent "generates a task summary", suggests algorithm categories and gives key hints.[^c16] The stage is said to cover "input/output feature extraction, and strategy association", which is close to the Specification and Idea pair here, though the paper does not mention a complexity estimate (my reading).[^c17] The ablation removes it on HumanEval with GPT-3.5-turbo: the table gives 76.8% with the stage removed, a drop of 15.4 points, and the text gives the two removals together, "results in accuracies of 77.4 and 76.8%", in that order.[^c18] The authors read the drop as showing that "early-stage task understanding and structured planning provide a solid foundation for high-quality initial code."[^c19] This is a second measurement of the comprehension-before-design split, not a replication of the first: a different pipeline, a different benchmark family, and a stage ablated on its own.

## Limits

The benefit is shown on harder problems, and the paper's own ablation reverses on easy ones. Without the intermediate reasoning, the variant "achieves the strongest results" on the simpler MBPP sets.[^c12] The authors draw the lesson that "elaborate prompt structures can be counterproductive for simple problems."[^c13] An intention layer is therefore not a free default; its value depends on the task being hard enough to need it.

The text reports final pass rates. It does not report whether the generated Specification is correct, or whether the stated time complexity matches the algorithm the code uses. The Idea is a claim the model makes about its own solution, and nothing in the slices I read checks that claim against the code. So the measured gain is in pass rate, not in the accuracy of the intention.

The ablations use a single, large model. The main table covers three models, from a 3B to a 671B mixture-of-experts, but I did not find a per-model ablation in the text, so whether the same stage contributions hold for the smaller models is not shown.

The benchmarks are mostly Python. McEval, the multilingual one, is used as "we use its Python subset of 50" problems.[^c14] The comparisons also run against the authors' own standardized instructions, which "differ from the highly optimized model-specific prompts designed to maximize reported performance".[^c15] The reported gains are therefore relative to a fixed prompt set, not to the best published prompting of each model.

The preview evidence is narrower still. It is one ablation, with one model and one benchmark, and the text reports no repeated runs or spread. The two drops it gives imply different full-system values, 92.2 from the preview and Blueprint rows and 93.5 from the debugging row (my arithmetic), and the text does not say which run each drop is measured against. The stage draws only on the model's own knowledge, since the paper says it "does not rely on external knowledge bases",[^c20] so nothing outside the model checks its hints (my inference). The paper's gain is reported for "particularly for problems involving implicit conditions or edge-case traps",[^c21] and the slices I read do not show whether the hints are correct.

## Related

- [[complexity-tiered-strategy-routing]] — the router that decides when a problem is sent to a structured route, and when a direct answer is enough.
- [[pre-collapse-intention-state]] — "intention" as a hidden state read before the first token; here the intention is written text that conditions the code.
- [[implicit-requirement-recovery-bottleneck]] — a stage diagnosis placing failure in requirement recovery; the Specification stage is aimed at that step (my reading, not the paper's claim).
- [[function-level-step-decomposition]] — code has no natural reasoning steps; ICoT places the steps at the level of the task's intention rather than at the function boundary.

[^c1]: arxiv-2512-14048 — "a Specification element that defines the input-output constraints, and an Idea element that captures the core algorithmic logic and estimates time complexity"
[^c2]: arxiv-2512-14048 — "separating task comprehension from solution design"
[^c3]: arxiv-2512-14048 — "explicitly models the task intention using a specification-and-idea structure"
[^c4]: arxiv-2512-14048 — "prompted with the input problem to generate a diverse set"
[^c5]: arxiv-2512-14048 — "leverages stochastic decoding techniques (e.g., nucleus sampling)"
[^c6]: arxiv-2512-14048 — "guiding code generation aligned with the task"
[^c7]: arxiv-2512-14048 — "which guides the model from explicit modeling of task requirements to core algorithmic design"
[^c8]: arxiv-2512-14048 — "ICoT consistently outperforms six prompting baselines"
[^c9]: arxiv-2512-14048 — "Pass@1 accuracy of ICoT and its ablated variants across six benchmarks using DeepSeek-V3-671B"
[^c10]: arxiv-2512-14048 — "removing the Specification stage reduces Pass@1 from 92.07% to"
[^c11]: arxiv-2512-14048 — "on McEval, removing the Idea stage leads"
[^c12]: arxiv-2512-14048 — "without intermediate reasoning achieves the strongest results"
[^c13]: arxiv-2512-14048 — "This supports our prior finding that elaborate prompt structures can be counterproductive for simple problems."
[^c14]: arxiv-2512-14048 — "we use its Python subset of 50"
[^c15]: arxiv-2512-14048 — "differ from the highly optimized model-specific prompts designed to maximize reported performance"
[^c16]: doi-10-3389-frai-2025-1660912 — "the Previewing Agent generates a task summary"
[^c17]: doi-10-3389-frai-2025-1660912 — "input/output feature extraction, and strategy association"
[^c18]: doi-10-3389-frai-2025-1660912 — "results in accuracies of 77.4 and 76.8%"
[^c19]: doi-10-3389-frai-2025-1660912 — "early-stage task understanding and structured planning provide a solid foundation for high-quality initial code"
[^c20]: doi-10-3389-frai-2025-1660912 — "does not rely on external knowledge bases"
[^c21]: doi-10-3389-frai-2025-1660912 — "particularly for problems involving implicit conditions or edge-case traps"
