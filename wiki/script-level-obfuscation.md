---
description: "Rewriting a Chinese harmful query's sensitive span as pinyin, homophones, symbol splits or zero-width characters keeps its intent; ten lightweight LLMs then answer about a third unsafely."
aliases: ["Chinese-specific adversarial patterns", "pinyin mix attack", "character-level obfuscation"]
sources: ["arxiv-2601-00588"]
---
# Script-level obfuscation of harmful queries

A harmful request can keep its intent while the words that trigger a filter are respelled at the level of script rather than meaning. CSSBench builds four such rewrites for Chinese. Pinyin replaces a sensitive word, in full, as initial letters, or mixed with characters inside one span. Homophones swap a sensitive word for a near-sound equivalent. Symbol mixing writes parts of a term in "mixed writing with Latin letters, digits, or emoji,"[^c1] sometimes with spaces that split the term. Zero-width insertion places "insertion of zero-width characters within"[^c2] a sensitive term, so the characters the model reads differ from what a reader sees.

The authors' premise is that these forms are how the harmful intent actually arrives. Real Chinese malicious queries "typically conceal intent via homophones, pinyin, symbol-based" splitting,[^c3] and the variations Chinese allows are the ones "that allow adversaries to circumvent safety guardrails, including homophones,"[^c4] which guardrails tuned on English phrasing do not cover. The mechanism the authors give is that a guard keys on surface character patterns, so a rewrite that keeps the meaning can pass it. The paper does not isolate that mechanism; it shows the effect and leaves the cause as the authors' reading.

What was measured: ten widely used Chinese lightweight LLMs were run on malicious queries in six domains, each rewritten under these patterns, and on a set of 250 borderline benign queries. Across models, attack success "roughly from 31 to 39" and "about one in three obfuscated malicious prompts still receives unsafe answers even"[^c5] when the models' own safety behaviour is on. The pattern matters. Pinyin and Symbol Mixing give the highest average attack success, mostly in the mid thirties; Homophone and Zero-width are lower, in the high twenties or low thirties. The authors read this as "phonetic rewriting and mixedscript forms are generally the most effective at" getting past character-level heuristics.[^c6] Robustness is not uniform across patterns: some systems acquire "relatively patternagnostic robustness,"[^c16] while "others remain vulnerable to specific classes of obfuscation such as" pinyin or symbol mixing.[^c7]

The metric is a pair. Attack success is "jailbreak evaluation as the proportion of responses" that comply unsafely,[^c8] and over-refusal is the share of borderline prompts refused. A composite error rate, a weighted micro-average of both error types, puts the models in one ranking; it "micro-averages errors" over malicious and borderline queries together.[^c9] Overall composite error ranges "from about 30.6 to 47.4" across the models.[^c10]

## Limits

- The judge is a model. Responses were labelled by "judge with Qwen3Guard-Gen-8B, a multilingual"[^c11] safety model. The authors avoid keyword rules because they "misclassify borderline but helpful answers as refusals, or miss refusals without common keywords."[^c12] The sections read report no agreement with human labels, so every attack-success figure is the judge's reading.
- A low attack success is not, by itself, safety. The authors warn that low attack success can be "aggressive rejection even on malicious queries."[^c13] The appendix makes the same point about Hunyuan-0.5B, which has among the lowest attack success and is known from the main results "to suffer from very high over-refusal, which means"[^c17] that its low figure is partly rejection. Any pattern's attack success has to be read with over-refusal beside it.
- The gap to plain queries is asserted, not measured in the sections read. The authors say benchmarks on unperturbed queries "may overestimate safety and miss failures that occur once attackers query with these patterns."[^c14] I found no paired comparison of the same malicious queries in plain and obfuscated form, so the size of that gap is not shown here.
- The variants were produced by a model rewriting under a structured instruction. The paper calls the patterns "common cases in deployments,"[^c15] but does not measure how often real attackers use them. Whether these rewrites match real attacks is an assumption.
- Scope. Chinese only; ten lightweight models; default behaviour under greedy decoding, single-turn prompts and no safety system message. Whether the effect is specific to Chinese script or holds for any orthographic change in another language is not tested here.

## Related

- [[minimal-edit-prompt-attack]] — another surface-level attack, but semantic and LLM-driven; there success tracks the model's confidence margin, a quantity this paper does not measure.
- [[informed-abstention-framework]] — the same joint-reporting point, unsafe compliance and over-refusal read together, made there for agent tool calls.
- [[llm-red-teaming]] — the wider practice of probing a model from outside with adversarial inputs, of which these variants are one case.

[^c1]: arxiv-2601-00588 — "mixed writing with Latin letters, digits, or emoji,"
[^c2]: arxiv-2601-00588 — "insertion of zero-width characters within"
[^c3]: arxiv-2601-00588 — "real-world Chinese malicious queries typically conceal intent via homophones, pinyin, symbol-based"
[^c4]: arxiv-2601-00588 — "that allow adversaries to circumvent safety guardrails, including homophones,"
[^c5]: arxiv-2601-00588 — "about one in three obfuscated malicious prompts still receives unsafe answers even"
[^c6]: arxiv-2601-00588 — "phonetic rewriting and mixedscript forms are generally the most effective at"
[^c7]: arxiv-2601-00588 — "others remain vulnerable to specific classes of obfuscation such as"
[^c8]: arxiv-2601-00588 — "jailbreak evaluation as the proportion of responses"
[^c9]: arxiv-2601-00588 — "a model on CSSBench: it micro-averages errors"
[^c10]: arxiv-2601-00588 — "Overall CER ranges from about 30.6 to 47.4"
[^c11]: arxiv-2601-00588 — "judge with Qwen3Guard-Gen-8B, a multilingual"
[^c12]: arxiv-2601-00588 — "misclassify borderline but helpful answers as refusals, or miss refusals without common keywords."
[^c13]: arxiv-2601-00588 — "aggressive rejection even on malicious queries."
[^c14]: arxiv-2601-00588 — "may overestimate safety and miss failures that occur once attackers query with these patterns"
[^c15]: arxiv-2601-00588 — "patterns are common cases in deployments"
[^c16]: arxiv-2601-00588 — "relatively patternagnostic robustness"
[^c17]: arxiv-2601-00588 — "to suffer from very high over-refusal, which means"
