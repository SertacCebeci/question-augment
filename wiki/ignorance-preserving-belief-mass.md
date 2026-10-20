---
description: "Holding belief as Dempster-Shafer mass with explicit ignorance, then asking to cut nonspecificity before discord, beat point-probability beliefs in document-grounded diagnostic questioning."
aliases: ["Dempster-Shafer belief for questioning", "nonspecificity-first question policy", "evidential network information gathering", "BBA elicitation"]
sources: ["arxiv-2603-05909"]
---
# Ignorance-preserving belief mass

A questioner must track what it does not yet know, not only what it favours. InfoGatherer keeps its belief over a finite hypothesis set as a Dempster-Shafer basic belief assignment (BBA): mass may sit on single hypotheses (specific support), on small subsets (ambiguity), or on the whole frame (residual ignorance).[^c1] Point probabilities cannot say "the evidence is vague"; a BBA can, so the agent need not commit early.

## How evidence enters

Retrieved documents are expanded into a layered graph of variables (hypothesis at the root, intermediate factors, user-observable features at the leaves). Each edge gets conditional BBAs from text snippets. An LLM may allocate mass only to singletons, to sets of at most two states, or to the full frame; vague, non-committal or contradictory snippets put mass on the full frame.[^c2] Several snippets on one edge are fused with Yager's rule, which sends conflict mass to the full frame, so contradiction becomes ignorance instead of being normalised away.[^c3] A user's answer is mapped to a BBA the same way (hedged answers keep leftover mass on the whole frame) and fused into the node, and beliefs are propagated to the hypothesis node.[^c4]

## How it picks the question

Candidate questions are scored by the expected drop in Deng entropy of the hypothesis BBA. That entropy splits into nonspecificity (mass on large sets, ambiguity) and discord (competition among focal sets, which reduces to Shannon [[entropy]] on singletons).[^c5] The policy is lexicographic: reduce nonspecificity first, and only once it falls below a threshold reduce discord.[^c6] Expectation is taken over answers weighted by the current pignistic distribution, which makes this an analogue of [[expected-information-gain]] on a richer uncertainty object. The dialogue stops when the top pignistic probability reaches a confidence threshold (0.85 in the experiments) and abstains if the turn budget runs out.[^c7]

## What was measured

On MedQA and BarExamQA recast as underspecified dialogues with simulated clients, with gpt-5-nano the method reached 66.5% success in the legal domain against 17.1% for ask-or-predict and 27.2% for MediQ, and 69.3% in the medical domain with the shortest dialogues (7.4 turns).[^c8] The ablation that swaps BBAs for extracted point probabilities (uniform fallback when none can be extracted) lowered success from 66.5% to 61.3% legal and 69.3% to 67.5% medical, and cost more turns.[^c9] The authors explain this as the probability variant being forced to commit mass the text does not justify, distorting early beliefs and pointing questions at the wrong uncertainty.[^c10] Confidence traces showed baselines overconfident: self-consistency confidence can rise through rationalisation rather than new information, and the evidential objective gave a conservative early phase followed by sustained late gains.[^c11]

## Limits

- The claim that nonspecificity-first ordering causes the better trajectories is the authors' reading of confidence curves; no ablation of the ordering itself is reported in the text I read (my inference).
- Gains over the probability variant are modest in medicine (1.8 points with gpt-5-nano) and no variance is reported there; the large gaps are against weak baselines.
- Replacing retrieved documents with a model-written reference gave higher success in medicine (74.6% vs 69.3%), so document grounding is not uniformly better.[^c12]
- Clients are LLM simulations answering from a fixed fact list; multiple-choice hypothesis sets are closed, unlike open user needs. The stopping threshold was set from observation.
- Dempster-Shafer theory is imported: what survives is the representation of ambiguity and conflict; the axioms of belief combination are not shown to match how LLMs assign mass, which is prompted, not calibrated.

## Related

- [[expected-information-gain]] — the point-probability criterion this generalises
- [[entropy]] — discord reduces to it on singleton mass
- [[candidate-set-entropy-question-selection]] — a heuristic entropy rule over candidates, without an ignorance term
- [[task-ambiguity]] — the underspecified-query setting
- [[elicitation-burden-tradeoff]] — success versus number of turns

[^c1]: arxiv-2603-05909 — "Mass assigned to singletons {z} represents specific"
[^c2]: arxiv-2603-05909 — "We allocate an explicit ignorance mass"
[^c3]: arxiv-2603-05909 — "which preserves contradictions as increased igno-"
[^c4]: arxiv-2603-05909 — "This fusion routes contradictions to ΘZt"
[^c5]: arxiv-2603-05909 — "It decomposes uncertainty into nonspecificity"
[^c6]: arxiv-2603-05909 — "it prioritizes reducing discord to discriminate"
[^c7]: arxiv-2603-05909 — "the dialogue ends, and the agent abstains."
[^c8]: arxiv-2603-05909 — "reaches 69.3% success and the shortest dialogues (7.4 turns)"
[^c9]: arxiv-2603-05909 — "improves success from 61.3% to"
[^c10]: arxiv-2603-05909 — "must commit belief mass across single hypotheses even when"
[^c11]: arxiv-2603-05909 — "agreement across samples may rise through rationalization rather than the acquisition of new information"
[^c12]: arxiv-2603-05909 — "achieves higher success (74.6% vs. 69.3%)"
