---
description: "Prompt constraints that are individually neutral or helpful can combine into a pass-rate loss beyond their additive sum, in some model families only; single-factor prompt tests cannot predict it."
aliases: ["compound prompt constraints", "super-additive degradation", "three-way prompt interaction", "complex interference"]
sources: ["doi-10-48550-arxiv-2609-03156", "arxiv-2512-24556"]
---
# Super-additive prompt-constraint interaction

Production prompts stack several constraints: an output format, a persona, an urgency framing. Most studies test each alone. This work crosses all three in a 3x3x3 full-factorial design (format, persona, urgency, three levels each, 27 conditions) on the 164 HumanEval+ problems with five OpenAI models, 22,140 evaluations under greedy decoding.[^c1]

## The quantity

For each triple condition the interaction is the residual between the observed pass@1 and an additive prediction: baseline plus the three main effects measured in isolation. A negative value means the compound is worse than the sum of its parts.[^c2] The point is that the isolated effects are all one can measure cheaply; the residual says how wrong that extrapolation is.

## What was found

- GPT-4o-mini showed the strongest effect: mean interaction -7.6 pp, all 8 triple combinations below additive. GPT-4o: -4.2 pp, 5 of 8. GPT-4.1-mini (+1.7 pp, 0/8) and GPT-4.1 (+1.3 pp, 2/8) showed no systematic pattern.[^c3]
- The worst cell was JSON + expert persona + moderate urgency at -12.2 pp. JSON combinations averaged -10.7 pp against -4.6 pp for XML.[^c4] The authors attribute this to the overhead of JSON string encoding competing with persona and urgency processing; that is their interpretation, not a tested mechanism.
- Vulnerability tracked model family, not size: both GPT-4o models degraded, both GPT-4.1 models resisted.[^c5] The authors link GPT-4.1's resistance to its instruction-following optimization, again as a suggestion.
- For GPT-4o-mini each constraint alone helped or was negligible, yet the combination fell 12.2 pp below additivity, a failure invisible to single-factor evaluation.[^c6]

## Where the additive frame fails

For o3-mini the baseline was low (59.8%) and any structured-output constraint raised it to about 88%; no further degradation appeared with persona and urgency. The authors judge the additive framework inapplicable there, because single-factor effects of 20-30 pp create ceiling effects.[^c7]

## The same shape in a safety setting

The non-additive pattern also appears where the outcome is refusal rather than pass rate, under another name. Crossing the language and the tense of one harmful request, the authors report "combinations of variables that sometimes amplify, and other times" cancel each other, and they call this Complex Interference.[^c8] Their starting hypothesis was "a simple multiplicative compounding effect," and the results instead showed amplification in some cells and cancellation in others.[^c9] The measure is different from the additive residual above: the safety study reports cell-level safety rates, not a residual against main effects, and it does not test a per-cell additive baseline. The shared object is a joint effect that isolated factor tests do not predict, so the name is recorded here as an alias. That identification is my inference from the structure, not the authors' claim.

## Limits

- One task (Python code generation), one benchmark, one vendor's models, greedy decoding only; whether the pattern holds for other tasks, vendors or sampling is untested here.
- Additivity on the percentage-point scale is an assumption; a bounded outcome near ceiling or floor makes the residual hard to read (as o3-mini shows).
- The mechanism for JSON being worse is conjecture.
- It concerns reliability of generated code, not question quality; transfer to how a question should be phrased is my inference.

## Related

- [[expert-persona-confidence-amplification]] — a persona effect that depends on format and baseline, so personas also interact with other prompt elements
- [[compound-ai-systems]] — systems-level view of stacked components
- [[temporal-framing-safety-asymmetry]] — the tense axis of the safety audit whose language-by-tense interaction is the same non-additive shape

[^c1]: doi-10-48550-arxiv-2609-03156 — "yielding 22,140 individual evaluations under greedy decoding."
[^c2]: doi-10-48550-arxiv-2609-03156 — "A negative"
[^c3]: doi-10-48550-arxiv-2609-03156 — "GPT-4omini exhibits the strongest super-additive degradation"
[^c4]: doi-10-48550-arxiv-2609-03156 — "XML-based combinations (I¯ = −4.6 pp)"
[^c5]: doi-10-48550-arxiv-2609-03156 — "rather than to parameter count."
[^c6]: doi-10-48550-arxiv-2609-03156 — "This nonlinear interaction represents"
[^c7]: doi-10-48550-arxiv-2609-03156 — "The additive interaction framework is inapplicable"
[^c8]: arxiv-2512-24556 — "combinations of variables that sometimes amplify, and other times"
[^c9]: arxiv-2512-24556 — "Although we hypothesized a simple multiplicative compounding effect"
