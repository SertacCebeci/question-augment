---
description: "A CAP-theorem-style conjecture — under semantic underdetermination an LLM cannot jointly guarantee strong correctness, strict non-bias, and decisive utility."
aliases: ["CAP-like trilemma for LLMs", "correctness-non-bias-utility trilemma"]
sources: ["venugopal-2026"]
---
# Correctness–non-bias–utility trilemma

> Borrowing the CAP theorem's shape: when the prompt's premises do not pick
> out one answer, an LLM cannot be simultaneously exactly right, uncommitted
> to any unstated preference, and decisive.

## Definition / Mechanism

Venugopal (2026) defines a prompt $x$ as **semantically
underdetermined**, $D(x)$, when its premise-compatible answer set $S_x$ has
$|S_x| > 1$ — the facts $F_x$ do not entail a unique answer. Strong
correctness requires $F_x \models y$; strict non-bias forbids the model from
preferring one answer over another unless $F_x$ itself orders them; decisive
utility requires a concrete answer rather than a refusal or clarification
request. The central conjecture is that correctness, non-bias, and utility
form a trilemma under semantic underdetermination.[^c1]
For the two-candidate case the paper proves the conflict directly: a decisive
answer must be one of $\{a_1,a_2\}$, non-bias forbids the answer being either
without a premise-supported ordering, and correctness fails for both because
neither is entailed — so a criterion $\theta$ must be added, and if $\theta$
is not supplied or justified it functions as bias.

## Why it matters

A refusal or clarification request $r$ satisfies correctness and non-bias
($C_{strong}(r,x)=1$, $NB_{strict}(r,x)=1$) at the cost of decisiveness
($U_{decisive}(r,x)=0$). This is analogous to a consistency-preserving
distributed system under CAP.[^c2]
The paper's practical response is not to eliminate the trade-off but to make
it explicit: answer directly when $|S_x|=1$; otherwise ask for a criterion,
answer conditionally on each plausible criterion, or answer with the
criterion stated. This policy does not eliminate the trilemma. It makes the
trade-off explicit.[^c3]

## Transfer

| | |
|---|---|
| Home field | distributed systems: the CAP theorem, proved for an asynchronous network model under a network-partition stress condition |
| Here | LLM response generation, with semantic underdetermination ($\lvert S_x\rvert>1$) standing in for partition |
| What survives | the logical form "stress condition $\Rightarrow$ not all three properties together"; refusal read as the correctness-preserving default under stress, exactly as a partitioned node preserving consistency by refusing |
| What does not | CAP's impossibility proof (an asynchronous-network argument); here the trilemma is proved only for the worked $\lvert S_x\rvert=2$ case and stated as a conjecture for the general case, with no proof for larger or continuous answer spaces |

[^c4]

## Limits

- The paper proves the conflict only for a two-candidate answer set; the
  general-$S_x$ case is asserted as a conjecture, not derived, so the claim
  this note rests on (the trilemma holds for arbitrary underdetermined
  prompts) is unproven outside that worked case.
- "Bias" is defined maximally broadly — any unsupported selection
  preference, not only demographic or social bias — so results here do not
  transfer to a fairness benchmark's measured bias rate without translation.
- Single-author, purely formal paper with no experiment on an actual model;
  nothing here shows a deployed LLM's refusals track $D(x)$ rather than
  some other cause.

## Related

[[abstention]] · [[clarification-request]] · [[value-of-information]] · [[possible-worlds]]

[^c1]: venugopal-2026 — "The central conjecture is that correctness, non-bias, and utility form a trilemma under semantic underdetermination."
[^c2]: venugopal-2026 — "This is analogous to a consistency-preserving distributed system under CAP."
[^c3]: venugopal-2026 — "This policy does not eliminate the trilemma. It makes the trade-off explicit."
[^c4]: venugopal-2026 — "The CAP theorem is a foundational result in distributed systems."
