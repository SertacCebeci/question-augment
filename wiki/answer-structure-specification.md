---
description: "A query can be specified as a question, an answer structure (one number or a fixed-length list with named elements) and the definitions that resolve its terms, so the answer can be checked."
aliases: ["answer structure", "expected answer format", "query triple", "answer-shape specification"]
sources: ["arxiv-2601-02598"]
---
# Answer-structure specification

A query can carry its own answer shape. In LongDA each of the 505 queries has three parts: a question that states the analytical goal, an answer structure, and additional information. The answer structure "defines the expected format of the response, which is either a single numerical value or a fixed-length list with predefined semantic elements"; the paper's examples are lists such as [men, women] and [under18, age18_64, age65plus].[^c1] The three parts are, in the authors' words, "the minimal information required to make each query both unambiguous for automatic evaluation and faithful to real-world analytical practice."[^c2] The additional information is where a publication's own definitions go, included "to resolve potential linguistic ambiguities."[^c3]

The mechanism is that fixing the shape before any answer exists turns a free-text reply into something that can be checked element by element. A list with named elements fixes order and labels, so each value is attached to a meaning rather than to a position; a scalar fixes its form more loosely. (My inference: the paper does not analyse why the named list helps.) The split in the benchmark is 221 scalar queries (44%) and 284 list queries (56%).[^c4]

The benchmark also scores two things separately. Coverage is "the proportion of queries for which the answer syntactically conforms to the specified answer structure."[^c5] Match is the numerical correctness within tolerance, and the paper says its two primary metrics "evaluate whether agents produce structurally valid outputs and numerically correct answers within a tolerance."[^c6] An answer can conform in shape and still be wrong in value, and the two are kept apart, so a shape failure is not read as a computation failure.

From the asker's side, the structure is a slot: the question opens a place for the answer to take a particular form, and the answerer must fill it in that form. (My inference, drawn from the INTENT framing of slots; the paper does not put it this way.) Its effect on difficulty is visible but confounded. List queries are "consistently more difficult than scalar ones, due to both increased computational complexity and the requirement to follow specific answer structures."[^c7] Shape-following and computation rise together in that contrast.

## Limits

- The paper does not isolate the structure. Scalar and list queries differ in computation as well as in shape, and the sections read report no run in which the same computation is asked with and without a stated structure. That a stated structure helps an answerer is therefore an inference, not a measured result here.
- Coverage is a syntactic check against the template. It shows that the output fits the shape, not that the labels were understood.
- The structure is designed for automatic scoring. Whether asking with a fixed shape costs accuracy in settings where the shape is not known in advance is not tested.
- The element lists in LongDA are fixed and predefined. Open-ended, nested or conditional structures are not examined.
- Because lists are harder partly for shape reasons, the 56% list share is not a difficulty estimate on its own.

## Related

- [[context-dominates-model-choice]] — the definitions a document supplies turn a guess about a phrase into a lookup; the additional information plays a similar role for terms (my framing).
- [[answer-format-dependent-bias-measurement]] — there the answer format varies and changes the measured result; here the format is written into the query itself.
- [[ambiguity-taxonomy]] — the classes of underspecification that a named structure and attached definitions are meant to close (my framing).

[^c1]: arxiv-2601-02598 — "The answer structure defines the expected format of the response, which is either a single numerical value or a fixed-length list with predefined semantic elements"
[^c2]: arxiv-2601-02598 — "the minimal information required to make each query both unambiguous for automatic evaluation and faithful to real-world analytical practice"
[^c3]: arxiv-2601-02598 — "include them as additional information to resolve potential linguistic ambiguities"
[^c4]: arxiv-2601-02598 — "221 queries (44%) require a single numerical answer"
[^c5]: arxiv-2601-02598 — "the proportion of queries for which the answer syntactically conforms to the specified answer structure"
[^c6]: arxiv-2601-02598 — "evaluate whether agents produce structurally valid outputs and numerically correct answers within a tolerance"
[^c7]: arxiv-2601-02598 — "List queries are consistently more difficult than scalar ones, due to both increased computational complexity and the requirement to follow specific answer structures"
