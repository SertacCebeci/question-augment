---
description: "A three-level dialogue-act taxonomy (act, subtype, utterance) embedded in hyperbolic space so a question's formulation is chosen top-down and related subtypes stay geometrically close."
aliases: ["three-level action taxonomy", "Poincaré dialogue-act embedding"]
sources: ["lin-2026-dual", "nickel-kiela-2017"]
---
# Hyperbolic dialogue-act taxonomy

> Formulating a question is decomposed top-down — which act, which subtype,
> which words — and the act/subtype space is embedded in hyperbolic geometry
> so that sibling formulations (e.g. two kinds of probing question) stay
> close to each other and far from unrelated acts.

## Definition / Mechanism

Lin, Deng, Wang & Yang discretize how a justice's turn is formulated into
three levels rather than treating utterance generation as one open-ended
choice: "Level 1 defines high-level dialogue acts, such as Questioning,
[[hypothesis-testing|Hypothesis Testing]], or Declaration. Level 2 refines each act into
subcategories (e.g., Clarification, Probing, Comparison), while Level 3
specifies the final utterance." The motivation stated is that "domain-
specific agents can often reduce complexity by operating on a finite set
of dialogue acts" rather than a vast open-ended action space.[^c1]

To let the policy generalize across related act-subtypes instead of
treating each as an unrelated discrete action, the taxonomy is represented
in a Poincaré (hyperbolic) embedding space, following Nickel & Kiela's
method for embedding hierarchical/tree data: "Poincaré embeddings are
defined in a hyperbolic geometry that naturally preserves hierarchical and
tree-like relationships, where parent nodes lie closer to the origin and
child nodes are positioned exponentially farther away." The embedding is
trained by a softmax-style objective over observed positive pairs (parent–
child or sibling relations in the act hierarchy) against sampled negative
pairs, so that "the Dialogue Agent can learn smoother transitions across
levels, leverage proximity for related actions (e.g., between sibling
subacts), and better generalize across hierarchically related behaviors."[^c2]

## Why it matters

Stall 3 asks how a question touches the axis once an axis is chosen. This
gives a concrete, two-part answer: formulation is a discrete top-down
choice (act, then subtype, then wording) rather than a single free-text
generation step, and the geometry of the discrete choice space is built so
that "close" formulations (two ways of probing the same point) are
literally close in the space the policy searches, which a flat, unordered
action set cannot represent.

## Transfer

| | |
|---|---|
| **Home field** | Representation learning: Nickel & Kiela (2017) embed symbolic hierarchical/tree data (e.g. WordNet) into an n-dimensional Poincaré ball so that hierarchy and similarity are captured jointly, and show this beats Euclidean embeddings on data with latent hierarchies |
| **Here** | The symbolic hierarchy is a hand-built three-level taxonomy of judicial dialogue acts and subtypes; the embedding is trained on parent–child and sibling pairs drawn from that taxonomy, then used as the representation a dialogue policy conditions on |
| **What survives** | The geometric claim that tree-structured relations (parent closer to origin, children farther and separated by branch) are a natural fit for a fixed discrete act/subtype hierarchy, and the training objective (positive pairs vs. sampled negatives under a hyperbolic-distance softmax) |
| **What does not** | Any measured evidence for *this* application: the paper reports no ablation isolating the embedding's contribution to the dialogue policy's performance (unlike the [[appraisal-gated-topic-switching|appraisal agent]] and each reward component, which are each ablated), so the generalization benefit claimed for sibling subacts is asserted, not demonstrated on this task |

## Limits

The taxonomy itself is domain-specific (built from Supreme Court transcript
annotation) and hand-designed at three fixed levels; the note's claim about
what the geometry buys the formulation decision rests on the original
Poincaré-embedding result on unrelated hierarchical data (WordNet), carried
over by analogy, since no isolated test of the embedding's effect on this
dialogue task is reported.[^c3]

## Related

[[appraisal-gated-topic-switching]] · [[elicited-response-reward]] · [[optimal-decision-tree]] · [[question-evaluation-method]]

[^c1]: lin-2026-dual — "Level 1 defines high-level dialogue acts, such as Questioning, Hypothesis Testing, or Declaration. Level 2 refines each act into subcategories (e.g., Clarification, Probing, Comparison), while Level 3 specifies the final utterance."
[^c2]: lin-2026-dual — "Poincaré embeddings are defined in a hyperbolic geometry that naturally preserves hierarchical and tree-like relationships, where parent nodes lie closer to the origin and child nodes are positioned exponentially farther away."
[^c3]: lin-2026-dual — "We conducted four ablations to clarify the role of each reward component and the appraisal agent: (i) w/o the appraisal agent, (ii) w/o the succinct reward, (iii) w/o the novelty reward, and (iv) w/o the goal relevance reward."
