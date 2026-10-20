---
description: "Benchmark contamination is estimated by three independent probes (web n-gram overlap, surface-form rewording, masked-text reconstruction) that agree on which subjects are most affected."
aliases: ["benchmark contamination audit", "TS-Guessing probe", "indirect-reference diagnostic"]
sources: ["arxiv-2603-16197"]
---
# Benchmark contamination: a convergent multi-method audit

A high score on a public benchmark mixes knowledge with exposure to the test items. Eshwar and Karmakar (2026) audit six frontier models on MMLU with three probes that observe contamination from different sides. Their claim is that no single probe suffices and that agreement among them is the evidence.

## The three probes

**Web lexical overlap.** For 513 MMLU questions (9 per subject, 57 subjects), the first 150 characters were searched on the web and the top-5 snippets kept. A question counted as contaminated if more than 0.30 of its 8-grams appeared in the snippets and the correct answer text appeared verbatim.[^c1] Overall rate was 13.8%, highest in STEM at 18.1%, with Philosophy at 66.7%.[^c2] The authors note that the search index does not mirror pretraining corpora, so the result is a lower bound on web exposure.[^c3]

**Surface-form diagnostic.** If a model leans on familiar wording, accuracy should fall as wording departs from the training text.[^c4] GPT-4o rewrote 100 questions in two ways: a full paraphrase, and an indirect-reference form that describes key entities by a property or event instead of naming them. Average accuracy fell from 0.615 (original) to 0.564 (paraphrase) and 0.545 (indirect), a 7.0 point drop for indirect reference. Law and Ethics fell about 19.8 points, the subjects the web probe had rated highly contaminated.

**Masked-text reconstruction (TS-Guessing).** In Option Mask, one wrong option is hidden and the model, told the correct answer, must rewrite the hidden wrong option; with no exposure there is no principled way to recover its wording. In Word Mask, one long content word is blanked from the stem. A question is flagged if option-mask partial overlap is at least 0.50 or the masked word is recovered exactly.[^c5] The average combined flag rate across the six models was 72.5%, far above the random baselines.[^c6] This probe needs no web index and works on closed models.

## Convergence

The probes rank categories alike: STEM is highest in the web probe (18.1%) and in the masked-text probe (55.9%), and the subject-level accuracy drops in the paraphrase probe line up with the web-probe subject rates.[^c7] The authors treat this alignment as independent evidence for one phenomenon.

## A memorization signature that is not verbatim

DeepSeek-R1 had the highest option-mask partial rate (76.6%) with 0% exact option and 0% exact word recall, plus the lowest original accuracy (0.292) and a small indirect drop (-0.032). The authors read this as distributed memorization: stored conceptual structure without exact phrasing.[^c8] The practical consequence is that a model can look insensitive to rewording and still be contaminated, so a small surface-form drop does not clear a model. (The interpretation of R1 is the authors', based on one model and one benchmark; the explanation is unproven.)

## Limits

- The probes measure exposure or surface sensitivity, not its effect on a score. Web presence "is not proof that a model has memorized those questions."[^c9] The estimated performance gain uses a fixed 0.4 factor borrowed from prior work, not an estimate from these models (my reading of the method).
- The 72.5% flag rate is far larger than the 13.8% web rate; the gap is large, and masked-text success can also come from knowledge or from guessable options rather than memory. The paper does not test that alternative with a known-clean benchmark, so the absolute rate is unvalidated (my inference).
- Samples are small: 9 questions per subject, about 17 per subject in the rewording test, one benchmark, one rewriter (GPT-4o, itself one of the audited models). Subject-level rankings rest on tiny counts.
- Convergence in ranking is shown qualitatively, with no correlation statistic.

## Related

- [[reasoning-contamination-of-verbalized-confidence]] — a different "contamination" (interference inside one generation), not benchmark leakage
- [[adversarial-unanswerable-questions]] — questions built to defeat answering shortcuts
- [[clarification-benchmarks]] — benchmark design for asking, subject to the same leakage concern
- [[llm-judge-biases]] — another way scores can diverge from the capacity they claim to measure

[^c1]: arxiv-2603-16197 — "and (b) the correct answer text appeared verbatim in the snippets. The dual condition"
[^c2]: arxiv-2603-16197 — "The overall contamination rate was 13.8%. A further 40.7% of questions showed any lexical overlap with web content, and 25.3% had"
[^c3]: arxiv-2603-16197 — "comprehensively mirror pretraining corpora, so this method is best interpreted as a lower bound on"
[^c4]: arxiv-2603-16197 — "if performance is inflated by surface familiarity, accuracy should"
[^c5]: arxiv-2603-16197 — "A question is flagged contaminated if OM partial ≥ 0.50 or WM exact = 1."
[^c6]: arxiv-2603-16197 — "models was 72.5%—far above both random baselines—constituting strong behavioral evidence"
[^c7]: arxiv-2603-16197 — "Both methods independently rank STEM as the most contaminated category."
[^c8]: arxiv-2603-16197 — "of distributed memorization: the model has stored the conceptual and semantic structure of MMLU"
[^c9]: arxiv-2603-16197 — "not proof that a model has memorized those questions."
