---
description: "Stripping symbol names from binaries costs weaker agents far more than stronger ones, while optimization and linking barely matter, suggesting names serve as lexical anchors for analysis."
aliases: ["symbol-name reliance", "lexical anchors in binary analysis", "stripped-symbol sensitivity"]
sources: ["doi-10-48550-arxiv-2608-11469"]
---
# Symbol-name anchoring

Binary analysis has classical obstacles: compiler optimization and static linking obscure the code a reader must interpret. A benchmark that varies these build factors separately finds that, for language-model agents, the classical obstacles mostly do not register, while removing symbol names does.[^c1] "Optimization and linking have little effect while stripping symbols is costly."[^c2]

The effect is uneven across capability. Among the unhardened instances, weaker models lose much more to stripping than stronger ones: "Weaker models are thus far more sensitive to symbol" stripping.[^c4] GPT-6-Astra, the strongest model, shows no loss to stripping (5.39 vs. 5.36).[^c8] The authors' reading is that these agents "lean on lexical anchors more than on instruction-level reasoning."[^c3] A name tells the agent what a routine is for before any semantics has been recovered, so the agent can skip the recovery step. The authors draw the contrast with people explicitly: "The failure modes also differ from those of human analysts."[^c5]

The contrast is specific to names. Protection is a different kind of obstacle: "Protection is the one classical obstacle that transfers," and hardening cuts GPT-5.6-sol's score "from 4.69 to 2.50" on the same build.[^c7][^c9] So the pattern is not that agents find binary analysis hard in general; it is that some agents depend on names that hardening does not remove.

## Limits

- The lexical-anchor account is the authors' suggestion, marked by "suggesting." The work has no ablation that separates names from other readable content such as strings, so the mechanism is their inference (my reading agrees with it but does not test it).
- Stripping is measured on unhardened builds. Protected presets also strip symbols, since the "obfuscation and stripping layers" are part of the shared baseline of every preset,[^c6] so the protected results cannot be read as a pure stripping effect.
- The comparison to human analysts is not measured here. The human side comes from the classical-RE literature the authors cite, not from a human baseline on this benchmark.
- The figures come from one benchmark, eleven models, and a capability ordering the authors define. The weaker-model result depends on that ordering.

## Related

- [[option-matching-shortcut]] — a surface-matching shortcut that replaces deduction in reasoning models, the same pattern of cue over derivation in a different setting
- [[answer-option-surface-cue]] — surface features of wording that answerers pick up instead of the content
- [[benchmark-target-scale]] — the same benchmark's finding on program size, which bears on how much a shortcut can carry

[^c1]: doi-10-48550-arxiv-2608-11469 — "barely register, whereas stripping symbols is costly"
[^c2]: doi-10-48550-arxiv-2608-11469 — "optimization and linking have little effect while stripping symbols is costly"
[^c3]: doi-10-48550-arxiv-2608-11469 — "lean on lexical anchors more than on instruction-level reasoning"
[^c4]: doi-10-48550-arxiv-2608-11469 — "thus far more sensitive to symbol"
[^c5]: doi-10-48550-arxiv-2608-11469 — "The failure modes also differ from those of human analysts"
[^c6]: doi-10-48550-arxiv-2608-11469 — "and the obfuscation and stripping layers"
[^c7]: doi-10-48550-arxiv-2608-11469 — "Protection is the one classical obstacle that transfers"
[^c8]: doi-10-48550-arxiv-2608-11469 — "5.39 vs. 5.36"
[^c9]: doi-10-48550-arxiv-2608-11469 — "from 4.69 to 2.50"
