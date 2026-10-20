---
description: "A rule-based reward pays a conclusion extra only when it explicitly points back to analysis written earlier in the answer, aiming to make unsupported additions costly during RL training."
aliases: ["conclusion cross-reference bonus"]
sources: ["arxiv-2512-00601"]
---
# Conclusion cross-reference reward

Outcome-only reinforcement learning pays for a correct final choice and nothing about how the answer is built. Clinical-R1 adds a rule-based term on the shape of the answer. The model must put its reasoning in a separate analytic block and its conclusion in another, and a bonus is paid when the conclusion refers back to the analytic block: "Additional reward is given when the conclusion explicitly references analytical elements from the dx"[^c1] (the paper's tag name for that block). The check is textual. It asks whether the conclusion cites the earlier text, not whether the cited sentences are true.

The mechanism the authors give is about what an unsupported addition has to do to earn reward. Because the conclusion is rewarded for pointing at sentences already written in the analysis, an invented finding has no such sentence to point at. In their words, CRPO works by "making unsupported additions costly: conclusions must point to sentences already established in <dx>."[^c2] They attribute to this a reduction in "language drift" and in invented labs, staging or etiologies.[^c8] The term does not inspect evidence. It makes the conclusion's dependence on earlier text a condition of reward, so a conclusion that drifts away from its own analysis is paid less. This is a structural pressure on the answer, set against the fluent-but-detached chain described in [[cot-hallucination-trap]].

The full reward has three parts. An accuracy reward is 1 for a correct choice. The clinical reasoning reward is 1 for the tagged format, with the extra 0.5 for the cross-reference, "an additional reward of 0.5 is given."[^c3] A consistency term "we define a consistency reward based on the ratio" of content tokens to all tokens, which discourages off-task output.[^c4] The authors state why the last term is needed: GRPO "may allow models to explore off-task responses or produce irrelevant tokens" when "comprehensiveness is rewarded."[^c5] So a reward for completeness is paired with a penalty on the padding that completeness can produce.

The weights matter. The accuracy coefficient is "k = 10," and the total maximum is "the maximum reward a response can get" in the paper's words, which is k + 2.[^c6][^c9] By my arithmetic the cross-reference bonus is 0.5 of a maximum of 12, about four per cent. The shape term is small beside accuracy, so any effect it has on the answer has to come from a small gradient.

On the reported results, the paper says "CRPO-trained models match or surpass GRPO in" answer accuracy.[^c10] The faithfulness gains are the larger claim. CRPO "consistently yields the strongest medical faithfulness across datasets," and the biggest gains are in citation density and distractor rejection.[^c11] Those scores come from a judge: "All of the above evaluation are done in an LLM-as-judge."[^c7]

## Limits

- Every faithfulness and hallucination number is a count made by an LLM judge (Llama-3.1-8B-Instruct and GPT-5). No clinician rated the reasoning in the text read, so the faithfulness claims measure the judges' reading of the answers.
- The text read contains no run with the cross-reference term alone removed. The GRPO-versus-CRPO comparison changes the format term, the cross-reference bonus and the consistency term together. The attribution of the hallucination reduction to the cross-reference is the authors' reading, not a separated effect.
- A textual reference is not evidence. By my inference, a conclusion that names a sentence from the analysis passes the check even if that sentence is wrong, and the reward cannot see the error. The paper does not test this case.
- The setting is narrow: one 3B model (Qwen2.5-3B-Instruct, "The base model we use is Qwen2.5-3B-Instruct"), multiple-choice medical QA.[^c12] Whether the mechanism holds for open-ended clinical answers, longer cases or other domains is not tested here.
- The accuracy claim is "match or surpass," not a clear gain. The abstract's own wording is "while maintaining comfortable accuracy enhancements,"[^c13] which is a weaker claim than an accuracy improvement.

## Related

- [[traceable-evidence-chain]] — tying each claim to a source as an audit trail; a human-review route to the same wish for checkable answers
- [[stage-structured-visual-reward]] — a reward on one tagged output section, the nearest existing case of paying for answer structure
- [[accuracy-auditability-trade-off]] — outcome reward can push a model away from auditable reasoning, the drift this structural term is meant to block
- [[cot-hallucination-trap]] — fluent reasoning detached from its evidence, which the cross-reference is meant to make costly

[^c1]: arxiv-2512-00601 — "Additional reward is given when the conclusion explicitly references analytical elements from the dx"
[^c2]: arxiv-2512-00601 — "making unsupported additions costly: conclusions must point to sentences already established in <dx>"
[^c3]: arxiv-2512-00601 — "an additional reward of 0.5 is given"
[^c4]: arxiv-2512-00601 — "we define a consistency reward based on the ratio"
[^c5]: arxiv-2512-00601 — "models to explore off-task responses or produce irrelevant tokens, such as content in other languages, especially when comprehensiveness is rewarded"
[^c6]: arxiv-2512-00601 — "so in total, the maximum reward a response can get"
[^c7]: arxiv-2512-00601 — "All of the above evaluation are done in an LLM-as-judge"
[^c8]: arxiv-2512-00601 — "which reduces language drift and discourages invented labs"
[^c9]: arxiv-2512-00601 — "For CRPO, the importance of accuracy coefficient k = 10"
[^c10]: arxiv-2512-00601 — "CRPO-trained models match or surpass GRPO in"
[^c11]: arxiv-2512-00601 — "strongest medical faithfulness across datasets"
[^c12]: arxiv-2512-00601 — "The base model we use is Qwen2.5-3B-Instruct"
[^c13]: arxiv-2512-00601 — "maintaining comfortable accuracy enhancements"
