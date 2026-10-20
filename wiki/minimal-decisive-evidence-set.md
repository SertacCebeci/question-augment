---
description: "A self-verifying agent submits a short index-selected list of its own action-observation pairs as the only input to the judge, trading verifier cost and hallucination against missed proof."
aliases: ["curated evidence set", "minimal evidence set", "evidence curation for verifier", "proof submission", "snapshot evidence"]
sources: ["arxiv-2512-22322"]
---
# Minimal decisive evidence set

A finished task is usually judged after the fact by a verifier that reads the whole trajectory: every tool call and every screenshot. The verifier then carries the full history, which is long, expensive, and open to hallucinated or false-positive judgments. SmartSnap changes what the verifier is given. When the agent claims completion, it returns a list of integer indices E pointing into its own history, and the selected pairs are concatenated as the sole material for a general LLM-as-a-Judge. The paper states this directly: "the agent learns to output a set of integer indices E."[^c1] Each indexed item is an *exhibit*, an atomic pair of the action taken and the observation it produced, described as "an objective, unalterable fact rather than the"[^c2] agent's own summary. The selection, not the prose, is what the agent learns.

The stated aim is to shrink the verifier's input "to a minimal, curated evidence set," which the authors frame as "fundamentally resolving the trade-off between verification cost and reliability."[^c3]

The two-sided objective is the core of the mechanism. The paper reads its Completeness and Conciseness principles as a pair of verifier error rates. "From a statistical perspective, the goal is to maximize the"[^c4] true positive rate of the verifier, so that a correct run is not rejected for missing proof. Conciseness is read as the lever on the other error: "Conversely, the Conciseness principle is crucial for minimizing the"[^c5] false positive rate. Two reasons are given for brevity: "a shorter, more information-dense submission reduces its cognitive load and the"[^c6] likelihood of hallucination, and "long inputs for the verifier mitigates the risk of context rot."[^c7]

Why completeness has teeth is the verifier's rule that absence counts as absence. The grading stage assumes that "What is not shown in the evidence is assumed not to have happened."[^c8] A correct run whose key step is left out is therefore marked wrong, "penalized due to incomplete evidence."[^c9] Submission must therefore happen while the state still exists. The paper's argument for moving verification inside the episode is that the agent has "position within the live environment sandbox (that is often destroyed or unavailable by the time of post-hoc"[^c10] verification.

The set is also used as a training signal. The reward combines a binary completeness outcome with a conciseness term: "we include a penalty term proportional to the size of the"[^c11] evidence, with a small coefficient. The reported effect is on task success: the abstract gives gains "bringing performance gains up to 26.08% and 16.66% respectively to 8B and 30B models."[^c12]

## Limits

- The sections read report no run that switches off the curation step while holding the rest of the pipeline fixed. The comparisons are against prompting, against fine-tuning on the vanilla Android Instruct data, and against RL. The fine-tuning comparison keeps "the same 726 tasks" but not the form of the supervision, so it does not isolate the evidence set.
- The reading of the 3C principles as true-positive and false-positive control is the paper's framing, not a result. It calls the principles "a theoretical foundation for training self-verifying agents,"[^c15] but the text gives no bound or proof connecting E's size to either error rate. That link is my inference.
- Everything is tested on one benchmark. The authors say "The current experiments are limited to one benchmark due to the resource-intensive nature of RL"[^c13] in sandboxed environments. The atomic action-observation exhibit fits GUI tool calls; whether it fits reasoning or coding traces, where the observation is not a screen, is untested.
- The success numbers are scored differently from the training reward. The reported evaluation uses a judge that "analyzes all the interaction trajectories"[^c14] rather than the submitted evidence. The gain is therefore measured by a verifier that sees more than the agent's proof.
- A concise set can be honest and still misleading if the exhibits chosen are true but unrepresentative. The paper does not measure that case. This is my inference.

## Related

- [[evidence-oriented-action]] — how the set is built when the history lacks the exhibit a judge needs
- [[llm-judge-validation-gap]] — the judge whose input this note shrinks; the gap between judge and truth is untouched by shrinking alone
- [[pessimistic-min-judge-aggregation]] — another way to make a judge's reward reliable, by requiring agreement rather than by curating input
- [[process-outcome-consistency-verification]] — a verifier that checks derivation against outcome, a check on the same claim from the other side
- [[same-model-self-verification-conditional-confidence]] — a different "self-verification": a same-model confidence check, not the agent submitting its own proof

[^c1]: arxiv-2512-22322 — "the agent learns to output a set of integer indices E."
[^c2]: arxiv-2512-22322 — "an objective, unalterable fact rather than the"
[^c3]: arxiv-2512-22322 — "fundamentally resolving the trade-off between verification cost and reliability."
[^c4]: arxiv-2512-22322 — "From a statistical perspective, the goal is to maximize the"
[^c5]: arxiv-2512-22322 — "Conversely, the Conciseness principle is crucial for minimizing the"
[^c6]: arxiv-2512-22322 — "a shorter, more information-dense submission reduces its cognitive load and the"
[^c7]: arxiv-2512-22322 — "long inputs for the verifier mitigates the risk of context rot"
[^c8]: arxiv-2512-22322 — "What is not shown in the evidence is assumed not to have happened."
[^c9]: arxiv-2512-22322 — "penalized due to incomplete evidence."
[^c10]: arxiv-2512-22322 — "position within the live environment sandbox (that is often destroyed or unavailable by the time of post-hoc"
[^c11]: arxiv-2512-22322 — "we include a penalty term proportional to the size of the"
[^c12]: arxiv-2512-22322 — "bringing performance gains up to 26.08% and 16.66% respectively to 8B and 30B models."
[^c13]: arxiv-2512-22322 — "The current experiments are limited to one benchmark due to the resource-intensive nature of RL"
[^c14]: arxiv-2512-22322 — "It analyzes all the interaction trajectories (e.g., traces and"
[^c15]: arxiv-2512-22322 — "a theoretical foundation for training self-verifying agents."
