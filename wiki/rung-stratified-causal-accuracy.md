---
description: "Reporting causal accuracy per rung of Pearl's ladder, and per query type, can show brittleness the aggregate hides; in one 8B model the rung differences were small and not tested as such."
aliases: ["rung-level causal accuracy", "level-specific causal evaluation", "causal ladder stratification"]
sources: ["arxiv-2512-13725", "arxiv-2511-22854"]
---
# Rung-stratified causal accuracy

Pearl's causal ladder sorts causal questions into three levels, which the work names association, intervention and counterfactual inference; the framework is said to "distinguish three qualitatively different forms of reasoning".[^c1] A causal benchmark can be sorted along the same levels. A model is then scored once per level, and within a level once per query type, instead of with one pooled number. The work builds such a set from CLadder: "1000 samples per rung (R1, R2, R3),"[^c2] with query types spread roughly evenly inside each rung. Its stated reason is that "This rung-aligned evaluation avoids collapsing performance into a single aggregate score".[^c3]

What the stratification showed, for Llama-3-8B read at BF16, INT8 and NF4, is a difference in spread rather than in level. Across the three precision modes, Rung 2 had the largest variance in accuracy, σ² = 1.1×10⁻³, against 2.0×10⁻⁴ for Rung 1 and 4.2×10⁻⁴ for Rung 3.[^c4] The work states that intervention is the most compression-sensitive level "even when absolute accuracy differences remain small".[^c5] At the level of query type, the pattern is sharper in one direction: backdoor adjustment, collider bias and deterministic counterfactuals stayed flat across precisions, while the compositional types (NIE, ETT, explanation-away) showed mild sensitivity.[^c6] The work's conclusion is that "quantization-induced effects are uneven across causal operations and may be obscured" by a single score.[^c7]

The mechanism the work offers is its own reading, not something it measured: intervention and nested queries require more composed internal computation, so a small perturbation would reach them first. The stratification itself is what makes such a reading possible to check, because a pooled accuracy has no place to show a rung-specific spread. In the paper's words, "These results underscore the importance of rung-level evaluation: aggregate causal accuracy alone can mask structured" sensitivity.[^c8]

Rung differences are not always small. In a different setting, two 32B reasoning models answered the full CLadder set before and after a debate, and the rung breakdown was large: "Rung 3 questions were associated with a significant drop in accuracy" relative to the other two rungs, and the same questions "benefited the most from the debate in both model".[^c13][^c14] Those gains were 8.82 points for Qwen3 and 12.10 for DeepSeek-R1 on rung 3. This measures a difference in level across rungs, not the spread across precision settings reported above, so the two results do not conflict; they answer different questions.

## Limits

The differences are small. "Across all precision settings, causal accuracy remains stable, with differences below 0.5%."[^c9] The comparison of rungs is a comparison of three variances over three precision points. The work reports that the bootstrap intervals overlap across precisions, and reads that as "statistically unchanged under quantization",[^c10] but it reports no test of whether Rung 2's spread is larger than Rung 1's or Rung 3's. Per-type intervals are not given in the text read, so the query-type ranking has no stated uncertainty.

Overall accuracy in the zero-shot table sits between 0.508 and 0.512 for every precision. The text does not state the answer format of the CLadder items. If they are yes/no, that is chance level, and stratifying chance-level answers can reveal little about where competence sits (my inference, not the work's claim).

The measurement is one model, zero-shot, decoded greedily: "All evaluations use greedy decoding to eliminate stochastic variance."[^c11] Whether the same rung ordering holds in other models is not shown; the work says "Larger-scale models may exhibit different robustness or drift".[^c12]

## Related

- [[quantization-causal-drift]] — the precision comparison that this stratification was applied to; the drift is read per rung here.
- [[rung-mismatch-in-interpretability-claims]] — also uses Pearl's ladder, but to check whether a claim about a model matches the rung of its evidence; here the ladder sorts a model's answers, not the claims made about it.

[^c1]: arxiv-2512-13725 — "distinguish three qualitatively different forms of reasoning"
[^c2]: arxiv-2512-13725 — "1000 samples per rung (R1, R2, R3),"
[^c3]: arxiv-2512-13725 — "This rung-aligned evaluation avoids collapsing performance into a single aggregate score"
[^c4]: arxiv-2512-13725 — "Rung 2 (intervention) exhibits the highest variance in accuracy"
[^c5]: arxiv-2512-13725 — "even when absolute accuracy differences remain small."
[^c6]: arxiv-2512-13725 — "Backdoor adjustment, collider bias, and deterministic counterfactual queries exhibit high robustness across all precision modes."
[^c7]: arxiv-2512-13725 — "quantization-induced effects are uneven across causal operations and may be obscured"
[^c8]: arxiv-2512-13725 — "These results underscore the importance of rung-level evaluation: aggregate causal accuracy alone can mask structured"
[^c9]: arxiv-2512-13725 — "Across all precision settings, causal accuracy remains stable, with differences below 0.5%."
[^c10]: arxiv-2512-13725 — "This overlap indicates that causal accuracy is statistically unchanged under quantization at the 8B scale."
[^c11]: arxiv-2512-13725 — "All evaluations use greedy decoding to eliminate stochastic variance."
[^c12]: arxiv-2512-13725 — "Larger-scale models may exhibit different robustness or drift"
[^c13]: arxiv-2511-22854 — "Rung 3 questions were associated with a significant drop in accuracy"
[^c14]: arxiv-2511-22854 — "benefited the most from the debate in both model"
