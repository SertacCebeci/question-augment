---
description: "In multi-hop answering a wrong binding at one hop becomes the next search query, so later evidence is gathered around the wrong entity and the chain can look self-consistent."
aliases: ["cascade amplification of binding errors", "multi-hop error cascade"]
sources: ["doi-10-48550-arxiv-2607-17535"]
---
# Binding-error cascade

A multi-hop answer is a chain of bindings. The entity chosen at one hop sets the query for the next, and the source states the dependency directly: "each hop conditions the next retrieval query on the entity selected at the previous hop."[^e1] A binding error is therefore not local. Once the chain has picked a wrong entity, the later searches are aimed at that entity, and the evidence they return can be true of it.

The source's account of what follows is that downstream steps do not repair the mistake: "Downstream hops are unlikely to correct the error; instead, they often construct a self-consistent chain around" the wrong entity, with every cited fact true about some entity in the corpus.[^e2] This is the property that makes the final answer hard to audit from its citations. Each step checks out, and the chain as a whole is wrong.

The source gives a simple arithmetic for the chain. If each hop is corrupted independently with probability p_i, the chain is corrupted with probability one minus the product of the per-hop success probabilities. Its example is a three-hop chain at per-hop 0.3, which it reports as corrupted with probability of about 66%, "more than twice the per-hop rate."[^e3] The label the source gives this case is "Independent hop-level opportunities."[^e4] Under that assumption, the chain is less reliable than its weakest step by a multiplicative amount, not by the weakest step alone.

For an attacker the consequence is that one flipped hop is enough: "The attacker needs only to flip the weakest hop; the cascade handles the" remainder.[^e5] My inference, not the source's: the same arithmetic reads from the answerer's side as a reason to check the binding at each hop, not the final answer, since the final answer is where the error has already been amplified.

How the source measures this. Its outcome is the final answer, and it treats the answer as evidence of propagation rather than as the event itself: "Final-answer flips are downstream evidence of" propagation, and the event it tracks is the first post-exposure binding error.[^e6] Its benchmark uses chains of fixed length: "Each sample is a three-hop entity chain."[^e7] The summary claim is that "binding can corrupt the downstream chain, making Multi-Hop" agents especially exposed.[^e8]

## Limits

- The 66 % figure is an illustration with an assumed per-hop rate of 0.3, not a rate the source measured.
- The independence in the product formula is an assumption. Errors that share a document, a decoy, or a retrieval query are correlated, and under correlation the chain-level rate differs from the product. The source does not estimate per-hop rates in the parts I read.
- The claim that downstream hops rarely correct the error is asserted in the section on the cascade. The source frames a test of whether "a single salience flip is sufficient to trigger cascade amplification"[^e9], and I did not check the results for that test.
- Every chain in the source is three hops, and the cascade is measured only under adversarial edits to documents. Whether benign binding errors cascade the same way is not shown here.
- The source's cascade is about a single binding step being wrong. It does not show that a wrong step is more likely to be followed by another wrong step than an independent draw would be.

## Related

- [[salience-relevance-decoupling]] — the mechanism that produces the first wrong binding in the source's account
- [[knowledge-overshadowing]] — a dominant condition makes the next query drift, the same carry-over from one step to the next
- [[misleading-grounding-propagation]] — a wrong localization carried into the rationale, a parallel propagation in a different pipeline
- [[implicit-subject-resolution-injection]] — multi-hop failure located at resolving an unnamed subject, which is the binding step
- [[evidence-forgetting-rate]] — wrong multi-hop answers despite retrieved golden evidence, measured apart from the binding path

[^e1]: doi-10-48550-arxiv-2607-17535 — "each hop conditions the next retrieval query on the entity selected at the previous hop."
[^e2]: doi-10-48550-arxiv-2607-17535 — "Downstream hops are unlikely to correct the error; instead, they often construct a self-consistent chain around"
[^e3]: doi-10-48550-arxiv-2607-17535 — "more than twice the per-hop rate."
[^e4]: doi-10-48550-arxiv-2607-17535 — "Independent hop-level opportunities."
[^e5]: doi-10-48550-arxiv-2607-17535 — "The attacker needs only to flip the weakest hop; the cascade handles the"
[^e6]: doi-10-48550-arxiv-2607-17535 — "Final-answer flips are downstream evidence of"
[^e7]: doi-10-48550-arxiv-2607-17535 — "Each sample is a three-hop entity chain"
[^e8]: doi-10-48550-arxiv-2607-17535 — "binding can corrupt the downstream chain, making Multi-Hop"
[^e9]: doi-10-48550-arxiv-2607-17535 — "test whether a single salience flip is sufficient to trigger cascade amplification"
