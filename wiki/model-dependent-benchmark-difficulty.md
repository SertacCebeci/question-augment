---
description: "In a negotiation benchmark, which game is hardest depends on the model tested, so one game's score does not give an objective cross-model comparison; format-parsing bugs also inflate a leakage metric."
aliases: ["game difficulty not aligned across models", "benchmark claim unsupported"]
sources: ["arxiv-2602-18230"]
---
# Model-dependent benchmark difficulty

A reproduction of the Scoreable Games negotiation benchmark tested whether a user can "objectively compare skills in multi-agent negotiation between different LLMs". The authors found the claim unsupported, because model performance is inconsistent across games.[^c1]

## Mechanism

Each model was run across all the negotiation games. Rankings of difficulty did not agree between models. Mistral-Small did well on games 1 and 2 but scored low on game 3. GPT-4o mini and Qwen2.5-72B struggled most with game 2, while GPT-4 and Mistral-Small found game 1 hardest.[^c2] The authors conclude: "a game's relative difficulty can vary significantly depending on the model evaluated."[^c3] Their reading is that difficulty is tied to unseen factors in game-agent dynamics, so a score on a single game is a score on a model-game pair. This parallels [[reformulation-method-ranking-instability]], where the ranking of methods shifts with the backbone.

A second validity problem sits in the measurement instrument. The leakage metric (how often an agent reveals private scoring information) was "heavily confounded by structural code behavior".[^c4] When a model omitted required answer tags, the system itself exposed confidential output. This made up most reported leakage in the authors' runs. Strong models such as GPT-4 followed the format, while smaller models often did not, so a format-compliance gap was scored as a behavioral difference.[^c5]

## Why it matters for asking and answering

An evaluation of answers or dialogue skill is only as portable as its item set and its parser. Comparing models on one item, or through a brittle output format, mixes ability with format-following. This is my inference from the two findings, not a result the paper states in this form.

## Limits

Only a handful of models and three games were used, and the extra metrics were the authors' own. The paper does not separate whether the inconsistency comes from game design, prompt sensitivity or sampling noise; no variance estimate over repeated runs of one model-game pair is cited here. The authors also say it "remains unclear" whether the leakage was a subversive attempt by the model. Their replacement baseline did not match the original numbers. Nothing here concerns asking questions directly.

## Related

- [[reformulation-method-ranking-instability]] — the same pattern for reformulation methods: rankings shift with the generating model.
- [[capacity-dependent-format-tax]] — format compliance differs by model capacity, which is the leakage-confound mechanism here.

[^c1]: arxiv-2602-18230 — "Using the framework provided, a user can objectively compare skills in multi-agent negotiation between different LLMs."
[^c2]: arxiv-2602-18230 — "GPT-4o mini and Qwen2.5-72B struggle most with"
[^c3]: arxiv-2602-18230 — "a game’s relative difficulty can vary significantly depending on the model"
[^c4]: arxiv-2602-18230 — "heavily confounded by structural code behavior"
[^c5]: arxiv-2602-18230 — "smaller models often failed to do so, causing"
