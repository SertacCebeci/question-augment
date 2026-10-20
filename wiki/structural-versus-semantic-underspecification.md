---
description: "Underspecified prompts fail in two separable ways: one blocks execution (where a referent lives), one blocks correctness (what analysis is meant); fixing the first leaves the second."
aliases: ["structural vs semantic ambiguity", "execution-blocking versus correctness-blocking underspecification"]
sources: ["arxiv-2511-21920", "arxiv-2511-20709"]
---
# Structural versus semantic underspecification

An underspecified request can be short of two different things. It may not say where the referent is: which dataset path, which attribute, which file. Or it may not say what the analysis is: which preprocessing, which visualization, which function. The paper states the split directly, as "(1) resolving structural ambiguities that hinder execution and (2) ensuring semantic clarity that guides correct analysis and visualization."[^c1]

The split is a claim about which failure each fix reaches. A structural gap stops a script from running, because a path does not resolve or a name is missing. A semantic gap lets the script run and produce the wrong thing. Two repairs of different kinds therefore reach different outcomes. The paper's wording is that "data-aware prompt disambiguation significantly enhances the former," while reaching a good end-to-end result "requires complementary strategies, such as retrieval-augmented prompt enhancement or iterative refinement, to improve task specification."[^c2]

## What the measurements show

The pattern the split predicts is visible in the authors' figures. Grounding referents in the file moved scripts out of the failed category into the runnable one. It did not move them into the correct one: "while script executability improved, the proportion of outputs that produced correct analytical or visualization results showed only marginal gains."[^c3] The authors read the residue as acceptable: "they are generally easier for users to debug and fix compared to runtime failures."[^c4]

A second, separate test points the same way. Iterative repair driven by runtime error messages helped on the tabular datasets, where the errors were "syntactic or API-level issues," and did little on the MRI datasets, where scripts "encountered deeply embedded logic or domain-specific processing issues."[^c5] A repair loop that reads error messages can reach the structural and API class; the semantic class does not announce itself as an error.[^c6]

## Limits

- The split is the authors' framing. No experiment in the text varies one kind of gap while holding the other fixed; the simple and detailed prompts vary both together.
- The two labels are not operationalised. The text gives no procedure for classifying a given prompt's gaps as structural or semantic, so a reader cannot apply the split to a new prompt from the paper alone.
- "Correct" means the script "runs successfully and produces the expected output," where the expected output is one the authors held.[^c7] The semantic side is therefore measured against a reference the authors chose, not against the user's intent.
- Five models and one repair configuration (Devstral-24B for the repair experiment) were used. The pattern is not tested on other repair setups.
- My inference: the split may blur where a semantic error surfaces as a runtime fault, for example a wrong axis that crashes the plot call. Such a fault would be counted as structural by a runtime check while being semantic in origin. The paper does not separate these cases.
- A third site that the two-way split does not place. In DualGauge's functional failures the open part is the output contract: "generation leaves the invocation contract underspecified, and models fill the gap inconsistently."[^c8] The failures the audit found are contract failures, where the output misses "the expected output shape rather than the underlying computation."[^c9] My inference, not the paper's: a gap of this kind is neither a missing path nor a missing analysis step, so applying the split to it would need a third class, and the text does not supply one.

## Related

- [[data-grounded-reference-disambiguation]] — the structural-side fix: a referent resolved against the file's own paths, which raises execution and leaves correctness nearly flat
- [[referent-match-set-ambiguity]] — types a referent by how many candidates match it, a finer cut on the structural side
- [[text-to-sql-ambiguity-taxonomy]] — another typology of ambiguity in generated queries; not compared against this split here
- [[agentic-iteration-gap-under-localized-verifier-feedback]] — repair driven by localized feedback is uneven by error class, the same pattern this split predicts

[^c1]: arxiv-2511-21920 — "resolving structural ambiguities that hinder execution"
[^c2]: arxiv-2511-21920 — "requires complementary strategies, such as retrieval-augmented prompt enhancement or iterative refinement, to improve task specification"
[^c3]: arxiv-2511-21920 — "while script executability improved, the proportion of outputs that produced correct analytical or visualization results showed only marginal gains"
[^c4]: arxiv-2511-21920 — "they are generally easier for users to debug and fix"
[^c5]: arxiv-2511-21920 — "encountered deeply embedded logic or domain-specific processing issues"
[^c6]: arxiv-2511-21920 — "where execution failures stem from syntactic or API-level issues"
[^c7]: arxiv-2511-21920 — "where the script runs successfully and produces the expected output"
[^c8]: arxiv-2511-20709 — "generation leaves the invocation contract underspecified, and models fill the gap inconsistently"
[^c9]: arxiv-2511-20709 — "miss the expected output shape rather than the underlying computation"
