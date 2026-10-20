---
description: "Divergent creativity is scored as the share of a solution's techniques that human solutions lack, separately from correctness, so novelty and convergent success can move apart."
aliases: ["divergent creativity", "NeoCoder-Divergent"]
sources: ["arxiv-2512-11509"]
---
# Technique-novelty divergent creativity

A model's output can be scored for creativity on two axes that are measured
apart. The NeoCoder benchmark does this on programming problems: "NeoCoder
quantifies creativity along two axes."[^c1] The convergent axis asks whether
the output is right and within the constraints. The divergent axis asks
whether it is new. Its mechanism is a set difference against human writing.
The benchmark has about 30 human-written correct solutions per problem, and
the techniques they use are extracted as a reference set: "atomic techniques
observed in human" solutions.[^c2] For each model output, the divergent term
counts the atomic techniques it uses that the human set does not contain, and
averages that count over the outputs. "Divergent creativity captures novelty
beyond human patterns."[^c3]

The convergent term is a rate of success, not of novelty. "Convergent creativity
measures the proportion of correct solutions that simultaneously" satisfy all
the constraints of the current state.[^c4] A model can therefore be scored
high on one axis and low on the other. The split is what lets the authors
report a null on convergent creativity beside a change on divergent creativity
for the same interventions.[^c5]

The benchmark counts techniques with an LLM judge. The techniques are extracted
from each output by an LLM-as-a-judge step, and the list is what the
divergent term counts. The reference set is therefore the set of
techniques the judge finds in human code, not a set of ideas independently
known to be novel.[^c6] I read the divergent formula in the extracted text as
having no correctness indicator, so the novelty count is taken over outputs
whether or not they pass tests. That is my reading of a formula that may be
garbled in extraction, not a statement the authors make.

CS4 has no human technique set, so its diversity axis is different.
Divergent diversity there is "Quantified by" a Dist-N score, the product of
unique-to-total n-gram ratios over n = 2 to 4.[^c7] That measures lexical
variety across the output, not novelty against a reference. The convergent
analogue is a composite: "Creativity: Evaluated through a composite metric,"
the product of a coherence score and constraint satisfaction.[^c8]

The point of keeping the axes apart is shown in an intervention. Amplifying
creativity-correlated layers and suppressing anti-correlated ones raised the
divergent score while the convergent score stayed flat: the "dissociation
reveals that divergent and convergent creativity" can be separated.[^c9]

## Limits

- Divergent creativity here is novelty relative to a reference pool, not
  novelty in the sense of a new hypothesis. The reference pool sets what
  counts as new. A different pool would give a different score; this is my
  inference from the definition, not something the paper tests.
- A higher count of unfamiliar techniques is not the same as a better idea.
  Unfamiliar code can be wrong, and the divergent term does not weigh
  technique quality. The paper does not analyse this, and I have not verified
  it in the appendix.
- The technique extraction rests on an LLM judge, and the slices I read give
  no agreement check on that extraction.
- The decoupling is reported with hedging: divergent and convergent creativity
  are "possibly decoupled." It was shown for LLaMA and Qwen-coder on NeoCoder,
  and for LLaMA 8B on CS4 only, where "CS4 results are evaluated on LLaMA 8B
  only due to computation."[^c10]
- CS4 coherence is judged pairwise against a baseline story at 23 constraints,
  so the scale of the coherence term depends on that choice; the slices I read
  do not test an alternative baseline.
- Both benchmarks are proxies. The authors state that "creativity" here is
  measured on programming and story tasks, and that the measure has not been
  built for scientific hypotheses.[^c11]

## Related

- [[hallucination-reduction-divergence-effect]] — the interventions whose effects are read through these two axes
- [[divergent-convergent]] — same words, different object: a design-process split between generating and judging options, not a measure of outputs
- [[effective-diversity]] — counts distinct useful outputs; a diversity measure, not a reference-relative novelty count
- [[innovation-correctness-tradeoff-in-problem-generation]] — the same novelty-versus-correctness pair under fine-tuning, which this note's two axes make measurable

[^c1]: arxiv-2512-11509 — "NeoCoder quantifies creativity along two axes"
[^c2]: arxiv-2512-11509 — "atomic techniques observed in human"
[^c3]: arxiv-2512-11509 — "Divergent creativity captures novelty beyond human patterns"
[^c4]: arxiv-2512-11509 — "Convergent creativity measures the proportion of correct solutions that simultaneously"
[^c5]: arxiv-2512-11509 — "Meanwhile, convergent creativity is largely unaffected."
[^c6]: arxiv-2512-11509 — "Using LLM-as-a-Judge, the"
[^c7]: arxiv-2512-11509 — "Diversity: Quantified by"
[^c8]: arxiv-2512-11509 — "Creativity: Evaluated through a composite metric"
[^c9]: arxiv-2512-11509 — "dissociation reveals that divergent and convergent creativity"
[^c10]: arxiv-2512-11509 — "CS4 results are evaluated on LLaMA 8B only due to computation"
[^c11]: arxiv-2512-11509 — "proxy of actual scientific hypothesis generation"
