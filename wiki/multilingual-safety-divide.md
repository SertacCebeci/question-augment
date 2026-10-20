---
description: "Translating harmful requests into a low-resource language once bypassed safety; a 2025 English-Hausa audit found the change depends on the model, and one model was safer in Hausa."
aliases: ["multilingual safety gap", "low-resource language jailbreak", "translation-based attack", "reverse linguistic vulnerability"]
sources: ["arxiv-2512-24556"]
---
# Multilingual safety divide

Safety alignment is often assumed to transfer from English to other languages. The early finding against that assumption was that it does not. Wang et al. and Yong et al. report that attackers "could bypass safety filters simply by translating harmful queries into low-resource" languages.[^c1] Yong et al. "documented a 79%" success rate for translation-based attacks against GPT-4.[^c2] The mechanism proposed in that line of work is that a model does not understand the translated attack well enough to refuse it. That was the dominant failure mode in 2023.[^c3]

The 2025 audit tests whether this still holds. It renders each harmful base prompt in English and in Hausa, a low-resource language. The Hausa versions were drafted by native speakers, who adapted the phrasing to local dialect norms rather than translating mechanically.[^c4] Of the 259 prompt instances that were safe in English, 35 became unsafe in Hausa, a drift rate of 13.5%.[^c5]

The gap is not uniform across models. GPT-5.1 showed the expected pattern: "GPT-5.1 shows the largest language-dependent vulnerability, with safety dropping (14.6" percentage points from English to Hausa.[^c6] Claude 4.5 Opus went the other way: "Claude 4.5 Opus performs better in Hausa than in English (+7.5%), suggesting different" alignment transfer.[^c7] Gemini 3 Pro showed no gap, but only because it performed poorly in both languages. The authors put it this way: "linguistic parity, but only because it performed poorly in all languages (26.7% baseline)."[^c8]

The authors therefore conclude that the divide is not a universal property of the models in 2025: "we did not observe universal degradation" of safety in low-resource languages.[^c9] Their hypothesis for the shift is that prior adversarial research served as training signal, so the divide "was a temporary alignment artifact rather than an inherent flaw": "We hypothesize that this shift indicates a remediation feedback loop."[^c10] For Claude's higher Hausa safety they propose uncertainty-driven refusal: the higher safety is "likely due to conservative refusal behaviors triggered by" linguistic uncertainty.[^c11]

## What survives and what does not

What survives the update is that the language of a request is a variable a safety evaluation has to hold fixed. A result measured in English does not tell how a model treats the same request in another language, and the sign of the difference can differ between models. What does not survive is the single-direction claim that low-resource languages are a backdoor for all models.

## Limits

- The two-language comparison is one pair: English and Hausa, with Standard Hausa only. The authors note that "our formal Hausa prompts likely represent a lower bound on real-world vulnerability."[^c12] Non-standard or code-mixed varieties are not tested in the slices I read.
- The abstract and the body give different Claude figures. The abstract reports "Claude 4.5 Opus proving significantly safer in Hausa (45.0%) than" in English at 36.7%.[^c13] The body reports Hausa 44.6% against English 37.1%.[^c14] I take the body's table figures as the reference; the discrepancy is unresolved in the text.
- Refusal under linguistic uncertainty is the authors' hypothesis. They write "We hypothesize that these signals activate a conservative refusal response," and the study does not probe internal states to test it.[^c15]
- Scoring used an automated judge, "Gemini 2.5 Flash, calibrated to a strict" safety rubric.[^c16] The judge's behaviour in Hausa is not separately validated in the slices read.
- Three models, one snapshot each, 480 prompts per model, so each language-by-model cell is a small sample. Differences of a few points between models are not tested for significance in what I read (my reading).

## Related

- [[temporal-framing-safety-asymmetry]] — the other axis of the same audit; the paper reports language and tense interacting.
- [[script-level-obfuscation]] — a different surface change, an orthographic one, that also shifts a model's safety judgement, measured in Chinese.
- [[forced-choice-safety-collapse]] — a reformulation that keeps the request fixed and changes its format, with a similar effect on refusal.

[^c1]: arxiv-2512-24556 — "could bypass safety filters simply by translating harmful queries into low-resource"
[^c2]: arxiv-2512-24556 — "who documented a 79%"
[^c3]: arxiv-2512-24556 — "models simply did not understand the translated attacks well enough to refuse"
[^c4]: arxiv-2512-24556 — "native Hausa speakers were employed to draft the low-resource equivalents, preserving"
[^c5]: arxiv-2512-24556 — "Of these, 35 became unsafe when translated into Hausa"
[^c6]: arxiv-2512-24556 — "GPT-5.1 shows the largest language-dependent vulnerability, with safety dropping (14.6"
[^c7]: arxiv-2512-24556 — "Claude 4.5 Opus performs better in Hausa than in English (+7.5%), suggesting different"
[^c8]: arxiv-2512-24556 — "linguistic parity, but only because it performed poorly in all languages (26.7% baseline)."
[^c9]: arxiv-2512-24556 — "we did not observe universal degradation"
[^c10]: arxiv-2512-24556 — "We hypothesize that this shift indicates a remediation feedback loop"
[^c11]: arxiv-2512-24556 — "likely due to conservative refusal behaviors triggered by"
[^c12]: arxiv-2512-24556 — "our formal Hausa prompts likely represent a lower bound on real-world vulnerability."
[^c13]: arxiv-2512-24556 — "Claude 4.5 Opus proving significantly safer in Hausa (45.0%) than"
[^c14]: arxiv-2512-24556 — "performing better in Hausa (44.6%) than in English (37.1%)."
[^c15]: arxiv-2512-24556 — "We hypothesize that these signals activate a conservative refusal response."
[^c16]: arxiv-2512-24556 — "Gemini 2.5 Flash, calibrated to a strict"
