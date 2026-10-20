---
description: "Self-play's own reverse question-construction trace, harvested for free during task generation, is fed only to a teacher so a search agent's student copy trains under dense token-level guidance."
aliases: ["QCP", "question construction path", "π-Play", "pi-Play", "Privileged Information Self-Play"]
sources: ["arxiv-2604-14054"]
---
# QCP-guided self-distillation

> The examiner that builds a self-play question by chaining hops backward
> from an answer already leaves a full trace of how it did so; giving that
> trace only to a teacher copy of the student turns a sparse pass/fail
> reward into dense, token-level supervision, for free.

## Definition / Mechanism

An examiner agent builds each training question by starting at a random
document, picking an entity as Hop 1, and repeatedly issuing search
queries to chain forward to a further hop, stopping at hop $n$ to emit
the final question $q$ and answer $o^\star$. The sequence of searches and
reasoning it used to do this — the question construction path $c$ — is
recorded as a side effect of task generation: "self-play naturally
produces a question construction path (QCP) during task generation, an
intermediate artifact that captures the reverse solution process."[^c1]
Every prior self-play framework discards $c$ once $(q, o^\star)$ is
emitted; QCP-guided self-distillation keeps it as privileged information.

Three same-scale copies of one base LLM — examiner, teacher, student —
are trained together. The student sees only $q$ and is optimized with
GRPO on outcome reward, exactly as in ordinary self-play. A teacher copy,
kept as an EMA of the student's weights, is additionally conditioned on
$c$ and rolls out its own trajectory; the student is then pulled toward
the teacher's token distribution along its own rollout with a per-token
KL distillation term, added to the GRPO loss. Because the teacher's edge
over the student is informational (it is told $c$) rather than a matter
of capacity (it is the same size), its guidance is reliable without a
larger external model: "the construction path $c$ is only visible to
the teacher model, ensuring that the teacher can produce reliable
guidance while the student learns to solve the task without direct
access to privileged information."[^c2]

The examiner itself is trained by a moderate-difficulty reward from the
student's own pass rate, so the whole loop is a closed, three-way
curriculum with no external data or labels. An ablation isolates what
makes $c$ work as privileged context: replacing it with the
ground-truth answer alone collapses the teacher to uselessness, while a
QCP truncated to half its length still beats the ground truth
substantially — "GT contains only the final answer and provides little
information about the underlying logic used to construct the question,
making it difficult for the teacher to provide effective guidance to
the student. In contrast, the full QCP achieves the best performance,
while Partial QCP performs second best."[^c3]

## Why it matters

The gain is not only accuracy but a change in how the trained agent asks:
compared against self-play baselines trained on the same data-free
recipe, the QCP-distilled student answers more questions correctly while
issuing fewer, less redundant search queries — "compared with
conventional self-play methods such as SQLM* and Dr.Zero, π-Play achieves
higher accuracy with fewer search actions, indicating more efficient
behavior. The same trend holds for query redundancy."[^c4]

Dense, per-token supervision on *which* search to issue next, not just
whether the episode ended correctly, is what a sparse outcome reward
cannot supply; QCP supplies it without curated demonstrations, human
feedback, or a stronger teacher model, and at a training-time cost the
paper reports as "π-Play introduces only a small per-step training
overhead of 4.3% relative to Dr.Zero."[^c5]

## Transfer

| | |
|---|---|
| **Home field** | Privileged-information distillation and on-policy distillation, where a teacher sees strictly more than the student by design (an oracle label, a human hint, a bigger model). |
| **Here** | The privileged signal is not supplied — it is the by-product left over from generating the training question itself, so no one has to author or curate it. |
| **What survives** | The teacher/student split by information, not by capacity, and the reverse-KL/token-level distillation machinery of prior self-distillation work (e.g. [[knowledge-boundary-aware-self-distillation]]). |
| **What does not** | The requirement that privileged information be hand-authored (a hint, a rubric, a human demonstration) or computed from the model's own uncertainty; here it is a mechanical trace of forward-chained hops. |

## Limits

Demonstrated only on multi-hop factual QA over one corpus (English
Wikipedia) and one model family (Qwen3, three sizes); whether QCP-style
traces exist as a free by-product in task domains without an
explicit reverse hop-chaining construction (e.g. open-ended or
preference-based tasks) is unverified — the paper's own construction
procedure requires a source document and an explicit hop count to
reverse-engineer from. The teacher is an EMA of the student rather than
an independently optimized policy, an approximation the authors adopt
only to avoid extra compute, not because it is shown optimal. The
authors themselves note the self-distillation objective is the
"foundational" version and that stronger on-policy or self-distillation
techniques are left to future work.

## Related

[[knowledge-boundary-aware-self-distillation]] · [[self-consistency-difficulty-score]] · [[calibration-training]]

[^c1]: arxiv-2604-14054 — "self-play naturally produces a question construction path (QCP) during task generation, an intermediate artifact that captures the reverse solution process"
[^c2]: arxiv-2604-14054 — "the construction path c is only visible to the teacher model, ensuring that the teacher can produce reliable guidance while the student learns to solve the task without direct access to privileged information"
[^c3]: arxiv-2604-14054 — "GT contains only the final answer and provides little information about the underlying logic used to construct the question, making it difficult for the teacher to provide effective guidance to the student. In contrast, the full QCP achieves the best performance, while Partial QCP performs second best."
[^c4]: arxiv-2604-14054 — "compared with conventional self-play methods such as SQLM* and Dr.Zero, π-Play achieves higher accuracy with fewer search actions, indicating more efficient behavior. The same trend holds for query redundancy."
[^c5]: arxiv-2604-14054 — "π-Play introduces only a small per-step training overhead of 4.3% relative to Dr.Zero"
