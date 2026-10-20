---
description: "Naming a pedagogical framework in an LLM prompt does not reliably yield a high-order question; the framework named changes the yield by ~25 points."
aliases: ["teacher-judged high-order question rate", "CER vs Bloom's Taxonomy vs Divergent Questioning"]
sources: ["ucar-2026"]
---
# High-order question framework comparison

> Prompting an LLM with a named pedagogical framework does not reliably
> produce a high-order question: which framework you name changes the yield
> by roughly 25 percentage points, and none reaches even 70%.

## Definition / Mechanism

Llama3.1_70B and GPT-4 were each prompted, once per framework, to write five
questions per source text (30 secondary-school physics texts × 3 languages —
Basque, Spanish, English), grounding the prompt in one of three educational
frameworks in turn: Bloom's Taxonomy (at the Analyze, Evaluate or Create
level), Claim-Evidence-Reasoning (CER), or [[divergent-questioning|Divergent Questioning]] — 300
questions total. Secondary-school teachers then rated each answerable
question on Bloom's Taxonomy level (Remember … Create); Analyze/Evaluate/
Create count as high-order.

Of the answerable questions, "slightly more than half (50.41%) of the
questions [were] classified as high-order questions (i.e., Analyze, Evaluate
or Create)" Uçar et al. (2026), out of "nearly 77%" judged
answerable at all.[^c1]

Broken down by the prompt's grounding framework: "the divergent questioning
(69.81%) and Bloom's Taxonomy Evaluate (64.71%) prompts were most successful
in generating high-order questions... Bloom's Taxonomy Analyze only 38.18%
of the questions were considered high-order. A similar percentage is
observed when relying on the CER framework (41.82%). With 52.94% the
Bloom's Taxonomy Create strategy... also seems to result in more high-order
questions, making it the third best strategy" [[ucar-2026|Uçar et al.
(2026)]].[^c2]

## Why it matters

The framework named in the prompt is not interchangeable scaffolding: two of
five tested groundings (Divergent Questioning, Bloom's-Evaluate) roughly
double the high-order yield of the two worst (CER, Bloom's-Analyze), even
though all five ask for a "high-order" question by design. A pipeline that
picks a single framework and trusts its label is picking a coin with a
known, uneven bias.

The frameworks are not redundant with each other: "CER and divergent
questioning strategies seem to generate complementary questions, as the
generated questions vary" in structure and content across frameworks
Uçar et al. (2026), and the paper reports this as its positive
finding — the alternative frameworks "provide viable alternatives to Bloom's
Taxonomy" rather than a strictly worse substitute for it.[^c3]

## Limits

- One domain (secondary-school physics), one set of 30 source texts, two
  LLMs, four teacher-raters (one used for inter-annotator agreement only).
  Cohen's Kappa was low for Answerability and Adoption despite high raw
  agreement (a reported "Kappa paradox"), so the [[calibration|reliability]] of the
  high-order label itself is not fully settled by this study.
- "High-order" is exactly the top three of Bloom's Taxonomy's own six
  levels; a framework's score is partly a measure of how well its prompt
  happens to target those three, not of question quality independent of
  that taxonomy.
- Percentages are per-question counts within one condition, not effect
  sizes with confidence intervals; no significance test is reported for the
  gaps between frameworks.

## Related

[[question-asking-as-program-generation]] · [[investigative-question-grpo-training]] · [[semantic-entropy]]

[^c1]: ucar-2026 — "nearly 77% of the generated questions were considered Answerable based on the accompanying text. For this subset of answerable questions, further evaluation shows that questions were distributed across all levels of Bloom’s Taxonomy, with slightly more than half (50.41%) of the questions classified as high-order questions (i.e., Analyze, Evaluate or Create)."
[^c2]: ucar-2026
[^c3]: ucar-2026 — "the alternative frameworks produce structurally and conceptually varied questions, suggesting they could complement each other and provide viable alternatives to Bloom’s Taxonomy."
