---
description: "Answering from inconsistent data by intersecting query answers over all minimal repairs; update-based repair keeps a faulty record's correct fields, and one nucleus can answer a whole query class."
aliases: ["consistent query answering", "consistent answer", "update-based repairing", "uprepair", "nucleus of repairs"]
sources: ["wijsen-2005"]
---
# Consistent answer over repairs

When a database violates its integrity constraints, a repair is a consistent database "as close as possible" to the original. Repairs are usually not unique, so the answer to a question is defined as what holds in every repair: the intersection of the query answers over all repairs, the consistent answer.[^c1] Intuitively all repairs are equally possible, and only tuples present in all answers are certainly true.[^c1]

## Update-based repair

Nearly all earlier work repaired by deleting or inserting whole tuples. The cost is that a tuple can hold correct and erroneous components together, and deleting it loses the correct ones.[^c2] Wijsen instead replaces suspect values by variables ("fixes") and then fills the variables with constants to get consistent "uprepairs". In the running example, doubting the model "sedan" in one tuple leaves its other fields in play; the question "give all versions" still returns "luxury" and "standard", whereas deleting the tuple would lose the luxury car.[^c3] Which value is mistaken is not decided: each choice of suspect field gives a different fix, and the answer keeps only what survives all of them.

## Nucleus

The set of uprepairs can be infinite. For full dependencies and conjunctive queries they can be summarised in one tableau, the nucleus, homomorphic to all uprepairs and maximal with that property; running a conjunctive query on it gives the consistent answer, with no query rewriting.[^c4] A nucleus is computed once and reused for any conjunctive query, but must be recomputed when the data change.[^c5]

## Complexity (data complexity)

- Fix checking is in P for full dependencies; consistent answering is in NP for full dependencies and conjunctive queries.[^c6]
- A family of constraints exists where a relation with n-1 tuples admits no conjunctive-query nucleus smaller than 2^n.[^c6]
- For key dependencies, a nucleus for linear queries is polynomial, yet consistent answering is NP-complete for general conjunctive queries.[^c6]
- The author found no case tractable under insertion/deletion repair and intractable under update repair, or the reverse.[^c7]

## Limits

The work is database theory; whether people or language models asking questions of conflicting sources should adopt "answer only what every repair supports" is my inference, not tested here. It assumes the constraints are correct and the data are the faulty part, a distinction the author notes separates this from reasoning in inconsistent knowledge bases.[^c8] Results are about relational data with full or contradiction-generating dependencies and conjunctive queries; nothing is shown for free-text answers. Nucleus size can be exponential in the general case.

## Related

- [[agm-belief-revision]] — also revises by minimal change, but picks one revised state instead of intersecting all
- [[truth-maintenance-system]] — tracks which conclusions depend on conflicting premises
- [[contradiction-gate]] — acting on detected conflict rather than answering across all resolutions
- [[residue-of-a-contradiction]] — what remains after a contradiction, akin to the consistent core

[^c1]: wijsen-2005 — "The generally accepted query semantics is to execute the query on each repair and return the intersection of all answers, the so-called consistent query answer."
[^c2]: wijsen-2005 — "When we delete a tuple because it contains an error, we also lose the correct components as an undesirable side effect."
[^c3]: wijsen-2005 — "The question “Give all versions” yields “luxury” and “standard.”"
[^c4]: wijsen-2005 — "The tableau G, called nucleus, will be"
[^c5]: wijsen-2005 — "The drawback is that the nucleus has to be recomputed when the underlying"
[^c6]: wijsen-2005 — "Fix checking is in P for full dependencies. Consistent query answering is in"
[^c7]: wijsen-2005 — "So far, we found no instance of the consistent query answering problem that is known to be tractable under deletion/"
[^c8]: wijsen-2005 — "The clear"
