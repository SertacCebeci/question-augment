---
description: "Crediting each stated intermediate conclusion only if all its annotated prerequisites are also correct exposes chain failures that final-answer accuracy and flat checklist coverage hide."
aliases: ["DACS", "Dependency-Aware Checklist Score", "dependency-grounded credit"]
sources: ["doi-10-13140-rg-2-2-29034-48321", "doi-10-48550-arxiv-2606-03361", "arxiv-2512-12989"]
---
# Dependency-aware checklist scoring

A long research question can be annotated as a directed acyclic graph of necessary intermediate conclusions leading to a short answer. Mr.LHDR does this for 102 questions with 1,231 annotated conclusions and a mean dependency depth of 10.4.[^c1] Four scores are then read off the same response: Overall Accuracy (final answer only), Strict Accuracy (every annotated conclusion stated correctly), Checklist Score (mean coverage, ignoring dependencies) and the Dependency-Aware Checklist Score (DACS).[^c2]

DACS is recursive: a node's credit is its own correctness times the credit of every direct prerequisite, with an empty product equal to one. A conclusion is therefore credited only if it and all its transitive prerequisites are satisfied.[^c3] Independent branches keep their credit, but a missing ancestor zeroes everything downstream.[^c4]

What it reveals, as measured there:

- Final-answer accuracy overstates completion. The authors report that "final-answer success overstates complete task execution": the best regular model reached 43.1% OA but 34.3% SA, and the best dedicated system 32.4% OA but 19.6% SA.[^c5]
- DACS below CS marks conclusions stated without their prerequisites. For example, Gemini 2.5 Flash scores 65.0% CS but 58.0% DACS.[^c6]
- Strict accuracy falls monotonically with checklist length in every length range with at least 20 items, for every representative model.[^c7]

For asking, the practical reading (my inference, not the paper's claim) is that a question's difficulty is better described by its prerequisite depth than by its answer, and that an answer's quality is better judged by whether its intermediate steps are consistent than by the final string.

## Limits

- The scores see only conclusions stated in the response. The authors say they evaluate "dependency-consistent stated conclusions rather than actual evidence-chain completion": they neither observe the agent's reasoning nor establish that a conclusion came from retrieval.[^c8]
- Credit depends on an author-annotated DAG presumed irreducible; alternative valid routes to the answer are not given credit (my inference).
- Judgments come from an LLM judge; only 102 questions, and neighbouring systems' confidence intervals overlap, so results support broad patterns, not a ranking.[^c9]
- Not tested here on clarification or question-asking quality; the transfer to conversational settings is untested.
- Failure counts can overstate defects when failures depend on each other. In a coding-migration study, a single missing key or signature suppressed many downstream checks, so the failed-check total was not a count of independent bugs.[^c11] Grading by dependency, as DACS does for conclusions, is the natural remedy; the coding study did not score that way (my inference).

## Related

- [[dependency-aware-subquestion-scheduling]] — uses dependency structure to run sub-questions, rather than to score answers
- [[search-effort-accuracy-decoupling]] — another case where an outcome measure fails to track process
- [[clarification-benchmarks]] — benchmarks that likewise must choose what to credit besides the final answer
- [[soft-dependency-retention]] — a soft version of the same licensing for rubric rewards: an unsupported prerequisite discounts its child rather than removing its credit, with the discount set by a retention factor[^c10]

[^c1]: doi-10-13140-rg-2-2-29034-48321 — "The benchmark contains 1,231 annotated intermediate conclusions with a mean dependency"
[^c2]: doi-10-13140-rg-2-2-29034-48321 — "to distinguish final-answer"
[^c3]: doi-10-13140-rg-2-2-29034-48321 — "A node therefore receives credit only if both the node itself and all of its"
[^c4]: doi-10-13140-rg-2-2-29034-48321 — "This recursion preserves credit for independent branches but withholds"
[^c5]: doi-10-13140-rg-2-2-29034-48321 — "Second, final-answer success overstates complete task execution."
[^c6]: doi-10-13140-rg-2-2-29034-48321 — "Gemini 2.5 Flash reaches 65.0% CS but 58.0% DACS"
[^c7]: doi-10-13140-rg-2-2-29034-48321 — "SA decreases monotonically with checklist length for every representative model."
[^c8]: doi-10-13140-rg-2-2-29034-48321 — "they evaluate"
[^c9]: doi-10-13140-rg-2-2-29034-48321 — "Because confidence"
[^c10]: doi-10-48550-arxiv-2606-03361 — "Prerequisite edges encode graded support: when a prerequisite parent is unsupported, the child event remains possible but its probability should be discounted, with"
[^c11]: arxiv-2512-12989 — "Many failures follow from missing keys or signatures; they are not 30 independently identified bugs."
