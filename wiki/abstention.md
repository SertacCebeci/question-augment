---
description: "\"I don't know\" is a third output, not a weak answer: the answerer is a El-Yaniv & Wiener (2010) define a **selective model** as a pair $(f,"
aliases: ["reject option", "classification with a reject option", "selective classification", "selective prediction", "CAR (commit rate / conditional accuracy axis)", "confidence-threshold abstention", "confidence gate", "selection-conditioned error rate"]
sources: ["chow-1970", "el-yaniv-2010", "franc-2023", "geifman-2017", "herbei-2006", "kadavath-2022", "arxiv-2601-00138", "arxiv-2512-23924", "arxiv-2601-00841", "arxiv-2512-16795", "doi-10-48550-arxiv-2408-14141", "arxiv-2512-11614", "arxiv-2512-06380", "arxiv-2512-04597", "doi-10-48550-arxiv-2607-14399", "arxiv-2512-01556", "arxiv-2511-21025", "arxiv-2511-19806", "doi-10-48550-arxiv-2405-02228"]
---
# Abstention — the reject option

> "I don't know" is a third output, not a weak answer: the answerer is a
> *pair* — what to say, and whether to say it — and the second half has its
> own price, its own curve and its own learning problem.

## Definition / Mechanism

El-Yaniv & Wiener (2010) define a **selective model** as a pair $(f, g)$: a
prediction function $f$ and a selection function $g: \mathcal{X} \to \{0,1\}$
that outputs $f(x)$ when $g(x)=1$ and abstains when $g(x)=0$. Two quantities
follow: **coverage** $\phi(g) = \mathbb{E}[g(x)]$, the mass of the
non-rejected region, and **selective risk**
$R(f,g) = \mathbb{E}[\ell(f(x),y)\,g(x)] / \phi(g)$ — the loss *conditioned on
having answered*. Sweeping $g$ traces the **risk–coverage curve**.[^c1] The same ratio, under the name selection-conditioned error rate, is the target of a method that turns it into a linear expectation constraint and calibrates it on held-out data.[^c48] See linearized-selection-risk-constraint.

Chow (1970) gave the classical solution for a known posterior: reject when the
maximum posterior falls below a threshold set by an explicitly named cost of
rejection, and showed the error rate can be recovered from the reject
function.[^c2]

Herbei & Wegkamp (2006) study the binary case, where the classifier
reports "I don't know" when the conditional class probabilities are too close
to separate.[^c3]

Franc, Průša & Voráček (2023) prove the structural fact that matters here.
Three formulations —

- **cost-based**: name the price of rejecting;
- **bounded-improvement**: name a selective risk to guarantee, maximise coverage;
- **bounded-coverage**: name a coverage to meet, minimise selective risk —

lead to the **same** prediction strategy, a Bayes classifier with a randomised
Bayes selection function.[^c4]

So the answerer cannot escape naming a number; it can
only choose *which* number is easier to state.[^c5]

They further define a *proper
uncertainty score* as the scalar summary sufficient to build that selection
function, and learn it for a black-box predictor: the score is a separate
estimation problem, not a by-product of the predictor.[^c6]

Geifman & El-Yaniv (2017) make the threshold certifiable: their SGR algorithm
binary-searches a confidence threshold on held-out data and returns a selective
classifier with a risk bound.[^c7]

Their abstract reports 2% top-5 ImageNet error
guaranteed with probability 99.9% at almost 60% coverage.[^c8]

A system-level version of the same pair is a gate on self-reported confidence with a designer-set threshold. On NExT-QA with Gemini 2.0 Flash, sweeping that threshold gave a smooth, monotone curve: "Sweeping threshold ε produces smooth risk-coverage tradeoffs, reducing error rates" from 23.6% to 9.4% at 63.7% coverage.[^c18] The gate is the designer's knob and does not use the model's own abstain flag.[^c19] Whether the same knob keeps its meaning when the evidence weakens is a separate question, taken up in [[evidence-sensitivity-of-confidence]].

