---
description: "How explicit a prompt is changes LLM reasoning accuracy unevenly: large gains on procedural tasks, almost none on open-ended ones, and larger gains for smaller models."
aliases: ["prompt specificity", "degree of explicitness", "prompt vagueness", "prompt detail effect"]
sources: ["arxiv-2512-02246", "arxiv-2511-17722"]
---
# Prompt specificity effect

A prompt can be more or less specific: more or less detailed about the steps, the constraints and the form of the answer. The DETAIL paper treats this as a continuous dimension. It takes a detailed prompt and rewrites it through repeated LLM calls into increasingly vague versions, giving three levels per task.[^p1] The reported result is that specificity helps, but not evenly: it "improves accuracy, especially for smaller models and procedural" tasks.[^p2]

The paper does not spell out a mechanism. My reading is that explicit detail supplies structure the model would otherwise have to produce on its own: a vague prompt leaves that structure to the model, a detailed one hands it over. On that reading the effect should be largest where the task has a fixed procedure (my inference). The measured gradient from vague to detailed prompts fits this. Math word problems gain +0.47 and logic puzzles +0.36,[^p3] code understanding gains +0.29,[^p4] commonsense inference only +0.08,[^p5] and decision-making +0.02.[^p6] The authors read the last case as one where detail can cost something: "over-specification may constrain rather" than help the model.[^p7] The same tension is named at the start of the paper, where detailed prompts "may also constrain the model’s reasoning pathways."[^p8]

The model is a second axis. The smaller model in the study depended on specificity much more than the larger one. Going from vague to detailed prompts, GPT-4 rises from 0.60 to 0.83 at baseline, and O3-mini from 0.34 to 0.68 (my reading of Table 1). The authors read the gap as a matter of capacity: O3-mini shows it "heavily depend on explicit external" structure,[^p18] while GPT-4 "is capable of internally compensating for" under-specification.[^p19] Structured prompting narrows the gap for vague prompts. The paper says Self-Consistency and Chain-of-Thought "compensates for vague prompts by guiding or diversifying the model’s reasoning paths."[^p9]

Specificity is measured with perplexity, under GPT-2-medium. The paper takes perplexity as "a proxy for linguistic predictability and familiarity."[^p10] Lower perplexity means more generic phrasing, and the rewriting produces "a monotonic decrease in perplexity from" the detailed level to the vague one.[^p11]

What transfers beyond this setting is the idea that the explicitness of a question is a variable to be set, and that the right setting depends on the task and on the answerer. The same broad-versus-narrow trade appears in [[query-specificity-menu]], where the query is a retrieval search rather than a reasoning prompt. The detail that is missing from a question is also what [[underspecified-question-eager-answering]] describes, where models answer instead of asking. The present note concerns what detail does to the answer once it is given.

The sign of the effect can change with what the detail names. In a synthetic visual counting benchmark, prompts add color, texture or shape to a count question, and specificity behaves differently by feature type. For background features it "consistently improves performance," with background texture giving the largest gains.[^p20] For object texture it is "the only category where specificity monotonically degrades accuracy across all models."[^p21] The authors read the split as a matter of what the added detail does to the segmentation of the objects: specificity "aids counting when it simplifies visual segmentation (background cues)"[^p22] but "becomes detrimental when it introduces competing object-level processing demands."[^p23] That account is the one in [[segmentation-cue-load]]. This is a different setting from the reasoning prompts above. The detail describes the image, not the steps, and the measure is count error, not a reasoning score. Whether the same sign change holds for reasoning prompts is not tested in that paper, so the two results do not form one curve.

## Limits

Specificity is confounded with length and content. The rewriting changed the prompts' size: "Average prompt length: Level-3 (124 tokens)," against 57 tokens at Level-1.[^p12] A gain could come from the added words or from the changed content as much as from specificity as such. The paper does not separate these (my inference from the design).

