---
description: "A task is kept as a research question only if a no-search answer from the model's own knowledge scores poorly; high-scoring parametric answers mark the question as not needing retrieval."
aliases: ["search necessity filter", "parametric-baseline task filter"]
sources: ["arxiv-2601-09688"]
---
# Search necessity filter

A question can look hard and still be answerable from what a model already knows. DeepResearchEval tests this directly. After an LLM-based qualification pass keeps tasks that need up-to-date knowledge, multi-source integration and multi-layered investigation (confidence above 0.7), a model attempts each retained task "using only parametric knowledge (no external tools)".[^c1] A separate evaluator scores that non-search answer on accuracy, depth, timeliness, professionalism and structure. Tasks that earn high quality without search are discarded.[^c2]

In the pipeline, 200 persona-generated candidates were reduced to 155 retained tasks.[^c3] Seven PhD-level experts then judged those 155; 80% were approved by at least four of them, which the authors take as evidence that the automated filter reliably yields deep-research tasks.[^c4]

The mechanism treats the question's need for retrieval as an empirical property, measured by the quality of the no-retrieval answer, rather than as something read off the question's wording. This is my reading: it gives an asker a test for whether a question deserves external evidence, and gives an answerer a signal that retrieval would add little.

## Limits

- The threshold for "high quality" is not a validated cut-off, and the evaluator is itself an LLM whose scoring of its own family's parametric answers may be lenient.
- Human validation checked that retained tasks looked like deep research, not that discarded ones were truly answerable without search.
- The filter is tied to one model's knowledge cutoff; a task needing search for one model may not for another (my inference).
- Only 100 of the 155 tasks were used, chosen by human ranking.

## Related

- [[post-cutoff-corpus-benchmark-isolation]] — forces retrieval need by data date instead of by testing a no-search baseline
- [[parametric-knowledge-gates-retrieval-noise-damage]] — what the model already knows decides whether retrieval helps or hurts
- [[rubric-formation-gap]] — the same benchmark paper's other lever: deciding what to check

[^c1]: arxiv-2601-09688 — "an LLM attempts each retained task t using only parametric knowledge (no"
[^c2]: arxiv-2601-09688 — "Tasks achieving high quality scores without search are filtered out, resulting in 155 retained tasks."
[^c3]: arxiv-2601-09688 — "We generate four tasks"
[^c4]: arxiv-2601-09688 — "80% of tasks were deemed qualified by at least four experts."
