---
description: "A retrieval reward that weights precision by a power of recall and log-scales it at low precision, so training favours coverage first and screening burden only once recall is high."
aliases: ["recall-modulated precision reward", "recall-weighted precision term", "recall-gated precision bonus"]
sources: ["arxiv-2602-00005"]
---
# Recall-gated precision reward

When a policy's output is a set of retrieved documents, a scalar reward has to decide how much precision is worth against recall. The AutoBool paper handles this inside the reward itself, with a gate. Recall enters directly, and precision enters through a term that is "a recall-modulated reward".[^c1] The precision term is multiplied by a power of recall, so it counts little while coverage is poor. It is also log-transformed, so a small gain from very low precision registers more than the same gain near the top of the range.

The paper states three properties before it writes the formula: recall must be prioritized; precision should matter more as recall rises ("precision should matter more as recall");[^c2] and early precision gains should be emphasized. The text introduces the implementation as "To implement this, we apply two mechanisms":[^c3] the recall weighting on precision, and the logarithm, which the authors describe as "applying a logarithmic transformation to increase sensitivity when precision is low".[^c4]

The exponent alpha sets how strong the gate is. At alpha = 0.5 the reward is weakly recall-oriented, "allowing precision to contribute earlier in the learning process".[^c5] At alpha = 2 it is strongly recall-oriented, "where precision only meaningfully contributes once high" recall has been reached.[^c6] Alpha is therefore a dial between two behaviours: early pressure toward fewer results, or a policy that first climbs to high recall and only then is pushed to be concise.

The retrieval term is one of three summed parts of the total reward, with a formatting reward and a validity reward.[^c8] Degenerate retrievals get fixed values rather than the formula: an empty result set (the case "if |D| = 0") takes a flat penalty, and a query with zero recall and zero precision takes another.[^c7] These cases are a design choice of the reward, and they matter for training because an invalid query otherwise has no gradient toward a valid one.

The authors' ablation reports that the reward's hyperparameters act differently by prompt type: "prompts are more robust when hyperparameters vary, whereas no-reasoning prompts are more sensitive".[^c9] So the gate is not a universal setting; the prompt style decides how much its constants can be moved.

What transfers is the shape, not the Boolean setting. Any task whose output is a retrieved set, where a coverage measure has to be combined with a size or screening cost, faces the same choice of whether precision should count before coverage is reached. The gate answers it by making precision conditional on recall. Whether that is better than a plain F-beta or a linear mix is not tested in the parts of the paper read here (my inference: the gate is a shape choice, and a shape alone does not show it beats the simpler alternatives).

## Limits

- The relevant set is not screening judgments. The authors take the references a systematic review cites in its results as "references are treated as the included studies (i.e., the gold-standard relevant set) for that review".[^c10] A reward built on citation-derived relevance inherits whatever citations miss or include.
- The main comparisons are against prompting and against larger GPT models, not against alternative reward shapes on the same training run. The sensitivity analyses for the scale factor, the smoothing constant and the penalty values sit in Appendix A.4, which I did not read in full; the claim that every component matters rests on the paper's summary of them.
- Stability depends on the backbone. The authors found the LLaMA runs "significantly less stable than Qwen3", with reward collapses, so the reward's effect is not separated from the optimizer's behaviour in those runs.[^c11]
- The smoothing constant s = 100 and the global scale M are fixed in the main setup. The parts read do not justify those values beyond the appendix.

## Related

- [[recall-only-partial-credit]] — recall alone cannot register over-selection; this gate adds a precision term, but makes it unable to offset missed recall, which is my reading of the design's purpose.
- [[context-recall-precision-tradeoff]] — the same favour-recall-first trade, here in a context-retrieval setting rather than in a training reward.
- [[prompted-versus-trained-query-augmentation]] — reinforcement learning against a retrieval reward is the training setting in which this reward is used.
- [[hard-tail-recall-threshold]] — the paper also reports the share of queries above 80% and 90% recall, a tail measure of the kind that note treats; the link is my reading.

[^c1]: arxiv-2602-00005 — "It balances a direct reward for recall and a recall-modulated reward for"
[^c2]: arxiv-2602-00005 — "precision should matter more as recall"
[^c3]: arxiv-2602-00005 — "To implement this, we apply two mechanisms"
[^c4]: arxiv-2602-00005 — "applying a logarithmic transformation to increase sensitivity when precision is low"
[^c5]: arxiv-2602-00005 — "allowing precision to contribute earlier in the learning process"
[^c6]: arxiv-2602-00005 — "where precision only meaningfully contributes once high"
[^c7]: arxiv-2602-00005 — "if |D| = 0"
[^c8]: arxiv-2602-00005 — "The final reward combines all components"
[^c9]: arxiv-2602-00005 — "prompts are more robust when hyperparameters vary, whereas no-reasoning prompts are more sensitive"
[^c10]: arxiv-2602-00005 — "references are treated as the included studies (i.e., the gold-standard relevant set) for that review"
[^c11]: arxiv-2602-00005 — "their RL training was significantly less stable than Qwen3"
