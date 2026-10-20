---
description: "Prompt templates are ranked by humans choosing between paired outputs, scored with Glicko2 and adaptively sampled toward the top two, exposing large gaps that theory-grounding did not predict."
aliases: ["prompt tournament", "tournament-style prompt evaluation", "comparative-judgment prompt evaluation", "Glicko2 prompt ranking"]
sources: ["doi-10-48550-arxiv-2601-16134"]
---
# Prompt Tournament Evaluation

Prompts are usually refined ad hoc: a designer sees a failure and patches the text. The work argues that "few if any researchers describe the formal process by which prompt performance was evaluated."[^c1] The tournament replaces this with a ranking procedure. Each prompt template generates an output (here, a follow-up question in a reading-support dialogue) for the same real learner interaction. Judges see two outputs from two different templates and pick the one they prefer, or skip. This is comparative judgment: a preference between options, "rather than assigning an absolute score to a single sample at a time."[^c2]

## Mechanism

Ratings come from the Glicko2 system, which keeps for each competitor a rating, a rating deviation (reliability) and a volatility. It also yields a Bradley-Terry win probability for every pair of prompts, "the estimated probability that one prompt's output will be preferred over another."[^c3]

Sampling is adaptive. After each round "the system identifies the two prompts with the highest ratings and schedules them for additional head-to-head evaluation," so annotator effort goes to separating the leading candidates.[^c4] The cost is uneven coverage: trials per matchup ranged from 0 to 91, and some pairs (for example two weaker templates) were never compared.[^c5]

Judges used a holistic three-part rubric (format, dialogue support, appropriateness for adult learners) and chose rather than scored, because this "was chosen to better capture the nuanced differences in response quality that emerge from the interaction of multiple criteria."[^c6] The rubric was trained with example pairs. Eight judges made 213 decisions over 120 real interactions drawn from three deployments.[^c7]

## What it showed

Six templates were compared: a Baseline plus five built from prompt patterns (Persona, Cognitive Verifier, Context Manager, Alternative Approaches) and learning theory. The Strategic Reading Coach (persona plus context manager, aimed at metacognitive strategy) beat the second-ranked Scaffolding Expert with probability 0.81 over 55 trials and beat every other template with probability at least 0.90.[^c8] The old Baseline placed third, and the Scaffolding Expert beat it with probability 1.00.[^c9] The Connection Builder, grounded in constructivist theory, did poorly, which the authors read as showing "that theoretical alignment alone does not guarantee effective prompt performance."[^c10]

The authors also note that the design lets prompt and model combinations be ranked in one tournament, since the same prompt can behave differently on another model.[^c11]

## Limits

- One model (Llama 3), one task (follow-up questions after a self-explanation question), one rubric; the authors say the prompt-level findings may not generalize.[^c12]
- Judges were members of the development team, familiar with the context. Their preferences may not match learners' outcomes; no learning outcome was measured. This is my reading of the design, not a test the paper ran.
- The pattern-level explanation (persona plus context manager "works well together") is confounded: each template differs in wording, length (Baseline 374 words versus 117-192 for the rest) and pedagogical stance, so patterns were not isolated. This is my inference.
- Adaptive sampling leaves most lower-ranked pairs with 0-3 trials, so win probabilities there rest on very little data; the 1.00 values with 1 trial are not strong evidence.
- Judge bias, agreement and position effects are not reported.

## Related

- [[recursive-comparative-judgment]] — a different use of the term: pruning a candidate pool, not ranking prompts by preference
- [[llm-judge-biases]] — the judge here was human, but swapping in an LLM judge would import these biases
- [[socratic-question-type-utility]] — what makes a follow-up or Socratic question useful, the quality the rubric tried to capture

[^c1]: doi-10-48550-arxiv-2601-16134 — "few if any researchers describe the formal process by which prompt performance was evaluated"
[^c2]: doi-10-48550-arxiv-2601-16134 — "rather than assigning an absolute score to a single sample at a time"
[^c3]: doi-10-48550-arxiv-2601-16134 — "the estimated probability that one prompt’s output will be preferred over another"
[^c4]: doi-10-48550-arxiv-2601-16134 — "the system identifies the two prompts with the highest ratings and schedules them for additional head-to-head evaluation"
[^c5]: doi-10-48550-arxiv-2601-16134 — "The number of trials varies between matchups, from 0 to 91"
[^c6]: doi-10-48550-arxiv-2601-16134 — "to better capture the nuanced differences in response quality that emerge from the interaction of multiple criteria"
[^c7]: doi-10-48550-arxiv-2601-16134 — "In total, judges made 213 preference decisions."
[^c8]: doi-10-48550-arxiv-2601-16134 — "win probabilities of at least 90% compared to all other prompts"
[^c9]: doi-10-48550-arxiv-2601-16134 — "Against the Baseline template, it achieved a 100% win probability."
[^c10]: doi-10-48550-arxiv-2601-16134 — "suggests that theoretical alignment alone does not guarantee"
[^c11]: doi-10-48550-arxiv-2601-16134 — "different combinations of prompt and LLM can be evaluated simultaneously"
[^c12]: doi-10-48550-arxiv-2601-16134 — "might not generalize beyond this context"
