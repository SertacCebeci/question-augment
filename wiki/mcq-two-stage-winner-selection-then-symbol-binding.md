---
description: "In small LMs answering multiple-choice, the winning option is decodable in content space right after the last option; mapping it to an answer letter happens late, at the answer prefix."
aliases: ["decide then bind in MCQA", "symbol binding in multiple-choice", "winner selection and symbol routing"]
sources: ["arxiv-2601-03914"]
---
# MCQ two-stage computation: winner selection, then symbol binding

Answering a multiple-choice question is two jobs, not one: the model must find the right answer and then emit the symbol (letter) that stands for it. Wong, Nouwen and Gatt probe Llama-3.2-3B-Instruct and Qwen3-8B on ARC-Easy and a synthetic color-copying task, and find these jobs happen at different token positions.

## Mechanism

The newline after each option holds a linearly decodable signal of whether that option is correct. A probe trained on ARC-Easy transfers to color copying, where option-level AUC and top-1 accuracy both reach 1.0 in middle-to-late layers.[^c1]

A 4-way winner-identity probe shows a two-stage progression. Winner identity is decodable at the end-of-options checkpoint in intermediate layers, before the answer prefix appears. At the `Answer: (` prefix it stays weak until later layers, then rises sharply.[^c2]

Symbol permutations separate a content-coded decision from a symbol-coded one. The option symbols are reshuffled while the text order stays fixed, and the probes are not retrained. Against the new correct symbol, accuracy at the end-of-options checkpoint collapses, while accuracy in the answer region approaches ceiling. Against the winner's content position, the end-of-options probe stays strong in middle layers and collapses near emission.[^c3] The authors read this as the model selecting a winner in option/content space first, then binding it to the output symbol under the current symbol-content assignment.

Causal patching along the probe direction agrees. Patching at the earlier boundary does not by itself change the emitted answer. The probe-aligned effect rises sharply only at the final pre-emission token.[^c4] So the early signal is decodable but not the control variable.

This separates two things earlier work conflated: the model choosing the correct answer, and the model choosing the symbol to emit.[^c5] It also explains why analyses confined to the last token can miss early commitment. This is the authors' reading of their data.

## Why it bears on asking

A wrong letter can be a binding failure rather than a knowledge failure. A question's apparent difficulty then mixes the task with the format, which is the meta-task the authors name.[^c6] Letter-position and symbol-choice sensitivities (see [[mcq-answer-position-bias]]) would, on this account, act at the binding stage. That link is my inference; the paper does not test it.

## Limits

- Only two small model families (3B and 8B) and two tasks, one of them synthetic; the authors say localization may vary with scale, architecture and post-training.[^c7]
- Results use one prompt template and a direct single-symbol answer. Chain-of-thought or free-text answers may use other strategies.
- Probe-aligned patching has an asymmetry: binary probes are one-dimensional, multinomial ones richer, so failed interventions are not proof of no causal signal.[^c8]
- Attention-head-level interventions to separate the two stages are left for future work.

## Related

- [[mcq-answer-position-bias]] — position and label preferences that may act at the binding stage
- [[absent-answer-forced-choice-bias]] — forced-choice formats distort answers beyond knowledge
- [[format-compliance-normalized-performance-and-format-variance]] — format effects confounded with capability

[^c1]: arxiv-2601-03914 — "The ARC-Easy probe direction also transfers to the color copying task."
[^c2]: arxiv-2601-03914 — "winner identity exhibits a consistent two-stage progression"
[^c3]: arxiv-2601-03914 — "performance remains strong at end-of-options checkpoints in middle layers but collapses near emission."
[^c4]: arxiv-2601-03914 — "the probe-aligned representation that directly controls the answer token logits becomes causally effective only near emission."
[^c5]: arxiv-2601-03914 — "(a) the model selecting the correct answer; and (b) the model selecting the symbol to emit."
[^c6]: arxiv-2601-03914 — "this failure may stem from a misunderstanding of the target question, the MCQA format, or both."
[^c7]: arxiv-2601-03914 — "Mechanistic findings, especially localization claims about"
[^c8]: arxiv-2601-03914 — "This asymmetry means that differences in intervention"
