---
description: "Translate to logic only the sentence spans that pass a structural and a semantic check, keep the rest as text, and revert any translation the check rejects."
aliases: ["confidence-aware symbolic translation", "partial symbolic translation", "hybrid premise set", "selective formalization", "hybrid natural-language and logic context"]
sources: ["arxiv-2512-03360"]
---
# Selective symbolic translation

Before a logical reasoner can work on a text, each sentence has to be written as a formula, and that translation can be wrong. The HBLR framework treats translation as a per-sentence decision rather than a single step applied to the whole input. A sentence first passes a rule-based structural filter that looks for logic-compatible patterns, which the authors list as "explicit predicate-argument constructions, the presence of logical connectives or quantifiers such as" the words "if," "then," "and," and "or."[^s1] A sentence that passes is translated into a formula, and an LLM-based semantic verifier then compares the formula with the sentence. The verifier accepts the formula "only when it can be confidently verified as fully consistent with s"; otherwise the sentence stays in natural language.[^s2] The stated reason for the asymmetry is that "an incorrect logical form is more harmful than retaining the original natural language."[^s3]

The output is a hybrid context rather than a set of formulas. The premises are a mixture of formulas and sentences, and the conclusion can be either, "expressed in logical or textual form depending on translation confidence."[^s4] A translation that is accepted but later found lossy is handled by a separate reflection step that "reverts lossy ones back to text when necessary."[^s5] The reasoner then works over the mixed set. The gate is therefore a filter on what counts as a formal premise, not a repair step: a rejected sentence is passed through as text, not re-translated.

What the gate buys is measured against two extremes, on GPT-4 and the paper's five benchmarks. Against keeping everything in natural language (All-NL), "the selective strategy yields a 7.2% improvement," and against translating everything into first-order logic (All-FOL) it is 4.7% higher on average, with the authors reading the second gap as the cost of "full formalization can introduce translation errors."[^s6][^s7] The retained share is not fixed. On average "only 15.74% of the input remains in natural language," with the lowest share on LogicalDeduction and a higher share on AR-LSAT and FOLIO, which the authors read as following translation confidence.[^s8] The motivation comes from the paper's own measurement of a translator (SymbCoT). LLMs "achieve high translation accuracy on synthetic datasets like ProntoQA and ProofWriter," but "performance drops sharply" on the curated sets FOLIO and AR-LSAT.[^s9][^s10]

## Limits

- **The gate is judged by an LLM.** The semantic verifier is the same kind of model as the translator, prompted with few-shot exemplars. The authors describe it as "a conservative safeguard" rather than a perfect judge. Its false-accept rate is not reported in the parts I read, so a formula that is still wrong after the check is not ruled out.
- **The structural filter is a list of patterns.** The logic-compatible patterns are predefined. Their precision and recall are not measured in the text I read.
- **Three strategies were compared, not each gate.** The comparison is selective translation against All-NL and All-FOL. I did not find a run that removes only the verifier or only the structural filter, so the contribution of each gate is not separated.
- **Not uniform across domains.** On LogicalDeduction with GPT-3.5-Turbo, "An exception occurs on the LogicalDeduction task with GPT-3.5-Turbo, where Logic-LM slightly outperforms HBLR."[^s11] The authors attribute this to the model's inference, since "it struggles with complex inference," not to the translation.[^s12]
- **The translation itself is not scored here.** Table 1's translation accuracies are for the SymbCoT translator, read through solver outputs. The selective method's own formulas are not checked against gold formalizations in the parts I read. Retention is a share of text, not a measure of whether the formulas that were kept are correct; a low retention on LogicalDeduction says most sentences passed the gate, not that those formulas are right.
- **The answer metric is multiple choice.** Accuracy on answer choices can hide a wrong premise that still leads to the right option. This is my reading; the paper does not discuss it.

## Related

- [[formalizability-routing]] — sorts claims by whether a solver can take their meaning and sends the rest to soft checking. It is the same per-item gate between formal and soft handling, applied to verification instead of to the reasoning input; the identification is my inference, not the paper's.
- [[backward-chaining-subgoal-decomposition]] — the reasoning side of the same framework: the hypothesis is assumed and its premises traced back over the hybrid set.
- [[neurosymbolic-text-to-logic-retrieval]] — text-to-logic translation used once for retrieval, with the same fragility on open language.

[^s1]: arxiv-2512-03360 — "which include explicit predicate-argument constructions, the presence of logical connectives or quantifiers such as"
[^s2]: arxiv-2512-03360 — "is accepted only when it can be confidently verified as fully consistent with s"
[^s3]: arxiv-2512-03360 — "an incorrect logical form is more harmful than retaining the original natural language"
[^s4]: arxiv-2512-03360 — "expressed in logical or textual form depending on translation confidence"
[^s5]: arxiv-2512-03360 — "reverting lossy ones back to text when necessary"
[^s6]: arxiv-2512-03360 — "the selective strategy yields a 7.2% improvement over All-NL"
[^s7]: arxiv-2512-03360 — "full formalization can introduce translation errors"
[^s8]: arxiv-2512-03360 — "only 15.74% of the input remains in natural language"
[^s9]: arxiv-2512-03360 — "LLMs achieve high translation accuracy on synthetic datasets like ProntoQA and ProofWriter"
[^s10]: arxiv-2512-03360 — "performance drops sharply"
[^s11]: arxiv-2512-03360 — "An exception occurs on the LogicalDeduction task with GPT-3.5-Turbo, where Logic-LM slightly outperforms HBLR"
[^s12]: arxiv-2512-03360 — "it struggles with complex inference"
