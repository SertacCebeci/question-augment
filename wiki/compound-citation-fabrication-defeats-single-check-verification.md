---
description: "In 100 fabricated NeurIPS 2025 citations every one combined several deception layers, so any single check (title, link, name) passes them; only full cross-matching catches them."
aliases: ["compound deception in fabricated citations", "false verifiability", "identifier hijacking", "citation hallucination failure modes"]
sources: ["arxiv-2602-05930"]
---
# Compound citation fabrication defeats single-check verification

A language model asked for references produces records whose parts look legitimate separately. Ansari classified 100 fabricated citations found by GPTZero's checker (human-confirmed) in 53 accepted NeurIPS 2025 papers, each reviewed by 3–5 experts.[^c1] The coding was done by one author, with a primary code (the failure most visible to a verifier) and a secondary code (the other deception present).[^c2]

## Five failure modes

- Total Fabrication: authors, title, venue and identifiers all invented. 66% of primary codes.
- Partial Attribute Corruption: real authors or venues attached to wrong titles, years or pages. 27%.
- Identifier Hijacking: a valid arXiv ID or DOI that resolves to a real paper whose metadata does not match. 4%.
- Placeholder Hallucination: "Firstname Lastname", "to be updated". 2%.
- Semantic Hallucination: a domain-plausible title that exists nowhere. 1%.[^c3]

The paper also names a sixth case, Contamination Inheritance: one fabricated CVPR citation had already appeared in an earlier arXiv version of another paper, so the model may have copied a polluted training example rather than invented it.[^c4]

## The compound finding

All 100 citations carried a secondary mode as well. Secondary codes were Semantic Hallucination 63, Identifier Hijacking 29, Placeholder 4, Partial Corruption 3, Total Fabrication 1. Of the 66 Total Fabrications, 50 (76%) borrowed a plausible title.[^c5] Each layer defeats a cheap heuristic: "does the title fit the field", "does the link work" (false verifiability: a working link to an unrelated paper), and "do I recognise the names or venue".[^c6] The author's conclusion is that checking any one attribute fails, and only confirming that authors, title, venue, date and identifier all match one real source works.[^c7]

For an asker or answerer, the point is about what counts as evidence of grounding. A check that the answer's pointer resolves is weaker than a check that the pointer's content matches the claim. The two obvious placeholder cases still passed review, which the author reads as citation checking not being in the reviewer workflow at all.[^c8]

## Per-paper pattern

The 53 papers average 1.89 fabrications (median 2, maximum 13). 49 papers (92%) have 1–2, read by the author as light "gap-filling", and a few have 4–13, read as heavy reliance.[^c9]

## Limits

- The sample is only citations GPTZero's tool already flagged. Fabrications it missed, and the base rate among all references, are unknown, so the percentages describe the flagged set, not LLM output in general.
- One coder, no inter-rater agreement reported. Primary versus secondary assignment is a judgement ("most prominent"), so the 100% compound rate partly reflects the coding scheme: a citation with several wrong fields is almost bound to receive a secondary code.
- The claim that reviewers use the three heuristics is inferred from outcomes, not measured: no reviewer behaviour or eye-on-reference data was collected. The "structured fabrication that anticipates how humans verify" reading is the author's interpretation; the model has no known intent. This is unverified.
- The 92%/8% "minimal versus heavy AI use" reading is an inference from counts, not from knowing authors' workflows.
- No detector or intervention was tested; the proposed mandatory automated verification is a recommendation only.
- Not tested: whether the same distribution holds for other models, venues or fields.

## Related

- [[presupposition-hallucination-gap]] — another case where fluent, plausible output conceals that its premise is false
- [[process-outcome-consistency-verification]] — verification by cross-checking components against each other rather than one signal
- [[accuracy-masks-selective-reliability]] — a surface-level pass rate hiding the failures underneath

[^c1]: arxiv-2602-05930 — "GPTZero’s analysis identified 100 hallucinated citations spanning 53 distinct papers"
[^c2]: arxiv-2602-05930 — "The primary code identifies the most prominent failure characteristic"
[^c3]: arxiv-2602-05930 — "Total Fabrication (66%), Partial Attribute Corruption (27%), Identifier Hijacking (4%), Placeholder Hallucination (2%), and Semantic Hallucination"
[^c4]: arxiv-2602-05930 — "We have named this failure mode as “Contamination Inheritance (CI).”"
[^c5]: arxiv-2602-05930 — "among the 66 Total Fabrications, 50 cases (76%) utilized"
[^c6]: arxiv-2602-05930 — "This creates false verifiability i.e. the citation passes the “link works” test while failing comprehensive verification."
[^c7]: arxiv-2602-05930 — "Only comprehensive cross-verification, confirming that authors, title, venue,"
[^c8]: arxiv-2602-05930 — "This indicates that citation checking is not part of the standard reviewer workflow at elite conferences"
[^c9]: arxiv-2602-05930 — "49 of 53 papers (92%) contain only 1–2 hallucinations"
