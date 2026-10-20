---
description: "Multi-hop failure in small LMs is localized to resolving an unnamed subject; injecting the explicit subject's tokens at one layer and magnitude raises answer probability, random tokens do not."
aliases: ["memory injection", "explicit-subject activation injection"]
sources: ["doi-10-48550-arxiv-2411-05037"]
---
# Implicit-subject resolution injection

A multi-hop prompt refers to an entity that is never named ("The largest coral reef system in the world ..."). The thesis by Sakarvadia's thesis hypothesizes that the model fails because it cannot resolve the implicit subject to the explicit one ("The Great Barrier Reef"), which limits the later layers' retrieval of facts about that subject.[^c1]

## Mechanism

For each multi-hop prompt, the tokens of the explicit subject (taken from the matching single-hop prompt) are injected as a "memory" into the attention-layer hidden activations at a chosen layer ℓ and with a magnitude τ in 1..15. Success is the percent increase in the probability of the expected next token, with versus without injection.[^c2] No weights change, so the intervention cannot damage unrelated tasks by construction (the author's argument; side effects on other prompts were not measured in the slices read; my reading).

Each model and dataset pair has its own best (ℓ, τ): the heatmaps show a narrow green region, with red (harm) elsewhere.[^c3] Best curated injections raised the expected-token probability on average by 45% (GPT2-Small, hand set), 424% (GPT2-Small, 2WMH), 68% and 204% (GPT2-Large).[^c4] Example: for "The highest peak in the world is located in the ..." the answer probability moved from 3.40% to 22.58%.

## The control that makes it a localization claim

Injecting the 40 most common random words per part of speech at the same best (ℓ, τ) mostly lowered the correct-answer probability (for example −7.6% to −17.1% for GPT2-Small), and no random injection beat a curated one.[^c5] So the gain comes from the content of the injected subject, which supports the diagnosis that the missing step is subject resolution rather than a generic activation perturbation. The effect is a probability increase on the next token, not necessarily a changed top-1 answer.

## Limits

Only GPT-2 models (Small, Large, XL in the appendices) and two small datasets were used. The injection needs the explicit subject, which is supplied from the single-hop prompt, so it is an oracle intervention, not a deployable fix. The tuning of (ℓ, τ) is done on the evaluation prompts themselves. Averages exclude outliers beyond two standard deviations. Some random injections on GPT2-Large 2WMH were positive (3.5% to 17.6%), so the control is not uniformly negative. Causal sufficiency of the hypothesis for larger models is untested.

## Related

- [[bridge-conditioned-retrieval]] — the retrieval-side analogue: supply the bridge entity explicitly before the second hop
- [[hop-depth-difficulty-with-entropy-check]] — hop depth as the source of difficulty
- [[rung-mismatch-in-interpretability-claims]] — the random-injection control is an interventional check of the kind that rung asks for
- [[gated-activation-steering-for-abstention]] — another activation-level intervention at inference

[^c1]: doi-10-48550-arxiv-2411-05037 — "We hypothesize that a model’s poor performance on multi-hop prompts is due to its inability"
[^c2]: doi-10-48550-arxiv-2411-05037 — "We measure the success of a memory injection by calculating the"
[^c3]: doi-10-48550-arxiv-2411-05037 — "We observe that each model/dataset combination has an optimal"
[^c4]: doi-10-48550-arxiv-2411-05037 — "in multi-hop tasks, by up to 424%."
[^c5]: doi-10-48550-arxiv-2411-05037 — "no random injection result exceeded the performance"
