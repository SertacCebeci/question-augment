---
description: "Readers who judge a language model's answer by fluency, structure and citation density let well-formed errors pass; the error is made jointly by the answer and the reader, not by the model alone."
aliases: ["hermeneutic error", "plausibility artefact", "illusion of validity", "discursive validity", "co-constructed error"]
sources: ["arxiv-2512-16750"]
---
# Plausibility masks error

An answer can carry an error and still be read as sound, because the reader checks its form before its content. The study behind this note ran a three-round human evaluation of chatbot answers, and it describes what this does to the kind of error at stake: LLM errors shift "from predictive (factual inaccuracy, unstable reasoning) to hermeneutic forms, where linguistic fluency, structural coherence, and superficially plausible citations conceal deeper distortions of meaning."[^c1]

The concept is a joint one. The authors report that evaluators' ability to recognize errors falls "as plausibility and linguistic fluency of the answers increase".[^c2] They sum it up as "the more language resembles understanding, the harder it becomes to identify its mistakes."[^c3]

**Three mechanisms.** The authors describe a "porous zone" between model output and human reading, with three recurrent parts. First, "Fluent, well-structured responses invite trust, which makes evaluators more likely to repair and fill in the gaps".[^c4] Second, "both models and evaluators rely heavily on keyword matching or skimming methods instead of analytical checking."[^c5] Third, once a response feels useful, "explicit verification of factual details, temporal consistency, or causal links becomes less likely."[^c6] The effect on scores is stated as: "This suggests that the evaluation is strongly influenced by linguistic fluency and naturalness of response, rather than factual accuracy or argumentative consistency."[^c7]

**Density as a stand-in for validity.** Across the rounds, evaluators valued length and references "as indicators of quality, regardless of their credibility or relevance."[^c8] The authors call this a discursive validity: "the more extensive and formally structured the response, the greater the sense of completeness".[^c9] Density then hides faults: "However, the density of information masks internal inconsistencies, contradictions, and even unnoticed factual errors."[^c10] In their words, "The textual density and marked presence of references can create an illusion of validity."[^c11]

**Silence in place of non-knowledge.** When the models could not answer, they offered neighbouring material, "rather than signaling non-knowledge. Evaluators rarely reported or penalized this behavior."[^c12]

**Verification burden.** The abstract reports "a systematic verification burden and cognitive drift: as tasks became denser, evaluators increasingly relied on surface cues, allowing erroneous yet well-formed answers to pass as credible."[^c13] The discussion ties the reliance on form to a psychological literature: "Under time pressure or cognitive load, users rely on these heuristic cues rather than analytical verification."[^c14]

**Framing.** The authors name the result a hermeneutic fallibility, in which "the distinction between truth and plausibility collapses at the level of expression."[^c15] Its errors are "plausibility artefacts".[^c16]

What this adds (my inference, not the authors' test): the reader is part of the error's detection. An answer's form is visible at once; its content is visible only at the cost of checking. A reader who does not check has no other signal, so the cost of verification, more than the answer's truth, decides what passes.

## Limits

- The sample is small and local. Four chatbots were scored by three evaluators, with two analysts, all from one research team at one Portuguese university. "The evaluators (3) scored or annotated each AI response according to the instrument provided for each round".[^c19] The prompts were written by the team, not drawn from users.
- The rounds confound several things at once. "Each round deliberately changed both task structure and evaluative instrument"[^c17], and the rounds ran "over separate months"[^c18], so a rise in reliance on surface cues cannot be assigned to density alone. Model versions and evaluator fatigue moved with it.
- Browsing was not controlled for one model: "the browsing function remained permanently activated with no option to disable it."[^c20]
- The fluency link is read from scores and comments. The design does not hold content fixed while varying only fluency, so the causal reading is an inference from patterns (my inference).
- The psychology behind the mechanism (heuristics, cognitive load, transparency illusion) is cited from the literature in the discussion and is not tested here (my inference).
- "Hermeneutic" is the authors' term. In the part I read, no operational test separates a hermeneutic error from an ordinary factual one.

## Related

- [[cot-hallucination-trap]] — the machine side of the same gap: a fluent rationale stays plausible while detached from the evidence; this note is about the reader who does not catch it.
- [[answer-option-surface-cue]] — a surface cue lets a test-taker skip the content; here the reader skips the content of an answer.
- [[llm-judge-biases]] — an automated judge shows a preference for longer answers, the same preference for density the human evaluators showed.
- [[compound-citation-fabrication-defeats-single-check-verification]] — fabricated citations that pass a single check; the study's "superficially plausible citations" is that failure seen by a human reader.

[^c1]: arxiv-2512-16750 — "from predictive (factual inaccuracy, unstable reasoning) to hermeneutic forms, where linguistic fluency, structural coherence, and superficially plausible citations conceal deeper distortions of meaning"
[^c2]: arxiv-2512-16750 — "as plausibility and linguistic fluency of the answers increase"
[^c3]: arxiv-2512-16750 — "the more language resembles understanding, the harder it becomes to identify its mistakes"
[^c4]: arxiv-2512-16750 — "Fluent, well-structured responses invite trust, which makes evaluators more likely to repair and fill in the gaps"
[^c5]: arxiv-2512-16750 — "both models and evaluators rely heavily on keyword matching or skimming methods instead of analytical checking"
[^c6]: arxiv-2512-16750 — "explicit verification of factual details, temporal consistency, or causal links becomes less likely"
[^c7]: arxiv-2512-16750 — "This suggests that the evaluation is strongly influenced by linguistic fluency and naturalness of response, rather than factual accuracy or argumentative consistency"
[^c8]: arxiv-2512-16750 — "the number of references as indicators of quality, regardless of their credibility or relevance"
[^c9]: arxiv-2512-16750 — "the more extensive and formally structured the response, the greater the sense of completeness"
[^c10]: arxiv-2512-16750 — "However, the density of information masks internal inconsistencies, contradictions, and even unnoticed factual errors"
[^c11]: arxiv-2512-16750 — "The textual density and marked presence of references can create an illusion of validity"
[^c12]: arxiv-2512-16750 — "rather than signaling non-knowledge. Evaluators rarely reported or penalized this behavior"
[^c13]: arxiv-2512-16750 — "as tasks became denser, evaluators increasingly relied on surface cues, allowing erroneous yet well-formed answers to pass as credible"
[^c14]: arxiv-2512-16750 — "Under time pressure or cognitive load, users rely on these heuristic cues rather than analytical verification"
[^c15]: arxiv-2512-16750 — "the distinction between truth and plausibility collapses at the level of expression"
[^c16]: arxiv-2512-16750 — "The resulting hallucinations are not random failures, but plausibility artefacts"
[^c17]: arxiv-2512-16750 — "Each round deliberately changed both task structure and evaluative instrument"
[^c18]: arxiv-2512-16750 — "Conducting the rounds over separate months also allowed us to observe potential model and evaluation drift"
[^c19]: arxiv-2512-16750 — "The evaluators (3) scored or annotated each AI response according to the instrument provided for each round"
[^c20]: arxiv-2512-16750 — "the browsing function remained permanently activated with no option to disable it"
