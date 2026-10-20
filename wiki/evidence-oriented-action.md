---
description: "After the goal is met, an agent may take extra actions whose only purpose is to make its success visible, because a judge treats what the history does not show as not having happened."
aliases: ["evidence-oriented action", "evidence creation", "proof-generating action", "creative evidence seeking", "post-goal verification action"]
sources: ["arxiv-2512-22322"]
---
# Evidence-oriented action

An agent acting on a task performs two kinds of action, and the paper separates them on purpose. Task-oriented actions are the ones taken to achieve the goal. Evidence-oriented actions are different: they "may be taken after the goal is met, with the sole intent of generating a better proof."[^d1][^d2] The second kind does not advance the task; it exists to make the first kind's result checkable.

The motivating case is installing a browser extension. The task-oriented step is clicking "Add extension" in a confirmation dialog. The dialog disappearing after that click is weak support for success, since it does not show the extension loaded, which is "thus constituting weak evidence."[^d3] The evidence-oriented step is to leave the web page and look at the browser's toolbar for the new icon: "This inspection forms a perfect evidence-oriented action."[^d4]

The paper's Creativity principle gives the rule: "If the necessary evidence does not exist in the interaction history, the agent is encouraged" "to create it by taking additional actions."[^d5][^d6] The agent moves from a historian of its own actions to an investigator who looks for an observable consequence it has not yet recorded. The paper's bet is that this capability "is the key to achieving true robustness in agentic RL."[^d7]

The mechanism works through the verifier. A judge that treats absence as failure makes a silent history worthless however well the task was done, because "What is not shown in the evidence is assumed not to have happened."[^d8] An evidence-oriented action converts a silent success into a visible one. Its output then becomes an exhibit that can be indexed into the curated set described in [[minimal-decisive-evidence-set]].

The paper also argues that the habit has a training side. Creating evidence requires searching "a broader state space that includes the entire sandbox," which the paper says helps meet both completeness and conciseness. It adds that the practice "implicitly incentivizes reasoning and reflection of agent for active collection of evidence according to the environment feedback."[^d9] That is the paper's claim about learning, not a measured effect of this principle in isolation.

## Limits

- The only worked case is the browser-extension example and the checklist in the paper's Figure 3, a transaction recorded in a finance app. The sections read give no measured rate of how often evidence-oriented actions occur, nor how often they change the verdict.
- The claim that creation is "the key" is an assertion. The sections read contain no run that compares a Creativity-guided agent with one that reuses only its task history, so the principle is not separated from the completeness and conciseness rewards it sits beside.
- The composite reward in the paper has four named terms: format, validity, completeness and conciseness. None rewards creating evidence as such. Any pressure toward evidence-oriented action is therefore indirect, through the completeness outcome. This reading is my inference from the reward's structure.
- An extra action after the goal can change the state it is meant to observe, for instance by opening a screen that refreshes or by triggering a save. The paper's examples do not address this side effect. It is my inference that the check is only as good as the observation it makes.
- Evidence-oriented actions are the paper's own proposal for GUI tasks, where a screen can show the outcome. Whether tasks with no observable end state, such as a claim or a derivation, admit an equivalent action is untested.

## Related

- [[minimal-decisive-evidence-set]] — the curated set that these actions feed, and the verifier rule that makes them necessary
- [[sufficiency-gated-imagination]] — a parallel question: extra generated evidence helps some queries and hurts others, so when to generate it is itself a decision
- [[tool-type-confidence-dichotomy]] — evidence-gathering tools and verification tools move confidence in opposite directions; an evidence-oriented action sits on the verification side of that split

[^d1]: arxiv-2512-22322 — "evidence-oriented actions, which may be taken after the goal is met, with the"
[^d2]: arxiv-2512-22322 — "sole intent of generating a better proof."
[^d3]: arxiv-2512-22322 — "thus constituting weak evidence."
[^d4]: arxiv-2512-22322 — "This inspection forms a perfect evidence-oriented action."
[^d5]: arxiv-2512-22322 — "If the necessary evidence does not exist in the interaction history, the agent is encouraged"
[^d6]: arxiv-2512-22322 — "to create it by taking additional actions."
[^d7]: arxiv-2512-22322 — "Such capability to create evidence is the key to achieving true robustness in agentic RL"
[^d8]: arxiv-2512-22322 — "What is not shown in the evidence is assumed not to have happened."
[^d9]: arxiv-2512-22322 — "It implicitly incentivizes reasoning and reflection of agent for"
