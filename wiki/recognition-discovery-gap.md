---
description: "Confirming a stated design relation is easier for an LLM than discovering the relations unprompted, and accuracy falls as the prompt withdraws guidance."
aliases: ["guidance ladder", "verification versus open-ended generation", "recognition versus discovery"]
sources: ["arxiv-2511-20933"]
---
# Recognition-discovery gap

The same model can be asked about one kind of relation under three formulations that differ in how much of the answer the prompt supplies. In Verification the model is given "an assertion and must simply confirm or deny it."[^r1] In Guided Generation it is given a seed entity, a single method or a single class, and must return the entities related to it. In Open-ended Generation "the model is given only the raw code and must autonomously discover design elements."[^r2] The authors take the ladder from Bloom's taxonomy, placing verification among the recognition levels and open-ended generation among the evaluating and creating levels.[^r3] The paper calls this an analogy; it does not test whether the levels map onto cognitive levels in the taxonomy's sense.

The measured result is that the ladder orders performance for both concepts. "For both cohesion and coupling, model performance is highest in Verification tasks," and "is lowest in Open-ended Generation tasks that offer minimal help."[^r4] For the 70B model on coupling, averaged over the three code transformations, F1 "falls from a high of 0.90 in Verification to 0.74 in Guided generation" and then to 0.61 in the open-ended setting.[^r5] For cohesion the same model reaches an F1 of 0.825 in verification[^r6a] and 0.649 in guided generation, below its coupling average.[^r6] In open-ended cohesion the score is an adjusted Rand index, and the authors report that it reached "0.43 in open-ended tasks"; they describe the resulting clustering as "far from indicating a coherent clustering."[^r7][^r7b]

The two concepts do not fall at the same rate or to the same place. The abstract's summary is that "their practical knowledge is fragile and highly asymmetrical."[^r8] Coupling keeps "a moderate F1 score for identifying coupled pairs" when the task is fully open, while cohesion is "significantly challenged."[^r9][^r9b] The ladder also interacts with injected noise. Coupling under distortion drops for the 70B model "from 0.59 to 0.27 F1 in open-ended tasks," while cohesion "remain[s] stable in verification and guided settings."[^r10][^r10b] The abstract states the interaction directly: the cohesion resilience "also fails when all guidance is removed."[^r11]

The paper's trace analysis gives one reading of why the open-ended end is hard. For coupling, "llms produce shorter reasoning traces in open-ended settings than in guided ones," and the authors name the pattern "cognitive shortcutting for coupling versus" a longer but still failing analysis for cohesion.[^r12][^r12b]

My inference, not the paper's: the ladder varies what the answerer must supply. A verification prompt supplies the hypothesis, so the answerer only tests it. An open-ended prompt asks the answerer to generate the hypothesis space as well, including the structure the answer lives in. For asking this is the same split between a question that states a relation and asks whether it holds, and a question that asks which relations there are. Which of the two the answerer can do well is a separate matter from how detailed the wording is. [[prompt-specificity-effect]] varies the wording; the ladder here varies the task.

## Limits

The study uses one model family, DeepSeek-R1 at 14B, 32B and 70B. The authors state that the results "may not apply to other programming languages" or to "other llms (e.g., GPT-4, Llama 3)."[^r13] Every case is Java.

The paper's scope is recognition, not repair. "Our work focused on assessing the recognition of design concepts" and the authors leave refactoring of the flawed code to future work.[^r14]

The three formulations differ in output form as well as in guidance: a yes/no answer, a list of related entities, and a partition of methods or a set of pairs. The ladder therefore may measure output format as much as guidance. The paper controls prompt length by stratified sampling, but no comparison holds the output form fixed while varying guidance. This is my reading of the design.

The two concepts are scored with different metrics, and the authors say that "a direct numerical comparison between metrics is inappropriate here."[^r15] The cohesion-coupling asymmetry is therefore a qualitative reading of the numbers, not a measured difference between the two.

The intermediate points are not varied. Three levels of guidance are given, and the drop between them is not shown to be linear or to have a threshold.

## Related

- [[generation-verification-gap]] — the same split between checking and producing, stated for proofs rather than design relations
- [[prompt-specificity-effect]] — how much detail a prompt carries; the ladder here varies what the model must produce, with the wording left aside
- [[distractor-similarity-reasoning-inflation]] — noise that resembles the question; this paper's noise is injected code, and its effect depends on the formulation
- [[underspecified-question-eager-answering]] — missing detail makes models answer where they should ask; the open-ended end of the ladder is where the answerer must supply the structure itself

[^r1]: arxiv-2511-20933 — "assertion and must simply confirm or deny it, (2) Guided generation: the model is given a partial"
[^r2]: arxiv-2511-20933 — "model is given only the raw code and must autonomously discover design elements."
[^r3]: arxiv-2511-20933 — "Success in this task mirrors the Evaluating and Creating levels of the taxonomy"
[^r4]: arxiv-2511-20933 — "is lowest in Open-ended Generation tasks that offer minimal help."
[^r5]: arxiv-2511-20933 — "falls from a high of 0.90 in Verification to 0.74 in Guided generation"
[^r6]: arxiv-2511-20933 — "is higher than its score for cohesion (0.649)"
[^r6a]: arxiv-2511-20933 — "The 70B model achieves an F1-score of 0.825 for cohesion,"
[^r7]: arxiv-2511-20933 — "while cohesion reaches an ARI score of 0.43 in open-ended tasks."
[^r7b]: arxiv-2511-20933 — "are far from indicating a coherent clustering."
[^r8]: arxiv-2511-20933 — "their practical knowledge is fragile and highly asymmetrical."
[^r9]: arxiv-2511-20933 — "The model maintains a moderate F1 score for identifying coupled pairs"
[^r9b]: arxiv-2511-20933 — "In contrast, its performance on cohesion is significantly challenged."
[^r10]: arxiv-2511-20933 — "from 0.59 to 0.27 F1 in open-ended tasks"
[^r10b]: arxiv-2511-20933 — "models remain stable in verification and guided settings"
[^r11]: arxiv-2511-20933 — "this resilience also fails when all guidance is removed."
[^r12]: arxiv-2511-20933 — "coupling tasks, surprisingly, llms produce shorter reasoning traces in open-ended settings"
[^r12b]: arxiv-2511-20933 — "revealing cognitive shortcutting for coupling versus"
[^r13]: arxiv-2511-20933 — "The results, derived from Java code and the DeepSeek-R1 family of models, may not apply to other programming languages"
[^r14]: arxiv-2511-20933 — "Our work focused on assessing the recognition of"
[^r15]: arxiv-2511-20933 — "While a direct numerical comparison between metrics is inappropriate here"
