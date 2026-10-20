---
description: "Free-form clarifying feedback is split into three typed clauses — what to include, what to exclude, which direction to search — scored separately and conjoined by AND."
aliases: ["FALM", "Feedback ALignment Module", "contains/not-contains/temporal decomposition"]
sources: ["arxiv-2604-24893"]
---
# Typed feedback clause decomposition

> A follow-up is not one thing to embed and match — it is up to three
> separable constraints, and treating it as one blurs all three together.

## Definition / Mechanism

**The setting (Subedi, Bazzani & Al-Halah (2026)).** In
episodic memory search over egocentric video, a model answers a query with a
predicted moment; the user can then reply with a short natural-language
correction (e.g. "Before this. I'm looking for the big blue mug not the
white one") instead of a second query. The **Feedback ALignment Module
(FALM)** turns that free-form reply into a re-ranking signal over the
video's clips.

**The decomposition.** Rather than encoding the feedback once and matching
it against clips as a single vector, FALM's supervision is built by reading
the feedback as up to three independent clauses: "we design prompts that
encourage the feedback to include any combination of three types of
information: (1) additional disambiguating details about the queried
object or moment derived from Diq ; (2) contrastive cues highlighting
differences between Rqi and Rfj based on Diq and Djf ; and (3) temporal
guidance indicating whether to search before or after the current reference
span Rfj ." At training time these are extracted back out of each
feedback string by an LLM and turned into three separate label channels:
"we generate pseudo-labels to supervise the learning of FALM by indicating
clip relevance based on three cues extracted from the feedback: (1)
Contains: what information the correct response should contain, (2) Not
Contains: what should not appear in the response, and (3) Temporal: whether
to search before or after the reference span." Each channel is scored
against every clip independently (a contains-similarity, an
inverted not-contains-similarity, and a before/after mask), and only then
recombined: "we combine the three label types using a logical AND
operation to form the final FALM labels: $L = L^c \land L^k \land L^t$."[^c3]
Not every feedback string carries all three clauses; a clip is filtered by
whichever subset is present. The resulting alignment score reweights the
candidate clips of an existing (frozen or fine-tuned) retrieval model,
shifting its attention without retraining it from scratch.

## Why it matters

The alternative — matching one pooled feedback embedding against clip
embeddings — conflates "include this" with "exclude that" with "look
elsewhere," three constraints with opposite or orthogonal effects on the
candidate set. Typing the clause before scoring lets each one narrow the
set the way it actually should (inclusion keeps clips, exclusion removes
them, direction restricts the search window), rather than averaging them
into a single fuzzy similarity. That this decomposition, not model scale,
is what is missing elsewhere is visible in the comparison against a
commercial vision-language model given the same raw feedback text: "despite
the strong R1 performance of Gemini-2.5-Flash, it is unable to
significantly improve its predictions when given feedback and a reference
span." A much larger model that reads the feedback whole does not
recover what a much smaller model recovers by reading it as three clauses.

## Limits

The three-way taxonomy (contains / not-contains / temporal) is hand-fixed
for this task and this domain (egocentric-video moment retrieval); the
paper does not test whether a clarifying reply in another modality or task
decomposes cleanly into the same three types, or whether a fourth type of
clause (e.g. a relative comparison that is neither inclusion nor timing)
would be lost by this scheme. Labels are extracted from feedback by an LLM
and validated only by downstream task accuracy, not by human agreement on
the clause split itself. The mechanism is evaluated single-turn; its
multi-turn extension averages the outputs of repeated single-turn passes
rather than jointly decomposing accumulated feedback, and is reported as a
baseline for future work rather than a tested claim of the same kind.

## Related

- [[constraint-as-information]]
- [[clarification-request]]
- [[interpretation-space]]
- [[proxy-instantiation]]

[^c3]: arxiv-2604-24893 — "we combine the three label types using a logical AND operation to form the final FALM labels: L = Lc ∧Lk ∧Lt ."
