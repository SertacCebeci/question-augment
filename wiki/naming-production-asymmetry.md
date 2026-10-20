---
description: "Enumerating a given list (how many items?) is harder for LLMs than producing a list of a stated length (give N), and the wrong counts still land near the target."
aliases: ["naming versus production", "how-many versus give-N", "numerosity naming and production", "forward versus reverse enumeration"]
sources: ["arxiv-2512-04727"]
---
# Naming versus production asymmetry

Cognitive studies of numerical skill use two tasks that run in opposite directions. In numerosity naming (how-many) the model is given a string and must output how many elements it holds. In numerosity production (give-N) the model is given a target number and must generate a sequence with that many elements: "the model is given a target numerical value and is asked to generate" the sequence.[^n1] Hou et al. put both to LLMs, with letters and with five-letter words, and the two directions come apart. Accuracy in naming stays lower even when the model is explicitly told to count, which the authors read as "it is more challenging to enumerate a given" list "rather than producing one from scratch".[^n2]

The asymmetry is strongest when a counting procedure is cued ([[enumeration-cue-dependence]]). Under that cue the top proprietary models are near ceiling "only in the production task", while in naming they "still struggle with counting the number of elements in a given" list.[^n3] When no procedure runs, the gap shrinks. The authors read this as both tasks falling back on estimation: "reduced, suggesting that in such conditions the LLMs rely on similar approximate".[^n4]

Wrong answers are not random. Proprietary models that miss "still get reasonably close to the target number", which the authors show with mean absolute error as well as accuracy.[^n5] Accuracy and error size are therefore two properties of one answer. My inference, not the paper's: a question that demands an exact count and one that accepts a magnitude are scored on different axes, and the same model can pass one and fail the other.

The stimulus format also matters. Words were counted more accurately than letters, "accurate in naming and production tasks involving words rather than letters".[^n6] The words were chosen so that each is one token, and the authors tie the advantage to the "correspondence with the tokens provided as input to the models".[^n7] They note that this is "aligned with recent findings that highlight the importance of tokenization", a link they did not test by manipulating tokenization.[^n8]

## Limits

- The main analysis uses repeated items. Heterogeneous sequences are in a supplement, and the paper says "Performance is qualitatively similar, though homogeneous sequences seem slightly" harder.[^n9] I did not read that supplement.
- Targets run only from 10 to 100, and the paper states "we test models on target numbers ranging from 10 to 100 in increments of 10".[^n10]
- The naming and production tasks differ in input as well as direction: one gets a string, the other a number. The gap may partly be an input-format effect. The paper's explanation is a suggestion, not a manipulation.
- Scale does not remove the gap. Llama accuracy rose from about 0.10 to 0.24 across 3B to 70B, and the authors say counting is "not strictly emergent in the classic sense of a sharp threshold or phase transition".[^n11]

## Related

- [[enumeration-cue-dependence]] — the cue decides whether a counting procedure runs at all; this note is the task-form axis of the same study.
- [[task-conditional-prompt-gain]] — a prompt gain that changes sign across tasks; here the task form changes how the model fails, not only how much it gains.

[^n1]: arxiv-2512-04727 — "the model is given a target numerical value and is asked to generate"
[^n2]: arxiv-2512-04727 — "it is more challenging to enumerate a given"
[^n3]: arxiv-2512-04727 — "still struggle with counting the number of elements in a given"
[^n4]: arxiv-2512-04727 — "reduced, suggesting that in such conditions the LLMs rely on similar approximate"
[^n5]: arxiv-2512-04727 — "they still get reasonably close to the target number"
[^n6]: arxiv-2512-04727 — "accurate in naming and production tasks involving words rather than letters"
[^n7]: arxiv-2512-04727 — "correspondence with the tokens provided as input to the models"
[^n8]: arxiv-2512-04727 — "aligned with recent findings that highlight the importance of tokenization"
[^n9]: arxiv-2512-04727 — "Performance is qualitatively similar, though homogeneous sequences seem slightly"
[^n10]: arxiv-2512-04727 — "we test models on target numbers ranging from 10 to 100 in increments of 10"
[^n11]: arxiv-2512-04727 — "not strictly emergent in the classic sense of a sharp threshold or phase transition"
