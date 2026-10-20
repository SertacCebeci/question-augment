---
description: "The achievable-region formalism trading an agent's memory rate against its peer-communication rate at a fixed task loss; its Pareto-efficient edge is the remembering-signaling frontier."
aliases: ["remembering-signaling frontier", "memory-communication rate region"]
sources: ["talebirad-2026"]
---
# Remembering-signaling frontier

> Given a fixed task and decision rule, how much of the information a
> bounded agent needs should come from its own retained history versus a
> peer's message? Talebirad, Redman, Parsaee & Zaïane (2026)
> define the achievable region of memory-rate/communication-rate pairs that
> reach a target loss, and name its efficient edge the frontier.

## Definition / Mechanism

Fix a task $T$ (instance distribution and loss) and a decoder $A$ mapping
the decision maker's current observation plus supplied representations to
the task output. Source rules `src` state which of the decision maker's
past records and which peer observations an encoding scheme may use; each
scheme $\pi$ encodes allowed history as $M_\pi$ and allowed peer
observations as a message $C_\pi$, either possibly empty.[^c1]

The achievable memory–communication rate region is
$$R^{MC,\varepsilon}_A=\{(b_m,b_c)\in\mathbb{R}_+^2:\exists\pi\in\Pi_A(src),\ D_A(\pi;T)\le\varepsilon,\ R_m(\pi)\le b_m,\ R_c(\pi)\le b_c\}$$
Its Pareto-efficient lower boundary — where reducing either rate forces the
other up or breaks the loss bound — is the **remembering–signaling
frontier**; given per-bit costs $c_m, c_c$, the point minimizing
$c_m b_m + c_c b_c$ lies on it.[^c2]

The paper's own hypotheses, not yet confirmed at scale: holding the
maximum loss reduction obtainable from history fixed, an agent needs fewer
message bits from a peer when its **usable-history gain** (the loss
reduction from adding the history representation, measured before the
peer message is added) is larger; and curves obtained by varying memory
rate alone and message rate alone should predict the **crossover** — the
point where the least-cost split moves from favoring messages to favoring
memory as targets grow more repetitive or stable.[^c3]

## Why it matters

This gives "should the agent ask a peer or rely on what it already
retained" a formal budget trade-off rather than a binary choice: asking
(signaling) and remembering are substitute rate resources against the same
loss target, each priced by its own per-bit cost.

## Limits

- The region is defined for a fixed decoder, task, source-rule family and
  scheme family chosen in advance; changing any of these changes the
  region — these are stated inputs, not properties the frontier predicts.
- The crossover and usable-history-gain claims are hypotheses to be
  tested, not established results: the paper reports only a small
  preliminary referential-game experiment
  ([[predictability-message-length-dissociation]]) and explicitly defers
  estimating the frontier itself to future work.
- No shape claim (convexity, monotonicity) is made or proved for
  $R^{MC,\varepsilon}_A$ in the source; unlike [[rate-distortion-theory]]'s
  $R(D)$, that property is open here.

## Related

[[rate-distortion-theory]] · [[predictability-message-length-dissociation]] · [[value-of-information]] · [[bounded-rationality]]

[^c1]: talebirad-2026 — "Each π ∈ ΠA (src) describes how allowed history is retained and encoded as Mπ , and how allowed peer observations are encoded as a message Cπ . Storing Mπ remotely still counts toward the memory rate, and the earlier transmission of a cached Cπ still counts toward communication. Either encoded output may be empty, allowing a scheme to use one source, both sources, or neither."
[^c2]: talebirad-2026 — "The Pareto-efficient lower boundary contains allocations where reducing either rate would require increasing the other or exceeding the loss threshold. We call this boundary the remembering–signaling frontier. Let cm , cc > 0 be the respective per-bit costs of memory and communication. Any region point minimizing cm bm + cc bc lies on the frontier."
[^c3]: talebirad-2026 — "Among conditions where it gains equally from history, we hypothesize that the learned decoder will need fewer message bits to reach the target loss when its usable-history gain is larger."
