---
description: "Placing a user-feedback loop at each pipeline stage that produces a decision, instead of only after the full artifact is rendered, raises goal satisfaction on a multi-stage generation task."
aliases: ["stage-specific conversational feedback", "stage-specific refinement loops"]
sources: ["ozden-2026"]
---
# Stage-specific elicitation

> Ask at the stage that owns the decision, not only once the whole artifact
> exists to be criticised.

## Definition / Mechanism

ConvDeck is a five-stage paper-to-slide pipeline (preprocessing, outline
generation, conversational outline refinement, slide generation,
conversational slide refinement) that opens a feedback loop at each of the
two stages whose output the user can meaningfully constrain — outline
structure (Stage 3) and rendered slide content (Stage 5) — rather than
collecting all feedback in one post-hoc pass on the finished deck: "ConvDeck
integrates interaction at two stages: (i) outline generation, where users
can revise high-level decisions such as narrative flow, section emphasis,
slide ordering, and content coverage before the full deck is rendered, and
(ii) slide generation, where users can further refine slide-level content,
visual organization, figures, layout, and other deck details."[^c1]

The contrast class is explicit in the paper's own framing of prior work:
non-conversational systems take no feedback at all, and conversational
baselines "apply user feedback as post-hoc edits on the fully rendered
deck" — a single stage that must absorb every kind of correction, structural
and cosmetic alike, through surface-level language edits on the finished
output.[^c2]

## Why it matters

Two results attribute the gain to *where* the loop sits, not merely to
having one. Against two conversational baselines that only edit the
rendered deck (ConvHTML, AutoSlides), ConvDeck's stage-aligned loops reach
79% average goal satisfaction (LLM judges) versus 66% and 70%, and 78% by
human raters versus 72% and 74%.[^c3]

A second study isolates each stage's own loop: outline-relevant goals rise
from 37.7% to 92.0% satisfaction after the outline-refinement stage alone
(+54.3 points), and slide-relevant goals rise from 68.4% to 86.4% after the
slide-refinement stage alone (+18.0 points) — each stage's loop moves only
the goals whose decision that stage owns.[^c4]

## Limits

- The comparison is against the paper's own post-hoc-editing baselines
  (ConvHTML, AutoSlides) on one task (paper-to-slide generation) and one
  goal inventory (50 predefined goals in 5 categories) the authors built;
  the gain has not been shown to generalise to a pipeline whose stages are
  not already cleanly separable into "structural" versus "cosmetic" the way
  outline and rendered slides are.
- The 79%/78% headline numbers average over two LLM judges and a 30-person
  user study on 30 papers; the per-stage before/after numbers (Table 3) are
  reported for the LLM-judge protocol only in the extract read here.
- The claim is about *when* a loop is placed in an existing multi-stage
  architecture, not about *whether* to ask at all or *what* question to
  ask — [[clarifying-interaction-decomposition]] separates that "when"
  question from this one; this note is about which pipeline stage, not
  which turn.

## Related

[[clarifying-interaction-decomposition]] · [[elicitation-protocols]] · [[speak-act-refinement]]

[^c1]: ozden-2026 — "ConvDeck integrates interaction at two stages: (i) outline generation, where users can revise high-level decisions such as narrative flow, section emphasis, slide ordering, and content coverage before the full deck is rendered, and (ii) slide generation, where users can further refine slide-level content, visual organization, figures, layout, and other deck details."
[^c2]: ozden-2026 — "apply user feedback as post-hoc edits on the fully rendered deck"
[^c3]: ozden-2026 — "Human ratings favor ConvDeck in every category (overall 78%, vs. 72% for ConvHTML and 74% for AutoSlides)"
[^c4]: ozden-2026 — "37.7% 92.0% ↑ +54.3% 68.4% 86.4% ↑ +18.0%"
