---
description: "A narrated rationale is kept only if each sentence's variables, values and control-flow words match the program's execution trace, so training text is checked against what the code did."
aliases: ["trace-grounded CoT verification", "execution-grounded rationale verification", "trace-grounded rationale filter", "verified chain of thought"]
sources: ["arxiv-2512-00127"]
---
# Execution-trace rationale verification

A rationale written about a program can be checked against the program's own record of what it ran. In arxiv-2512-00127 the record is produced by instrumenting each solution with pysnooper, which captures function entry, every executed line, variable assignments with their state transitions, and return values. The paper calls the result "a ground-truth record of the program".[^c1]

The rationale is then written from that record rather than from nothing. The narration step translates the trace: "Notably, the model translates factual execution rather than generating from scratch."[^c2] The check runs afterwards, on the text. Since rationale sentences do not line up one-to-one with trace lines, the paper uses a window rather than a line match.[^c3] For each sentence, an LLM extracts the verifiable entities, meaning variable names, values and control-flow keywords, and each one is looked up in a lookahead window of the trace.[^c4][^c5] Separately, the predicted input and output in the rationale are string-matched against the test's ground-truth I/O. "Rationales failing either check are discarded."[^c6]

What the check verifies is the factual content of each sentence: that the names and values it cites occur in the recorded run, in the right region. It does not verify a reasoning chain as a whole.

The measured effect is in one ablation. On Qwen2.5-Coder-7B, the paper compares rationales from an LLM with no trace against its full pipeline on LiveCodeBench-Exec. "First, execution grounding matters most", and "LLM-generated CoT without trace grounding (59.3 on LCB) lags" behind the full approach, which reaches "well behind our full approach (68.2)."[^c7][^c8][^c9] The no-trace arm is a judge baseline: for each problem it generates several CoT candidates and "use[s] a judge model to select the best rationale-and-answer pair".[^c10] So the comparison sets trace-checked text against judge-selected text. It does not isolate the trace from the candidate selection that the judge also performs.

## Limits

- The ablation is one base model, and the paper's own setup is stated that way: "fine-tuned models use 25k bi-directional data. Tested on" Qwen2.5-Coder-7B.[^c11] The sections read do not show the same ablation on a second model.
- The method is Python-only at present: "current implementation targets Python because it" offers a tracing layer.[^c12] The paper argues the verification step transfers to other languages, but that claim is not tested in the text read.
- The verifier is itself a model call for entity extraction, so the check depends on a model's reading of which entities a sentence contains. The window algorithm is given in an appendix that was not in the text read.
- The check confirms that what a sentence names occurs in the record. It does not confirm that the causal link between two sentences is right, so a rationale that cites the right variables and values for a wrong reason would pass. This is my inference; the paper does not test it.
- The sections read do not report how many rationales the window check rejects, so the filter's cost on the 54,000-item set is unknown from this text.

## Related

- [[program-computed-ground-truth]] — the answer key there is a program run over stored geometry; here the same kind of run supplies the reference the narration is checked against.
- [[phase-wise-trace-correctness]] — scores a reasoning trace stage by stage against ground truth as an evaluation; this is the same comparison used as a filter on training text.
- [[object-grounded-trace-scoring]] — matches the objects a visual trace names against a reference mask, the nearest analogue of matching named entities to a record.
- [[executable-answer-verification]] — runs an interpreter on final answers; this runs a record check on the reasoning text.
- [[cot-hallucination-trap]] — fluent rationales that follow the question's cues rather than the evidence; the failure this check is built to catch in code.
- bidirectional-cot-training — the same pipeline's backward items, which are deduced from an output and so are not narrations of a trace.

[^c1]: arxiv-2512-00127 — "a ground-truth record of the program"
[^c2]: arxiv-2512-00127 — "rather than generating from scratch"
[^c3]: arxiv-2512-00127 — "sentences do not map one-to-one to trace lines, we"
[^c4]: arxiv-2512-00127 — "using an LLM, then check each entity against a"
[^c5]: arxiv-2512-00127 — "lookahead window in the trace."
[^c6]: arxiv-2512-00127 — "Rationales failing either check are discarded"
[^c7]: arxiv-2512-00127 — "First, execution grounding matters most"
[^c8]: arxiv-2512-00127 — "LLM-generated CoT without trace grounding (59.3 on LCB) lags"
[^c9]: arxiv-2512-00127 — "well behind our full approach (68.2)."
[^c10]: arxiv-2512-00127 — "use a judge model to select the best"
[^c11]: arxiv-2512-00127 — "fine-tuned models use 25k bi-directional data. Tested on"
[^c12]: arxiv-2512-00127 — "current implementation targets Python because it"
