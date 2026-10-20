---
description: "Whether users fact-check a chatbot answer is set mainly by their own trust and habits, not by the answer or by tool access; both over- and underreliance persist with search at hand."
aliases: ["decision to verify", "verification behavior as user-dependent"]
sources: ["doi-10-48550-arxiv-2605-28498", "arxiv-2512-22418"]
---
# User-driven verification decision

In a within-subjects question-answering experiment (N=199, six questions, three chatbot answers correct and three incorrect, a browser extension recording visited URLs), participants could freely consult other AI chatbots or the web. Access to fact-checking did not remove reliance: the authors report that "Overreliance and underreliance persist despite access to fact-checking tools."[^c1] Most participants did verify: "The vast majority (87%) interacted with at least one fact-checking tool", yet this "does not necessarily indicate the absence of reliance."[^c2]

## Mechanism

The strongest determinant of all three behavioral measures (URL count, AI-source visits, non-AI visits) was the participant, not the question: "Some participants were prone to verify or not verify the answer regardless of the context."[^c3] Prior trust in chatbots was the most significant fixed-effect predictor. It raised interaction with the experiment chatbot but lowered checking with other sources, more so for non-AI URLs.[^c4]

Two failure modes follow. Overreliance: high-trust users used the same chatbot that gave the answer as the checker. Underreliance: users who judged a question too difficult for the chatbot agreed with it less, which rejected incorrect answers but also dismissed correct ones.[^c5]

Verification can also be shallow because of anchoring: sources were validated by alignment, but "this alignment was anchored to the chatbot's answer, as it was the first information source they encountered", so one corroborating source counted as enough, which is why non-AI URL count did not predict accuracy.[^c6] Consulting additional AI sources did predict accuracy; chatbot literacy did not change whether users verified but improved accuracy when the chatbot was wrong, which the authors read as better evaluation during verification (their interpretation).[^c7]

A qualitative study of vibe coding reads trust in AI-generated code as modes rather than one setting. Its coders trusted AI "purposively, unwillingly, or selectively".[^c9] The selective mode was the more common one: "coders demonstrated selective trust, calibrating when to rely on AI and when to intervene".[^c10] Some coders treated certain tasks as "not worth careful verification".[^c11] The vibe-coding paper is a tension with the experiment above, which found the decision set mainly by the participant. Its statements come from video, not from measured verification rates, so the two readings stand side by side: task calibration in one, participant disposition in the other.

## Limits

- Participants installed a tracking extension; many abandoned at the introduction, so the sample may be unrepresentative, and off-browser checking was untracked.[^c8]
- The answers participants met in external tools were not recorded, and AI tools are nondeterministic.
- The "persistence" and "anchoring" readings are the authors' inference from behavior; only 25.6% stated a default trust stance.
- Six self-authored questions; no test of other domains.

## Related

- [[user-driven-sycophancy]] — the model-side counterpart: assistants reinforcing the user's hypothesis
- [[social-sycophancy]] — agreeable assistant behavior that invites the reliance measured here
- [[warmth-induced-agreement-under-uncertainty]] — the style effect on agreement in the same study

[^c1]: doi-10-48550-arxiv-2605-28498 — "Overreliance and underreliance persist despite access to fact-checking"
[^c2]: doi-10-48550-arxiv-2605-28498 — "The vast majority (87%) interacted with at least one fact-checking tool throughout the"
[^c3]: doi-10-48550-arxiv-2605-28498 — "Some participants were prone to verify or not verify"
[^c4]: doi-10-48550-arxiv-2605-28498 — "Existing trust in chatbots was the most significant predictor of verification behavior between fixed-effects"
[^c5]: doi-10-48550-arxiv-2605-28498 — "While this skepticism helped participants reject incorrect answers, it also led them to dismiss correct ones."
[^c6]: doi-10-48550-arxiv-2605-28498 — "this alignment was anchored to"
[^c7]: doi-10-48550-arxiv-2605-28498 — "This suggests that chatbot literacy influences not whether users verify, but how"
[^c8]: doi-10-48550-arxiv-2605-28498 — "people who agree to install an extension might not"
[^c9]: arxiv-2512-22418 — "Vibe coders purposively, unwillingly, or selectively trust AI"
[^c10]: arxiv-2512-22418 — "More often, coders demonstrated selective trust, calibrating when to rely on AI and when"
[^c11]: arxiv-2512-22418 — "Professional programmers selectively treated certain tasks as not worth careful"
