---
description: "A reasoning agent delegates a free-form region description, naming a relation, fuzzy property or concept rather than an object, to a separate visual searcher that returns the region."
aliases: ["vSearcher task", "free-form region search"]
sources: ["arxiv-2512-18745"]
---
# Generalized visual search

Generalized visual search is the task of locating, in an image, a region
that is named by what it relates to or what it means, not by a category
label. The source defines it as "locating relational, fuzzy, or conceptual
regions described in free-form language".[^c1] The mechanism is a split
between two agents. A reasoning model (vReasoner) decomposes a question
and, when it needs evidence, "issues relevant image region descriptions
to vSearcher".[^c2] The searcher localizes the described region, may crop
it with an image-cropping tool, and returns it, so the reasoner can
continue; "the latter is mainly responsible for locating detailed visual
information and presenting them to" the reasoner.[^c3] The searcher is a
multimodal model trained with reinforcement learning, its reward an IoU
score "that matches the description" against ground-truth boxes.[^c4]

What the split changes for the asker is what it has to know. A sub-query
that names an object requires the asker to know the object's label; a
description by relation or function ("the marker next to the ride a child
can board alone", an illustrative phrase of mine) requires only what the
asker needs to be found, and leaves the resolution to the searcher. The
source's claim is that a searcher trained this way "empowers frontier
multimodal models (as vReasoners), significantly improving their
performance on a wide range of benchmarks".[^c5] The benchmark on which
the gap was motivated is one the authors built, where a frontier model
"only obtains 40.8% accuracy".[^c6]

## Limits

- The searcher was trained against a fixed external reasoner. The source
  states that it delegates "higher-order reasoning at training time to a
  strong external model".[^c7] Nothing in the work shows that searcher and
  reasoner co-adapt, or that the gain survives a reasoner the searcher
  never saw.
- The cropping step was rarely used. The average tool-call count "often
  ends up close to 1", and the stated reason is that the reasoner
  "usually describe[s] a rough region that is not very hard for vSearcher
  to locate, so the tool has little utility for vSearcher."[^c8] So the
  descriptions in the training distribution were easy to resolve. My
  inference: how hard the description is, not the search method, is what
  decides whether the crop matters. The work does not test harder
  descriptions.
- The task is perceptual. The work says nothing about a human asker's
  descriptions, and it does not show that a region-valued sub-query
  transfers to asking questions whose answers are not regions.
- The gains are reported on benchmarks the authors chose, one of them
  their own. The abstract's word "significantly" is the source's; the
  work reports no effect size that a reader can check against a
  baseline set chosen by someone else.

## Related

- [[self-ask-decomposition]] — the same delegation of a sub-question to an
  external tool, here a search engine over text; the searcher above returns
  a region, not a passage.
- [[on-demand-resolution-zoom]] — an answerer that requests a finer view
  mid-reasoning under a budget; the same request for a view, on video
  frames rather than image regions.
- [[dac-cross-agent-abstention-reward]] — a searcher and a generator split
  so that the generator's judgment is the searcher's reward; the source's
  in-loop variant uses a related coupling, with the reasoner's rating of
  each search result as the reward.

[^c1]: arxiv-2512-18745 — "locating relational, fuzzy, or conceptual regions described in free-form language"
[^c2]: arxiv-2512-18745 — "and, if needed, issues relevant image region descriptions to vSearcher"
[^c3]: arxiv-2512-18745 — "while the latter is mainly responsible for locating detailed visual information and presenting them to"
[^c4]: arxiv-2512-18745 — "encourages vSearcher to propose an accurate region that matches the"
[^c5]: arxiv-2512-18745 — "our vSearcher empowers frontier multimodal models (as vReasoners), significantly improving their performance on a wide range of benchmarks."
[^c6]: arxiv-2512-18745 — "which only obtains 40.8% accuracy"
[^c7]: arxiv-2512-18745 — "we delegate higher-order reasoning at training time to a strong external model"
[^c8]: arxiv-2512-18745 — "region that is not very hard for vSearcher to locate, so the tool has little utility for vSearcher."
