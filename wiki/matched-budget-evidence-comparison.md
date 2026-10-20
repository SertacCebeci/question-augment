---
description: "Whether raw dialogue or a structured packet wins depends on the text budget: full raw leads, but at a matched word budget a resolved packet beats recency-truncated raw by 42–73 points."
aliases: ["budget-matched comparison", "word-budget control", "matched-budget control", "recency truncation baseline", "token-matched baseline"]
sources: ["doi-10-48550-arxiv-2608-23568"]
---
# Matched-budget evidence comparison

Two ways of giving a model evidence cannot be ranked without fixing how much text each may use. In memory QA the ranking can flip with the budget. The work shows this on the same 500 LongMemEval questions and nine models. At full length, the raw conversation is the strong baseline: "It outperforms budgeted formal packets on every" model.[^m5] Once the budget is tight, the ranking reverses.

The control truncates the raw conversation "to about 800 words, keeping the most recent turns," and compares it with a streamlined resolved packet on the same questions.[^m10] Truncated raw "scores only 7.6–12.0%, while streamlined" packets score 50.0–82.0%.[^m3] The packet leads "by 42.4–72.6 points on every model."[^m1] The gap is measured in matched word budgets, not in token counts.[^m11]

## Why the budget decides the ordering

The work's reading is that the budget is not neutral with respect to content. A recency cut keeps the last turns and discards the rest, so "truncation often drops earlier answer-bearing turns,"[^m4] and the model never sees the evidence it needs. A resolved packet "preserves the value regardless" of where it sat in the dialogue.[^m9] The work states the consequence directly: "The result is not that structure is intrinsically better than raw dialogue."[^m6]

The mechanism the text supports is therefore one of loss under truncation, not one of format. Full raw conversation has no truncation loss, which is why it leads at full length. The reversal appears only when the budget removes the answer-bearing turns. (My inference: a recency window is a poor baseline for any budget, because it is chosen by position, not by what answers the question.)

## Limits

- Word counts stand in for tokens. The work calls its tokenmatched baseline "a proxy for token-budget matching," and says a provider tokenizer would be a tighter control.[^m7]
- The control does not separate localization from rendering. "The budgeted comparison therefore does not isolate oracle evidence localization" from the surface form.[^m8] An oracle raw excerpt, which would isolate localization, was not run.
- The 42–73 point gap is an advantage over one truncation rule, the most recent words. It does not show that structured evidence beats every raw excerpt at the same budget. A raw baseline truncated to the answer-bearing turns could close much of the gap, and the work did not test that.
- The packet in this comparison is a resolved current-state value, which is short by design. The result does not say that any compressed memory beats any raw record.
- One benchmark family and nine commercial models were tested. Whether the reversal holds on other memory benchmarks is not established by this control alone.

## Related

- [[reader-facing-evidence-rendering]] — the broader claim that the artifact moves accuracy; this note is the budget control inside that claim.
- [[compressed-memory-versus-raw-retrieval]] — the raw-versus-compressed question on behavior logs, where a budget confound was flagged and left open.
- [[effective-context-length]] — the context size at which a model stops using what it is given; a word budget is a context size, so the two interact.

[^m1]: doi-10-48550-arxiv-2608-23568 — "dialogue by 42.4–72.6 points on every model."
[^m3]: doi-10-48550-arxiv-2608-23568 — "truncated raw conversation scores only 7.6–12.0%, while streamlined"
[^m4]: doi-10-48550-arxiv-2608-23568 — "truncation often drops earlier answer-bearing turns,"
[^m5]: doi-10-48550-arxiv-2608-23568 — "It outperforms budgeted formal packets on every"
[^m6]: doi-10-48550-arxiv-2608-23568 — "is not that structure is intrinsically better than raw"
[^m7]: doi-10-48550-arxiv-2608-23568 — "proxy for token-budget matching"
[^m8]: doi-10-48550-arxiv-2608-23568 — "The budgeted comparison therefore does not isolate oracle evidence localization"
[^m9]: doi-10-48550-arxiv-2608-23568 — "whereas resolved P2 preserves the value regardless"
[^m10]: doi-10-48550-arxiv-2608-23568 — "we truncate raw conversation to about 800 words, keeping the most recent turns"
[^m11]: doi-10-48550-arxiv-2608-23568 — "matched word budgets, streamlined resolved-P2"
