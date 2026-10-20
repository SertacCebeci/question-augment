---
description: "Splitting a prompt's requirements into atomic yes/no criteria questions, scored over many responses and editable by the user, surfaces misalignment and the user's own unstated requirements."
aliases: ["criteria questions", "instruction-level alignment report", "CoPrompter criteria generation"]
sources: ["doi-10-48550-arxiv-2411-06099"]
---
# Atomic criteria questions for prompt alignment

CoPrompter takes a user's prompt requirements ("guidelines") and decomposes them into atomic instructions, each a single requirement. Each atomic instruction becomes a criteria question (CQ) with a ground-truth label, for example "Does the conclusion include a bullet list of three specific takeaways?" with ground truth Yes.[^c1] The design aim is that decomposition "makes it easier to identify and address specific areas of misalignment."[^c2]

## Mechanism

1. **Decompose.** One compound instruction (a bullet list of takeaways that gives actionable advice) is split into two atomic instructions, and each becomes its own question.[^c1] Each question also gets a priority tag (main task, subtask, format) and metadata tags such as content vs. style and subjective vs. objective.[^c3]
2. **Flag subjectivity.** Subjective criteria such as "concise summary" are shown with several interpretations, since "concise" may mean 2-3 lines in one context and 10-15 in another. The user then adds a clarification.[^c4] The formative study had linked subjective instructions to misalignment from differing interpretations between engineer and model.
3. **Typed criteria.** Users can add measurable criteria (a word count or range), descriptive yes/no criteria, and layered measurable criteria that first locate a section and then apply a numeric check.[^c5]
4. **Score many responses.** The prompt is run several times (participants chose 5 to 10 responses). Each response is judged against every criterion, and the report aggregates per criterion, per category and overall. It shows which criteria fail most often, so changes can be prioritized.[^c6]
5. **Edit the criteria, not only the prompt.** Users can add, delete or modify criteria, and changes are versioned so only the latest version is used.[^c4]

## What was observed

In a formative survey, participants' typical prompts held 5-10 instructions, and the majority said an acceptable prompt took 10+ attempts and 40+ response evaluations.[^c7] The reported failure types were overlooked instructions, hallucinated content, misinterpreted details and inconsistent responses.[^c8]

In the evaluation with 8 industry prompt engineers, the breakdown itself did work beyond scoring. Seeing guidelines in chunks helped them find requirements that were missing or needed revising, and one participant revised an instruction they had hardly considered when drafting it.[^c9] Participants also edited the criteria after seeing responses, for example rewriting a vague audience criterion into a more specific one. Responses revealed requirements the user had not yet articulated.[^c10] Per-score rationales let them see when the LLM judge misread a criterion, which they valued given worries about LLM-as-judge.[^c11] When a criterion showed 0% alignment (a 50-100 word limit), one participant added emphasis wording to the prompt.[^c12]

My reading, not the paper's claim: the criteria list works as an externalized, editable statement of intent. Asking about a prompt well involves clarifying what one wants, and the evaluator's decomposition prompts that clarification before any response is judged.

## Limits

- The evaluation was a small qualitative study (8 participants) with self-reported satisfaction; no controlled comparison against a baseline workflow is established here.
- The criteria questions and the alignment scores both come from an LLM. Judge accuracy against human labels is not what the study measures, and participants did sometimes disagree with the scores. Judge reliability is treated in [[llm-judge-validation-gap]].
- Participants were advised to keep criteria to 10 for latency, so behavior with long criteria lists is untested.
- One participant found the priority tags arbitrary and misaligned with their priorities.[^c13]
- Whether better alignment scores mean better downstream task outcomes is not shown.

## Related

- [[checklist-diagnostic-decomposition]] — also replaces one holistic question with independent binary questions, there to classify rather than to grade a response
- [[llm-judge-validation-gap]] — the reliability question this per-criterion LLM judging inherits
- [[llm-judge-biases]] — known biases of the judge that scores each criterion
- [[expert-report-derived-atomic-rubrics]] — atomic rubric items derived from a source, here derived from the user's own prompt
- [[recursive-rubric-decomposition]] — decomposing criteria further, as opposed to a single flat atomic split

[^c1]: doi-10-48550-arxiv-2411-06099 — "Corresponding Criteria Question: Does the conclusion include a bullet list of three specific takeaways?"
[^c2]: doi-10-48550-arxiv-2411-06099 — "and address specific areas of misalignment."
[^c3]: doi-10-48550-arxiv-2411-06099 — "priority tags (e.g., main task, subtask, or"
[^c4]: doi-10-48550-arxiv-2411-06099 — "All changes are tracked and versioned to ensure only the"
[^c5]: doi-10-48550-arxiv-2411-06099 — "Layered Measurable allows users to set complex evaluation criteria that first identify a specific section"
[^c6]: doi-10-48550-arxiv-2411-06099 — "consolidates areas where requirements were not met and shows which criteria fail most frequently, helping"
[^c7]: doi-10-48550-arxiv-2411-06099 — "participants expressed that it took 10+ attempts and evaluation of 40+ responses to reach an optimized prompt."
[^c8]: doi-10-48550-arxiv-2411-06099 — "including overlooked or ignored instructions, hallucinated content, misinterpreted details, and inconsistent responses across multiple interactions."
[^c9]: doi-10-48550-arxiv-2411-06099 — "Participants mentioned that seeing their guidelines broken down into chunks helped them understand their requirements better and"
[^c10]: doi-10-48550-arxiv-2411-06099 — "Participants also discovered new checks they would want to make on their responses based on new requirements."
[^c11]: doi-10-48550-arxiv-2411-06099 — "Some participants also expressed concerns over using LLM as a judge, in this case, reasonings helped"
[^c12]: doi-10-48550-arxiv-2411-06099 — "laid more emphasis on the instruction by adding phrases like ’Make sure’ before the word length instruction."
[^c13]: doi-10-48550-arxiv-2411-06099 — "However, P2 found"
