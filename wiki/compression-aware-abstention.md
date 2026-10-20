---
description: "A trained LoRA policy that answers only when the answer-bearing evidence survived KV-cache eviction, and refuses when the compressor removed it."
aliases: ["compression-aware abstention"]
sources: ["khodabandehlou-2026", "arxiv-2512-12008"]
---
# Compression-aware abstention

> KV-cache compression evicts context tokens under the assumption that
> low-importance tokens carry no answer-relevant signal; when that
> assumption fails for a given query the model is left with an input
> missing exactly the evidence it needs, and a base model tends to fabricate
> a confident wrong answer rather than notice the gap.

## Definition / Mechanism

Khodabandehlou & Krishnamachari (2026) formulate compression-aware
abstention as a supervised learning problem: given a context $c$, a query
$q$ and a per-token KV-cache survival mask $m$ produced by a compressor at
retention ratio $r$, a small LoRA adapter (10.1M parameters, rank 16, on
the four attention projections of Qwen2.5-7B-Instruct) is trained on the
truncated input $\tilde c(m)$ to output the answer when the supporting
evidence survived and a fixed refusal string when it did not, splitting the
loss as $\mathcal{L}=\mathcal{L}_{\text{CONF}}+\mathcal{L}_{\text{ABS}}$ so
that over-answering and over-refusing are penalized separately.[^c1]

Trained on ≈2.6K compression-labeled MuSiQue 2-hop examples, the adapter
raises honest accuracy at every tested retention ratio (0.05–0.80) over the
unaided base model, and cuts confident-wrong answers on evidence-removed
examples from 232 to 7 (a 97% reduction) while preserving the base's
correct-answer rate on evidence-retaining examples (answerability
preservation ratio 1.00–1.36 across eight prompt-style cells). Under actual
compressed-cache decoding (not just prompt-style truncation), a variant
trained across multiple compressors raises correct answering on
evidence-retaining examples from 4% to 25% aggregate over the unaided base,
and from 1.4% to 32% at high retention.[^c2]

A prompt-only abstention baseline (instructed to refuse when unsure, no
training) over-abstains: at high retention it refuses roughly half of the
examples where the evidence actually survived, versus 6–10% for the
trained adapter — evidence that the trained policy is conditioning on
content, not on a fixed prior. A threshold policy on retention ratio alone
(ignoring the truncated input) can reach higher *aggregate* honest accuracy
(0.93) than either trained adapter, because the gold-label distribution is
itself U-shaped in $r$; the authors use this to argue aggregate accuracy is
not a valid measure of compression-awareness and report per-ratio slices
instead.[^c3]

## Why it matters

This is a trained instance of the general reject-option decomposition
$(f,g)$ in [[abstention]] — here the selection function $g$ is conditioned
on the survival mask of a specific evidence-destroying process (context
compression) rather than on a generic confidence score. It gives stall 7
("is $|W|$ small enough?") a concrete, checkable failure mode: an agent
whose context has been silently truncated by a memory-saving layer below
it has no signal that $|W|$ grew back unless the truncation itself is
observable and the training target is built from it.[^c4]

## Transfer

| | |
|---|---|
| In its home field | KV-cache eviction for inference-memory reduction, scored by a compressor's own importance rule, evaluated as behavior preservation under compression |
| Here | any asking/answering agent whose context budget is cut below what a prior turn established, not only by a KV-cache compressor |
| What survives | training a refuse-or-answer policy directly from a record of *what evidence was removed*, rather than from the model's own confidence; tight (near-verbatim) evidence spans as the granularity that makes the training label informative |
| What does not | the specific mask $m$ and retention ratio $r$ are KV-cache-compressor artifacts; a general context-management layer would need its own definition of "survival" to reuse the training recipe |

## Limits

- The claim rests on a single base model family (Qwen2.5-7B-Instruct, with
  Llama-3.1-8B-Instruct as one held-out check) and one QA format (MuSiQue
  2-hop, English); the paper does not test open-ended or multi-turn asking.[^c5]
- The gold label is built from a governance ground truth the deploying
  system controls (the compressor's own mask); an agent that does not
  instrument its own context-truncation step cannot construct this
  supervision at all.[^c6]
- The survival mask $m$ is here a function of one compressor's rule at one retention ratio. A study of eviction on long reasoning traces (Hold Onto That Thought) finds that the rule, not only the budget, decides what survives, and that its ranking does not carry across settings: "No singular strategy is dominant for the non-reasoning Llama-3.1-8B-Instruct."[^c7] Its attention-based rules keep the question's critical keywords at a higher rate: "SnapKV-D and H2O retain critical tokens at a higher rate than other methods."[^c8] A label built from one rule's mask therefore does not describe another rule's cache. The same study also reports that small budgets can lengthen the output: "occurs more frequently, resulting in a higher likelihood of critical token eviction, resulting in longer reasoning."[^c9] The abstention policy is trained to answer or refuse and does not measure this cost; that is my inference from the two papers, not a result of either.

## Related

[[abstention]] · [[calibration]] · [[semantic-entropy]] · [[evidence-survival-fraction]] · Commitment

[^c1]: khodabandehlou-2026 — "The adapter parameters θ are LoRA weights (Hu et al., 2022) attached to a frozen base LLM f , optimizing"
[^c2]: khodabandehlou-2026 — "A 10.1M-parameter LoRA adapter trained on ∼2.6K MuSiQue 2-hop QA examples reduces base-model hallucinations by 97% under prompt-style truncation while preserving correct answering on evidence-retaining examples."
[^c3]: khodabandehlou-2026 — "at high retention, they abstain on about half of C ONFIDENT-gold examples, while the trained adapter abstains on only 6–10%."
[^c4]: khodabandehlou-2026 — "we ask whether the compressed context still contains enough evidence to support an answer"
[^c5]: khodabandehlou-2026 — "Qwen2.5-7B-Instruct (Qwen Team, 2024) for all main results; Llama-3.1-8B-Instruct (Llama Team, Meta AI, 2024) as a held-out base model."
[^c6]: khodabandehlou-2026 — "A KV cache compressor at retention ratio r produces aPper-token survival mask m ∈ {0, 1}nc"
[^c7]: arxiv-2512-12008 — "No singular strategy is dominant for the non-reasoning Llama-3.1-8B-Instruct."
[^c8]: arxiv-2512-12008 — "SnapKV-D and H2O retain critical tokens at a higher rate than other methods."
[^c9]: arxiv-2512-12008 — "occurs more frequently, resulting in a higher likelihood of critical token eviction, resulting in longer reasoning."
