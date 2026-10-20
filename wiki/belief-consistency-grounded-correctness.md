---
description: "A hidden-state probe can track a step's coherence with the prefix it was given instead of its correctness, so the two signals split once the prefix holds an error."
aliases: ["belief consistency", "grounded correctness", "belief-consistency versus grounded correctness", "prefix coherence versus correctness"]
sources: ["doi-10-48550-arxiv-2605-17877"]
---
# Belief consistency versus grounded correctness

A turn in a multi-step trajectory can be judged by two different things. Belief consistency is whether the turn is coherent with the history that precedes it. Grounded correctness is whether the turn makes real progress toward the task. When the history is clean the two mostly agree: the paper's own wording is that "a step that is coherent with a correct history is also likely correct".[^c7] They come apart when the history contains an error. A step that carries the error forward is coherent with the prefix and wrong; a step that repairs the error contradicts the prefix and is right.

The Kim et al. work reports that a linear probe on an LLM's hidden states, read at the evaluation turn, degrades under this kind of contamination. The probes degrade "tracking coherence with the (possibly corrupted) prefix rather than grounded correctness".[^c1] The explanation the authors give concerns training: the next-token objective "optimizes representations to capture what is coherent with the prefix, not what is objectively correct for the underlying task".[^c2] The authors state this as a hypothesis, not as a measured mechanism: "we hypothesize that the hidden state encodes belief-consistency".[^c6]

The mechanism is tested with a diagnostic set in which the two notions are set against each other. Each item is a contaminated prefix and a candidate turn, and the candidates are either consistent-but-incorrect (they follow the error) or repair turns (they fix it and contradict the prefix). The design fixes what each kind of probe should do: "By construction, a probe tracking belief-consistency will rank consistent-but-incorrect above repair turns (AUROC at or below chance)".[^c3] The reported result is that the hidden-state probes behave in the first way, and the authors draw the RL consequence directly: "using such a probe as a reward would actively penalize repair".[^c4]

The complement is attention. Attention-based features "remain robust to contamination but underperform on clean" prefixes.[^c5] The authors' reading is that attention records where the model routes information rather than the accumulated content, so it is less tied to whether the prefix was right. That reading is theirs and is not separately tested here.

The reward built on this diagnosis (PAIR) is not the point of this note. The transferable part is the split itself: a signal read from a model's own state can measure coherence with what was said, and when the said thing is wrong, coherence rewards repeating it. For asking and answering, my inference is that any judge of a reply whose signal is "does this fit the conversation so far" inherits the same bias, and that a check for fit is not a check for correctness. The paper does not test answer-level judging in conversation; this extension is mine.

## Limits

- The main probing experiment uses one backbone, Qwen-2.5-7B-Instruct, with linear probes.[^c8] The text I read does not show the split with other models or at other scales.
- The contamination is constructed: earlier steps are replaced with erroneous alternatives, and the matched clean and contaminated prefixes are made by the authors. Whether naturally occurring errors produce the same divergence is not tested.
- The diagnostic dataset makes the two notions oppose each other by design. It shows which signal a probe reads when they are opposed; it does not show how often they are opposed in ordinary trajectories.
- The probes in the main experiment are trained on clean data and then applied to contaminated prefixes. Whether training on contaminated data would make a probe track correctness is not what the paper tests, by my reading.
- The belief-consistency label is the authors' hypothesis, and the attention explanation is their reading. Neither is a measured mechanism in the text I read.
- The study is about step-level rewards in agent reinforcement learning. Its carry-over to judging a reply in a dialogue is my inference.

## Related

- [[belief-entrenchment]] — belief updates predictable from the prior belief; there the drift is measured on the update, here the signal is a turn's coherence with the prefix.
- [[evidence-grounded-step-reward]] — another step-level signal for RL, which checks each step against retrieved evidence rather than against the preceding trajectory.
- [[misconception-regime-output-confidence-failure]] — internal correctness probes still work where output-based confidence fails; a contrast to the failure of hidden-state probes under contamination here.
- [[internal-prober]] — a hidden-state read-out used to predict a gain, whose reliance on the internal state is the same kind of dependence.

[^c1]: doi-10-48550-arxiv-2605-17877 — "tracking coherence with the (possibly corrupted) prefix rather than grounded correctness"
[^c2]: doi-10-48550-arxiv-2605-17877 — "optimizes representations to capture what is coherent with the prefix, not what is objectively"
[^c3]: doi-10-48550-arxiv-2605-17877 — "tracking belief-consistency will rank consistent-but-incorrect above repair turns (AUROC at or below chance)"
[^c4]: doi-10-48550-arxiv-2605-17877 — "probe as a reward would actively penalize repair"
[^c5]: doi-10-48550-arxiv-2605-17877 — "attention-based features remain robust to contamination but underperform on clean"
[^c6]: doi-10-48550-arxiv-2605-17877 — "we hypothesize that the hidden state encodes belief-consistency"
[^c7]: doi-10-48550-arxiv-2605-17877 — "a step that is coherent with a correct history is also likely correct"
[^c8]: doi-10-48550-arxiv-2605-17877 — "We use Qwen-2.5-7B-Instruct [26] as our backbone"
