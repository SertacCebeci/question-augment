---
description: "Splitting an answer into claims and checking each by web search flagged most rubric-tied injected errors, but also flagged 55% of original answers, so it is a weak signal, not a grader."
aliases: ["SAFE", "search-augmented factuality evaluation", "claim-level retrieval factuality check", "retrieval-based factuality check"]
sources: ["doi-10-48550-arxiv-2609-12718"]
---
# Claim-decomposed retrieval check

A rubric asks whether a criterion is met. A claim-level check asks a different question: does each factual statement in the answer have support outside the answer? The paper uses a simplified version of the Search-Augmented Factuality Evaluator (SAFE), which the authors credit to Wei et al. (2024). It "decomposes an answer into claims, converts each claim into a search query, and checks whether the retrieved evidence supports it."[^s1]

## Mechanism

The check does not need a criterion written in advance. Every claim the answer makes is a candidate for checking, so an error that no rubric author anticipated can still be reached, provided it is a checkable claim. On 380 HealthBench pairs across 11 non-omission error types, where rubric scores were tied, the evaluator "identified the injected error as a checkable claim in" 88.7% of cases, and "flagged it as unsupported in 87.5%" of those.[^s2] The paper reads this as evidence that "retrieval can recover factuality signal that rubric evaluation misses."[^s3]

The recovery was uneven by error type. "The strongest results occurred for errors that are difficult to encode in fixed rubrics, including evidence fabrication, dosage error, and additional diagnosis."[^s4] These are the error types the rubric side cannot enumerate (see [[rubric-blind-spot]]), so the two results fit together: the cases where a fixed list fails are the cases where a claim-level search does best.

What transfers is the structure, not the numbers. A check that works per claim localises the suspect statement, which a single score does not, and it changes the question from "does the response meet the criteria" to "is this sentence supported." What does not transfer is the evidence source: the search here is general web search, not a clinical corpus.

## Limits

- False positives are high. The same check "flagged claims from the original responses as unsupported in 55.3% of pairs", and the paper calls this "indicating substantial false positives."[^s5] A check that rejects more than half of the unmodified answers cannot by itself separate correct from incorrect ones on this evidence.
- The cause is attributed to the search, not measured. The authors attribute it to "limitations of general web search for clinical claims", and say that relevant guidelines may not be retrieved.[^s6] They do not test a different corpus.
- The paper says the estimates are soft: "these estimates are indicative", with only 29–36 pairs per error type.[^s7]
- The authors' own remedy is untested here: "A more reliable evaluator would require retrieval from a clinical evidence corpus."[^s8] The result is labelled "preliminary", and the paper says the signal "requires further validation."[^s9]
- Recovery is measured against rubric ties, not against clinician judgement of the same injected errors. Whether a flagged claim is clinically harmful is a separate question the paper does not answer for this check.
- My inference, not the paper's: a claim-level check and a rubric can disagree in both directions, so a pipeline using both would need a rule for which verdict governs; the paper does not specify one.

## Related

- [[rubric-blind-spot]] — the failure this check is proposed to cover: errors no fixed criterion names.
- [[exemplar-retrieval-grounded-grading]] — retrieval used to ground a grader in stored exemplars; here retrieval supplies external evidence for each claim, a different use of search in grading.
- [[controlled-error-injection]] — the injected-error pairs on which the recovery rate was measured.

[^s1]: doi-10-48550-arxiv-2609-12718 — "claims, converts each claim into a search query, and checks whether the retrieved evidence supports it"
[^s2]: doi-10-48550-arxiv-2609-12718 — "flagged it as unsupported in 87.5%"
[^s3]: doi-10-48550-arxiv-2609-12718 — "retrieval can recover factuality signal that rubric evaluation misses"
[^s4]: doi-10-48550-arxiv-2609-12718 — "The strongest results occurred for errors that are difficult to encode in"
[^s5]: doi-10-48550-arxiv-2609-12718 — "indicating substantial false positives"
[^s6]: doi-10-48550-arxiv-2609-12718 — "limitations of general web search for clinical claims"
[^s7]: doi-10-48550-arxiv-2609-12718 — "these estimates are indicative"
[^s8]: doi-10-48550-arxiv-2609-12718 — "A more reliable evaluator would require retrieval from a clinical evidence corpus"
[^s9]: doi-10-48550-arxiv-2609-12718 — "requires further validation"
