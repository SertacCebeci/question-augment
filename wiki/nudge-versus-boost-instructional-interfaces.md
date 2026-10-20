---
description: "Information-access features either steer a choice without explanation (nudging) or build the user's own search skill (boosting); only the second is argued to transfer across tasks."
aliases: ["nudging vs boosting", "search systems as instructive interfaces", "learning to search"]
sources: ["arxiv-2601-08035"]
---
# Nudge versus boost in instructive interfaces

A conceptual paper recasts search engines and generative assistants as didactic environments. Its useful split is between two ways an interface can change what a user asks and how they judge answers. A nudge steers a decision "without restricting choice" through interface structure, for example result positioning or visual cues. A boost aims to strengthen the user's own ability, for example by teaching how to evaluate credibility, formulate queries or compare sources.[^c1]

## Mechanism

Nudges cost the user almost no effort and work under time pressure or cognitive load. But they typically operate without explanation or reflection, so they build little transferable skill. If they are not transparent they can also be manipulative.[^c2] The paper labels nudging behaviourist: it "manipulates stimulus-response links without fostering conceptual understanding".[^c3]

Boosts promote autonomy, skill transfer and long-term competence, but they demand more effort, and their payoff depends on motivation, prior knowledge and the user's ability to apply the skill in context.[^c4] The paper labels boosting constructivist, since it builds mental models and strategies learners can apply across contexts.[^c5]

The paper places these among seven frameworks (adding scaffolding, cognitive apprenticeship, self-regulated learning, instructional feedback and heutagogy) that run from implicit, system-driven to explicit, learner-driven support. Applied to five features, the contrast is concrete. Query auto-completion is brief and one-way and gives no explanation or feedback. Source labels depend on users noticing and understanding them. A ReAct agent's visible reasoning trace shows how a complex query is solved, but users cannot control the plan, which limits engagement without additional scaffolding.[^c6] My reading, not the paper's measurement: the same feature moves along the axis depending on whether it explains itself, so "a suggestion" is a nudge and "a suggestion plus its reason and feedback on use" is closer to a boost.

Prior IIR studies cited as evidence that feedback can teach: showing effective example queries with immediate performance feedback helped users internalise patterns, and a dashboard comparing behaviour to expert benchmarks led to longer queries and more deliberate clicking over five weeks.[^c7] Boost interventions had mixed outcomes: some changed behaviour, while attempts to induce intellectual humility or guide reformulation with reflective prompts had weaker effects.[^c8]

## Limits

The paper is a conceptual analysis on two illustrative tasks (a coffee-and-growth claim, veganism) and five mock-ups; it reports no experiment of its own, so the claim that boosts transfer better than nudges is argued from the literature, not measured here. The nudge/boost labels follow the cited decision-science origin and the paper's own behaviourist/constructivist mapping, which is a classification, not a tested taxonomy. Related work it cites also shows that adding instructional scaffolding to web search changed behaviour without improving learning gains, and real-time feedback could distract.[^c9] Which interventions fade correctly, and for whom, is not established.

## Related

- [[question-autocompletion]] — the nudge case the paper uses: suggestions without explanation
- [[prompt-coach]] — an explicit coaching feature closer to the boost end
- [[scaffolding-collapse]] — scaffolding that fails to hold up, a limit on the support side
- [[receptivity-gated-counterfactual-nudge]] — nudging gated on user receptivity

[^c1]: arxiv-2601-08035 — "Unlike nudging, boosting aims to strengthen users’ own abilities, for example, by teaching how to evaluate information credibility, formulate effective queries, or compare sources."
[^c2]: arxiv-2601-08035 — "Nudges typically operate without explanation or reflection, which limits their value for building transferable skills or understanding."
[^c3]: arxiv-2601-08035 — "Nudging is behaviourist"
[^c4]: arxiv-2601-08035 — "Boosting promotes autonomy, skill transfer, and long-term competence."
[^c5]: arxiv-2601-08035 — "Boosting is constructivist: it builds mental models and strategies that learners can apply across contexts."
[^c6]: arxiv-2601-08035 — "users cannot control the agent’s plan or reasoning, limiting engagement and reflection without additional"
[^c7]: arxiv-2601-08035 — "participants exposed to expert comparisons"
[^c8]: arxiv-2601-08035 — "had weaker"
[^c9]: arxiv-2601-08035 — "adding instructional scaffolding to web search changes search"
