---
description: "Demonstrations chosen because the model answered them wrongly at baseline, with their known outcomes shown in the prompt, lifted ICU mortality AUROC from 0.806 to 0.873 on MIMIC-IV."
aliases: ["misprediction-retrieved cases", "error-corrective exemplars", "case-based prompting", "failure-case retrieval for prompts"]
sources: ["arxiv-2512-19735"]
---
# Error-selected exemplars

A prompt can carry worked examples, and the usual rule for picking them is similarity to the item being answered ([[similarity-selected-exemplars]]). A different rule picks examples by the model's own track record. Run the model without examples over a labelled pool, keep the items it got wrong, and retrieve from that failure pool the cases closest to the new item, together with their known outcomes. The model then sees a concrete instance where its answer diverged from the truth. The authors state the purpose this way: "By providing concrete examples of prior prediction errors and known outcomes, CAP aims to guide the model toward more clinically grounded reasoning."[^e1]

The mechanism is therefore a repository built from failures, not from correct answers. In the ICU study the repository was 400 training cases, and every one of them[^e9] was a case the baseline prompt had misclassified: "all cases in the repository were both misclassified by the baseline prompting strategy and sensitive to at least one demographic perturbation."[^e2] At inference, the nearest case is retrieved by clinical similarity and inserted with its features and its outcome, alongside the target patient's summary. The method is training-free; the model's parameters are untouched.[^e8]

What it did, on MIMIC-IV with an LLM predicting in-hospital mortality from first-24-hour variables: the baseline prompt reached AUROC 0.806 and AUPRC 0.497, and the full method reached AUROC 0.873 and AUPRC 0.694.[^e3] The retrieval-strategy ablation splits the gain. Retrieving from the same failure repository by clinical similarity alone gave AUROC 0.846,[^e8] so most of the improvement came from showing failed cases with outcomes. The further step to 0.873 came from adding the historical error type and a demographic-sensitivity annotation to the retrieved case.[^e4] Retrieving by demographic match alone scored below the baseline, at AUROC 0.765, and the authors conclude "the benefit of CAP cannot be attributed to demographic matching alone."[^e5]

The transferable point is about what the demonstration is for. A similar case with a correct answer tells the model what the answer looks like. A similar case the model got wrong, with its outcome, tells the model where its own reasoning went astray on this kind of input. The two are different selection criteria and the work treats them as such.

## Limits

- One dataset (MIMIC-IV), one LLM, and a retrospective setting. The authors say "Further validation across additional LLMs, external datasets, and prospective clinical scenarios is required before deployment."[^e6]
- The error filter was never isolated. Every retrieval arm, including the clinical-only one, drew from the failure repository, and no arm drew from a pool of correctly answered training cases. So the work does not show that selecting by error beats selecting by similarity from a general pool. That contrast is my inference from the design, not a tested result.
- No random-from-failure-pool arm exists either, so the similarity effect inside the failure pool is not isolated (my inference).
- The full method also used a demographic-sensitivity screen run by GPT-4 and a demographic-first candidate filter. The authors report the demographic-aware variant as mixed: it lowered the mean FNR gap from 0.069 to 0.061 but also lowered AUROC from 0.846 to 0.839.[^e7] The fairness effects are modest in size (my reading), and age-related disparities "remained non-negligible."[^e10]
- Whether the gain depends on the baseline's error rate, on repository size, or on the number of retrieved cases was not swept. Only one retrieved case per query was used.
- It is not shown that the retrieved outcomes help an answerer that already knows the domain; the study measures a single classifier-like output, not a dialogue.

## Related

- [[similarity-selected-exemplars]] — the usual rule for choosing demonstrations, which this note contrasts with a rule that selects by the model's own failures
- [[stage-level-hallucination-loss-masking]] — the model's own wrong answers used as training examples, with the false stages masked from the loss; a training-time analogue of learning from failures
- [[rag-bias-reduction-versus-cot-bias-increase]] — another case where a prompting change moves accuracy and fairness in different directions
- [[narrative-over-demographic-persona-conditioning]] — how demographic information in a prompt alters an LLM's agreement with a person's answers

[^e1]: arxiv-2512-19735 — "By providing concrete examples of prior prediction errors and known outcomes, CAP aims to guide the model toward more clinically grounded reasoning"
[^e2]: arxiv-2512-19735 — "all cases in the repository were both misclassified by the baseline prompting strategy"
[^e3]: arxiv-2512-19735 — "On MIMIC-IV, CAP improved AUROC from 0.806 to 0.873 and AUPRC from 0.497 to 0.694"
[^e8]: arxiv-2512-19735 — "Compared with the Baseline Prompt, Clinical-only Retrieval improved AUROC from 0.806"
[^e9]: arxiv-2512-19735 — "we selected 400 representative cases to construct the final"
[^e10]: arxiv-2512-19735 — "although age-related disparities remained non-negligible"
[^e4]: arxiv-2512-19735 — "Full CAP additionally included historical error type and demographic-sensitivity annotation."
[^e5]: arxiv-2512-19735 — "findings indicate that the benefit of CAP cannot be attributed to demographic matching alone."
[^e6]: arxiv-2512-19735 — "Further validation across additional LLMs, external datasets, and prospective clinical scenarios is required before deployment."
[^e7]: arxiv-2512-19735 — "reduced the mean FNR gap from 0.069 to 0.061 and the aggregated race gap from"
