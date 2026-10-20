---
description: "A retriever scores documents against a target hypothesis minus a weighted mimic hypothesis, so the source is chosen by what it must rule out, not only by what it should match."
aliases: ["CHR", "Contrastive Hypothesis Retrieval", "contrastive document scoring", "mimic hypothesis subtraction"]
sources: ["arxiv-2604-04593"]
---
# Contrastive hypothesis retrieval

> Naming the mimic is what lets the retriever rule it out.

## Definition / Mechanism

Kim et al. (2026) observe that query-expansion
retrieval (HyDE, Query2Doc, and kin) builds the query vector from one
generated hypothesis of what the answer is, so it only ever states what to
find; nothing in the query construction represents what a plausible wrong
answer looks like, and a query that drifts toward that wrong answer's
semantic region has no counter-force.[^c1]

Contrastive Hypothesis Retrieval (CHR) routes the source through two
hypotheses instead of one. Given a query and its candidate answers, a
single LLM call produces a target hypothesis $H^+$ (the reasoning for the
likely correct answer) and a mimic hypothesis $H^-$ (the reasoning for the
most plausible incorrect one, including *why* it is plausible and what
rules it out). Every candidate document is then scored by

$$S(d) = \mathrm{Sim}(d, H^+) - \lambda \cdot \mathrm{Sim}(d, H^-)$$[^c2]

which, for normalized embeddings, is retrieval with the shifted query
vector $H^{+\!} - \lambda H^{-\!}$: the mimic direction is subtracted out of
the search vector itself, before any document is scored, rather than
filtered from a candidate pool after the fact. The same difference is
computed directly on BM25 scores for sparse retrieval, so the mechanism
does not require an embedding space.

A fixed $\lambda$ presumes $H^+$ and $H^-$ point in different directions.
When the corpus discusses the two conditions almost interchangeably, the
subtraction removes target-relevant evidence along with the intended hard
negative — the paper's own name for this is semantic co-occurrence
collapse. CHR replaces the fixed penalty with $\lambda_{\text{eff}} =
f_\phi(c) \cdot \lambda_{\max}$, a schedule (linear, threshold or sigmoid)
that softens toward zero as the cosine similarity $c$ between $H^+$ and
$H^-$ rises, so near-collapsed pairs degrade toward $H^+$-only retrieval
instead of erasing the query.[^c3]

## Why it matters

The mechanism is validated by where the gains come from, not only that
they occur. On the $n=587$ cases where CHR answers correctly and HyDE does
not, 85.2% of the two methods' top-5 retrieval lists share **no**
documents, and the mean overlap is 0.18 — evidence that naming the source
to avoid moves the query to a different region of the corpus, not that it
merely re-ranks the same short list HyDE would have found anyway.[^c4]

For source selection generally: a constraint on who or what is asked can be
built from an explicit negative (the plausible wrong source) as well as
from the positive target, and the two need independent, adjustable weight
rather than being folded into one generated hypothesis.

## Limits

Effectiveness is capped by how separable the two hypotheses are in the
corpus's own language, not by the retriever or the schedule: when $H^+$
and $H^-$ describe genuinely interchangeable concepts (the paper's example
is IL-4 versus IL-13 in Th2-mediated inflammation), the adaptive weight
cannot manufacture a discriminative signal it was never given, and this
collapse accounted for about 23% of the fixed-$\lambda$ variant's failure
cases.[^c5]

The hypothesis pair is generated with the candidate answer
options visible to the LLM; the method is evaluated only on multiple-choice
medical QA, and generating a mimic without an answer list to choose from is
left open. The hypothesis generator is held fixed to one large model, so
the cost–accuracy trade-off of a smaller one is `unverified` here.

## Related

- [[bridge-conditioned-retrieval]] — the other c4 case where a candidate
  document is scored against something beyond the bare query; there it is
  prior evidence the pipeline already found, here it is a generated
  negative.
- [[value-of-information]] — scoring what to keep by what it would let you
  rule out is the same move as scoring a question by what it removes.
- [[novice-expert-problem]] — a source chosen by a stated model of the
  wrong answer relies on that model being extractable from an LLM at all.

[^c1]: arxiv-2604-04593 — "They model only what to find without any mechanism to explicitly suppress what to avoid."
[^c2]: arxiv-2604-04593 — "S (d) = Sim(d, H + ) − 𝜆 · Sim(d, H − )"
[^c3]: arxiv-2604-04593 — "𝜆eff = 𝑓𝜙 (𝑐) · 𝜆max,"
[^c4]: arxiv-2604-04593 — "there is zero document overlap between the top-5 results of CHR and HyDE in 85.2% of the instances, and the mean overlap ratio is only 0.18."
[^c5]: arxiv-2604-04593 — "such collapse accounted for approximately 23% of failure cases, occurring primarily when 𝐻 − closely paraphrases 𝐻 + instead of identifying a distinct clinical mimic."
