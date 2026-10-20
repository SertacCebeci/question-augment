---
description: "Changing the number of worked examples in a code-refactoring prompt moved output form non-monotonically and per language; compilability, length and complexity had no common trend."
aliases: ["shot count", "k-shot setting", "number of in-context examples", "number of demonstrations"]
sources: ["arxiv-2511-21788"]
---
# In-context example count

A few-shot prompt is an instruction, a set of worked example pairs, and the test input. The number of pairs is a knob of its own. The refactoring study ran prompts "ranging from 0-shot to 10-shot"[^c1], each pair being a complex program with its refactored form: "are example pairs of complex and refactored code."[^c2] Which pairs fill the slots is a separate matter; the prompts were built with "selected example pairs embedded alongside" the test code.[^c3] The count, as a variable, is what this note concerns.

The measured effect is on the shape of the output, not on one quality score. In the zero-shot baseline, compilability sat in a narrow band, "between 88.67% (C#) and 92.67% (C++)."[^c4] Two examples moved it in opposite directions by language: "While C experiences a decline to 83%"[^c5], while the managed languages rose to "compilability rates of 94% and above."[^c6] The order changed again at six shots: "Java attains a compilability of 96%"[^c7], and "Python experiences a significant decline"[^c8] to 87.33%.

Length moved with the count as well. Lines of code "increase modestly for all languages, with particularly pronounced growth in C#."[^c9] The authors read the growth in C# as a shift toward output that is "more descriptive or boilerplate."[^c10]

What this gives someone asking is a dependence, not a slope. The count does not carry a direction that can be relied on: the authors summarize the C and C++ results as "reflecting more unpredictable outcomes."[^c11] My reading is that a count which helps one target language can hurt another, and that a shift seen at one count says little about the next. This is inference from the table, not a result the paper states.

## Limits

The sample is small. The dataset holds 10 code samples.[^c12] It has "2 samples each for C and C++, 3 for Python," and one each for C# and Java.[^c13] Per-language trends rest on one or two items. The text also states that "example prompts significantly alters the compilability trends,"[^c14] but the shot tables report means with spreads and no test I could find in the sections read; the word "significantly" is not backed by a stated test here.

The model is one variant: "We utilize the GPT-3.5-turbo-0125 model."[^c15] The shot sweep is run on a fine-tuned model, and the sections read do not separate what fine-tuning contributes from what the prompt contributes. The temperature was tuned over a range, "with 0.3 yielding optimal"[^c16] performance; the shot sweep appears at that one setting, and no shot-by-temperature grid appears in the read text. The count is therefore not isolated from temperature or from fine-tuning.

Compilability is a syntactic measure. The work checks outputs with online compilers and IDEs, and adds human review "to ensure syntactic correctness."[^c17] A program that compiles is not thereby correct, and this note does not claim a correctness effect of the count. The example selection rule is also not varied, so the note does not say whether a better choice of pairs would change the picture.

## Related

- [[demonstration-label-consistency]] — which demonstrations are chosen; this note concerns how many.
- [[similarity-selected-exemplars]] — a selection rule that this work does not isolate from the count.
- [[proof-depth-decline-under-shift]] — another sweep of shot counts from zero to five, on deduction accuracy rather than code form.
- [[search-induced-abstention-degradation]] — another report in which adding shots gave no significant gain.

[^c1]: arxiv-2511-21788 — "ranging from 0-shot to 10-shot"
[^c2]: arxiv-2511-21788 — "are example pairs of complex and refactored code"
[^c3]: arxiv-2511-21788 — "with selected example pairs embedded alongside"
[^c4]: arxiv-2511-21788 — "In the 0-shot baseline, compilability ranges narrowly between 88.67% (C#) and 92.67% (C++)"
[^c5]: arxiv-2511-21788 — "While C experiences a decline to 83%"
[^c6]: arxiv-2511-21788 — "compilability rates of 94% and above"
[^c7]: arxiv-2511-21788 — "Java attains a compilability of 96%"
[^c8]: arxiv-2511-21788 — "Python experiences a significant decline"
[^c9]: arxiv-2511-21788 — "increase modestly for all languages, with particularly pronounced growth in C#"
[^c10]: arxiv-2511-21788 — "that the model tends to produce more descriptive or boilerplate"
[^c11]: arxiv-2511-21788 — "reflecting more unpredictable outcomes"
[^c12]: arxiv-2511-21788 — "We curated a dataset D consisting of 10 code samples from"
[^c13]: arxiv-2511-21788 — "The dataset includes 2 samples each for C and C++, 3 for Python,"
[^c14]: arxiv-2511-21788 — "example prompts significantly alters the compilability trends"
[^c15]: arxiv-2511-21788 — "We utilize the GPT-3.5-turbo-0125 model"
[^c16]: arxiv-2511-21788 — "with 0.3 yielding optimal"
[^c17]: arxiv-2511-21788 — "as well as human evaluation to ensure syntactic correctness"
