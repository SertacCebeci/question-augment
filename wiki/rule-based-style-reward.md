---
description: "Explanation style scored by surface formulas, a readability grade cap and a politeness-marker density, serves as a reward that needs no human-scored explanations or learned reward model."
aliases: ["rule-based tone metric", "formula-scored style reward", "Flesch-Kincaid reward", "surface-formula tone reward"]
sources: ["arxiv-2601-04208"]
---
# Rule-based style reward

Style can be scored without a human rater or a learned judge, by applying surface formulas to the text. In the LEXMA study the consumer explanation is scored on two such formulas. Readability is binary: the explanation earns the reward when its Flesch–Kincaid grade level is at most 8. That formula "depends on average sentence length and average syllables per word."[^c1] Politeness is a density: the "rule-based density of politeness markers" is counted over tokens, matched against a taxonomy of strategies such as gratitude expressions and deference markers.[^c2] The density is multiplied by four and capped at 1, so that the two terms share the range [0, 1] and carry comparable weight, and their sum is the tone reward.[^c3]

The design choice is what it avoids. The decision reward is computed from ground-truth labels, and the tone reward from these formulas. The authors say this "avoids the need for human-scored explanation labels or learned reward models."[^c4] A style target therefore becomes a cheap, repeatable training signal that does not need a corpus of scored explanations, which is the label-efficiency problem the paper starts from.

The cap on politeness is a deliberate guard against gaming. The authors want messages that are "overloaded with formulaic cues" to score no higher than polite ones.[^c5] Without the cap, a generator could raise the reward by stacking marker phrases, which would satisfy the formula without being more courteous.

The reported effect is that tone tuning "drives readability to plain-language levels and raises politeness while keeping the decision fixed."[^c6] Here the formula is the measurement, and the claim is about what the formula measures.

What the mechanism gives, in my reading, is a property that a formula can approximate becoming a label-free training target. What it does not give is any evidence that the formula captures what a reader experiences as plain or respectful. Readability as sentence and syllable length does not see meaning, so a short, confusing sentence scores as plain. Politeness as marker density sees phrases, not intent. The cap limits one kind of gaming and does nothing about the others.

Compared with an LLM judge, a formula trades bias for crudeness. A judge can read meaning but carries the biases catalogued in [[llm-judge-biases]]. A formula is stable and cheap but measures only the surface that the formula can see.

## Limits

- The readability cutoff of 8 and the politeness scale of 4 are set by the authors, with the cutoff justified by convention. The text I read gives no sensitivity test of either constant (my reading).
- The readability formula and the dictionary approach are borrowed from finance text work, cited as Loughran and McDonald 2014 for the dictionary method. Their validity for consumer explanations is not tested here.
- The formulas are not checked against the paper's own human ratings of clarity and politeness in the text I read. The formulas and the human results are reported separately, so agreement between them is assumed, not shown (my reading).
- The reward is binary for readability, so an explanation just under the cutoff and one far under it are scored the same.
- One study, one domain, one model. The cap and the cutoff have not been compared against other formulas.

## Related

- [[decision-fixed-audience-adaptation]] — the tone adapter that this reward trains, with the decision held fixed
- [[llm-judge-biases]] — the judged alternative that formula scoring avoids, at the price of measuring less
- [[outcome-credit-through-explanation]] — the decision-side reward that runs alongside this one in the same training

[^c1]: arxiv-2601-04208 — "on average sentence length and average syllables per word"
[^c2]: arxiv-2601-04208 — "the rule-based density of politeness markers"
[^c3]: arxiv-2601-04208 — "We multiply this density by four and cap the result at 1"
[^c4]: arxiv-2601-04208 — "This avoids the need for human-scored explanation labels or learned reward models"
[^c5]: arxiv-2601-04208 — "overloaded with formulaic cues"
[^c6]: arxiv-2601-04208 — "Tone tuning drives readability to plain-language levels and raises politeness while"
