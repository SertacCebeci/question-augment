---
description: "Asking a crowdworker whether an image shares a category's shared trait, then its distinguishing trait, to walk a labeling hierarchy top-down instead of naming a class outright."
aliases: ["visual genus-differentia questioning", "hierarchy-guided annotation questioning"]
sources: ["arxiv-2604-14449"]
---
# Genus-differentia question routing

> Instead of asking an annotator to name a label, ask whether the image has
> the trait its candidate parent category shares with its siblings, then
> whether it has the trait that tells it apart from those siblings — and let
> the answers pick the next question.

## Definition / Mechanism

Proposed for crowdsourced image labeling Diao & Giunchiglia (2026),[^s1]
each category node in a predefined object hierarchy carries two properties
fixed in advance: its **visual genus** — "shared properties among different
objects" that it inherits from its parent — and its **visual differentia** —
"distinguishing properties among different objects within the same genus."
 A generation procedure walks the hierarchy from the root using these two
question types, alternating a *vertical loop* and a *horizontal loop*: "the
vertical loop aims to refine the labels of input images iteratively, moving
from root to leaf nodes in the object hierarchy... By asking annotators if
the image shares a visual genus with specific categories in the hierarchy,
candidate categories are determined, and then triggering the corresponding
horizontal loop. The goal of the horizontal loop is to ascertain the most
refined category within its domain for the input image, involving
comparisons with subcategories of the candidate." The routing is a
single recursive procedure: query the root's differentia; if it fails,
return "discharged" (no label); otherwise descend into whichever child's
differentia the annotator confirms, repeating until no child matches, and
return the deepest confirmed node's label. The question asked at each
step is never "what is this," only a yes/no test of one property against
the current node, so the label is the residue of a path of binary answers
rather than a single subjective choice.

## Why it matters

Against two baselines that ask for a class name directly — one with no
hierarchy shown, one with a name-only hierarchy shown — routing questions by
genus and differentia raised inter-annotator agreement in both a 50-image
and a 100-image task setting: "Method C demonstrated the highest accuracy
and consistency among the three methods... Krippendorff's Alpha under both
the 50-image and 100-image task settings, demonstrating that hierarchy-guided
annotation with explicit visual properties produces more [consistent
annotations]." The gain was not free: annotation time per task rose from
4.12 to 5.47 minutes (50-image tasks) and 8.27 to 9.47 minutes (100-image
tasks) moving from the name-only baseline to the genus/differentia
condition, with payment rising correspondingly. The mechanism's claim is
narrow but concrete: decomposing "what category is this" into a chain of
"does it have trait X" questions, where each trait is fixed by the
hierarchy rather than chosen by the annotator, trades annotator time for
inter-annotator agreement.

## Limits

- Measured only on human crowdworkers labeling images against a
  hand-built 12-category hierarchy (birds, vehicles, musical instruments);
  no evidence here that the same routing improves an AI agent's own
  question asking, only that it improves an *elicitation interface* aimed
  at a human. [?]
- The agreement gain is confounded with the hierarchy itself: Method B
  (name labels shown inside the same hierarchy, no genus/differentia
  questions) already improves over Method A, so part of the effect is the
  hierarchy's presence, not the genus/differentia question form specifically.
- No ablation isolates the vertical loop from the horizontal loop, or
  tests whether skipping the genus question (asking only differentia) loses
  the gain.
- Genus and differentia are authored by hand from WordNet and Wikipedia
  before annotation begins; the routing does not learn or select which
  property to ask about.

## Related

- [[differential-questioning]] — also conditions the next question on a
  structured candidate set, but on the asker's own leading hypotheses
  rather than on a fixed genus/differentia hierarchy.
- [[generalized-binary-search]] — the same top-down binary-test-per-node
  shape, without the genus/shared-trait vs. differentia/distinguishing-trait
  split this mechanism adds.
- [[calibration]] — the agreement metric here (Krippendorff's alpha) is a
  consistency measure, not a calibration measure, but both are proxies for
  whether an elicitation procedure converges on a shared reading of the
  same input.

[^s1]: arxiv-2604-14449
