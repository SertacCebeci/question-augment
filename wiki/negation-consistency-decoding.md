---
description: "Asking H and its negation and forcing the label pair through the fixed negation map recovers answers a three-way LLM hid behind UNKNOWN, at 4-5 calls per question (FOLIO FOL, 204 items)."
aliases: ["CGD-PD", "consistency-guided decoding", "epistemic UNKNOWN recovery", "negation-map decoding"]
sources: ["arxiv-2604-06196"]
---
# Negation-consistency decoding

In three-way logical question answering (TRUE, FALSE, UNKNOWN) over a consistent premise set, the label of a hypothesis H fixes the label of its negation: TRUE and FALSE swap and UNKNOWN stays UNKNOWN.[^c1] Standard prompting treats H and not-H as independent inputs, so a model can answer them incompatibly. The decoder treats the two queries as two noisy views of one logical state and makes the final answer obey the map.

## Two kinds of UNKNOWN

UNKNOWN has two roles. It can be genuine underspecification (the premises entail neither side). It can also be epistemic: the model returns it from uncertainty, instability or conservatism although one side is entailed.[^c2] The decoder aims to remove the second kind and keep the first. An answer-quality metric therefore has to separate the two. The paper's "epistemic UNKNOWN rate" is the share of gold TRUE/FALSE items predicted UNKNOWN.[^c3]

## The decoding cascade (CGD-PD)

1. Classify H and the mechanically negated hypothesis. If the pair satisfies the map and is not UNKNOWN on both sides, return it.
2. Re-run a targeted "fixer" prompt on each UNKNOWN side. It treats UNKNOWN as a last resort and, when it keeps it, names the missing premise.[^c4]
3. If one side is now decisive and the other UNKNOWN, project the decisive side through the map.[^c5]
4. If both stay UNKNOWN, ask two binary entailment probes (YES/NO, no UNKNOWN option). Return TRUE for (YES, NO), FALSE for (NO, YES), otherwise UNKNOWN. Both YES is a conflict and abstains.[^c6]
5. If both sides are decisive but violate the map, a lightweight adjudicator picks between the two consistent assignments.[^c7]

The wrapper uses two calls in the common case and up to six, averaging 4-5 on FOLIO validation.[^c8]

## What was measured

On FOLIO's first-order-logic fields (204 validation items, temperature 0, no chain of thought), GPT-5.2 accuracy rose from 63.7 to 68.1 percent and Claude Sonnet 4.5 from 42.2 to 49.0. Epistemic UNKNOWN fell from 41.5 to 36.3 and from 72.6 to 53.3 percent.[^c9] Paired bootstrap intervals excluded zero: +4.4 points (+1.5 to +7.4) for GPT-5.2 and +6.8 (+3.4 to +10.3) for Claude.[^c10] Answered accuracy did not fall as coverage rose (Claude coverage 24.5 to 41.2 percent, answered accuracy 60.0 to 61.9), so the gain is not only UNKNOWN relabelled as low-quality decisions.[^c11]

The cost is over-resolution. For Claude, genuinely underspecified items turned into decisive labels rose from 13 to 21, and gold-UNKNOWN items kept fell from 81.2 to 69.6 percent.[^c12] GPT-5.2 kept 88.4 percent in both conditions.

## Limits

- Scope is narrow: premises and hypotheses are given as FOL formulas so that negation is mechanical. The authors state that natural-language negation scope is a harder setting not tested here.[^c13]
- Two API models, one strict prompt family, one validation split. The single-call Claude baseline is 75.5 percent UNKNOWN, so its gain largely measures recovery from an overly conservative prompt, not best-case performance.[^c14]
- No call-matched baseline: self-consistency at the same budget was not compared, so the benefit of logical coupling over plain extra sampling is untested. The authors call this the most informative next check.[^c15]
- Projection from one decisive side is only as reliable as that single call; there is no solver guarantee.[^c5]
- The per-branch contribution (fixer, probes, adjudicator) is not isolated; only aggregate change counts (15/204 and 34/204) are given.
- Reading this as a design principle for questioning in general (use known relations between related queries) is my inference from one task, not something the paper establishes beyond logic QA.

## Related

- [[uncertainty-decomposition]] — the epistemic versus genuine split of UNKNOWN is a case of separating reducible from irreducible uncertainty
- [[selective-answer-finalization]] — also trades abstention against rewriting and has to protect cases where abstaining was right
- [[inconsistency-penalized-confidence]] — uses a model's self-inconsistency as a signal; here inconsistency across paired queries triggers repair
- [[decoupled-support-contradiction-retrieval]] — treats support and contradiction as separate probes, as the YES/NO entailment pair does

[^c1]: arxiv-2604-06196 — "Under this map, T RUE and FALSE swap,"
[^c2]: arxiv-2604-06196 — "Epistemic U NKNOWN: the model returns U NKNOWN"
[^c3]: arxiv-2604-06196 — "fraction of gold determinate examples (T RUE or FALSE)"
[^c4]: arxiv-2604-06196 — "the prompt asks it to name the missing premise"
[^c5]: arxiv-2604-06196 — "This projection is rule-constrained"
[^c6]: arxiv-2604-06196 — "This includes the conflict case"
[^c7]: arxiv-2604-06196 — "The adjudicator is used only when"
[^c8]: arxiv-2604-06196 — "it uses 4–5 calls on average"
[^c9]: arxiv-2604-06196 — "CGD-PD improves accuracy on both models while reducing"
[^c10]: arxiv-2604-06196 — "CGDPD yields a +4.4 point accuracy gain (95% CI: +1.5 to +7.4)"
[^c11]: arxiv-2604-06196 — "These numbers suggest that CGD-PD is not simply replacing abstentions with lower-quality decisive labels in this"
[^c12]: arxiv-2604-06196 — "the number of genuinely"
[^c13]: arxiv-2604-06196 — "natural-language negation scope is an important and harder"
[^c14]: arxiv-2604-06196 — "The Claude single-call baseline is notably conservative under"
[^c15]: arxiv-2604-06196 — "allocate the same call budget to self-consistency or related"
