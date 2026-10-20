---
description: "A figure-only QA generator leans on prior knowledge and writes questions the figure does not entail; the remedy is to give it the figure-citing paragraphs that hold the missing context."
aliases: ["information asymmetry", "figure-only generation gap", "context asymmetry in QA synthesis", "information asymmetry in question generation"]
sources: ["arxiv-2511-19899"]
---
# Generation-context asymmetry

A question-answer pair is generated from some input, and the answer is then judged against what the answer actually depends on. When the input carries less than the answer depends on, the generator fills the gap from elsewhere. For figures in scientific papers the input is usually the figure and its caption, while the paragraphs that cite the figure hold the symbols, settings and intended takeaway. The paper calls the resulting mismatch information asymmetry: "This mismatch causes the LVLM to over-rely on its prior knowledge".[^a1] The figure shows the data; the body text says what the figure is for. A generator that sees only the first writes questions whose answers the figure does not settle.

The mechanism, as the authors state it: the model receives the figure and caption, "omitting essential figure-associated context that authors describe" in the body, and "may over-rely on its broad knowledge and generate QA pairs that" extend past what the figure shows.[^a2] These are questions that look answerable but whose answers need the paper, not the figure.

The paper measured the symptoms in a small audit. It took 100 items from ArXivQA and sorted the erroneous ones. Incorrect visual grounding came first with "Incorrectly Visually Grounded (19/100)", then "Non-Visual (6/100)" for items answerable without the figure, and the figure-intent and outside-knowledge categories made up the rest.[^a3] The authors put the overall error rate at "it still exhibits a 37%"[^a4] and attribute the errors to two sources. Asymmetry leads to the outside-context errors, in their words "extend beyond what the figure alone conveys, leading to E2–E4".[^a8] Hallucination accounts for the visual-grounding errors and for E2, since the first two failure modes "stem directly from this phenomenon", as the paper puts it.[^a9]

Adding context is one remedy the paper examines. Prior work (SPIQA) gives the generator the figure-citing paragraphs, and the authors grant that this helps but leave a gap: "adding figure-citing paragraphs alone reduces information asymmetry but does not prevent visually unsupported" pairs from entering the data.[^a5] The proposed fix is to generate questions from the text that cites the figure, so the generator never has to supply the missing context from its own prior, then to check the answers against the figure.[^a6]

## Limits

- The audit is 100 items from one dataset, and the labels are the authors' own judgement of erroneous items. The stored answer the audit checks is the LVLM's own output, a prediction "rather than ground truth",[^a7] so the categories say what the authors judged wrong, not an independently verified error rate.
- The asymmetry is argued from the error categories, not isolated by experiment. In the sections read, the ablations vary filtering stages, not the context given to a figure-only generator, so the claim that context alone removes E2–E4 errors is not tested.
- Context does not remove the generator's errors. The paper says of SPIQA that it "mitigates information asymmetry by incorporating figure-citing paragraphs as context, but does not verify" its answers, which is why the remedy is paired with verification (see [[decoupled-modality-verification]]).
- The concept as stated comes from one arXiv-figure setting. Whether the same gap appears when a generator is given other kinds of source material is not shown here; this is my inference from the design, not a finding of the paper.

## Related

- [[decoupled-modality-verification]] — the paper's other root cause, hallucination; the text-only generator addresses asymmetry, the vision check addresses hallucination, and the two are separate questions.
- [[question-generation-as-policy]] — what a question generator is shown decides which evidence its questions can reach, a related dependence of question content on the generator's input.
- [[cross-modal-aggregation-gap]] — a caution that one channel is not automatically enough: figure and caption together do not beat either alone for verifying a claim.

[^a1]: arxiv-2511-19899 — "This mismatch causes the LVLM to over-rely on its prior knowledge"
[^a2]: arxiv-2511-19899 — "omitting essential figure-associated context that authors describe"
[^a3]: arxiv-2511-19899 — "Incorrectly Visually Grounded (19/100)"
[^a4]: arxiv-2511-19899 — "it still exhibits a 37%"
[^a5]: arxiv-2511-19899 — "information asymmetry but does not prevent visually unsupported"
[^a6]: arxiv-2511-19899 — "generate QA from figure-citing paragraphs to mitigate information asymmetry, and verify against figures to enforce visual grounding"
[^a7]: arxiv-2511-19899 — "rather than ground truth"
[^a8]: arxiv-2511-19899 — "extend beyond what the figure alone conveys, leading to E2–E4"
[^a9]: arxiv-2511-19899 — "from this phenomenon. Methods such as ArXivQA rely solely on"
