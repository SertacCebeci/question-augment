---
description: "On puzzles, letting a model move, receive localized constraint-violation feedback and correct itself lifts success far beyond one-shot answering, and is a distinct axis from reasoning effort."
aliases: ["agentic gap", "iterative verification gain", "agentic uplift"]
sources: ["arxiv-2603-02119", "arxiv-2512-12989", "arxiv-2512-01174", "arxiv-2511-21920", "doi-10-48550-arxiv-2606-01057"]
---
# Agentic iteration gap under localized verifier feedback

In Pencil Puzzle Bench, each puzzle variety has an ordered constraint set; local rules are checked before global ones, and a broken direct constraint returns error feedback that names the rule and highlights the offending cells.[^c1] In agentic mode the model makes moves, checks the board, and course-corrects over many turns, whereas in direct-ask mode it answers once.[^c2]

## What was measured

Models with weak one-shot performance benefit disproportionately: Claude Opus 4.6 at default effort (no extended thinking) scored 0.3% direct-ask and 30.0% agentic.[^c3] GPT-5.2 at xhigh effort rose from 27.0% direct to 56.0% agentic, and the agentic score grew steadily with effort level (0.00%, 10.0%, 23.3%, 36.7%, 56.0% from none to xhigh).[^c4]

The gap shrinks but persists when the model already reasons internally. The paper reports that it ranges "from ++4.8pp for models with strong reasoning to ++30.0pp for models without", and reads reasoning depth and agentic iteration as two distinct axes.[^c5] Iteration also unlocked varieties that no model solved one-shot: all 20 varieties were solved at least once after the expanded agentic runs.[^c6]

Mechanism, as the authors frame it: feedback says what went wrong and where, not merely that something is wrong, so each turn gives the solver a targeted correction signal.[^c7] My own inference: the gain therefore depends on the verifier being localized and deterministic; it is not shown to transfer to settings where feedback is vague or itself fallible.

## Limits

- Agentic runs used a 30-puzzle baseline over 4 varieties (extended to 60 puzzles only for three models), much smaller than the 300-puzzle direct evaluation; uplifts compare different puzzle subsets in places.
- Infrastructure error rates were large (for example 27.8% to 50.0% of attempts), which can bias agentic success rates and differs across models.[^c8]
- Higher effort was not monotonic: Opus 4.6 at default effort beat Opus 4.6@max (30.0% vs 23.3%).[^c9]
- Strategies were baselines without prompt engineering; the causal share of feedback versus simply more compute (many turns) was not separated.
- Puzzles have exact, formal rules; whether open-ended questions with no deterministic checker gain similarly is untested.
- Access is not delivery. In a coding migration with a deterministic external checker, offering the checker as an optional action did not raise the full-pass rate in any of four paired comparisons.[^c10] The paper tests optional access, not required feedback, so it does not show how much a delivered diagnostic would have helped.[^c11] A diagnostic followed by an edit is also not repair: "receiving diagnostics and making subsequent edits is insufficient evidence that the reported defect was repaired."[^c12]
- Repair is uneven by error class. In a drawing benchmark with one feedback turn, rule-named feedback cut syntax errors by 100% and coordinate errors by 75%,[^c13] logic errors by 67%,[^c14] and efficiency warnings least, at 33%.[^c15] The mean gain is small for a related reason: 71.2% of tasks already scored perfectly on the first turn and skipped the second,[^c16] so the average gain of +3.2% rests on the 28.8% that improved.[^c17] My inference is that a localized checker helps most where the error is a missing or malformed item, and least where the fix needs a changed plan. The drawing task is not a puzzle, and the two settings are not pooled here.

- Repair driven by runtime errors shows the same unevenness on code. The loop only receives what the runtime reports: "error messages and append them to the original prompt."[^c18] On MRI datasets the repair mechanism "yielded little to no improvement," because the failures were "deeply embedded logic or domain-specific processing issues," while simpler tabular data needed few rounds.[^c19] A script that runs and is wrong produces no runtime signal; the paper's own classes separate it as "runnable but incorrect."[^c20] Whether a localized checker would reach that class is not tested there.
- The procedural 3D benchmark measures the same split on meshes. Across 11 models on two tracks, multi-turn error feedback raised aggregate executability from 0.702 to 0.974.[^c21] About 90% of baseline failures were one family: "Blender 5.0 API mismatches, which are localized and copy-pasteable as fixes once the traceback" was visible.[^c22] Shape quality did not follow evenly: "Chamfer and Uni3D show a clear capacity split," and for the Gemini Flash-class and Gemma models the recovered meshes showed "near-zero 3D-shape deltas despite large executability gains."[^c23][^c24] A coding-agent harness raised executability "0.747 to 0.973, a +22.6 pp gain," yet on instances both columns solve the paper finds it does not yield "semantically richer or more shape-accurate geometry once a script compiles."[^c25][^c26] My inference: a localized runtime error repairs the interface the compiler checks; whether the compiled geometry is right is a separate question. That is the "runnable but incorrect" class above, now on meshes rather than assertions. Not tested: whether the shape gap closes with a checker that inspects geometry rather than the traceback.

