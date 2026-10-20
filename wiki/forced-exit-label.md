---
description: "Labelling a stop point by forcing an answer there and checking it against gold gives per-position supervision for a stop probe, with no judge model or human annotation."
aliases: ["forced exit", "counterfactual forced exit", "forced-answer label", "cue-level exit label"]
sources: ["arxiv-2512-05325"]
---
# Forced-exit label

A reasoning trace contains many points at which the model could have stopped, and the trace does not record whether stopping there would have been right. The forced-exit label answers that by intervention. Take one long chain of thought. At a candidate position, cut the trace before the token, append the model's own answer cue, and let the base model write a short answer-only continuation. The continuation is parsed and compared with the gold answer, and the result is one bit.[^c1] The label therefore encodes a single question: "If we had exited at this cue, would the resulting answer have been correct?"[^c2]

The construction needs nothing beyond the model and the task's answer key. "labels are obtained using only the base model and task answers" — no external judge and no human rater.[^c3] The parse uses the same rule-based extractor as the evaluation, so the label is as strict as the benchmark itself.[^c4]

**What the label is attached to.** The label belongs to a position, not to the trace. Each position in the trace gets its own example, and a probe learns the probability that a forced exit at that position is correct, given the hidden state there. LYNX's probe reads several layers at the position and outputs a probability in [0, 1]; the probability is then turned into a stop decision by a calibrated threshold (see [[reflective-cue-decision-points]]). The labels are not balanced. "Since cue-level labels are typically imbalanced" for the smaller models, because early forced exits are mostly not yet safe, so the training loss weights the two classes equally.[^c5]

**Relation to the answer-now test.** [[search-decision-boundary-misalignment]] uses the same test: a forced answer that is correct marks the state as sufficient. There the test is a diagnosis that yields preference pairs for training a search agent. Here the same test is the training label for a probe that reads hidden states. The object is shared; the use differs. The label also states its target, which [[prefix-correctness-readout]] does not: a prefix score there is trained on complete trajectories, and the target a prefix is scored against is not given in the text I read.

**What it makes possible.** A probe trained on these labels can be read at inference, where no forced answer is generated. That is the point of the construction: the expensive counterfactual is paid once, offline, and the online cost is one probe evaluation per cue.

## Limits

- Each position's label comes from one sampled continuation of one trace. The paper runs "a single long CoT rollout with the base model under a fixed decoding" per problem.[^c6] A label is a draw, not an expectation over samples. My inference: the same caveat applies to a forced answer used as a diagnosis.
- A correct forced answer can be a lucky guess, and the label does not check for one. My inference, the same gap noted for the answer-now test.
- The label needs a gold answer and a parse that is decidable. Open-ended questions have no such label, so the construction is confined to verifiable tasks as the paper uses them.
- The cost of building the labels is not measured. The authors "do not optimize the cost of forced-exit dataset construction, viewing it as amortized over downstream usage."[^c7] Each cue costs one extra short generation, and the text reports no total.
- The probe was trained on one mathematical corpus, so the label's meaning on other tasks rests on the transfer result, not on a relabelling of those tasks. I did not read the non-math experiments in detail.

## Related

- [[reflective-cue-decision-points]] — the positions at which these labels are taken and the probe is read
- [[search-decision-boundary-misalignment]] — the same forced-answer test, used there as a diagnosis and as preference data
- [[prefix-correctness-readout]] — a partial-trace score whose target is not stated; a forced-exit label states one
- [[implicit-stopping-knowledge]] — the claim that models know when to stop, which these labels test at cue positions

[^c1]: arxiv-2512-05325 — "we construct a counterfactual forced exit"
[^c2]: arxiv-2512-05325 — "If we had exited at this cue, would the resulting answer have been correct?"
[^c3]: arxiv-2512-05325 — "labels are obtained using only the base model and task answers"
[^c4]: arxiv-2512-05325 — "using the same rule-based extractor as in"
[^c5]: arxiv-2512-05325 — "Since cue-level labels are typically imbalanced"
[^c6]: arxiv-2512-05325 — "we perform a single long CoT rollout with the base model under a fixed decoding"
[^c7]: arxiv-2512-05325 — "do not optimize the cost of forced-exit dataset construction"
