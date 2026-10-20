---
description: "What counts as an explanation depends on what the agent knows: a cause explains only if it is sufficient in every world the agent considers possible, and is not already known."
aliases: ["epistemic explanation", "explanation relative to knowledge", "knowledge-relative causal explanation"]
sources: ["arxiv-2511-21260"]
---
# Knowledge-relative explanation

A true cause can fail as an explanation. Halpern and Pass make the explanation depend on the asker: "the HP definition of causality is relative to an agent and, specifically, what the agent knows."[^c1] The motivating observation is that an agent asking why a man has lung cancer will not count a known exposure as an explanation: the agent "will not consider the fact that he worked for years in asbestos manufacturing an explanation if he already knew this fact."[^c2] The same fact, asked about by someone who lacks it, is an explanation. The explanatory value is in the gap between what is known and what is asked.

**The mechanism.** The agent's knowledge is modelled as an epistemic state: "an agent's knowledge is captured by the agent's epistemic state K".[^c3] K is a set of contexts, the ones the agent considers possible, with the causal model held fixed. The paper's explanation condition has four parts, in its causal-model form. X = x is an explanation of ψ relative to K if: (EX1b) in every context in K, setting X to x brings about ψ, so X = x is a sufficient cause for all the agent's live possibilities; (EX1a) in each context where X = x and ψ both hold, a conjunct of X = x is part of an actual cause of ψ there; (EX2) X = x is minimal; and (EX3) some context in K has both X = x and ψ. The explanation is non-trivial only if (EX4) it is not already settled by what is known: "The explanation is not already known given the observation of ψ."[^c4]

The knowledge clause does the work. Take the rock-throwing case with three possible contexts where both rocks are thrown but the first to arrive varies. If the agent's possibilities are the two contexts in which both rocks are thrown and Suzy's rock arrives first or simultaneously, then "ST = 1 ∧ BT = 1" is an explanation of the shattering, "but a trivial one; it was already known."[^c5] Its triviality comes from K, not from the world. Because the agent's possibilities rule out the case in which only Billy throws, the explanation carries no new information.

**Why a conjunct is added.** Sufficiency across K can force an explanation to be longer than any single cause. The paper's device for this is EX1a: "EX1(a) allows adding a conjunct" to an explanation so that it becomes a cause in each context.[^c6] This is why the explanation can be a conjunction even when no single conjunct is a cause everywhere in K.

**The abstract form.** The paper translates the clauses to any counterfactual framework, where the set K is "the obvious analogue" of the causal-model contexts: "a set of worlds in some model in a ccf."[^c7] Its authors say that "All the primed conditions except for EX1(a)′ are fairly direct translations of their unprimed counterparts."[^c8] The one clause that is not a direct translation needs the witness-conditioned cause as an input.

## Limits

- The paper drops the probability over K that Halpern's fuller definition includes: "we ignore the probability here."[^c9] Its explanations are therefore a qualitative notion. Whether ranking explanations by probability changes which is non-trivial is not tested.
- The authors assume the causal model is fixed, and say this is "without loss of generality," because uncertainty about the model can be encoded in the context. That is their claim. It is not checked here.
- The support for "explanation depends on what the agent knows" is the paper's cited observation, from Gärdenfors and others, not an experiment on how people explain. Nothing here measures how an asker's knowledge is elicited in practice.
- The examples are the authors' constructions, with a small number of contexts. The text does not show how K would be obtained for a real asker, nor how large a K has to be before the non-triviality test becomes informative.
- The explanation section is a definition plus worked examples. The text here is an extract, and the cross-reference to the explanation section is left as "??".

## Related

- [[causal-model-of-explanation]] — Lipton's account gives causes as what explains; this note adds that which causes explain depends on what the asker's knowledge leaves open. The two are not in the same paper, and the link is my inference.
- [[contrastive-explanation]] — relativizes an explanation to a foil; this note relativizes it to a set of possible worlds. Whether the two relativizations coincide was not checked.
- [[foil-inference]] — infers the unstated foil of a why-question; the knowledge set K here is taken as given rather than inferred.
- [[witness-conditioned-actual-cause]] — the cause that EX1a draws on, and the parameter whose choice fixes which causes count.

[^c1]: arxiv-2511-21260 — "the HP definition of causality is relative to an agent and, specifically, what the agent knows"
[^c2]: arxiv-2511-21260 — "if he already knew this fact"
[^c3]: arxiv-2511-21260 — "an agent’s knowledge is captured by the agent’s epistemic state K"
[^c4]: arxiv-2511-21260 — "The explanation is not already known given the observation of ψ"
[^c5]: arxiv-2511-21260 — "but a trivial one; it was already known"
[^c6]: arxiv-2511-21260 — "EX1(a) allows adding a conjunct"
[^c7]: arxiv-2511-21260 — "the obvious analogue of K is just a set of worlds in some model in a ccf"
[^c8]: arxiv-2511-21260 — "are fairly direct translations of their unprimed counterparts"
[^c9]: arxiv-2511-21260 — "we ignore the probability here"
