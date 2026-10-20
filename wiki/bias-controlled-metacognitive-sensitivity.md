---
description: "Raw agreement between a model's yes/no 'do you know' answer and its correctness is inflated by yes-bias; d'type2 separates item-level self-knowledge from response tendency, and can be trained up."
aliases: ["d'type2", "type 2 d-prime", "metacognitive sensitivity", "dual-questioning protocol"]
sources: ["arxiv-2602-02605"]
---
# Bias-controlled metacognitive sensitivity

Whether a model "knows what it knows" is usually scored as raw alignment: the share of items where its yes/no meta answer ("do you know X?") matches whether its direct answer was correct. Park et al. (2026) show this number mostly measures accuracy times yes-rate, and replace it with d'type2, the signal-detection separation between the model's meta answers on correct versus incorrect items.

## Mechanism

Each item is posed twice in independent contexts: a direct question and a meta question, so the meta answer cannot self-confirm against the model's own earlier answer.[^c1] The score is d'type2 = Φ⁻¹(Hit Rate) − Φ⁻¹(False Alarm Rate); about 0 is chance, about 0.5 is a low lower bound, about 1.0 is moderate, and 2.5 or more is near ceiling.[^c2]

Raw alignment fails because a model that answers 90% of direct questions correctly gets 90% raw alignment by saying Yes to every meta question.[^c3] In the paper's closed-model comparison, Gemini 3 Flash had the highest raw alignment (90.71%) yet the lowest d'type2 (0.68) of the proprietary models, with a 96.34% yes ratio; d'type2 penalises the response-bias false alarms.[^c4] The paper also tracks Yes Failure Ratio (claims to know, answers wrongly) and No Failure Ratio (claims not to know, answers rightly) as the two error directions.[^c5]

The metric is trainable. The paper's evolution-strategy fine-tuning, rewarded on agreement between direct correctness and meta answer across independent passes, raised d'type2 in all open models toward 1.0; a Qwen2.5 3B model reached 1.02 despite lower accuracy than proprietary models, which the authors read as improved discrimination rather than a global strategy shift.[^c6] On FictionalQA (invented events, so prior familiarity cannot proxy for correctness), d'type2 rose to 0.65 for a model that had learned the facts by SFT and never saw meta prompts there.[^c7] Patching only the top 10% largest-magnitude weight changes lifted d'type2 from 0.20 to 0.63, most of the total gain.[^c8]

## Limits

The evidence is the authors' own; d'type2 is computed from binary meta answers, so it cannot see graded confidence (a continuous Type 2 AUROC is reported as a complement). The FictionalQA result is for one 1.5B model. Whether a high d'type2 reflects access to internal states, rather than a learned heuristic the controls missed, is argued by elimination, not shown. The sparse-subnetwork reading ("specialized subnetwork") is the authors' suggestion, not a demonstration; the patching test is correlational. Note the tension with [[individuated-metacognition]], where untrained frontier models' binary confidence collapsed to a shared difficulty axis; here d'type2 on a single model does not test whether its signal is model-specific, so the two measures are not the same claim (my inference).

## Related

- [[individuated-metacognition]] — asks whether confidence is model-specific; this note asks whether it discriminates correct from incorrect once yes-bias is removed
- [[calibration]] — calibration is a different property from discrimination sensitivity
- [[abstention]] — a meta answer of No is an abstention signal whose worth is its d'type2

[^c1]: arxiv-2602-02605 — "Isolating these inquiries within independent contexts ensures that meta answers preclude self-confirmation"
[^c2]: arxiv-2602-02605 — "d′type2 = Φ−1 (Hit Rate) − Φ−1 (False Alarm Rate)"
[^c3]: arxiv-2602-02605 — "it can achieve 90% raw alignment simply by"
[^c4]: arxiv-2602-02605 — "d′type2 penalizes such response-bias-driven"
[^c5]: arxiv-2602-02605 — "Yes Failure Ratio (YFR): The proportion of instances where the model claims to know the"
[^c6]: arxiv-2602-02605 — "This result suggests that ESMA improves"
[^c7]: arxiv-2602-02605 — "the application of ESMA resulted in a significant increase in d′type2 to 0.65."
[^c8]: arxiv-2602-02605 — "value rose sharply from 0.20 to 0.63"
