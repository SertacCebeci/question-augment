---
description: "Hiding answer words from a rationale lowers lexical overlap but not answer dependence; trajectory anchoring (entropy gap with vs without the answer) measures it; skeleton-first lowered all three."
aliases: ["answer anchoring metrics", "reverse chain-of-thought post-hoc rationalization", "semantic suppression failure", "structural skeleton-guided reasoning"]
sources: ["arxiv-2602-14469"]
---
# Lexical concealment versus trajectory anchoring

When a model writes a reasoning trace with the answer in view (reverse chain-of-thought generation, RCG), the trace can justify the answer instead of deriving it. The work frames the harm as a distribution gap: traces are produced under P(R | Q, A), but a student must reason under P(R | Q).[^c1] How much of that gap a trace carries is not visible in its words, so the paper measures it at three depths.

## Three levels of answer dependence

- **Lexical anchoring**: IDF-weighted recall of answer content words (those not already in the question) inside the trace. It is a surface indicator, and the authors say reducing it "does not guarantee improved downstream performance, because models may simply learn to obscure the same underlying dependence".[^c2]
- **Trajectory anchoring**: the mean per-token entropy drop caused by showing the answer, H(p(. | Q, R[:t])) minus H(p(. | Q, A, R[:t])). A high value means knowing the answer substantially reduces uncertainty at each step, so a trace with no answer words can still be strongly tethered to it.[^c3]
- **Probabilistic anchoring**: the clipped fraction of the answer's baseline surprisal removed by the whole trace, i.e. how recoverable the answer is from the reasoning.

## Why concealment instructions are the wrong lever

The intuitive fix is semantic suppression, a prompt such as "do not reveal the answer until the end". The paper claims it masks lexical overlap while raising trajectory anchoring, and borrows Wegner's ironic process theory: avoiding the answer requires tracking it.[^c4] Their summary: "The model rationalizes more subtly, but more heavily."[^c5] Lexical anchoring then rates a worse trace as better; the paper plots this against downstream accuracy (its Figure 1).

The proposed alternative, Structural Skeleton-guided Reasoning (SSR), first writes an abstract skeleton of functional tags (for example PLAN then INFR) and then writes the full trace guided by it, so structure is separated from answer content rather than forbidden access to the answer.[^c6] A distilled variant (SSR-D) trains the target model to produce skeleton then reasoning, and is reported to gain up to 10 points over suppression baselines.[^c7]

## Limits

- The suppression-specific "ironic increase" claim was weakened by the authors' own appendix. After a blind-baseline rerun, "SUP was essentially tied with NEU" on excess probabilistic anchoring (10.65 vs. 10.88) and neither suppression baseline raised total probabilistic excess.[^c8] The claim that suppression raises trajectory anchoring and the ironic-process mechanism should be read as a hypothesis (the appendix itself labels it a mechanistic hypothesis), not an established cause.
- A fourth, entropy-shape metric was retired because it tracked trace length, not answer dependence; trajectory-style metrics are only as good as their baseline calibration.[^c9]
- Evidence is synthetic reasoning-trace distillation for small Qwen models; whether the same dynamic holds when a person or model explains a known answer in dialogue is my inference, untested here.
- Entropy gaps need token-level access to the model, so they are unavailable for closed models.

## Related

- [[deferred-answer-exposure]] — same failure (rationalizing a revealed answer), fixed by ordering information rather than by a skeleton
- [[reasoning-masked-sycophancy]] — reasoning that looks independent while following an outside cue
- [[context-conditioned-oracle-anchoring]] — another case of a visible reference steering what is generated

[^c1]: arxiv-2602-14469 — "reasoning traces are generated under P (R | Q, A) with full answer visibility, but distillation"
[^c2]: arxiv-2602-14469 — "because models may simply learn to obscure the same underlying dependence."
[^c3]: arxiv-2602-14469 — "A high Atraj indicates that knowing the answer substantially"
[^c4]: arxiv-2602-14469 — "dependent on the answer the model is trying to suppress–"
[^c5]: arxiv-2602-14469 — "rationalizes more subtly, but more heavily."
[^c6]: arxiv-2602-14469 — "Rather than suppressing the answer, SSR decouples the structure of reasoning from its content."
[^c7]: arxiv-2602-14469 — "by up to 10 points over suppression baselines"
[^c8]: arxiv-2602-14469 — "SUP was essentially tied with NEU on Aexcess"
[^c9]: arxiv-2602-14469 — "Why we retired Aent ."
