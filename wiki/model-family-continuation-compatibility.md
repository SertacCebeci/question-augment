---
description: "Finishing another model's cut-off reasoning chain works better within a model family; the paper credits family match, yet receiver strength orders the same results."
aliases: ["cross-family continuation", "intra-family continuation", "reasoning chain interchangeability", "midstream model handoff", "representational compatibility of reasoning"]
sources: ["arxiv-2512-20647"]
---
# Model-family continuation compatibility

Take a chain of reasoning one model wrote, cut it at some point, and let a second model finish it. Whether the finished chain is still right depends on the pair. The question is whether a partially completed chain "from one model can be reliably continued by another model, either within the same model family or across families."[^c1] The cut points come from cumulative token log-probability: the chain is recorded with token log-probabilities, "to guide strategic truncation at 25%, 50%, and" 75% of the cumulative total, giving early, mid and late prefixes.[^c2] Each prefix is continued by a second model, and the complete chain is scored by final-answer accuracy and by a process reward model.

The continuers are chosen so that one is a smaller model from the base's own family and the other is from a different lineage. Gemma-3-1B-IT is "used to evaluate how well reasoning chains can be completed by a structurally" similar but smaller model.[^c3] LLaMA-3.1-8B-Instruct is "representing a different architectural lineage" for the Gemma base, and it is the same-family continuer for the LLaMA-70B base.[^c4] Two metrics compare a hybrid chain with its base: NRG, a normalized gain in accuracy, and XMD, which "provides a normalized measure of reasoning incompatibility".[^c5]

## What was measured

On MATH, the intra-family pairing improves with later cuts. In the paper's words, "intra-family continuations show steady improvement with longer truncation depths."[^c6] For the LLaMA-70B base, the same-family LLaMA-8B rises from 42.18% to 50.06% across the three cuts, while cross-family Gemma-1B gains less, from 36.16% to 41.98%.[^c7] The cross-family pairing is the one that looks worst in the paper's summary, and its explanation is representational.

## The mechanism the paper proposes

The paper says that "each model family tends to rely more on its own reasoning patterns", and that differences between families may "hinder smooth continuation across families."[^c8] Its summary is that "compatibility between base and continuation models remains the key factor determining success."[^c9]

The idea that survives this reading is that a chain carries the habits of its writer, and a continuer that shares them picks it up with less loss. The paper does not measure representations or styles. The mechanism is its hypothesis, and I take it as untested (my inference).

## Limits

- **Receiver strength orders the same results.** Full-chain accuracy of the two continuers in Table 1 is 36.28% for Gemma-3-1B-IT.[^c10] The text says the two continuation models "perform comparably."[^c11] Table 1 does not show that: LLaMA-3.1-8B-Instruct is the stronger receiver alone. On my reading of Tables 2 and 3, LLaMA-8B has higher accuracy, higher PRM score and lower XMD than Gemma-1B at every cut in both tables. The family pairing flips between the two tables, but the winner does not. Family and capacity are the same contrast in this design, and the paper concedes that capacity matters: effective interoperability "depends on both model capability and the degree of representational and contextual" alignment.[^c12]
- **The family effect is not uniform on the paper's own metrics.** With the Gemma base, the cross-family LLaMA-8B "exhibits a greater net gain of" 43.60% to 63.80%, against 41.76% to 55.26% for the intra-family Gemma-1B.[^c13] Its NRG is lower, and the paper notes that it "shows slightly lower NRG".[^c14] So "cross-family continuation fails" holds for one base and one metric, not as a general claim. The conclusion that "alignment plays a decisive role in the success or failure of such hybrid chains" is stronger than these tables support.[^c15]
- **The baseline is inconsistent.** The text gives "Gemma 3-1B-IT and Gemma 3-4B-IT performed with accuracies of 48.0%," while Table 1 gives 36.28% for Gemma-1B.[^c16] NRG is computed against the base chain, so the figure used matters.
- **Context overhead is attributed, not tested.** The paper says that "this bottleneck is attributed to the finite" working memory of LLMs, citing prior work. Nothing here measures memory or context load.[^c17]
- **Sampling is unclear.** The method says that "each continuation model generates a single completion for each prefix using a" temperature of 0.7.[^c18] The limitations say "All experiments were conducted using deterministic continuations."[^c19] Either way there is one completion per prefix and no variance is reported.
- **Scope is narrow.** "Our evaluation is confined to math reasoning (MATH)."[^c20] The PRM is one math-specific model, "We adopt Qwen2.5-PRM" as the primary PRM, so every PRM score rests on one judge.[^c21] The design has two base chains, two continuers and one benchmark.
- **Truncation depth is not a cure.** "These observations highlight that truncation depth alone does not ensure effective reasoning transfer."[^c22] XMD stays non-negligible even at the 75% cut.

## Related

- [[cross-model-cot-prefix-transfer]] — the same channel, a trace handed to another model as a prefix, but there the question is where the correct answer first becomes visible in the prefix; here it is whether the pairing keeps the chain correct.
- [[thinker-executor-cot-reusability-verifiability]] — handing a whole CoT to other models, where reusability and verifiability rank models differently from accuracy; this note concerns cut prefixes and the pairing.
- [[cot-reasoning-faithfulness-by-truncation]] — truncation as a probe of whether a rationale is used; here the cut is a handoff point, not a faithfulness test.
- [[model-orchestration]] — routing phases of a task to different models; the paper's suggested pattern, reserving a high-capacity model for uncertain steps, runs into the pairing limit above.

[^c1]: arxiv-2512-20647 — "whether a partially completed reasoning chain from one model can be reliably"
[^c2]: arxiv-2512-20647 — "recording token-level log-probabilities to guide strategic truncation at 25%, 50%, and"
[^c3]: arxiv-2512-20647 — "is used to evaluate how well reasoning chains can be completed by a structurally"
[^c4]: arxiv-2512-20647 — "representing a different architectural lineage"
[^c5]: arxiv-2512-20647 — "XMD provides a normalized measure of reasoning incompatibility"
[^c6]: arxiv-2512-20647 — "In contrast, intra-family continuations show steady improvement with longer truncation depths."
[^c7]: arxiv-2512-20647 — "rising only +7.9 pp"
[^c8]: arxiv-2512-20647 — "each model family tends to rely more on its own reasoning patterns"
[^c9]: arxiv-2512-20647 — "compatibility between base and continuation models remains the key factor determining success."
[^c10]: arxiv-2512-20647 — "36.28%"
[^c11]: arxiv-2512-20647 — "perform comparably."
[^c12]: arxiv-2512-20647 — "depends on both model capability and the degree of representational and contextual"
[^c13]: arxiv-2512-20647 — "exhibits a greater net gain of"
[^c14]: arxiv-2512-20647 — "but shows slightly lower NRG"
[^c15]: arxiv-2512-20647 — "alignment plays a decisive role in the success or failure of such hybrid chains."
[^c16]: arxiv-2512-20647 — "Gemma 3-1B-IT and Gemma 3-4B-IT performed with accuracies of 48.0%"
[^c17]: arxiv-2512-20647 — "This bottleneck is attributed to the finite"
[^c18]: arxiv-2512-20647 — "Each continuation model generates a single completion for each prefix using a"
[^c19]: arxiv-2512-20647 — "All experiments were conducted using deterministic continuations."
[^c20]: arxiv-2512-20647 — "Our evaluation is confined to math reasoning (MATH)."
[^c21]: arxiv-2512-20647 — "We adopt Qwen2.5-PRM"
[^c22]: arxiv-2512-20647 — "These observations highlight that truncation depth alone does not ensure effective reasoning transfer."
