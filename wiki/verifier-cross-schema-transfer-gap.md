---
description: "Fine-tuned text-to-SQL correctness verifiers reach 0.77-0.80 AUROC in-domain but drop to 0.66-0.67 on unseen schemas, a gap more data and scale do not close."
aliases: ["verifier transfer gap", "leave-one-database-out verifier gap"]
sources: ["richardson-2026"]
---
# Verifier cross-schema transfer gap

> A trained checker of "is this SQL correct" is only as good as the schemas
> it was trained on; nothing tried here — more data, more parameters, a
> stronger teacher — buys it a schema it has not seen.

## Definition / Mechanism

Richardson (2026) fine-tunes correctness verifiers
(a feature classifier, an encoder classifier, and LoRA-tuned generative
judges at two sizes) on 6,400 execution-labeled (question, schema, SQL) →
correct examples, then evaluates with leave-one-database-out (LODO):
"fine-tuning works in-distribution. The trained models reach approximately
0.77–0.80 auroc, and the 7B generative judge gives the best in-domain result
at 0.798... the same models transfer poorly. Across architectures and
scales, the trained verifiers land near 0.66–0.67 on unseen databases.
Scaling the generative judge from 1.5B to 7B improves the in-domain number
but does not improve LODO transfer." A large frozen judge (GPT-4o, never
fine-tuned) transfers better than any of the trained ones: "0.710" macro-LODO
versus 0.66-0.67.[^c1]

None of the levers tried close the gap: "the transfer gap is not closed by
the additional levers we tried. Adding Spider's schemas to increase training
diversity, distilling rationales from a strong judge, scaling the generative
verifier, and cross-benchmark training all leave transfer in roughly the
same band. The evidence is consistent with the fine-tuned models relying on
schema-specific surface regularities rather than learning a robust
cross-schema reasoning procedure." The paper's own reading: "Cross-schema
transfer appears to track model scale and reasoning rather than
fine-tuning."[^c2]

In-domain, the cheap trained verifier is still the better [[abstention]] tool:
"A feature classifier with no LLM call at inference gives a risk–coverage
frontier competitive with the frozen GPT-4o judge and far above
self-consistency. At a 20% risk target it answers 21% of questions,
compared with 9% for the frozen judge and 1% for self-consistency."[^c3]

## Why it matters

This names a concrete choice for a system that must decide who verifies an
answer (stall 4 as well as stall 2): a cheap, schema-specific verifier
trained on the deployment's own data is both more accurate and a cheaper
route to a usable abstention policy in-domain, but any system that must
handle a schema it has not trained on needs a large frozen reasoning judge,
not a bigger fine-tuned one — the two are not substitutes and the gap
between them is not currently closeable by more training.

## Limits

"Transfer" here is leave-one-database-out within one benchmark family
(relational schemas, SQL), not a shift to a different task; a domain shift
larger than "a new database" is untested. Ground truth is execution
correctness, unavailable in domains without an executable oracle, so the
finding does not obviously carry to open-ended answer verification.[^c4]

## Related

[[cross-provider-judge-ensemble]] · [[abstention]] · [[black-box-correctness-ceiling]]

[^c1]: richardson-2026
[^c2]: richardson-2026
[^c3]: richardson-2026
[^c4]: richardson-2026 — "The transfer evaluation uses leave-one-database-out (LODO): one database is held out, the verifier is trained on the remaining databases, and the held-out database is scored."
