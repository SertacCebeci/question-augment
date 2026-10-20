---
description: "Procedural hallucination: a model fails to report a value present in its own context; errors split into gating (2A) and binding (2B), and the answer is often encoded but unused."
aliases: ["procedural hallucination", "present but not used", "Stage 2A/2B decomposition", "readout-stage routing failure"]
sources: ["arxiv-2602-19239"]
---
# Procedural hallucination as readout routing failure

A procedural hallucination is a failure to execute a verifiable specification given in the model's own prompt, as opposed to a factual hallucination about world knowledge.[^c1] The setting is a specification function g(W) that deterministically maps a prompt to one token in a known candidate set; the model hallucinates when its greedy output differs from g(W) although g is unambiguous.[^c2]

## Two stages of failure

The paper splits an error by what the model does at the readout position. A gate indicator marks whether the top token is a candidate at all. Stage 2A (gating) errors are those where the model does not enter answer mode, which the authors call a format or instruction-following problem.[^c3] Stage 2B (binding) errors are those where it enters answer mode but picks a wrong candidate, an information-routing problem often driven by recency bias.[^c4] Both are read from logprob margins (GateGap, ValueGap), so the classification needs only output logits.

In the hard regime on synthetic long-context key-value tasks, most errors were 2B: the model enters answer mode but selects the wrong candidate.[^c5] The abstract reports this across model families, with Qwen collapsing earliest as distance grows (my paraphrase of the robustness ordering Gemma > Llama > Qwen).

## Present but not used

On Stage 2B error trials a linear probe on the final-layer residual stream recovers the correct value far above chance (74% vs about 2% on Qwen2.5-3B, per the abstract). The authors conclude it is not a knowledge failure: the information is present and not routed to the output.[^c6] They formalize this as available information I(V;H) versus used information I(V;Y); their routing efficiency, the ratio of the two, measures how much of what is available the output exploits.[^c7] Procedural hallucination corresponds to a ratio far below 1. A pseudo-prior (answer rate after deleting the evidence while keeping template and recency cues) separates guessing from using the evidence.

## Intervention

Restating the true binding near the query ("checkpointing", every 128 tokens) converted 0/400 correct to 399/400 for Qwen2.5-3B at distance k = 1024 on one task.[^c8] That is evidence that the bottleneck is access at readout, not storage; the paper treats this as raising available information near the query.

## Limits

- Main results are synthetic binding tasks with a single-token candidate set; only one naturalistic variant is included. Whether open-ended question answering shows the same 2A/2B split is not established here.
- The probe recovery figure is for one model (Qwen2.5-3B) in my reading; I did not verify the other tables.
- Probe recovery shows the information is linearly decodable, not that the model could have used it; the "present but not used" reading is the authors' interpretation.
- The information-theoretic bounds (Fano, SDPI) assume things like a uniform value distribution; I did not check their proofs.
- Checkpointing is an oracle intervention: it assumes someone knows the true binding.

## Related

- [[visibility-action-gap]] — another case where information available to a system is not turned into the right action
- [[confidently-wrong-low-entropy-regime]] — errors made with confidence, where output signals do not reveal the failure
- [[retrieval-cue-disruption]] — failures of recall when cues are disrupted, adjacent to access-versus-storage

[^c1]: arxiv-2602-19239 — "Unlike factual hallucination, which"
[^c2]: arxiv-2602-19239 — "Let Ŷ (W ) denote the model’s next-token output at the readout"
[^c3]: arxiv-2602-19239 — "This is a format or instruction-following problem."
[^c4]: arxiv-2602-19239 — "This is an information-routing problem, often driven by recency"
[^c5]: arxiv-2602-19239 — "The model enters answer mode but selects the wrong candidate."
[^c6]: arxiv-2602-19239 — "This is not a knowledge failure."
[^c7]: arxiv-2602-19239 — "Routing efficiency captures how much of the available information the model actually exploits."
[^c8]: arxiv-2602-19239 — "it converts 0/400→399/400 correct"
