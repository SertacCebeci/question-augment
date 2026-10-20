---
description: "Evidence is found mostly by literal word overlap with the question; when none is shared, VLMs can fail to link the two and some refuse although the answer is in the context."
aliases: ["literal overlap dependence", "minimal literal overlap", "keyword-match retrieval", "lexical correspondence reliance"]
sources: ["arxiv-2512-15649"]
---
# Literal-match dependence

Finding a fact in a long context leans heavily on matching words. The VTC benchmark states the premise directly: "Literal matches make it much easier for VLMs to locate the relevant information and answer correctly."[^l1] A lexical hit is cheap. The answerer can find the fact and carry it across to the answer, and the paper notes this can happen "possibly without understanding the meaning of the text."[^l2]

The dependence can be separated by construction. The reasoning task keeps the answer in the context but cuts the lexical bridge. Its stated aim is to "minimize literal overlap between questions and their corresponding needles", with keywords whose "relationships are defined by associative links", such as real-world or commonsense facts.[^l3] Retrieval then has no handle to grab, and the answerer must infer the link.

What happens next is measured by the same paper, on rendered text (see vision-text-compression). The VLMs' performance on this task "reveals a stark performance collapse across all evaluated VLMs".[^l4] The authors separate two failure kinds. Many errors are not failures to find the fact: they are "failed retrieval but a breakdown in the subsequent reasoning step".[^l5] In their example the model extracts that a person is a vegan but does not conclude the person cannot eat fish; the paper says that models "fail to perform the required logical inference".[^l6]

The refusal is the more unusual pattern. When the wording of the question has no literal counterpart in the context, one model family answers that the information is absent. The authors' account is that when the question's phrasing does not "explicitly appear in the compressed visual text, the model conservatively defaults to a refusal".[^l7] The Qwen3-VL-235B-A22B-Instruct model "refused to answer more than 60% of the questions" in their table,[^l8] and "We also found this in the InternVL3.5 series" as well.[^l9] The answer was in the context. The refusal rests on the premise that a missing literal match means a missing fact.

## What survives the transfer

The dependence is not only a property of images. The text-only baseline also drops on this reasoning task: "the Qwen3-8B LLM baseline also" degrades,[^l10] but its score "far surpasses that of most VLMs".[^l11] So the literal-match effect is shared, and the rendered medium adds to it. The refusal pattern is the part that appears specific to the VLMs tested.

## Limits

- Overlap is not a measured variable in the sections read. The items are built with few literal matches, but no overlap score or dose-response curve is reported. The contrast is between two tasks.
- The two tasks differ in the inference step as well as in overlap. So the overlap effect is confounded with the reasoning step. Separating them is my inference, not a result.
- The refusal cause is a guess. The authors write "We guess this may stem from over-tuned" safety alignment, and that is untested.
- The results are for synthetic needles with constructed associations. No human answerers are tested here, so whether people show the same drop when a question shares no words with its evidence is open.
- Refusal is reported for two model families only. Whether the same refusal appears in other models, or in text-only models given the same wording gap, is not tested in these sections.

## Related

- [[reverse-constructed-indirect-question]] — a question built to remove its search handle on purpose; the same literal dependence, used to make search fail.
- vision-text-compression — the rendered-context medium in which the reasoning collapse was measured.
- [[semantically-defined-queries]] — queries where lexical and neural retrievers disagree; lexical overlap decides what is found there too.
- [[lexical-reranker-sign-diagnostic]] — a lexical reranker helps or hurts depending on whether paraphrase suppresses overlap; the same dependence seen from the retriever side.
- [[abstention]] — the refusal described here is an error by the paper's own account, since the answer is present; the abstention note is where a correct refusal would be judged.

[^l1]: arxiv-2512-15649 — "Literal matches make it much easier for VLMs to locate the relevant information and answer correctly"
[^l2]: arxiv-2512-15649 — "possibly without understanding the meaning of the text"
[^l3]: arxiv-2512-15649 — "minimize literal overlap between questions and their corresponding needles"
[^l4]: arxiv-2512-15649 — "reveals a stark performance collapse across all evaluated VLMs"
[^l5]: arxiv-2512-15649 — "failed retrieval but a breakdown in the subsequent reasoning step"
[^l6]: arxiv-2512-15649 — "fail to perform the required logical inference"
[^l7]: arxiv-2512-15649 — "explicitly appear in the compressed visual text, the model conservatively defaults to a refusal"
[^l8]: arxiv-2512-15649 — "refused to answer more than 60% of the questions"
[^l9]: arxiv-2512-15649 — "We also found this in the InternVL3.5 series"
[^l10]: arxiv-2512-15649 — "the Qwen3-8B LLM baseline also"
[^l11]: arxiv-2512-15649 — "its performance (e.g., 94.18% at 1k) far surpasses that of most VLMs"
