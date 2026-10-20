---
description: "A reasoning trace can be read as a path of rising probability for the reference answer; its net gain and how smoothly that path climbs give a per-prefix progress score."
aliases: ["ground-truth probability trajectory", "answer probability along the chain", "optimization view of chain-of-thought", "proxy objective over reasoning prefixes"]
sources: ["arxiv-2512-01925"]
---
# Answer-likelihood trajectory

Take a question with a known answer, and let the model write its reasoning trace. After each prefix of that trace, ask the model how probable the known answer is as its next continuation. The result is a sequence of numbers, one per prefix, that starts at the answer's probability with no reasoning and ends near the final step. The paper treats this sequence as the trace of an optimization: the probability of the reference answer is taken as a proxy for the objective, and the trace as a path climbing toward it. The proxy is stated directly: "the probability of the model generating the ground truth answer a serves as an effective proxy for the objective function".[^c1] The reasoning given is that as the trace updates the model's internal state, "the probability of producing the ground-truth answer increases, thereby".[^c2] In the paper's notation the value is an average log-probability over the answer's tokens, taken at each prefix.

The score has two parts, both read from that sequence. The first is a magnitude term. It compares the prefix value with a baseline, the answer's probability with no trace, which the paper describes as "the direct probabilistic prediction from" the model.[^c3] The relative gain is squashed through tanh, so the term sits in (0, 1]; the paper says this "restricted to (0, 1], thus mitigating the impact of extreme values".[^c4] A higher value "signifies a greater increase in the objective function".[^c5]

The second part is a stability term. A rise in probability can be steady or can zigzag, and the paper wants the steady kind. It uses Kendall's tau between the sequence of values and their step indices, to "measure the stability of the optimization process".[^c6] On my reading of its formula, the rank agreement between values and positions is rescaled to [0, 1]. The paper's stated reading is that a steady path scores near 1, and "whereas ineffective updates result in a score near 0".[^c7] The two terms are mixed with a weight, and the paper sets it to one half in its runs.[^c8]

The same quantity is used as a training signal. The trace is cut at paragraph breaks, and the cut points are picked by the entropy of the first token of each segment. For each chosen cut, the score is computed with the answer appended, and the reward for a segment is the change from the previous cut: it "signifies the gain from introducing the partial trajectory from the end of" the earlier segment.[^c9] The entropy filter rests on the view that "High-entropy tokens act as critical decision points".[^c10] The paper's illustration is one problem from AIME 2024 with four correct traces from a 1.5B model, where the negative of the proxy falls as the trace grows.[^c11] In the example it reads, low-reward steps "typically involve self-doubt or redundant re-examination".[^c12]

For asking and answering, the note's content is a way to read progress through a reasoning trace against a reference answer, without a second model judging the steps. That reading is my inference from the mechanism; the paper uses the signal for training, not for evaluation at answer time. In the paper's comparison with vanilla GRPO, accuracy rose on AIME24 "while reducing token consumption by approximately 50%".[^c13]

## Limits

- The score is defined with the reference answer: the paper writes "where a is the ground-truth answer".[^c14] In training that answer exists. At answer time, when no reference is given, the score cannot be computed as written; using it on unlabelled traces is my conjecture, not something the paper tests.
- The proxy's validity rests on one figure, four correct traces from one problem. The slices read do not report how the score relates to correctness across many traces or many problems. A rising answer probability could also come from the trace restating the answer; this was not separated out.
- The authors limit the scope themselves: "its efficacy on subjective or difficult-to-verify problems is unexplored",[^c15] and its "scalability to larger LLMs remains an open question".[^c16] The models tested are up to 8B.
- The weight, the smoothing factor and the number of selected segments are fixed by hand; the sensitivity tables were not read in this pass, so how much the result depends on them is not known here.
- The token saving is a training outcome of RL with the reward, not a measured effect of the trajectory score alone. The component ablations were not read, so the claim that the stability term, rather than the reward shaping in general, does the work is not checked here.

## Related

- [[information-utility-retrieval-control]] — the same answer-likelihood gain, applied per retrieval step as a search-control reward instead of per reasoning segment
- [[counterfactual-retrieval-information-gain]] — an answer log-probability difference with and without a retrieved document; no baseline-without-trace, and no trend term
- [[signed-process-reward-stabilization]] — the same family of heavy-tailed step rewards, stabilised by a dead zone and clipping, where this note squashes with tanh
- [[calibrated-surprisal]] — answer surprisal given the question, a single point without the trace
- [[prefix-correctness-readout]] — a learned head that scores a partial generation for correctness, reading the same prefixes with a trained rather than likelihood-based score
- [[concise-reasoning-mode]] — shorter traces as a cost lever; here a shorter trace is a by-product of a process reward, not a chosen mode

[^c1]: arxiv-2512-01925 — "the probability of the model generating the ground truth answer a serves as an effective proxy for the objective function"
[^c2]: arxiv-2512-01925 — "the probability of producing the ground-truth answer increases, thereby"
[^c3]: arxiv-2512-01925 — "which can be interpreted as the direct probabilistic prediction from"
[^c4]: arxiv-2512-01925 — "range is restricted to (0, 1], thus mitigating the impact of extreme values"
[^c5]: arxiv-2512-01925 — "signifies a greater increase in the objective function"
[^c6]: arxiv-2512-01925 — "to measure the stability of the optimization process"
[^c7]: arxiv-2512-01925 — "whereas ineffective updates result in a score near 0"
[^c8]: arxiv-2512-01925 — "We set the hyperparameters w = 0.5 and α = 0.1"
[^c9]: arxiv-2512-01925 — "signifies the gain from introducing the partial trajectory from the end of"
[^c10]: arxiv-2512-01925 — "High-entropy tokens act as critical decision points"
[^c11]: arxiv-2512-01925 — "reasoning trajectories. We select four"
[^c12]: arxiv-2512-01925 — "typically involve self-doubt or redundant re-examination"
[^c13]: arxiv-2512-01925 — "while reducing token consumption by approximately 50%"
[^c14]: arxiv-2512-01925 — "where a is the ground-truth answer"
[^c15]: arxiv-2512-01925 — "its efficacy on subjective or difficult-to-verify problems is unexplored"
[^c16]: arxiv-2512-01925 — "its scalability to larger LLMs remains an open question"
