---
description: "Reasoning faithfulness as two output-level tests, stance consistency and causal influence under injected opposing reasoning; about half of outputs fail and accuracy does not predict it."
aliases: ["RFEval", "counterfactual reasoning intervention faithfulness", "reasoning faithfulness (RF)", "causal decoupling"]
sources: ["doi-10-48550-arxiv-2602-17053", "arxiv-2601-02314"]
---
# Stance consistency plus causal influence as reasoning faithfulness

The RFEval benchmark defines a behavioral proxy for whether a reasoning model's stated reasoning is real, using only its text. Faithfulness is the conjunction of two checks.[^c1]

## The two conditions

**Stance consistency.** A stance extractor maps any text to a position (for example an answer option). The output is split into reasoning, optional explanation and answer. Each part must either keep the stance of everything before it, or explicitly identify and justify a departure; one unjustified break anywhere fails the whole output, even if the answer is correct.[^c2]

**Causal influence.** A counterfactual reasoning chain that asserts a different stance is appended to the input. The reasoning shows causal influence if the stance of the new reasoning or of the answer changes. The authors call this a necessary condition only; whether the change is coherent is checked by stance consistency on the intervened output.[^c3]

An instance is faithful only if baseline and intervened outputs are both stance-consistent and influence holds. Evaluation uses only contrastive pairs, where the injected stance differs from the model's own baseline stance, because with an aligned injection "no change" is ambiguous and "change" may have unrelated causes.[^c4]

## What was measured

On 7,186 instances over seven tasks and 12 open-source models, 49.7% of outputs were unfaithful, mostly through stance inconsistency, concentrated in math and code.[^c5] Within model families, adding RLVR-style training on top of SFT lowered faithfulness; the authors attribute this to rewards that score format and correctness, and report that average reward was slightly higher for stance-inconsistent outputs.[^c6] Once model and task are controlled, accuracy and faithfulness are only weakly and non-significantly associated, so accuracy is not a proxy.[^c7]

A second instrument for the same test is Project Ariadne (arxiv-2601-02314), which names the failure causal decoupling: the final answer stays invariant when a step of the agent's reasoning is replaced by a contradicting one. It differs from the appended-text design in a way that bears on the caution below: the intervention is applied to the agent's own generated chain, and the agent is re-executed from the point of intervention.[^c8] The paper treats a low faithfulness score ϕ = 1 − S(a, a*) as the sign of decoupling, where S is a semantic similarity between the original and the counterfactual answer.[^c9] The similarity is judged by a second model, so the test applies to open-ended answers that have no finite stance set.[^c10] A violation is counted only when the answers stay similar and the intervention is strong enough that a change would be expected; the violation density is the share of audits that violate, and it is highest for scientific queries.[^c11]

## Why it matters for asking and answering

A correct answer with an incoherent chain, or a chain the answer ignores, looks identical to a sound one if only the answer is graded. Probing by changing the stated reasoning, not the question, exposes whether a stated rationale carries the answer. This reading is mine, not the paper's.

## Limits

- The test is behavioral; the paper itself says true faithfulness to internal computation is not accessible, so this is a proxy.[^c1]
- Stances come from an extractor and "identified" departures from a judge; their errors enter every score. I did not read their validation closely.
- Injected reasoning is "output-level", appended to the context; a model may treat it as user-provided text rather than its own thought, which differs from intervening on the model's own chain. This is my caution, untested here.
- Only contrastive instances count, so the score says nothing about cases where the model already agrees with the injection.
- The RLVR finding comes from within-family ablations of open models, not a controlled training experiment.
- Only tasks with finite stance sets (answer options) fit the definition.
- The Ariadne variant relaxes that limit, but its equivalence call rests on one judge model; the text read gives no agreement check against humans, and no values for the similarity threshold or the minimum intervention strength.[^c10]
- In its experiments Ariadne intervenes at one step only, a logic flip at the initial step, chosen "to maximize the potential for downstream effects"; the framework is stated for every step and for other modalities, which were not tested there.[^c12]
- The headline figures do not line up. The abstract gives a violation density "of up to 0.77 in factual and scientific domains",[^c13] the table gives 0.96 for scientific reasoning, and the text describes 500 queries[^c14] while reporting audits over "30 distinct reasoning traces".[^c15] How the 500 queries relate to the 30 audits is not stated. These are my readings of the paper's text.
- The paper calls its result "proving that the intermediate reasoning state is nonessential" for factual retrieval.[^c16] No probability is computed; the claim that the answer distribution barely moves is inferred from similarity scores. Invariance under one replacement shows that the answer did not depend on that step in these runs, not that the trace is decorative in general. This reading is mine.
- The SCM and do-calculus vocabulary carries over only as intervene-and-rerun: the paper fits no structural equations and holds the model parameters fixed, so Pearl's identification machinery is not used. This is my reading.
- The "error-correction" account, that the agent notices the contradiction and returns to its prior, is read from logs; the paper's wording is that the agent "reverts to its high-probability parametric prior".[^c17]

## Related

- [[accuracy-masks-unstable-reasoning]] — also finds accuracy hides unsound routes, using activation stability rather than output counterfactuals
- [[supported-faithfulness-score]] — another faithfulness score for comparison of what is measured
- [[reasoning-faithfulness-observer-effect]] — measuring faithfulness can change it
- [[implicit-answer-conditioning]] — answers conditioned on something other than the stated reasoning
- [[cot-intervention-health-metrics]] — the same counterfactual family, but it removes or rewrites the trace instead of contradicting one step

[^c1]: doi-10-48550-arxiv-2602-17053 — "no consensus definition of faithfulness exists, a practical behavioral proxy is needed."
[^c2]: doi-10-48550-arxiv-2602-17053 — "any deviation—from a contradiction within r to an unjustified transition between r, e, and"
[^c3]: doi-10-48550-arxiv-2602-17053 — "Crucially, κ acts as a necessary condition to verify if the intervention had any effect."
[^c4]: doi-10-48550-arxiv-2602-17053 — "We evaluate faithfulness only on contrastive pairs (δ = 1), where the injected"
[^c5]: doi-10-48550-arxiv-2602-17053 — "we find unfaithfulness in 49.7% of outputs, predominantly from stance inconsistency."
[^c6]: doi-10-48550-arxiv-2602-17053 — "the average reward is very similar for χ = 1 and χ = 0, and is in fact slightly higher for stanceinconsistent outputs."
[^c7]: doi-10-48550-arxiv-2602-17053 — "accuracy is neither a sufficient nor a reliable proxy for faithfulness: once controlling for model and task, the accuracy–faithfulness link is weak and statistically"
[^c8]: arxiv-2601-02314 — "agent from the point of intervention"
[^c9]: arxiv-2601-02314 — "indicates Causal Decoupling, proving the intervention on"
[^c10]: arxiv-2601-02314 — "was computed using a secondary Claude 3.7 Sonnet instance as the scoring"
[^c11]: arxiv-2601-02314 — "was highest in Scientific Reasoning (ρ = 0.96)"
[^c12]: arxiv-2601-02314 — "to maximize the potential for downstream effects"
[^c13]: arxiv-2601-02314 — "(ρ) of up to 0.77 in factual and scientific domains"
[^c14]: arxiv-2601-02314 — "We utilized a dataset of 500 queries spanning three"
[^c15]: arxiv-2601-02314 — "Our audit of 30 distinct reasoning traces reveals a"
[^c16]: arxiv-2601-02314 — "proving that the intermediate reasoning state is nonessential for terminal decision-making in factual"
[^c17]: arxiv-2601-02314 — "to its high-probability parametric prior"
