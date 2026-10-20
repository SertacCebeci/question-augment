---
description: "A failure seen in a long dialogue is rewritten as a single-shot case and kept only if a reference model reproduces it, so the probe is selected for the failure it was built to detect."
aliases: ["replicated mistake scenarios", "conversation-to-single-shot distillation", "mistake-to-QA distillation"]
sources: ["doi-10-48550-arxiv-2512-20983"]
---
# Mistake distillation to a single-shot probe

A conversation-level score says that an interaction failed, not where or why. The paper's stated gap is that "we know that an interaction failed, but not how or why."[^d1] Post-training refinement needs more than that: it has to locate "where in a conversation reasoning broke down."[^d11] The method is to turn each localized failure into a short self-contained item and then test whether the failure can be provoked again without the conversation around it.

The pipeline runs in stages. A simulated patient and doctor hold a conversation, and an LLM judge scores it on many rubric dimensions; the paper mines "low-scoring dimensions (score ≤ 3)" and turns them into structured mistake records, deduplicated within each conversation.[^d2] Each unique mistake is then rewritten as a single-shot vignette, "designed to trigger the same error."[^d3] The vignette is the probe. It has no prior turns, and its only job is to reproduce the reasoning slip that the conversation showed.

The step that gives the method its character is replication. Each scenario is run on two reference models, and "a scenario is considered replicated if either model replicates the mistake."[^d4] A scenario that both models handle correctly is not discarded at once: a reflection step "generates a more challenging version," which is retested on the same two models.[^d5] Of 7,010 extracted mistakes, "3390/7010 mistakes were reproduced."[^d6] Only then do medical experts check validity and realism, on a subset: "215 mistakes (of which 211 unique) were validated by medical experts."[^d7]

What transfers from this is a construction, not a result. A failure located in a long interaction can be reduced to a single question that a model either fails or passes, and that outcome can serve as a label for a benchmark. The replication filter also makes the label carry information: an item enters the pool because some model failed it, and it stays only as long as that failure recurs. On my reading of the paper's limitations, this means the 12-model evaluation is not a neutral sample of medical questions.

## Limits

- The selection is on failure. Scenarios were kept if Gemini 2.5 Pro or GPT-5 erred, and the scores of other models are measured on that subset. My reading of the paper's limitations section is that this biases the final benchmark toward questions where those two models failed. The paper gives this as a limitation and does not measure its size.
- Equivalence to the original conversation is not measured. Experts checked that each mistake and scenario is "valid" for clinical accuracy and realism.[^d8] That is a validity check on each item, not evidence that the single-shot probe fails for the same reason as the conversation it came from. The generator is asked to make the scenario "reliably elicit[] the same reasoning challenge," and that claim is the generator's intent, not a measured match.[^d9]
- The expert check covers 211 unique mistakes out of 3,390 replicated ones. The twelve-model results rest on that subset.
- Judging is binary. The replication test and the scoring both use "an LLM judge" that returns a boolean.[^d10] Where an answer is partly right, the binary verdict forces it to one side. My reading of the paper's limitations is that this threshold is set by the judge alone.
- The dimensions are not independent. The paper notes redundancy among them, so the same underlying failure may be counted more than once.
- The claim that the approach generalizes beyond medicine is not tested here. The only domain is medical, and the simulated patients are LLMs, not real patients.

## Related

- [[controlled-error-injection]] — the other way to get a labelled wrong answer: edit a correct response at a known point. Here the error is a real model failure, and the label is a replication outcome rather than an edit.
- [[hallucination-diagnosis-task]] — the localization task that a per-turn or per-step error label is meant to serve; this paper's pipeline builds its labels from conversation-level judging instead.

[^d1]: doi-10-48550-arxiv-2512-20983 — "we know that an interaction failed, but not how or why"
[^d2]: doi-10-48550-arxiv-2512-20983 — "We analyze low-scoring dimensions (score ≤ 3)"
[^d3]: doi-10-48550-arxiv-2512-20983 — "Each extracted mistake is converted into a single-shot question describing a clinical scenario designed to trigger the same error"
[^d4]: doi-10-48550-arxiv-2512-20983 — "A scenario is considered replicated if either model replicates the mistake."
[^d5]: doi-10-48550-arxiv-2512-20983 — "a reflection step generates a more challenging version"
[^d6]: doi-10-48550-arxiv-2512-20983 — "A total of 3390/7010 mistakes were reproduced"
[^d7]: doi-10-48550-arxiv-2512-20983 — "a total of 215 mistakes (of which 211 unique) were validated by medical experts"
[^d8]: doi-10-48550-arxiv-2512-20983 — "Medical experts reviewed each mistake and its corresponding scenario for clinical accuracy and realism"
[^d9]: doi-10-48550-arxiv-2512-20983 — "reliably elicits the same reasoning challenge"
[^d10]: doi-10-48550-arxiv-2512-20983 — "An LLM judge (Gemini 2.5 Flash) evaluates each response using a boolean decision (true/false)"
[^d11]: doi-10-48550-arxiv-2512-20983 — "where in a conversation reasoning broke down"
