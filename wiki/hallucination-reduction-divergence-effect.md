---
description: "Hallucination-reduction decoding and prompting changes divergent creativity in method-specific directions: CoVe raises it, DoLa lowers it, RAG leaves it flat, convergent creativity unchanged."
aliases: ["creativity cost of hallucination reduction", "hallucination-creativity relationship", "factuality-creativity trade-off"]
sources: ["arxiv-2512-11509"]
---
# Hallucination reduction and divergent creativity

Reducing hallucination is not one lever with one creative cost. Three
hallucination-reduction methods, re-implemented on LLaMA, Qwen and Mistral
models, moved divergent creativity in different directions. Chain of
Verification (CoVe) drafts an answer, writes verification questions,
answers them and revises. "This iterative verification chain enables models
to critically" evaluate and correct their own outputs before finalizing.[^c1]
Decoding by Contrasting Layers (DoLa) "contrasts the predictions from a
higher layer with those from" an earlier one, chosen at each step by
Jensen-Shannon divergence.[^c2] Retrieval-Augmented Generation (RAG) places
retrieved passages in the prompt.

The measured result is a sign difference. "these methods have opposing
effects on divergent creativity."[^c3] CoVe "decoding enhances divergent
creativity across" most evaluated models, with the largest gain near 12.5%
above baseline for LLaMA 1B on NeoCoder.[^c4] DoLa "systematically dampens
divergent creativity across diverse tasks."[^c5] RAG "has no effect on
divergent creativity"; its per-model shifts run both up and down around
zero.[^c6] Convergent creativity, the share of correct solutions that
satisfy all constraints, is the part the authors report as "largely
unaffected."[^c7] The authors had expected all three to suppress creativity,
since "creative thinking often relies on making unconventional associations"
that can look like hallucination; the sign of the effect did not match that
expectation.[^c8]

The authors offer a mechanism for DoLa, as a hypothesis. Linear probes
trained to predict divergent output found that "early layers exhibit stronger
correlations with creativity than later layers."[^c9] DoLa subtracts early-layer
predictions, so if early layers carry divergent representations, the
contrast would remove them. Amplifying the top creativity-correlated layers
and suppressing the bottom ones, during decoding, "boosts divergent creativity"
on NeoCoder for LLaMA and Qwen-coder without lowering convergent creativity.[^c10]
The authors call this "promising" and "preliminary."[^c11] For CoVe the
mechanism is only conjectured: CoVe may prompt the model to reconsider rather
than commit early, and the authors did not test it.[^c12] For RAG the
authors attribute the null effect to retrieval quality, which they did not
measure.[^c13]

My inference, not the paper's: the answer to "does less hallucination mean less
creativity?" depends on which intervention is meant. Under this evidence the
same hallucination goal can cost divergent output (DoLa), add to it (CoVe) or
leave it unchanged (RAG). A single "hallucination versus creativity" curve
would hide that.

## Limits

- Creativity is measured on two benchmarks, NeoCoder (199 programming
  problems) and CS4 (story generation). The authors say these "are only a
  proxy of actual scientific hypothesis generation."[^c14] No scientific
  hypothesis task was run.
- Model coverage is uneven. NeoCoder used five models (LLaMA 70B, 8B, 1B,
  Mistral 7B, Qwen-Coder 7B); CS4 used three, and the layer amplification
  result is shown for LLaMA 8B only on CS4.[^c15] The consistency claim across
  families and scales ("suggests that the creativity-hallucination relationship
  is an") is a reading of these runs, not a test of all models.[^c16]
- Mistral with CoVe is not uniform: "Mistral 7B, however, represents a
  deviation from this overall upward trend," moving from about -3% to +2% on
  NeoCoder.[^c17]
- RAG was run on NeoCoder only: "was applied only to the NeoCoder benchmark."[^c18]
- No ablation isolates CoVe's mechanism: "we did not conduct ablation studies
  to isolate the mechanism."[^c12]
- The LLM judge (GPT-5-mini) scored several metrics: "Wherever LLM-as-a-Judge
  evaluation was required."[^c19] The slices I read do not report judge
  agreement or its effect on the sign of the results.
- Each generation setting was run three times and averaged; the slices I read
  report means, not spread across runs, so the size of a 2-4% shift against
  run-to-run noise is not established here.
- The layer-amplification result is one method on two benchmarks and does not
  show that DoLa's factuality gain can be kept while its creativity cost is
  removed; that combination was not measured.

## Related

- [[technique-novelty-divergent-creativity]] — how the divergent and convergent scores used here are defined
- [[innovation-correctness-tradeoff-in-problem-generation]] — novelty and correctness pulled apart by fine-tuning on existing problems; this note concerns decoding and prompting, where convergent success stayed flat
- [[null-image-logit-subtraction]] — another contrastive decoding that subtracts a second pass from the main one; its effect on creativity is not measured in this work
- [[divergent-convergent]] — a different "divergent/convergent": a design-process split, not a measure of model outputs

[^c1]: arxiv-2512-11509 — "This iterative verification chain enables models to critically"
[^c2]: arxiv-2512-11509 — "contrasts the predictions from a higher layer with those from"
[^c3]: arxiv-2512-11509 — "these methods have opposing effects on divergent creativity"
[^c4]: arxiv-2512-11509 — "CoVe decoding enhances divergent creativity across"
[^c5]: arxiv-2512-11509 — "DoLa systematically dampens divergent creativity across diverse tasks"
[^c6]: arxiv-2512-11509 — "RAG has no effect on divergent creativity"
[^c7]: arxiv-2512-11509 — "Meanwhile, convergent creativity is largely unaffected."
[^c8]: arxiv-2512-11509 — "creative thinking often relies on making unconventional associations"
[^c9]: arxiv-2512-11509 — "early layers exhibit stronger correlations with creativity than later layers"
[^c10]: arxiv-2512-11509 — "This method boosts divergent creativity"
[^c11]: arxiv-2512-11509 — "We provide a promising preliminary"
[^c12]: arxiv-2512-11509 — "we did not conduct ablation studies to isolate the mechanism"
[^c13]: arxiv-2512-11509 — "This neutral effect could stem from retrieval quality issues."
[^c14]: arxiv-2512-11509 — "proxy of actual scientific hypothesis generation"
[^c15]: arxiv-2512-11509 — "CS4 results are evaluated on LLaMA 8B only due to computation"
[^c16]: arxiv-2512-11509 — "suggests that the creativity-hallucination relationship is an"
[^c17]: arxiv-2512-11509 — "Mistral 7B, however, represents a deviation from this overall upward trend"
[^c18]: arxiv-2512-11509 — "was applied only to the NeoCoder benchmark"
[^c19]: arxiv-2512-11509 — "Wherever LLM-as-a-Judge evaluation was required"
