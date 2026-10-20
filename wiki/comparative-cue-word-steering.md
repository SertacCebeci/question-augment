---
description: "Putting more, less or equal in a comparison question pulls wrong answers toward that word, though the quantities are unchanged; chain-of-thought shrinks the pull and JSON output partly restores it."
aliases: ["directional framing bias", "comparative framing bias", "linguistic steering", "directional error (DirErr)"]
sources: ["doi-10-48550-arxiv-2506-03923"]
---
# Comparative cue-word steering

Shafiei, Saffari and Moosavi (2025) built MathComp: 300 comparison scenarios in which two people have a quantity (hours, dollars, actions) and the answer is "more", "equal" or "less". Each scenario appears in 14 prompt variants. There are seven framings (neutral, direct more/equal/less, indirect more/equal/less), and the framing clause sits at the beginning or the end. Six models from GPT, Claude and Qwen were tested. The finding is that logically equivalent questions containing a comparative word "systematically steer predictions in the direction of the framing term."[^c1]

## The measure

Accuracy hides which way a model errs. The authors define directional error DirErr(y) as the share of cases where the model answers y among all cases where y is wrong. It is the model's rate of erring toward y, given every chance to do so. 100% means it always drifts to y whenever y is not correct.[^c2] Reporting it per label shows whether a framing pushes toward less, more or equal.

## What was observed

- **Baseline skew.** With no cue word most models drift most toward "More" (26% for Sonnet to 93% for Qwen-3B at begin position). "Less" is second, and "Equal" is rarely over-predicted.[^c3]
- **Cue steering.** Adding "more" or "less", as a direct question or an indirect prime, raises DirErr toward that word. "Equal" framing raises equal-errors to as much as 94%, from a negligible neutral level.[^c4]
- **Position matters less than word.** Moving the framing clause between beginning and end affects models differently, but "lexical content generally outweighs positional effects."[^c5]
- **Scale.** GPT-4o and Claude Sonnet 3.7 stay at or below 55% in every framing except Indirect-Equal, while smaller models often exceed 90% drift toward the cue word.[^c6]
- **Identity terms.** Replacing Person B with a demographic phrase ("a woman", "an Asian person") raises erroneous "More" answers across many framings, with identical arithmetic. Indirect "Less" prompts sometimes give higher More-error than More prompts, which the authors read as a possible "framing override" by priors about the demographic phrase. The interaction can amplify or mute the cue.[^c7]

## Mitigation and its residue

Free-form chain-of-thought "drastically reduces" directional error and brings most DirErr values below 30%, but cue words still increase error in their own direction, only less.[^c8] Structured CoT with JSON output is less robust and is more affected by "equal" and "less" cues. By manual analysis the model often computes correctly but words its answer in the cue's frame, for example "Person A spends less money than Person B" when the prompt stressed "less". The label is then misclassified although the arithmetic is right.[^c9]

My reading (inference, not the paper's claim): a questioner who wants an unbiased comparison should keep the comparative word out of the question, or ask for the quantities first. The asker's own word choice is a source of error independent of the answerer's competence.

## Limits

- Only comparative math word problems with a three-way label; transfer to open-ended or factual comparison is untested.
- Six models, two sizes per family, some closed; the demographic analysis is shown mainly for Sonnet 3.7 and GPT-4o-mini and treats gender as binary.
- The JSON mislabeling account rests on the authors' manual analysis, not a systematic coding.
- No mechanism inside the model is identified; "framing override" is a conjecture.

## Related

- [[prompt-content-over-surface-form]] — reports no consistent direction from surface changes; here a meaning-bearing word does have a direction
- [[format-induced-answer-collapse]] — another way output format changes which answer appears
- [[answer-format-dependent-bias-measurement]] — the measured bias depends on the answer format, as here with JSON versus free text
- [[mcq-answer-position-bias]] — a position-driven directional bias in multiple choice, contrasted with lexical cue steering

[^c1]: doi-10-48550-arxiv-2506-03923 — "systematically steer predictions in the direction of the framing term."
[^c2]: doi-10-48550-arxiv-2506-03923 — "number of instances for which y is not the correct"
[^c3]: doi-10-48550-arxiv-2506-03923 — "Without any cue word the majority of models show their largest drift toward"
[^c4]: doi-10-48550-arxiv-2506-03923 — "DirErr%(equal) to as much as 94%, while it was"
[^c5]: doi-10-48550-arxiv-2506-03923 — "affects models differently, but lexical content generally outweighs positional effects."
[^c6]: doi-10-48550-arxiv-2506-03923 — "framing except Indirect-Equal), whereas smaller"
[^c7]: doi-10-48550-arxiv-2506-03923 — "protected demographic term increases the rate of"
[^c8]: doi-10-48550-arxiv-2506-03923 — "bringing most DirErr% values below 30%."
[^c9]: doi-10-48550-arxiv-2506-03923 — "Structured CoT (with JSON"
