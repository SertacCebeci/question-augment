---
description: "A search agent's stop-or-continue threshold can be misplaced two ways, over-search and under-search; both are diagnosed by answering at each step and trained away with preference pairs."
aliases: ["decision boundary misalignment", "over-search and under-search", "DAS", "decision boundary alignment for deep search agents"]
sources: ["openalex-org-w7127739895"]
---
# Search decision-boundary misalignment

A deep search agent repeatedly chooses between Search and Answer. Zhang et al. (2026) call the threshold at which accumulated information is enough to answer the *decision boundary*, and say that outcome-centric training leaves it misplaced.[^c1] The latent state K_t is Sufficient or Insufficient; it is never observed. Two errors follow.

## Two errors

- **Over-search** (efficiency failure): the agent searches although K_t is already Sufficient. Information gain is zero, the search cost is still paid, and Answer would have earned the full reward.[^c2]
- **Under-search** (accuracy failure): the agent answers while K_t is Insufficient, takes the penalty for an incorrect answer, and forgoes a search whose information value would have exceeded its cost.[^c3]

The two are one-sided errors of a single threshold. Moving the boundary to cut one raises the other.

## Diagnosis by intervention

Unchosen actions are unobservable, so the paper revisits each decision point after the trajectory ends and applies a do-operator. For a factual Search, it forces do(A_t := Answer) with an instruction to answer from the current state alone. A correct counterfactual answer means K_t was Sufficient, so the search was over-search.[^c4] For a factual Answer that turned out wrong, K_t is inferred as Insufficient directly, with no intervention. The intervention do(A_t := Search) is still run to produce a corrected trajectory.[^c5]

## Alignment from the counterfactuals

Each diagnosed error gives a preference pair. For over-search, the shorter answer-now trajectory is preferred and the original trajectory is rejected. For under-search, the corrected trajectory with the extra search is preferred and the premature one is rejected. The policy is fine-tuned with DPO on these pairs.[^c6] The setup used 20,000 pairs from NQ and HotpotQA, built from RL-tuned Qwen2.5-7B and 14B, with DPO beta 0.3 and LoRA.[^c7]

## What was measured

- Accuracy-only reinforcement learning trades one error for the other. On NQ with Qwen2.5-7B, RL raised EM from 0.190 to 0.410 and cut the under-search rate from 0.672 to 0.505. The over-search rate rose from 0.196 to 0.263.[^c8]
- Scale and workflow do not remove the problem. 14B models and inference-centric agents (GPT-4o, Gemini-2.5-Flash, DeepSeek-V3) still show both errors.[^c9]
- DAS lowered both rates and cut search queries and inference time versus the RL baselines, with the highest EM in nearly all configurations.[^c10]
- Ablation: dropping the under-search pairs gave the most efficient and most aggressive agent. Dropping the over-search pairs gave an over-cautious one. The two signals act antagonistically, so both are needed.[^c11]

## Limits

- The answer-now probe defines "sufficient" as "the forced answer happens to be correct". That is a proxy: a lucky guess is counted as sufficiency. The paper gives no check on this beyond the correctness test. This is my inference.
- Diagnosis needs gold answers, so the method applies to QA with verifiable ground truth, not to open-ended questions.
- The setting is Wikipedia retrieval with top-3 chunks and a few multi-hop QA sets. Nothing was tested on web-scale search or non-factoid tasks.
- The utility model (R_correct, R_incorrect, C_search, R_info) is stated but never estimated. The boundary is aligned by preference data, not by computing utilities.
- The diagnosis is per step on one sampled trajectory, so a counterfactual answer is one draw, not an expectation.

## Related

- [[counterfactual-search-routing-oracle]] — the same paired factual and counterfactual labelling, applied once before the first search rather than at every step.
- [[value-of-information]] — the formal utility rule that over-search and under-search are defined against, though here it is never computed.
- [[stopping-rules]] — the boundary is a learned stopping rule; the paper uses no sequential-test guarantee.
- [[abstention]] — the Answer side of the boundary, which here is always a committed answer rather than a refusal.

[^c1]: openalex-org-w7127739895 — "We identify the root cause as misaligned decision boundaries, the threshold determining when accumulated information suffices to answer."
[^c2]: openalex-org-w7127739895 — "An over-search error is strictly defined by the state where the agent chooses to Search despite"
[^c3]: openalex-org-w7127739895 — "an under-search error occurs when the agent chooses to Answer while 𝐾𝑡 remains"
[^c4]: openalex-org-w7127739895 — "A correct counterfactual answer implies that the agent’s knowledge state was indeed sufficient, whereas an incorrect answer"
[^c5]: openalex-org-w7127739895 — "the latent state is immediately inferred to be 𝐾𝑡 = Insufficient. No"
[^c6]: openalex-org-w7127739895 — "The rejected sequence (𝑦𝑟 ) is the agent’s original, factual trajectory that terminated prematurely with a low-quality answer."
[^c7]: openalex-org-w7127739895 — "we constructed a preference"
[^c8]: openalex-org-w7127739895 — "the model alleviates undersearch only to exacerbate over-search."
[^c9]: openalex-org-w7127739895 — "no agent achieves"
[^c10]: openalex-org-w7127739895 — "DAS effectively mitigates decision boundary errors by simultaneously lowering the"
[^c11]: openalex-org-w7127739895 — "These two signals function antagonistically; emphasizing"
