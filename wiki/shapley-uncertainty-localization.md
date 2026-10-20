---
description: "Attributes an LLM input's total aleatoric uncertainty to individual ambiguous spans via Shapley values, so a clarification can target the highest-attribution span instead of the whole input."
aliases: ["ShaQ", "Shapley-based input uncertainty Quantification", "span-level uncertainty attribution"]
sources: ["lee-2026-localizing"]
---
# Shapley uncertainty localization (ShaQ)

> A scalar [[efe-planning-as-variational-inference|ambiguity]] score says an input is unclear; ShaQ says *which part*
> of it is, by pricing each ambiguous span's share of the total uncertainty
> as a Shapley value — which axis to ask about first, read off a coalition
> game instead of guessed.

## Definition / Mechanism

Lee, Yoon & Lee (2026) extract a set of ambiguous
spans $S=\{s_1,\dots,s_n\}$ from an input $x$ (contiguous, minimally
coherent phrases admitting multiple readings) and treat them as players in
a cooperative game. A coalition $A\subseteq N$ of spans has value equal to
the [[mutual-information|mutual information]] its joint clarification would carry about the
answer: "the value function v : 2N → R assigns to each coalition A ⊆ N the
mutual information between Y and the joint clarifications of the spans
indexed by A"[^c1], and each span's marginal contribution to any coalition
reduces to a conditional mutual information: "For any coalition A ⊆ N \
{k}, the marginal contribution of span sk satisfies v(A ∪ {k}) − v(A) = I(Y
; Ck | x, CA)" (Theorem 4.1). The Shapley value $\phi_k$ is the
size-weighted average of this marginal contribution over every coalition
$A\subseteq N\setminus\{k\}$ — the standard Shapley weighting from
cooperative game theory, not a new weighting scheme.

Because exact evaluation needs the [[conditional-entropy|conditional entropy]] of every coalition,
the paper computes it with a bottom-up marginalization algorithm that
treats each unclarified span as a variable integrated out of the
already-sampled joint-clarification pool, rather than re-querying the
model per coalition; this is what keeps every marginal contribution
non-negative (their Property 4.1) instead of the sign artifacts a naive
per-coalition LLM call would introduce.[^c1]

The resulting attributions satisfy the Shapley efficiency axiom: "the sum
of local span-level attributions exactly recovers the global input-level
aleatoric uncertainty. Together with Theorem 4.1, this establishes our
approach as a generalization of prior input-level uncertainty estimation
(Hou et al., 2024)" — the prior work's single aggregate aleatoric-uncertainty
score is recovered as the sum $\sum_k \phi_k$, with ShaQ adding the
per-span split.[^c2]

On ambiguity-detection benchmarks, "ShaQ and ShaQ (Max) consistently
achieve strong performance across different backbones and evaluation
metrics, demonstrating the robustness of our uncertainty localization
framework. In particular, on AmbiEnt, where ambiguity often involves more
complex and compositional phenomena, ShaQ and ShaQ (Max) outperform
existing baselines by a substantial margin in AUROC and AUPRC" — against
[[semantic-entropy|semantic entropy]], sample-diversity/repetition, self-consistency, Deep
Ensembles, Ask4Conf-D and the leave-one-out ablation of ShaQ itself, on
AmbigQA and AmbiEnt (Table 1).[^c3]

## Why it matters

For stall 2 — which axis to ask about first — ShaQ turns "the input is
ambiguous" into a ranked list of spans, each carrying a defensible share of
the measured uncertainty; the top-$\phi_k$ span is the one a targeted
clarifying question should address first, in place of re-asking the whole
input or picking a span by hand.

## Transfer

| | |
|---|---|
| **Home field** | cooperative game theory (Shapley 1953) and SHAP feature attribution (Lundberg & Lee 2017): a fixed set of features/players, a model's scalar prediction as the payoff, exact or sampled Shapley values over a tractable coalition space |
| **Here** | the "players" are LLM-extracted ambiguous spans of a natural-language query, not predefined features; the payoff is an information-theoretic quantity — mutual information between the answer and a coalition's clarification — not a model's output value |
| **What survives** | the efficiency axiom (attributions sum exactly to the total value) and the weighted-marginal-contribution formula that defines $\phi_k$ |
| **What does not** | SHAP's fixed, canonical feature set — spans are not a canonical decomposition of text and depend on the Localizer module's output; exact per-coalition evaluation, replaced by the paper's own bottom-up marginalization approximation to keep contributions non-negative |

## Limits

- The bottom-up marginalization step that makes contributions non-negative
  assumes the sampled premises of unclarified spans are independent of
  those already fixed — an assumption the paper states, not something it
  tests directly against inputs where spans are strongly dependent beyond
  the two- and three-span running examples shown.
- Span identification is itself an LLM call (the Localizer); a span that
  the Localizer misses gets no attribution at all, and natural language has
  no canonical span decomposition to check it against.
- Evaluated as an ambiguity-*detection* signal (AUROC/AUPRC/F1 against
  ground-truth ambiguity labels on AmbigQA, AmbiEnt, and a qualitative
  MediTOD case study) rather than as an online policy that asks about the
  top span and re-measures; whether the ranking it produces is the same
  ranking a live clarification loop should follow is not separately tested
  here.

## Related

[[clarification-only-aleatoric-uncertainty]] · [[semantic-entropy]] · [[mutual-information]] · [[uncertainty-decomposition]]

[^c1]: lee-2026-localizing — "the value function v : 2N → R assigns to each coalition A ⊆ N the mutual information between Y and the joint clarifications of the spans indexed by A"
[^c2]: lee-2026-localizing
[^c3]: lee-2026-localizing — "ShaQ and ShaQ (Max) consistently achieve strong performance across different backbones and evaluation metrics, demonstrating the robustness of our uncertainty localization framework. In particular, on AmbiEnt, where ambiguity often involves more complex and compositional phenomena, ShaQ and ShaQ (Max) outperform existing baselines by a substantial margin in AUROC and AUPRC."
