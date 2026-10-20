---
description: "A science-education scaffold — state a claim, cite evidence, connect it by reasoning — reused as an LLM prompt frame for generating questions, with mixed results."
aliases: ["CER", "Claim-Evidence-Reasoning"]
sources: ["ucar-2026"]
---
# Claim-Evidence-Reasoning (CER)

> A three-part scaffold for scientific argumentation — claim, evidence,
> reasoning — repurposed as an LLM prompt to force a generated question to
> require textual support, not just a topic.

## Definition / Mechanism

CER "emphasizes reasoning by guiding students to identify a central claim,
provide supporting evidence, and logically connect the evidence to the
claim (McNeill et al., 2006)," and is described by [[ucar-2026|Uçar et al.
(2026)]] as "particularly well-suited for engaging with complex scientific
concepts, making it a strong candidate for high-order questioning."[^c1]

As an LLM prompt frame — one of three tested groundings alongside Bloom's
Taxonomy and [[divergent-questioning|Divergent Questioning]] — CER-grounded
prompts stayed close to their own definition: "Six out of seven questions
included the key terms claim, evidence, and reasoning... indicating little
deviation from the definition of the framework," and in Spanish "all eight
questions included the term afirmación (affirmation), and key CER elements:
claim, evidence, and reasoning" Uçar et al. (2026).[^c2]

## Why it matters

Faithfulness to the source framework did not translate into a high-order
question: of the answerable CER-grounded questions, only 41.82% were rated
high-order by teachers — level with the *worst*-performing Bloom's-Taxonomy
grounding (Analyze, 38.18%) and well below Divergent Questioning (69.81%)
and Bloom's-Evaluate (64.71%) — see
[[high-order-question-framework-comparison]]. A prompt that reproduces its
scaffold's vocabulary exactly can still under-perform on the outcome the
scaffold was borrowed for.

## Transfer

| | |
|---|---|
| **Home field** | science education: CER is a writing/argumentation scaffold used to assess or coach a *student's* written argument (McNeill et al., 2006, as cited in Uçar et al. 2026) |
| **Here** | an LLM prompt instruction asking the model to generate a *question* that requires a student to produce a claim, cite evidence from a supplied text, and reason from one to the other |
| **What survives** | the three-part vocabulary and structure (claim / evidence / reasoning); generated questions reliably named all three elements |
| **What does not** | the framework's original role — scoring or scaffolding a student's own argument — carries no guarantee about the cognitive level of a *question* built around it; in this study it did not raise the high-order rate above the taxonomy's weakest level |

## Limits

- The claim about CER's origin and definition is read from [[ucar-2026|Uçar
  et al. (2026)]]'s own account, not verified against McNeill et al. (2006)
  directly — that primary source was not read for this note.
- One domain (secondary-school physics), one prompt template, two LLMs,
  three languages; "little deviation from the definition" is reported
  qualitatively (fractions out of 7–8 questions per language), not as a
  systematic count across the full sample.

## Related

[[high-order-question-framework-comparison]] · [[divergent-questioning]] · [[question-asking-as-program-generation]]

[^c1]: ucar-2026 — "emphasizes reasoning by guiding students to identify a central claim, provide supporting evidence, and logically connect the evidence to the claim (McNeill et al., 2006)"
[^c2]: ucar-2026 — "Six out of seven questions included the key terms claim, evidence, and reasoning, as can be seen in Q2, indicating little deviation from the deﬁnition of the framework."
