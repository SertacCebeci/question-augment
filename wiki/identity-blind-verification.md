---
description: "A verifier that scores teacher and student rollouts together, without knowing which is which, keeps the reward spread; the teacher's answers in the pool anchor difficulty."
aliases: ["blind scoring", "identity-blind rubric verification", "blind verifier pool", "teacher-anchored blind verification"]
sources: ["doi-10-48550-arxiv-2605-07396"]
---
# Identity-blind verification

When a verifier scores a response against a rubric, it can also know where the response came from. In distillation the response is either a teacher answer or a student rollout, and a verifier that knows which is which may favour one source for reasons unrelated to the criteria. The rubric-based distillation paper handles this by blinding the verifier. Its design rule reads: "the Verifier should blindly score both teacher and student rollouts together to calibrate bias" arising from varying question difficulty.[^c1] Two effects are separated in the paper: the identity effect, and the role of the teacher answers that stay in the pool.

Identity. The verifier does not see labels saying which rollout is the teacher's. The paper's summary is that "Blind scoring prevents identity-driven bias while preserving the reward spread."[^c2] The measured cost of removing the blind is small but consistent in their table: the ablated run ("w/o blind scoring (verifier sees teacher)") reaches 61.75 Pass@1 against 65.02 for the full method on AIME24. The text puts it as "Revealing identities costs 3.25 points."[^c3]

Anchor. The teacher answers are kept in the scored pool even though the purpose is to score students. The authors write that "retaining teacher responses in the blind pool is essential as" a difficulty anchor.[^c4] Their argument is about the spread of scores rather than their level. A verifier that sees only student rollouts, the paper says, "often causes the Verifier to collapse toward" a middle score, "mean scores regardless of task complexity."[^c5] My reading is that the teacher's answers serve as the high end of the scale, so the same criteria give spread across easy and hard prompts. The paper says this "remains properly calibrated across diverse problem difficulties," which keeps the group-relative advantages informative: it is "maintaining the discriminative power of GRPO advantages."[^c6]

The mechanism, then, is not that a teacher's answer is trusted. The teacher's answers are reference points in the same scale, so the verifier's per-criterion decisions are made relative to a known-good spread, while the identity labels that could bias those decisions are hidden. The authors do not claim that blinding removes all source information; they report the effect of hiding the labels.

## Limits

- The identity effect is one difference, 3.25 points, on one benchmark (AIME24) and one student-teacher pair. Interval, seed, and variance are not reported in the sections I read.
- Hiding labels does not hide style. If teacher and student answers differ in form, a verifier can still tell them apart from the text. The paper does not test whether a stylistically matched pool changes the result (my inference).
- The claim that a student-only pool collapses scores toward the mean is stated as the authors' expectation ("often causes"). I did not find a run of that configuration in the sections I read, so the anchor effect is argued, not tabled.
- The method costs a verifier call per rollout and per criterion, and the pool includes teacher answers; the cost of the teacher pool is not separated from the cost of the rest.
- Blinding is about the verifier. It does not address a verifier that is systematically wrong on some criteria; see [[rubric-verifier-failure-modes]].

## Related

- [[rubric-reward-on-policy-distillation]] — the distillation reward whose verifier is blinded in this way.
- [[anonymized-cross-review]] — anonymized answers in a critique stage, where the source is hidden to stop favouritism; the same blinding idea, applied to critique rather than to a rubric score.
- [[generative-verification]] — a verifier kept blind to the detector's own confidence; there the blind is to the detector's self-report, here to the source of the response.
- [[verifier-discrimination-and-calibration]] — why a verifier's score spread matters apart from its accuracy, which is what the anchor argument is about.
- [[rubric-verifier-failure-modes]] — the structural ways a rubric verifier goes wrong, which blinding does not fix.

[^c1]: doi-10-48550-arxiv-2605-07396 — "the Verifier should blindly score both teacher and student rollouts together to calibrate bias"
[^c2]: doi-10-48550-arxiv-2605-07396 — "Blind scoring prevents identity-driven bias while preserving the reward spread."
[^c3]: doi-10-48550-arxiv-2605-07396 — "Revealing identities costs 3.25 points."
[^c4]: doi-10-48550-arxiv-2605-07396 — "retaining teacher responses in the blind pool is essential as"
[^c5]: doi-10-48550-arxiv-2605-07396 — "Evaluating students in a vacuum often causes the Verifier to collapse toward"
[^c6]: doi-10-48550-arxiv-2605-07396 — "maintaining the discriminative power of GRPO advantages."
