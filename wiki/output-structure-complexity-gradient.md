---
description: "Zero-shot JSON format compliance falls as the requested output grows from a scalar to lists and composite objects, with high variance by model and layout; prompt search fixed one failing cell."
aliases: ["format-instruction following failure", "JSON response format success rate", "StructuredRAG"]
sources: ["doi-10-48550-arxiv-2408-11061"]
---
# Output-structure complexity gradient

When a prompt only describes the reply format (no constrained decoding), the chance that the reply parses depends strongly on how complex the requested structure is. This is the empirical rate behind the "format-restricting instruction" row of [[structured-output]].

## What was measured

Shorten et al. built six tests over 56 Wikipedia abstracts, each with an answerable and an unanswerable question (112 questions per test). The tests ask for a string, an integer, a boolean, a list of strings, a composite AnswerWithConfidence object, and a list of such objects. A reply passes only if it parses into the requested JSON with the correct keys and the correct value types.[^c1] Two models were tested, Gemini 1.5 Pro and 4-bit Llama 3 8B-instruct, with two prompt layouts, at temperature 0.[^c2]

Across 24 experiments the mean success rate was 82.55%, but individual cells ranged from 0 to 100%: 11 of 24 reached 100%.[^c3] Simple scalar outputs did well; lists and composite objects did worse.[^c4] The list-of-strings task averaged 72.1% and the list-of-composites task 67.6%. The gap between models was widest there: Gemini 99.6% and 85.3%, Llama 44.7% and 50%.[^c5]

## Failure forms

The commonest failure was a conversational preamble before the JSON, such as "Here is the output in the required JSON format:".[^c6] A type slip also counts as failure: an integer returned as the string "4".[^c7] The DSPy-style layout sometimes made the model append a "Reasoning:" tail, as chain-of-thought prompting does.[^c6]

## Prompt layout has no stable winner

The two layouts were f-String (task variables embedded in natural prose) and Follow the Format (task, then response format, then inputs). Gemini did better with f-String (100% against 86.8%); Llama did better with Follow the Format (76.5% against 67.0%).[^c8] The authors report no significant overall difference.[^c9] Repeating the call is not a fix: results averaged over 3 trials were consistent, so naive retry was judged unlikely to help.[^c10]

## Prompt search can close a cell

OPRO, with GPT-4 proposing paraphrases and JSON validity as the metric, found a prompt for Llama 3 8B on the list-of-composites task that succeeded 100% of the time, within the first 10 paraphrases of the first round.[^c11] The data were split 40 train, 16 test.

## Limits

- Only parse success was measured. Answer correctness and the interaction between format and task quality were left to future work.[^c12]
- Two models, 3 trials, 56 short contexts (the shortest is 30 tokens; longer contexts were only briefly tried). The authors hypothesize, without testing it, that longer or noisy retrieved contexts make it harder.
- Whether the OPRO prompt generalizes beyond the one task, or beyond its 16 test items, is not shown. The OPRO result is one cell.
- The suggestion that adding a chain-of-thought "rationale" key lowers success is the authors' conjecture, not a measured result.
- Constrained decoding was deliberately excluded, so nothing here compares it to prompting.

## Related

- [[structured-output]] — this note gives measured rates for its prompt-only member
- [[constrained-decoding]] — the guarantee that this paper sets aside
- [[format-restriction-effect]] — what a format restriction costs in answer quality, which this paper did not measure
- [[capacity-dependent-format-tax]] — model-capacity dependence of format effects, as here between Gemini and Llama
- [[reasoning-formatting-decoupling]] — related to the reasoning-tail failure

[^c1]: doi-10-48550-arxiv-2408-11061 — "An output from the LLM passes these tests if it is able to be parsed into the requested JSON response format."
[^c2]: doi-10-48550-arxiv-2408-11061 — "All LLM APIs are tested with a temperature set to 0 to"
[^c3]: doi-10-48550-arxiv-2408-11061 — "Across 24 experiments, we find an average success rate of 82.55%."
[^c4]: doi-10-48550-arxiv-2408-11061 — "performance degrades significantly on list outputs and"
[^c5]: doi-10-48550-arxiv-2408-11061 — "achieving average success rates of 72.1% and 67.6% respectively."
[^c6]: doi-10-48550-arxiv-2408-11061 — "The most common failure case is for the LLM API to"
[^c7]: doi-10-48550-arxiv-2408-11061 — "We further consider cases where the model outputs a string type"
[^c8]: doi-10-48550-arxiv-2408-11061 — "achieving 76.5% success compared to"
[^c9]: doi-10-48550-arxiv-2408-11061 — "We do not find a"
[^c10]: doi-10-48550-arxiv-2408-11061 — "suggesting that trying again naively would be unlikely to succeed."
[^c11]: doi-10-48550-arxiv-2408-11061 — "OPRO finds the prompt that succeeds 100% of the time within the first 10 paraphrasings of"
[^c12]: doi-10-48550-arxiv-2408-11061 — "We leave inference throughput comparisons and the entanglement of"
