---
description: "Scoring candidate seeds by the student's loss on its own greedy answers, the uncertainty-sampling rule, gave the most data-efficient synthetic sets, ahead of LLM-as-a-judge scoring."
aliases: ["loss (high)", "uncertainty sampling on student generations", "student-loss uncertainty sampling", "high-loss seed selection"]
sources: ["arxiv-2512-00884", "arxiv-2512-00380"]
---
# Loss-based seed selection

The score is the student's own loss on its own answer. For each seed question the student greedily decodes an answer, and the length-normalised cross-entropy of that answer under the student is the seed's score. The highest-loss seeds are taken first, and the teacher is asked to write new questions from them.[^b1] In a sequence model this is the uncertainty-sampling rule of the active-learning literature. When the target of the loss is the model's own generation, "this score reflects an uncertainty in the produced sequence".[^b2]

The paper compares this rule with several alternatives: a reward model scoring the student's answer, an LLM judge comparing student and teacher answers, a diversity-based gradient method (BADGE), and sampling from correct and incorrect pools. Across the datasets and budgets, "the highest-performing approach is simply uncertainty sampling" on the student's own generations.[^b3] The paper states the ranking as pairwise win counts over datasets, with a one-standard-error interval, not as effect sizes.[^b4] LLM-as-a-judge "also tends to be somewhat effective, though by a reduced margin".[^b5]

The cost argument is the practical reason the rule is preferred. Its score needs only the student's forward pass, while "Because of the need to access a teacher model for scoring, LLM-as-a-judge is computationally" expensive.[^b6] The paper's reading is that the compute saved is better spent on generating more synthetic data.

Two variants are measured and both do worse. Scoring with the ground-truth answer instead of the student's own generation is "less effective empirically than using the former".[^b7] A reward model is a weaker signal on some tasks: "reward scoring performs poorly for the Game of 24 since it is biased by long student answers".[^b8] The paper attributes this to length bias: "is because the reward scorer introduces biases; specifically, it prefers longer responses".[^b9] For tasks that lie outside the scorer's training distribution, scorers "can perform even worse than random sampling".[^b10]

The same kind of score has been applied to structured knowledge rather than to generated answers. APIKG4Syn scores each parent–child link of an API knowledge graph by the negative log of the model's conditional probability of the child given the parent and relation, and uses that uncertainty to choose which nodes to combine.[^b11][^b12] This is a different quantity from the greedy-answer loss, and the paper does not compare the two; the structured use and its path search are in [[uncertainty-path-seed-composition]].

## Limits

- The ranking is across four datasets and four small students, with the teacher's outputs assumed correct (see [[student-in-the-loop-synthetic-generation]]). Nothing here shows the rule wins on tasks outside reasoning.
- The score is taken on the student's greedy answer. A student that is confidently wrong has a low loss on its own answer and is never selected. The paper's result does not test this miss rate; that is my inference from how the score is defined.
- The active-learning literature has a caution on uncertainty-based querying: it can spend labels where a wrong guess is cheap. [[noise-seeking-uncertainty-sampling]] states it for excess error with labelled points. Whether a loss-on-own-generation score falls into the same trap here is not tested, and the setting differs (generated data, no abstention).
- The margins between uncertainty and LLM judging are described as "somewhat" effective and "a reduced margin"; the paper's comparison is by win count, so the size of the gap is not measured.
- Diversity was not shown to add anything on top of the loss score in these experiments. The loss rule is the one that won, not a rule that combines it with diversity.

## Related

- [[uncertainty-path-seed-composition]] — the same model-uncertainty score, applied to knowledge-graph links and summed along searched paths
- [[student-in-the-loop-synthetic-generation]] — the loop in which this score is used to choose the seeds each round
- [[seed-property-inheritance]] — why a seed's loss tends to reappear in what the teacher writes from it
- [[llm-judge-biases]] — the bias problems of LLM scoring, which this paper's cost and reliability findings echo
- [[expected-information-gain]] — the information-maximising ideal that uncertainty sampling approximates
- [[positive-first-most-ambiguous-selection]] — an uncertainty-based query rule that changes the score to favour likely positives

[^b1]: arxiv-2512-00884 — "as the model’s loss on greedily decoded student generations"
[^b2]: arxiv-2512-00884 — "this score reflects an uncertainty in the produced sequence"
[^b3]: arxiv-2512-00884 — "the highest-performing approach is simply uncertainty sampling"
[^b4]: arxiv-2512-00884 — "we aggregate results as a pairwise winrate matrix P"
[^b5]: arxiv-2512-00884 — "LLM-as-a-judge also tends to be somewhat"
[^b6]: arxiv-2512-00884 — "Because of the need to access a teacher model for scoring, LLM-as-a-judge is computationally"
[^b7]: arxiv-2512-00884 — "Interestingly, we find this to be less effective empirically than using the former,"
[^b8]: arxiv-2512-00884 — "reward scoring performs poorly for the Game of 24 since it is biased by long student answers"
[^b9]: arxiv-2512-00884 — "is because the reward scorer introduces biases; specifically, it prefers longer responses"
[^b10]: arxiv-2512-00884 — "for tasks that are out-of-distribution for the scoring model, like Game of 24, these"
[^b11]: arxiv-2512-00380 — "UE for each non-leaf node, thereby quantifying the model"
[^b12]: arxiv-2512-00380 — "The negative logarithm of this probability"
