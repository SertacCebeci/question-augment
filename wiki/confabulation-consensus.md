---
description: "Agents with shared error sources can agree on a wrong answer that outvotes a correct minority; counting then fails by construction, and adding agents does not fix correlated errors."
aliases: ["confabulation consensus", "correlated-error majority failure", "echo-chamber ensemble", "majority-wrong regime"]
sources: ["doi-10-48550-arxiv-2602-09341"]
---
# Confabulation consensus

A majority vote over agents treats each agent as one piece of evidence. That treatment is sound only when the agents' errors are independent. When they are not, the count can settle on an answer that several agents hold for the same reason, and a correct answer held by a minority is discarded. The auditing paper calls this *confabulation consensus*: agents "share correlated biases and converge on the same incorrect rationale."[^c1] The correlation comes from a shared substrate: agent errors "can be highly correlated due to shared pretraining, prompt anchoring, and interaction dynamics."[^c2]

The paper states the cost in variance. Let each of $N$ agents be correct with probability $p$, with average pairwise correlation $\rho$ between correctness indicators. The sample mean of those indicators then has variance $p(1-p)\,[1+(N-1)\rho]/N$. With $\rho = 0$ this falls as $1/N$ and the Condorcet picture holds. With $\rho$ bounded away from zero it tends to $p(1-p)\rho$ however many agents are added.[^c3] The paper's summary: "increasing the number of agents alone does not guarantee increasingly reliable majority decisions under persistent positive correlation."[^c3] Its gloss is an echo chamber: "a shared bias may simultaneously shift many agents toward the same incorrect answer," so a large $N$ can carry far fewer independent signals than its size suggests.[^c4]

The failure is sharpest on the majority-wrong slice. The paper's MinC set is the instances where the majority answer is wrong but a correct minority exists. On that set majority voting "deterministically achieves 0% on MinC by construction," because an increased multiplicity of an erroneous hypothesis cannot be voted away.[^c5] On the same slice the paper's AgentAuditor reaches "65.35% on GSM8K and 81.82% on AMC."[^c6]

The paper gives the same point as a toy proposition about a single decision. With more erroneous than correct supporters, majority voting "deterministically" returns the wrong answer. A branch-level discriminator that picks the correct branch with probability $q > 1/2$ does better than chance on exactly these cases.[^c7] The proposition is conditional on $q$, which is assumed, not measured.

**What transfers.** The Condorcet jury theorem comes from social choice, and the variance algebra from statistics. The algebra transfers intact: it says what a count is worth once a correlation is fixed. What does not transfer cleanly is the meaning of $\rho$. The paper reads it as a single latent bias that, when switched on, moves many agents to one wrong answer. That is a generative story the paper states rather than estimates from its runs.[^c8]

## Limits

- The variance result is for a homogeneous Bernoulli model with one average correlation. Real agents differ in accuracy and in how they correlate. In the sections read here the paper does not estimate $\rho$ for its own multi-agent runs (my reading).
- Proposition E.2 is a two-branch toy case. Its $q$ is a parameter, not a number from the experiments (my reading).
- The reported gains are measured on the majority-wrong slice, which is selected by the failure itself. The slice shows that the aggregator can recover such cases. It does not show how often real systems fall into them across all instances.
- The paper's own scope is narrow: "the method should not be expected to improve every instance or every multi-agent system."[^c9]
- The method has no evidence to work with in some cases: "structural auditing has little evidence with which to recover the answer."[^c10] That covers near-identical traces, shared wrong reasoning everywhere, and a candidate set without the correct answer.
- The phenomenon has older names in other fields (see Related). The term "confabulation" is the paper's own, and the note keeps it only as the paper's label.

## Related

- [[effective-independent-votes]] — the same $N_{\text{eff}}$ algebra, applied to LLM-judge panels where agreement and accuracy came apart
- [[coincident-failure]] — independently built software versions failing together is the same correlated-error structure in another field
- [[verification-weighted-voting]] — a tool-checked weight that breaks the frequency-driven loop which rewards frequent-but-wrong answers
- [[critical-divergence-point]] — the localisation the paper proposes as the remedy once whole-answer counting is set aside

[^c1]: doi-10-48550-arxiv-2602-09341 — "agents share correlated biases and converge on the same incorrect rationale"
[^c2]: doi-10-48550-arxiv-2602-09341 — "agent errors can be highly correlated due to shared pretraining, prompt anchoring, and interaction dynamics"
[^c3]: doi-10-48550-arxiv-2602-09341 — "increasing the number of agents alone does not guarantee increasingly reliable majority decisions under persistent positive correlation"
[^c4]: doi-10-48550-arxiv-2602-09341 — "a shared bias may simultaneously shift many agents toward the same incorrect answer"
[^c5]: doi-10-48550-arxiv-2602-09341 — "MV deterministically achieves 0% on MinC by construction"
[^c6]: doi-10-48550-arxiv-2602-09341 — "reaching 65.35% on GSM8K and 81.82% on AMC"
[^c7]: doi-10-48550-arxiv-2602-09341 — "Under perfect answer extraction, majority voting deterministically"
[^c8]: doi-10-48550-arxiv-2602-09341 — "one can view correlated errors as arising from a latent"
[^c9]: doi-10-48550-arxiv-2602-09341 — "the method should not be expected to improve every instance or every multi-agent system"
[^c10]: doi-10-48550-arxiv-2602-09341 — "structural auditing has little evidence with which to recover the answer"
