---
description: "an LLM reads a player's latent trait profile from an opportunity-aware behavioral record instead of asking a questionnaire, then conditions generation on it."
aliases: ["opportunity-aware behavioral inference", "reading players from behavior", "behavior-driven player profile"]
sources: ["lu-2026"]
---
# Behavior-inferred player profile

> The constraint on "what kind of player is this" can come from watching, not
> asking — but only if the record keeps what the player *could* have done
> beside what they did.

## Definition / Mechanism

At each decision moment $t$ a player faces a state $s_t$ and a feasible choice
set $A_t$, and takes an action $a_t$; a session is recorded as
$\tau=\{(s_t,A_t,a_t)\}_{t=1}^T$ — an *opportunity-aware* record that keeps
declined choices on file beside taken ones, because behavior is generated
jointly by tendency and opportunity and the same latent trait produces
different behavior under a different $A_t$. A few-shot LLM reader $f$, with no
gradient updates, maps $\tau$ to a trait estimate $\hat\theta=f(\tau)$, using a
fixed in-context library of prior verified sessions; $\hat\theta$ then
conditions downstream content generation in place of a player's own answer to
a questionnaire.[^c1]

## Why it matters

Removing the declined-choice information from the record degrades exactly the
two trait dimensions whose expression depends on having an opportunity to
express them — Skill's [[recovery-postulate|recovery]] falls from ρ=.74 to .59 and Collector's from
.39 to .35 — while a dimension expressed continuously regardless of
opportunity (Dodge) is unchanged; the opportunity-aware design is load-bearing,
not decorative.[^c2]

In a twelve-participant pilot that held the downstream generator fixed and
varied only where the profile came from, levels built from the
behavior-inferred profile raised the LLM's own ability reading for every
participant relative to baseline, while levels built from a self-report
questionnaire scattered both above and below baseline.[^c3]

## Transfer

| | |
|---|---|
| **In its home field** | Evidence-centered design and stealth assessment (Mislevy, Steinberg & Almond 2003; Shute & Ventura 2013) treat task performance in an educational or game task as evidence for a latent competence model, scored by an explicit probabilistic measurement model built for that task. |
| **Here** | A latent four-dimensional trait vector inferred from a bullet-hell shooter's opportunity-aware decision log by a few-shot LLM reader with no task-specific probabilistic model and no gradient training. |
| **What survives** | The core move — treat behavior under a known choice set as the evidence, not a self-report of the trait — and the requirement that the record keep what was *not* chosen, without which "did not want it" cannot be told from "never had the chance." |
| **What does not** | ECD's explicit competency and evidence models (e.g. Bayes nets) are replaced here by an unaudited LLM prompt; nothing in this pipeline formalizes the reader's own evidentiary reasoning the way ECD requires. |

## Limits

Validated in one genre (a vertically scrolling shooter) with a game engine
that already enumerates the feasible choice set at every decision moment; the
method needs a translation layer to supply $A_t$ for any other game, and the
paper does not test one. The human-study comparison to a questionnaire is a
pilot at $n=12$, reported as directional and not significance-tested — the
ability-reading gap is not a confirmed effect. The profile is read once from
a [[calibration]] session and held fixed; nothing here evaluates traits that
drift as a player learns the game. Source lu-2026 is an arXiv preprint
(2026), not verified against a peer-reviewed venue.

## Related

[[constraint-as-information]] · [[value-of-information]] · [[ground-truth-admission-test]]

[^c1]: lu-2026 — "A session is therefore recorded as a sequence of opportunity-aware decision moments: τ = {(st , At , at )}Tt=1 , θ̂ = f (τ ), where f is the reader under evaluation, instantiated here mainly as a large language model."
[^c2]: lu-2026 — "Removing what could have been done from the records degrades precisely the two dimensions that depend on opportunities for expression—Skill falls from .74 to .59 and Collector from .39 to .35—while Dodge is unchanged."
[^c3]: lu-2026 — "Readings under the questionnaire-generated condition scatter in both directions relative to baseline, several participants falling below it, whereas the behavior-generated condition is higher for every participant."