## Known as

| Field | Name there | Relation |
|---|---|---|
| Pattern recognition (Chow) | reject option, error–reject tradeoff | exact |
| Statistics | classification with a reject option | exact |
| Machine learning theory | selective classification | exact |
| Applied ML / NLP | selective prediction | exact — same $(f,g)$ pair measured by the same two numbers, coverage and selective risk; the only difference is the scope of application (open-ended outputs rather than a fixed label set) |

[^c9.1][^c9.2][^c9.3][^c9.4][^c9]

Not this concept: **Chow's rule** is one optimal strategy *inside* the
framework, not another name for it; the **risk–coverage curve** is the object
the framework produces, not the framework; **refusal** in LLM safety is
declining on policy grounds and is measured as a rate over harmful prompts, not
as selective risk at a coverage; **P(IK)** (Kadavath et al. 2022) is a candidate
uncertainty score, not a selection function.[^c10]

## Why it matters

On stall 10 this supplies what [[calibration]] does not: a *decision*. It
separates the answer from the choice to give it, and it says that choice is
undecidable until the asker's cost of an empty answer is written down as a
number, a risk level or a coverage level.[^c11]

It also imports [[roc-curve]]'s
argument to the answerer's side — an answerer that abstains often and one that
abstains rarely differ in operating point, so comparing them at a single point
is malformed.[^c12]

## Transfer

| | |
|---|---|
| In its home field | a classifier over a fixed label set, i.i.d. test points, a fixed loss $\ell$, ground truth available on a validation sample |
| Here | an answerer over an open-ended answer space, one question at a time, usually no labelled held-out set |
| What survives | the $(f,g)$ decomposition; the requirement that abstention carry a named price (or a named risk/coverage guarantee); risk–coverage as the comparison object instead of a single accuracy; the uncertainty score as a separate estimation problem |
| What does not | SGR's guarantee (needs an i.i.d. labelled sample and a fixed loss); Chow's optimality (holds for the true posterior); the three-model equivalence (proved in the Bayes-optimal setting, not for a black-box answerer with an arbitrary score) |

[^c13.1][^c13.2][^c13.3][^c13.4][^c13]

## Abstention in active learning

Abstention also changes what a learner that queries labels can promise. In a dissertation on interactive learning, Chow's error charges (1/2 − γ) for each abstention, with γ a small constant, so the price of abstaining is kept marginally below a coin flip.[^c21] Under that error the dissertation states an algorithm whose classifier has Chow's excess error at most ε with polylogarithmic label complexity, "without any low noise assumptions".[^c22] It calls a classifier with proper abstention one that abstains only when abstaining is optimal.[^c23] Under Massart or Tsybakov noise, the classifier so obtained is said to achieve the minimax optimal label complexity under standard excess error.[^c25] The motivation is the high-noise regime, where a classical lower bound says active learning gives no improvement over passive learning.[^c24] The noise conditions are in [[massart-tsybakov-noise]]; the trap that abstention avoids is in [[noise-seeking-uncertainty-sampling]].

## Refusal under a cost-heavy reward

Abstention can also become the default output of a learned policy when the reward prices it wrongly, with no abstention-specific training signal at all. In an offline study of per-query retrieval control, a learned policy "can exhibit refusal collapse under a cheap SLO when refusal is heavily rewarded."[^c26] The mechanism the author gives is that "In offline routing, cost-heavy rewards can make" refusal look attractive, especially when wrong answers are penalized and the reward is measured "per-query without explicit constraints on abstention."[^c27][^c28] Under the cheap profile the learned policy refused on 94.5% of questions, with near-zero accuracy.[^c29] My reading: this is the same failure the selective-prediction literature names when the risk is not paired with a calibrated abstention constraint, and it is a different cause from the unanswerable-share collapse in [[abstention-base-rate-sensitivity-in-rl]]. The study does not test that.

