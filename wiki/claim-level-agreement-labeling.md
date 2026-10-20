---
description: "Each atomic claim of a final answer is tagged by how many independent candidate answers support or contradict it, any contradiction overriding support; the tag measures agreement, not truth."
aliases: ["claim-level consistency labeling", "inter-model agreement tags", "agreement-based claim verification"]
sources: ["arxiv-2601-00850"]
---
# Claim-level agreement labeling

A final answer is a bundle of propositions, and they do not all have the same support. The EdgeJury pipeline splits the chairman's answer into atomic claims, each "a single, verifiable proposition that can be judged independently of other statements".[^c1] A verifier then marks each earlier candidate answer as supporting, contradicting or irrelevant to each claim. The claim label follows a fixed precedence. Any contradiction makes the claim "contradicted". No contradiction and at least three supports make it "consistent". Anything else, including a 2–2 split, is "uncertain".[^c2]

The label is a tally, not a verdict. Its inputs are the candidates the generation stage wrote, which the paper draws from different model families and role prompts. So the label counts how many separately generated answers reach the same proposition. It does not change the answer: "it does not modify the final answer."[^c3] The paper describes what the tags are: they "indicate inter-model agreement, not external" support.[^c4] The authors call them "helpful indicators of internal agreement, not ground truth".[^c5]

The mechanism is a reading of an answer's support structure. That is a different object from the answer's correctness. A claim that every candidate shares is "consistent" whether or not it is true. The precedence rule is asymmetric: one dissenting candidate suffices for "contradicted", while "consistent" needs three of the four. That makes the label flag more claims than it confirms. The asymmetry is my reading of the rule, not a result the paper reports.

## Limits

- Shared error is invisible to the tag. The paper says it "cannot detect shared misconceptions if all candidates agree on the same falsehood"[^c6], and that "models share a misconception, EdgeJury may still be wrong".[^c7] The benchmark is built on misconceptions, so the case where a claim is most often "consistent" is also the case where the tag is least reliable. (my reading)
- Under-detection is a known failure: the stage "may under-detect support under heavy paraphrase, may miss implicit contradictions".[^c8] An "uncertain" can therefore be a paraphrase failure, not real doubt.
- Independence is assumed, not shown. In the paper's deployment, two of the four candidates are instances of one model family with different role prompts, alongside a 3B model and a Mistral 7B.[^c9] Agreement among related sources is weaker evidence than the count suggests, which is the subject of [[coincident-failure]].
- The threshold of three supports out of four, and the precedence, are design rules. The accuracy of the tags against human labels is reported in a later section that this pass did not read, so this note makes no accuracy claim for them.
- The verifier is itself a model. The paper implements the stage "as a single verifier model call with constrained JSON output".[^c10] Errors in extracting claims or in the per-candidate labels are not separated from the agreement label in the parts read. (my reading)
- The label is per claim, so an answer with many claims can carry many tags that are individually weak. How a reader should combine them is not addressed. (my reading)

## Related

- [[anonymized-cross-review]] — the stage before: the critiques the chairman uses to change the answer; this stage tags what that stage produced and changes nothing
- [[coincident-failure]] — why agreement among related sources is weak evidence of truth
- [[self-consistency-difficulty-score]] — a single-model answer-agreement signal, the nearest cousin of this count
- [[cross-provider-judge-ensemble]] — the same count-of-independent-verdicts idea applied to judges, with a measured gain

[^c1]: arxiv-2601-00850 — "a single, verifiable proposition that can be judged independently of other statements"
[^c2]: arxiv-2601-00850 — "any explicit contradiction overrides support"
[^c3]: arxiv-2601-00850 — "it does not modify the final answer"
[^c4]: arxiv-2601-00850 — "these tags indicate inter-model agreement, not external"
[^c5]: arxiv-2601-00850 — "helpful indicators of internal agreement, not ground truth"
[^c6]: arxiv-2601-00850 — "cannot detect shared misconceptions if all candidates agree on the same falsehood"
[^c7]: arxiv-2601-00850 — "models share a misconception, EdgeJury may still be wrong"
[^c8]: arxiv-2601-00850 — "may under-detect support under heavy paraphrase, may miss implicit contradictions"
[^c9]: arxiv-2601-00850 — "we use two instances of LLaMA-3.1-8B (different role prompts), one LLaMA-3.2-3B, and"
[^c10]: arxiv-2601-00850 — "Stage 4 is implemented as a single verifier model call with constrained JSON output"
