---
description: "Four small models critique each other's anonymized answers against a fixed issue list before a chairman synthesizes; removing that critique stage cost 7.6 points on TruthfulQA MC1."
aliases: ["anonymized peer review of answers", "cross-review before synthesis", "peer critique stage", "LLM council critique"]
sources: ["arxiv-2601-00850"]
---
# Anonymized cross-review

Each candidate answer is written separately. Then every model reads the other answers, relabelled as Candidate A, B, C and D, so that no reviewer knows which model or role produced which answer. The paper's stated purpose for the relabelling is that each model "reviews peer answers anonymized as Candidate A/B/C/D to reduce positional or identity bias".[^c1]

The review is not free prose. It is a constrained object: a score per candidate on accuracy, insight and clarity; a list of concrete issues, each typed by a fixed label; and "best bits", passages worth keeping. "Review outputs are constrained to a structured JSON schema containing" these parts.[^c2] The labels are fixed at four: `factual_risk`, `missing_edge_case`, `unclear` and `incomplete`. The first carries most of the weight for the answer, since it is defined as "a likely incorrect, unsupported, or unverifiable claim that could change" the selected answer.[^c3]

The reviews are not used as votes. The paper turns each reviewer's scores into a total order and aggregates the orders by Borda count, but the ranking is only one input. The chairman is a separate model that receives the question, all candidates and the aggregated review summaries. Its job is to select strong segments, "attempting to resolve conflicts using critiques", and then rewrite for clarity.[^c4] The design claim is that this synthesis "integrates minority-correct reasoning rather than discarding it via voting".[^c5]

The mechanism is therefore a change of operation, not of sample. Majority vote keeps the answer most candidates share. The chairman can keep the one sentence from the one candidate that was right and drop the sentence a reviewer flagged. The paper counts a critique as having acted when a reviewer flags a concrete issue and the chairman "explicitly removes or revises the flagged span in the final answer".[^c6] That lets an edit be traced to a critique, rather than only inferred from a score change.

## What was measured

On the full TruthfulQA MC1 set, "817 questions",[^c7] the complete pipeline reached 76.2%. Removing the chairman synthesis gave 67.4% and removing cross-review gave 68.6%, with paired McNemar tests and Holm–Bonferroni correction.[^c8] The text states the cost of the critique stage directly: "removing cross-review costs 7.6 absolute points on TruthfulQA".[^c9] The gain is uneven across question kinds. Cross-review added +12.4% on common misconceptions and +18.7% on trick questions, and +2.1% on simple factual ones.[^c10] The paper's own reading is that "Stage 2 (cross-review) and Stage 3 (chairman synthesis) are the dominant" contributors to accuracy.[^c11] The full pipeline also "outperforms self-consistency and majority vote", the two baselines that aggregate by sampling or voting.[^c12]

## Limits

- The component ablation I read is on one benchmark, TruthfulQA MC1, where the answer is a single letter. Whether critique helps free-form answers, where the "best bits" and rewriting carry more of the content, is not shown in the material read here. (my reading)
- The attribution of fixed errors is a sampled, hand-labelled analysis: "We attribute improvements by labeling a sampled subset of failures".[^c13] It is not a counted rate.
- Results depend on the prompts: "Role prompts and chairman instructions materially affect performance."[^c14]
- The critique is an extra round of calls. "EdgeJury increases median latency (8.4s vs. 2.1s single-model)".[^c15]
- The anonymization rationale is the paper's design claim. No ablation of anonymization is reported in the parts read, so this note credits it with no measured effect. (my reading)
- The reviewers are the candidate writers. A critic built from the same weights as the writer can share its blind spot, and the paper does not measure how often a shared error survives review. Its own note on the agreement stage says that stage "cannot detect shared misconceptions if all candidates agree on the same falsehood".[^c16] The [[coincident-failure]] note holds the wider measurements on why independently produced sources fail together.
- The single-round design is a choice made for latency. The paper argues against multi-round debate on cost; in the parts read it does not compare the two on accuracy. (my reading)

## Related

- [[disagreement-retention-in-debate]] — multi-round debate that rebroadcasts disagreeing answers by index; cross-review is single-round and passes on structured critiques instead
- [[cross-provider-judge-ensemble]] — independent verifiers combined by their verdicts; the same diversity argument on the judging side
- [[claim-level-agreement-labeling]] — the stage after synthesis, which tags the final answer's claims by candidate agreement without rewriting it
- [[coincident-failure]] — why reviewers and writers drawn from one model family may fail together

[^c1]: arxiv-2601-00850 — "Each model reviews peer answers anonymized as Candidate A/B/C/D to reduce positional or"
[^c2]: arxiv-2601-00850 — "Review outputs are constrained to a structured JSON schema containing"
[^c3]: arxiv-2601-00850 — "a likely incorrect, unsupported, or unverifiable claim that could change"
[^c4]: arxiv-2601-00850 — "attempting to resolve conflicts using critiques"
[^c5]: arxiv-2601-00850 — "integrates minority-correct reasoning rather than discarding it via voting"
[^c6]: arxiv-2601-00850 — "explicitly removes or revises the flagged span in the final answer"
[^c7]: arxiv-2601-00850 — "Results are reported on the full TruthfulQA MC1 set (817 questions)"
[^c8]: arxiv-2601-00850 — "Component contribution analysis on TruthfulQA MC1"
[^c9]: arxiv-2601-00850 — "removing cross-review costs 7.6 absolute points on TruthfulQA"
[^c10]: arxiv-2601-00850
[^c11]: arxiv-2601-00850 — "Stage 2 (cross-review) and Stage 3 (chairman synthesis) are the dominant"
[^c12]: arxiv-2601-00850 — "outperforms self-consistency and majority vote"
[^c13]: arxiv-2601-00850 — "We attribute improvements by labeling a sampled subset of failures"
[^c14]: arxiv-2601-00850 — "Role prompts and chairman instructions materially affect performance."
[^c15]: arxiv-2601-00850 — "EdgeJury increases median latency (8.4s vs. 2.1s single-model)"
[^c16]: arxiv-2601-00850 — "cannot detect shared misconceptions if all candidates agree on the same falsehood"
