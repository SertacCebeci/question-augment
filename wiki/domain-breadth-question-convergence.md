---
description: "Across five LLMs and domains, a requirement's breadth — not the model — sets whether generated competency questions converge on the same set or diverge into disjoint ones."
aliases: []
sources: ["arxiv-2604-16258"]
---
# Domain breadth and question-set convergence

> A narrow, constrained requirement makes five different models ask
> nearly the same questions; a broad, narrative one makes each model ask
> questions none of the others do — same models, same prompt template,
> opposite outcome.

## Definition / Mechanism

Five LLMs (two closed: Gemini 2.5 Pro, GPT-4.1; three open: KimiK2,
Llama3.1-8B, Llama3.2-3B) were each given the same requirement
specification — a user story or a use case, from one of five domains —
and asked, with an identical zero-shot instruction, to generate a set of
competency questions (CQs): the natural-language questions an ontology
must be able to answer. The resulting CQ sets were compared with
embedding-based [[questioning-diversity|diversity]] metrics (average
pairwise cosine similarity, centroid distance, Shannon entropy) and a
pairwise bidirectional-coverage overlap score between every pair of
models' sets, alongside readability (Flesch-Kincaid, Dale-Chall) and
structural-complexity features of the CQs themselves.

Domain characteristics, not the model, were the primary determinant of
what was elicited. A domain that describes a narrow, well-defined task —
finding a park by weather, crowd size and location — forced high
thematic agreement: four of five models converged on largely the same
CQs, with bidirectional overlap up to 56.2% between two models and
centroid similarities above 0.9. A domain specified instead as a
persona-driven narrative (a museum curator's or a donor's goals, left
implicit rather than enumerated) produced almost zero overlap between
any pair of models — each explored a different, non-overlapping facet
of the same requirement, despite being thematically aligned. A
domain that was narrow in scope but technically dense (genetics,
treatments and clinical outcomes) instead drove every model toward its
most complex and least readable output, independent of which model.[^c3]

## Why it matters

Whether an LLM asked to generate elicitation questions from a
requirement will reproduce what another model would ask, or supply
something novel, is set by the breadth of the requirement's own
framing before a model is ever chosen. A narrow, structured
specification needs only one model to sample the requirement space
adequately; a broad or narrative one needs several, because none
covers it alone — the paper's own conclusion is that CQ generation
"requires combining multiple models and retaining human-in-the-loop
refinement to ensure comprehensive and accurate coverage." Model
choice still matters at the margin: closed models were consistently
more stable and readable, open models traded that stability for higher
diversity, and the smallest open model at times failed to cover the
domain at all.[^c5]

## Limits

Five domains and five models is a demonstration, not a law relating
"domain breadth" (an unquantified, post-hoc label) to convergence; no
independent measure of breadth predicts the overlap score in advance.
There is no ground-truth CQ set to check correctness against — deliberately,
to avoid rewarding memorised training data — so "diversity" and
"novelty" are read off embedding statistics, never validated against
whether the extra questions are ontologically sound. **Unverified:** in
the one domain, one model (Llama3.2-3B) registered 0% overlap with
every other model even though the domain was otherwise the most
convergent one; the paper reads this as comprehension failure rather
than genuine novelty, but the study offers no independent check that
distinguishes the two.

## Related

[[questioning-diversity]] · [[survey-response-model]] ·
[[cross-provider-judge-ensemble]] · [[ambiguity-taxonomy]]

[^c3]: arxiv-2604-16258 — "The Personalized Depression Treatment Ontology (PDTO), a highly complex, context-rich domain involving relationships between genetics, treatments, and outcomes, consistently elicited the most complex and least readable CQs from all five models. This domain produced the peak scores for nearly every model in every complexity and readability metric (e.g., c1 of 16.33 for KimiK2, FKGL of 18.21 for Llama3.2-3B)."
[^c5]: arxiv-2604-16258 — "with closed models offering greater stability and readability and open models trading clarity for higher diversity, while some models fail to provide adequate coverage altogether."
