---
description: "Long reasoning can carry forward only verified intermediate lemmas, not the whole trajectory, so the next round starts from a compressed, checked record of partial progress."
aliases: ["lemma library", "lemma memory", "sub-lemma repository", "verified intermediate-result memory", "lemma-based compression"]
sources: ["arxiv-2512-10739"]
---
# Verified lemma memory

A reasoning agent cut off by its context window can keep its progress outside the window if it writes that progress down as intermediate claims rather than as the trajectory that produced them. In Intern-S1-MO the agent runs in rounds. A reasoner attempts the problem, a summarizer compresses that round's reasoning into sub-lemmas, a verifier checks them, and the verified ones go into a library that the next round receives together with the question.[^c1] The stated purpose is to extend the reasoning horizon "beyond a single context window through hierarchical decomposition."[^c2] The mechanism rests on the compression step: the agent "compresses its current reasoning history into concise sub-lemmas in a structured" memory repository, so that later rounds can reuse a result without re-running the exploration that produced it.[^c3]

Summarizing is not free. The authors write that "summarizing compelling exploration is as complex as the exploration process itself," because it requires distilling a result and checking its logic independently.[^c4] For that reason the library update gets its own reasoning turn: "a dedicated reasoning turn after each exploration step to update the lemma library."[^c5]

Verification is what makes the library safe to reuse. The authors' reason is error propagation: a model that relies on an erroneous premise "will expend significant resources trying to validate questionable results."[^c6] They argue that lemmas are easier to check than whole solutions, since "the verification of lemmas is comparatively more tractable than that of" the complete problem.[^c7] Each lemma receives several independent theorem-verifier calls, and the pass fraction "correctly identified is used as the confidence score", so the library holds a soft confidence per lemma rather than a single accept or reject bit.[^c8] The authors keep the scores soft on purpose; their check of lemma correctness is reported as explaining why verifier scores are "retained as soft confidence annotations."[^c9]

What was measured. The authors report that "approximately 70% of the explored" lemmas on the harder benchmarks are used in the final proof, which they read as lemmas doing "effective context compression and critical content delivery."[^c10] The average length ratio before and after compression "reaches approximately 64:1."[^c11] In the CNMO2025 ablation, which builds the system up from a single-round agent, the full system moves the score "from 178.0 to 232.4"[^c12], and the authors conclude that "each agent component brings consistent gains across all benchmarks."[^c13] A token-matched control is also reported: seven parallel samples of GPT-OSS-120B move from 11 to 18 on IMO2025, and the authors note that this "remains below Intern-S1-MO" at a comparable token budget. They read this as showing that "sampling alone does not account for the full improvement."[^c14][^c15]

## Limits

- The memory is never isolated. The ablation adds multi-round reasoning, theorem verification, process verification and then RL one after another, so the "+ Multi-round Reasoning" row carries the library and the extra rounds together. No row compares the library with a raw-trace memory of the same token count. (My inference from the table layout.)
- Utility is a proxy. A lemma left out of the final proof may have been a correctly ignored dead end, or a useful step the writeup did not cite. The ratio measures inclusion, not correctness.
- The cost is large. One Intern-S1-MO run consumes "391.7K generated tokens per problem on average"[^c16], against 55.9K for one GPT-OSS-120B rollout. The authors themselves say their token-matched comparison "is not a strict compute-matched" one, because hardware, wall-clock cost and implementation differ.[^c17]
- Small evaluation sets. The ablation leaves out IMO2025 because of "the limited number of problems in IMO2025," and uses HMMT, AIME and CNMO instead.[^c18]
- Verifier reliability rests on 50 manually annotated lemmas, with a lemma counted as accepted when its score "is greater than 0.25."[^c19] The threshold is the authors' choice and is not varied in the text read.
- The domain is mathematics, where a lemma is a checkable claim. For a question whose intermediate steps have no verifier, the same library has nothing to gate it. (My inference; not tested here.)

## Related

- [[context-register]] — another bounded state for a long-running agent. Its slots are typed and written by code for search; the lemma library holds proved claims written by a summarizer model and gated by a verifier.
- [[premature-closure]] — the answerer's commitment failure. The work names exhausted reasoning budget as one trigger; a lemma library is one way to keep partial progress from being discarded when the budget runs out.
- [[stop-continue-criteria-in-retrieval-loops]] — stopping rules for retrieve-reason loops. The memory decides what carries across rounds; a budget or verifier rule decides when the rounds stop.
- [[generative-verification]] — the checking step that the library depends on.

[^c1]: arxiv-2512-10739 — "the summarizer agent compresses the current reasoning"
[^c2]: arxiv-2512-10739 — "beyond a single context window through hierarchical decomposition"
[^c3]: arxiv-2512-10739 — "the agent compresses its current reasoning history into concise sub-lemmas in a structured"
[^c4]: arxiv-2512-10739 — "summarizing compelling exploration is as complex as the exploration process itself"
[^c5]: arxiv-2512-10739 — "a dedicated reasoning turn after each exploration step to update the lemma library"
[^c6]: arxiv-2512-10739 — "if they rely on erroneous historical premises, they will expend significant resources trying to validate questionable results."
[^c7]: arxiv-2512-10739 — "the verification of lemmas is comparatively more tractable than that of"
[^c8]: arxiv-2512-10739 — "correctly identified is used as the confidence score"
[^c9]: arxiv-2512-10739 — "retained as soft confidence annotations."
[^c10]: arxiv-2512-10739 — "approximately 70% of the explored"
[^c11]: arxiv-2512-10739 — "the average length ratio before and after compression, which reaches approximately 64:1."
[^c12]: arxiv-2512-10739 — "score from 178.0 to 232.4"
[^c13]: arxiv-2512-10739 — "each agent component brings consistent gains across all benchmarks."
[^c14]: arxiv-2512-10739 — "Parallel sampling improves GPT-OSS-120B from 11 to 18, but remains below Intern-S1-MO"
[^c15]: arxiv-2512-10739 — "sampling alone does not account for the full improvement"
[^c16]: arxiv-2512-10739 — "391.7K generated tokens per problem on average"
[^c17]: arxiv-2512-10739 — "It is not a strict compute-matched"
[^c18]: arxiv-2512-10739 — "the limited number of problems in IMO2025"
[^c19]: arxiv-2512-10739 — "a lemma is classified as verifier-accepted when its score is greater than 0.25"
