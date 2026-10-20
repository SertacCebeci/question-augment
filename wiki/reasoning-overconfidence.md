---
description: "On multi-solution tasks an LLM states more confidence than the share of correct answers it recovers; short chain-of-thought shows this strongly, long chain-of-thought less so."
aliases: ["ROC", "confidence-completeness gap"]
sources: ["arxiv-2512-01725"]
---
# Reasoning overconfidence

A multi-solution task asks for every valid answer to one problem, so the
returned set is scored by how much of the ground-truth set it covers.
Reasoning overconfidence (ROC) is the case where the model's stated
confidence in that returned set exceeds how much of the true set it
actually recovers. The test is a per-instance inequality: a model is
reasoning-overconfident "when its reported confidence exceeds its observed
performance", with performance taken as recall.[^c1] Recall is used
instead of F1 because F1 "would blur the exploration shortfall we seek to
isolate."[^c2] The authors' point is that the failure is an omission made
with confidence: the answers given may be right, and the trouble is what
is missing. Precision would mix that omission with errors in the answers
that were given.

The effect was measured on MuSoBench, a benchmark the authors built from
two enumeration tasks: TimeTabling (conflict-free course schedules) and
SubsetSum (all subsets of a set that sum to a target). The corpus "spans
ten complexity levels and the SubsetSum corpus seven, with 100 instances
per level," and every instance's full solution set was enumerated
algorithmically and checked by hand.[^c3] On this benchmark the
conventional short chain-of-thought (Short-CoT) prompt shows the effect
strongly: "Short-CoT produces expected calibration error (ECE) values above
78.22% for every model".[^c4] On the recall-confidence plot its outputs
fall in "the low-recall, high-confidence corner."[^c5] The authors' account
of the behaviour is that Short-CoT "seldom revis[es] its initial reasoning
path, which largely explains its inflated confidence."[^c6]

Long chain-of-thought (Long-CoT), trained for extended reasoning with
reflection, reduces the effect. It "decreases the ECE by at least 18.28%
across all model families", and for closed-source models gives single-digit
ECE. Open-source models did not reach calibration: "open-source models
continue to exhibit pronounced ROC, exceeding" 56.46% even after Long-CoT
prompting.[^c7][^c8]

Several factors move the effect in the same direction across these runs.
Longer reasoning traces carry lower confidence: Figure 5(a) "shows a strong
negative correlation: extended chains yield lower confidence."[^c9] As task
complexity rises and the solution space shrinks, Short-CoT keeps its
confidence while recall falls: "maintains high confidence while recall drops
sharply, revealing persistent overconfidence."[^c10] Decoding temperature
does not help: it "increases token-level diversity rather than alleviating
ROC or expanding solution" coverage.[^c11] Reflection does: "additional
reflection rounds raise recall while lowering confidence, thereby lessening
ROC."[^c12] Aggregating self-consistency samples by vote also helps, with
the vote "markedly increases recall on both datasets and improves
calibration, indicating stronger ROC mitigation and" broader coverage.[^c13]

The phenomenon is distinct from ordinary miscalibration in one respect the
paper stresses: the target is completeness of a set, not the correctness of
one answer. The authors argue that earlier work on confidence in LLMs judges it only
by the accuracy of one final answer.[^c18] ROC asks whether confidence
tracks coverage.

## Limits

- The benchmark has bounded solution spaces, which is what makes recall
  computable. The authors state the cost of the alternative: prior datasets
  "are either tightly constrained or nearly unbounded, which hinders
  reliable estimation of completeness."[^c14] Whether ROC appears in open-
  ended generation, where completeness has no ground truth, is not tested.
- Confidence is verbal. "In our setup, the model first generates a full
  answer and then reports its confidence" on a 0–100 scale.[^c15] ROC is a
  statement about that elicitation, not about internal probabilities.
- The Short-CoT and Long-CoT comparison is paradigm against model for two of
  the three families. Short-CoT is "Qwen3-8B (non-thinking mode) [37],
  DeepSeek-V3 [26], and gpt-4o-mini [1]"; the Long-CoT models are different
  models for DeepSeek (R1) and GPT (o4-mini).[^c16] Only the Qwen comparison
  holds the model fixed.
- The mitigation results (self-consistency voting, reflection checkpoints)
  are reported for "the Long-CoT Qwen3-8B model" in the self-consistency
  table.[^c17] They are not shown across families.
- The mechanism is a hypothesis, not a result. The attention-based support
  for it is preliminary; see [[cognitive-rigidity]].
- Transfer to asking (my inference, not the paper's): an answer list that
  arrives with high confidence gives the asker no sign of what is missing,
  so the asker faces the same stopping question the answerer does.

## Related

- [[calibration]] — ROC is calibration with recall in place of accuracy; the
  ECE machinery carries over, the target does not
- [[cognitive-rigidity]] — the hypothesised cause of the effect
- [[judge-coverage-overestimation]] — judges also credit surface completeness,
  the judge-side version of a confident incomplete set
- [[entropy-gated-forced-reconsideration]] — an appended reconsideration cue
  tested on single-answer math; the same kind of cue is applied here to
  enumeration
- [[thinking-mode-exploration-dissociation]] — thinking did not add
  exploration on bandit choice; the enumeration measure here differs
- [[unbudgetable-completeness]] — why a set's completeness can be costly to
  certify; ROC is a model's claim of completeness without that certificate

[^c1]: arxiv-2512-01725 — "when its reported confidence exceeds its observed performance"
[^c2]: arxiv-2512-01725 — "would blur the exploration shortfall we seek to isolate"
[^c3]: arxiv-2512-01725 — "spans ten complexity levels and the SubsetSum corpus seven, with 100 instances per level"
[^c4]: arxiv-2512-01725 — "Short-CoT produces expected calibration error (ECE) values above 78.22% for every model"
[^c5]: arxiv-2512-01725 — "Short-CoT results clustering in the low-recall, high-confidence corner (red)."
[^c6]: arxiv-2512-01725 — "seldom revising its initial reasoning path, which largely explains its inflated confidence"
[^c7]: arxiv-2512-01725 — "Long-CoT decreases the ECE by at least 18.28% across all model families"
[^c8]: arxiv-2512-01725 — "open-source models continue to exhibit pronounced ROC, exceeding"
[^c9]: arxiv-2512-01725 — "shows a strong negative correlation: extended chains yield lower confidence"
[^c10]: arxiv-2512-01725 — "Short-CoT, however, maintains high confidence while recall drops sharply, revealing persistent overconfidence."
[^c11]: arxiv-2512-01725 — "Decoding temperature increases token-level diversity rather than alleviating ROC or expanding solution"
[^c12]: arxiv-2512-01725 — "additional reflection rounds raise recall while lowering confidence, thereby lessening ROC"
[^c13]: arxiv-2512-01725 — "markedly increases recall on both datasets and improves calibration, indicating stronger ROC mitigation and"
[^c14]: arxiv-2512-01725 — "which hinders reliable estimation of completeness"
[^c15]: arxiv-2512-01725 — "In our setup, the model first generates a full answer and then reports its confidence"
[^c16]: arxiv-2512-01725 — "models, including Qwen3-8B (non-thinking mode) [37], DeepSeek-V3 [26], and gpt-4o-mini [1]"
[^c17]: arxiv-2512-01725 — "Performance of self-consistency strategies on the Long-CoT Qwen3-8B model, using n=32 parallel"
[^c18]: arxiv-2512-01725 — "still judge confidence only by the accuracy of a single final"
