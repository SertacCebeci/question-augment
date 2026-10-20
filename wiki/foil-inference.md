---
description: "A why-question's unstated foil is best inferred from the asker's hindsight expectation, not prior expectation or closeness; LLMs show inconsistent coupling on the same task."
aliases: ["foil inference", "contrastive foil selection", "hindsight-expectation account of foil inference", "why-question foil"]
sources: ["besch-2026"]
---
# Foil inference

> A why-question ("Why did E happen?") is elliptical for a contrastive one
> ("Why E rather than E′?"); answering it well requires first inferring the
> unstated E′ — the foil — and the best cue for that inference is not what
> the listener thought would happen before E, but what they now think could
> have happened instead of E, after learning that E occurred.

## Definition / Mechanism

Explanations, and the why-questions that request them, are contrastive:
"E happened rather than E′, because C rather than C′." The foil E′ is
usually left unstated and must be inferred from context before a useful
answer can be given — Willie Sutton answering "why rob banks" with "because
that's where the money is" mistook the asker's foil ("not robbing") for a
different one ("robbing elsewhere").[^c1]

Besch & Gerstenberg (2026) tested three candidate cues for how a listener
infers E′: prior expectation (what one thought would happen next, before E),
closeness (what alternative is most similar to E), and hindsight expectation
(what one now thinks could have happened instead of E, once E is known). In
a pre-registered study (five vignette scenarios × three context variants,
N=45–52 per condition), foil selections correlated with all three but most
strongly with hindsight expectation (r=.82 vs. r=.58 prior, r=.62
closeness, all p<.001); a combined regression (H4) confirmed hindsight's
dominance over the other two predictors.[^c2]

## Known as

| Field | Name there | Relation |
|---|---|---|
| Philosophy of explanation (Lipton 1990; Hilton 1990, as cited in besch-2026) | foil / contrast class | close — same object, defined without the hindsight-expectation mechanism |
| Cognitive science (Besch & Gerstenberg 2026) | foil, E′ | exact |
| This wiki | foil inference | exact |

## Why it matters

A why-question touches its axis only through an unstated contrast, and
getting that contrast wrong answers a different question than the one
asked (the Sutton case). This gives the answerer a concrete, testable cue
— hindsight expectation — for recovering the axis a why-question
implicitly names, instead of treating "why" as self-explanatory.

## Transfer

| Aspect | Content |
|---|---|
| Home field | Bayesian linear/multinomial regression of a listener's judgment on a candidate predictor, used in cognitive science to rank predictors of a human choice |
| Here | scores hindsight expectation, prior expectation and closeness as candidate cues for which foil a why-question implicitly names |
| What survives | the ranking method itself: hindsight expectation is the strongest single predictor and the winner of the combined (H4) regression |
| What does not | the human ranking, when the same regression and the same 15 vignettes are run on four LLMs (GPT-5.2, Llama-3.1-70B, Mistral-7B, Qwen2.5-7B): hypothesis support is inconsistent across models and a multinomial comparison finds no predictor beats a uniform baseline for any of them |

[^c3]

## Limits

The claim rests on five hand-designed vignette scenarios with three
response options each, judged by US-based Prolific participants; the
predictors are correlational (r, regression β), not a causal manipulation
of what listeners attend to, so hindsight expectation is shown to be the
best available cue among the three tested, not proven to be the mechanism
listeners actually use. The LLM result is four models under one prompting
setup (single-token forced choice, T=0.7, 50 samples) and should not be
read as a general claim about LLM pragmatic competence.

## Related

[[possible-worlds]] · [[constraint-as-information]]

[^c1]: besch-2026 — "Explanations are inherently contrastive: E happened rather than E’ because of C rather than C’. However, these contrasts, or “foils”, are rarely mentioned explicitly but have to be inferred in context."
[^c2]: besch-2026 — "Across vignette × option percentages (𝑁 = 45), foil selection correlated with prior expectation (𝑟 = .58), closeness (𝑟 = .62), and most strongly with hindsight expectation (𝑟 = .82) (all 𝑝 < .001)."
[^c3]: besch-2026 — "Across LLMs, the linear regression results provided mixed support for the hypotheses: GPT-5.2 and Llama-3.1-70B supported H1 and H3 (but not H2), Mistral-7B supported H3 only, and Qwen2.5-7B supported none."
