---
description: "In multi-hop agent relays, message format barely matters for a strong relay but under a weak one it splits into an encoding toll and a drift benefit, and no format corrects errors."
aliases: ["format effect in agent relays", "encode-drift trade-off", "faithful not corrective channel"]
sources: ["doi-10-48550-arxiv-2607-09678"]
---
# Capability-gated format effect in relays

When one agent re-encodes another's message hop after hop, the message format does different work depending on how capable the relaying model is. The study behind this note passed briefs of twelve programmatic facts through six hops in five formats (free NL, precision-instructed NL, JSON, triples, key-value), scored against the generating facts rather than another model's output.[^c1]

## Mechanism

**Strong relay: format is nearly free.** With a strong API model every format was close to lossless (hop-6 QA recall at least 0.973), and the little loss that occurred sat at the first encoding step. The "telephone-game" collapse reported in earlier chain studies did not appear.[^c2] This is the reason the format choice looks free at the frontier.[^c3]

**Weak relay: two opposed mechanisms.** With a 1.5B relay, across-format dispersion of hop-6 recall grew 8.7 times (CI 5.3-15.5), from a 2.3-point range to 20.5 points.[^c4] The authors decompose the effect into two terms of opposite sign:

- An *encoding toll*. Turning a prose brief into a rigid scheme is hard for a weak model. Key-value (0.765) and JSON (0.800) paid large and statistically indistinguishable hop-1 tolls. Precision-instructed NL encoded best (0.962).[^c5]
- A *drift rate*. Once encoded, JSON drifted least by a wide margin, losing 4.7 raw points over hops 1-6. Free NL and triples lost 21.8 and 20.7.[^c6] Key-value paid the same toll as JSON but drifted about three times as much, which rules out survivor bias.[^c7]

The two terms flip the ranking in transit: JSON was fourth of five at hop 1 and second at hop 6 in 98% of bootstrap resamples.[^c8] Drift resistance is not a property of structure as such: line-oriented triples drifted like free prose.[^c9] The authors' reading is that a closed, fixed key set gives each fact a stable address that survives re-encoding, but with one fixed-schema format they could not separate this from nesting or JSON familiarity.[^c10]

**Faithful, not corrective.** A paired-fork test injected one wrong value mid-relay. Every format carried it forward (83-100% surface persistence at the final hop), and the true value in clean arms survived about as often, so faithfulness is direction-blind.[^c11] Injecting one wrong value caused no detectable collateral loss on the other eleven facts. In the authors' words, structure buys a faithful, error-localizing channel, not an error-correcting code.[^c12]

## Why it matters for asking and answering

The question a sender should ask about a handoff channel depends on the receiver. A format that costs nothing for a strong model can lose a fifth of the facts for a weak one. A rigid schema should not be trusted to repair a wrong premise it was handed (my inference: the receiver should be asked to verify a premise, because the channel will not).

## Limits

- "Capability" is a bundled contrast (model family, scale, quantization, serving stack all change), not a clean scale axis.[^c4]
- Only one fixed-schema format was tested, so the closed-key explanation is unseparated from nesting and pretraining familiarity.[^c10]
- The corpus is synthetic atomic facts in three domains; the injected error was a redundancy-free leaf, so no channel could have corrected it from in-message evidence. Correction is therefore not tested where redundancy exists.
- Weak tier n = 50 items, one weak model, and the paper is a single-author preprint.
- Whether the weak-tier pattern holds for mid-sized models was not measured.

## Related

- [[fact-attenuation]] — another measured loss of facts at agent handoffs, there across pipeline architectures, here across message formats.

[^c1]: doi-10-48550-arxiv-2607-09678 — "Ground truth is programmatic:"
[^c2]: doi-10-48550-arxiv-2607-09678 — "a strong relay is nearly lossless for every format (hop-6 QA recall ≥ 0.973)"
[^c3]: doi-10-48550-arxiv-2607-09678 — "the format choice looks free at the frontier and decisive below it"
[^c4]: doi-10-48550-arxiv-2607-09678 — "The across-format dispersion of hop-6 recall grows 8.7× (SD over"
[^c5]: doi-10-48550-arxiv-2607-09678 — "Rigid formats pay the largest encoding tolls"
[^c6]: doi-10-48550-arxiv-2607-09678 — "Json drifts least by a wide margin"
[^c7]: doi-10-48550-arxiv-2607-09678 — "Kv is a toll-matched control"
[^c8]: doi-10-48550-arxiv-2607-09678 — "Json starts fourth of five at hop 1 and finishes"
[^c9]: doi-10-48550-arxiv-2607-09678 — "Drift resistance is not a property of structure per se"
[^c10]: doi-10-48550-arxiv-2607-09678 — "we cannot separate the closed key set from nesting"
[^c11]: doi-10-48550-arxiv-2607-09678 — "Faithfulness is direction-blind"
[^c12]: doi-10-48550-arxiv-2607-09678 — "Structure buys a faithful, error-localizing channel, not an error-correcting code."
