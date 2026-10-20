---
description: "A constraint-space data-synthesis method that builds labeled training samples for detecting user-side implicit conflict by transforming dialogue constraints along Hymes's SPEAKING dimensions."
aliases: ["SynUC"]
sources: ["wang-2026-towards"]
---
# SynUC

A method for synthesizing training data for [[user-side-implicit-conflict]]
detection. Rather than generating conflicting utterances directly in
surface text, SynUC first extracts a multi-turn dialogue's active task
hierarchy and its valid explicit/implicit constraints, then transforms
those constraints — not the text — to produce a target-category follow-up
utterance, then verifies the result before accepting it as a training
sample.

"SynUC synthesizes label-controllable training samples for user-side
conflict detection in a constraint space." [[wang-2026-towards|Wang et al.
(2026)]][^c1]

"The constraint transformation module is built on Hymes's SPEAKING
framework (Hymes, 2013) and modeled as a cross-sample self-evolving
memory, allowing high-quality constraint conflict construction experience
to be reused." Wang et al. (2026)[^c2]

Applied to WildChat, SynUC produced UC-Data (2,487 samples) used for both
supervised fine-tuning and reinforcement learning (DR-GRPO) of a
lightweight detector, with an added "constraint-attribution reward" that
scores whether the model identifies the specific conflicting constraint
pair, not just the label.

"SynUC achieves an overall F1 score of 79.50% on UC-Bench, outperforming
MultiTurnInstruct, the strongest SFT baseline, by 10.80 percentage points
and ConInstruct by 18.59 percentage points." [[wang-2026-towards|Wang et
al. (2026)]][^c3]

"SynUC (DR-GRPO†), which further incorporates the constraint-attribution
reward 𝑅attr, achieves 81.01% F1 and 84.09% IC recall on the overall test
set, improving over the strongest baseline by 11.75 and 1.41 percentage
points, respectively." Wang et al. (2026)[^c4]

## Known as

Not applicable — the alias list carries one name from one field (SynUC is
this wiki's only name for the method; SPEAKING is a component, not an
alias of SynUC).

## Transfer

| | Home field | Here |
|---|---|---|
| Formalism | SPEAKING — Hymes's eight-part mnemonic (Setting/Scene, Participants, Ends, Act sequence, Key, Instrumentalities, Norms, Genre) for describing a speech event | A fixed eight-schema set used to enumerate the dimensions along which a historical constraint can be transformed into a new, conflicting one |
| What survives | The eight named dimensions as an exhaustive-feeling checklist of ways a communicative act can vary | The same checklist, repurposed to generate controllable, labeled conflict *types* (e.g. a shift on the Participants dimension implying a new audience) rather than to analyze a naturally occurring utterance |
| What does not | The ethnographic, descriptive purpose — SPEAKING was built to characterize how a real speech event unfolds, not to manufacture synthetic ones, and carries no claim about which dimension a real user is more likely to shift | Any evidence that these eight dimensions are the right or complete generative model of how real implicit conflicts arise; the paper's ablations show the schema helps synthesis quality, not that it is ethnographically faithful |

## Limits

The reported gains (SFT +10.80–18.59 F1 points, DR-GRPO† +11.75 F1 / +1.41
IC-recall points over the strongest baseline) are relative to baselines
the authors themselves reproduced and adapted from other tasks, not
baselines independently tuned for this one — [?] not independently
reproduced by this wiki. The constraint extractor and the transformation
module are themselves LLM calls, so synthesis quality is bounded by the
same model family's ability to identify constraints that the detector is
later trained to recognize; the method's claim is about a lightweight
detector trained on synthesized data outperforming general-purpose
prompting, not about detection in the open-ended-response setting the
Findings 1–4 diagnosis was made in.

## Related

- [[user-side-implicit-conflict]]
- [[constraint-as-information]]

[^c1]: wang-2026-towards — "SynUC synthesizes label-controllable training samples for user-side conflict detection in a constraint space."
[^c2]: wang-2026-towards
[^c3]: wang-2026-towards — "SynUC achieves an overall F1 score of 79.50% on UC-Bench, outperforming MultiTurnInstruct, the strongest SFT baseline, by 10.80 percentage points and ConInstruct by 18.59 percentage points."
[^c4]: wang-2026-towards
