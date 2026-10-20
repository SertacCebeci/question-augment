---
description: "The value of information lies not in what you learn but in **whether it The value of the best decision you would make after learning the answer,"
aliases: ["VoI", "expected value of information", "Howard's information value"]
sources: ["biyik-2019", "howard-1966", "arxiv-2601-06407", "arxiv-2601-01522", "doi-10-48550-arxiv-2608-26846", "doi-10-48550-arxiv-2608-20316"]
---
# Value of information

> The value of information lies not in what you learn but in **whether it
> changes your decision**.

## Howard (1966)

$$\mathrm{VoI}(q) = \mathbb{E}\big[\max_a U(a\mid \text{answer})\big] - \max_a \mathbb{E}\big[U(a)\big]$$[^s1][^s2]

The value of the best decision you would make after learning the answer, minus
the value of the best decision you would make now. Howard (1966) built the
quantity precisely against a Shannon-style measure: a theory that scores
outcomes by their probabilities alone, without their consequences, cannot say
what an experiment is worth.

## EVPI — the value of perfect information

Howard (1966) computes the **expected value of clairvoyance** — what you would
gain if the uncertain state were revealed exactly — and shows it is an upper
bound on the value of any experimental program. The scope of the bound is the
sentence that matters: *within a fixed decision problem* — fixed action set,
fixed prior, fixed utility — no signal about that state can be worth more than
EVPI. It says nothing about a question that changes the decision problem
itself (adds an action, revises the utility, opens an unmodelled axis); such a
question is outside the bound, not below it.

## The most important consequence: VoI can be zero

$$\mathrm{VoI}(q) = 0 \iff \text{you would choose the same action whatever the answer}$$

— modulo utility-indifferent actions. The forward direction is unconditional;
the converse holds only when the optimal action is unique. With ties in
$\arg\max_a$ you may pick a *different* action for different answers and still
have $\mathrm{VoI}(q) = 0$, because the tied actions carry the same expected
utility. Read the equivalence as: *the achieved utility* is the same whatever
the answer.

This is the difference from [[expected-information-gain]]:

```text
EIG > 0   but   VoI = 0     →   the question informs but is useless
```

Questions with high EIG that change no decision exist; under a fixed decision
problem they are pure cost.

## The pruning rule — this wiki's inference, not Howard's

Howard gives the quantity; the reading below is this wiki's, and it is a
heuristic, not a theorem:

> Treat a question as worth asking only if **different answers would produce
> different output**.

Used as a [[stopping-rules|stopping condition]] it sits alongside [[sprt]]: SPRT stops when the
evidence is decisive, this stops when no answer would move anything. In a
science-fiction story, "what colour are the protagonist's eyes" has positive
EIG, but if nothing downstream ever reads it, its VoI against that
output is zero. The step from "no downstream use" to $\mathrm{VoI}=0$ is an
inference by analogy: it presumes the output can stand in for an action set
and a utility that nobody has written down.

## Subtract the cost

Howard (1966) makes the decision to buy information a net one:

$$\text{Net} = \mathrm{VoI}(q) - \mathrm{Cost}(q)$$

Cost differs by orders of magnitude between a question an agent puts to
itself and one it puts to a user, and that gap — not the mathematics — is what
separates the two thresholds; the fuller treatment is [[question-budgets]]
(this wiki's framework, not Howard's).

One worked instance shows what the net rule costs to run. Bıyık et al. (2019)
attach a query-dependent cost $c(Q)$ to each question, select by
$\max_Q\, I(\omega; q \mid Q) - c(Q)$, and prove (their Theorem 3) that a
greedy asker should stop asking exactly when that maximum turns negative. Two
substitutions are visible in it: **information gain stands in for VoI**, so
the rule prices what is learned rather than what the decision gains; and the
cost is a *function of the question*, which is what makes stopping a property
of the questions that remain instead of a counter. Their other result cuts the
opposite way — the answerer's difficulty need not enter $\mathrm{Cost}$ at
all, because [[mutual-information|mutual information]] already subtracts the answerer's own response
[[entropy]] ([[volume-removal]]).

