---
description: "An app that captures live context, guesses what the user is reporting, then asks adaptive follow-ups yields more complete reports than a text box, but the follow-ups drift to solutions."
aliases: ["context-aware feedback reporting", "FeedAIde", "adaptive in-app feedback elicitation"]
sources: ["arxiv-2603-04244"]
---
# App-context-grounded feedback elicitation

Instead of a blank text field, the reporting flow starts where the user is: a multimodal LLM reads the live app context, offers candidate interpretations of the issue (the user may enter their own), then asks adaptive follow-up questions to refine the report with the user.[^c1] The system also attaches what the user need not type: interaction logs, device information and product version.[^c2]

## What was measured

In a small user study the participants all preferred the context-aware flow to a plain text field. Ease of reporting was rated 3.71/4 and helpfulness 3.43/4, with helpfulness rising by 2.29 points.[^c3]

Two experts rated the resulting reports. Bug reports from the adaptive flow scored higher on observed behavior (1.50/2) and reproduction steps (2/2). The latter came from automatic interaction logging, not from questions.[^c4] For feature requests, descriptions went from 0% to 100% and product version from 0% to 100%.[^c5] The experts agreed almost perfectly (kappa 0.906 for bugs, 0.9207 for features).[^c6]

The mechanism, in short: much of the completeness gain came from context captured without asking, while the questions mainly added narrative detail the user would otherwise omit. This split is my reading of the tables, not a decomposition the paper ran.

## Where the questions fell short

Feature requests showed a failure of what the questions aimed at. Only 53.8% of adaptive reports specified the underlying problem (traditional: 0%). The experts noted that the follow-ups "often focused more on refining a solution rather than uncovering the underlying issue."[^c7] Users tend to state a solution rather than their problem. The UX expert argued that choosing the solution is the designer's job.[^c8] A follow-up that elaborates the user's stated solution therefore deepens the framing the asker should be questioning.

The model's first guess at the user's intent was right only about 30% of the time. When it was right, users reacted with clear enthusiasm.[^c9] Loading took 10 to 20 seconds per request, which every participant flagged.[^c10]

## Limits

- Tiny sample: only two bug reports and two feature requests were used as scenarios, so feedback types such as usability or content suggestions are untested; the authors say generalization needs replication.
- The comparison is against a bare text field, not against a static structured form. How much of the gain is adaptivity versus simply captured fields is not isolated (my inference).
- The about-30% hit rate is an observation, not a controlled measure.
- Whether users answer such follow-ups outside a lab study is untested here.

## Related

- [[on-demand-follow-up-generation]] — follow-ups generated from a short context window; there too, generation's contribution is hard to isolate
- [[follow-up-question-rescue-effect]] — follow-ups as repair of incomplete first answers
- [[outcome-aware-follow-up-elicitation]] — follow-ups steered by what the elicited information is for
- [[task-ambiguity]] — unspecified intent that the first report leaves open

[^c1]: arxiv-2603-04244 — "a context-aware, interactive feedback approach"
[^c2]: arxiv-2603-04244 — "FeedAIde automatically captured this information, achieving"
[^c3]: arxiv-2603-04244 — "the helpfulness score"
[^c4]: arxiv-2603-04244 — "FeedAIde automatically captured Steps to Reproduce through interaction logging"
[^c5]: arxiv-2603-04244 — "while FeedAIde automatically captured this information, achieving"
[^c6]: arxiv-2603-04244 — "was 𝜅 = 0.906 for the bug reports and 𝜅 = 0.9207 for the"
[^c7]: arxiv-2603-04244 — "often focused more on refining a solution rather than"
[^c8]: arxiv-2603-04244 — "users often describe a solution rather than their problem"
[^c9]: arxiv-2603-04244 — "were not always precise"
[^c10]: arxiv-2603-04244 — "the loading times ranged from 10 to 20 seconds per request"
