---
description: "Humans rejected more AI verdicts as the AI grew more confident, most of all when it accused a statement of deception; confidence lowered adoption instead of raising it."
aliases: ["high-confidence aversion", "confidence-driven rejection of AI judgments", "aversion to confident algorithmic accusations"]
sources: ["arxiv-2512-02848"]
---
# High-confidence aversion to AI judgments

Given an AI's verdict on a single statement, people did not adopt it more as its stated confidence rose. In a deception-detection experiment, participants judged statements while shown veracity predictions from a fictitious classifier. Each prediction carried one of five confidence levels, and the authors measured how far each person's own judgment departed from the model's. The headline result is that "humans followed predictions from a highly accurate model more than from" a less accurate one,[^h1] but that "the more confident the model, the more people deviated" from it.[^h2] The deviation was largest for predictions of deception: humans "tended to disagree more from AI accusations of deception."[^h5]

The mechanism, as measured, is a shift in how far the person moves away from the verdict, not a loss of attention to it. Under the high-accuracy model, deviation from deception predictions rose only at the top confidence levels, while deviation from truthful predictions rose more gradually.[^h6] The authors summarise the pattern as "participants tend to reject more over-confident" predictions, "especially those stemming from a low-accuracy model and those predicting deception."[^h16] Their pre-registered hypothesis, that confidence would raise endorsement of the accurate model, "was only partially supported."[^h3] The sign of the confidence effect ran against the trust literature the paper cites: they observed "greater deviations from very confident predictions than from low-confident ones."[^h4]

Two further results bear on what the rejection costs. Participants who relied on the model's predictions reached an AUC of 0.76 against 0.90 for the model alone, "Yet, this detection rate was significantly lower than" the model's.[^h6b] The authors read this as human interaction "worsens detection performance compared to relying entirely on the AI model."[^h7] Under the low-accuracy model, human performance (AUC 0.57) "mirror[ed]" the model's (0.54) "yet without" overcoming it.[^h8]

The rejection tracked beliefs about who is better at the task. Deviations were larger for participants who thought themselves or the average human better than the AI, which the authors read as "display larger deviations from the algorithmic predictions."[^h10] They offer overestimation of one's own detection skill as part of the explanation, a "tendency to overestimate their own deception detection" capacity.[^h9] The same paper gives a second account, through the truth-default theory, in the [[truth-default-theory]] note.

The confidence values were assigned by the design, not produced by a trained model: "the confidence range and value remained randomly assigned but flipped" when a prediction was wrong.[^h11] So what the participants saw was a labelled level of confidence, attached to a set of correct and incorrect predictions in fixed proportions.

For asking and answering, the transferable concept is that a confidence figure attached to an accusation can lower its uptake. The stated certainty of an answer is read by the receiver against the stakes of the claim, and a high figure on a damaging claim can read as overreach. This is my inference from the measured pattern, not a finding of the paper.

## Limits

- The predictions were always visible; this is a forced condition. "our study explored the role of transparency on trust exclusively under a forced condition"[^h13], so a choice to request AI output may change the result.[^h12]
- The incentive was absent: "we run our experiment in a non-incentivised task, and we did not provide any"[^h14] information about consequences for the accused. The authors expect that consequences could make aversion stronger, which is untested.
- Exclusions shaped the result: "when previously excluded participants were included in the analysis" the three-way interaction was no longer significant, so the attention-based sample matters.[^h15]
- The authors offer two explanations and report that the link to self-belief is small, "since these associations are small, other" factors may contribute.[^h17]
- One task (verbal deception judgments about autobiographical statements), one fictitious model, one accuracy contrast (54% vs 89%).

## Related

- [[truth-default-theory]] — the second account the authors give for the rejection of accusations
- [[over-reliance-discrimination-failure]] — the reverse failure: wrong AI answers adopted rather than confident accusations rejected
- [[rationale-certainty-framing-trust-shift]] — a certainty cue raised trust in a factual answer in another study; here the same kind of confidence lowered adoption of a deception verdict, so the direction depends on the claim

[^h1]: arxiv-2512-02848 — "humans followed predictions from a highly accurate model more than from"
[^h2]: arxiv-2512-02848 — "the more confident the model, the more people deviated"
[^h3]: arxiv-2512-02848 — "However, this hypothesis was only partially supported."
[^h4]: arxiv-2512-02848 — "greater deviations from very confident predictions than from low-confident ones."
[^h5]: arxiv-2512-02848 — "tended to disagree more from AI accusations of deception."
[^h6]: arxiv-2512-02848
[^h6b]: arxiv-2512-02848 — "Yet, this detection rate was significantly lower than"
[^h7]: arxiv-2512-02848 — "worsens detection performance compared to relying entirely on the AI model."
[^h8]: arxiv-2512-02848 — "with human performance mirroring that of the corresponding model, yet without"
[^h9]: arxiv-2512-02848 — "tendency to overestimate their own deception detection"
[^h10]: arxiv-2512-02848 — "display larger deviations from the algorithmic predictions."
[^h11]: arxiv-2512-02848 — "the confidence range and value remained randomly assigned but flipped."
[^h12]: arxiv-2512-02848 — "our study entails the fact that the"
[^h13]: arxiv-2512-02848 — "our study explored the role of transparency on trust exclusively under a forced condition"
[^h14]: arxiv-2512-02848 — "we run our experiment in a non-incentivised task, and we did not provide any"
[^h15]: arxiv-2512-02848 — "when previously excluded participants were included in the analysis"
[^h16]: arxiv-2512-02848 — "This pattern of findings confirms that participants tend to reject more over-confident"
[^h17]: arxiv-2512-02848 — "since these associations are small, other"