## Instantiated for LLM agents (Dong et al. 2026)

Dong et al. compute VoI directly for a clarify-or-commit agent. The LLM states a belief b(θ) over candidate user intents; for each candidate closed-ended question it simulates each answer, re-estimates the belief, and scores VoI(q) = V_post(b,q) − V(b). The agent asks the question with the highest NetVoI(q) = VoI(q) − c and commits once the maximum is non-positive.[^c1] Unlike the Bıyık instance above, this prices the decision's gain, so the same uncertainty yields different stopping by stakes: with identical cost c = 0.05, the agent kept asking in a diagnosis task (reward 10) past where a confidence threshold would stop, and halted early in an animal-guessing game (reward 1).[^c2] Reported result: VoI matched or exceeded the best manually tuned baselines in 18 of 20 conditions, with no threshold to tune.[^c3] This is evidence that the net rule works with LLM-estimated beliefs, not that those beliefs are calibrated.

## Known as

| Field | Name there | Relation |
|---|---|---|
| Decision analysis | value of information / VoI | exact |
| Decision analysis | expected value of information | exact |
| Decision analysis (Howard 1966) | Howard's information value | exact |
| Decision analysis | EVPI / expected value of clairvoyance | close — **not this concept**: EVPI is this functional evaluated at a perfectly informative signal, so it is a single upper bound over all $q$, not $\mathrm{VoI}(q)$ for a particular question |

## Transfer

| | |
|---|---|
| **In its home field** | A decision problem with an explicit action set $A$, a prior over states, a utility $U$, and a signal with a known likelihood; VoI is then a computed number (Howard 1966) |
| **Here** | A question asked by an agent or of a user, whose answer space is unbounded free text; the action set is implicit, the prior unwritten, and no utility exists on paper — so $\mathrm{VoI}(q)$ is a judgement, not a computation |
| **What survives** | The invariance test — a question earns its place only if some answer would change what gets done — and EVPI as a qualitative ceiling: no amount of asking beats knowing, within one fixed problem |
| **What does not** | The number. Without an enumerated $A$ and a written $U$ there is no arithmetic in $\mathrm{VoI}-\mathrm{Cost}$, no ordering of two questions by VoI, and no test of whether a claimed $\mathrm{VoI}=0$ is really zero rather than unmodelled |

## Limits

- Needs a utility function and a decision set — absent during exploration
  ([[expected-utility]]).
- The $\mathrm{VoI}=0$ equivalence holds only modulo utility-indifferent
  actions: with ties in $\arg\max$, the chosen action may differ across
  answers at zero VoI.
- The EVPI bound is scoped to a fixed action set, prior and utility, and to
  signals about the same uncertain state; a question that enlarges the
  decision problem is not covered by it.
- Myopic in its usual form: the value of one piece of information now.
  Information that pays only in combination has $\mathrm{VoI} \approx 0$
  individually and is undervalued.
- Assumes the decision-maker will act optimally on what they learn.
- **The instance in *Subtract the cost* is not VoI.** Bıyık et al. (2019)
  maximise information gain net of cost; with no utility over actions their
  stopping theorem inherits EIG's blindness to whether the answer changes
  anything, and it holds for greedy selection from a finite query set under
  their assumed model of the answerer. It is evidence that the net *form* is
  operable, not that VoI itself has been computed.
- `howard-1966` is confirmed only to its bibliographic record — IEEE Trans.
  Systems Science and Cybernetics 2(1), 22–26, doi:10.1109/TSSC.1966.300074 —
  and carries `verified: prior` in `wiki/meta/sources.json`; the published
  text sits behind IEEE and has not been read against this note, so the EVPI
  bound and the net rule are stated here as the field states them.
- The LLM instance restricts to closed-ended questions with a one-step lookahead, takes a constant per-question cost c, and uses the LLM's own simulated answer likelihoods and utilities; its gains are shown on four benchmarks with simulated users, and utility scales (reward 1 vs 10) are set by the experimenters.[^c1]
- The pruning rule and the cost split are this wiki's inferences; only the
  definition, the EVPI bound and the net rule are Howard's.

