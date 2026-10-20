---
description: "A policy given the price of each clarifying turn and each answer word as input switches between asking, enumerating and answering to match those prices, trained by self-play."
aliases: ["steerable grounding policy", "SGP", "cost-conditioned clarification policy", "cost-steerable assistant"]
sources: ["arxiv-2512-04068"]
---
# Steerable clarification policy

A clarification policy is steerable when the price of its own conduct is an
input to it rather than a constant built into its training. In the self-play
setup of Berant, Chen, Fisch and colleagues the assistant receives two numbers:
α, the cost of asking one clarifying question, and β, the cost of each word it
generates. "The assistant receives as input the numerical cost of asking a
clarification question, and of generating each word."[^c1] The reward it is
trained on is accuracy minus those prices: "We want the answer to be accurate,
to minimize the number of turns, and to get short answers."[^c2] Accuracy is
token-level F1 against the gold answer; the turn term is α times the number of
clarifying questions; the length term is β times the words of the final answer.

## Mechanism

The assistant chooses among three actions: ask (#CLARIFY), answer (#ANSWER), or
enumerate candidate readings (#MULTI ANS). Which one earns the most reward
depends on the prices. The paper's own threshold argument is the mechanism in
one line: "if asking a clarification question can increase expected accuracy by
δ, and α < δ, then asking will yield higher" reward than answering directly.[^c3]
So the same ambiguous query has a different best action at a different α and β.
A policy that answers with a fixed habit is right at one price and wrong at the
others.

Training makes the dependence learnable. For each rollout the paper samples α
and β from small sets (α from {0, 2, 20}, β from {0.1, 0.7, 5.0}) and feeds
them to the assistant's prompt. The rollouts are then filtered and reduced to
the best action sequence for each price pair, by reinforced self-training
(ReST). "Crucially, different settings of α and β lead to different optimal
action sequences."[^c4] The policy is trained to pair each price with the
behaviour that is best at that price.

What the work reports: prompted baselines do not steer. "Even strong prompted
models fail to condition on cost coefficients, even when using chain-of-thought
prompting."[^c5] Models trained this way do: "models trained with SGP
appropriately condition on the provided cost coefficients,"[^c6] and the trained
policy "generalizes to numerical cost values unobserved during training."[^c7]

## Transfer

The threshold in the mechanism is the value-of-information comparison of
[[value-of-information]]: ask when the expected gain exceeds the price of asking.
What survives the transfer is that comparison with the price as a parameter. What
does not survive is any guarantee that a trained policy reaches the
value-of-information optimum. The paper gives no such bound, and the reward uses
token F1 as its stand-in for accuracy.

## Limits

The prices are given, not inferred. The paper says so: "cost coefficients can be
inferred from user preference data or feedback, which we leave for future work."[^c8]
So the work shows steering when the price is known, and says nothing about how a
deployed assistant would learn it.

The main results use one base model: "we use Gemma 2 9B (Google, 2024b) as our
baseline model for both the user simulator" and the assistant.[^c10] The user is
itself a model, instructed not to answer from its own knowledge. Real users were
not tested.

Only one clarifying question is allowed: "We limit the number of clarification
questions to 1."[^c9] With one ambiguity per query this leaves four action
sequences. Behaviour over several rounds of asking is outside what was measured.

I did not read the steerability metrics in full (the section after the setup),
so the claim that behaviour moves monotonically with the prices rests on the
abstract and the summary table, not on a checked curve. The "prompted models do
not steer" finding is also specific to the prompts in the paper's appendix.

## Related

- [[multi-turn-reward-clarification-training]] — trains on a turn penalty fixed at one value; the steerable policy makes the penalty an input.
- [[value-of-information]] — the closed-form ask-or-act threshold that the price parameter plugs into.
- [[regret-based-clarification-evaluation]] — scores costed clarification policies against a reference planner, but under one fixed cost weight.
- [[interpretation-averaged-action-selection]] — how the training labels for each price pair are chosen.
- [[multi-answer-enumeration]] — the third action, whose price is the per-word cost.

[^c1]: arxiv-2512-04068 — "The assistant receives as input the numerical cost of asking a clarification question, and of generating each word"
[^c2]: arxiv-2512-04068 — "We want the answer to be accurate, to minimize the number of turns, and to get short answers."
[^c3]: arxiv-2512-04068 — "if asking a clarification question can increase expected accuracy by δ, and α < δ, then asking will yield higher"
[^c4]: arxiv-2512-04068 — "Crucially, different settings of α and β lead to different optimal action sequences."
[^c5]: arxiv-2512-04068 — "even strong prompted models fail to condition on cost coefficients, even when using chain-of-thought prompting"
[^c6]: arxiv-2512-04068 — "models trained with SGP appropriately condition on the provided cost coefficients"
[^c7]: arxiv-2512-04068 — "generalizes to numerical cost values unobserved during training"
[^c8]: arxiv-2512-04068 — "cost coefficients can be inferred from user preference data or feedback, which we leave for future work"
[^c9]: arxiv-2512-04068 — "We limit the number of clarification questions to 1"
[^c10]: arxiv-2512-04068 — "we use Gemma 2 9B (Google, 2024b) as our baseline model for both the user simulator"
