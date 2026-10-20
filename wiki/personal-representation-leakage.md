---
description: "Personal information stored by a personalized LLM (profiles, personas, preference signals, memory) leaks in three ways: over-exposure, attribute inference, and persistence across sessions."
aliases: ["representation leakage", "personalization leakage", "user-representation leakage"]
sources: ["doi-10-48550-arxiv-2606-09038"]
---
# Personal representation leakage

Personalization works by keeping something about the user: a profile, a persona sentence, a preference embedding, a memory of past exchanges. The survey treats that stored thing as an attack surface. It groups the risks under one heading, "forms of representation leakage,"[^c1] which it defines as leakage that "arises when user information encoded in representations is exposed, inferred, or entangled beyond its intended use."[^c2] Read that definition as three distinct mechanisms, because each needs a different observer and a different defence.

*Over-exposure* is leakage through outputs or through analysis of internal representations. Structured profiles, preference embeddings and textual personas "often encode fine-grained attributes that can act as quasi-identifiers"[^c3], so an adversary can link a reply to external data and re-identify the user. The observer is whoever can read the output.

*Attribute inference* requires no disclosure at all. The sensitive trait sits in the representation without being stated there: "latent representations implicitly encode sensitive traits that are not explicitly disclosed."[^c4] The attacker infers it from model behaviour or response patterns, even when no direct identifier is present. The observer is whoever probes the behaviour. For preference signals the survey's table names this as "Sensitive attribute inference from inferred preferences."[^c5]

*Information persistence* is the time dimension. User-specific information "remains embedded in representations or memory structures over time"[^c6], which makes it hard to isolate or remove and lets it propagate across interactions. The memory case is the sharpest. The survey says long-term memory "is vulnerable to injection attacks that contaminate the memory store through seemingly benign interactions, with injected records persisting silently across sessions and activating on semantically related future queries."[^c7] Here persistence is a leakage route and an injection route at once: a stored record can surface later, to a different query, without the user having asked for it.

Retrieval-augmented personalization makes the same stored material reachable at inference time. "sensitive personal records stored in external memory are injected into model prompts"[^c8], where they can be exposed through unintended access or adversarial probing. Prompting-based personalization has a parallel problem: user information in hard or soft prompts is "vulnerable to membership inference attacks"[^c9], and sensitive information "becomes immediately accessible to the LLM and any third-party service during each interaction."[^c10]

The defences the survey lists trade against the personalization itself. Anonymizing hard prompts before sending them out, and differential privacy on prompts, are presented as mitigations. For the differential-privacy route the survey says plainly that "they often degrade personalization performance due to injected noise."[^c11] The protection and the personalization draw on the same budget.

## Limits

This is a taxonomy, and its mechanisms are described and attributed to other works ("[43, 86–90]" and similar). The text reports no measured leakage rates for the three mechanisms, and its table of attack surfaces is coarse and, in the survey's own words, "often overlapping." The three-way split is my organization of the survey's definition, not a split the survey defends as exhaustive. The text does not compare the defences it lists, and it leaves the privacy-utility trade-off as an "open challenge" without a number.

Two things are my inference. First, the observer-based reading (reader of outputs, prober of behaviour, later query) is a way to tell the mechanisms apart; the survey does not state it. Second, a control on what memory is admitted (see [[evidence-admission-gate]]) bears on the persistence and injection route, but the survey does not evaluate such a control, so its effect on leakage is not established here.

## Related

- [[user-conditional-safety]] — the same stored user information that lets a reply suit its recipient is the material this leakage exposes; the two notes are the benefit and the cost of one representation.
- [[evidence-admission-gate]] — gating which retrieved memory enters context, a candidate control on the injection and persistence route.

[^c1]: doi-10-48550-arxiv-2606-09038 — "forms of representation leakage"
[^c2]: doi-10-48550-arxiv-2606-09038 — "exposed, inferred, or entangled beyond its intended use"
[^c3]: doi-10-48550-arxiv-2606-09038 — "often encode fine-grained attributes that can act as quasi-identifiers"
[^c4]: doi-10-48550-arxiv-2606-09038 — "latent representations implicitly encode sensitive traits that are not explicitly disclosed"
[^c5]: doi-10-48550-arxiv-2606-09038 — "Sensitive attribute inference from inferred preferences"
[^c6]: doi-10-48550-arxiv-2606-09038 — "user-specific information remains embedded in representations or memory structures over time"
[^c7]: doi-10-48550-arxiv-2606-09038 — "with injected records persisting"
[^c8]: doi-10-48550-arxiv-2606-09038 — "sensitive personal records stored in external memory are injected into model prompts"
[^c9]: doi-10-48550-arxiv-2606-09038 — "vulnerable to membership inference attacks"
[^c10]: doi-10-48550-arxiv-2606-09038 — "immediately accessible to the LLM and any third-party service during each interaction"
[^c11]: doi-10-48550-arxiv-2606-09038 — "they often degrade personalization performance due to injected noise"
