---
description: "Users with unformed intents cannot answer clarifying questions; DiscoverLLM models intents as a tree that concretizes only when responses surface options, and rewards discovery progress."
aliases: ["intent discovery", "latent intent hierarchy simulator", "intent formation through interaction"]
sources: ["arxiv-2602-03429"]
---
# Intent discovery versus elicitation

Clarifying-question work assumes the user holds a well-defined intent they have not yet articulated. DiscoverLLM argues this fails for open-ended tasks: "when intents are not yet discovered or formed, there is nothing to surface".[^c1] A user asked "what type of unique tone do you want?" may simply not know; they discover the answer by seeing outcomes, as people do in design and writing.[^c2]

## The formalization

Intent state grows monotonically over turns: "I0 ⊆ I1 ⊆ · · · ⊆ IT".[^c3] Intents form a tree of requirements from broad to specific, and the refinement space is the set of undiscovered children of already-discovered nodes, so a node can only be discovered after its parent.[^c4] The intent state updates only when the assistant's response either asks about a refinement or reveals it in a concrete artifact.[^c5]

The key asymmetry is the user expressiveness constraint: users "can only articulate intents in It and cannot request undiscovered refinements". A question such as "what type of pet?" therefore does not advance the conversation, because the user has not yet realized the refinement.[^c6] Nodes pass through undiscovered, emerging and discovered states; related-but-non-matching options accumulate toward a randomly sampled threshold, modelling learning by seeing what one does not want.[^c7]

## Reward

Discovery progress is the count of newly discovered intents per turn, "Rd (rt ) = |It+1 | − |It |", which covers satisfaction too, since satisfying an intent also discovers it.[^c8] An efficiency penalty on response length is capped at 1, so each discovered intent (+1) outweighs it; the authors report that normalizing by remaining intents gave inconsistent signals.[^c9] Trees are built automatically from existing artifacts by synthesizing requirements, abstracting them, and organizing them hierarchically.[^c10]

## Reported results

Fine-tuning Llama3.1-8B-Instruct and Qwen3-8B on creative writing, technical writing and SVG tasks improved intent discovery by around 10%, raised LLM-judged interactivity by 83% and cut conversation length by 32% against the best baselines; a 75-person user study showed higher satisfaction and shorter completion time.[^c11] The target behavior is diverging when intents are unclear and converging when they concretize.[^c12]

## Limits

- The user is a simulator; the tree is ground truth the simulator holds, so results depend on the LLM-built trees and simulated reactions. The human study is the only check against real users.
- The authors state they model discovery, not construction: the assistant "can only surface possibilities users are already disposed toward", and refinement is monotonic, with no abandoning or backtracking.[^c13]
- Evaluated on open-ended creation tasks; whether discovery framing helps in factual or closed-answer questioning is not tested here. Whether "intent discovered" in the simulator matches a user's real preference is my inference, not measured separately.

## Related

- [[underspecified-question-eager-answering]] — models guess instead of asking back; this note says asking back is also insufficient when the user has not formed the intent
- [[ambiguity-versus-incapability-routing]] — separates why a request is unanswerable; discovery adds a third case, an unformed intent
- [[history-conditioned-intent-reconstruction]] — reconstructs intent from history, whereas here intent is built by the response
- [[initial-exploration-problem]] — a related issue of probing before the target is known

[^c1]: arxiv-2602-03429 — "But when intents are not yet discovered or formed, there is nothing to surface"
[^c2]: arxiv-2602-03429 — "people discover what they need (problem space) by exploring possible outcomes (solution space)"
[^c3]: arxiv-2602-03429 — "I0 ⊆ I1 ⊆ · · · ⊆ IT"
[^c4]: arxiv-2602-03429 — "This captures progressive discovery (Sec. 2.1): a node can"
[^c5]: arxiv-2602-03429 — "directly asks about that aspect or reveals it through a concrete artifact that satisfies it"
[^c6]: arxiv-2602-03429 — "users can only articulate intents in It and cannot request undiscovered refinements in R(It )"
[^c7]: arxiv-2602-03429 — "undiscovered → emerging → discovered"
[^c8]: arxiv-2602-03429 — "Rd (rt ) = |It+1 | − |It |"
[^c9]: arxiv-2602-03429 — "each discovered intent contributes"
[^c10]: arxiv-2602-03429 — "We construct intent trees automatically from existing artifacts"
[^c11]: arxiv-2602-03429 — "reduced conversation length by 32%"
[^c12]: arxiv-2602-03429 — "adaptively diverging (i.e., explore options) when"
[^c13]: arxiv-2602-03429 — "the assistant can only surface"
