---
description: "Transitivity coverage scores a reasoning chain by the share of its step pairs that link, object to subject, which tests connectedness of steps, not whether each inference is valid."
aliases: ["transitivity coverage", "transitivity score", "transitive closure coverage", "step-link closure score"]
sources: ["arxiv-2512-00552"]
---
# Chain-step transitivity coverage

A reasoning chain can be scored for whether its steps connect, without checking each step's content. The paper first writes every step as a logical form: "extracts logical forms by capturing entities, relations, and" values, each step a tuple of subject, relation, object and values. From the steps it builds a directed graph of entity links.[^c1] The score then counts, over pairs of steps, whether the object of an earlier step is exactly the subject of a later one. The indicator is binary: "Binary δij indicators capture the fundamental logical property of transitivity".[^c2] The sum over pairs is divided by the number of pairs, with the normalization stated as: "The (T choose 2) normalization ensures transitivity scores remain comparable".[^c3]

The mechanism is linking. A chain in which step i hands its output to step j is one where a conclusion of one step is available to the next. A chain whose steps never pick up each other's outputs is a list of disconnected facts, however fluent each one is. The paper also computes a transitive closure, "We compute the transitive closure:",[^c4] which adds every entity reachable by a path. The number reported is the pairwise link share, and a variant is given for entity overlap: "A flow-adjusted variant accounts for entity overlap:".[^c5]

The binary choice is argued, not tested. The authors reject partial credit because a continuous measure "would inappropriately suggest" partial transitivity, a notion they say has no formal meaning here.[^c6] That is a position on the metric, and the text gives no comparison against a graded alternative.

On the small model the coverage was low: "Transitivity scores reach merely 32.2%, indicating frequent".[^c7] The paper reads this as "violations of basic logical closure principles".[^c8]

## Limits

- It measures links, not validity. δij asks whether step i's object equals step j's subject. It does not ask whether either inference is correct, so a chain of wrong but well-linked steps scores high (my inference from the definition).
- Exact string equality decides the score. Paraphrase, a different name for the same entity, or a differently extracted logical form makes a link vanish. The extraction step is described but its accuracy is not reported in the sections I read, so the 32.2% partly measures the extractor.
- Closure is computed but not reported. The text computes G+, the graph of all reachable pairs, but the headline value is the one-step link share. A test that asks whether the implied links exist is not in the reported results.
- One model and one benchmark, with no reference value. Without a baseline from a larger model or from a gold chain scored by the same procedure, 32.2% shows low connectedness by this measure, not how far the measure is from a sound chain.
- The flow-adjusted variant changes the denominator's meaning, and the sections I read do not show its values next to the plain score.

## Related

- [[judge-transitivity-violation]] — transitivity over a judge's pairwise verdicts, scored by flips to a weak total order. Same word, different object: there the relation is a judge's preference, here it is the link between a chain's steps.
- [[bidirectional-reasoning-consistency]] — the paper's other chain-level measure, comparing the forward chain with a backward reconstruction of the same answer.
- [[reasoning-path-fidelity]] — scores a chain by checkpoint recall against an expert path; this measure needs no reference path and sees only the chain's internal links.

[^c1]: arxiv-2512-00552 — "extracts logical forms by capturing entities, relations, and"
[^c2]: arxiv-2512-00552 — "Binary δij indicators capture the fundamental logical property of transitivity"
[^c3]: arxiv-2512-00552 — "The (T choose 2) normalization ensures transitivity scores remain comparable"
[^c4]: arxiv-2512-00552 — "We compute the transitive closure:"
[^c5]: arxiv-2512-00552 — "A flow-adjusted variant accounts for entity overlap:"
[^c6]: arxiv-2512-00552 — "would inappropriately suggest"
[^c7]: arxiv-2512-00552 — "Transitivity scores reach merely 32.2%, indicating frequent"
[^c8]: arxiv-2512-00552 — "violations of basic logical closure principles"
