---
description: "Each answer token's highest cosine to any retrieved triple's embedding, averaged over the answer; low values mark an answer drifting from the retrieved subgraph toward parametric memory."
aliases: ["SAS", "token-triple semantic alignment", "knowledge integration fidelity", "semantic alignment score"]
sources: ["arxiv-2512-09148"]
---
# Semantic alignment score

Attention can show where a model looks; it does not show whether what it looked at reaches the representation the answer is produced from. The semantic alignment score is built to test that second step. Each retrieved triple is linearized as head, relation, tail and "encoded by the same language model (LM)", giving a masked-mean embedding of its hidden states.[^s1] For each answer token, the hidden vector from a top layer is compared with each triple embedding by cosine, and the token's score is the best match: "take the maximum over a finite set".[^s2] The sentence-level score is the mean over answer tokens, constrained to [0, 1] "to focus on positive semantic alignment".[^s3]

The motivation is a known gap: "even when attention is directed toward relevant inputs, the feed-forward layers may still fail to integrate this information into the final representations used for generation".[^s4] The score therefore reads the output of that integration rather than the attention that feeds it. Its interpretation is stated by the authors: "a smaller value suggests possible drift toward parametric memory and, therefore, higher hallucination risk".[^s5]

In the paper's setting, SAS carries more of the signal than attention concentration does. Both measures differ significantly between truthful and hallucinated answers, "with effect sizes indicating a moderate (SAS) and small (PRD) association".[^s6] The two are weakly correlated, so they capture different things: see [[shortest-path-attention-concentration]]. In the ablation, "SAS-only significantly outperforms PRD-only in AUC on both models".[^s7]

The claim in the introduction is stronger than the effect size that follows it. The authors write that "hallucinations are strongly associated with weak semantic grounding, as indicated by low SAS scores", but the measured association for SAS is moderate. The reading that holds is the moderate one.[^s8]

## Limits

The score is one number per answer token, pooled to a sentence mean. Its maximum over the triple set means one sufficiently similar triple is enough for a token to score high, whether or not that triple supports the answer's entity. The paper does not test that case directly. (My inference from the formula.)

The comparison is an embedding similarity between a generator's hidden state and a triple's encoding by the same model. The [[semantic-illusion]] note records that embedding and entailment scores can place plausible hallucinations with faithful text. Whether SAS inherits that failure was not tested in this work; the paper reports that it beats semantic baselines on its own set, not that it resists the illusion. (My caution, not a finding.)

The setup is narrow. The experiments use one dataset, MetaQA-1hop, with a fixed triple budget: "For MetaQA-1hop, we set K = 20 triples". The layer is fixed to "a top transformer layer just before the final output projection", and the text read here reports no sweep over layers.[^s9] The detector that uses SAS reaches its best AUC only after adding surface features, "indicating that surface features enhance classification accuracy", so SAS by itself is not the full detector.[^s10]

The labels are surface-level as well: truthful means exact match or sufficient token overlap with the gold answer. A correct answer phrased differently can be labeled wrong, and SAS is evaluated against those labels.

## Related

- [[shortest-path-attention-concentration]] — the attention-side measure; PRD says where attention goes, SAS says whether the answer's representation matches the knowledge that was attended.
- [[semantic-illusion]] — why embedding-based grounding scores can credit plausible hallucinations; the caution applies to any cosine alignment score.
- [[hidden-evidence-drift]] — a correct answer can rest on evidence that shifts unnoticed, the same gap between answer and evidence use that SAS tries to measure.
- [[parametric-suppression]] — deep feed-forward layers overwriting context with priors, the mechanism SAS is meant to detect from outside.

[^s1]: arxiv-2512-09148 — "and encoded by the same language model (LM)"
[^s2]: arxiv-2512-09148 — "take the maximum over a finite set"
[^s3]: arxiv-2512-09148 — "to focus on positive semantic alignment"
[^s4]: arxiv-2512-09148 — "even when attention is directed toward relevant inputs, the feed-forward layers may still fail to integrate this information into the final representations used for generation"
[^s5]: arxiv-2512-09148 — "a smaller value suggests possible drift toward parametric memory and, therefore, higher hallucination risk"
[^s6]: arxiv-2512-09148 — "with effect sizes indicating a moderate (SAS) and small (PRD) association"
[^s7]: arxiv-2512-09148 — "SAS-only significantly outperforms PRD-only in AUC on both models"
[^s8]: arxiv-2512-09148 — "hallucinations are strongly associated with weak semantic grounding, as indicated by low SAS scores"
[^s9]: arxiv-2512-09148 — "from a top transformer layer just before the final output projection"
[^s10]: arxiv-2512-09148 — "indicating that surface features enhance classification accuracy"
