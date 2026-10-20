---
description: "Randomly recombining codebook components into many prompts and keeping the best on labelled training texts moved LLM-human agreement more than the add-on techniques tested did."
aliases: ["combinatorial prompt generation", "codebook-recombined prompt selection", "empirical prompt selection on training data"]
sources: ["arxiv-2512-03818"]
---
# Combinatorial empirical prompting

A baseline prompt for a text-classification task is the instruction a model gets before the text: some context, a task statement, a definition of the construct, inclusion and exclusion criteria, and a format line. Combinatorial empirical prompting does not write one such prompt and hope it works. The authors write several variants of each part, then draw prompts from them at random. For each prompt the draw is: one context variant (an empty string is allowed), one task variant, one definition variant, a random number of inclusion and exclusion criteria appended to the definition, then the formatting line.[^c1] The case study made 50 such prompts per construct, "codebook-guided, human-generated" prompts, and ran each on a labelled training set.[^c2] The authors describe the procedure as "empirically evaluating the resulting prompts" after systematically recombining codebook-derived parts.[^c3]

The mechanism is selection against human codes. The winning prompt is the one whose wording puts the model's yes/no boundary where the coders' boundary sits, judged by F1 on texts the coders already labelled. The headline claim is that selecting the best combination in a training set "substantially improves alignment between" LLM and human classifications.[^c4] The size of the effect is read from the spread across the 50 prompts. For negative core beliefs on gpt-5.4 the gap between the best and the worst reached 0.28 F1, from 0.55 to 0.83.[^c5] The smallest gap was 0.06, for meaning making on the same model.[^c6] The gap is widest where the construct is hardest: "Prompt composition appears to matter most when constructs are difficult to classify."[^c7]

Components trade recall against precision. One inclusion rule in the case study lowered recall by 0.13 and raised precision by 0.11, on average.[^c8] Across 71 tested components for three constructs, "only three components increased both precision and recall," and only by 0.01.[^c9] The authors' reading is that the search gains by "optimizing tradeoffs in recall-oriented and precision-oriented prompt components," not by finding components that are strictly good.[^c10] My inference from this, not the paper's wording: copying the winning prompt from one construct copies one point on a trade-off, not a rule about the construct.

The chosen prompt is picked on a training set and then scored on a separate development set. The top prompt "often still demonstrates substantial improvements" over the median prompt, in five of six cases, though rarely significantly.[^c11] Patterns held across the split: the training ranking carried over to development.[^c12] On overfitting the authors write that "while overfit may not be a concern, uncertainty" is the greater worry.[^c13] So the binding constraint is the labelled sample needed to tell prompts apart, more than the selection step itself.

The same study also let a model propose variants from a seed prompt and kept the best per generation. That helped mostly from a weak seed: "automatic prompt engineering is most useful when the initial baseline prompt is" weak.[^c14] The baseline search here is a random draw with no iteration; the iterated version is closer to [[evolutionary-prompt-search]].

## Limits

- The development sets are small. The authors say "our development datasets are not large enough to reliably identify small" prompting effects.[^c15] For negative core beliefs, "there are just 65 examples of negative core beliefs in our development dataset."[^c16]
- The labelled texts come from one expressive-writing sample. "the expressive writing texts for meaning making and negative core beliefs were generated only by women."[^c17] The authors argue the test was of the method, not of the best wording, so the winning wordings do not carry over as claims.
- Two models and three constructs. "what works in one scenario may not work in another," and "model capabilities are certain" to change.[^c18][^c19]
- Alignment with human codes is evidence, not validity: "classifications alone is not a comprehensive assessment of validity."[^c20]
- Cost: the authors call prompt engineering "time-consuming" and say it "should only" be done "when resources allow and when maximizing classification performance and" validity matters.[^c21]
- The variants were written by the authors: "we manually generated multiple variants of each."[^c22] The search covers only the wordings someone thought of.

## Related

- [[evolutionary-prompt-search]] — an iterated search over prompts with an LLM doing the variation; the random draw here has no generations
- few-shot-exemplar-combination — in the same study, the choice of example set was the second and larger lever after the baseline
- [[task-conditional-prompt-gain]] — whether a prompt technique helps depends on the task; the additive techniques in this study are the small-gain case

[^c1]: arxiv-2512-03818 — "Randomly select one context description variant"
[^c2]: arxiv-2512-03818 — "We repeated this process 50 times to produce 50 codebook-guided"
[^c3]: arxiv-2512-03818 — "empirically evaluating the resulting prompts"
[^c4]: arxiv-2512-03818 — "substantially improves alignment between"
[^c5]: arxiv-2512-03818 — "This difference in F1 reached as high as 0.28"
[^c6]: arxiv-2512-03818 — "the smallest difference was a 0.06 increase in F1 for meaning making on gpt-5.4"
[^c7]: arxiv-2512-03818 — "Prompt composition appears to matter most when constructs are difficult to classify."
[^c8]: arxiv-2512-03818 — "have a recall that is 0.13 lower on average but a precision that is 0.11"
[^c9]: arxiv-2512-03818 — "only three components increased both precision and recall"
[^c10]: arxiv-2512-03818 — "optimizing tradeoffs in recall-oriented and precision-oriented prompt"
[^c11]: arxiv-2512-03818 — "the top prompt often still demonstrates substantial improvements"
[^c12]: arxiv-2512-03818 — "patterns in performance generalize from the training datasets to the development datasets"
[^c13]: arxiv-2512-03818 — "while overfit may not be a concern, uncertainty"
[^c14]: arxiv-2512-03818 — "automatic prompt engineering is most useful when the initial baseline prompt is"
[^c15]: arxiv-2512-03818 — "our development datasets are not large enough to reliably identify small"
[^c16]: arxiv-2512-03818 — "there are just 65 examples of negative core beliefs in our development dataset"
[^c17]: arxiv-2512-03818 — "the expressive writing texts for meaning making and negative core beliefs were generated only by women"
[^c18]: arxiv-2512-03818 — "what works in one scenario"
[^c19]: arxiv-2512-03818 — "model capabilities are certain"
[^c20]: arxiv-2512-03818 — "classifications alone is not a comprehensive assessment of validity"
[^c21]: arxiv-2512-03818 — "be undertaken when resources allow and when maximizing classification performance and"
[^c22]: arxiv-2512-03818 — "we manually generated multiple variants of each"
