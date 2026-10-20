---
description: "A prompt-only framework for black-box LLMs that jointly frames the answer-or-abstain decision with elicited confidence, announced payoffs, and normative guidance."
aliases: ["I-CALM", "Incentivizing Confidence-Aware Abstention for LLM Selective Answering"]
sources: ["arxiv-2604-03904"]
---
# I-CALM

> Three separate reasons to withhold an answer — not enough evidence, too
> costly to be wrong, not licensed to assert it — folded into one prompt,
> for a model whose weights nobody can touch.

## Definition / Mechanism

Zong et al. decompose the answer-or-abstain decision into three functional
roles, each grounded in a distinct human account of withholding assertion:
metacognitive monitoring, consequence-sensitive choice under risk, and
epistemic norms of assertion. I-CALM implements all three in a single
prompt for a fixed, black-box model, with no weight updates, auxiliary
classifiers, or access to internals.[^c1]

The **epistemic** component elicits a verbal [[calibration|confidence]]
score alongside the candidate answer — available in black-box settings
where hidden states and token probabilities are not. The **consequential**
component announces payoffs for the three outcomes in the prompt itself:
"a correct answer receives positive payoff, an incorrect answer receives
negative payoff, and an 'I don't know' response receives a positive
payoff," formally $r(\text{correct})=+\alpha$, $r(\text{wrong})=-\beta$,
$r(\text{abstain})=+\gamma$ — described only in natural language, never
used to update parameters. The **normative** component adds five
compact principles — truthfulness, humility, no assumptions without
evidence, responsibility, clarity — as standards for when surfacing a
claim is appropriate, distinct from a confidence-to-action rule.[^c3]

Component ablation on GPT-5 mini/PopQA isolates each role's failure mode
when removed: dropping the announced payoffs raises coverage from 0.56 to
0.76 but also raises the surfaced false-answer rate from 0.36 to 0.43 and
drops [[abstention-informedness]] from 0.44 to 0.33; dropping verbal
confidence collapses coverage to 0.25 (broad over-abstention rather than
targeted); dropping normative guidance raises coverage and the
false-answer rate together while leaving calibration essentially
unchanged. "Every ablation lowers $J_{abs}$, showing that all three
components contribute to I-CALM's error-targeting abstention behavior."[^c4]

## Why it matters

Evaluated with the [[abstention-informedness]] protocol across GPT-5
mini, Gemini-3.1-Flash-Lite and Llama-3-8B-Instruct on PopQA (and
SimpleQA-Verified), "I-CALM improves abstention quality by 28.7% over
verbal-confidence thresholding, the strongest baseline, at matched
coverage," and "across the 15 transfer settings, I-CALM attains the
highest $J_{abs}$ in 14 of them." Explicit IDK-permission prompting is
the sharpest contrast: it lowers surfaced risk on some models only by
collapsing coverage (0.290 for GPT-5 mini, 0.002 for Llama), which
I-CALM's payoff-plus-confidence combination avoids.

## Transfer

| | |
|---|---|
| **Home field** | Human decisions to withhold a factual assertion — metacognitive monitoring, expected-utility/prospect-theoretic choice under risk, deterrence theory, and Williamson's knowledge norm of assertion. |
| **Here** | Each account becomes one natural-language prompt component (confidence elicitation, stated payoffs, stated norms) added to a fixed model's context, not a mechanism the model is shown to implement internally. |
| **What survives** | The three-way split of *what do I know*, *what does it cost*, and *am I licensed to assert this* as functionally distinct levers on the same decision, each independently ablatable. |
| **What does not** | The paper explicitly disclaims that the model literally performs expected-utility maximization, prospect-theoretic weighting, deterrence reasoning, or knowledge-normed inference — these are motivating analogies for prompt design, not claims about the model's computation. |

## Limits

- Prompt-only and model-parameter-fixed by design: it "does not fully
  resolve severe underlying knowledge deficits," and its modest effect on
  the overall (not answered-only) false-answer rate is consistent with
  that scope, not a shortfall against a goal it never targeted.
- Tested on short-answer factual QA with one verifiable answer per
  question (PopQA, SimpleQA-Verified); multi-hop, long-form and
  multi-claim responses are left untested.
- The reported payoff configuration ($\alpha=1,\beta=1,\gamma=0.4$) is one
  point in a swept space; on GPT-5 mini specifically, verbal-confidence
  thresholding alone has modestly stronger raw selective-answering
  numbers than I-CALM at matched coverage, though I-CALM still wins on
  calibration there — the framework is not uniformly best on every metric
  on every model.
- Verbal confidence is explicitly not assumed to be "a perfectly faithful
  readout of the model's internal uncertainty," only a practical elicited
  signal — unverified beyond the paper's own empirical checks (Appendix
  B, not read here).

## Related

[[abstention]] · [[abstention-informedness]] · [[calibration]] · [[awa-rl]] · [[safety-oriented-prompting]]

[^c1]: arxiv-2604-03904 — "I-CALM organizes the answer-or-abstain decision around three functional dimensions."
[^c3]: arxiv-2604-03904 — "adds general standards for responsible factual assertion rather than merely specifying a confidence-to-action rule"
[^c4]: arxiv-2604-03904
