---
description: "Whether a context counts as sufficient depends on the criterion: reasonable inference passes a pragmatic test and fails a literal one, so one sufficiency verdict cannot serve every application."
aliases: ["verification strictness", "sufficiency spectrum", "pragmatic versus literal sufficiency", "leniency setting"]
sources: ["arxiv-2512-06476"]
---
# Sufficiency criterion strictness

A sufficiency verdict is a verdict under a criterion. The paper's observation is that information sufficiency "is not monolithic but exists on a spectrum," running "from pragmatic inference to literal fact-checking."[^c1] At the pragmatic end, a context that lets a reader infer the answer is sufficient. At the literal end, the context must state the answer in the form the question asks for.

The two ends disagree on the same items. The paper's verifier accepts inference, and on a question about when a CEO's resignation takes effect it deems a context sufficient when the text only says the CEO "would step down next year". The benchmark requires a precise date. The paper's account is that the verifier "deems it Sufficient, while the benchmark requires a precise date."[^c2]

The pragmatic default does worst where the benchmark is strict. On SQuAD v2 and FaithEval, a plain autorater beats the pragmatic verifier, "while our method performs substantially poorly."[^c3] The authors attribute this to the definition itself: the trouble is "the definition of sufficiency and its subjective nature."[^c4]

The fix changes one prompt, not the pipeline. The paper handles this by "treating verification strictness as a tunable parameter", and for exact wording it reconfigures the verifier to reject inference, so that "only the verification criteria shift" while the identification step stays the same.[^c5][^c6] Its leniency ablation (Table 6) reports insufficiency accuracy under the stricter setting on SQuAD v2 and FaithEval, and the authors' summary is that one method "can adapt to different task requirements, from pragmatic QA systems to strict faithfulness benchmarks," with some tuning.[^c7][^c8]

What transfers is the place of the criterion. The context is fixed across the two readings; what moves is the bar a found or inferred answer must clear. A question that names the answer's form, such as a date or a name, sets a literal bar whether or not the asker says so, and a reader who infers where the asker wanted a stated value will call the same context sufficient that the asker would not (my inference from the paper's example).

## Limits

- The spectrum rests on two benchmarks and one knob. The paper itself calls the strictness definition "manually set" and leaves automatic choice to future work.[^c9]
- The leniency ablation reported in Table 6 covers SQuAD v2 and FaithEval. In the sections read, the strict setting is not reported on the multi-hop sets, so whether it costs the pragmatic gains there is not shown (my reading).
- The "spectrum" is inferred from where the verifier disagrees with benchmark labels, and those labels are themselves one criterion. No continuum of criteria is measured (my inference).
- The default that the paper calls pragmatic was tuned on its multi-hop and answerability sets. Which criterion a deployed system should use is not settled by this work.

## Related

- [[literal-match-dependence]] — the literal end of the spectrum is where evidence found by word overlap is rewarded
- [[consequence-sensitive-support-resolution]] — sets the sufficiency bar by what a wrong call costs, a different source for the same criterion
- [[gap-claim-attribution-check]] — the verifier whose leniency this note describes
- [[evidence-insufficiency-regimes]] — how evidence falls short under a fixed bar; this note is about where the bar sits

[^c1]: arxiv-2512-06476 — "information sufficiency is not monolithic but exists on a spectrum,"
[^c2]: arxiv-2512-06476 — "it Sufficient, while the benchmark requires a precise date."
[^c3]: arxiv-2512-06476 — "while our method performs substantially poorly."
[^c4]: arxiv-2512-06476 — "definition of sufficiency and its subjective nature."
[^c5]: arxiv-2512-06476 — "treating verification strictness as a tunable parameter."
[^c6]: arxiv-2512-06476 — "only the verification criteria shift."
[^c7]: arxiv-2512-06476 — "Insufficiency accuracy with leniency ablation."
[^c8]: arxiv-2512-06476 — "can adapt to different task requirements, from pragmatic QA systems to strict faithfulness benchmarks,"
[^c9]: arxiv-2512-06476 — "manually set strictness definition for sufficiency."
