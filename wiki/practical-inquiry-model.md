---
description: "Scientific inquiry as a cycle of four activities (deliberation, conception, action, perception); the paper uses it to define scientific general intelligence and to sort benchmark tasks."
aliases: ["Practical Inquiry Model", "PIM", "four-quadrant inquiry cycle"]
sources: ["arxiv-2512-16969"]
---
# Practical inquiry model

The Practical Inquiry Model (PIM) is a theoretical framework, taken by the paper from earlier work, that "deconstructs the scientific process into a cycle of four core cognitive activities".[^c1] The four quadrants are Deliberation, "the search, synthesis, and critical evaluation of knowledge"; Conception, the generation of ideas; Action, the practical implementation via experiments; and Perception, the awareness and interpretation of results.[^c2] The model is a map of scientific cognition, and it is read as a loop: the quadrants are interdependent, and an AI with scientific intelligence must cover them all, since "An AI exhibiting true SGI must possess robust capabilities across this entire spectrum."[^c3]

The paper uses the four quadrants as a sorting key for evaluation. Each task of its benchmark is assigned to one quadrant, for example "Scientific Deep Research (Deliberation)".[^c4] Applied to existing benchmarks, the same key shows where they concentrate. Knowledge benchmarks are said to correspond "mainly to the Deliberation quadrant".[^c5] The paper's summary of the survey is that "Most current evaluations capture only fragments of the SGI spectrum."[^c6]

The transferable part is the structure, not any score. A capability is located in a stage of the cycle, and a benchmark that covers one stage says nothing about the others. For the question-and-answer setting this suggests a reading that the paper does not state: a question belongs to deliberation, and the answer is tested only when it passes through conception, action and perception. That reading is mine, not the paper's.

## Limits

- The paper imports PIM and does not test it. The slices read give no evidence that the four quadrants separate in model behaviour; the decomposition is asserted as the right partition of scientific cognition.
- The mapping of tasks to quadrants is the authors' choice, and the slices read do not justify each placement one by one.
- The framework names no notion of a good question. It says where questions sit in the cycle, not what makes one better than another.
- Coverage is judged per benchmark. A quadrant missing from a benchmark is a gap in the benchmark as much as in the model, and the paper's gap claim depends on the authors' reading of those benchmarks.
- The paper's failure results (low exact match, weak feasibility) are reported per task, and the link from a quadrant-level deficit to a single model failure is not established in the slices read.

## Related

- [[novelty-feasibility-decoupling]] — two axes of the conception quadrant, scored separately in one study, with feasibility lagging novelty in a level comparison
- [[retrieval-dissimilarity-novelty-reward]] — a training reward aimed at the conception quadrant
- [[question-generativity]] — a notion of a question's value that the four-quadrant cycle does not name

[^c1]: arxiv-2512-16969 — "deconstructs the scientific process into a cycle of four core cognitive activities"
[^c2]: arxiv-2512-16969 — "Deliberation (the search, synthesis, and critical evaluation of knowledge)"
[^c3]: arxiv-2512-16969 — "An AI exhibiting true SGI must possess"
[^c4]: arxiv-2512-16969 — "Scientific Deep Research (Deliberation)"
[^c5]: arxiv-2512-16969 — "corresponding mainly to the Deliberation quadrant"
[^c6]: arxiv-2512-16969 — "Most current evaluations capture only fragments of the SGI spectrum."
