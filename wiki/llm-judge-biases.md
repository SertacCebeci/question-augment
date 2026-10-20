---
description: "LLM judges of answer quality show position, verbosity and possibly self-enhancement bias; order swapping removes position effects, yet a strong judge still agrees with humans over 80%."
aliases: ["LLM-as-a-judge biases", "position bias in LLM judges", "verbosity bias"]
sources: ["lianmin-2023", "doi-10-48550-arxiv-2603-00077", "doi-10-48550-arxiv-2608-13608", "arxiv-2512-24947", "arxiv-2512-21066", "doi-10-48550-arxiv-2608-25071", "arxiv-2512-20159", "arxiv-2512-15701", "arxiv-2512-16041", "arxiv-2512-01896"]
---
# LLM judge biases

When a language model grades two answers to the same question, its verdict depends partly on features unrelated to quality. The work names three, measured on MT-bench (80 two-turn questions) and Chatbot Arena votes.

**Position bias.** The judge prefers an answer because of where it sits. In an example, GPT-4 preferred one answer, then flipped to the other when the two were swapped.[^c1] To measure it, the authors generated two similar answers per question by calling GPT-3.5 twice, and found that all judges tested showed strong position bias, most favoring the first position. Only GPT-4 gave consistent results in more than 60% of cases.[^c2] Claude-v1 also showed a name bias toward "Assistant A" under a renaming prompt.[^c3]

**Verbosity bias.** The judge favors longer answers even when they are no better. The test was a "repetitive list" attack: a numbered list is padded with a rephrasing of itself, adding no information. All judges were prone to it, though GPT-4 defended better. Judges returned a tie for identical answers but failed this attack.[^c4]

**Self-enhancement bias.** Judges may favor their own outputs. GPT-4 gave itself a win rate 10% higher than humans did, and Claude-v1 25% higher, but they also favored other models and GPT-3.5 did not favor itself. The authors state that the data cannot settle the question.[^c5]

**Mitigation by swapping.** The conservative fix is to judge twice with the order swapped and declare a win only if the answer wins both times, otherwise a tie. A cheaper, more aggressive fix is random position assignment at scale.[^c6] A few-shot judge raised GPT-4 consistency from 65.0% to 77.5%, at 4x the API cost.[^c7]

**Despite the biases, agreement is high.** On MT-bench, non-tie agreement between GPT-4 and humans reached 85%, above the 81% among humans themselves.[^c8] Agreement rose with the performance gap between the two models compared, from 70% to nearly 100%, so near-equal answers are where the judge is least reliable.[^c9]

**Mitigations do not transfer universally (rubric grading, 2026).** In a rubric-based setting, a configurable stack (option shuffling, few-shot calibration, same-model ensembles) was tested on a 480-decision benchmark. Judge family was the largest source of variation: pooled exact accuracy/kappa 60.4%/0.679 for Gemini, 51.0%/0.462 for GPT and 19.4%/-0.001 for LLaMA.[^c10] Removing shuffling changed accuracy by -0.4, -4.3 and +4.6 points across the three families, so the same mitigation helped one judge and hurt another; the authors conclude for model- and criterion-dependent choices, not a universally beneficial stack.[^c11] The same judge was lenient overall and, on a length criterion, caught brevity (0.70 recall) far better than verbosity (0.14 recall), a criterion-specific error profile.[^c12]

**Same-strength judges cannot see gains beyond themselves (2026).** A judge copied from the student, asked to pick the more accurate of baseline and harness labels on email classification, flipped verdicts with position in 50% of cases pooled and reached 48% reliability against gold. Asked to choose between its own answer and its stronger teacher's, it preferred its own 78% of the time, with 25% reliability, below chance.[^c13] The authors read this as self-preference: a judge cannot recognize answers above its own capability, so a frontier model cannot validate a frontier-model harness (see [[teacher-relative-uplift-proxy]]).[^c14]

**Verbosity in answer selection with a reference answer (2025).** A stronger LLM was used to choose between two candidate answers to an agricultural question, each scored against a reference answer on several criteria. The scoring function takes the reference as an input.[^c15] Even so, the paper's error categories include one labelled "Favors verbose responses", which it gives as about 5% of its sampled predictions.[^c16] The passages read do not say whether that share is of all 150 predictions or of the errors alone. The authors read the category as a need for length-normalized scoring. They do not test that normalization, so the verbosity effect is reported here as a failure mode, not as a measured rate.[^c17]