## A closed-form instance: Pandora's box

Weitzman's search problem has the same net shape with an outside option in place of an action set. Opening a costly box when the best value so far is $v$ has net expected payoff $\mathbb{E}[(V-v)^+] - c$, and it is worth opening "when the expected upside exceeds the cost".[^c11] The reservation price is the $v$ at which that net is exactly zero, and it orders the boxes for search (see [[pandora-box-reservation-price]]). This is this note's reading, not the source's: the rule fixes what is worth inspecting only for boxes whose distributions are known and, in the classical statement, independent.

## Needs likelihoods, not only a posterior

Bayesian LLM-agent work states a sharper version of the input requirement. The work arXiv:2601.01522 argues that "Discriminative agents have no principled basis for deciding when to gather additional information".[^c4] Its Theorem 7 writes the VOI of new evidence $z$ with a predictive $p(z\mid x)=\sum_s p(z\mid s)\,p(s\mid x)$ and an updated posterior $p(s\mid x,z)\propto p(z\mid s)\,p(s\mid x)$; "Both require likelihood functions" that a discriminative model does not supply.[^c5] So no function of the current posterior and the acquisition cost can return VOI.

What survives is the input claim: the posterior $p(s\mid x)$ alone does not fix the distribution of a future observation, so VOI cannot be read off it. What does not follow is that a discriminative model can never estimate VOI. A model that also outputs a predictive distribution over $z$ supplies the missing piece, and the theorem's statement is about the posterior as the only input. This note's own limit on the number stands: without a written utility and action set, VOI is still a judgement.

## Confidence in the current answer is not a value of retrieval

A calibrated confidence estimates whether the present answer is correct; it
does not estimate what the next evidence step would add. In a controlled
replay of multi-hop QA with fixed evidence paths, one more step changed an
incorrect answer to a correct one in "17.7% of transitions", and the reverse
happened in "3.6% change a correct answer to an incorrect one".[^c6][^c7]
Helpful steps therefore outnumber harmful ones on average. That average does
not say which episodes benefit. The paper separates the two quantities:
"retrieval control requires estimating whether the next evidence step is
likely to help."[^c8] Calibration "does not turn confidence into a
value-of-information estimate."[^c9] Read against this note's own rule, the
commitment signal is a monitor of the current state, and the VoI of the next
step is a different object that needs its own estimate.

The paper's remedy is a pairing, not a single score: calibration "to make
commitment risk interpretable", with "a separate estimate of expected
information gain or utility" governing retrieval.[^c10] No VoI score is
computed in the paper; the claim is that one is required, not that it is
provided.

## Related

[[expected-information-gain]] · [[question-budgets]] · [[volume-removal]] · [[rate-distortion-theory]] · [[roc-curve]] · [[bayesian-experimental-design]]

[^s1]: biyik-2019
[^s2]: howard-1966
[^c1]: arxiv-2601-06407 — "If maxq NetVoI(q) ≤ 0, the expected utility gain from further communication"
[^c2]: arxiv-2601-06407 — "It, therefore, halts the conversation earlier than the"
[^c3]: arxiv-2601-06407 — "VoI matches or exceeds the best manually-tuned baselines in 18 of"
[^c4]: arxiv-2601-01522 — "Discriminative agents have no principled basis for deciding when to gather additional information"
[^c5]: arxiv-2601-01522 — "Both require likelihood functions"
[^c6]: doi-10-48550-arxiv-2608-26846 — "17.7% of transitions change an incorrect answer to a correct one"
[^c7]: doi-10-48550-arxiv-2608-26846 — "whereas 3.6% change a correct answer to an incorrect one"
[^c8]: doi-10-48550-arxiv-2608-26846 — "retrieval control requires estimating whether the next evidence step is likely to help"
[^c9]: doi-10-48550-arxiv-2608-26846 — "does not turn confidence into a value-of-information estimate"
[^c10]: doi-10-48550-arxiv-2608-26846 — "a separate estimate of expected information gain or utility governs retrieval"
[^c11]: doi-10-48550-arxiv-2608-20316 — "which is positive when the expected upside exceeds the cost"
