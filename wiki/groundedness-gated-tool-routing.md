---
description: "An agent routes between text search, image search and captioning by whether the target entity is visually grounded, not by a fixed retrieval order."
aliases: ["DBAgent", "decision-based search agent", "failure-aware trajectory branching"]
sources: ["arxiv-2604-07146"]
---
# Groundedness-gated tool routing

> Which source to consult is decided by whether the entity is already identified, not by a fixed step order.

## Definition / Mechanism

A knowledge-based visual question answering (KB-VQA) agent picks, at every[^s1]
step, one action from a fixed set $A = \{a_{ans}, a_{text}, a_{img}, a_{cap}\}$
conditioned on its running state $s_t = (I, q, a_1, e_1, \ldots, a_{t-1},
e_{t-1})$ — the image, the question and every action and evidence pair so
far Wu et al. (2026). Answer ends the episode; text
search issues a query against a textual knowledge base; image search runs
similarity search against an image index and returns the linked article;
caption converts the current visual content into a task-oriented textual
description and is appended to the internal state without adding external
evidence — it does not touch the evidence buffer, only the reasoning
context that later queries are built from

The routing rule the training data teaches is conditioned on **groundedness**, not on retrieval depth or a step count. Each training sample is first probed without any tool call; if the ungrounded model still answers correctly, it becomes a zero-retrieval trajectory. A failure is split into two causes and each is routed to a different branch: if the entity is recognized but the fact is missing, the trajectory is built around text search; if the entity itself cannot be identified, the trajectory is built around image search followed by a caption step that supplies a semantic anchor for the query that follows Gold answers and entity labels are used only to build and label this offline training signal — they gate which branch a trajectory is assigned to, not what the agent sees at inference, when it has no ground truth to route by

The policy is learned by supervised fine-tuning over these branched, difficulty-stratified trajectories, with the loss masked to decision tokens only (the action tag and the reasoning that precedes it) and applied nowhere to the tool-returned evidence tokens, so the model is supervised on *which action to take*, not on memorizing retrieved content

## Why it matters

A fixed retrieve-then-generate pipeline treats "search" as one step that
always fires the same tool at the same point. This mechanism instead makes
the *choice of source itself* the trained behavior: two ablations that fix
the tool — always image-search the top-1 match, or always caption-then-text-search — both under-perform the routed policy, and the paper reads this as
evidence that the gain is in deciding when and how to retrieve, not in
retrieval quality alone An oracle variant that is handed the
ground-truth article still benefits from the routed policy over a
fixed one, which the paper attributes to evidence selection and grounded
reasoning rather than retrieval coverage

## Limits

- The routing signal is entirely offline: a held-out gold answer and an
  entity label decide, once, which branch (text-first vs. image-then-caption)
  a training trajectory follows. The agent never sees this signal at
  inference and never revises the branch assignment; a case that is
  ambiguous between the two failure types is forced into one.
- Evaluated only on two encyclopedic KB-VQA benchmarks (InfoSeek,
  Encyclopedic-VQA) with one backbone (Qwen2.5-VL-7B) and one knowledge
  base construction (Wikipedia, dense image and BGE text indices); whether
  the groundedness split transfers to sources that are not encyclopedic
  articles is unverified.
- Trained by SFT on automatically constructed trajectories, not by a
  reward that scores the routing decision itself; the paper's own
  limitations note this trades manual annotation for unverified trajectory
  quality, and flags iterative retrieval's inference-cost overhead as
  moderate but unresolved.

## Related

- [[embodied-ambiguity-sources]] — a comparable split of ambiguity into "what wasn't observed" vs. "whose intent is unclear," routed to different actions in a robot policy.
- [[g-steer]] — also a trained per-instance policy choosing among a small discrete action set (there: Retrieve / Ask / Stop) rather than a fixed pipeline.
- [[bridge-conditioned-retrieval]] — retrieval conditioned on prior evidence within one modality, where this note conditions the *choice of modality itself*.
- [[tree-search-methods]] — the broader family of adaptive, state-conditioned multi-step inference this routing policy is an instance of.

[^s1]: arxiv-2604-07146