**Overscoring with preserved order, and the generator as judge (2026).** In a study of iterative refinement of an explanation, 14 LLM judges overscored every criterion by 1.4–2.3 points against 12 crop scientists, yet largely kept the experts' order of 11 rounds. The worst judge was the model that had generated the advice.[^c18] The authors read the shared-family result as possibly "shared artifacts rather than independent validation," which the study could not separate from the judges' own merit.[^c19] See [[ordinal-judge-fidelity]] for the ordering argument.

**Self-preference after severity correction (2026).** Three judges from three vendors ranked twenty candidate models almost identically,[^c20] while their absolute levels differed. "against a grand mean of 0.524, gemini2.5-flash graded +0.077 leniently".[^c21] Raw self-preference, a judge's preference for answers from its own family, "was large and inconsistent in sign; after severity correction it collapsed to within noise of zero for all three judges".[^c22] My reading: a self-preference figure taken from raw scores can carry a judge's general leniency, and the severity offset is what separates the two. The study covers one specialty and three judges, and it reports a correction to a raw figure, not proof that self-preference is absent.

**Defect-detection bias on code (2025).** When judges grade LLM-written code, the skew found is directional rather than positional or length-driven. The AXIOM paper reports that its metrics "exhibit a strong bias towards defect detection": they catch defective code well, but "they often misclassify non-defective programs" as defective, most of all on code-quality defects.[^c23][^c24] The F1 score hides this. The Matthews correlation coefficient exposes it, since the MCC score "offers a more complete picture" of failures on correct programs.[^c25] The authors call the judges "an overly pessimistic, harsh grader".[^c26] The paper does not test whether a prompt change removes this skew. (my reading)

**Image pairs, the same two weaknesses (2025).** A vision-language model asked which of two reconstructions of one image is closer to the original shows both the order effect and the near-tie effect. The failure figure of the VLIC paper shows a case where "VLMs can hallucinate an incorrect ranking when the images are highly similar".[^c27] Its remedy was repetition: the agreement with human judgments on BAPPS rose as seeds of the same judge were added, and the majority vote over seeds is the route taken.[^c28] A second, traditional metric was also used as a veto, and a pair was kept only when the two agreed.[^c29] See [[zero-shot-perceptual-judge]].

**Order-swap disagreement as a measured rate (2025).** The Sage suite counts local inconsistency as the share of judgments "not the logical inverse when the answer order is reversed".[^c30] On 1120 answer pairs, the paper reports that the share was 76.2% for Llama3-8B-Instruct, 25.3% for Gemini-2.5-Flash-Lite and 44.4% for Qwen-3-4B-Instruct-2507, and reads the table as confirming that the bias exists.[^c31] The same local count also takes in run-to-run noise, not only position: the measure covers "inconsistencies arising from both systematic positional bias and the inherent stochasticity of the judge model".[^c32] The rate is therefore an upper bound on position bias alone (my reading). The paper's figures are for three small models, and no mitigation is compared in that table.

**Cross-judge level offset beside raw self-preference (2025).** Two judges, DeepSeek-V3 and GPT-4o, scored the same generated event reports on a 5-point scale. DeepSeek-V3 "consistently assigns higher scores" for identical reports, averaging 4.02 against 3.62 for GPT-4o.[^c33] The authors conclude that "absolute scores from different LLM evaluators are not directly comparable."[^c34] Self-preference on raw scores was small by comparison, and the authors call it negligible: DeepSeek-V3 gained +0.03 on its own reports and GPT-4o lost 0.02.[^c35] My arithmetic is that the level gap between the two judges (about 0.4 points) is more than ten times either judge's self-preference, so for cross-judge comparison the raw level of a judge mattered more than its authorship in this study (my reading).

## Limits

- The 2026 judge test is one task, three small models, judged by copies of the student; it does not show strong judges fail.
- Rubric-grading results are single runs on small sets (one binary and one nominal criterion); they describe error profiles, not a general hierarchy.[^c12]
- Judges tested were GPT-4, GPT-3.5, Claude-v1 (2023); newer judges were not measured.
- The position test used near-identical answers, which the authors call challenging; position bias was less prominent in other cases.[^c2]
- The origin of position bias is only suspected (training data or causal attention), not studied.
- Self-enhancement is not established; no controlled study was possible because style cannot be rephrased without changing quality.
- Consistency under swapping or few-shot prompting is not accuracy; the authors note few-shot examples could introduce new biases.[^c7]
- Mitigation for weak math and reasoning grading is a separate matter (see [[judge-then-solve]]); it was not covered here.
- The report-grading self-preference figures are raw scores from one task with two judges. The "negligible" verdict is the authors' reading; no severity-corrected comparison of the same judges is reported there (my reading).

