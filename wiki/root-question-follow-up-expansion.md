---
description: "Each root question is expanded for a fixed number of rounds: an LLM proposes several follow-ups, a scorer keeps one, and that question's answer seeds the next round."
aliases: ["Follow-Up Question Composer", "root-question expansion", "depth-bounded follow-up questioning"]
sources: ["arxiv-2512-13297"]
---
# Root-question follow-up expansion

An inquiry started from a set of root questions can be grown into a short tree rather than answered once. In MedInsightAgent, the Visual Root Finder first produces the roots from the image, the goal and retrieved background. The motive given for the second stage is that the roots alone are weak: "The initial set of root question often suffers from coverage limitations and stochastic variability."[^c1]

The second stage is the Follow-Up Question Composer. For a root question and its answer, a generator writes n candidate follow-ups, and "Then the Question Selector S scores each candidate and selects the highest-scoring one".[^c2] Candidates must satisfy two conditions: relevance to the image and the goal, and that they "must be distinct yet logically derived from the original root question, extending the inquiry".[^c3] The chosen follow-up is answered from the image, and the cycle repeats.

Depth is a parameter, not a stopping rule set by the answer. "Each root question is expanded through p rounds before" termination, and the system then outputs everything accumulated.[^c4] The reported setup uses four rounds with three new questions per round.[^c5] The paper's count of final insights, r × (q + 1) for r roots, is my reading of the same tree: each root contributes itself plus one insight per round. The count writes the depth as q where the prose writes it as p.

What the mechanism is credited with is measured by ablation on GPT-4o. The authors conclude that "multi-round iteration questioning is crucial for deeper exploration and more novel insights."[^c6] In the extracted Table 4, removing the composer gives Insight Recall 0.314 (against 0.361 for the full agent), F1 0.338 (against 0.384) and novelty 0.233 (against 0.270). These are the largest drops among the single-component removals. The text, however, says the Image-Analysis Tool "has the greatest impact" on the quality metrics, so the row alignment of the extracted table is uncertain and the numbers should be read as approximate.

The mechanism is therefore a pool of candidates, a selector, and a fixed depth. It differs from a single chain of questions conditioned on prior turns, as in [[chain-of-inquiry-scaffolding-effect]], because here the branching happens at each step and only one branch is kept. It also differs from ranking a pool by expected information, as in [[retrieval-conditioned-question-selection]], because the selector is an LLM judging relevance and distinctness rather than a learned value of a question.

## Limits

- The selector's scoring criterion is not given in the sections read, so the claim that choosing the best of n matters, as against asking one follow-up or asking all n, is untested here. The ablation removes the whole composer, which removes both the extra depth and the selection together.
- The metrics are judged by language models: G-Eval is "calculated as the average of the GPT-3.5Turbo and Gemini 2.5 Pro scores," alongside ROUGE-1. The reported results are from a single run at temperature 0, with no variance shown, so differences of a few hundredths are not established.[^c7]
- Extra depth does not remove redundancy. The paper finds that high precision causes repetition: "this reduces spurious assertions, it also increases redundancy, with many high-scoring insights being".[^c8]
- The evidence is one domain, 332 pathology cases drawn from one cancer data source, and the authors admit that "some outputs remain overly conceptual".[^c9]
- Whether depth helps a human asker, or a chat model asked in a different domain, is not tested.

## Related

- [[chain-of-inquiry-scaffolding-effect]] — an ordered single chain of questions conditioned on prior turns; this note adds branching from several roots with a selector at each step
- [[retrieval-conditioned-question-selection]] — ranks a candidate question pool by a learned score; the selector here is an LLM judging relevance and distinctness
- [[self-ask-decomposition]] — the model emits its own follow-up questions one at a time; here candidates are generated in a batch and one is kept
- [[four-causes-follow-up-generation]] — fixes the follow-up slots per turn in advance; here the slate is open and the choice is made by a scorer

[^c1]: arxiv-2512-13297 — "The initial set of root question often suffers from coverage limitations and stochastic variability."
[^c2]: arxiv-2512-13297 — "Then the Question Selector S scores each candidate and selects the highest-scoring one"
[^c3]: arxiv-2512-13297 — "They must be distinct yet logically derived from the original root question, extending the inquiry"
[^c4]: arxiv-2512-13297 — "Each root question is expanded through p rounds before"
[^c5]: arxiv-2512-13297 — "our MedInsightAgent, we run 4 rounds of iterations, with 3 new questions generated in each round."
[^c6]: arxiv-2512-13297 — "Further ablations on the Follow-up Question Composer demonstrate that multi-round iteration questioning is crucial for deeper exploration and more novel insights."
[^c7]: arxiv-2512-13297 — "All LMMs are configured with a temperature of 0 to ensure deterministic output."
[^c8]: arxiv-2512-13297 — "this reduces spurious assertions, it also increases redundancy, with many high-scoring insights being"
[^c9]: arxiv-2512-13297 — "although some outputs remain overly conceptual"
