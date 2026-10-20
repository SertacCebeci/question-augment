---
description: "Giving a planner the legal moves and its previous move removes the validity burden but not the planning one: moves stay valid, progress stalls, and no puzzle is solved."
aliases: ["external move validator", "valid-move oracle", "legal-move list condition", "validity offloading", "planning after validity is supplied"]
sources: ["arxiv-2511-21591"]
---
# Valid-move oracle planning residue

A language model asked to solve a sliding-tile puzzle has to do two things at once: keep an exact board, and choose moves that bring the board nearer the goal. Most failures in the 8-puzzle study are of the first kind, an invalid move. The paper names both deficits: "brittle internal state representations that lead to invalid moves and weak heuristic planning that results in loops."[^v11]

The validator condition removes the first burden on purpose. The model gets "a list of all valid moves and ask them to return the best one", plus its previous move to help it avoid immediate reversal.[^v1] An external function applies the chosen move, and "After applying the move, we update the puzzle state and move lists and re-query the model."[^v2] The model is no longer asked which moves are legal. What it still has to supply is the choice among them, which is the part that carries the goal.

## What the condition does and does not change

On the validity axis the condition works as designed. "The models no longer have to decide which moves are valid and which are not."[^v3] The failure profile moves away from invalid moves and toward repetition. Gemini-2.5-Pro and Llama 3.1 8B-Instruct were recorded "looping 92% and 86% of the time."[^v5] GPT-5-mini instead spent most runs making legal moves until the 50-move cap, with "its primary outcome was early termination (68%)."[^v9]

On the goal axis nothing improved. The paper's summary is blunt: "Despite this level of assistance, none of the models solve any puzzles in this setting."[^v4] Relative to the unassisted conditions the validator also lowered success, since "this intervention hurt performance, lowering the success rates of all models."[^v5b]

The paper measures progress with a Manhattan-distance heuristic, the summed distance of each tile from its goal cell. On that measure "the models made minimal progress toward the goal state despite making numerous valid moves."[^v6] The clearest case is GPT-5-mini: "GPT-5-mini made, on average, nearly forty-seven valid moves to achieve only about six moves of progress based on a Manhattan-distance heuristic."[^v7] The authors read this as a model that can track the state but "lacks a coherent long-term strategy, effectively wandering the state space without direction."[^v10]

## The residue

What survives the validator is the planning component taken alone: choosing, at each step, a legal move that lowers the distance to the goal over a horizon of tens of moves. The paper's stated aim is to isolate this component, to measure performance "when state tracking is no longer the bottleneck".[^v16] The condition shows that the component fails there too. That separation is the transferable part. A success rate measured with a legality oracle in place is not a measure of planning, and a gain from a legality check is not evidence that the model can direct a search.

My inference, not the paper's claim: the same separation would apply to any answerer that is handed a filter over its options. A filter can remove the illegal or malformed candidates. It does not supply the direction in which the answer should move. Whether that direction comes from the answerer's own search, from a structured search procedure, or from nowhere, the validator condition does not say.

## Limits

The study is one domain. "First, we examine only a single domain."[^v13] Whether the residue appears in other sequential tasks is not tested, though the authors suggest the 8-puzzle "may be representative of more challenging sequential planning tasks."[^v12]

The sample is small. The authors say "we evaluate the models on only 50 puzzles"[^v15] across four models. The zero successes are observed counts, not a bound on what a better planner would reach.

The validator design is one choice: a legal-move list plus the previous move, with a cap of 50 moves. Other scaffolds, such as full move history, explicit search bookkeeping, or a checker that rejects repeats, were not tested. The claim is about this condition, not about every way of supplying legality.

The progress measure is a distance heuristic, not the goal itself. A stall in Manhattan distance is evidence of weak progress, but the 50-move cap means a run that would have gained distance later was cut off. My inference: the text does not separate those two cases.

All runs used "a temperature of 1.0, and identical system prompts," so the loop and stall results are at one sampling setting.[^v14]

## Related

- [[tool-integrated-reasoning]] — the same split from the tool side: a code search also removes the planning from the model, which is why the 8-puzzle study excluded code.
- [[self-reinforcing-repetition-loop]] — a decoding-level account of loops; this condition shows loops that continue under an explicit no-repeat instruction.
- [[agentic-iteration-gap-under-localized-verifier-feedback]] — localized constraint feedback after an error lifts success on puzzles; here the checker removes a class of errors in advance and no puzzle is solved.
- [[round-trip-invertibility-consistency]] — another state-tracking failure in which self-critique plateaus.
- [[failure-mode-taxonomy]] — the termination classes used to sort these runs.

[^v1]: arxiv-2511-21591 — "we provide them with a list of all valid moves and ask them to return the best one"
[^v2]: arxiv-2511-21591 — "After applying the move, we update the puzzle state and move lists and re-query the model."
[^v3]: arxiv-2511-21591 — "The models no longer have to decide which moves are valid and which are not"
[^v4]: arxiv-2511-21591 — "Despite this level of assistance, none of the models solve any puzzles in this setting."
[^v5]: arxiv-2511-21591 — "looping 92% and 86% of the time"
[^v5b]: arxiv-2511-21591 — "this intervention hurt performance, lowering the success rates of all models"
[^v6]: arxiv-2511-21591 — "the models made minimal progress toward the goal state despite making numerous valid moves"
[^v7]: arxiv-2511-21591 — "GPT-5-mini made, on average, nearly forty-seven valid moves to achieve only about six moves of progress based on a Manhattan-distance heuristic"
[^v9]: arxiv-2511-21591 — "its primary outcome was early termination (68%)"
[^v10]: arxiv-2511-21591 — "lacks a coherent long-term strategy, effectively wandering the state space without direction"
[^v11]: arxiv-2511-21591 — "brittle internal state representations that lead to invalid moves and weak heuristic planning that results in loops"
[^v12]: arxiv-2511-21591 — "may be representative of more challenging sequential planning tasks"
[^v13]: arxiv-2511-21591 — "First, we examine only a single domain."
[^v14]: arxiv-2511-21591 — "a temperature of 1.0, and identical system prompts"
[^v15]: arxiv-2511-21591 — "we evaluate the models on only 50 puzzles"
[^v16]: arxiv-2511-21591 — "when state tracking is no longer the bottleneck"
