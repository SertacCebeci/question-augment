---
description: "Added evidence can cut a citation generator's hallucination rate by cutting its abstentions too, and adversarial metadata turns abstention into confident error."
aliases: ["abstention collapse under retrieval", "retrieval-induced abstention loss", "evidence-driven abstention shift"]
sources: ["doi-10-48550-arxiv-2405-02228"]
---
# Evidence-shifted abstention

A citation generator has two outputs: an attribution, or a refusal. The two rates that count them move with the evidence the generator is given, and they do not always move in the same way. Tilwani et al. evaluate proprietary and open-source LLMs on a benchmark of 12,723 sentence-level citation instances, "we evaluate proprietary and open-source LLMs under zero-context" and four further evidence conditions: metadata-augmented, cascaded metadata-augmented (CMP), retrieval-augmented, and adversarial.[^c1] The abstention rate (AR) is the share of queries answered with a refusal, and the hallucination rate (HR) is the share of non-refusals that are wrong; both are read on one run, so each condition yields a pair (see [[abstention]] for the same pair as selective risk).

The clearest case is retrieval. Going from naive to advanced retrieval-augmented generation lowers HR from 87.6% to 65.4%, but the same change "reduces AR from 5.0% to 0%".[^c2] The abstention share moved only five points, so most of the HR gain is not a refusal effect. What the pair does show is that the lowest-HR retrieval setting answers every query, and its HR is then scored only over the answers it gave. Retrieval-augmented variants generally behave this way, since they "frequently maintain near-zero abstention" under the adversarial setting as well.[^c3] The authors suggest a mechanism without testing it: "systems more confident without making them more correct" is how they describe retrieval that supplies topically relevant text which does not support the claim.[^c4]

Adding metadata moves the operating point in the other direction when the metadata is wrong. Under adversarial metadata "several systems" "exceed 85% HR",[^c5] so for those systems most answers given under misleading metadata are wrong. The CMP protocol stages this on purpose: the model first attempts a title with no context, and only if it abstains or errs is metadata supplied and the query repeated. The stated question is whether "additional context shifts systems from cautious abstention to confident error".[^c6] The authors describe CMP as "a diagnostic tool", not a calibration method,[^c7] and their main finding from it is that "models with poor uncertainty calibration cannot be rescued by better" prompting.[^c8]

So the effect of evidence is not one number. More evidence can lower HR while AR falls toward zero, which reads as improvement if HR is taken alone. Misleading evidence raises HR and, in the retrieval-augmented variants, leaves AR near zero. Read together, the two rates show whether a system is answering more because it is supported or because it has stopped refusing; the pair cannot be read from HR alone (my reading, from the paper's joint-interpretation rule).

## Limits

- The AR is not checked per query. The authors state that "AR reflects epistemic caution, not correctness"[^c9] and validate it only through "aggregate trends".[^c10] Whether a given refusal was the right one is not measured, so the effect of evidence on AR is a population trend.
- HR is strict. A non-abstaining answer counts as wrong unless it matches the ground truth after normalization, and "We treat partial matches as incorrect".[^c11] A near-miss title and a fabricated one weigh the same in HR. BLEU and F1 are reported beside it, but they do not enter the headline numbers.
- Comparing HR across conditions compares operating points, not only error rates. Here the coverages differ little (AR of 5.0% against 0%), but the paper does not compute a risk-coverage curve for any condition, so a gain at one coverage cannot be read as a gain at another (my reading).
- A system that always abstains has AR of 100% and HR of zero, "with zero hallucinations but provides no utility".[^c12] So low HR alone does not show a generator is better; the AR side has to carry the weight.
- The mechanism that retrieval makes systems more confident is the authors' suggestion. The benchmark shows the co-movement; it does not isolate whether the cause is the retrieved text, its relevance, or the prompt format.
- One benchmark over 12 arXiv subject categories, with human validation on 1,000 outputs. The shift is measured on citation attribution; whether it holds for factoid QA or for open-ended generation is not tested here.

## Related

- [[abstention]] — the selective-risk pair; AR and HR here are its coverage and selective risk under a 0-1 loss
- [[evidence-sensitivity-of-confidence]] — the converse question: whether a confidence gate's score holds when the evidence behind an answer shrinks
- [[unnecessary-abstention-aware-recall]] — counts refusals on answerable questions, which an AR that pools all refusals does not separate
- [[slo-reward-profile]] — another setting that moves a system toward refusal, here through the reward weights rather than the evidence
- [[abstention-option-uncertainty-inflation]] — an explicit abstain option changing the answer distribution, a related effect of the output format

[^c1]: doi-10-48550-arxiv-2405-02228 — "we evaluate proprietary and open-source LLMs under zero-context"
[^c2]: doi-10-48550-arxiv-2405-02228 — "reduces AR from 5.0% to 0%"
[^c3]: doi-10-48550-arxiv-2405-02228 — "frequently maintain near-zero abstention"
[^c4]: doi-10-48550-arxiv-2405-02228 — "systems more confident without making them more correct"
[^c5]: doi-10-48550-arxiv-2405-02228 — "systems exceed 85% HR"
[^c6]: doi-10-48550-arxiv-2405-02228 — "cautious abstention to confident error"
[^c7]: doi-10-48550-arxiv-2405-02228 — "as a training or calibration method but as a diagnostic tool"
[^c8]: doi-10-48550-arxiv-2405-02228 — "cannot be rescued by better"
[^c9]: doi-10-48550-arxiv-2405-02228 — "AR reflects epistemic caution, not correctness"
[^c10]: doi-10-48550-arxiv-2405-02228 — "We validate AR through aggregate"
[^c11]: doi-10-48550-arxiv-2405-02228 — "We treat partial matches as incorrect"
[^c12]: doi-10-48550-arxiv-2405-02228 — "with zero hallucinations but provides no utility"
