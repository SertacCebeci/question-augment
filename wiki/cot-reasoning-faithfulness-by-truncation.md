---
description: "Truncating a CoT at five checkpoints and measuring document-overlap, match rate and flip rate shows whether the rationale tracks retrieved evidence or is post-hoc."
aliases: ["CoT checkpoint faithfulness", "truncated-CoT faithfulness probe"]
sources: ["arxiv-2602-09442"]
---
# CoT reasoning faithfulness by truncation

A stated rationale can be a post-hoc story or the actual route to the answer. Parihar and Cheng test this in a RAG setting by cutting the chain-of-thought at five checkpoints (1 sentence, 25%, 50%, 70%, full) and forcing an answer at each. They record the answer two ways: the log-probability difference between stereotypical and anti-stereotypical words for a masked sentence, and free text generated after appending "Final answer:".[^c1] The two methods "give consistent outcomes".[^c2]

Three quantities summarise the result on a limited sample. Document dependence: 74.78% of words in full CoT explanations come from the retrieved documents. Match rate: 60% agreement between truncated checkpoints and the full-CoT answer. Volatility: 0.24 flips per item in bias direction across checkpoints.[^c3] The authors read intermediate answers that diverge from the final one, plus high document overlap, as evidence that the reasoning is progressive and evidence-dependent, not predetermined.[^c4]

The probe also gives an asymmetry: stereotype words are chosen more often under negative regard (61.78%) than anti-stereotype words under positive regard (15.38%), so the stereotypical association is activated more reliably.[^c5]

## Limits

- Evaluated "on limited samples", with one demonstration model, so the numbers are indicative only.[^c6]
- Word overlap with retrieved documents shows reliance on the text, not that the reasoning logic caused the answer. A 60% match rate is compatible with both genuine evolution and instability; the faithfulness reading is the authors' interpretation, and no intervention (editing the CoT and observing the answer) was done.
- No threshold is given for what counts as faithful.

## Related

- [[rag-bias-reduction-versus-cot-bias-increase]] — the bias result this probe was built to explain
- [[process-outcome-consistency-verification]] — another check that a reasoning process matches the outcome
- [[stance-consistency-plus-causal-influence-faithfulness]] — a faithfulness test that adds causal intervention, which this probe lacks

[^c1]: arxiv-2602-09442 — "Second, we use"
[^c2]: arxiv-2602-09442 — "give consistent outcomes"
[^c3]: arxiv-2602-09442 — "74.78% of words in full"
[^c4]: arxiv-2602-09442 — "showing reasoning is dynamic and evidence-dependent rather than predetermined"
[^c5]: arxiv-2602-09442 — "choices made"
[^c6]: arxiv-2602-09442 — "we assess faithfulness of CoT reasoning on limited samples"
