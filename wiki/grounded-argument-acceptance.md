---
description: "Whether a claim stands is settled by the whole attack graph: under grounded semantics a claim stands when its attackers are themselves defeated, and the verdict is unique."
aliases: ["grounded semantics", "Dung acceptability", "argument acceptability", "justified status under attack"]
sources: ["doi-10-48550-arxiv-2609-38409"]
---
# Grounded argument acceptance

A set of arguments and an attack relation between them is enough to ask which arguments survive. The ArgGYM paper takes this framing from Dung, who "established a fundamental connection between argumentation and non-monotonic reasoning, showing how forms of non-monotonic inference can be understood in terms of arguments, attacks, and acceptability."[^c1] On this reading a claim is not accepted because it has a good argument for it. Whether it is accepted is a verdict on the whole attack structure: "argumentation semantics determine which arguments, and consequently which conclusions, are accepted."[^c2]

The semantics used for nearly every task in the benchmark is grounded: "All tasks except semantics_query use grounded semantics, which has a unique extension."[^c3] Uniqueness is what lets the engine give one status per claim for each instance, so a task can ask for that status directly. The tasks name the statuses. One constructive task asks the model to "Modify the theory so that a justified target becomes overruled."[^c4]

The mechanism, as I read the grounded definition (my inference: the paper gives the status names and the engine, not the fixed-point procedure): an argument stands when every attacker of it is itself defeated by an argument that stands, and the extension is the least set closed under that rule. So an attack on a claim matters only if the attacker survives, and the survival of the attacker depends on the attackers it faces. The paper's discussion makes the same point at the level of the whole answer. "Correctly identifying individual supports, attacks, statuses, or defeaters is not sufficient when the required answer depends on their joint consequences."[^c5] It adds that "Attacks can be defeated, preferences can determine whether an attack succeeds, and changes to one part of a theory can propagate through multiple support and defeat relations."[^c6]

What transfers to asking and answering is a difference in the question. "Is there an argument for this claim?" needs one support chain. "Is this claim justified?" needs the status of every counterargument, and each counterargument's status depends on its own counters. (My inference: the paper measures status queries, not how people or models phrase them.)

## Limits

- The benchmark uses one semantics for almost all tasks. The paper says its choice "provides a consistent executable foundation, but it does not establish whether the same findings would hold more broadly across alternative argumentation semantics."[^c7] Other semantics could give other verdicts on the same graph; none was tested.
- The verdicts are the engine's, and the engine is hidden from the model: "The symbolic engine is used for generation and verification and is not available to the model during inference."[^c8] Grounded acceptance is therefore the scoring definition. The paper does not check it against human judgments of which arguments are defended.
- The note covers only how the attack structure decides which conclusions survive. It says nothing about whether a premise is true. The paper's own gloss is that conclusions are "warranted given the available information", which is a separate question from acceptance.
- The formal attack types (undermining, rebutting, undercutting) and the preference step that decides whether an attack succeeds are taken as given here. Which attacks count as defeats is the subject of [[preference-sensitive-defeat]].

## Related

- [[argumentative-consequence]] — another inconsistency-tolerant relation, defined on consistent sub-bases rather than on an attack graph
- [[truth-maintenance-system]] — keeps a belief set in line with its recorded reasons; its justification graph does a job similar to the attack graph here
- [[preference-sensitive-defeat]] — which attacks succeed as defeats, the input this note takes as given
- [[local-correctness-without-global-composition]] — the measured gap between correct local verdicts and a correct whole-state answer

[^c1]: doi-10-48550-arxiv-2609-38409 — "established a fundamental connection between argumentation and non-monotonic reasoning"
[^c2]: doi-10-48550-arxiv-2609-38409 — "argumentation semantics determine which arguments, and consequently which conclusions, are accepted"
[^c3]: doi-10-48550-arxiv-2609-38409 — "All tasks except semantics_query use grounded semantics, which has a unique extension."
[^c4]: doi-10-48550-arxiv-2609-38409 — "Modify the theory so that a justified target becomes overruled"
[^c5]: doi-10-48550-arxiv-2609-38409 — "Correctly identifying individual supports, attacks, statuses, or defeaters is not sufficient when the required answer depends on their joint consequences"
[^c6]: doi-10-48550-arxiv-2609-38409 — "Attacks can be defeated, preferences can determine whether an attack succeeds, and changes to one part of a theory can propagate through multiple support and defeat relations"
[^c7]: doi-10-48550-arxiv-2609-38409 — "it does not establish whether the same findings would hold more broadly across alternative argumentation semantics"
[^c8]: doi-10-48550-arxiv-2609-38409 — "The symbolic engine is used for generation and verification and is not available to the model during inference"
