---
description: "Gary Klein, *Performing a Project Premortem* (HBR, September 2007): a team The classic risk question — \"what could go wrong?\" — draws weak answers."
aliases: ["Klein's premortem"]
sources: ["klein-2007", "mitchell-1989"]
---
# Premortem

> Gary Klein, *Performing a Project Premortem* (HBR, September 2007): a team
> is told "a year has passed and the project was a total disaster — **why?**"
> and asked to write down the reasons.

## Mechanism

The classic risk question — "what could go wrong?" — draws weak answers. A[^s1][^s2]
premortem takes failure as **given** and asks for an explanation. Klein's
procedure is a group protocol: every member independently writes plausible
causes of the stipulated failure before any are shared, which also lowers the
cost of dissent inside the team.

The cognitive effect the protocol exploits is *prospective hindsight*, studied
by Mitchell, Russo & Pennington (1989): stipulating that an event has already
occurred, rather than that it might occur, raises the **number** of reasons
people generate for it. Their own account attributes the shift to the
*certainty* of the outcome rather than to past tense as such.

## Known as

| Field | Name there | Relation |
|---|---|---|
| decision methods / management | Klein's premortem | exact — Klein's own name for this protocol |
| behavioural decision research | prospective hindsight | **close, not exact** — the measured cognitive effect (more causes generated under a stipulated outcome), not this group procedure. Mitchell et al. measured reason counts in individuals; Klein specifies a facilitated team protocol. They are different objects and the effect result does not transfer to the protocol's outcome. |

## Why it matters

For an asking agent the premortem is a **conditioning move** on generation:

```text
"What could go wrong?"    →  failure treated as unlikely, generation is weak
"It DID fail. Why?"       →  failure stipulated; generation is drawn from
                             that region
```

In LLMs the same prompt shape is available directly, and plausibly stronger,
since the stipulation enters the context that conditions the next token — the
clean form of what a "persona" prompt gropes at.

## Transfer

| | |
|---|---|
| In information theory | conditioning on $Y=y$ presumes a joint distribution over defined random variables, $y$ an event of known probability in a specified sample space; $H(X\mid Y)\le H(X)$ is then a theorem ([[conditional-entropy]]). |
| Here | the "observation" is a *stipulated* future failure that has not occurred and carries no measure; the "variable" is an open-ended set of causes with no enumerated support. |
| What survives | the qualitative claim that conditioning moves the generating distribution, so what is sampled changes. |
| What does not | any quantitative statement — no $H(X\mid Y)$ reduction can be computed or claimed, because neither $X$ nor $Y$ is a defined random variable here, and the stipulated event is counterfactual rather than observed. |

## Generalisation: conditional generation (conjecture)

*This wiki's inference, not a tested result.* If the operative ingredient is
the stipulated outcome rather than failure specifically, the same move should
work in any direction:

```text
"This design survived 10 years. Why did it hold?"
"This feature was never used. Why?"
"A security researcher broke this. How?"
```

Each would generate questions on a different axis. See [[metamorphic-probes]].

## Limits

- The prospective-hindsight effect (Mitchell, Russo & Pennington 1989) `[?]`
  — marked unverified in `meta/sources.md`, see there — is a lab finding on
  the *quantity* of causes generated. The quality of the causes was not
  scored, and nothing in it speaks to decision quality.
- Klein (2007) is a practitioner article describing a protocol; it reports no
  controlled outcome evaluation of the premortem.
- The conditional-entropy reading is an analogy and carries no numbers; see
  `## Transfer`.
- The generalisation from failure-conditioning to arbitrary conditioning
  (success, non-use, adversary) is this wiki's own inference — conjecture.
  Mitchell et al. tested only the stipulated-outcome framing.
- "Probably even stronger in LLMs" is asserted here, untested (conjecture).

## Related

[[conditional-entropy]] · [[metamorphic-probes]] · [[dialectic-red-team]] · [[unknown-unknowns]]

[^s1]: klein-2007
[^s2]: mitchell-1989
