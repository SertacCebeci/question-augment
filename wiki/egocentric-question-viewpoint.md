---
description: "A question asked from the wearer's viewpoint, such as 'how to fix this?', leans on what the camera sees; it is gradable only when its reference picks out one object and one answer."
aliases: ["deictic visual question", "egocentric question", "first-person question", "viewpoint-anchored question"]
sources: ["arxiv-2511-22154"]
---
# Egocentric question viewpoint

A question put to a wearable assistant is often framed from the asker's own position. The WearVQA authors observe that "users tend to ask questions as if the assistant shares their viewpoint".[^q1] Their examples are "how to fix this?" asked when several objects are visible, and "should I use the tool on that corner to loosen the nut?"[^q2] The words "this" and "that corner" carry no content by themselves. The reference is fixed by where the wearer is looking, which is the frame the assistant receives. So the question depends on the image in a way a third-person question does not: the image is part of the question's meaning (my inference from those examples).

The benchmark turns this into a construction rule. Its questions must be "image-based", "short-form", "no external-source needed", and "unambiguous", and the last is stated as "the question has a single correct answer".[^q3] The paper illustrates the rule with a pair: "where is the dog relative to TV?" is admissible and "where is the dog?" is not, the second leaves the placement without a named reference point, so the answer can vary with the reading (my inference from the pair, not a reason the paper gives).[^q4] A deictic question with several matching objects has no single answer, so it cannot be graded against one ground truth. This is the asker's side of the transformation: the question must open a slot that a single answer can fill.

The answer side is graded too. The judge rubric includes "Egocentric: The response should be phrased in an egocentric way", and the paper's example of a failing answer is one that describes the picture ("The image shows the word...") rather than answering as the wearer would.[^q5] So what counts as a good answer includes its frame of reference, not only its content. My inference is that a question and its answer are both anchored to the same viewpoint, and a benchmark that scores only content would miss the mismatch.

## Limits

- The viewpoint claim rests on the authors' examples and on the design of their own question set. The paper does not measure how often real wearer queries are deictic, and no corpus of such queries is analysed in the text read.
- The unambiguity rule is stated as a design criterion. The paper reports one filter, removing questions that all main models answered correctly, which selects for difficulty, not for a single referent.[^q6] A manual audit found "minor inaccuracies, primarily in attribute labeling" in about 1.2% of entries, so reference errors were not separately counted.[^q7]
- The egocentric phrasing criterion is one of five judged criteria. The text read does not separate its effect on the correctness verdict from the others.
- English-only queries, and static images. Whether reference resolution differs for speech, for a moving wearer, or in another language is not tested here.

## Related

- [[ambiguity-taxonomy]] — the general catalogue of ambiguity; deictic reference is one of its types
- [[referent-match-set-ambiguity]] — types a referential ambiguity by how many objects in the scene match it; a "this" with several candidates is the multiplicity case
- [[clara-visual-disambiguation]] — when a reference is ambiguous, shows candidate images and lets the user pick, rather than asking in words
- [[egocentric-capture-degradation]] — the image side: the object a deictic question points at may be the one the capture hides
- [[llm-judge-validation-gap]] — the egocentric criterion is judged alongside correctness, and only correctness is validated against people

[^q1]: arxiv-2511-22154 — "users tend to ask questions as if the assistant shares their viewpoint"
[^q2]: arxiv-2511-22154 — "multiple objects are visible, or"
[^q3]: arxiv-2511-22154 — "Unambiguous: the question has a single correct answer"
[^q4]: arxiv-2511-22154 — "where is the dog relative to TV?"
[^q5]: arxiv-2511-22154 — "Egocentric: The response should be phrased in an egocentric way"
[^q6]: arxiv-2511-22154 — "we removed questions where all main models discussed in Section 4 provided correct answers"
[^q7]: arxiv-2511-22154 — "A manual audit revealed that approximately 1.2% of the dataset entries contained minor inaccuracies"
