---
description: "Epistemic bias is a shift in the stance of retrieved context, not in its truth; factually correct but one-sided passages can move an LLM answer's stance."
aliases: ["epistemic bias in retrieved context", "retrieval stance shift", "stance propagation from retrieval to answer"]
sources: ["arxiv-2512-00804"]
---
# Epistemic bias propagation

Retrieval-augmented answering inherits the stance of what it retrieves. Wu and Saxena define epistemic bias as the shift in average polarization score caused by an added set of passages, applied to both the retrieved set and the final response.[^c1] The score that makes this shift measurable is the one in [[polarization-score]].

The mechanism concerns what gets retrieved, not whether it is true. Earlier work on context manipulation mainly injected false or toxic content, which "can often be detected by fact-checking or" linguistic analysis.[^c2] A set of passages that is factually correct but systematically one-sided is a different case. The paper's claim is that such adversarial passages "effectively crowd out" alternative viewpoints at retrieval time, so the top-k set shifts toward one stance.[^c3] The answer then follows the set: the paper reports that across open-ended questions the retrieval-side shift and the response-side shift are rank-correlated, and that "epistemic bias can be effectively propagated through different LLMs" to responses.[^c4]

The effect bears on how open questions get answered. The paper's premise is that for many open-ended questions "there is no single objectively correct" answer, so there is no ground truth a fact-checker can enforce, and the stance of the evidence set is what moves the answer.[^c5] My inference from this: an answerer that reads only the top-k of a retrieved set has no view of the stance spread it was not shown, so a skewed set looks like a balanced one from inside the answer.

## Limits

- The evidence is a rank correlation across 452 open-ended, controversial questions drawn from WIKI-BALANCE, computed over several LLMs. It is a correlation across topics, not a per-answer effect size.[^c6]
- The paper's own discussion says the effect depends on topic openness: "This suggests a natural boundary" of applicability, because on topics with "strong factual consensus" it becomes harder to write accurate passages that deviate from the mainstream.[^c7] The bias is weaker where the question is closed.
- The bias is defined relative to the clean retrieval distribution, not to a neutral standpoint. The paper says its definition "makes no reference to an externally defined" neutral position, so it measures a redistribution of stance, not the distance from a correct answer.[^c8]
- The paper also states a structural tension for its attack setting: "This tension is not merely practical but" follows from the geometry, so a stronger stance push is easier to detect.[^c9] That claim is made under the paper's threat model and was not tested against other retrievers in the part I read.
- Whether the propagation holds for answerers that cite or weigh sources differently, or for retrieval with stance-aware reranking, is not established here.

## Related

- [[polarization-score]] — the scalar whose change across a retrieved set is the measure of this bias.
- [[answer-format-dependent-bias-measurement]] — another case where a measured bias depends on the conditions of the question, here the answer format rather than the evidence.
- [[answer-evidence-embedding-similarity]] — grounding of an answer in its evidence is a different property; a stance-skewed answer can be well grounded in a skewed set (my inference).

[^c1]: arxiv-2512-00804 — "LLM response is denoted by the shift in their (average) PS"
[^c2]: arxiv-2512-00804 — "toxic content, which can often be detected by fact-checking or"
[^c3]: arxiv-2512-00804 — "such adversarial passages effectively crowd out"
[^c4]: arxiv-2512-00804 — "epistemic bias can be effectively propagated through different LLMs"
[^c5]: arxiv-2512-00804 — "there is no single objectively correct"
[^c6]: arxiv-2512-00804 — "containing 452 open-ended, controversial questions across diverse topics"
[^c7]: arxiv-2512-00804 — "This suggests a natural boundary"
[^c8]: arxiv-2512-00804 — "makes no reference to an externally defined"
[^c9]: arxiv-2512-00804 — "This tension is not merely practical but"