## Refusal triggered by evidence

A retrieval-augmented answerer can be given a refusal rule that is not a threshold at all. In the conflict-aware RAG pipeline of arxiv-2512-16795, the instruction is to "generate a justified refusal when all retrieved evidence is labeled irrelevant or when the available information is incomplete or unverifiable; and"[^c30] The trigger is the evidence labels, set per snippet before the answer is written. It is not a confidence gate, so none of the coverage or selective-risk quantities above is computed for it. The paper scores refusal as F1 on answerable versus unanswerable queries, a different measure from selective risk at a coverage, and it does not compare the two. See [[evidence-conflict-type]] for the labels that feed the rule.

## Abstention scored against a crowd

A gate need not score the model's own confidence. CROWD-CALIBRATOR abstains when the distance between the model's output distribution and an estimated crowd distribution for the same item passes a threshold, and the rule is stated as "far off from the human probability distribution, the model will abstain."[^c31] Its claim is that this is "competitive with these baselines for hate speech detection and outperforms them for NLI."[^c32] The score is a distributional comparison rather than a confidence, and it needs dense annotation to be learned; see [[crowd-distance-abstention]].

## Abstention taught by misleading evidence

A reject target can come from how the context was built, with no unanswerable question in the data. In the Merlin-Arthur training for RAG, an adversarial prover masks the decisive evidence, and the generator is trained to reject on that masked context.[^c33] The paper reports that "Abstention emerges even without any manually annotated unanswerable example or preference pair." Under insufficient context, M/A training reduced incorrect answers "by up to 35 pp during training and by 18-20 pp" over vanilla finetuning.[^c34]

The same lever runs the other way in [[hard-positive-evidence-augmentation]], which counters over-abstention by training on sufficient evidence polluted with noise. Here the adversarial examples push toward rejection, and the protocol's soundness test counts a correct-class answer under misleading context as a failure (my reading; see [[merlin-arthur-protocol]]).

The paper also names the cost of this rule. The system is "conservative, refusing to answer helpful queries because it cannot find a direct citation."[^c35] The gains are measured against an instructed LLM and vanilla finetuning, on five QA sets and models from 1B to 32B parameters. The adversarial construction assumes the answer is not recoverable from memory, and the authors note that "Because LLMs frequently and effectively memorize benchmarks" they chose a stricter soundness measure rather than resolving that.[^c36] Whether a rejection is correct where the answer is memorized is not tested in the text read (my inference).

## Refusal as a forced-choice option

In a multiple-choice audio benchmark, "I don't know" is one option among five, and the refusal rate is whatever that option absorbs. Removing it turns the task into a four-way choice; open-source audio models without training "struggle to refuse to answer and have a clear" rise in every accuracy, so the option was doing the refusing.[^c37] After training on bystander-refusal data, the same models were tested with the choices removed altogether. Their refusal on bystander questions was 92% and 96%, against 45% and 48% before training.[^c38] My reading: the open-ended test shows a learned refusal, while the option test only shows that a listed exit is taken. The two numbers come from different item formats, so the gain is a within-model comparison, not a single accuracy. See [[selective-hearing]] for the benchmark.

## Abstention recall in embodied question answering

The reject option has an embodied form, measured on AbstainEQA, a benchmark that adds abstention cases to OpenEQA. Its headline number is a recall, not a selective risk: "even the best frontier model only attains 42.79% abstention recall, while humans achieve 91.17%".[^c39] The authors report that "scaling, prompting, and reasoning only yield marginal gains"[^c40] and that "fine-tuned models overfit to textual cues".[^c41] The judge that decides whether an output is a valid abstention is GPT-4o, and it is checked against people on a 300-item sample.[^c42][^c43]

