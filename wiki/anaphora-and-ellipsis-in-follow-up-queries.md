---
description: "A follow-up question leaves out content in two ways: anaphora points back to an earlier referent, ellipsis drops words the earlier turns supply; both must be restored before retrieval."
aliases: ["anaphora and ellipsis", "context-dependent follow-up", "conversational anaphora and ellipsis"]
sources: ["doi-10-71781-36302"]
---
# Anaphora and ellipsis in follow-up queries

A follow-up question in a conversation is incomplete in one of two linguistic ways. The thesis names both as the phenomena a conversational search system has to handle: such a system "usually needs to address two key semantic phenomena: anaphora and ellipsis".[^c1]

Anaphora is the first. "Anaphora occurs when the semantics of an expression depend on the preceding context".[^c2] The thesis's example is a second query that asks for "its famous scholars", where the pronoun has no meaning of its own and must be resolved to the topic of the first query.[^c3]

Ellipsis is the second. "ellipsis involves the omission of semantic elements that are understood from prior" discourse.[^c8] The thesis's example is a third query, "And the one on computer vision", which "is completely missing the verb and the core question structure", so its full meaning has to be rebuilt from the earlier turn.[^c4]

The two are different repairs. Anaphora needs a referent found in the context. Ellipsis needs a missing structure rebuilt from it. The thesis asks for both at once: systems "should employ adaptive context tracking to resolve these references and reconstruct omitted information".[^c5] The standard repair in the thesis is query rewriting, which "transform[s] context-dependent queries into stand-alone ones conditioned on the previous conversational context".[^c6] The thesis also separates it from query expansion, noting that the two "can produce different effects by restoring the missing tokens in the context or introducing relevant supplementary information to the query".[^c7]

What this concept adds to the wiki is a way of saying what a follow-up has lost. A retriever fed the last turn alone loses whatever a pronoun pointed to, and whatever an ellipsis left out. The reading of the phenomena is the thesis's own classification; the measured retrieval cost is in the non-standalone note.

## Limits

- The thesis gives two definitions and one example for each phenomenon. It does not count how often each occurs in its benchmarks, nor which one drives the retrieval loss.
- Anaphora and ellipsis are not tested apart. The retrieval gap measured elsewhere for non-standalone questions does not split the two either, so their separate effects are unknown here.
- The definitions come from the discourse-linguistics literature that the thesis cites; those sources were not read.
- All examples are English keyword-style queries. Whether the same split holds in other languages, or for follow-ups that are commands rather than questions, is not tested in what was read.
- My reading, not the thesis's: a method that resolves anaphora well may still miss ellipsis, because the rebuilt structure needs more than a referent. This is a guess and no experiment here checks it.

## Related

- [[non-standalone-question-retrieval-gap]] — the measured retrieval cost of a context-dependent turn, which these phenomena cause
- context-denoised-history-selection — which earlier turns to draw on to resolve these, keeping the useful ones and dropping the rest
- [[last-turn-flattening]] — passing only the last turn removes the very context these phenomena need, per my reading of its description

[^c1]: doi-10-71781-36302 — "usually needs to address two key semantic phenomena: anaphora and ellipsis"
[^c2]: doi-10-71781-36302 — "Anaphora occurs when the semantics of an expression depend on the preceding context"
[^c3]: doi-10-71781-36302 — "has no independent meaning on its own and should refer to the phrase"
[^c4]: doi-10-71781-36302 — "this follow-up query is completely missing the verb and the core question structure"
[^c5]: doi-10-71781-36302 — "systems should employ adaptive context tracking to resolve these references"
[^c6]: doi-10-71781-36302 — "stand-alone ones conditioned on the previous conversational context"
[^c7]: doi-10-71781-36302 — "the missing tokens in the context or introducing relevant supplementary information"
[^c8]: doi-10-71781-36302 — "ellipsis involves the omission of semantic elements that are understood from prior"
