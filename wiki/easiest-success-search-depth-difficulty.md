---
description: "Scoring a generated task's difficulty by the fewest searches among its successful solves, capped, rather than by success rate, so that shortcut-solvable tasks earn no difficulty credit."
aliases: ["Search-Depth Reward", "SDR", "minimum successful search depth"]
sources: ["doi-10-48550-arxiv-2608-01822"]
---
# Easiest-success search depth as task difficulty

Success rate cannot tell a shallow lookup from a task needing multi-step search.[^c1] In self-play, the task writer is rewarded when a task is solvable yet not trivially so: tasks every solver attempt solves or none solves get only a low base reward (0.2).[^c2] For the rest, difficulty is the minimum search depth over successful rollouts (depth = number of unique search queries), not the mean or maximum: if any successful rollout solves the task with shallow search, the task admits a shortcut.[^c3] The reward is r0 + (1 − r0)·min(h_min / H, 1), where H is a saturation depth, so arbitrarily many searches are not rewarded.[^c4]

The design choice is the aggregator: min over successes makes difficulty a property of the cheapest known route to the answer, which is what a shortcut is.

## Limits

Search depth counts unique queries, a proxy that assumes more queries mean more genuine hops. The paper reports the reward helps in an ablation on one benchmark with one backbone; no comparison of min against other aggregators is established in the slices I read. The cap H and the number of attempts per task are tuned constants. Applying this to human question-asking is my inference.

## Related

- [[self-answer-driven-search-depth]] — finds the earliest sufficient step instead of the cheapest success
- [[evidence-chain-question-generation]] — the grounding that makes depth meaningful

[^c1]: doi-10-48550-arxiv-2608-01822 — "success rate alone does not distinguish shallow lookup from deeper"
[^c2]: doi-10-48550-arxiv-2608-01822 — "they are respectively too hard or too easy."
[^c3]: doi-10-48550-arxiv-2608-01822 — "task admits a shortcut and should not receive a high difficulty"
[^c4]: doi-10-48550-arxiv-2608-01822 — "This cap prevents SDR from rewarding arbitrarily many"
