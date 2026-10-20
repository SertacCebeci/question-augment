---
description: "A reasoning trace helps a monitor only up to its conditional mutual information with the monitored attribute; practical monitors lose further to an information gap and an elicitation error."
aliases: ["chain-of-thought monitorability", "CoT monitorability uplift", "information gap and elicitation error"]
sources: ["arxiv-2602-18297"]
---
# CoT monitorability information bound

A monitor reads a reasoning trace Z (plus the prompt X) to predict an attribute Y of the output O. The paper defines the uplift as the accuracy of the Bayes-optimal trace monitor minus that of the Bayes-optimal prompt-only monitor, and proves it is non-negative and bounded by the conditional mutual information: 0 ≤ δ ≤ sqrt(2 I(Y; Z|X)).[^c1]

**Necessary, not sufficient.** Non-zero mutual information between trace and output, I(O; Z|X) > 0, is required for any uplift, but it does not guarantee one: an attribute can exist for which the trace gives none.[^c2] A trace can carry information for other reasons than being needed to solve the task, for example as a post-hoc explanation or as excerpts of the output. So "the task needs the trace" meets the necessary condition but proves nothing about monitoring.[^c3]

**Two practical errors.** A real monitor is not Bayes-optimal. Its accuracy loss is bounded by sqrt(2 ε_spec), and ε_spec splits into an information gap (the monitor's model of the agent's policy q versus the true policy π) plus an elicitation error (the monitor's approximation v of the output monitor g).[^c4] If the monitor is the agent's own policy, the information gap is zero by construction. The authors use this to explain why a model trained to write steganographic traces is best monitored by itself.[^c5]

**Uplift belongs to the policy.** Uplift is not a static property of the task: it is tied to the policy that generates the trace, so it need not transfer between policies. It is therefore trainable.[^c6] The paper trains for it with an oracle reward on monitor accuracy and with a label-free reward on conditional mutual information, and reports that both raise monitor accuracy and prevent trace degeneration when training against a monitor.[^c7]

## Limits

- The bound is an upper limit for the best possible monitor. It does not say a prompted LLM monitor attains it, and information encoded steganographically can resist extraction.[^c8]
- The paper itself notes that its mutual-information reward, if measured on the policy's own distribution, does not discourage obfuscation by steganography. It suggests measuring it with another LLM's distribution.[^c9]
- The accuracy bound uses a square root of mutual information, so it is loose for small values (my inference).
- Elicitation error is set aside as easier to fix by better monitor prompts, so it is not studied here.[^c10]
- Evidence is from the paper's own environments. Nothing here is about question asking, and the link to asking and answering is my inference: an answerer's stated reasoning is only a check on its answer to the extent it carries information about it.

## Related

- [[reasoning-faithfulness-observer-effect]] — exposing a trace to oversight changes the policy, the pressure this paper trains against
- [[hint-adherence-without-acknowledgement]] — a trace can omit what drove the answer, i.e. low information about the attribute
- [[capability-auditability-tradeoff]] — cost of requiring an inspectable trace

[^c1]: arxiv-2602-18297 — "Accuracy uplift δ in CoT monitorability of"
[^c2]: arxiv-2602-18297 — "(Not sufficiency) I(O; Z | X) > 0 does not guarantee"
[^c3]: arxiv-2602-18297 — "when CoT is a post-hoc explanation of the model output or"
[^c4]: arxiv-2602-18297 — "Proposition 3.13 (Decomposition of Misspecification Error)."
[^c5]: arxiv-2602-18297 — "the information gap is zero, and the misspecification error is"
[^c6]: arxiv-2602-18297 — "this means the uplift is a trainable attribute"
[^c7]: arxiv-2602-18297 — "preventing"
[^c8]: arxiv-2602-18297 — "does not"
[^c9]: arxiv-2602-18297 — "it does not disincentivize obfuscation via steganography."
[^c10]: arxiv-2602-18297 — "Elicitation error is generally"
