---
description: "In exhaustive set-enumeration questions, agents recover the membership far better than the per-item attributes; the gap is cell-finding, not set size or search effort."
aliases: ["set enumeration with attribute table", "item-F1 versus row-F1 gap"]
sources: ["doi-10-48550-arxiv-2606-27595"]
---
# Set membership versus cell completion gap

A breadth question names a closed set (a league, a dynasty, an election) and asks for every member plus a table of attributes per member. It differs from a depth question, which hides one short answer behind a chain of constraints. The answer is a whole table that must be exhaustive and internally complete.[^c1]

Three scores separate its parts: Item-F1 grades set membership, Column-F1 grades matched cells, and Row-F1 is the fraction of rows whose key and every attribute cell are correct.[^c2] In Ko-WideSearch, 20 web agents showed one consistent pattern: they recover the set but not the rows (Item-F1 92.8 against Row-F1 53.7 for the best system).[^c3] The same work reports that neither more search nor more spend closes the gap.[^c4]

## What the gap is and is not

- Not set size. Row-F1 pooled by gold set size is essentially flat from small to large tables, so larger sets are not harder.[^c5]
- Not search volume. Average tool calls per table against Row-F1 shows that more search does not buy completeness; the heaviest searchers scored lowest.[^c6]
- Difficulty comes from structure. The benchmark sets tiers by table width and a 2-D composite key, and membership holds up across tiers while downstream metrics fall.[^c7]
- Cell type matters. Open-ended free-text cells fail most, and cells with a standard answer such as a date or a name usually come out right. Finding the right value is the hard part, not formatting it.[^c8]
- A semantic LLM judge that credits same-referent surface variants raised Row-F1 by only 0.8 to 4.9 points. Strong models' remaining errors are more often surface variants, and weak models' are more often a wrong entity or value.[^c9]

My reading (an inference, not measured here): an asker who wants a table should treat membership and each attribute column as separate claims, because a correct list says little about whether the cells are right. A grader should likewise report them separately.

A construction point also applies: certifying that a gold set is complete and every cell correct is far harder than checking a single answer.[^c10]

## Limits

- Korean-language, web-sourced tasks only, scored by an automated normalization-aware comparator; the pattern's transfer to other languages or to non-web sources is untested here.
- Only three systems were instrumented for the per-cell-type breakdown, so the free-text finding rests on a small subset.
- Set-size flatness is correlational and pooled across models and categories. Width was varied by construction, but set size was not.
- Gold sets come from an automated build pipeline, so gold errors could slightly depress Row-F1.
- The note concerns agents answering; it does not show how a human asker should phrase breadth requests. That is my inference above.

## Related

- [[unbudgetable-completeness]] — completeness demands that no search budget can meet
- [[calibrated-completeness-stopping]] — when to stop searching for more members
- [[dual-judge-completeness-recall]] — grading recall of a complete answer
- [[interpretation-breadth-depth-asymmetry]] — breadth versus depth in a different setting

[^c1]: doi-10-48550-arxiv-2606-27595 — "difficulty is that the answer is a whole table, and it has to be"
[^c2]: doi-10-48550-arxiv-2606-27595 — "Row-F1: the fraction of rows whose key and every attribute cell are correct"
[^c3]: doi-10-48550-arxiv-2606-27595 — "(e.g. Item-F1 92.8 against Row-F1"
[^c4]: doi-10-48550-arxiv-2606-27595 — "neither more search nor more spend closes the gap."
[^c5]: doi-10-48550-arxiv-2606-27595 — "larger sets are not harder"
[^c6]: doi-10-48550-arxiv-2606-27595 — "more search does not buy completeness"
[^c7]: doi-10-48550-arxiv-2606-27595 — "Membership (Item-F1) holds up across the tiers"
[^c8]: doi-10-48550-arxiv-2606-27595 — "finding and normalizing the value, not formatting it"
[^c9]: doi-10-48550-arxiv-2606-27595 — "Row-F1 up by only 0.8–4.9 points"
[^c10]: doi-10-48550-arxiv-2606-27595 — "certifying that a gold set is complete and that every attribute cell is correct is far harder"
