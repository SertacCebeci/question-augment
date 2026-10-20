---
description: "Revising a multi-hop retrieval query from already-observed passages, instead of keeping the original question fixed, by mixing a residual-need signal with the question's own signal."
aliases: ["evireform", "residual query", "evidence-guided reformulation"]
sources: ["xu-2026-evireform"]
---
# Evidence-guided query reformulation

A retrieval system that answers a multi-hop question can keep its
retrieval signal tied to the original question throughout, or it can
revise what it asks for once an initial passage resolves part of the
question. EviReform formalizes the second option: retrieve propositions
for the original question $q$, observe their full source passages
$E_q$, and have an LLM express the remaining, unresolved need as one or
more residual queries $\rho_1,\dots,\rho_L$ — queries that
"preserve the constraints of the original question, incorporate a
bridge established by $E_q$, and ask for the unresolved relation or
attribute."[^c1]

The reformulated signal does not replace the original question's
retrieval signal; the two are normalized separately and mixed as
$s = \beta b(q) + (1-\beta)\, r$, where $b(q)$ is the seed from the
original question and $r$ is the averaged signal from the valid
residual queries ($s=b(q)$ if none return results), because
"independent normalization gives the original and residual channels
controlled total mass."[^c2]

The combined signal is then propagated one step over a proposition
graph connected by shared entities before the final passage ranking is
read out — so reformulation decides *what to ask next* and graph
propagation decides how far that answer's relevance spreads, kept as
two separable operations. Evaluated on 2WikiMultiHopQA, HotpotQA and
MuSiQue against sparse, dense, iterative (IRCoT, S2G-RAG, GeAR) and
graph baselines (PropRAG, HippoRAG 2, CatRAG): "EviReform exceeds the
strongest baseline by up to 5.59 Recall@5 points and 4.50 F1 points."[^c3]

## Limits

The claim rests on a single architecture's ablation, not a general
theorem: the mixing weight $\beta$ and the propagation weight $\alpha$
are both fixed at 0.5 across all datasets in the reported experiments,
so the note cannot say how sensitive the gain is to that choice. The
comparison is against the paper's own selection of baselines, run under
one shared token budget; it does not establish that evidence-guided
reformulation dominates every fixed-query graph retriever, only these.
`[?]` — the source is `xu-2026-evireform`, an arXiv preprint (2026),
not yet independently verified.

## Related

- [[value-of-information]] — asks whether the *next* query is worth
  issuing at all; EviReform assumes it is and asks what to issue.
- [[mutual-information]] — the entropy-drop criterion this method does
  not compute: reformulation is triggered by observed evidence, not by
  a scored information gain over candidate queries.
- [[adaptive-submodularity]] — shares the premise that what to ask next
  should depend on what has already been observed, not be fixed in
  advance.

[^c1]: xu-2026-evireform
[^c2]: xu-2026-evireform — "Independent normalization gives the original and residual channels controlled total mass."
[^c3]: xu-2026-evireform — "EviReform exceeds the strongest baseline by up to 5.59 Recall@5 points and 4.50 F1 points."
