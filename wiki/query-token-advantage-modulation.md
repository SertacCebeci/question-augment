---
description: "A per-step search signal is added to the group advantage only on that step's query tokens, divided by query length, so credit follows the query rather than the whole trajectory."
aliases: ["per-token advantage modulation", "query-token credit", "step-scaled advantage on query tokens"]
sources: ["doi-10-48550-arxiv-2604-15148"]
---
# Query-token advantage modulation

> Instead of giving every token of a rollout the same group-relative advantage, a search step's score is written only onto the tokens of the query that produced it.

## Mechanism

In GRPO each trajectory o_i gets one scalar advantage from its group-normalized reward, and that advantage is shared by all its tokens. Liang et al. (2026) break this uniformity. Let Q_t be the token positions inside the search query of step t. The modulated advantage for a token at position p is the trajectory advantage plus a step term on query tokens only: for p in Q_t it is the trajectory advantage plus alpha times the processed step score divided by |Q_t|, and for every other position it is the trajectory advantage alone.[^c1] Here alpha is a weight (0.3 in the paper) and the step score is the counterfactual retrieval information gain described in [[counterfactual-retrieval-information-gain]].

The authors justify the restriction to query tokens by the premise that the step score "reflects the quality of the documents retrieved by the fixed retriever, which is determined by the search query".[^c2] Within one trajectory, steps with different scores therefore receive "different gradient signals proportional to their informational contribution", which is the stated route to learning "which query formulations are more effective".[^c3]

The division by |Q_t| is the part that matters most for design. It makes a step's total contribution equal alpha times its score, independent of how many tokens the query uses. The authors say this "is therefore decoupled from the query length, which is essential to prevent the reward-hacking behavior".[^c4] Without it, the policy can gain by writing longer queries: "since each query token receives the IG bonus, longer queries accumulate larger total bonuses when the IG is positive".[^c5]

The reason this helps when every rollout fails is structural. A group in which all rewards are equal gives a zero trajectory advantage, so the trajectory term vanishes. The step term does not depend on the answer being correct, so it can still be nonzero on query tokens. The authors argue that this is what lets the model learn from "the relative quality of different search steps across otherwise indistinguishable trajectories".[^c6] The same vanishing-gradient situation is discussed in [[zero-variance-group-waste]].

## Limits

- The claim that query-only modulation is the right restriction rests on the authors' argument from the retriever's role (quoted above). The slices read here do not include an ablation that modulates all tokens instead; that comparison is not checked.
- The statement that a step's total contribution equals alpha times its score depends on how the GRPO loss aggregates tokens across a rollout. The formula is the paper's; the loss implementation was not read, so the total-contribution claim is taken as written.
- The paper picks one alpha (0.3) for all experiments and reports a sensitivity analysis (RQ4) that was not read in this pass.
- Only search-augmented question answering with a fixed retriever was tested. Whether the same token-level credit transfers to other tool calls, to learned retrievers, or to non-query tokens inside a search step (such as the refinement text) is not examined; the last point is my inference from the design.
- The division by query length prevents one specific hack, longer queries; it does not address queries that are short but uninformative, which the step score itself must catch.

## Related

- [[counterfactual-retrieval-information-gain]] — the per-step score that this note writes onto query tokens
- [[signed-process-reward-stabilization]] — the dead zone, negative scaling and clipping applied to the score before it enters the advantage
- [[zero-variance-group-waste]] — the all-equal rollout groups that trajectory-level advantage cannot learn from
- [[competence-aware-credit-assignment]] — other ways of assigning credit across steps in an agent
- [[intermediate-query-quality-credit]] — per-query grading that is used to refine queries rather than to shape advantages

[^c1]: doi-10-48550-arxiv-2604-15148 — "modulating the advantage of query tokens based on the IG of the corresponding search step"
[^c2]: doi-10-48550-arxiv-2604-15148 — "the quality of the documents retrieved by the fixed retriever, which is determined by the search query"
[^c3]: doi-10-48550-arxiv-2604-15148 — "different gradient signals proportional to their informational contribution, enabling the model to learn"
[^c4]: doi-10-48550-arxiv-2604-15148 — "is therefore decoupled from the query length, which is essential to prevent the reward-hacking"
[^c5]: doi-10-48550-arxiv-2604-15148 — "unnecessarily long queries: since each query token receives the IG bonus, longer queries accumulate"
[^c6]: doi-10-48550-arxiv-2604-15148 — "the relative quality of different search steps across otherwise indistinguishable trajectories"
