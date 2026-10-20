---
description: "Two role-differentiated LLM agents pose bounded, ordered questions (content then surface form) to a writer agent, and an evaluator keeps only revisions the questions actually improved."
aliases: ["SQ2E", "Stepwise Questioning Expert-Editor", "Expert-Editor Multi-Agent", "Expert-Editor Stepwise Questioning"]
sources: ["shen-2026"]
---
# Expert-editor stepwise questioning

> A fixed axis order — content quality before surface form — enforced by
> giving two different agents the two axes and a bounded [[question-budgets|question budget]]
> each, with a third agent deciding after every answer whether the
> resulting revision was actually worth keeping.

## Definition / Mechanism

Shen & Guo's SQ2E assigns a long-document summarization revision loop to
four roles: a writer drafts the summary, an **expert** questions its
semantic content, an **editor** questions its surface form, and an
**evaluator** judges each revision against its predecessor. The expert
always questions before the editor — content quality is resolved as an
axis before surface form is touched at all, a fixed order rather than a
per-item ranked one. The expert's questions are open-ended and capped at
five per round; the editor's are restricted to yes/no format and capped at
four, so the writer only revises when it confirms an issue exists: "the
editor's questions adopt a yes-no format. The author answers these
questions by compare the summary with the source article. If the issue in
the editor's question exists in the current summary, the author responds
'yes' and revises the summary."[^c1]

After every answer the writer revises, and the evaluator — not the
asking agent — decides whether the question counted: "A valid question is
defined as one where the expert or editor raise a question, the author
revised the summary accordingly, and the evaluator judged the revised
summary superior." An asked-and-answered question that does not clear this
evaluator gate leaves the summary unchanged; the gate, not the question's
content, is what makes an answer a kept constraint.[^c2]

## Why it matters

The design separates two things a single question-asking loop usually
conflates: which axis to ask about next, and whether an answer on that
axis was worth acting on. The axis order is not learned or scored per item
— it is fixed by role assignment (expert always first) — while the
keep/discard decision is delegated entirely to a third agent's pairwise
judgment, run after every single question rather than once at the end.
Measured against a direct-generation baseline and a prior
segment-and-aggregate method (HERA) on arXiv and PubMed across three LLM
backbones, the loop raised ROUGE, BERTScore and FactCC on two of three
backbones: "when using LLama-3.1-8B and Deepseek-R1 models, significant
improvements are observed in ROUGE, BERTScore, and FactCC metrics.
However, the scores of some metrics decrease noticeably on
LLama-3.1-70B." Per-round, most cases showed "the expert's questions led
to 3-4 valid optimizations, and the editor's questions resulted in 2-3
valid revisions" — so the content-first axis produced more accepted
revisions than the surface-form axis it strictly precedes.[^c3]

## Limits

- The content-before-surface order is never compared against the reverse
  or against an interleaved order; the paper reports only the one fixed
  sequence, so the claim is that this order worked, not that it worked
  better than an alternative.[^c4]
- The regression on the 70B [[backbone-of-a-formula|backbone]] is the authors' own conjecture
  ("we conjecture that this phenomenon may be attributed to the loss of
  precision during the inference of the 70B-parameter model") rather than
  a diagnosed cause, and the method's benefit does not hold uniformly
  across model scale.[^c5]
- Evaluated only on long-document scientific summarization (arXiv,
  PubMed) with automatic metrics (ROUGE, BERTScore, FactCC) and no human
  judgment; the evaluator that gates every revision is itself an
  unvalidated LLM judge, not a ground-truth check.[^c6]

## Related

Selection · [[value-of-information]] · [[constraint-as-information]]

[^c1]: shen-2026
[^c2]: shen-2026 — "A valid question is defined as one where the expert or editor raise a question, the author revised the summary accordingly, and the evaluator judged the revised summary superior."
[^c3]: shen-2026 — "when using LLama-3.1-8B and Deepseek-R1 models, significant improvements are observed in ROUGE, BERTScore, and FactCC metrics. However, the scores of some metrics decrease noticeably on LLama-3.1-70B."
[^c4]: shen-2026 — "Both roles pose questions incrementally based on the query plan formulated in previous steps."
[^c5]: shen-2026 — "We conjecture that this phenomenon may be attributed to the loss of precision during the inference of the 70B-parameter model, which is associated with the computational resources utilized in our experiments."
[^c6]: shen-2026 — "We employed three automated metrics to evaluate the relevance, completeness, and factual consistency of the generated summaries: ROUGE-L (Lin, 2004), BERTScore(Zhang et al., 2020), and FactCC (Kryściński et al., 2019)."
