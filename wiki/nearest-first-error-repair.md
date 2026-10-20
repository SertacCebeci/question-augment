---
description: "Repair a failed generation by searching outward from it along edits licensed by the error type, returning the nearest candidate the checker accepts, instead of regenerating the whole output."
aliases: ["search-based refinement", "SafeQL-style refinement", "error-directed refinement search", "best-first repair to executable"]
sources: ["doi-10-14778-3819518-3819545"]
---
# Nearest-first error repair

A generation that fails the system's own check need not be thrown away. The repair treats the failed output as the starting point of a search, and the error report says which component may change. In the Text-to-SQL case, "an unknown relation error is typically resolved by replacing the relation in the FROM clause".[^c1] The search applies only the substitutions that this error type licenses, and it expands candidates in order of distance from the original query, not in order of how plausible a fresh generation would be.[^c2] The first candidate the checker accepts is returned. In SafeQL the checker is the database engine itself, the substitutions are SQL edits, and the distance combines a "semantic distance metric that combines structural similarity and embedding-based relevance".[^c3] Because the queue is ordered by that distance and the first success ends the search, "the first valid query discovered is the one most semantically similar to the original input."[^c4]

Three things separate this from a regeneration loop. First, the error narrows the search, so the valid parts of the first output are kept; the stated aim is "while preserving all valid fragments of the original logic".[^c5] Second, the search keeps a queue and does not revisit states: a refinement is "enqueued for future exploration only if it has not been visited previously", so work on one branch is not repeated on another.[^c6] Third, type analysis inside the database removes substitutions before they are run: the method "incorporates type-based pruning, which eliminates type-inconsistent" substitutions.[^c7]

The reported effects are the authors' own. Search alone "resolves a large fraction of errors with no token overhead", and on Bird it leaves "leaving only 13%–17% of erroneous queries to proceed to" the regeneration fallback.[^c8] Measured against regeneration baselines, the hybrid "enables SafeQL to reach valid queries with 1.8–15.1× fewer tokens".[^c9] These numbers are execution accuracy and token counts against gold results. They say the repair is cheaper and reaches executable queries more often; they do not say the repaired query is the one the asker meant.

The transfer to other outputs is conditional. The mechanism needs a checker that names an error type, and a grammar that says which edits that type licenses. Where a generation has no such checker, the distance ordering has no signal to follow (my inference, not the paper's claim).

## Limits

- **The nearest query is nearest to the first query, not to the asker.** The reference point is taken "under the assumption that it reflects the LLM’s interpretation of the user’s intent".[^c10] If the first output misreads the question, the search returns the nearest executable version of the misreading. The paper's distance is "while remaining a heuristic rather than a strict notion of semantic equivalence".[^c11]
- **Search does not replace regeneration.** The paper concedes that "When this initial query is fundamentally misgenerated, search-based refinement alone is insufficient".[^c12] The hybrid design hands such cases back to an LLM that regenerates. The gain over regeneration is therefore in the common case of a near-miss; for a badly wrong first output the search alone does not help.
- **The error type licenses a coarse set of edits.** The paper's own example shows that "identical error messages Error: unknown attribute may correspond to different underlying causes".[^c13] A search that trusts the error type can explore substitutions at the wrong component, and the pruning and the distance are the only guards against that.
- **Parameters trade accuracy against latency.** The structure–embedding weight and the top-K pruning are tuned on a benchmark; the paper reports that "However, this also introduces a trade-off: mid-range values" of the weight do best, while larger values favour speed.[^c14]
- **Scope.** The method was tested on two Text-to-SQL benchmarks, Bird and Spider. The full-dev comparison is reported "using GPT-OSS-120B", a single model, so the spread across models is not established by that table.[^c15] Other structured outputs were not tested. The "up to 5.8%" and "15×" headline figures are the paper's maxima across settings, not typical values.
- **Anchoring is not ruled out by this result.** A related finding is that conditioning a small code model on its own failed attempt can cost accuracy relative to fresh resampling ([[self-repair-anchoring]]). Nearest-first repair anchors on the first output by design. The two have not been tested on the same task, so whether the anchoring penalty applies to a search that edits only the error-named component is open (my inference).

## Related

- [[self-repair-anchoring]] — the opposite bet on retry: a retry conditioned on the model's own failed attempt lost accuracy to blind resampling below 7B; nearest-first repair anchors on the first output on purpose, and the two were not tested together
- [[sigma-triage-regenerate-or-abstain]] — the regeneration side of the same choice, where a failed candidate is regenerated with constraint feedback or abstained on
- [[execution-verified-preference-pairs]] — the same kind of execution check used as a label for training rather than as a repair signal at inference
- [[minimal-patch-edit-label]] — a minimal repair used as the label a span is scored against; here the minimal repair is performed to produce the answer

[^c1]: doi-10-14778-3819518-3819545 — "an unknown relation error is typically resolved by replacing the relation in the FROM clause"
[^c2]: doi-10-14778-3819518-3819545 — "The search initializes a priority queue ordered by semantic distance from the LLM-generated initial query, expanding the closest candidates first."
[^c3]: doi-10-14778-3819518-3819545 — "semantic distance metric that combines structural similarity and embedding-based relevance"
[^c4]: doi-10-14778-3819518-3819545 — "thus guaranteeing that the first valid query discovered is the one most semantically similar to the original input."
[^c5]: doi-10-14778-3819518-3819545 — "while preserving all valid fragments of the original logic"
[^c6]: doi-10-14778-3819518-3819545 — "enqueued for future exploration only if it has not been visited previously"
[^c7]: doi-10-14778-3819518-3819545 — "incorporates type-based pruning, which eliminates type-inconsistent"
[^c8]: doi-10-14778-3819518-3819545 — "resolves a large fraction of errors with no token overhead"
[^c9]: doi-10-14778-3819518-3819545 — "leaving only 13%–17% of erroneous queries to proceed to"
[^c10]: doi-10-14778-3819518-3819545 — "the reference point under the assumption that it reflects the LLM’s interpretation of the user’s intent"
[^c11]: doi-10-14778-3819518-3819545 — "while remaining a heuristic rather than a strict notion of semantic equivalence"
[^c12]: doi-10-14778-3819518-3819545 — "When this initial query is fundamentally misgenerated, search-based refinement alone is insufficient"
[^c13]: doi-10-14778-3819518-3819545 — "identical error messages Error: unknown attribute may correspond to different underlying causes"
[^c14]: doi-10-14778-3819518-3819545 — "However, this also introduces a trade-off: mid-range values"
[^c15]: doi-10-14778-3819518-3819545 — "Comparison on the Bird full dev benchmark using GPT-OSS-120B"
