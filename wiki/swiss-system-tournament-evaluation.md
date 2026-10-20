---
description: "Pairing evaluated systems by current rating over a few rounds, never repeating a pair, cut the judged comparisons among eight RAG systems from 28 to 16 with the same final ranking as exhaustive play."
aliases: ["Swiss-system tournament", "Swiss tournament pairing", "Swiss-system ranking", "Swiss-system evaluation"]
sources: ["arxiv-2512-22629", "arxiv-2512-00617"]
---
# Swiss-system tournament evaluation

Ranking N systems by pairwise judgment in full round-robin needs every pair to meet once, which is N(N−1)/2 comparisons. A Swiss-system tournament keeps the number of rounds fixed and, in each round, pairs each system with an opponent of similar current standing, without repeating a pair. The pairings then depend on the results gathered so far, so the schedule adapts as the ranking forms.

In the DICE evaluation of retrieval-augmented generation (arxiv-2512-22629), the rule is stated directly: "Systems are initially assigned equal Elo ratings and paired dynamically each round based on current" performance estimates, "while avoiding repeat matches."[^c1] The pairing prefers close ratings: it "prioritizes systems with similar Elo scores to maximize information gain while maintaining competitive balance, thereby" preserving the ranking.[^c2] Each match is a set of questions, and its result is the cumulative soft score of the judge over those questions. "Elo ratings are updated after each match using cumulative soft win scores."[^c3] The per-question scores are the soft pairwise values of margin-gated-soft-pairwise-score, summed over the questions in a match, and the Elo update is weighted so that a lower-rated system beating a higher-rated one moves the ratings further. In the paper's words, "Weighted Elo updates incorporate rating differences and upset bonuses, amplifying K-factors when".[^c7]

## Mechanism and cost

With eight systems the schedule is four rounds of four matches each. That gives 16 comparisons, against 28 for the full round-robin, "representing a 42.9% reduction in computational cost."[^c4] The 42.9% is a count of judged comparisons. It is not a measured time or token cost, and it assumes each comparison costs the same. The tournament "was conducted over four rounds with four matches per round, totaling 16 comparisons".[^c8]

The paper's complexity claim is that the schedule reduces the cost from O(N²) to O(N log N) pairwise judgments. The reduction is stated for general N; the only case the paper runs is N = 8.

## Measured

The Swiss ranking was compared with the exhaustive one on the same eight configurations (a 2 × 2 × 2 design over embedding model, chunk size and generation model). "Validation against the exhaustive baseline (w/o Swiss) confirms identical rankings across all systems."[^c5] The authors also report that "the Swiss-system demonstrates minimal variance with shorter error bars than the exhaustive" approach.[^c6] The text I read does not say how the error bars were computed or over how many repetitions, so this claim rests on the authors' figure alone.

## Limits

- The O(N log N) scaling is an argument, not a measurement. One set of eight systems does not show how the number of rounds must grow with N, or whether the same identical ranking survives at larger N (my inference from the single test).
- The identical ranking is one run on one set of eight systems, judged by one reasoning model on 70 questions in one domain (Chinese financial QA). The paper names the single-domain setting as a limit of its evaluation.
- The text gives no numerical K-factor and no size for the upset bonus, so the Elo update cannot be reproduced from the text alone.
- A Swiss schedule commits to pairings from early results. If the judge is noisy in the first round, a system can be paired against the wrong opponents for the rest of the run. The paper does not test this (my inference). Whether the ranking is stable under a different judge or a different seed is also not reported in the text.
- Pairwise judges are exposed to position bias, and the paper names it as a weakness of pairwise evaluation generally: "remain vulnerable to position bias and inconsistent judgments".[^c9] The text I read reports no order-swapping control for the tournament's pair labels (see [[llm-judge-biases]]).
- The schedule has no stopping rule. It always plays the fixed number of rounds and then reports a rank, so two systems that are close in rating still receive a strict order. [[pairwise-confidence-adaptive-ranking]] addresses that case by stopping on confident adjacent pairs and reporting unresolved pairs as ties.

## Related

- [[prompt-tournament-evaluation]] — tournament-style comparison of prompts by humans, scored with Glicko2 and sampled adaptively toward the top two; a different pairing and rating scheme for the same kind of comparison
- [[pairwise-confidence-adaptive-ranking]] — stops on confident adjacent pairs and reports unresolved pairs as ties; the Swiss schedule has no such stop
- [[bradley-terry-preference-model]] — the batch model usually fitted to pairwise outcomes; Elo is a sequential update that approximates such a rating (my inference)
- [[llm-judge-biases]] — the position and verbosity effects that a pairwise tournament inherits from its judge
- margin-gated-soft-pairwise-score — the per-question score that feeds each match's Elo update
- rating-weighted-response-consensus — a different Elo tournament (arxiv-2512-00617) that scales K by the number of opponents in multi-agent matches, "This prevents excessive rating volatility when many agents"[^c10], and uses the ratings as vote weights rather than for pairing

[^c1]: arxiv-2512-22629 — "Systems are initially assigned equal Elo ratings and paired dynamically each round based on current"
[^c2]: arxiv-2512-22629 — "similar Elo scores to maximize information gain while maintaining competitive balance, thereby"
[^c3]: arxiv-2512-22629 — "Elo ratings are updated after each match using cumulative soft win scores."
[^c4]: arxiv-2512-22629 — "representing a 42.9% reduction in computational cost."
[^c5]: arxiv-2512-22629 — "Validation against the exhaustive baseline (w/o Swiss) confirms identical rankings across all systems."
[^c6]: arxiv-2512-22629 — "the Swiss-system demonstrates minimal variance with shorter error bars than the exhaustive"
[^c7]: arxiv-2512-22629 — "Weighted Elo updates incorporate rating differences and upset bonuses, amplifying K-factors when"
[^c8]: arxiv-2512-22629 — "The tournament was conducted over four rounds with four matches per round, totaling 16 comparisons"
[^c9]: arxiv-2512-22629 — "remain vulnerable to position bias and inconsistent judgments"
[^c10]: arxiv-2512-00617 — "This prevents excessive rating volatility when many agents"
