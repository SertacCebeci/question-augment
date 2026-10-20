---
description: "An intent no single part states can be recovered from a sequence of parts; the paper ties that recovery to logical links between parts and to how many parts there are."
aliases: ["cross-input intent aggregation", "sequential intent externalization", "intent assembled across a sequence"]
sources: ["arxiv-2512-05853"]
---
# Sequential intent assembly

An intent can be stated nowhere in a sequence and still be recovered from it. The VRSA paper, a visual jailbreak study, names the aim directly: the method is meant to make a model "gradually externalize and aggregate complete harmful intent by decomposing the original harmful text into several sequentially related sub-images."[^s1] The mechanism is that a reader who sees the parts in order links them into one narrative. Each part can read as ordinary content; the intent is only present in the whole.

Two properties of this assembly are measured in the paper, and one is described.

The first is that the links between parts carry weight. The paper scores logical coherence across the parts, and reports that adding its link step moves that score "from 2.34 to 3.56, indicating a stronger logical flow" across the parts.[^s2] The score is a measure of the sequence's internal coherence, not of whether the intent is recovered. The paper's ablation table reads the two together: attack success rises as components are added, and the authors say the components "can improve toxic score and attack success rate to varying degrees."[^s3]

The second is that the number of parts has an interior optimum. The paper varies the sequence length from one to six parts. More parts give more room to spread the intent, but "after reaching a certain quantity limit" the reader finds it "increasingly difficult for the MLLMs to understand the harmful intention of the visual reasoning task, resulting in a decrease in the effectiveness of the attack."[^s4] So recovery is not monotone in length. Past a point the reader fails to rebuild the whole from its parts, and the same failure would lower the success rate that the paper reports.

Read onto asking and answering, the transfer is mine, not the paper's. A question or a request assembled over several turns or several inputs is judged by a responder who may commit to a reading of each part before the whole is in view. If the responder recovers the whole, its commitment is to the assembled request; if it tracks each part alone, the request can read as harmless at every step. Which one happens depends on the links, and on how many parts the responder has to hold at once. The paper does not test multi-turn text, so this is a hypothesis the wiki carries, not a finding.

## Limits

- The only measured recovery is an attack success rate on a harmful-output judgement. The paper does not measure comprehension of the sequence in a neutral task, so it does not show that the reader understood the intent in the sense an answerer would need.
- The coherence scores are not shown to be human-rated. The paper's scene-selection step is an LLM judgement: "Here we apply the LLM with our pre-defined prompt Psim to judge the semantic correlation."[^s5] The method for the logical coherence score was not read closely, so its reliability is unknown.
- The ablation is on one subset and one model. The paper says it runs "ablation studies on the Illegal Activities subset using GPT-4o."[^s6] The length curve is in a figure whose values were not read here; the interior optimum is taken from the authors' description, not from numbers.
- The sequence in the single-turn setting is concatenated into one image. The paper notes the same parts could be used across turns, but that setting is not the one its results report. Whether a text sequence, or a multi-turn sequence, shows the same length effect is not tested.
- The paper's main claim is about attack success. Nothing in the parts read shows that recovery falls in ordinary use, where no one is trying to hide an intent.

## Related

- [[decomposed-breach-verdict]] — separates harm, alignment and detail for a jailbreak response, so a sequence can succeed on one axis and fail on another; the verdict is the place where assembly would show up as a mismatch.
- [[cross-modal-aggregation-gap]] — combining a figure and its caption did not beat the better single channel; the two papers measure different outcomes, so they do not contradict each other, but both ask whether parts are combined into one judgement.
- [[script-level-obfuscation]] — a second way a harmful request keeps its intent while the surface changes; there the change is in the characters, here in the arrangement of parts.

[^s1]: arxiv-2512-05853 — "gradually externalize and aggregate complete harmful intent by decomposing the original harmful text into several"
[^s2]: arxiv-2512-05853 — "score from 2.34 to 3.56, indicating a stronger logical flow"
[^s3]: arxiv-2512-05853 — "can improve toxic score and attack success rate to varying"
[^s4]: arxiv-2512-05853 — "increasingly difficult for the MLLMs to understand the harmful intention of the visual reasoning task"
[^s5]: arxiv-2512-05853 — "Here we apply the LLM with our pre-defined prompt Psim to judge the semantic correlation"
[^s6]: arxiv-2512-05853 — "we perform ablation studies on the Illegal Activities subset using GPT-4o"