The embodied cases that models miss most are the instruction-side ones, where the reading of the words, not the perception, has to decide. The split is in missing-evidence-source. My reading: this is the same weakness the forced-choice and refusal-collapse results above show from other angles, now measured where the missing evidence is in the scene. It is one benchmark and one recall figure, not a rate observed in deployed use.

## The verdict set as the exit

A reject option exists only if the answer set contains one. In a text-world eval, the first verdict grammar had two verdicts. Adding a third, incomplete, on four byte-identical anchors moved strong claims from 38/40 to 7/40, while the new verdict took 28/40 outcomes.[^c45] The author calls the added verdict the code for calibrated refusal that the earlier grammar could not express.[^c46] My reading: when the exit is absent, uncertainty is filed under the nearest committed claim. This is the forced-choice effect above, now measured in a multi-turn game. The paper bounds its own result: "Whether incomplete uptake is calibrated or merely the no-lose option is not settled here."[^c47] A comparable case, where the answer changed with what the answerer was told, is in [[success-criterion-disclosure]].

## Abstention scored above zero

Scoring can give the reject option its own value rather than zero. In CaptionQA a correct selection scores 1 and an incorrect one 0, while the option "Cannot answer from the caption" scores "1/nchoices + 0.05": the chance rate over the semantic options, plus a small margin.[^c49] A guess is then worth about what abstaining is worth, and a withheld answer is never scored as a wrong one. The paper's reason is that a caption which withholds is preferable to one that misleads: "less, but avoids misleading content, is preferable to one that".[^c50] This fixes the price of the exit at a number, the named price the framework above requires. The 0.05 is the authors' choice, and the parts read give no sensitivity check on it (my reading).

## Two rates as one trade-off

A benchmark of citation attribution writes the same pair without the word "selective". Its Abstention Rate is the share of queries answered with a refusal, and its Hallucination Rate is an error "frequency conditional on responding".[^c51] With the answered set as the denominator, HR is the answerer's selective risk under a 0-1 loss, and AR is one minus its coverage (my reading, from the two definitions). The authors read the pair jointly, since "AR and HR must be interpreted together" to characterize epistemic safety.[^c52] One difference from the selective setting is that AR has no instance-level ground truth: "AR reflects epistemic caution, not correctness".[^c53] The coverage axis is measured, but whether each refusal was the right one is not. The same pair under changing evidence is in [[evidence-shifted-abstention]].

## Limits

- Every model here treats the cost of abstaining as **exogenous**. The claim
  above — that "I don't know" is decidable only once that cost is named — is
  the framework's precondition restated, not a way to compute the cost; nothing
  in this literature says what an empty answer costs an asker.[^c14]
- Selective risk conditions on the accepted region and needs $\ell(f(x),y)$,
  i.e. ground truth per instance. For a one-off design question there is none,
  so the risk–coverage curve is not computable and only the decomposition
  transfers.[^c15]
- The uncertainty score is the load-bearing part and it does not travel:
  Kadavath et al. (2022) found language models predict P(IK) well and partially
  generalise across tasks, but calibrate poorly on new ones — so a threshold
  fitted in one domain is not a threshold in another.[^c16]
- Herbei & Wegkamp is binary classification; the "too close to separate"
  formulation does not carry to multi-class or open-ended answers unchanged.[^c17]
- A threshold tuned on one evidence regime is not a threshold for another. The
  VideoQA study reports that a deployed system "cannot rely on confidence
  thresholds tuned in-distribution."[^c20] The guarantee here is for the
  distribution the threshold was fitted on.
- The refusal collapse above comes from one study with N = 200 per condition and point estimates. Whether it survives another generator, or a reward that carries an explicit abstention constraint, is not tested in that work. My inference.
- The embodied recall figures come from a benchmark whose ambiguous queries were written by annotators and then "paraphrased into five semantically equivalent variants using a large language model".[^c44] The recall is scored by a GPT-4o judge, so the numbers inherit that judge's agreement with people (0.88 on the sampled items), not a human-only scoring.

