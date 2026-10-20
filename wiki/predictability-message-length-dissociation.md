---
description: "In a Lewis referential game, required message length shrank as target repetition rose but grew, not shrank, as a hidden deterministic rotation became more predictable."
aliases: ["repeat-vs-rotation predictability result"]
sources: ["talebirad-2026"]
---
# Predictability–message-length dissociation

> Not every kind of predictability shortens the messages two communicating
> agents need: repetition did, a hidden deterministic cycle did not.

## Definition / Mechanism

Talebirad, Redman, Parsaee & Zaïane (2026) ran a Lewis
signaling game with instruction-tuned sender–receiver pairs, using
$L\in\{1,2,3\}$ symbols per round (so $3^L$ possible messages) and
recording $L_{\min}$, the smallest $L$ at which a pair reached
$\geq 0.85$ accuracy over the final ten of forty rounds.[^c1]

Under a **repeat** target process (next target copies the previous one
with probability $p$, else uniform-random), "mean Lmin fell monotonically
from 2.67 at p = 0 to 1.00 at p = 0.95" across two batches of three seeds.
Under a **shuffled rotation** process (targets follow a fixed hidden cycle
with probability $p$, else jump randomly), the opposite direction held:
"mean Lmin increased from 2.33 at p = 0 to 3.00 at p = 1" even though "the
sequence completed five cycles in forty rounds" at $p=1$.[^c2]

The authors caution that the repeat-condition result does not isolate
history's contribution: "episode history was never removed while learned
symbol mappings were preserved, these runs do not isolate history's
contribution."[^c3]

## Why it matters

A criterion that scores "how predictable is the target" as one number
would treat these two conditions alike; the measured message lengths moved
in opposite directions. Repetition let agents shrink messages (arguably by
leaning on retained history), while a structurally predictable but
non-repeating cycle did not — evidence that *statistical predictability*
and *history-exploitable predictability* are not interchangeable inputs to
a memory-vs-communication trade-off such as the
[[remembering-signaling-frontier]].

## Limits

- Preliminary by the authors' own framing: one model family
  (instruction-tuned Gemma), three seeds per batch, forty rounds per run,
  two batches for the repeat condition and none reported as a rotation
  replication set beyond the three seeds shown.
- The repeat-condition result is explicitly not attributed to history use
  alone — symbol-mapping learning is confounded with any memory effect,
  per the caveat quoted above.
- The two target processes differ in rule complexity and number of
  distinct targets, so the direction reversal cannot yet be attributed
  specifically to "repetition versus structure" as opposed to other
  differences between the two processes.
- `replicated: false` — the paper itself calls this a preliminary result
  awaiting the registered follow-up experiments it proposes.

## Related

[[remembering-signaling-frontier]] · [[value-of-information]] · [[mutual-information]]

[^c1]: talebirad-2026 — "We recorded the smallest L whose pair achieved accuracy ≥ 0.85 over the final ten rounds as Lmin (chance = 0.25)."
[^c2]: talebirad-2026 — "mean Lmin fell monotonically from 2.67 at p = 0 to 1.00 at p = 0.95."
[^c3]: talebirad-2026
