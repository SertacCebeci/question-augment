---
description: "An attack becomes a defeat only if the attacked argument is not preferred to its attacker, so the ordering used to compare arguments decides which conflicts change the answer."
aliases: ["preference-based defeat", "weakest-link and last-link orderings", "defeat by preference", "ASPIC+ argument preference"]
sources: ["doi-10-48550-arxiv-2609-38409"]
---
# Preference-sensitive defeat

A conflict between two arguments is not yet a defeat. In the structured-argumentation framework the paper uses, arguments are built from premises and rules, "conflicts give rise to attacks, preferences determine whether preference-sensitive attacks succeed as defeats, and argumentation semantics determine which arguments, and consequently which conclusions, are accepted."[^p1] The step in the middle is the one this note is about: an attack exists whenever the conflict does, but whether it removes the attacked argument depends on a preference between the two.

The benchmark does not fix one preference. It "crosses two argument preference orderings, last-link and weakest-link, with two set orderings, elitist and democratic, yielding four preference configurations."[^p2] The two argument orderings compare arguments in different places. Under last-link, comparison "can depend primarily on the final defeasible steps of an argument", while weakest-link "can make preference information distributed across premises and defeasible rules relevant to the comparison."[^p3] So the same pair of arguments can stand in a defeat relation under one ordering and not under the other. (My inference from the definition: the answer to "does this attack succeed?" is only well-posed once the ordering is named.)

The measured effect is an aggregate difference between orderings. "Many configurations perform markedly better under last-link than weakest-link."[^p4] One model is the example: "Gemini 3.8 Flash at high effort scores 92.9% versus 71.8%."[^p5] The direction is not uniform across tasks. "DeepSeek-v4.1-Flash, for example, performs better under weakest-link on claim_chain" and on defeat_diagnosis. The paper's own reading of the aggregate is that "The resulting pattern is consistent with a greater burden on maintaining and combining preference-relevant state under some weakest-link instances."[^p6] That is an interpretation, not a tested mechanism.

What this changes for asking and answering: a question about whether a claim has been defeated carries a hidden parameter, the ordering that decides which attacks count. An answer that does not state it can be right under one ordering and wrong under the other. The paper's results suggest that models handle the two orderings unevenly, though it does not show that a question which names the ordering is answered better.

## Limits

- The orderings are not compared on matched theories. "Because these ordering cells are generated independently, the benchmark-wide comparison is descriptive rather than a causal effect of changing the ordering on a fixed theory."[^p7] The paper says that "last-link and weakest-link instances are generated independently rather than as matched versions of the same underlying theory."[^p8]
- Weakest-link is not a harder version of last-link, by the paper's own reading: "Weakest-link should therefore not be interpreted as uniformly harder."[^p9] The per-task reversals are the reason.
- The ordering effect is confounded with structure. "Curriculum configurations can vary several structural properties at once."[^p10] A difference between orderings may partly be a difference in the theories each ordering tends to produce.
- The note concerns the defeat step only. Whether a defeat changes the status of a claim is the acceptance step, treated in [[grounded-argument-acceptance]].

## Related

- [[grounded-argument-acceptance]] — the acceptance step that takes these defeats as its input
- [[truth-maintenance-system]] — its culprit choice needs an external ordering that the network does not supply, which is the same missing piece in another setting
- [[argumentative-consequence]] — works on a base with no priorities at all, so the choice of which attacks succeed never arises

[^p1]: doi-10-48550-arxiv-2609-38409 — "conflicts give rise to attacks, preferences determine whether preference-sensitive attacks succeed as defeats"
[^p2]: doi-10-48550-arxiv-2609-38409 — "crosses two argument preference orderings, last-link and weakest-link, with two set orderings"
[^p3]: doi-10-48550-arxiv-2609-38409 — "weakest-link can make preference information distributed across premises and defeasible rules relevant to the comparison"
[^p4]: doi-10-48550-arxiv-2609-38409 — "Many configurations perform markedly better under last-link than weakest-link"
[^p5]: doi-10-48550-arxiv-2609-38409 — "Gemini 3.8 Flash at high effort scores 92.9% versus 71.8%"
[^p6]: doi-10-48550-arxiv-2609-38409 — "The resulting pattern is consistent with a greater burden on maintaining and combining preference-relevant state under some weakest-link instances"
[^p7]: doi-10-48550-arxiv-2609-38409 — "the benchmark-wide comparison is descriptive rather than a causal effect of changing the ordering on a fixed theory"
[^p8]: doi-10-48550-arxiv-2609-38409 — "last-link and weakest-link instances are generated independently rather than as matched versions of the same underlying theory"
[^p9]: doi-10-48550-arxiv-2609-38409 — "Weakest-link should therefore not be interpreted as uniformly harder."
[^p10]: doi-10-48550-arxiv-2609-38409 — "Curriculum configurations can vary several structural properties at once"
