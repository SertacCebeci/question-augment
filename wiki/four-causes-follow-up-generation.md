---
description: "An LLM tutor deductively maps an empirically-derived taxonomy of learner questions onto Aristotle's Four Causes and prompts one follow-up question per cause each turn."
aliases: []
sources: ["arxiv-2604-10545"]
---
# Four-causes follow-up generation

> Four questions per turn, one per cause, chosen not by a prompt writer's
> intuition but by a taxonomy the learners' own dialogues produced.

## Definition / Mechanism

Cao et al. (2026)'s CausaDisco fixes *what* an LLM
tutor asks next by routing every follow-up through a four-slot template
instead of a single open-ended "anything else?" prompt. The slots are not
arbitrary: a formative study (N=26) coded learners' own questions into a
taxonomy (components, attributes, co-existent concepts, development,
realistic application, significance, real-world consequences), and this
taxonomy was then deductively mapped onto Aristotle's Four Causes —
material (components), formal (attributes, co-existent concepts),
efficient (realistic application, development), final (significance,
real-world consequences).
[^c1]

The mapping is operationalized as a single instruction to the LLM after
each answer: "Provide the top four related follow-up questions based on
the previous question using the four causes idea."
[^c2]

This turns a generic single follow-up into a fixed-width, diversity-guaranteeing slate:
one question anchored in each cause, so the learner is offered a
component question, an attribute question, a cause-of-change question and
a significance question every turn, rather than whatever single angle the
model's default continuation would have picked.

In a within-subjects controlled study (N=36) against a baseline of
unstructured LLM chat, this produced more dialogue with the system: more
dialogue turns, 6.97 vs. 4.08 (p<.01).
[^c3]

Self-rated logical coherence was also higher, 6.06 vs. 5.28 (p<.01).
[^c4]

Perceived in-depth understanding and streamlined efficiency were higher
too (both p<.05). The mechanism's effect on quiz-measured learning was
not significant: objective quiz scores did not differ between
conditions, 2.00 vs. 2.25 (p>.05).
[^c5]

## Why it matters

This targets question *formulation and diversity*, not selection or
stopping: instead of an uncertainty signal choosing whether to ask, a
fixed epistemological taxonomy guarantees which angles get asked every
turn, deductively derived from what learners were already observed to
want to know rather than an author's guess at good follow-ups. It is a
different lever from [[argument-grounded-socratic-questioning]], whose
specificity comes from a mined argument-graph edge in the writer's own
text; here the specificity comes from a category (one of four fixed
causes), not from grounding in the learner's utterance, and the goal is
breadth of exploration rather than convergence on one flaw.

## Limits

- The taxonomy-to-causes mapping is deductive and author-performed, not
  learned or validated against a held-out taxonomy; a different
  self-learning domain could yield a taxonomy that maps unevenly onto the
  four causes (the paper's own discussion section notes some disciplines
  do not engage all four causes equally).
- The LLM does not reliably execute the categorization it is asked to:
  it was observed that ChatGPT sometimes struggled to accurately assign
  the appropriate cause category to each question and to prioritize
  certain causes over others based on the context or scenario at hand.
[^c6]

  The four-slot structure is therefore a prompt instruction, not a
  verified constraint on the model's output (unverified).
- The controlled study measured engagement and self-rated understanding,
  not learning outcomes: objective quiz scores did not improve over the
  unstructured baseline, so the mechanism's benefit is demonstrated for
  interaction quantity and subjective sophistication, not for the task
  the self-learning system exists to serve.
- Single LLM (ChatGPT) and a single reading-comprehension self-learning
  task (blockchain/NFT material); no ablation isolates the four-cause
  template's contribution from persona-pattern prompting used alongside
  it.

## Related

[[argument-grounded-socratic-questioning]] · [[socratic-method]] ·
[[divergent-questioning]] · [[structural-disagreement-clarification]]

[^c1]: arxiv-2604-10545 — "The material cause naturally corresponds with the “components of concepts” category, which refers to the fundamental elements constituting a concept. The formal cause, which describes the distinct form or arrangement defining an object, aligns with the “attributes of concepts” category. Additionally, the formal cause includes “co-existent concepts,” helping clarify the characteristics that distinguish a concept from others. The efficient cause, representing the driving force behind an entity’s existence or change, aligns with both “realistic application” and “development of concepts,” as these categories explore the motivations and mechanisms of change. Lastly, the final cause, which denotes the purpose or intended outcome of an entity, maps to the “significance of concepts” and “real-world consequences” categories"
[^c2]: arxiv-2604-10545 — "For each interaction, the directive “Provide the top four related follow-up questions based on the previous question using the four causes idea” is employed."
[^c3]: arxiv-2604-10545 — "participants engaged in significantly more dialogue turns in the CausaDisco (𝑀 = 6.97, 𝑆𝐷 = 2.22) than in the baseline condition (𝑀 = 4.08, 𝑆𝐷 = 1.86, 𝑝 < .01)."
[^c4]: arxiv-2604-10545 — "Participants’ ratings of logical coherence are significantly higher in the CausaDisco condition (𝑀 = 6.06, 𝑆𝐷 = 0.95) than in the baseline condition (𝑀 = 5.28, 𝑆𝐷 = 1.28, 𝑝 < .01)."
[^c5]: arxiv-2604-10545 — "Participants’ objective quiz scores in the system condition are, on average, 2.00 (𝑆𝐷 = 0.93), a little lower than in the baseline condition (𝑀 = 2.25, 𝑆𝐷 = 0.89), but there is no significant difference (𝑝 > .05)."
[^c6]: arxiv-2604-10545 — "it was observed that ChatGPT sometimes struggled to accurately assign the appropriate cause category to each question and to prioritize certain causes over others based on the context or scenario at hand."
