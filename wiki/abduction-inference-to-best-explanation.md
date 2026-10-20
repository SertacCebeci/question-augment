---
description: "Abduction proposes a hypothesis explaining an observed effect; inference to the best explanation adds a comparison among rivals. Both are defeasible: a candidate is not yet a tested one."
aliases: ["abduction", "IBE", "inference to the best explanation", "abductive inference", "weak abduction", "strong abduction"]
sources: ["arxiv-2512-10080"]
---
# Abduction and inference to the best explanation

Abduction is inference from an observed effect to a hypothesised cause. The classic case: coming home to a wet lawn, you might conclude that it rained earlier. That conclusion is not certain, since a sprinkler would produce the same effect, but it is a plausible explanation.[^c1] Harman later popularised inference to the best explanation (IBE), which is abduction with a comparative step: several candidate hypotheses are generated and then weighed by criteria such as simplicity, coherence with background knowledge and scope, and the one that would best explain the evidence is tentatively accepted.[^c2]

Both are defeasible. Their conclusions can be wrong even when the reasoning looks sensible, because new evidence can defeat them. They lack the truth-preserving guarantee of deduction. The paper's phrase for what they keep is that they are "prudence-preserving: it suggests a good candidate to explore."[^c3]

**Strength varies.** The literature separates weak abduction, which is hypothesis generation without strong commitment, from strong abduction, which picks the most probable or best hypothesis. "Strong abduction entails choosing the best explanation among alternatives," and may need comparative judgment or further evidence.[^c4] Weak abduction builds a plausible story from the facts. The difference is the one between forming an insight and justifying it.

**Generation and testing are separate stages.** Reichenbach's two-stage picture puts abduction in the context of discovery, where candidates arise, and induction, or statistical inference, in the context of justification, where they are tested. "abduction provides the candidate, and induction assesses it."[^c5]

**What the concept is applied to in this paper.** The paper argues that a token-completion LLM performs the first stage and not the second. "They generate candidates (explanations, answers) but do not genuinely validate" them against reality, and in statistical terms it "perform[s] prior predictive sampling but lack[s] an external feedback loop for posterior evaluation."[^c6] The paper says LLMs "seem to perform at least weak abduction," and can "seem to carry out a form of strong abduction when all candidate hypotheses are explicitly provided."[^c7] Its account of why the output looks abductive is that the model "does not reason about causes from scratch but outputs typical causes" as they appear in its training text.[^c8] The paper calls the resulting excess of answers "over-abduction": "while the LLM often makes a guess regardless."[^c9]

The paper's central claim is that the resemblance is "not random but systematic, resulting from training on human explanations."[^c10] It also hedges the word: "When an LLM generates a plausible hypothesis for data, it is reasonable to draw an analogy to abduction, as long as we acknowledge it as an analogy."[^c10b]

**What survives the transfer and what does not.** The generate-then-test split and the defeasibility of the conclusions carry over: a candidate explanation is a reason to look, not a reason to believe. What the transfer does not supply is the comparison step. In IBE the comparison weighs rival hypotheses against the evidence; the paper's claim is that a next-token sampler produces a text shaped like such a comparison. Whether anything in the model performs the weighing is the question the paper leaves open. The philosophy also has its own disputes: some hold that IBE is "essentially a qualitative version of Bayesian reasoning," while others argue it "violates the principle of conditionalisation."[^c11] A reader who imports the term should say which version is meant.

**Use on the answerer's side.** The concept separates a candidate from a verified answer. A fluent explanation can be a good candidate and still be unchecked; the paper's own picture has the human supply the justification, since LLMs "function like brainstorming assistants that toss out" ideas.[^c12]

## Limits

- The paper establishes its claims by argument and illustration, not by measurement. Its dialogues were "created for this paper, can serve as a tangible illustration of LLM abductive behaviour"[^c13], so they show that the pattern can be produced, not how often.
- The paper's own limits: "Smaller or less trained models might not exhibit the abductive illusion as strongly."[^c14] It also uses "explanation" "as we have used it in a commonsense way," without the philosophy-of-science criteria.[^c15]
- Whether LLMs have an inference procedure at all is contested in the paper's own text: "The ongoing debate is whether LLMs merely reproduce surface patterns or possess some form of implicit models of the world and inference abilities."[^c16] The paper's claim that LLM output is only "reproducing a probable explanation" is its position, not a result.[^c17]
- The paper says any abductive reading is metaphorical: "Only metaphorically could one say that LLMs use a form of abductive heuristics."[^c18]
- (My inference) The text gives no operational test that separates weak from strong abduction in an LLM's output, so the distinction is applied by reading the examples. The concept is therefore usable for description and not yet for measurement.

## Related

- [[plausibility-masks-error]] — the reader's side of the same gap: a well-formed answer passes because its form is checked and its content is not.
- [[generate-then-verify-candidate-pipeline]] — an engineered version of the generate-then-test split, where the candidate stage and the check are separate components.
- [[causal-model-of-explanation]] — one account of what an explanation must supply (causes); the paper's commonsense use of "explanation" is the looser notion this note's comparison step presupposes.
- [[semantic-illusion]] — plausible outputs that keep the meaning of their evidence and so pass similarity checks; a cousin of the abductive appearance.
- [[cot-hallucination-trap]] — a fluent rationale that stays plausible while detached from the evidence, the machine-side failure that the abductive appearance makes easy to miss.

[^c1]: arxiv-2512-10080 — "you might abduce that it rained earlier"
[^c2]: arxiv-2512-10080 — "Harman (1965) later popularised the closely related idea of Inference to the Best Explanation"
[^c3]: arxiv-2512-10080 — "it is prudence-preserving: it suggests a good candidate to explore"
[^c4]: arxiv-2512-10080 — "Strong abduction entails choosing the best explanation among alternatives"
[^c5]: arxiv-2512-10080 — "abduction provides the candidate, and induction assesses it"
[^c6]: arxiv-2512-10080 — "They generate candidates (explanations, answers) but do not genuinely validate"
[^c7]: arxiv-2512-10080 — "They can even seem to carry out a form of strong abduction when all candidate hypotheses are explicitly provided"
[^c8]: arxiv-2512-10080 — "It does not reason about causes from scratch but outputs typical causes"
[^c9]: arxiv-2512-10080 — "while the LLM often makes a guess regardless"
[^c10]: arxiv-2512-10080 — "this resemblance is not random but systematic, resulting from training on human explanations"
[^c10b]: arxiv-2512-10080 — "When an LLM generates a plausible hypothesis for data, it is reasonable to draw an analogy to abduction, as long as we acknowledge it as an analogy"
[^c11]: arxiv-2512-10080 — "Some philosophers have argued that IBE is essentially a qualitative version of Bayesian reasoning"
[^c12]: arxiv-2512-10080 — "LLMs function like brainstorming assistants that toss out"
[^c13]: arxiv-2512-10080 — "created for this paper, can serve as a tangible illustration of LLM abductive behaviour"
[^c14]: arxiv-2512-10080 — "Smaller or less trained models might not exhibit the abductive illusion as strongly"
[^c15]: arxiv-2512-10080 — "as we have used it in a commonsense way"
[^c16]: arxiv-2512-10080 — "The ongoing debate is whether LLMs merely reproduce surface patterns"
[^c17]: arxiv-2512-10080 — "the LLM is not truly reasoning towards the best explanation; it is reproducing a probable explanation"
[^c18]: arxiv-2512-10080 — "Only metaphorically could one say that LLMs use a form of abductive heuristics"
