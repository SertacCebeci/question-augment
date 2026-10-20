---
description: "Sufficiency judged by first naming what is missing, then searching the context for that claim: a gap the text contains is refuted, so the context was sufficient after all."
aliases: ["Identify-then-Verify", "attribution verification", "consensus gap claim verification", "gap claim attribution"]
sources: ["arxiv-2512-06476"]
---
# Gap-claim attribution check

The paper changes what a sufficiency judgment is about. Asked a binary question, a model answers "sufficient" or "insufficient" with no checkable reason attached. The paper reformulates the task as a generative one: "What specific information is missing?" The answer becomes a claim the model has to commit to, and the authors say this "forces the model to produce a falsifiable claim".[^c1][^c2]

The check is a second, separate step. The consensus claim of missing information is passed to a second call with "a focused and less ambiguous task": verify whether the claimed information "is, in fact, absent from the source passage(s)."[^c3][^c4] The decision then runs in the direction that is easy to get backwards. "If the verifier finds the claimed missing information in the context, we classify the context as Sufficient; otherwise, Insufficient."[^c5] A gap that the text contains is refuted by the text, and the context counts as sufficient.

The reason for the second call is the failure the paper names. Asking for missing information "may not suffice, as the model may hallucinate non-existent gaps."[^c6] Decoupling identification from verification means "we prevent the model from finalizing a decision based on a hallucinated or misremembered information gap."[^c7] The paper reports the step's effect as relative error reduction, the share of the consensus's errors that verification corrects, "as high as 37%."[^c8]

The mechanism transfers at the level of shape. A gap is a claim about a text, and a claim about a text can be checked against that text, which is cheaper than trusting the first pass. That is different from [[reverse-prerequisite-gap-detection]], where the gap is found by a backward search over what a question's answer requires, inside one reasoning pass, with no second call to test a flagged gap. It is closer to [[evidence-verified-identification]], where a candidate is replayed against the evidence before it is trusted.

## Limits

- The verifier is an LLM doing a presence test, and it is lenient on purpose. It accepts "paraphrasing, and reasonable inferences as valid" as evidence that the claimed information is present.[^c9] A lenient verifier passes inferred answers, which is the error the paper finds on SQuAD v2 and FaithEval, where the pragmatic setting does worst.[^c10] See [[sufficiency-criterion-strictness]].
- The negatives are built by deletion. For the multi-hop sets, insufficient items are made by "the designated supporting passages from the context" being removed.[^c11] Real insufficiency seldom arrives as a clean removal, and the authors concede that real questions "are inherently open-ended and inferential, requiring models" to work with incomplete contexts.[^c12]
- The sections read report the pipeline's accuracy and the relative error reduction of verification. They do not report the verifier's false presences and false absences separately, so the check's own error rate is not measured here.
- The check tests presence in the passages. A gap that is real but worded in a way the verifier does not find comes back as insufficient, which is an error in the other direction (my inference).
- The identifier and the verifier were different models in the paper's main setup (Llama-3.1-8B and GPT-4o). Whether one model checking its own claims behaves the same is not tested in the text read.

## Related

- semantic-medoid-consensus — the aggregation step that produces the claim this check tests
- [[structured-gap-sufficiency-judge]] — a binary decision with a gap schema for the next query, with no second check on the gap
- [[reverse-prerequisite-gap-detection]] — gaps found by backward search over a question's requirements, with no separate verification call
- [[evidence-verified-identification]] — replays a candidate constraint against the source before trusting it
- [[evidence-insufficiency-regimes]] — how evidence can fall short, the kinds of gap a check like this has to catch

[^c1]: arxiv-2512-06476 — "What specific information is missing?"
[^c2]: arxiv-2512-06476 — "forces the model to produce a falsifiable"
[^c3]: arxiv-2512-06476 — "a focused and less ambiguous task"
[^c4]: arxiv-2512-06476 — "is, in fact, absent from the source passage(s)."
[^c5]: arxiv-2512-06476 — "missing information in the context, we classify the"
[^c6]: arxiv-2512-06476 — "the model may hallucinate non-existent gaps."
[^c7]: arxiv-2512-06476 — "the model from finalizing a decision based on a"
[^c8]: arxiv-2512-06476 — "gains as high as 37%."
[^c9]: arxiv-2512-06476 — "paraphrasing, and reasonable inferences as valid"
[^c10]: arxiv-2512-06476 — "while our method performs substantially poorly."
[^c11]: arxiv-2512-06476 — "the designated supporting passages from the context."
[^c12]: arxiv-2512-06476 — "are inherently open-ended and inferential, requiring models"
