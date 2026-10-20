---
description: "An LLM's knowledge boundary is three nested sets (universal, parametric, outward), and their differences give four knowledge types, from prompt-agnostic known to model-agnostic unknown."
aliases: ["LLM knowledge boundary", "knowledge boundary of LLMs"]
sources: ["doi-10-48550-arxiv-2412-12472"]
---
# LLM knowledge boundary

The knowledge boundary of a language model is the line between what the model can be shown to know and what it cannot. The survey that formalizes it states its aim as "a comprehensive and formalized definition of the knowledge boundary of LLMs",[^c1] because the earlier Know-Unknow framing "is conceptual and lacks formalization".[^c2] The line matters for asking because a model's behaviour past it differs: it can be overconfident there, and a question that falls beyond it needs a different treatment.

The definition has three boundaries. Each is a set of knowledge, and they nest, in the survey's words "where one subsumes another".[^c3]

- **Outward.** The boundary "defines the observable knowledge boundary for a specific LLM".[^c4] It is checked on "a limited available subset of expressions".[^c5] Knowledge inside it is knowledge the model answers correctly for every instance in that subset.
- **Parametric.** The "abstract knowledge boundary for a specific LLM".[^c6] Knowledge is inside it if at least one expression in the full verifying set Qk succeeds.
- **Universal.** The "whole set of knowledge known to human",[^c7] verifiable by input-output pairs.

Each piece of knowledge k is a set of input-output pairs Qk. Read against the three boundaries, four types follow (my reading of the nesting, with the survey's names):

- Prompt-agnostic known (PAK): inside the outward boundary; every checked expression succeeds, whatever the prompt.
- [[prompt-sensitive-known-knowledge]] (PSK): inside the parametric boundary but outside the outward one; some expression succeeds and some checked expression fails.
- Model-specific unknown (MSU): inside the universal boundary but outside the parametric one; Qk is non-empty, yet no expression in it succeeds for this model.
- Model-agnostic unknown (MAU): outside the universal boundary; Qk is empty, so the knowledge is unknown to humans.

The survey adapts this taxonomy to the older Know-Unknow Quadrant: "PAK and PSK can be viewed as a form of the known-knowns and the unknown-knowns" respectively, "while MSK and MAK jointly formulate the known-unknowns".[^c8] The text writes MSK and MAK in that sentence where its definitions use MSU and MAU. I read them as the same types.

The survey also links the boundaries to uncertainty. Epistemic uncertainty "quantifying the lack of model knowledge, which is related to our definition of Parametric Knowledge Boundary".[^c9] Aleatoric uncertainty "refers to the data-level uncertainty, such as ambiguous prompts having multiple valid answers",[^c10] and is "referring to the gap between Outward Knowledge" and parametric boundaries. My inference: an ambiguous question can fall outside the outward boundary while the model's parametric knowledge is unchanged. Ambiguity then looks like ignorance from the outside.

Most identification methods, per the survey, look at one side: "while the uncertainty decomposition is also concerned about the parametric knowledge boundary".[^c11] Its undesired-behaviour section names the cost of not knowing where the line lies. "LLMs often show overconfidence when addressing topics beyond their knowledge, delivering assertive".[^c12]

The survey declines to define the unknown-unknown: "We do not explicitly define the unknown-unknown, since it is largely".[^c13] The MAU type is "unknown to human", a property of the whole of human knowledge. It is not the asker-relative unknown-unknown of [[unknown-unknowns]], which is a gap in the asker's own axes. The two share a name and a cell in a grid, not an object.

## Limits

- The survey is a review. It says "we systematically review related research"[^c14], and the taxonomy is definitional. In the part read, no experiment tests whether the four types separate real model behaviour.
- The outward boundary is approximate by construction. Its check runs on "a limited available subset of expressions", and the prompt-agnostic nature of knowledge "can only be approximated using a limited subset".[^c15]
- The threshold is free. Each type is defined by a probability that "is larger than a threshold",[^c16] and the part read does not fix the value.
- The universal boundary has no procedure. The text asserts that it is "known to human", but gives no method to enumerate that set, so the MSU/MAU split cannot be checked directly. My inference.
- Each boundary is indexed to one model. A fact outside one model's boundary may be inside another's. My inference, not stated as a result.
- The name is shared with other objects. [[dual-path-knowledge-boundary-probing]] defines a knowledge boundary as the need for tools, and [[bimodal-response-entropy-knowledge-boundary]] as a split by answer entropy. Neither is this three-boundary definition.

## Related

- [[prompt-sensitive-known-knowledge]] — the type between the outward and parametric boundaries, where the question's form decides the answer.
- [[query-level-uncertainty]] — a pre-generation score aimed at the boundary. Its scope is epistemic uncertainty, which the survey ties to the parametric side.
- [[knowledge-boundary-aware-reward]] — an answer-side estimate of the boundary from sampled responses, used to set an abstention reward.
- [[abstention]] — what a system does with a query that falls beyond the boundary.
- [[dual-path-knowledge-boundary-probing]] — a boundary of tool need, sharing the name but not this definition.
- [[bimodal-response-entropy-knowledge-boundary]] — an entropy-based split under the same name.
- [[unknown-unknowns]] — the asker-relative cell the survey leaves undefined.

[^c1]: doi-10-48550-arxiv-2412-12472 — "a comprehensive and formalized definition of the knowledge boundary of LLMs"
[^c2]: doi-10-48550-arxiv-2412-12472 — "this definition is conceptual and lacks formalization"
[^c3]: doi-10-48550-arxiv-2412-12472 — "where one subsumes another"
[^c4]: doi-10-48550-arxiv-2412-12472 — "defines the observable knowledge boundary for a specific LLM"
[^c5]: doi-10-48550-arxiv-2412-12472 — "on a limited available subset of expressions"
[^c6]: doi-10-48550-arxiv-2412-12472 — "abstract knowledge boundary for a specific LLM"
[^c7]: doi-10-48550-arxiv-2412-12472 — "whole set of knowledge known to human"
[^c8]: doi-10-48550-arxiv-2412-12472 — "can be viewed as a form of the known-knowns and the unknown-knowns"
[^c9]: doi-10-48550-arxiv-2412-12472 — "quantifying the lack of model knowledge, which is related to our definition of Parametric Knowledge Boundary"
[^c10]: doi-10-48550-arxiv-2412-12472 — "refers to the data-level uncertainty, such as ambiguous prompts having multiple valid answers"
[^c11]: doi-10-48550-arxiv-2412-12472 — "while the uncertainty decomposition is also concerned about the parametric knowledge boundary"
[^c12]: doi-10-48550-arxiv-2412-12472 — "topics beyond their knowledge, delivering assertive"
[^c13]: doi-10-48550-arxiv-2412-12472 — "We do not explicitly define the unknown-unknown, since it is largely"
[^c14]: doi-10-48550-arxiv-2412-12472 — "we systematically review related research"
[^c15]: doi-10-48550-arxiv-2412-12472 — "can only be approximated using a limited subset"
[^c16]: doi-10-48550-arxiv-2412-12472 — "output probability is larger than a threshold"
