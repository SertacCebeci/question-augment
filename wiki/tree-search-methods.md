---
description: "$N$ samples from one model are not $N$ independent answers — independence is At stall 4 the agent can be its own source only by sampling itself more than once."
aliases: []
sources: ["wang-2022", "yao-2023", "multi-agent-debate-heterogeneity-2026", "arxiv-2512-05580"]
---
# Tree search methods

> $N$ samples from one model are not $N$ independent answers — independence is
> bought with diversity, and the published ways of spending inference-time
> compute differ in how much of it they buy.

## Mechanism

At stall 4 the agent can be its own source only by sampling itself more than[^s1][^s2][^s3]
once. What that buys depends on how correlated the samples are, and the three
published methods below sit at different points on that axis. They are
**separate methods**, measured on different tasks with different results — not
three names for one thing.

**Self-consistency (Wang et al. 2022, ICLR 2023).** Sample $N$ chain-of-thought
paths from one model, then take a **majority vote** over the final answers,
marginalising out the reasoning paths. Measured on arithmetic and commonsense
benchmarks (GSM8K, SVAMP, AQuA, StrategyQA, ARC-challenge) across UL2-20B,
GPT-3-175B, LaMDA-137B and PaLM-540B; the authors report gains over
chain-of-thought prompting of +17.9% on GSM8K, +11.0% on SVAMP, +12.2% on AQuA,
+6.4% on StrategyQA and +3.9% on ARC-challenge with their strongest models. All
numbers are the authors' own.

**Tree of Thoughts (Yao et al. 2023, NeurIPS 2023).** Keeps a tree of
"thoughts" — coherent intermediate text units — generates several per node, has
the model **self-evaluate** them, and searches the tree (BFS/DFS) with
lookahead and **backtracking**. Measured on three tasks the authors introduced:
Game of 24, creative writing and mini-crosswords, with GPT-4; on Game of 24
they report 4% success for chain-of-thought prompting against 74% for ToT. What
matters here is not the sampling but the revocability: commitment to a
trajectory becomes reversible.

**Multi-agent debate (Zhu et al. 2026, Findings of ACL 2026).** The authors
argue that under **homogeneous agents with uniform belief updates** debate
preserves expected correctness, so replicating identical agents cannot reliably
improve on the single-agent answer. They name two missing components —
**diversity of initial viewpoints** and **explicit, calibrated confidence
communication** — and report that a diversity-aware initialisation plus a
confidence-modulated protocol beat vanilla debate and majority vote on six
reasoning-oriented QA benchmarks. That those two components are the operative
ones is this paper's claim on its own six benchmarks; the wiki carries the
source unverified (see Limits).

## Why it matters

For an asker that treats itself as a source: the count $N$ is not the quantity
that buys precision — the effective number of independent draws is. Wang's
majority vote already presumes the sampled paths disagree; Zhu's homogeneity
result is the same point stated as a limit, that identical agents deliberating
add nothing; ToT spends the compute differently, on revoking commitments rather
than on counting agreements.

*Inferred here, not tested:* samples drawn under **one context and one mandate**
are correlated by construction, so the effective sample size is below $N$ and
the return curve of [[cramer-rao-bound]] flattens; varying the context and the
mandate under which each sample is drawn is what buys the independence back. No
source cited here measures that correlation, or the effective sample size of
self-generated questions.

## Transfer

The $1/\sqrt{N}$ argument and the additivity $\mathcal{I}_n = n\mathcal{I}_1$
are imported from estimation theory ([[cramer-rao-bound]]) and pointed at
sampled natural-language reasoning paths.

| | |
|---|---|
| **In its home field** | $n$ i.i.d. draws from a parametric family; an unbiased scalar estimator of a continuous parameter under likelihood regularity; variance is the loss |
| **Here** | $N$ reasoning paths sampled from one model under one prompt; a majority vote over discrete answer strings; no likelihood, no unbiasedness, no parameter — accuracy is the loss |
| **What survives** | the qualitative shape: accumulating more draws narrows the spread with diminishing returns, and correlation among the draws flattens that curve — which makes diversity structural rather than aesthetic |
| **What does not** | the additivity $\mathcal{I}_n = n\mathcal{I}_1$; the $1/\sqrt{N}$ rate as a number; the unbiasedness and regularity conditions; and any bound at all on majority-vote accuracy — the Cramér–Rao bound constrains an estimator's variance, not a vote's error probability |

## Limits

- Every number above is single-paper and author-reported, on benchmarks the
  authors chose (arithmetic, commonsense and reasoning QA; Game of 24,
  crosswords). None is an independent replication, and nothing here is measured
  on open-ended question-asking, which is this wiki's subject.