The measure is one the authors themselves call a heuristic. Their future-work list proposes to "replace current heuristics like perplexity alone" with measures such as entropy or syntactic structure.[^p13] Perplexity under a small model reflects how familiar the wording is, which is not the same as how much detail a prompt carries. A short, common phrasing can score as "specific" or "vague" by its wording alone (my inference; see [[generative-likelihood-evaluation]] for the same familiarity confound in a different setting).

The tasks and prompt variants were generated by API-driven "LLM calls without manual validation."[^p14] Correctness is judged by a GPT-3.5 semantic-equivalence step whose reliability "is not formally validated and may be biased by" the judge's own phrasing preferences.[^p15] The study covers 30 tasks, two models, three levels, and three repeats. The authors state that "We were unable to perform ablation studies, hyperparameter tuning, or" repeated sampling for confidence intervals, and they say the differences "should be interpreted directionally rather than conclusively."[^p16]

The per-category gains, including the near-zero decision-making result, are measured on this one task set. They do not show that open-ended tasks in general are indifferent to detail. The framework also "assumes controlled prompting conditions,"[^p17] while in practice vagueness is often unintentional, so the gradient described here may not describe real user prompts.

## Related

- [[query-specificity-menu]] — the same broad-versus-narrow trade, set per retrieval query rather than per reasoning prompt
- [[underspecified-question-eager-answering]] — missing detail makes models answer where they should ask; this note is about how much detail helps once it is supplied
- [[selective-abstraction]] — trades specificity for reliability in the content of an answer; here specificity is an input setting
- [[generative-likelihood-evaluation]] — the likelihood measure behind the paper's specificity proxy, and its familiarity confound
- [[segmentation-cue-load]] — the visual counting case, where specificity about the objects loads the count and specificity about the background helps it

[^p1]: arxiv-2512-02246 — "transforms highly detailed prompts into increasingly vague versions through iterative LLM calls."
[^p2]: arxiv-2512-02246 — "especially for smaller models and procedural"
[^p3]: arxiv-2512-02246 — "+0.47 and +0.36 gain respectively."
[^p4]: arxiv-2512-02246 — "Code Understanding also benefits (+0.29),"
[^p5]: arxiv-2512-02246 — "Commonsense Inference shows only a modest gain (+0.08), indicating that such tasks"
[^p6]: arxiv-2512-02246 — "Decision-Making Scenarios exhibit almost"
[^p7]: arxiv-2512-02246 — "suggests that for open-ended or ethical reasoning, over-specification may constrain rather"
[^p8]: arxiv-2512-02246 — "they may also constrain the model’s reasoning pathways."
[^p9]: arxiv-2512-02246 — "compensates for vague prompts by guiding or diversifying the model’s reasoning paths."
[^p10]: arxiv-2512-02246 — "which serve as a proxy for linguistic predictability and familiarity."
[^p11]: arxiv-2512-02246 — "a monotonic decrease in perplexity from"
[^p12]: arxiv-2512-02246 — "Average prompt length: Level-3 (124 tokens),"
[^p13]: arxiv-2512-02246 — "to replace current heuristics like perplexity alone."
[^p14]: arxiv-2512-02246 — "LLM calls without manual validation."
[^p15]: arxiv-2512-02246 — "is not formally validated and may be biased by"
[^p16]: arxiv-2512-02246 — "interpreted directionally rather than conclusively."
[^p17]: arxiv-2512-02246 — "The DETAIL framework assumes controlled prompting conditions,"
[^p18]: arxiv-2512-02246 — "heavily depend on explicit external"
[^p19]: arxiv-2512-02246 — "is capable of internally compensating for"
[^p20]: arxiv-2511-17722 — "For background features, specificity consistently improves performance"
[^p21]: arxiv-2511-17722 — "object texture is the only category where specificity monotonically degrades accuracy across all models"
[^p22]: arxiv-2511-17722 — "specificity aids counting when it simplifies visual segmentation (background cues)"
[^p23]: arxiv-2511-17722 — "but becomes detrimental when it introduces competing object-level processing demands"
