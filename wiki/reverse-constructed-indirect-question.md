---
description: "A question can be built backward from the source that holds its answer, then made indirect and compositional until search no longer retrieves that source directly."
aliases: ["reverse construction of questions", "source-first question construction", "indirect compositional question", "question built from its evidence"]
sources: ["arxiv-2512-23044"]
---
# Reverse-constructed indirect question

Most questions are written forward: from a topic, toward an answer the writer
hopes exists. The benchmark studied here builds its questions in the opposite
order, from a source to a question. The paper says it adopts "a reverse
construction strategy that begins with video exploration and" only then
reaches a question.[^c1] Each annotator takes two video categories, finds
candidate videos, watches one of them completely, and writes an
"initial question-answer pair focused on a specific" clip.[^c2]

The simple question is then made harder by two operations. The first adds
conditions. The questions are "augmented with compositional conditions to
ensure" that the target video cannot be found by a simple search.[^c3] The
second removes the handle a search would use. Annotators "use indirect
descriptions to reference video content rather than explicit" keywords.[^c4]
What remains is a question whose answer lives in one source, but whose wording
does not name that source.

Multi-source questions, the top level of the benchmark, use a different
order. Annotators first identify a set of related videos, and the question
requires "where information retrieved from one source serves" as the
prerequisite for locating the next.[^c5] The answer is then spread across
sources, and no single one of them carries it.

## The answer is constrained

The construction also fixes what an answer may look like. The output is
constrained "to short, objective strings, such as specific entity" names,
counts, or colours, "allowing for automated" comparison with the ground
truth.[^c6][^c7] The questions are "grounded in objective" spatio-temporal
attributes, not subjective readings.[^c8] So the wording is hard to search,
while the answer is easy to check. The benchmark states this pairing as its
design principle.

## Two checks after construction

Two filters test the finished question. The first asks whether it can be
answered without the source, because "samples may still be answerable through
commonsense knowledge without watching the video." The paper's check is a
text search plus a GPT-5 model, used "to filter out questions that can be
answered correctly."[^c9][^c10]

The second asks whether the answer is unique. Other annotators answer each
question following the evidence chain, and if "an alternative answer satisfies
all task" constraints but differs from the original, the sample is discarded.[^c11]

The principle behind both is the same. The benchmark is meant to test video
perception and reasoning, "not merely text-based web search," and to stop
models "solving questions via textual shortcuts."[^c12]

## Limits

- The sections read do not report how many candidate questions the two filters
  removed, or how often the model-based filter let a shortcut through. Without
  those counts the filters' strength is not shown.
- There is no comparison with questions written forward, from a topic, at the
  same difficulty. So the claim that reverse construction yields questions a
  search cannot retrieve is not tested against an alternative.
- Search agents "collapse" on the harder levels, which is consistent with the
  construction working.[^c13] It cannot separate the construction from the
  difficulty it adds: a harder question built any other way would also defeat
  a search agent. That separation is my inference.
- Level 1 has 125 questions, Level 2 has 62 and Level 3 has 23.[^c14] The
  harder levels, where the construction matters most, are the smallest.
- The unique-answer check depends on annotators agreeing with one another. The
  sections read do not report an agreement rate.
- Restricting questions to objective attributes is a choice. It excludes
  questions where competent answers legitimately differ. The wiki's
  [[single-reference-grading-confound]] note treats exactly that case as the one
  where a single reference answer fails.

## Related

- [[perception-context-tradeoff]] — why a question whose answer lives in a
  video defeats a text proxy of that video.
- [[cost-ordered-perception-pyramid]] — the agent the constructed questions
  were used to test.
- [[single-reference-grading-confound]] — the unique-answer condition this
  construction enforces, and where a single reference answer misleads.
- [[short-form-check-blindness-to-open-ended-bias]] — the checkability that the
  short objective answer buys, and what a closed-form check can miss.

[^c1]: arxiv-2512-23044 — "We adopt a reverse construction strategy that begins with video exploration and"
[^c2]: arxiv-2512-23044 — "initial question-answer pair focused on a specific"
[^c3]: arxiv-2512-23044 — "augmented with compositional conditions to ensure"
[^c4]: arxiv-2512-23044 — "Annotators use indirect descriptions to reference video content rather than explicit"
[^c5]: arxiv-2512-23044 — "where information retrieved from one source serves"
[^c6]: arxiv-2512-23044 — "to short, objective strings, such as specific entity"
[^c7]: arxiv-2512-23044 — "names, counts, or colors, allowing for automated"
[^c8]: arxiv-2512-23044 — "Questions are grounded in objective"
[^c9]: arxiv-2512-23044 — "samples may still be answerable through commonsense knowledge without watching the video."
[^c10]: arxiv-2512-23044 — "it to GPT-5 to filter out questions that can be answered correctly."
[^c11]: arxiv-2512-23044 — "If an alternative answer satisfies all task"
[^c12]: arxiv-2512-23044 — "via textual shortcuts (e.g., retrieving a movie plot"
[^c13]: arxiv-2512-23044 — "performance collapses in Level 2 and Level 3 tasks,"
[^c14]: arxiv-2512-23044 — "Level 1 (125 samples) tests explicit"
