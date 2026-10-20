---
description: "Option-ID set, delimiter and separator choices that change no meaning reorder MLLM rankings on multiple-choice VQA benchmarks, even with order controlled by circular evaluation."
aliases: ["option format sensitivity", "MC-VQA prompt format sensitivity", "format-induced benchmark rank reversal", "option ID format effects"]
sources: ["arxiv-2511-22341"]
---
# Prompt-format rank instability

On a multiple-choice benchmark, a model's score depends on how its options are typeset into the prompt, not only on what they say. The option ID set (uppercase or lowercase letters, numbers, Roman numerals), the delimiter that joins each ID to its option (colon, dot, bracket, double brackets) and the separator between options can each change while the question and its options stay fixed. Rosenthal et al. combine these factors into 48 prompt formats for multiple-choice visual question answering (MC-VQA), "yielding 48 semantically equivalent prompt formats".[^c1] Across seven MLLMs and five datasets they report "frequent rank reversals even under order-invariant evaluation."[^c2]

The effect is large in their examples. LLaVA-OV "shifts from the second-lowest to the top" rank when the format changes,[^c3] with an accuracy difference of "nearly 50 percentage points" between formats.[^c4] The authors' summary is that "performance remains highly sensitive to semantically neutral prompt format choices".[^c5] The rank is the thing a benchmark reports, so a format choice that moves the rank changes the benchmark's conclusion without changing the question.

Option order is not the whole story. Earlier work on multiple-choice bias concerns order, and "existing work primarily focuses on option permutations or model calibration."[^c6] The authors control order with circular evaluation, and find that it "effectively mitigates option order preference."[^c7] The format instability remains: "This instability persists despite controlling for option-order effects through circular evaluation."[^c8] The paper's notation separates the two levers. A prompt is "F = (I, d, s), where d denotes the delimiter separating an option ID from its option text",[^c9] with I the ID set and s the separator, while the option permutation is a further term. My inference from this notation: order and format are independent parameters of one prompt, so a protocol that fixes only one of them leaves the other free.

Model size does not remove the effect. On V*Bench, Qwen2.5-VL-32B varies less than its 7B counterpart, "with an accuracy deviation of 2.6 pp compared to 7.1 pp,"[^c10] but Gemma-3-27B shows "increased sensitivity, with 5.9 pp deviation compared to 3.9 pp for the smaller model."[^c11] The authors conclude that increasing model size "does not consistently reduce prompt sensitivity."[^c12]

The authors place the cause below reasoning: "We trace this instability to low-level language modeling effects rather than changes in visual or semantic reasoning."[^c13] The first named mechanism is tokenization. Two patterns recur across formats: the option ID-delimiter pair "tokenizes" into more tokens than the model expects, and the tokenizer can "fail to preserve the option ID as a standalone token."[^c14][^c15] The authors read such atypical tokens as something that "may reduce evaluation stability."[^c16] Two further sources, the models' handling of option ID sets beyond familiar ones and the attention given to option IDs during selection, are named in the abstract: the choice of option ID sets "directly affects the reliability of attention patterns for option selection."[^c17] I did not check those analyses against their tables in this reading.

The same paper reads the instability as a symptom of what multiple-choice scores measure. "Accordingly, MC-VQA rankings correlate weakly"[^c18] with open-ended evaluation, and the authors take this to mean that "MC-VQA reflects option-selection dynamics"[^c19] as well as reasoning. They claim that MC-VQA "substantially overestimates multimodal reasoning ability."[^c20]

## Limits

- The 48 formats are one designed grid: four ID sets, four delimiters, three separators. They sample the space of prompt formats, not the whole of it. The paper notes that "there is no standardized format" for these elements,[^c21] so the grid is a choice, and a benchmark's real format is another point in the same space.
- The instability is not uniform. On MMBench and V*Bench "the top-ranked model remains stable,"[^c22] and HRBench-4K shows the most stable rankings. The effect is strongest in the lower and middle ranks on several datasets, so the claim is about rankings that are close, not about every leader.
- The scale test covers one dataset (V*Bench) and a few model families, including GPT-5.2 variants. Whether larger models behave the same on other benchmarks is not tested here.
- The mechanism is the authors'. The tokenization patterns are described; the paper's own wording is that they "may reduce evaluation stability," which is weaker than a demonstrated cause. The attention and generalisation accounts rest on analyses I did not read in full.
- Reversals show that a ranking depends on format. They do not show which format, or which ranking, reflects capability. My inference: a benchmark that reports one format's ranking has not established that ranking as the true one.
- Everything here is multiple-choice VQA with one optimised instruction prompt, "we use an optimized instruction prompt for all datasets."[^c23] Whether the effect carries to text-only multiple-choice or to open-ended answering is not tested in this work.

## Related

- [[permutation-consistency-training]] — the option-order axis that the multiple-choice literature already controls; this note is the axis it leaves out
- [[answer-format-dependent-bias-measurement]] — the answer type (closed, Likert, open) changes measured bias; this note is the typesetting inside one multiple-choice format
- [[mcq-answer-position-bias]] — when a model writes items, it places the correct option non-uniformly; a different positional effect, on the authoring side
- [[option-matching-shortcut]] — showing options at all changes how reasoning models answer; this note concerns how the shown options are typeset
- [[answer-option-surface-cue]] — option wording that a test-taker can exploit; here the surface of the ID and delimiter is what moves the score

[^c1]: arxiv-2511-22341 — "yielding 48 semantically equivalent prompt formats"
[^c2]: arxiv-2511-22341 — "frequent rank reversals even under order-invariant evaluation."
[^c3]: arxiv-2511-22341 — "shifts from the second-lowest to the top"
[^c4]: arxiv-2511-22341 — "with an accuracy difference of nearly 50 percentage points"
[^c5]: arxiv-2511-22341 — "performance remains highly sensitive to semantically neutral prompt format choices"
[^c6]: arxiv-2511-22341 — "existing work primarily focuses on option permutations or model calibration"
[^c7]: arxiv-2511-22341 — "we find that circular evaluation effectively mitigates option order preference."
[^c8]: arxiv-2511-22341 — "This instability persists despite controlling"
[^c9]: arxiv-2511-22341 — "F = (I, d, s), where d denotes the delimiter separating an option ID from its option text"
[^c10]: arxiv-2511-22341 — "with an accuracy deviation of 2.6 pp compared to 7.1 pp"
[^c11]: arxiv-2511-22341 — "increased sensitivity, with 5.9 pp deviation compared to 3.9 pp for the smaller model"
[^c12]: arxiv-2511-22341 — "does not consistently reduce prompt sensitivity."
[^c13]: arxiv-2511-22341 — "We trace this instability to low-level language modeling effects rather than changes in visual or semantic reasoning."
[^c14]: arxiv-2511-22341 — "the option ID-delimiter pair tokenizes"
[^c15]: arxiv-2511-22341 — "fails to preserve the option ID as a standalone token."
[^c16]: arxiv-2511-22341 — "may reduce evaluation stability."
[^c17]: arxiv-2511-22341 — "of option ID sets directly affects the reliability"
[^c18]: arxiv-2511-22341 — "Accordingly, MC-VQA rankings correlate weakly"
[^c19]: arxiv-2511-22341 — "MC-VQA reflects option-selection dynamics"
[^c20]: arxiv-2511-22341 — "MC-VQA substantially overestimates multimodal reasoning ability"
[^c21]: arxiv-2511-22341 — "there is no standardized format"
[^c22]: arxiv-2511-22341 — "the top-ranked model remains stable"
[^c23]: arxiv-2511-22341 — "we use an optimized instruction prompt for all datasets"