## Related

- [[process-outcome-consistency-verification]] — verifying process steps, not only final outcomes
- [[stage-specific-elicitation]] — feedback loops placed at each decision stage rather than only at the end
- [[multi-agent-process-verification-unreliability]] — process verification when the verifier is itself unreliable, the contrast to a deterministic checker
- [[independent-implementation-check]] — the external checker in the coding case; there, its availability to the agent did not raise completion
- [[explicit-verifiable-criteria]] — the same drawing benchmark on the prompt side: conditions the checker tests, when stated in the prompt, were met more reliably

[^c1]: arxiv-2603-02119 — "When a direct constraint is broken, the engine provides immediate, localizable error feedback including"
[^c2]: arxiv-2603-02119 — "The agentic strategy, where models iteratively make moves, check the board for constraint violations,"
[^c3]: arxiv-2603-02119 — "only 0.3% direct-ask performance (+30.0 percentage points on the 30 puzzles evaluated in both"
[^c4]: arxiv-2603-02119 — "gains +35.7pp from agentic iteration (20.2% → 56.0% on the same 84 puzzles)."
[^c5]: arxiv-2603-02119 — "reasoning depth and agentic iteration are two distinct axes of capability"
[^c6]: arxiv-2603-02119 — "solved 3 previously unsolved varieties; all 20 varieties have now been solved at least once."
[^c7]: arxiv-2603-02119 — "targeted feedback about what went wrong, not just that something is wrong."
[^c8]: arxiv-2603-02119 — "Infrastructure error rates (timeouts,"
[^c9]: arxiv-2603-02119 — "at default effort (high) outperforms Opus 4.6@max (30.0% vs 23.3% on the baseline 30-puzzle set)."
[^c10]: arxiv-2512-12989 — "Checker access does not increase the observed full-pass rate in any comparison"
[^c11]: arxiv-2512-12989 — "This result concerns optional access, not the effect of requiring a check or a repair."
[^c12]: arxiv-2512-12989 — "receiving diagnostics and making subsequent edits is insufficient evidence that the reported defect was repaired"
[^c13]: arxiv-2512-01174 — "SYNTAX ERROR (100% reduction) and COORDINATE ERROR (75% reduction) respond effectively to"
[^c14]: arxiv-2512-01174 — "LOGIC ERROR reduction (67%)"
[^c15]: arxiv-2512-01174 — "EFFICIENCY WARNING showed the lowest reduction"
[^c16]: arxiv-2512-01174 — "of tasks achieved perfect scores on Turn 1 (early stopping),"
[^c17]: arxiv-2512-01174 — "28.8% showed measurable improvement through feedback,"
[^c18]: arxiv-2511-21920 — "error messages and append them to the original prompt"
[^c19]: arxiv-2511-21920 — "yielded little to no improvement"
[^c20]: arxiv-2511-21920 — "where it executes without errors but generates"
[^c21]: doi-10-48550-arxiv-2606-01057 — "increases from 0.702 (single-turn) to 0.974 (multi-turn), representing a +27.2 pp"
[^c22]: doi-10-48550-arxiv-2606-01057 — "are Blender 5.0 API mismatches, which are localized and copy-pasteable as fixes once the traceback"
[^c23]: doi-10-48550-arxiv-2606-01057 — "Chamfer and Uni3D show a clear capacity split"
[^c24]: doi-10-48550-arxiv-2606-01057 — "near-zero 3D-shape deltas despite large executability gains."
[^c25]: doi-10-48550-arxiv-2606-01057 — "0.747 to 0.973, a +22.6 pp gain comparable to the stateless retry of Finding 4"
[^c26]: doi-10-48550-arxiv-2606-01057 — "semantically richer or more shape-accurate geometry once a script compiles."
