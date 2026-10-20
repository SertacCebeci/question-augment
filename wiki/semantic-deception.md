---
description: "Semantic load in a symbol-remapped addition can pull reasoning models into answering the sentence instead of computing, and it lowers accuracy on the addition even when the addition is recognized."
aliases: ["semantic load in symbol remapping", "semantic interference with symbol manipulation", "meaningful-symbol deception"]
sources: ["arxiv-2512-20812"]
---
# Semantic deception

A symbol that carries meaning of its own can take the place of the task it encodes. The experimental form is a remapping. Each digit and operator of a simple addition is swapped for a novel token, the swap table is given in the prompt, and the model must translate the expression and add it. What varies is the semantic load of the replacement tokens. Level 1 uses meaningless letter strings. Level 2 uses random words that form no sentence. Level 3 uses words that form an affirmative sentence expecting no reply. Level 4 uses words that form a request a model is built to answer, split into 4a (a long text is expected) and 4b (a one-word answer is expected).[^c1] The authors call the failure "semantic deception": the model answers the sentence, not the calculation. Their design isolates the cause: "the only thing that changes is the dictionary used to present the equation."[^c2]

The paper reads two different outcomes. The first is recognition: whether the model attempts the addition at all. Here the overall effect is small. "From level 1 to 3 LLMs always attempt to answer to the calculation," and the authors add that "this growth of errors is not" remarkable.[^c3][^c4] The exception is a subset of models. Only the two models with an integrated chain-of-thought, o1 and DeepSeek-r1, ever answered the sentence, and only at the top level.[^c5] The overall summary puts the level effect as "the more we advance into the levels, the more LLMs make mistakes."[^c6]

The second outcome is execution. Among responses that do attempt the addition, accuracy still depends on the level. The authors call this the "hidden effect": "the semantic deception is applicable to the execution of" the addition, and "It indicates that there are hidden effects."[^c7][^c8] This is the sharper finding for anyone who would judge a model by its answer. A model that has recognized the task can still fail the arithmetic when the surrounding symbols carry a stronger meaning.

The two measures do not line up with model type. The authors state that "we can not conclude anything about reasoning or" non-reasoning models from accuracy, because the reasoning model o1 is more accurate than GPT-4o, while the reasoning model r1 is less accurate than DeepSeek-V3.[^c9] Only the sentence-answering failure tracks the presence of an integrated chain-of-thought. The authors suggest that chain-of-thought may amplify the cue: "may indicate that CoT could have a bad influence."[^c10] The mechanism they offer is that repeating elements of the sentence inside the reasoning focuses attention on them. That is their conjecture, not something the experiment isolates.

My reading of the design is that semantic deception is a competition between the task the prompt sets and a prior that the surface content of a request provides. The arithmetic is held fixed across prompts, so any change in output comes from the content of the symbols. This is the sense in which the paper says LLMs "are prone to surface-level coherence that can mask deep reasoning failures."[^c11] For the wiki, the transferable concept is the gap between the form of a request and the operation it asks for. A question's surface meaning can be answered in place of its content. Whether the same happens to human-posed questions is not tested here.

## Limits

- Scale is small. The study uses "four LLMs, including two reasoning models," with five additions per level and each prompt repeated 10 times.[^c12] The authors note a limitation: "that we have not added variability in the way the exercises are presented."[^c13]
- The recognition effect is weak overall. A reader who looks only at whether models answer the calculation sees little effect; the accuracy result is the one that carries weight.
- Token choice is a confound. The authors concede "It is uncertain whether or not all symbols, like dots or questions marks" behave alike, and that formulations such as "answer in one word" could "impact greatly the results and also be considered testing something else than abstract" symbol manipulation.[^c14][^c15] Level 4a and 4b therefore differ in ways the design does not separate from request type.
- The chain-of-thought account is suggested, not tested. The comparison that supports it, v3 more accurate than r1, is between different models, so model family and chain-of-thought are confounded. The authors hedge with "may indicate."[^c10]
- The paper's broader verdict goes past the data. "These findings tend to confirm that" LLMs have no genuine reasoning capacities.[^c16] The measurement shows that a semantic cue can change behaviour on a trivial task. It does not measure whether a model reasons; the note takes the measurement and not the verdict.
- No human baseline is given, and the claimed application to high-stakes decisions (law, healthcare, education) is asserted, not measured.

## Related

- [[option-matching-shortcut]] — a visible candidate list lets reasoning models match instead of deduce; a surface cue takes the place of a derivation here too
- [[symbol-name-anchoring]] — names let agents skip recovering meaning, the same pattern of a lexical cue replacing the underlying work, in binary analysis
- [[refusal-shortcut-learning]] — safety-tuned reasoning models bind refusals to trigger words rather than to intent
- [[distractor-similarity-reasoning-inflation]] — similar irrelevant context lowers reasoning-model accuracy while adding reasoning tokens

[^c1]: arxiv-2512-20812 — "Symbols are words that combined together form a request that LLMs are"
[^c2]: arxiv-2512-20812 — "the only thing that changes is the dictionary used to present the equation"
[^c3]: arxiv-2512-20812 — "From level 1 to 3 LLMs always attempt to answer to the calculation"
[^c4]: arxiv-2512-20812 — "However, this growth of errors is not"
[^c5]: arxiv-2512-20812 — "the fact that only o1 and r1-the two models with integrated CoT-sometimes generate"
[^c6]: arxiv-2512-20812 — "the more we advance into the levels, the more LLMs make mistakes"
[^c7]: arxiv-2512-20812 — "the semantic deception is applicable to the execution of"
[^c8]: arxiv-2512-20812 — "It indicates that there are hidden effects"
[^c9]: arxiv-2512-20812 — "we can not conclude anything about reasoning or"
[^c10]: arxiv-2512-20812 — "may indicate that CoT could have a bad influence"
[^c11]: arxiv-2512-20812 — "they are prone to surface-level coherence that can mask deep reasoning failures"
[^c12]: arxiv-2512-20812 — "experiments with four LLMs, including two reasoning models"
[^c13]: arxiv-2512-20812 — "that we have not added variability in the way the exercises are presented"
[^c14]: arxiv-2512-20812 — "It is uncertain whether or not all symbols, like dots or questions marks"
[^c15]: arxiv-2512-20812 — "impact greatly the results and also be considered testing something else than abstract"
[^c16]: arxiv-2512-20812 — "These findings tend to confirm that"
