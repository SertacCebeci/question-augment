---
description: "A simulated user prompted with a detailed profile trades profile fidelity against human-like style: unconstrained it caricatures and runs long; constrained, its variety collapses."
aliases: ["persona-style-transparency trade-off", "caricature trap in simulated patients", "profile fidelity versus conversational realism"]
sources: ["arxiv-2511-18491"]
---
# Profile adherence versus style in simulated users

A simulated user is usually an LLM given a description of a person and asked to answer as that person. The description pulls in two directions. The more detail it carries, the more the model keeps the stated history, symptoms and goal; but the model also starts to play the description, and the text takes on the tone the description implies. MindEval, a benchmark that puts a clinician model in conversation with a simulated patient, reports the first failure in these words: "LLMs often embodied a caricature of the profile, rather than a realistic human being."[^c1] Its example is a 60-year-old lawyer traumatised by an old case, whom the model makes too ominous: such a patient "would sound excessively ominous and pensive."[^c10]

Restrict the style, and the other failure appears. The authors write that "too many restrictions on style and presence would collapse the LLM into a handful of modes common to all profiles".[^c2] Their examples of such modes are never sharing anything, or always writing a single sentence. The result is a simulator that is realistic in each turn and uniform across patients, so the benchmark tests fewer kinds of person.

A third failure concerns cooperation. The expert annotators noted that the simulated patients "shared very openly, which runs counter to the variability that would be expected across" real individuals.[^c3] One psychologist put it more bluntly: "The patient LLM often felt too easy to work with."[^c4] The simulated patient accepts suggestions and gives information quickly. For someone answering, such a user is a generous interlocutor; a real one resists, and an answer that works on a cooperative patient may not work on a resistant one. The paper does not measure this effect on scores; it is my reading of the expert comment.

The paper measures closeness to human style directly. Ten psychologists were hired to play patients from 20 profiles in 25-minute sessions with a clinician model, and their turns were compared with turns the same model produced under different prompts. Each turn was embedded, the embeddings were reduced by t-SNE, and the mean distance to the human turns was taken. The full prompt, with the profile and the formatting rules both in place, is the closest to human text on average: its mean distance is 40.48, against 63.56 for a simple prompt.[^c5] The formatting rules alone give human-looking text, though with much less variability,[^c9] while removing all instructions gives text "not faithful to the patient profile, or writing style".[^c6] The authors' summary is that the prompt "guides the LLM to be more faithful to the patient profile, while preserving a more human-like writing style."[^c7]

Verbosity belongs to the same trade-off. Text produced without formatting instructions "is almost 10 times longer than human text."[^c8] Length is a style property that a profile does not fix, and it is one the judge also has to penalise separately if it matters.

## Limits

- The realism measure is a distance between two clouds of embedded turns. It does not show that any single simulated turn would pass for human, and it compares against ten psychologists playing patients, not against real patients.
- The comparison is at the level of turns; the claim that long, drifting sessions are realistic is not tested. The paper names the longitudinal dynamics of therapy as outside what its interactions capture.
- The trade-off is described and partly mitigated by one prompt, not resolved. The authors call the patient model a limitation and do not measure an alternative that removes the caricature without the collapse.
- Whether a more realistic simulated user changes which answerers score well is not shown in the parts read. The benchmark's scores depend on the simulator, and no run compares rankings under a less cooperative simulator (my inference).
- The same family of failure appears in simulated survey respondents, where the spread is compressed; see [[simulated-respondent-variance-deficit]]. Whether the mechanism is the same there is not established.

## Related

- [[user-response-persona-simulation]] — a simulator with six discrete reply personas; the same question of how a profile becomes a reply, but with categories rather than a free-text backstory
- [[task-state-grounded-user-simulation]] — a simulated user that tracks task state to keep its behaviour consistent; a different remedy for a simulator that drifts from its profile
- [[simulated-respondent-variance-deficit]] — simulated respondents spread less than humans; the collapse to a few modes is the same loss of spread, seen in a conversation
- [[llm-judge-validation-gap]] — the judge side of the same benchmark: the simulated patient and the judge both need checking against people

[^c1]: arxiv-2511-18491 — "LLMs often embodied a caricature of"
[^c2]: arxiv-2511-18491 — "too many restrictions on style and presence would collapse the LLM into a handful of modes common to all profiles"
[^c3]: arxiv-2511-18491 — "shared very openly, which runs counter to the variability that would be expected across"
[^c4]: arxiv-2511-18491 — "The patient LLM often felt too easy to work with."
[^c5]: arxiv-2511-18491 — "turns generated with the M IND E VAL prompt are closest to human turns, on average"
[^c6]: arxiv-2511-18491 — "Removing all instructions yields text that is not faithful to the patient profile, or writing style"
[^c7]: arxiv-2511-18491 — "it guides the LLM to be more faithful to the patient profile, while preserving a more human-like writing style"
[^c8]: arxiv-2511-18491 — "text generated without any formatting instructions is almost 10 times longer than human text."
[^c9]: arxiv-2511-18491 — "though with much less variability"
[^c10]: arxiv-2511-18491 — "would sound excessively ominous and pensive."
