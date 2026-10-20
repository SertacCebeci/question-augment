---
description: "Instructions rewritten from prose into a numbered decision tree with sequencing rules and literal confirmation tokens; a single deployment reported a 5.6-point success-rate gain."
aliases: ["Decision Tree Protocol", "decision-tree prompt", "operational protocol prompt"]
sources: ["arxiv-2512-24040"]
---
# Decision tree protocol

A prompt can state an agent's procedure as prose or as a protocol. In prose, a step is a sentence the agent has to interpret. In the protocol form, the same step becomes a numbered branch: a condition, the action it selects, a fixed order between actions, and a check that must receive a literal reply before an action runs. The paper describes the move as one "from unstructured natural language to structured Decision Tree Protocols."[^c1]

The form has three parts, as the paper names them. Ambiguity resolution decomposes a goal into sub-steps. Sequencing rules fix an order the prose left open. Safety guardrails are "Introducing binary check-nodes"[^c2] that stop an agent acting on a loose reply. The example the authors give of the defect is an instruction that "is non-deterministic. It fails to specify which update should happen first."[^c3] The repaired version states that "address modifications must precede item modifications"[^c4] and asks for a literal "YES" before a state-changing call.[^c16]

The loop that writes the tree works on failures only. A filter "discards successful interactions and explicitly retains" the failure cases.[^c5] An analyser diagnoses each failure, an optimizer aggregates the diagnoses into a tree, and a coach edits the system prompt with it. The paper's stated reason the form should help is that it forces "a deterministic reasoning path that prevents the recurrence of" known errors.[^c6] The authors also claim that "a single 'debugged' failure" gives more information than hundreds of successes, but no run compares the two signals.[^c7]

What was measured. In a production knowledge-management agent, with no labelled data and "3 automated iterations"[^c8], the success rate rose "from 73.6% (Base Prompt) to" 79.2%.[^c9] The authors credit the trees with resolving "ambiguity in user intents that had previously resulted in conversational dead ends."[^c10] On the retail domain of a tool-use benchmark, one model went "from a baseline of 68.3% to a peak of 78.1% by Iteration 2"[^c11] and then fell back, while a smaller model rose and dipped before reaching its best score in the sixth iteration.[^c12] The baseline in every case was a prose prompt, described as "written in standard natural language prose."[^c13]

## Limits

- The form is never isolated. The optimized prompt differs from the baseline in form and in content (new rules, new branches) at the same time. Whether the same content written as prose would score the same is not tested. That reading is mine, from the design.
- The production result is one deployment, one run, three iterations. No variance or significance is reported, and the success metric counts interactions "without hallucination or logic errors",[^c17] judged in a way the text does not spell out.
- The gains are not monotone. The benchmark model regressed in its third iteration, and the authors suggest "further constraint injection beyond the second round may yield" diminishing returns or over-constraint.[^c14]
- The claim that the trees "effectively" reduce hallucination and logic errors is a design statement; the text reports no separate measurement of hallucination.[^c15]
- The one no-answer case (a forecast question the agent now declines) is a single before-and-after transcript, not a rate.[^c18]
- The tree is tuned on the failures it is later scored on. Held-out generalisation of the protocol is not reported.

## Related

- [[evolutionary-prompt-search]] — searches a population of wordings against a dev score; the protocol form instead replaces a wording with a diagnosed branch, and this paper's loop keeps no population.
- [[instruction-dilution-of-structured-reasoning]] — shows that the order a structured scaffold runs in can be lost inside a long prompt; a decision tree fixes order by its layout, which that note does not test.
- [[prompt-coach]] — also turns prompt weaknesses into targeted fixes, but asks the developer questions rather than rewriting the prompt for them.

[^c1]: arxiv-2512-24040 — "unstructured natural language to structured Decision Tree Protocols."
[^c2]: arxiv-2512-24040 — "Introducing binary check-nodes"
[^c3]: arxiv-2512-24040 — "is non-deterministic. It fails to specify which update should happen first"
[^c4]: arxiv-2512-24040 — "address modifications must precede item modifications"
[^c5]: arxiv-2512-24040 — "discards successful interactions and explicitly retains"
[^c6]: arxiv-2512-24040 — "forcing it into a deterministic reasoning path that prevents the recurrence of"
[^c7]: arxiv-2512-24040 — "than hundreds of successful rollouts"
[^c8]: arxiv-2512-24040 — "was executed for 3 automated iterations"
[^c9]: arxiv-2512-24040 — "The overall task completion rate improved from 73.6% (Base Prompt) to"
[^c10]: arxiv-2512-24040 — "resolved ambiguity in user intents that had previously resulted in conversational dead ends."
[^c11]: arxiv-2512-24040 — "jumping from a baseline of 68.3% to a peak of 78.1% by Iteration 2"
[^c12]: arxiv-2512-24040 — "The smaller model exhibited a more volatile learning"
[^c13]: arxiv-2512-24040 — "written in standard natural language prose."
[^c14]: arxiv-2512-24040 — "further constraint injection beyond the second round may yield"
[^c15]: arxiv-2512-24040 — "effectively reducing hallucination and logic errors"
[^c16]: arxiv-2512-24040 — "Ask for a Literal"
[^c17]: arxiv-2512-24040 — "without hallucination or logic errors"
[^c18]: arxiv-2512-24040 — "returned a standard disclaimer rather than fabricating a prediction."
