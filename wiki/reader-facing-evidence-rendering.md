---
description: "Holding the conversation and answer contract fixed, the reader-facing artifact alone moves memory-QA accuracy 24–49 points per model; evaluations should report it or control it."
aliases: ["evidence rendering", "reader-facing artifact", "rendering effect on memory QA", "artifact spread", "reader-facing evidence artifact"]
sources: ["doi-10-48550-arxiv-2608-23568"]
---
# Reader-facing evidence rendering

A memory or retrieval-augmented system does not hand the answering model a conversation. It hands the model a rendering of one.[^c1] The rendered text is what the work calls the reader-facing evidence artifact. It fixes which turns appear, how many are kept, whether a conflict between two statements has been settled, what metadata surrounds the value, and whether the text carries any cue that the model may abstain.

Two artifacts can encode the same fact and still be different inputs. The work's example is a user who says they live in Boston, later says they moved to Denver, and is then asked where they live now. A ChatGPT-style memory entry, a MemGPT-style typed record and a LangChain-style paragraph summary all carry the answer, yet the work says they "are not equivalent reader inputs."[^c2]

## What is measured

The experiment holds the underlying dialogue, the question and the expected answer fixed, and varies only the artifact the answering model reads. The main setting is 500 LongMemEval questions and nine commercial models, with tools, search and provider-native memory disabled. The deployed-style templates "create a 24–49 point accuracy spread per model."[^c3] Across models the best-to-worst spread is "24.6–48.8 points per model."[^c4] Across the diagnostic and budget controls, "measured accuracy ranges from near zero to 82%, depending on" what artifact is shown.[^c5]

The point is that a reported gain between two memory systems may come from the artifact each one hands its reader. The work states the design rule directly: the reader "sees only the rendered artifact and a fixed free-form answer contract."[^c6] The output format is held constant on purpose, so that only the input side varies. Prior work on fixed output schemas, which the work cites, asks the converse question.

## Where the answer enters

The work builds a five-level packet ladder from one store of turn-addressed dialogue. Conflicts between candidate events are resolved by precedence, and a current-state value exists only when a slot collapses to one applicable, non-blocked event. The lowest level is "P0 raw_packet, with witness addresses and blocker flags but no answer text."[^c7] Levels P0 and P1 leave the answer out, and every model stays near zero. At P2 the resolved value is written into the packet body, and "responsive models recover to 15–25% at P2."[^c8] Metadata added above P2 "changes accuracy by at most" two points per model.[^c9]

On this evidence, the variable that moves accuracy is whether the answer-bearing value is written into the artifact at all. The surrounding packet surface, at least in this ladder, moves it very little. This is an inference from a ladder whose levels differ in several respects at once, so it tells where the failure sits, not which property of the wording is responsible.

## Deployed-style surfaces

The template comparison renders the same dialogue as ChatGPT-style natural-language entries, LangChain session summaries, MemGPT-style typed JSON records and raw conversation. Under the primary substring scorer, the natural-language entries have higher point estimates than raw conversation on "point estimates than raw conversation on seven of" nine models. LangChain summaries are the weakest surface, and "summaries are consistently weakest (4.4–10.6%)."[^c10] This comparison is not a pure same-content ablation: it is "rather than a pure same-content ablation," since the surfaces also differ in which turns they include.[^c11]

## The artifact can switch answering off

The artifact also decides whether a model answers. Three models scored 0.0% on the formal ledger packets, yet answered the same facts from natural-language entries at 45.4–53.4%. The work reads this as "artifact/prompt-triggered abstention rather than" a missing capability.[^c12] It adds that "formal ledger packets can trigger refusal" even when compact natural-language evidence remains usable.[^c13] This links the note to [[abstention]]: when abstentions count as incorrect, a model that abstains more loses overall accuracy, and its answered-only score can look better. The work gives one case, where the answered-only figure was "83.7% conditional accuracy mostly because it abstains."[^c14] So the reported number depends on the artifact and on how abstention is scored. The refusal here is prompt-dependent in the same way that [[instruction-gated-refusal]] describes for missing evidence.

## Reporting norm