- Whether debate beats the cheaper baseline of sampling plus majority vote at a
  matched compute budget is not settled by any source this note cites; the note
  claims only what Zhu et al. report against their own vanilla-debate and
  majority-vote baselines.
- `multi-agent-debate-heterogeneity-2026` is registered `[?]` (unverified) in
  the wiki's sources. This revision identifies it with Zhu, Zhang, Chi,
  Stafford, Collier & Vlachos, *Demystifying Multi-Agent Debate: The Role of
  Confidence and Diversity*, Findings of ACL 2026 (arXiv 2601.19921), pending
  the verifier; until then the homogeneity claim is sourced but unconfirmed.
- The effective-sample-size claim in *Why it matters* is this wiki's own
  inference from [[cramer-rao-bound]], not a measured quantity, and the
  Cramér–Rao conditions it borrows do not hold here (see Transfer).
- The Bengali math study (arxiv-2512-05580) also calls its method "Tree of Thoughts", but the prompt it tests is narrower than Yao's search. Its ToT is one zero-shot system prompt that asks the model to explore several paths and then choose a final answer, in a single generation.[^s4][^s5] My reading of that prompt is that no separate self-evaluation, lookahead or backtracking is run, so its results do not test the revocability that the section above attributes to ToT.
- The "up to five points" gain is larger than the text's own peaks. The abstract's headline is measured against CoT cells the text does not treat as peaks. The text gives GPT-OSS-120B's CoT peak as 88%, the same as its ToT score,[^s6][^s7] and Maverick's CoT peak as 86%, not the 83% used for its +5 comparison.[^s8][^s9] Against the CoT peaks the text states, ToT is 0 to 2 points ahead for the four models it names: GPT-OSS-20B (86 to 87),[^s16] GPT-OSS-120B (88 to 88), LLaMA-3.3-70B (87 to 88),[^s17] and Maverick (86 to 88).
- The comparison is not matched. ToT was run only zero-shot, while CoT ran at 1 to 7 shots, so the strategy and the number of exemplars change together.[^s10] The paper reports one number per cell, at temperature 1.0,[^s11] and the sample is 100 items.[^s12] My inference: a gap of one or two items is not separated from resampling noise by anything the paper reports.
- The scale claim rests on one small model. The paper's own statement is that "Tree-of-Thought prompting depends heavily on model scale",[^s13] and LLaMA-3.1-8B fell to 31% under ToT.[^s14] That is one 8B model, and scale is not separated from model family.
- Grading is final-answer only, by exact match, checked by hand.[^s15] A path that reaches the right number by a wrong route counts as correct, so the paper's claim of "globally consistent" reasoning is not measured by this metric.

## Related

[[cramer-rao-bound]] · [[semantic-entropy]] · [[dialectic-red-team]] · [[novice-expert-problem]] · [[self-ask-decomposition]] · [[tree-of-thought-socratic-teaching]] — the same label on a tutor that scores live paths and switches between them, a switching rule the one-prompt Bengali variant does not have
- [[mcts-training-trace-generation]] — the same kind of search run offline, with an outcome reward, to produce training traces rather than to spend compute at answer time

[^s1]: wang-2022
[^s2]: yao-2023
[^s3]: multi-agent-debate-heterogeneity-2026
[^s4]: arxiv-2512-05580 — "explored multiple reasoning branches before converging on"
[^s5]: arxiv-2512-05580 — "After exploring different paths, choose the most"
[^s6]: arxiv-2512-05580 — "CoT by up to five percentage points, with GPT-OSS-120B"
[^s7]: arxiv-2512-05580 — "GPT-OSS-120B peaked at 88% in the 1-shot high"
[^s8]: arxiv-2512-05580 — "Maverick improved from 83% in CoT to 88% under ToT"
[^s9]: arxiv-2512-05580 — "achieved strong results, peaking at 86% under 5-shot CoT"
[^s10]: arxiv-2512-05580 — "our proposed tree-of-thoughts prompting was evaluated exclusively under the zero-shot setting"
[^s11]: arxiv-2512-05580 — "For the GPT-OSS models, we fixed the temperature at 1.0"
[^s12]: arxiv-2512-05580 — "This study was limited to 100 samples from the SOMADHAN dataset"
[^s13]: arxiv-2512-05580 — "Tree-of-Thought prompting depends heavily on model scale"
[^s14]: arxiv-2512-05580 — "LLaMA-3.1-8B collapsed under ToT, falling to just 31%"
[^s15]: arxiv-2512-05580 — "correct if the final numeric or symbolic result exactly matched"
[^s16]: arxiv-2512-05580 — "from its CoT peak of 86% to 87% with ToT"
[^s17]: arxiv-2512-05580 — "LLaMA-3.3-70B increased from 87% with CoT"
