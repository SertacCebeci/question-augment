---
description: "If what a source said can be carried with unforgeable proof of who said it, Lamport, Shostak & Pease (1982), *TOPLAS* 4(3), 382–401, §4."
aliases: ["signed-message agreement", "SM(m) agreement"]
sources: ["lamport-1982"]
---
# Authenticated agreement

> If what a source said can be carried with unforgeable proof of who said it,
> the number of sources stops being the binding constraint — attribution is
> spendable in place of redundancy, and it is bought with a different, weaker
> guarantee.

## Definition / Mechanism

Lamport, Shostak & Pease (1982), *TOPLAS* 4(3), 382–401, §4.[^s1]

To the oral-message assumptions A1–A3 (`byzantine-agreement-bound` (draft dropped)) add

> **A4.** (a) A loyal general's signature cannot be forged, and any alteration
> of the contents of his signed messages can be detected. (b) Anyone can verify
> the authenticity of a general's signature.

No assumption is made about a *traitor's* signature: traitors may forge each
other's, i.e. collude (p. 391).

**Algorithm SM($m$).** The commander signs and sends his value. A lieutenant
who receives a properly signed order not already in his set $V_i$ adds it,
appends his own signature, and relays it. When no more messages can arrive he
obeys $\mathrm{choice}(V_i)$, where $\mathrm{choice}$ of a singleton is its
element and of the empty set is the default order.

**Theorem 2 (p. 393).** For any $m$, SM($m$) solves the Byzantine Generals
Problem if there are at most $m$ traitors — **for any number of generals**.
(The problem is vacuous below $m+2$.) The $3m+1$ threshold is gone; three
generals with one traitor now have a solution, because the traitorous
commander's two contradictory orders both arrive carrying his signature and
both lieutenants therefore hold the same two-element $V_i$ (Fig. 5).

**Connectivity too.** With oral messages the communication graph must be
$3m$-regular (Theorem 3). With signatures, **Theorem 4 and its corollary
(p. 396)**: if the subgraph of loyal generals is connected, SM($n-2$) solves
the problem for $n$ generals regardless of the number of traitors; more
generally SM($m+d-1$) works when that subgraph has diameter $d$. Signatures buy
off both resources the oral bound charges for — headcount and direct access.

**What it costs instead.** Every message carries the whole chain of
signatures, and a lieutenant relays each new order to everyone not already on
the chain; paths run to length $m+1$. A4(a) "can never be guaranteed, since
$S_i(M)$ is just a data item" (p. 400) — a faulty processor can generate it by
chance or by cryptanalysis, and the design goal is only to make that
probability small. And because a signature is easy to reproduce once seen, the
same message must never be signed twice: sequence numbers are required when
SM($m$) is used repeatedly (p. 400).

## Known as

| Field | Name there | Match |
|---|---|---|
| Distributed computing | signed-message agreement / the SM($m$) result | exact — the paper's own naming (§4, Theorems 2 and 4) |
| Distributed computing | authenticated Byzantine agreement | close — names the *problem setting* (agreement when relayed claims carry signatures), of which this theorem is the founding result; other results in that setting are separate objects, so the name is not carried as an alias of this note |
| Distributed computing | **unforgeable signature (A4)** | *not this concept* — the assumption the result is bought with, not the result |
| Distributed computing | **Byzantine broadcast with authentication**, Dolev–Strong | *not this concept* — a later protocol in the same setting, with its own round and message bounds that this note has not read; logged as a separate topic |

## Why it matters

1. **Provenance and redundancy are exchangeable.** The same problem, the same
   adversary, the same channel — and the threshold moves from "more than three
   times the bad sources" to "no constraint on count at all", purely because
   each relayed claim carries verifiable authorship. For an asker this means a
   thin, well-attributed source set can be worth more than a large anonymous
   one, and that the choice between "get more sources" and "get better
   provenance" is a real substitution and not two ways of saying *be careful*.
2. **It identifies precisely what attribution has to do.** Not "the source is
   reputable" — A4 is about the *message*: that its author cannot be faked and
   its content cannot be altered undetected in relaying. A citation that can be
   checked against the cited text does this; a claim of the form "X says …"
   that cannot be resolved to X's words does not.
3. **A traitor becomes detectable rather than merely survivable.** In Fig. 5
   the lieutenants learn the commander is a traitor, because two different
   orders bear his signature. Under oral messages the same scenario is
   indistinguishable from a loyal commander. Signed answers convert a
   contradiction into evidence about *which* source is bad — the input a
   culprit-selection step needs ([[truth-maintenance-system]]).
4. **The guarantee changes kind.** The oral bound is combinatorial and holds
   absolutely under its assumptions; this one holds only as far as forgery is
   improbable. Buying redundancy with attribution therefore converts a
   counting guarantee into a cryptographic-style one.

## Transfer

| | |
|---|---|
| **Home field** | processors relaying a value, an adversary that may lie arbitrarily and collude, and a signature scheme such that a nonfaulty party's signature cannot be produced by anyone else and can be verified by everyone |
| **Here** | an asker receiving claims that have passed through other parties — citations, quotations, retrieved passages, summaries by an intermediate agent — and deciding whether more sources or better attribution is the thing to spend on |
| **What survives** | the substitution itself: verifiable authorship of a *relayed* claim removes a headcount requirement and a connectivity requirement that are otherwise both binding; and the operational content of "attribution" — unfakeable author plus tamper-evident content, per message, not per source |
| **What does not** | the guarantee. Natural-language provenance has no A4: a quotation can be faithfully attributed and still be a selective excerpt, and nothing in the theorem covers a source that signs a true report of a false thing it was told. The paper's own remedy for A4(a) is a probability made small by cryptography, which has no counterpart for prose; and nothing in the wiki measures how often a chain of attributed claims in practice fails A4(a) or A4(b) |

## Limits

- This note's claim — that attribution substitutes for source count — is a
  claim about **relayed** claims, and rests on the theorem's setting where the
  original assertion is a fixed message. It says nothing about how many sources
  to consult when each is queried directly and independently.
- A4 is the whole load. The authors themselves state that property (a) cannot
  be guaranteed and is only made improbable (p. 400); an asker working in
  natural language has no analogue of the signature function at all, so the
  transfer above is a statement about what *would* be needed, not a report that
  it is available.
- Signatures do not touch correctness. As with the oral case, if the commander
  is a traitor the loyal parties agree on whatever he signed; agreement about
  provenance is not agreement about the world.
- The substitution is read off this one paper's two theorems. Later results in
  the same setting may price authentication differently, and this note does not
  speak for them.
- The cost side (message size growing with the signature chain, sequence
  numbers against replay) is stated from the paper's §6–7 and has no measured
  counterpart here for any question-asking system.

## Related

`byzantine-agreement-bound` (draft dropped) · `flp-impossibility` (draft dropped) · [[novice-expert-problem]] · [[truth-maintenance-system]] · [[tacit-knowledge]]

[^s1]: lamport-1982