The work draws a norm from these results: "These results support a reporting norm," that memory and RAG evaluations should state the reader-facing evidence artifact or include a fixed-artifact control.[^c15] Without that control, the 24–49 point spread would be indistinguishable from model or pipeline progress. The norm is the work's recommendation, and the measured spread is what supports it.

## Limits

- The deployed-style templates are deterministic approximations. The work says they are not "evaluations of ChatGPT, LangChain, MemGPT, or" any product implementation.[^c16] They "omit real retrieval errors, summarization errors, and pipeline artifacts."[^c17]
- The budget control does not separate localization from rendering. The work says an oracle raw-excerpt baseline "would further separate localization from rendering," and that baseline was not run.[^c18] See [[matched-budget-evidence-comparison]] for the budget side.
- The scorer is a substring match. The work reports that judge rescoring "shows mixed" model-specific significance for the template ordering, so only the larger effects are robust across scorers.[^c19]
- The work's own caution is that its results show "rendering can materially change measured accuracy," not a universal ranking of one surface over another.[^c20] The benchmark family is LongMemEval, with LoCoMo and HotpotQA as transfer checks, and nine models.
- What the artifact does to refusal is described, not explained. The work treats the refusal as an "artifact-and-prompt interaction," and does not isolate which part of the prompt triggers it.

## Related

- [[matched-budget-evidence-comparison]] — the budget control, in which the raw-versus-structured ordering reverses under a matched word budget.
- [[compressed-memory-versus-raw-retrieval]] — the same raw-versus-compressed question for behavior logs, where a budget confound was left open.
- [[format-restriction-effect]] — the output-side counterpart: asking for a fixed schema in the answer, where this note varies the evidence the model reads.
- [[prompt-content-over-surface-form]] — codebook classification where informational content mattered more than surface form, a related claim about what changes accuracy.
- [[abstention]] — the scoring question of how abstentions enter accuracy.
- [[instruction-gated-refusal]] — refusal that depends on the prompt instead of on missing evidence.

[^c1]: doi-10-48550-arxiv-2608-23568 — "it hands the reader a rendering of one."
[^c2]: doi-10-48550-arxiv-2608-23568 — "not equivalent reader inputs."
[^c3]: doi-10-48550-arxiv-2608-23568 — "deployed-style templates create a 24–49 point accuracy spread per model."
[^c4]: doi-10-48550-arxiv-2608-23568 — "24.6–48.8 points per model."
[^c5]: doi-10-48550-arxiv-2608-23568 — "measured accuracy ranges from near zero to 82%, depending on"
[^c6]: doi-10-48550-arxiv-2608-23568 — "Externally, the reader sees only the rendered artifact and a fixed free-form answer contract."
[^c7]: doi-10-48550-arxiv-2608-23568 — "P0 raw_packet, with witness addresses and blocker flags but no answer text"
[^c8]: doi-10-48550-arxiv-2608-23568 — "responsive models recover to 15–25% at P2"
[^c9]: doi-10-48550-arxiv-2608-23568 — "Metadata above P2 changes accuracy by at most"
[^c10]: doi-10-48550-arxiv-2608-23568 — "summaries are consistently weakest (4.4–10.6%)."
[^c11]: doi-10-48550-arxiv-2608-23568 — "rather than a pure same-content ablation"
[^c12]: doi-10-48550-arxiv-2608-23568 — "artifact/prompt-triggered abstention rather than"
[^c13]: doi-10-48550-arxiv-2608-23568 — "formal ledger packets can trigger refusal"
[^c14]: doi-10-48550-arxiv-2608-23568 — "83.7% conditional accuracy mostly because it abstains."
[^c15]: doi-10-48550-arxiv-2608-23568 — "These results support a reporting norm"
[^c16]: doi-10-48550-arxiv-2608-23568 — "not as evaluations of ChatGPT, LangChain, MemGPT, or"
[^c17]: doi-10-48550-arxiv-2608-23568 — "so it omits real retrieval errors, summarization errors, and pipeline artifacts."
[^c18]: doi-10-48550-arxiv-2608-23568 — "would further separate localization from rendering."
[^c19]: doi-10-48550-arxiv-2608-23568 — "judge rescoring shows mixed"
[^c20]: doi-10-48550-arxiv-2608-23568 — "rendering can materially change measured accuracy"
