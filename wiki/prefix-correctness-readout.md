---
description: "A correctness head trained only on finished generations can score a partial one; in one paper it matched full-solution performance after 40% of the completion."
aliases: ["early correctness prediction", "partial-trajectory verification", "prefix verifier", "early failure detection"]
sources: ["arxiv-2512-20578"]
---
# Prefix correctness readout

Most correctness checks wait for the answer. A check on a partial generation asks something different: whether the trace so far already shows that the run is going wrong. The Gnosis paper tests whether a head fit on complete trajectories can be applied to prefixes without refitting. It reports that the ability "is emergent": "although Gnosis is trained exclusively on complete" trajectories, "it generalizes zero-shot to partial prefixes without any additional fine-tuning."[^c1]

The reported numbers come from a figure and its text. On both math reasoning and TriviaQA, the head "reaches near-peak accuracy and positive BSS after observing only 40% of the generation."[^c2] The figure caption puts it the same way: "Gnosis already matches the full-solution performance of the other methods" after 40% of the completion.[^c3] The contrast drawn is with external reward models and a single-token probe, which the paper says need the full response before they stabilise.[^c4]

The mechanism is the fixed-size input described in [[fixed-budget-trace-descriptor]]. A prefix is pooled to the same budget as a full trace, so the same head reads it with the same cost, and nothing is retrained. That is what makes the readout a candidate for control rather than only for scoring. The paper draws two uses from it. A chain of thought "can be terminated immediately if" the internal alarm fires, which prevents "wasted compute on failing paths"; or the query can be escalated to a stronger model when the current backbone is judged unable to answer correctly.[^c5]

The wiki's own reading of stopping rules is relevant here. [[stop-continue-criteria-in-retrieval-loops]] reports that most multi-hop retrieval systems stop at a fixed hop, token or latency budget, and that state-dependent stops are rare. A prefix readout is a state-dependent stop of the kind that survey says is uncommon. My inference: a head that scores the trace so far is a stop rule of that type, and the paper's result is about whether such a score can be read early, not about whether stopping on it saves net compute.

## Limits

- The prefix result is for complete-trajectory training only. The text does not say how a prefix is labelled, and I could not find a statement of the target a prefix is scored against: whether it is the final answer's correctness, or something else.
- The 40% figure is one reported point. The curve across prefix lengths is in the figure, not in the text I read, so the shape between 0% and 40% is not in the text.
- Two domains are shown, math reasoning and TriviaQA. Prefix behaviour on the MMLU-Pro domain and on other backbones is not stated in the text I read.
- The paper says the readout "enables aggressive compute-aware control policies."[^c6] That is a statement of what the score makes possible. The text reports no end-to-end run in which a stop or escalation rule is applied and total compute and accuracy are both measured.
- Stopping early on a low score can cut a trace that would have recovered. This cost is not measured. My inference.

## Related

- [[stop-continue-criteria-in-retrieval-loops]] — stop rules in multi-hop retrieval, where state-dependent stops are reported as rare; a prefix readout is one such stop.
- [[fixed-budget-trace-descriptor]] — the fixed-size input that lets one head read a prefix of any length at the same cost.
- [[trajectory-geometry-uncertainty-probe]] — a per-token readout over layers; the prefix readout instead reads the whole trace so far, across positions.
- [[single-pass-internal-signal-detector]] — a single-pass detector read during generation; the prefix readout asks the same kind of question before the generation ends.
- [[joint-reward-cost-prediction]] — the same kind of prefix readout extended to a joint distribution over final reward and remaining length, read from reserved logits in the same forward pass. Whether it transfers beyond the math setting is not tested there.

[^c1]: arxiv-2512-20578 — "although Gnosis is trained exclusively on complete"
[^c2]: arxiv-2512-20578 — "reaches near-peak accuracy and positive BSS after observing only 40% of the generation"
[^c3]: arxiv-2512-20578 — "Gnosis already matches the full-solution performance of the other methods"
[^c4]: arxiv-2512-20578 — "single-token learnable probe typically require the"
[^c5]: arxiv-2512-20578 — "preventing wasted compute on failing paths"
[^c6]: arxiv-2512-20578 — "This enables aggressive compute-aware control policies"
