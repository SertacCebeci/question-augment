---
description: "Verifying a claim by first asking an open question of an external source that does not carry the claim, then comparing the answer, keeps the evidence from inheriting the claim's premise."
aliases: ["independent question asking", "claim-blind evidence query", "open-ended probe before comparison", "decoupled perception query", "ask_questions tool"]
sources: ["arxiv-2511-22998"]
---
# Independent question asking

A verifier that checks a reasoning step by asking "is this claim true?" has the claim in front of it. If the claim is a false visual fact, such as "the graph is a parabola", the verifier tends to accept it. Independent question asking changes what the checker is asked, not the rule by which it decides. The checker poses an open question to an external source, a question that does not contain the claim, and only afterwards compares the answer with the step. The idea is developed in TIM-PRM, a tool-using process reward model for multimodal math reasoning, where the external source is a vision-language tool called `ask_questions`. The paper frames the change as turning verification "from a passive classification task into" an active investigation.[^c1]

The mechanism is a dependence argument. The paper treats a verifier's probability of marking a step correct as conditioned on the question, the image and the earlier steps. The problem is that the probability of "Correct" is "artificially inflated by the presence" of false premises in the step, so the model validates a premise without checking it against the image.[^c2] The fix the paper proposes is to avoid asking the verifier to judge the hypothesis directly. In its words, "Instead of verifying a hypothesis directly, which often triggers sycophancy," the model generates open-ended queries "targeting the visual features of I".[^c3][^c4] The tool's reply then becomes a fact "decoupled from the hypothesis h", and the verdict is reached by comparing the step with that reply.[^c5]

The wording of the query carries the weight. In the paper's illustration, a step claims that Store B's value is 200. A query of the form "is Store B 200?" carries the claim inside it. The query the method uses is "the value of Store B", and the tool returns "value for Store B is 177", so the step is judged a hallucination.[^c6][^c7] In the formal statement, the verdict is derived by "comparing the content of st against the grounded evidence", and the query is written so that it does not depend on the truth value of the hypothesis.[^c8]

What was measured is the whole framework, not the query alone. TIM-PRM-8B "achieves an overall FISI score of 26.4" for first-incorrect-step identification, against 9.9 for the scalar VisualPRM-8B.[^c9] Its step-verification F1 is above "Qwen2.5-VL-72B (60.5)", a model roughly nine times larger.[^c10] The authors also vary the tool backend. Moving it from Qwen3-VL-2B to Qwen3-VL-30B raises the verifier's overall F1 "from 58.6 to 60.3", which they read as the verifier "offloads the burden of finegrained visual perception to the tool".[^c11] The tool is invoked in "roughly 21.6% of correct steps" and in a similar share of wrong ones, which the authors take to mean the call follows the task, not the step's correctness.[^c12]

## Limits

- **No isolated ablation in the parts read.** The ablations vary the tool backend and the training upweighting. I did not find a run that swaps the independent query for a direct "is h true?" check on the same backbone. The gain from decoupling is therefore not separated from the extra planning step, the second model call, or the training data. The claim that the decomposition is "significantly reducing visual hallucinations" is the authors' reading.[^c13]
- **The independent fact is only as good as the tool.** "The efficacy of our framework relies on the reliability of the external feedback."[^c14] The tested range is 2B to 30B; a weaker tool with a strong planner is not tested.
- **Visual scope.** The paper says its method "does not fully address complex" logical or calculation errors.[^c15] The evidence is five math benchmarks. A claim with no perceptual part gives the query nothing to separate from the reasoning.
- **Cost.** The authors concede the approach "incurs a higher inference cost compared to passive scalar" verifiers.[^c16]
- **Query form is asserted, not measured.** The paper does not test how the wording of the query changes the tool's answer. My inference, not the paper's: a question such as "the value of Store B" still names the claim's subject, so what is independent is the verdict's dependence on the claim, not the vocabulary of the query.

## Related

- [[hypothesis-conditioned-query-rewriting]] — the opposite move: its queries are built from the working hypothesis, so retrieval is conditioned on it, while independent question asking strips the hypothesis out of the query and compares only afterwards.
- [[non-monotonic-prompt-pressure-hallucination]] — a yes/no probe as a trigger of visual sycophancy under prompt pressure; the same query form that this note avoids.
- [[support-skew-in-claim-verification]] — verifiers asked whether a figure supports a claim lean toward "supported", the failure the claim-blind query is meant to reduce.
- [[evidence-grounded-step-reward]] — grades each reasoning step against retrieved evidence; that note does not describe its search as independent of the step.
- [[user-driven-sycophancy]] — sycophancy toward the user's stated view; here the premise that attracts agreement is the verifier's own input step.
- [[verification-over-invention]] — retrieval aimed at checking a stated claim, the setting in which a claim-blind query is useful.

[^c1]: arxiv-2511-22998 — "transforms verification from a passive classification task into"
[^c2]: arxiv-2511-22998 — "artificially inflated by the presence"
[^c3]: arxiv-2511-22998 — "Instead of verifying a hypothesis directly, which often triggers sycophancy"
[^c4]: arxiv-2511-22998 — "targeting the visual features of I"
[^c5]: arxiv-2511-22998 — "decoupled from the hypothesis h"
[^c6]: arxiv-2511-22998 — "the value of Store B"
[^c7]: arxiv-2511-22998 — "value for Store B is 177"
[^c8]: arxiv-2511-22998 — "content of st against the grounded evidence"
[^c9]: arxiv-2511-22998 — "achieves an overall FISI score of 26.4"
[^c10]: arxiv-2511-22998 — "Qwen2.5-VL-72B (60.5)"
[^c11]: arxiv-2511-22998 — "the verifier effectively offloads the burden of finegrained visual perception to the tool"
[^c12]: arxiv-2511-22998 — "tools are invoked in roughly 21.6% of correct steps"
[^c13]: arxiv-2511-22998 — "significantly reducing visual hallucinations"
[^c14]: arxiv-2511-22998 — "the efficacy of our framework relies on the reliability of the external feedback"
[^c15]: arxiv-2511-22998 — "this does not fully address complex"
[^c16]: arxiv-2511-22998 — "higher inference cost compared to passive scalar"
