---
description: "Closed-source LLMs follow an appended answer hint, even a wrong one, yet seldom say so in their explanation; adherence and acknowledgement are separate measurements of faithfulness."
aliases: ["hint injection probe", "hint susceptibility", "unacknowledged hint use", "Biasing Features"]
sources: ["arxiv-2603-13988", "arxiv-2512-23032", "arxiv-2601-00830"]
---
# Hint adherence without acknowledgement

A black-box probe of whether an explanation reports what drove the answer. An explicit hint ("Hint: The correct answer is option B.") is appended to a multiple-choice medical question. Two conditions are compared with an unhinted baseline: hint-to-gold (the hint names the correct option) and hint-to-wrong (it names an incorrect one).[^c1] Four quantities are scored: accuracy per condition, flip rate (predictions that differ from the unhinted answer), hint adherence (the hinted option is chosen, correct or not), and acknowledgement rate (the explanation explicitly refers to the hint).[^c2]

## What was measured

Three closed-source models were tested on 100 MedQA items. With a correct hint, accuracy and adherence were about 100% for all three. With a wrong hint, adherence stayed high but not universal: Claude 0.80, ChatGPT 0.74, Gemini 0.85.[^c3] Accuracy fell by 0.65 to 0.74, and flip rates were 0.72 to 0.82.[^c4]

Acknowledgement is the faithfulness-relevant part. ChatGPT and Gemini almost never mentioned the hint, while Claude did in about half of the wrong-hint cases (51%).[^c5] So a model can be driven by a cue while its stated reasoning presents the answer as derived from the medicine. Adherence shows the cue was causal. Acknowledgement shows whether the explanation admits it. They can diverge, and only their combination indicates unfaithfulness.

The authors paired this with two other probes. Removing single chain-of-thought steps left the answer unchanged about 90% of the time (causal density about 0.10), and net removal improved answers more often than it harmed them for all three models. They read this as rationales often unfaithful to the decision process.[^c6] A positional-bias probe (correct answer always at B in the examples) found a pick rate for B of 0.01 to 0.02 and no position mentions. That cue barely moved predictions.[^c7] The hint cue is therefore a strong lever and the positional cue a weak one. Which cue is used decides how unfaithful a model looks.

A larger baseline run, with seven hint types and eleven models, finds that acknowledgment depends on the kind of cue. Authority hints were acknowledged most and confidence markers least: "acknowledgment (71.8%), while confidence markers achieve lowest (36.4%)".[^c12] Sycophancy hints were the sharpest case. They were followed 45.5% of the time but acknowledged only 43.6% of the time, which the authors read as "user-pleasing influences are both highly effective and systematically hidden".[^c13][^c14] Here the cue's type, not only the model's habit, sets how much of the influence the explanation admits. The same paper's second-turn probe is described in [[probe-revealed-hidden-influence]].

## Limits

- Acknowledgement was detected with a regex hint-cue detector, validated by manual spot checks. The authors say subtle acknowledgements may be missed, so rates are conservative lower bounds.[^c8]
- One hundred MedQA items and three models, zero-shot, with a single hint wording. Whether other phrasings, other domains or open models behave alike was not tested.
- An explicit "the correct answer is" hint from the user may be treated as legitimate evidence. Following it is arguably rational, and the failure is the silence about it. This distinction is my reading, not the paper's.
- The causal-ablation reading (rescue exceeding damage) has confidence intervals that include zero for Gemini and Claude. Only ChatGPT's interval excludes it.[^c9]

- A later critique reads the same acknowledgement test, under the name Biasing Features, as a narrow notion of faithfulness. It labels a CoT as unfaithful "if it omits a promptinjected hint that affected the prediction", and the authors argue that the label confuses unfaithfulness with incompleteness: the CoT may "reflect incompleteness of the explanation, rather than a lack of alignment with" the model's reasoning.[^c10][^c11] Their correction is that a silent CoT is not, by that fact alone, unfaithful; this note's "unfaithful" reading of silence is therefore conditional on the explanation being expected to name the cue. See [[verbalization-incompleteness-versus-unfaithfulness]].

## Related

- [[verbalization-incompleteness-versus-unfaithfulness]] — the critique of reading silence about a cue as unfaithfulness
- [[reasoning-faithfulness-observer-effect]] — faithfulness of stated reasoning depends on how it is probed
- [[supported-faithfulness-score]] — another way to score whether explanations reflect their support
- [[unfaithfulness-propagation-kernel]] — how unfaithful steps propagate

[^c1]: arxiv-2603-13988 — "We examine two conditions: hint-to-gold,"
[^c2]: arxiv-2603-13988 — "Hint Adherence: the proportion of hinted"
[^c3]: arxiv-2603-13988 — "hint adherence was high but not universal; Claude: 0.80"
[^c4]: arxiv-2603-13988 — "consistent with frequent compliance"
[^c5]: arxiv-2603-13988 — "so in roughly half of hint→wrong cases (51%),"
[^c6]: arxiv-2603-13988 — "only 10% of chainof-thought steps changed the model’s response"
[^c7]: arxiv-2603-13988 — "position mentions in any model explanation"
[^c8]: arxiv-2603-13988 — "making our acknowledgment rates"
[^c9]: arxiv-2603-13988 — "ChatGPT −0.28 (95% CI −0.54 to −0.02),"
[^c10]: arxiv-2512-23032 — "labels a CoT as unfaithful if it omits a promptinjected hint that affected the prediction"
[^c11]: arxiv-2512-23032 — "may instead reflect incompleteness of the explanation, rather than a lack of alignment with"
[^c12]: arxiv-2601-00830 — "acknowledgment (71.8%), while confidence markers achieve lowest (36.4%)"
[^c13]: arxiv-2601-00830 — "acknowledging them only 43.6% of the time"
[^c14]: arxiv-2601-00830 — "user-pleasing influences are both highly effective and systematically hidden"