## Related

[[calibration]] · [[roc-curve]] · [[verbal-probability-expressions]] · [[semantic-entropy]] · [[stopping-rules]] · Commitment · [[evidence-sensitivity-of-confidence]] — whether a gate's score contracts when the evidence behind an answer shrinks · [[massart-tsybakov-noise]] — the noise shapes under which abstention-free active learning saves labels · [[noise-seeking-uncertainty-sampling]] — uncertainty-based querying can waste labels where abstaining would cost little · [[slo-reward-profile]] — the reward weights that price refusal in a learned per-query RAG router · [[merlin-arthur-protocol]] — abstention as the verifier's soundness output, trained on adversarial context · [[explained-information-fraction]] — conditioning on the answered region, as selective risk does · missing-evidence-source — where the missing evidence sits (world, instruction, presupposition), which bears on which abstention cases an embodied answerer can detect · [[success-criterion-disclosure]] — a hidden success criterion manufactures false completions in a text-world eval; naming it removes them, with a halting confound · [[data-existence-gate]] — the same reject option placed before analysis, decided by whether the store holds the data at all, not by a confidence threshold · [[latent-representation-abstention-probe]] — a learned score for abstaining on a VLM's own OCR answers, read from its hidden states after it has answered

[^c1]: el-yaniv-2010 — "In selective classification the learner should output a binary selective classifier defined to be a pair ( f , g), with f being a standard binary classifier, and g : X → [0, 1] a selection function whose meaning is as follows."
[^c2]: el-yaniv-2010 — "authored by Chow (1957, 1970), focusing on Bayesian solutions for the case where the underlying distributions are fully known."
[^c3]: chow-1970
[^c4]: franc-2023 — "We prove that despite their different formulations the three rejection models lead to the same prediction strategy: the Bayes classifier endowed with a randomized Bayes selection function."
[^c5]: chow-1970
[^c6]: franc-2023 — "We define the notion of a proper uncertainty score as a scalar summary of the prediction uncertainty sufficient to construct the randomized Bayes selection function. We propose two algorithms to learn the proper uncertainty score from examples for an arbitrary black-box classifier."
[^c7]: geifman-2017 — "The algorithm performs a binary search to find the optimal bound guaranteeing the required risk with sufficient confidence. The SGR algorithm outputs a selective classifier (f, g) and a risk bound b∗ ."
[^c8]: geifman-2017 — "using our method an unprecedented 2% error in top-5 ImageNet classification can be guaranteed with probability 99.9%, and almost 60% test coverage."
[^c9.1]: chow-1970
[^c9.2]: chow-1970
[^c9.3]: el-yaniv-2010 — "Throughout the paper we use the term selective classification to refer to ‘classification with a reject option.’"
[^c9.4]: geifman-2017
[^c10]: kadavath-2022 — "Next, we investigate whether models can be trained to predict "P(IK)", the probability that "I know" the answer to a question, without reference to any particular proposed answer."
[^c11]: chow-1970
[^c12]: chow-1970
[^c13.1]: el-yaniv-2010 — "using a finite training sample of m labeled examples, Sm = {(xi , yi )}m i=1 , assumed to be sampled i.i.d. from some unknown underlying distribution P(X,Y ) over X × {±1}."
[^c13.2]: chow-1970
[^c13.3]: chow-1970
[^c13.4]: chow-1970
[^c14]: chow-1970
[^c15]: chow-1970
[^c16]: kadavath-2022 — "Models perform well at predicting P(IK) and partially generalize across tasks, though they struggle with calibration of P(IK) on new tasks."
[^c17]: chow-1970
[^c18]: arxiv-2601-00138 — "Sweeping threshold ε produces smooth risk-coverage tradeoffs, reducing error rates"
[^c19]: arxiv-2601-00138 — "We define abstention at the system level based solely on a confidence threshold ε, rather than relying"
[^c20]: arxiv-2601-00138 — "cannot rely on confidence thresholds tuned in-distribution."
[^c9]: chow-1970
[^c13]: chow-1970
[^c21]: arxiv-2512-23924 — "The price of abstention is only marginally smaller than random"
[^c22]: arxiv-2512-23924 — "without any low noise assumptions"
[^c23]: arxiv-2512-23924 — "enjoys proper abstention if it abstains"
[^c24]: arxiv-2512-23924 — "is a classical lower bound showing that, in high-noise regimes, active"
[^c25]: arxiv-2512-23924 — "the classifier learned in Theorem 2.2 achieves the minimax optimal label complexity under"
[^c26]: arxiv-2601-00841 — "can exhibit refusal collapse under a cheap SLO when refusal is heavily rewarded"
[^c27]: arxiv-2601-00841 — "In offline routing, cost-heavy rewards can make"
[^c28]: arxiv-2601-00841 — "per-query without explicit constraints on abstention"
[^c29]: arxiv-2601-00841 — "under cheap, Argmax-CE collapses to refusal (94.5%), yielding"
[^c30]: arxiv-2512-16795 — "evidence is labeled irrelevant or when the available information is incomplete or unverifiable; and"
[^c31]: doi-10-48550-arxiv-2408-14141 — "far off from the human probability distribution, the model will abstain"
[^c32]: doi-10-48550-arxiv-2408-14141 — "competitive with these baselines for hate speech detection and outperforms them for NLI."
[^c33]: arxiv-2512-11614 — "By using the adversarial Morgana prover to mask decisive evidence"
[^c34]: arxiv-2512-11614 — "Abstention emerges even without any manually annotated unanswerable example or preference pair"
[^c35]: arxiv-2512-11614 — "conservative, refusing to answer helpful queries because it cannot find a direct citation"
[^c36]: arxiv-2512-11614 — "Because LLMs frequently and effectively memorize benchmarks"
[^c37]: arxiv-2512-06380 — "struggle to refuse to answer and have a clear"
[^c38]: arxiv-2512-06380 — "of 92% and 96% respectively. The refusal rate for"
[^c39]: arxiv-2512-04597 — "even the best frontier model only attains 42.79% abstention recall, while humans achieve 91.17%"
[^c40]: arxiv-2512-04597 — "scaling, prompting, and reasoning only yield marginal gains"
[^c41]: arxiv-2512-04597 — "fine-tuned models overfit to textual cues"
[^c42]: arxiv-2512-04597 — "we adopt GPT-4o to determine whether each output from the embodied agent reflects a valid abstention"
[^c43]: arxiv-2512-04597 — "between LLM-based and human scores is 0.88"
[^c45]: doi-10-48550-arxiv-2607-14399 — "moved strong claims from 38/40 to 7/40, while the new incomplete verdict took 28/40 outcomes"
[^c46]: doi-10-48550-arxiv-2607-14399 — "The incomplete verdict is the calibrated-refusal code the"
[^c47]: doi-10-48550-arxiv-2607-14399 — "Whether incomplete uptake is calibrated or merely the no-lose option is not settled here"
[^c48]: arxiv-2512-01556 — "We refer to the left-hand side of Eq. (1) as the selectionconditioned error rate: the marginal error probability of a prediction after it has been selected by the calibrated rule."
[^c44]: arxiv-2512-04597 — "paraphrased into five semantically equivalent variants using a large language model"
[^c49]: arxiv-2511-21025 — "1/nchoices + 0.05"
[^c50]: arxiv-2511-21025 — "less, but avoids misleading content, is preferable to one that"
[^c51]: doi-10-48550-arxiv-2405-02228 — "frequency conditional on responding"
[^c52]: doi-10-48550-arxiv-2405-02228 — "AR and HR must be interpreted together"
[^c53]: doi-10-48550-arxiv-2405-02228 — "AR reflects epistemic caution, not correctness"
