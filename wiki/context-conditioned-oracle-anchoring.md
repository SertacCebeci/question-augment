---
description: "Handing a stronger model a weaker ensemble's reasoning lifts it when that reasoning is right (up to +19.2pp) and drags it down when wrong (up to -18.0pp), so context must be gated by confidence."
aliases: ["context poisoning in hierarchical MoA", "SLM-context anchoring", "anchoring in context-aware escalation"]
sources: ["arxiv-2602-19509"]
---
# Context-conditioned oracle anchoring

When a query is escalated from a cheap ensemble to a stronger "Oracle" model, the Oracle can either answer alone (routing-based) or receive the cheap models' chain-of-thought and answers with instructions to review, reconcile and correct them (context-aware). Khaled tested the second on four benchmarks, splitting escalated queries by whether the small-model majority answer was correct.[^c1]

## What was measured

When the small-model majority was correct, context raised Oracle accuracy by +0.5 to +19.2pp. When it was wrong, context lowered Oracle accuracy by 14.9 to 18.0pp on three of four benchmarks.[^c1] On MATH 500 the same pair is +19.2pp versus -18.0pp (59.0% to 41.0%).[^c2] GSM8K's positive side is only +0.5pp because the Oracle is already at 99.0% on majority-correct items; the negative side stays at -14.9pp.[^c1] So the context acts as an anchor: the effect's sign follows the correctness of the context, not the Oracle's own ability, and the Oracle "cannot reliably discount incorrect SLM reasoning, even when the capability gap is substantial."[^c3]

The author likens it to retrieval-augmented generation, where wrong retrieved documents make the model commit to plausible-but-wrong reasoning instead of solving independently.[^c4]

## Consequence for routing

Because the downside is as large as the upside, the author argues routing-based design is a safeguard, not only a cost saving, and proposes a ternary decision: retain at Layer 1 (high confidence), escalate with context (medium confidence), escalate without context (low confidence). This needs two thresholds.[^c3] That proposal is untested here; the claim that such a system would exceed the Oracle baseline is the author's projection from the split data. The ternary rule is a hypothesis, not a result.

## Limits

- HumanEval shows no effect on the majority-wrong subset; the author guesses test execution gives an objective signal that resists anchoring, which is not tested.[^c1]
- One Oracle family (Llama-3.3-70B) and three small models; whether stronger or reasoning-trained Oracles resist anchoring is untested.
- Splits condition on the majority being correct, which is known only post hoc; a real router sees only a confidence estimate, so realized gains depend on router precision.
- Only one instruction style ("review, reconcile, correct") was used; prompts telling the Oracle to distrust candidates were not compared.
- The RAG parallel is the author's analogy, not a measurement.

## Related

- [[implicit-escalation-threshold]] — the single-threshold escalation decision this adds a second axis to
- [[uncertainty-aware-router]] — routing on uncertainty, the router role here
- [[self-repair-anchoring]] — the same anchoring on prior wrong output, in self-repair
- [[diagnostic-anchoring-in-agentic-llms]] — anchoring on earlier context in LLM agents
- [[context-fidelity-boosting]] — controlling how much the model leans on supplied context

[^c1]: arxiv-2602-19509 — "When the SLM majority is wrong, context degrades Oracle accuracy by"
[^c2]: arxiv-2602-19509 — "context degrades Oracle performance by −18.0pp (59.0% → 41.0%)"
[^c3]: arxiv-2602-19509 — "the Oracle cannot reliably discount incorrect SLM reasoning, even when the capability gap is substantial"
[^c4]: arxiv-2602-19509 — "passing incorrect retrieved documents to an LLM can cause"
