---
description: "A clarifier grounds what to ask in the live target system's own state — crawling it, diffing its form fields against the scenario description, and naming only the delta."
aliases: ["WebMAC clarification module", "Clarifier-Coder-Executor-Analyst pipeline"]
sources: ["arxiv-2604-13559"]
---
# Execution-grounded gap clarification

> Do not ask the user what might be missing — execute against the target
> system, read what actually exists, and ask only about the difference.

## Definition / Mechanism

Wan, Chen, Huang & Xie (2026) build WebMAC's
clarification module as a pipeline of role agents rather than one LLM call:
a Coder writes a script that crawls the target web page, an Executor runs
it, and an Analyst turns the returned HTML into a structured account of
what interactive elements the page actually contains, then decides —
`IsClarify` — whether the tester's Gherkin-form scenario description
covers all of them: "The Analyst will analyze four aspects: script
execution (whether it runs successfully), web system functional
components, web system description, and whether the test scenario needs
to be clarified."[^c2]

When the two disagree, the Clarifier does not ask a generic "is anything
missing?" — it asks for exactly the fields present on the live page but
absent from the description: "The When statement in the initial
instantiated test scenario only contains the first name and last name
fields, while the webpage contains five form components, namely first
name, last name, address, city, and telephone. Therefore, the Clarifier
asks a clarification question for the components not mentioned in the
test scenario, 'What do you need to add for the user's address, city, and
telephone?'." A Rewriter folds the tester's answer back into the
scenario; a Summarizer distills the exchange into the JSON contract the
next module consumes.[^c1]

The system under test, not the description or the tester, is the source of
the reference set against which "missing" is defined; the question's
content is a set difference, not an inference over language alone. Full
crawled HTML is filtered to interactive elements by regular expression
first, because unfiltered page markup is too noisy for the Analyst to
diff reliably.

## Why it matters

Against a baseline that infers missing fields only from post-hoc execution
errors ("address is null") and fills gaps with placeholders, grounding the
question in a direct read of the target system's actual required fields
removes both the guesswork and the trial-and-error iteration: "WebMAC
improves the execution success rate of generated test scripts by 30%–60%,
increases testing efficiency by 29%, and reduces token consumption by
47.6%."[^c3]

This names a fourth answer to "where does the constraint come
from" beside the user, a knowledge base, or the environment-as-oracle of
[[ambiguity-driven-execution-probing]]: the environment probed not to
resolve an existing ambiguity but to *generate the question itself*,
turning "what should I ask" into a diff against ground truth rather than a
language-only judgment call as in [[interopt-gap-guided-clarification]].

## Limits

The mechanism requires an executable, crawlable target with a legible
notion of required fields (a web form); it gives no procedure for a target
without that structure, or where "missing" cannot be read off structured
elements (e.g. a semantic rather than a slot-filling gap). It is
evaluated on four small web systems with one baseline and one backbone
family; the paper reports no result for targets whose completeness cannot
be determined by crawling alone.

## Related

[[ambiguity-driven-execution-probing]] · [[interopt-gap-guided-clarification]] · [[clarification-request]] · [[expected-information-gain]]

[^c1]: arxiv-2604-13559 — "The When statement in the initial instantiated test scenario only contains the first name and last name fields, while the webpage contains five form components, namely first name, last name, address, city, and telephone. Therefore, the Clarifier asks a clarification question for the components not mentioned in the test scenario, “What do you need to add for the user’s address, city, and telephone?”."
[^c2]: arxiv-2604-13559 — "The Analyst will analyze four aspects: script execution (whether it runs successfully), web system functional components, web system description, and whether the test scenario needs to be clarified."
[^c3]: arxiv-2604-13559 — "WebMAC improves the execution success rate of generated test scripts by 30%–60%, increases testing efficiency by 29%, and reduces token consumption by 47.6%."
