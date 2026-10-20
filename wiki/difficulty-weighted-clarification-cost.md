---
description: "Charge each clarifying question by its cognitive difficulty and pass the weighted sum through a logarithm, so burden climbs steeply for the first questions and flattens for later ones."
aliases: ["diminishing clarification burden", "log-normalized clarification cost", "question-difficulty clarification penalty"]
sources: ["arxiv-2512-06196"]
---
# Difficulty-weighted clarification cost

When a system asks a person questions before it acts, the cost of asking belongs in the objective, or the system will ask without limit. The paper gives one concrete way to count it. Each clarifying question is classed as easy, medium or hard by a fixed prompt, and the cost is a logarithm of a weighted count, normalized by the logarithm of 16. In the form the text gives, with the weights as printed, the count is 0.1 per easy question, 0.5 per medium and 1 per hard one, and the cost is the log of one plus that count, divided by log 16.

The logarithm is the part that changes how questions are priced. The paper says the normalization is there "to model diminishing burden".[^c1] Under the formula, the increment of cost from one more question shrinks as the count grows, so the first few clarifications are expensive and later ones add less. The weights make difficulty matter: from the formula, ten easy questions sum to the same weight as one hard question. This is my arithmetic from the printed constants, not a result the paper states.

The cost is one term in a manager's reward. The manager is asked to maximize stakeholder utility while "minimizing clarification and revision costs", so the penalty is traded against the quality of the output it helps produce.[^c2] The stated purpose is that the penalty "discourages excessive or complex clarifications while tolerating minor ones".[^c3] The paper also reports the size of the penalty directly: "one clarification incurred roughly an 18% reward penalty, five clarifications 42%, and ten clarifications 60%."[^c4] These are the authors' figures; I did not reconstruct them from the formula, because they depend on the weighting coefficient and the reward scale, which are set in an appendix I did not read.

## Limits

- The difficulty classes are assigned by a language model prompted with criteria: the classification uses "a fixed LLM prompt specifying criteria for easy, medium, and hard".[^c5] The burden is therefore a model's judgment of what a person would find hard, not a measured human effort.
- The cost is meant to measure "the stakeholder's cognitive burden", and the paper describes that burden as the number or complexity of feedback turns.[^c6] No measurement against real people is reported in the text read.
- The weights 0.1, 0.5 and 1 and the base 16 are the authors' choices. No sensitivity check on them appears in the sections read.
- The cost is a fixed penalty. It is not weighed against the information the questions bought, so it cannot say when a question pays for itself. A value-based account asks that question directly; see [[elicitation-burden-tradeoff]], where each query carries a flat cost and the optimal count is set by expected mismatch.
- The logarithm bounds the penalty for long dialogues only in the sense that its increments shrink. A very long clarification still adds cost, and the paper's reported figures cover up to ten questions.

## Related

- [[elicitation-burden-tradeoff]] — the optimal number of questions weighs a flat per-query cost against expected mismatch; here the cost is difficulty-weighted and concave, and the benefit is not part of the objective.
- [[threshold-optimality-of-clarification]] — a clarification is worth asking when its interaction cost falls below the drop in epistemic risk it buys; this note gives one concrete form of that cost term.
- [[question-type-cost-mining]] — prices questions by their kind through interaction costs, a different way of assigning cost to the same act.
- [[ordinal-proxy-alignment]] — the rubric objective from the same paper, which the clarification cost feeds into when it decides how many questions a rubric needs.

[^c1]: arxiv-2512-06196 — "following a logarithmic normalization to model diminishing burden"
[^c2]: arxiv-2512-06196 — "minimizing clarification and revision costs"
[^c3]: arxiv-2512-06196 — "This discourages excessive or complex clarifications while tolerating minor ones."
[^c4]: arxiv-2512-06196 — "one clarification incurred roughly an 18% reward penalty, five clarifications 42%, and ten clarifications 60%"
[^c5]: arxiv-2512-06196 — "LLM prompt specifying criteria for easy, medium, and hard"
[^c6]: arxiv-2512-06196 — "measures the stakeholder’s cognitive burden"
