---
description: "Whether a response is safe depends on who receives it, so user-invariant safety evaluation can miss what personalization changes; a survey cites a 43.2% gain."
aliases: ["user-conditional safety", "relational safety", "user-invariant safety evaluation"]
sources: ["doi-10-48550-arxiv-2606-09038"]
---
# User-conditional safety

A standard safety framework treats acceptable model behaviour as the same for every user. The personalization survey argues that this assumption fails for personalized systems: safety there is "inherently user-conditional"[^c1], not a property fixed in advance, "rather than universally defined."[^c2] Its example is one response, such as guidance on medication dosage, detailed financial risk information, or emotionally charged content, which "may be appropriate for one user while posing potential harm to another"[^c3], depending on the user's background, situation or expertise.

The mechanism is a change in what gets judged. Under user-invariant evaluation the unit is the model's reply to a prompt. Under the user-conditional reading the unit is the pair of reply and recipient, so the same text can be acceptable or harmful depending on what the system knows about who is asking. Personalization is precisely the addition of that knowledge: the survey writes personalized generation as conditioned on the current query and on the user's representation and memory, "where x is the current user query."[^c4] In my reading, this is why the survey treats personalization as a safety lever in both directions. It reports that "incorporating personalized user context improves safety scores by 43.2%"[^c5], from "a large-scale evaluation across seven sensitive domains." It also reports the opposite side of the same gap: a study of twenty widely used LLMs found that "current models exhibit limited ability to adapt their safety behavior to individual user"[^c6] attributes.

Read together, the two findings describe a gap between information and use. Context can carry what a safe answer needs, but current models do not reliably use it. The survey names this as one of three structural inadequacies in the literature: "as user-invariant rather than relational"[^c7], meaning safety is scored per response and not per user.

## Limits

The 43.2% figure and the twenty-model result are cited from other papers. The survey does not run either experiment here, so the size of the effect is not established by this text, and the text does not say how the safety score was defined or which users and domains were used beyond the phrase "seven sensitive domains." The claim that safety is user-conditional is the survey's framing, argued from examples, not measured. The text gives no procedure for judging a response against a particular user's vulnerability.

Two limits are my inference, not the text's. First, a user-conditional standard assumes the user context is reliable, and the leakage risks of stored user information ([[personal-representation-leakage]]) make that a separate and costly problem. Second, a user-conditional standard makes every safety score depend on a user population, so an evaluation must now name the population it measured.

## Related

- [[user-driven-sycophancy]] — the survey places sycophancy among the risks of personalization: "preference-based personalization methods may reinforce sycophantic tendencies"[^c8]; a user's stated view pressing on the answer is the same concern seen from the user side.
- [[evidence-admission-gate]] — a per-item control on which retrieved context enters the model, one way to limit what user information a reply may use.
- [[personal-representation-leakage]] — the cost side: the stored user information that makes a reply suit its recipient is also what leaks.

[^c1]: doi-10-48550-arxiv-2606-09038 — "safety in personalized systems is inherently user-conditional"
[^c2]: doi-10-48550-arxiv-2606-09038 — "rather than universally defined"
[^c3]: doi-10-48550-arxiv-2606-09038 — "may be appropriate for one user while posing potential harm to another"
[^c4]: doi-10-48550-arxiv-2606-09038 — "where x is the current user query"
[^c5]: doi-10-48550-arxiv-2606-09038 — "incorporating personalized user context improves safety scores by 43.2%"
[^c6]: doi-10-48550-arxiv-2606-09038 — "current models exhibit limited ability to adapt their safety behavior to individual user"
[^c7]: doi-10-48550-arxiv-2606-09038 — "as user-invariant rather than relational"
[^c8]: doi-10-48550-arxiv-2606-09038 — "preference-based personalization methods may reinforce sycophantic tendencies"
