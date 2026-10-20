---
description: "A request for more evidence names a position in the source and gets nothing back when no real observation covers that position; a reward can penalise requests that land uncovered."
aliases: ["BEV-grounded pose query", "spatial grounding reward", "coverage-gated retrieval", "hypothesize-look-verify"]
sources: ["arxiv-2512-15160"]
---
# Coverage-checked evidence request

A reasoner that can ask for more evidence in the middle of an answer has to say what it wants. In EagleVision the request is a pose. The model writes a position and an orientation on a bird's-eye-view map of the scene, and the system looks for the stored video frame whose pose is closest.[^c1] The loop the paper builds around this is a "closed-loop hypothesize–look–verify cycle": the model proposes a spatial claim, asks for the view that would test it, and revises the answer from what comes back.[^c2]

The part that matters is the check on the address. Each stored frame is scored against the requested pose by a similarity that falls off with distance in position and orientation. The nearest frame is returned only if its score clears a coverage threshold. Otherwise the system returns an error prompt, which the paper glosses as "indicating no frame covers the queried pose."[^c3] A request aimed at a place the source does not cover therefore does not come back as a plausible but wrong view. It comes back as a refusal, and the reasoning has to go on without it.

The paper also treats the address as something to learn. Task rewards for answer correctness, output format and tool use "do not prevent the model from querying geometrically invalid viewpoints," which are "poses that fall outside the camera trajectory and therefore cannot be matched to any real frame."[^c4] A spatial grounding term is added that "penalizes trajectories containing any query whose best retrieval similarity" falls below the coverage threshold.[^c5] The penalty is on the whole trajectory, so one uncovered request costs the rollout, and the policy learns which places are worth asking about from the reward alone, without human reasoning traces.

What was measured. In the reward ablation the spatial term adds a further +0.5: "the Spatial term reaches 63.5 (+0.5)," with the tool term described as the larger contributor, since "the Tool reward provides the main gain."[^c6][^c7] The grounded pose query itself is compared against iterative reasoning without it. Adding BEV grounding "lifts performance to 62.7 (+3.3 over baseline)."[^c8] The authors read this as the benefit of "explicit geometric anchoring via active view selection."

## Limits

- The spatial term is the smaller of the reward gains in the ablation read, and it is one table on one backbone. The gain is not separated from the extra supervision the tool term brings.
- In the slices read, no count of uncovered queries before and after training is reported. The reward is shown to raise accuracy; that it lowers the rate of invalid requests is the natural reading, not a reported measurement.
- The coverage threshold and the pose-similarity scales are hand-set hyperparameters. Their sensitivity was not read.
- The source here is a densely sampled video with a pose index built by an off-the-shelf SLAM system. A text corpus or a human interlocutor has no pose space, so "coverage" would need another definition. That transfer is my inference; the paper does not test it.
- Results are on VSI-Bench and SQA3D, both spatial benchmarks with fixed question templates. Nothing shows the penalty changes behaviour on open questions.

On the asker's side the move, as I read it, is that the address of a request is checked against what the source holds: a request for a part of a source that is not there yields a refusal, and the refusal is itself information about the source's coverage. This is my inference from the mechanism. The paper says nothing about questions to people.

## Related

- [[strategic-perception-timing]] — decides when to re-consult a visual source during a chain; this note concerns where a request is addressed and what happens when the address is empty.
- [[referent-match-set-ambiguity]] — an empty match set from one robot's own view is a typed case of "nothing here"; the same absence seen from the referent side rather than the retrieval side.
- [[groundedness-gated-tool-routing]] — chooses among retrieval tools by whether the target is visually grounded; here the grounding is checked after the request, by the retrieval score.
- [[tool-integrated-reasoning]] — the general loop in which a tool result re-enters the context; the tool in this paper is a pose query into a spatial index.

[^c1]: arxiv-2512-15160 — "predict a pose on the BEV plane to retrieve the nearest real frame"
[^c2]: arxiv-2512-15160 — "closed-loop hypothesize–look–verify cycle"
[^c3]: arxiv-2512-15160 — "indicating no frame covers the queried pose"
[^c4]: arxiv-2512-15160 — "poses that fall outside the camera trajectory and therefore cannot be matched to any real frame"
[^c5]: arxiv-2512-15160 — "penalizes trajectories containing any query whose best retrieval similarity"
[^c6]: arxiv-2512-15160 — "the Spatial term reaches 63.5 (+0.5)"
[^c7]: arxiv-2512-15160 — "the Tool reward provides the main gain"
[^c8]: arxiv-2512-15160 — "Introducing BEV grounding further lifts performance to 62.7 (+3.3 over baseline)"
