---
description: "How many agents hold the opposing view changes whether a strongly held belief moves in debate; the effect is model-dependent and, on the ethics set, not monotone in group size."
aliases: ["peer pressure", "majority pressure"]
sources: ["arxiv-2512-06573"]
---
# Peer-group size and belief change

A target agent that holds a belief strongly is placed among a peer group that argues the opposite. The question is how often the target's belief moves, and whether the number of peers matters. In the paper's setup the target starts at strength 5 and open-mindedness 5, and the peers each defend the same wrong or misaligned answer. Over four rounds of debate, the target's belief strength tends to fall, and the change comes late: "belief revision typically occurs gradually. Target agents often maintain their initial stance during the first rounds."[^c1] The authors describe the mechanism as one of emphasis: "persuaders tend to emphasize their strongest arguments rather than engage deeply in back-and-forth discussions."[^c2] The target's score tends to hold until it is already weak, and the authors report that belief change came mainly once strength reached 1 or 2.

The effect of group size is the measured quantity. On the multiple-choice set (MMLU), with peer groups of one or three, the result is that "for the models in the peer group size of 3, a lower belief change rate" appeared.[^c3] Two of the three models showed a significant negative correlation between group size and change; the third did not reach significance. On the ethics set (Aporia), with one to four peers, the pattern is not monotone. "When there is only one persuader, belief revision and belief change are more frequent than when there are two persuaders. Additionally, when the peer group size increases to three or four, the belief change rate rises again, implying that larger peer groups have a more substantial influence on the target agent."[^c4] The authors read the whole as support for the peer-pressure hypothesis: "the size of the peer group affects the belief change rates of the aligned agents."[^c5]

The background for this is a conformity result the paper cites: "LLM agents frequently concur with the beliefs of the majority, even when these hypotheses are inaccurate, particularly as the majority's size increases."[^c6] The paper's contribution is to measure the same effect on a belief that is stored as a strength, so that change can be read round by round rather than only at the end.

## Limits

- The group sizes are few. MMLU used peer groups of one and three; Aporia used one to four. Five runs per condition. Correlations on so few group sizes are fragile, and the non-monotone Aporia pattern is reported, not explained.
- The direction is model-dependent. On Aporia, the paper's own correlations have opposite signs for different models: Llama-3.3 is negative and Phi-4 positive, and GPT-4o-mini "rarely change[s] their belief strength, and belief change is nonexistent" in its condition. A single group-size law is not what the data show.
- The peers are homogeneous. "Each debate used a homogeneous setup, where all agents in the group used one of the aforementioned models."[^c7] Mixed-model peer groups, where pressure might come from a stronger or weaker source, are not tested.
- The target is maximally open. "All agents have very high open-mindedness (level 5)."[^c8] Because the earlier result shows that open-mindedness moves belief change, the pressure figures are for the most revisable setting, and the paper does not show how they change for a target with a lower weight.
- On MMLU the peers defend a randomly chosen wrong answer. The pressure in that set is toward error, and the paper does not separate the effect of group size from the effect of the argument's quality or from the target's own confidence.
- Belief change is read from the model's own revised score, not from an independent measure of whether the target was persuaded.

## Related

- [[belief-box]] — the stated belief whose strength is read round by round under pressure
- [[open-mindedness-revision-weight]] — the target's weight on argument, held at its maximum in these runs
- [[debate-elicits-sycophancy]] — pressure from an argued position versus a direct question; a related test of whether a model yields
- [[confidence-gated-fusion]] — a debate that runs only when one agent's confidence is well ahead of the other's; a different gate on who argues to whom (my contrast)

[^c1]: arxiv-2512-06573 — "belief revision typically occurs gradually. Target agents often maintain their initial stance during the first rounds"
[^c2]: arxiv-2512-06573 — "persuaders tend to emphasize their strongest arguments rather than engage deeply in back-and-forth discussions"
[^c3]: arxiv-2512-06573 — "we observed for the models in the peer group size of 3, a lower belief change rate"
[^c4]: arxiv-2512-06573 — "When there is only one persuader, belief revision and belief change are more frequent than when there are two persuaders"
[^c5]: arxiv-2512-06573 — "The size of the peer group affects the belief change rates of the aligned agents."
[^c6]: arxiv-2512-06573 — "LLM agents frequently concur with the beliefs of the majority, even when these hypotheses are inaccurate"
[^c7]: arxiv-2512-06573 — "Each debate used a homogeneous setup, where all agents in the group used one of the aforementioned models."
[^c8]: arxiv-2512-06573 — "All agents have very high open-mindedness (level 5)"
