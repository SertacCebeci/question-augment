---
description: "In knowledge conflicts the gold answer often hits rank 1 mid-network, then deep FFN layers overwrite it with priors; contrasting context and null passes localizes the layers without labels."
aliases: ["parametric suppression", "knowledge-conflict layer overwrite", "CoRect"]
sources: ["arxiv-2602-08221", "arxiv-2512-07515"]
---
# Parametric Suppression

When retrieved evidence contradicts what a model memorized, the failure is not always that the model never used the evidence. Projecting each layer's hidden state through the unembedding head (the logit lens) shows the gold answer often wins at some depth and then loses at the output. Ma, Zhang and Nie (2026) name this Parametric Suppression: "the gold answer token often achieves a high probability in intermediate layers, only to be suppressed in the final output."[^c1]

## Measured prevalence

On 500 Natural Questions training cases involving knowledge conflicts, "282 out of 500 cases exhibit this flip phenomenon: the gold answer reaches Rank 1 at some point but is not the final prediction." They split into Middle Flip (154 cases, lost in later layers) and Last Layer Flip (128 cases, dominant until the final projection).[^c2] The authors read this as the model often possessing the answer yet failing to express it.[^c3] Their hypothesis, not tested here in isolation, is that certain deep FFN layers act as key-value memories for parametric facts and overwrite an evidence-consistent state that attention had built.[^c4]

## Locating the layers without the answer

Weight editors such as ROME need the target answer, which an open-ended RAG system lacks. CoRect replaces it in two stages. First, run the prompt twice, with the full context and with a null context of instruction tokens only. For each of the last k layers, the per-token score is the log-probability under the context pass minus that under the null pass; this is averaged and max-normalized. The top candidates are then filtered by the attention mass the final layer gives to their occurrences in the context, and the target maximizes information score plus a weighted attention score.[^c5]

Second, with target unembedding vector w, the suppressive layers are those whose update u_l has negative projection on w. Each gets a patch that cancels that projection, scaled by alpha. At alpha = 1 the suppression is only neutralized ("disinhibition"); above 1 the sign flips into active promotion. The final-logit change for the target is stated to be positive in either regime.[^c6] The framing is removal of the inhibiting component rather than injection of a new direction.[^c7]

## Why it matters for asking and answering

The context-versus-null contrast is a label-free measure of how much the evidence moved the model, the same signal that output-level decoders use, but here read per layer to say where the prior takes over. It separates "the model never found the answer" from "the model found it and lost it", which calls for different remedies.

## Limits

- The 56% figure counts any rank-1 appearance at any layer; the authors concede "some rank fluctuations may reflect legitimate reasoning steps", so not every flip is suppression.[^c8]
- Prevalence was measured on one dataset sample (500 NQ cases); the FFN-overwrite explanation is a hypothesis motivated by prior editing work, not isolated here.
- Cost: the method needs multiple passes and residual-stream access, so latency exceeds vanilla decoding and it is unavailable for black-box APIs.[^c9]
- Benchmark gains (QA and summarization) are reported by the authors; I did not read per-baseline numbers.
- A later detector study reports that the binary FFN-versus-context account is incomplete: relying on it alone is "insufficient for robust detection."[^c10] That study splits the output probability into per-block shares rather than tracking a flip across layers, so it does not test this note's FFN-overwrite hypothesis (see [[residual-probability-decomposition]]).

## Related

- [[context-fidelity-boosting]] — an output-level, context-versus-null-contrast bias that CoRect contrasts with by intervening inside the residual stream
- [[parametric-knowledge-gates-retrieval-noise-damage]] — another account of how parametric knowledge interacts with retrieved context
- [[dual-path-knowledge-boundary-probing]] — probing what the model internally knows

[^c1]: arxiv-2602-08221 — "the gold answer token often achieves a high probability in intermediate layers, only to be suppressed in the final output"
[^c2]: arxiv-2602-08221 — "282 out of 500 cases exhibit this flip phenomenon: the gold answer reaches Rank 1 at some point but is not the final prediction"
[^c3]: arxiv-2602-08221 — "the model often possesses the capability to solve the problem, yet fails to manifest it in the final generation"
[^c4]: arxiv-2602-08221 — "certain FFN layers overwrite this evidence-consistent state with parametric memories"
[^c5]: arxiv-2602-08221 — "one with a null context consisting only of the instruction tokens"
[^c6]: arxiv-2602-08221 — "setting α = 1 reduces the term to zero, strictly neutralizing the suppression"
[^c7]: arxiv-2602-08221 — "we frame this as disinhibition rather than injection"
[^c8]: arxiv-2602-08221 — "some rank fluctuations may reflect legitimate reasoning steps"
[^c9]: arxiv-2602-08221 — "it introduces non-negligible computational overhead compared to standard decoding"
[^c10]: arxiv-2512-07515 — "is insufficient for robust detection"