## Related

- [[mcq-answer-position-bias]] — the same order effect, in a model answering rather than judging
- [[cross-provider-judge-ensemble]] — averaging judges from different providers is another route around single-judge bias
- [[judge-then-solve]] — solving first, then judging, addresses the reasoning-grading weakness
- [[masking-vs-mitigating-bias-reduction]] — swapping hides order effects rather than removing the cause (my inference)

[^c1]: lianmin-2023 — "upon switching the positions of the two responses, GPT-4’s judgement flips"
[^c2]: lianmin-2023 — "Only GPT-4 outputs consistent results in more than 60% of cases."
[^c3]: lianmin-2023 — "Claude-v1 also shows a name bias which makes it favors"
[^c4]: lianmin-2023 — "demonstrating that all LLMs may be prone to verbosity bias"
[^c5]: lianmin-2023 — "our study cannot determine whether the models exhibit"
[^c6]: lianmin-2023 — "only declare a win when an answer is preferred in both orders"
[^c7]: lianmin-2023 — "the few-shot judge can significantly"
[^c8]: lianmin-2023 — "which is even higher than the agreement among"
[^c9]: lianmin-2023 — "from 70% to nearly 100%"
[^c10]: doi-10-48550-arxiv-2603-00077 — "Judge family is the largest source of variation"
[^c11]: doi-10-48550-arxiv-2603-00077 — "support model- and criterion-dependent configuration choices, not a universally beneficial"
[^c12]: doi-10-48550-arxiv-2603-00077 — "detects brevity (0.70 recall) far better than verbosity (0.14"
[^c13]: doi-10-48550-arxiv-2608-13608 — "the student-judge falls to 25%, below"
[^c14]: doi-10-48550-arxiv-2608-13608 — "A student judge has no ability to recognize a"
[^c15]: arxiv-2512-24947 — "is the scoring function for criterion"
[^c16]: arxiv-2512-24947 — "Favors verbose responses"
[^c17]: arxiv-2512-24947 — "Judge bias (5%) indicates need for lengthnormalized scoring."
[^c18]: arxiv-2512-21066 — "the worst judge was the model that had generated the recommendations"
[^c19]: arxiv-2512-21066 — "may partly reflect shared artifacts rather than independent validation"
[^c20]: doi-10-48550-arxiv-2608-25071 — "The three judges ranked the 20 candidates"
[^c21]: doi-10-48550-arxiv-2608-25071 — "against a grand mean of 0.524, gemini2.5-flash graded +0.077 leniently"
[^c22]: doi-10-48550-arxiv-2608-25071 — "Raw self-preference was large and inconsistent in sign; after severity correction it collapsed to within noise of zero for all three judges"
[^c23]: arxiv-2512-20159 — "LLM-as-a-judge metrics exhibit a strong bias towards defect detection"
[^c24]: arxiv-2512-20159 — "they often misclassify non-defective programs"
[^c25]: arxiv-2512-20159 — "MCC score offers a more complete picture"
[^c26]: arxiv-2512-20159 — "an overly pessimistic, harsh grader"
[^c30]: arxiv-2512-16041 — "not the logical inverse when the answer order is reversed"
[^c31]: arxiv-2512-16041 — "confirm the presence of bias"
[^c32]: arxiv-2512-16041 — "inconsistencies arising from both systematic positional bias and the inherent stochasticity of the judge model"
[^c27]: arxiv-2512-15701 — "VLMs can hallucinate an incorrect ranking when the images are highly similar"
[^c28]: arxiv-2512-15701 — "The VLM becomes more predictive of human judgment on BAPPS"
[^c29]: arxiv-2512-15701 — "Ensemble the VLM reward with LPIPS"
[^c33]: arxiv-2512-01896 — "DeepSeek-V3 consistently assigns higher scores"
[^c34]: arxiv-2512-01896 — "absolute scores from different LLM evaluators are not directly comparable"
[^c35]: arxiv-2512-01896 — "while self-evaluation biases are statistically significant, their practical impact is negligible"
