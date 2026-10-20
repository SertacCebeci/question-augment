---
description: "Among KV cache compressions, dropping reasoning tokens (eviction) harms answer support, while keeping every token at 2-bit precision (quantization) stays close to the full cache."
aliases: ["coverage versus precision", "token coverage under KV compression", "eviction versus quantization"]
sources: ["doi-10-48550-arxiv-2608-01631"]
---
# Cache coverage over precision

A KV cache compression can fail along two different axes. It can drop states, so some earlier tokens are no longer available to the model (coverage). Or it can keep every state and store each one in fewer bits (precision). The paper separates these with a single control and finds that the two axes have very different effects on reasoning.

Token-eviction methods keep a subset of states and discard the rest. The quantization control, KIVI at 2 bits, keeps all of them at reduced precision. The paper describes the control as one that "reduces the precision of cached states while preserving token coverage over the reasoning trace."[^c1] Its results "remain close to Full-KV across all metrics."[^c2] The eviction methods, by contrast, show the answer-evidence gap described in [[answer-evidence-gap]].

The paper gives a mechanism. Eviction "risk breaking the dependency structure and verification steps required for valid derivations," because intermediate tokens are the ones removed.[^c3] Quantization "retains the tokens in the reasoning process," so the paper reads the result as showing that "preserving broad coverage of evidential states matters more for reasoning faithfulness than preserving them at full precision."[^c4] In the abstract the conclusion is put as a suspicion about the failure's source: a coverage-preserving control is "substantially less affected, suggesting that the failure is tied less to KV memory reduction itself than to losing access to parts of the reasoning trace."[^c5]

The consequence for measurement is my inference, not a result stated in the paper. If memory is reduced by discarding states, the loss of evidence can hide behind a flat accuracy number, because accuracy does not see the chain. If memory is reduced by lowering precision on the same states, the paper's measurements suggest the reasoning is much less disturbed. The paper states this as its finding; it is not a recommendation about which method to deploy.

## Limits

- Only one quantization method is in the study, against ten eviction methods and one trace set. The abstract describes "ten token-eviction KV compression methods and one quantization method on three models."[^c6] Whether other bit widths or quantizers behave the same is not tested in the text. My inference: the claim rests on one precision level, 2-bit, so it says nothing about the gentle end of the precision range.
- The comparison is made under a 256-token budget for eviction. The paper says that at larger budgets results cluster together, so the coverage penalty may look smaller there.[^c7]
- The mechanism is offered as an interpretation of behavioural results. The paper does not attribute cache entries to answer or evidence roles, and it does not claim "that the cache factorizes into distinct answer and evidence components."[^c8]
- Quantization keeps all tokens but changes their values. A quantized state can be less precise in ways the chain-consistency judge does not see. The paper's judge-based labels cover the chain text only.

## Related

- [[answer-evidence-gap]] — the failure this contrast is used to explain; the gap is what the eviction methods show and the quantization control avoids.
- [[quantization-causal-drift]] — a different precision question: weight quantization in a model, not the cache. There the drift on causal reasoning was small at 8B, which fits the idea that precision alone is not the main lever, though the two measurements are not the same object.

[^c1]: doi-10-48550-arxiv-2608-01631 — "states while preserving token coverage over the reasoning trace."
[^c2]: doi-10-48550-arxiv-2608-01631 — "Its results remain close to Full-KV"
[^c3]: doi-10-48550-arxiv-2608-01631 — "eviction methods risk breaking the dependency structure and verification steps required"
[^c4]: doi-10-48550-arxiv-2608-01631 — "Quantization, by contrast, retains the tokens in the reasoning process,"
[^c5]: doi-10-48550-arxiv-2608-01631 — "substantially less affected, suggesting that the"
[^c6]: doi-10-48550-arxiv-2608-01631 — "methods and one quantization method on"
[^c7]: doi-10-48550-arxiv-2608-01631 — "often made results cluster near Full-KV, making it"
[^c8]: doi-10-48550-arxiv-2608-01631 — "that the cache factorizes into distinct answer and"
