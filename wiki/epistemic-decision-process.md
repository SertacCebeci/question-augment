---
description: "A finite-horizon belief-state decision process for multi-turn information seeking in which the optimal next action depends on the posterior over a hidden task variable, not just the visible history."
aliases: ["Epistemic Decision Process", "EDP"]
sources: ["nath-2026"]
---
# Epistemic decision process

> Selection in a multi-turn asking loop is a decision problem over beliefs:
> the same visible history can hide two different posteriors, and only a
> policy that reads the posterior can tell them apart.

## Definition / Mechanism

Nath & Krishnaswamy (2026) formalize an **Epistemic Decision
Process (EDP)** as $E=(Z,\rho_0,A,\Omega,O,u,T)$: a latent task variable
$z^\star$ drawn from prior $\rho_0$, an action space $A$, an observation
kernel $O$, an evidential utility $u$, and horizon $T$. At turn $t$ the
history $h_t=(a_0,o_0,\dots,a_{t-1},o_{t-1})$ induces a posterior belief
$b_t(z):=P(z^\star=z\mid h_t)$; the agent samples $a_t\sim\pi_\theta(\cdot\mid
h_t)$, receives $o_t\sim O(\cdot\mid z^\star,h_t,a_t)$, and updates
$b_{t+1}=\tau(b_t,h_t,a_t,o_t)$ via a Bayesian belief-update operator.[^c1]

A policy is **belief-agnostic** if it factors only through a
belief-independent interface state $s(h_t)$ — $\pi(a_t\mid h_t)=g(a_t\mid
s(h_t))$ — and **epistemically adaptive** if it can also depend on $b_t$:
$\pi(a_t\mid h_t)=f(a_t\mid s(h_t),b_t)$, strictly so if two histories share
$s(h_t)=s(h'_t)$ but differ in belief ($b_t\neq b'_t$) and the policy's
action distribution differs on them. Under a belief-state [[sufficient-statistic|sufficiency]]
assumption (the kernel and utility depend on $h_t$ only through $s(h_t)$ and
$b_t$), an optimal policy exists that is Markovian in the augmented state
$(s(h_t),b_t,t)$ (Proposition 3.1).[^c2]

**Theorem 3.2** (adaptive policies require epistemic credit) has two parts.
(i) Performance gap: for every depth $d\ge1$ there is an EDP $E_d$ with
horizon $d$ in which an epistemically adaptive policy achieves
$P(\text{success})=1$ while every belief-agnostic policy is bounded by
$P(\text{success})\le 2^{1-d}$ — the cost of ignoring belief compounds
exponentially with horizon. (ii) Estimator insufficiency: any trajectory-level
advantage estimator that is a function only of the total episode return $G$
has strictly positive irreducible error against the belief-conditioned
Bayesian advantage $A^\pi_B(h_t,a_t)$ whenever the same $G$ can arise from
belief-distinct decisions — sparse, end-of-episode reward cannot in general
recover per-turn epistemic credit.[^c3]

## Why it matters

For stall 2 (which axis first, how to score the next question), EDP names
the object that a selection criterion should be a function of: not the
surface history of questions and answers, but the posterior it induces. It
gives a formal reason a criterion computed from visible text alone — a
transcript summary, a fixed heuristic — can be arbitrarily bad relative to
one that reads the belief, and that this gap is not fixable by training on
whole-episode success alone.

## Transfer

| | |
|---|---|
| **In its home field** | Belief-state formulations (POMDPs, Bayes-adaptive MDPs) are standard in RL and control; EDPs are the source's own task-level specialization, distinct from BAMDPs in modelling uncertainty over a hidden *task* variable rather than transition/reward parameters or latent MDP identity |
| **Here** | A multi-turn LLM agent choosing questions/actions under uncertainty about a hidden target, with the belief made an explicit part of the decision-relevant state $(s(h_t),b_t,t)$ |
| **What survives** | The Markov-in-augmented-state existence result (Prop. 3.1); the exponential-in-depth separation between belief-aware and belief-agnostic policies (Thm 3.2(i)); the impossibility of recovering per-turn Bayesian advantage from episode return alone (Thm 3.2(ii)) |
| **What does not** | Exact belief tracking itself — the LLM instantiation never computes $b_t$ in closed form; it is approximated by a serialized text state summary, so the theorem's guarantees are about the idealized process, not about what any trained policy provably achieves |

## Limits

- Theorem 3.2(i) is an existence result ("there exists an EDP $E_d$..."),
  not a claim that every EDP separates this sharply; it establishes that the
  gap *can* be exponential, not a lower bound for the benchmark used to train
  [[echo-epistemic-credit]].
- The framework and its proofs are a single 2026 arXiv preprint's own
  formalization, not independently replicated; full proofs are stated to be
  in an appendix not read here.
- The LLM instantiation treats a serialized textual state summary as the
  encoding of $b_t$ — the theorem's belief-state sufficiency assumption
  (kernel and utility depend on history only through $s(h_t)$ and $b_t$) is
  not independently verified for that encoding.

## Related

[[echo-epistemic-credit]] · [[intervention-advantage]] · [[value-of-information]] · [[language-posterior]]

[^c1]: nath-2026
[^c2]: nath-2026
[^c3]: nath-2026
