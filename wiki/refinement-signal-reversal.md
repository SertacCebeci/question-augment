---
description: "Revision that lowers a request's visible aim can also raise it: in paired debate outputs, 8 rewrites beat their no-debate baseline and 6 fell behind, some by over-justifying."
aliases: ["debate regression", "debate improvement", "revision backfire", "over-justification backfire", "two-sided refinement"]
sources: ["arxiv-2512-23717"]
---
# Refinement signal reversal

Revision is meant to remove the signal it targets. A paired comparison from multi-agent debate shows that the same revision step can also put that signal back. The setting is a debate framework that turns an explicit harmful request into a less explicit one, and each debate output is compared with a no-debate output for the same query. The sample is small: "We randomly sample 50 original harmful queries."[^c1] Of these, the paper extracts "14 divergent cases: 6 Debate Regression cases, where"[^c2] debate did worse, meaning "the non-debate transformation bypasses detection but the debate version does not."[^c3] The other direction is the one the debate was built for: "8 Debate Improvement cases, where the non-debate version fails but"[^c4] the debate version got past the refusal.

Both directions come from one operator. Where revision helped, the agents "identify and revise overt red-flag phrasing,"[^c5] which removes explicit cues. Where it hurt, the revision added material. In one case the paper attributes, "the agents over-justified the legitimacy of the question, ironically introducing red-flag"[^c6] terms. The paper's account of the optimisation side is that "Attempts to overly optimize camouflage may strip away defensive framing"[^c7], which makes the evasive goal itself visible. Its general summary is that "the interaction dynamics also introduce instability,"[^c8] so the trajectory can "oscillate between excessive specificity and over-abstraction."[^c9]

The mechanism, as the paper reads it, is path-dependent: the round that strips one cue can add another. What was measured is the paired outcome. That the cause is over-justification and over-specification is the authors' reading of per-case analyses.

A second result points the same way. In the main table, a one-shot single-LLM rewrite is second-best on effectiveness and "even outperforms its reflection-augmented variant."[^c10] The reflection variant is one extra self-revision pass, and it did worse than no revision at all. The full debate method leads on effectiveness, but its intent preservation is only second-ranked: "0.12. At the same time, it maintains a strong balance on intent preservation (0.73)."[^c11]

Intent preservation is checked by a separate judge, and the paper drops rewrites that fail it: "After filtering out queries that fail the intent"[^c12] preservation test, effectiveness is scored on what remains. Effectiveness is a refusal indicator from a test model, so a rewrite counts as a success whenever the test model does not refuse.

For asking, the analogue would be a question revised to read as more acceptable that, in the revision, states its real purpose more plainly. Nothing here tests questions. This is my inference from the two-sided pattern, not a finding.

## Limits

- One paper, one model family for every role. The text says that "judges) are instantiated with DeepSeek-V3,"[^c13] so debaters, summariser, generator and judges share one model's blind spots.
- The paired sample is small: 14 divergent cases out of 50, split 6 against 8. The text read reports no significance test. A two-case difference is noise until a larger run says otherwise (my inference).
- The per-case cause comes from an LLM reading the debate transcript: the paper says "we provide the full debate context to" the model.[^c14] That is a judge's reading, not a controlled intervention, and the mechanism labels are not independently checked.
- The effectiveness measure is the refusal of one test model, not a judged quality of the rewrite. Intent is judged separately and binarily, and the reversal cases do not report how many rewrites lost intent.
- The evaluation data is a sample: "we sample the first"[^c15] queries from Safe-RLHF, and the paired-divergence analysis uses a different random 50. The results are not a rate over the dataset.

## Related

- [[refinement-quality-peak]] — another iterated refinement with an interior optimum; the same paper's debate-round curve is a second instance there.
- [[faithfulness-gated-attack-reward]] — the meaning check that keeps a rewrite on the seed's intent; here it is a post-generation filter, not a reward gate.
- [[script-level-obfuscation]] — keeping intent while changing surface form, with no revision loop.
- [[llm-red-teaming]] — the practice whose refusal-rate measure these numbers use.

[^c1]: arxiv-2512-23717 — "We randomly sample 50 original harmful queries."
[^c2]: arxiv-2512-23717 — "14 divergent cases: 6 Debate Regression cases, where"
[^c3]: arxiv-2512-23717 — "the non-debate transformation bypasses detection"
[^c4]: arxiv-2512-23717 — "8 Debate Improvement cases, where the non-debate version fails but"
[^c5]: arxiv-2512-23717 — "identify and revise overt red-flag phrasing"
[^c6]: arxiv-2512-23717 — "the agents over-justified the legitimacy of the question, ironically introducing red-flag"
[^c7]: arxiv-2512-23717 — "Attempts to overly optimize camouflage may strip away defensive framing"
[^c8]: arxiv-2512-23717 — "the interaction dynamics also introduce instability"
[^c9]: arxiv-2512-23717 — "cause the transformation trajectory to oscillate between excessive specificity and over-abstraction"
[^c10]: arxiv-2512-23717 — "even outperforms its reflection-augmented variant."
[^c11]: arxiv-2512-23717 — "0.12. At the same time, it maintains a strong balance on intent preservation (0.73)"
[^c12]: arxiv-2512-23717 — "After filtering out queries that fail the intent"
[^c13]: arxiv-2512-23717 — "judges) are instantiated with DeepSeek-V3"
[^c14]: arxiv-2512-23717 — "we provide the full debate context to"
[^c15]: arxiv-2512-23717 — "we sample the first"
