---
description: "Selection bias in discrete-choice answering is a permutation-invariance failure; RL that scores a response against all option orderings of the same item, plus a consistency reward, reduces it."
aliases: ["PA-GRPO", "permutation-aware GRPO", "permutation-blindness", "cross-permutation advantage"]
sources: ["arxiv-2603-21016"]
---
# Permutation-consistency training

Selection bias is the answering-side counterpart of [[mcq-answer-position-bias]]: a model choosing among options flips its decision when only labels or positions change. The work defines it as the violation of permutation invariance: for any non-semantic permutation, the mapped semantic choice should remain the same, and bias shows up as "systematic preference flips triggered by label or position changes".[^c1] It is the same family of artifact as the position effects catalogued in [[llm-judge-biases]].

## Mechanism

**Permutation-blindness.** Standard GRPO scores each prompt variant on its own. A policy can then earn high reward under a "favorable" ordering and do poorly under another (for example reversed), and nothing penalizes the inconsistency. The authors name this failure permutation-blindness.[^c2]

**Permutation group.** Each item is expanded into P reordered prompts, with N sampled responses each. For four-option MCQ the set is the four cyclic shifts plus the reverse order (P = 5), so every option appears in every position; for pairwise judging it is both orders (P = 2).[^c3]

**Cross-permutation advantage.** The P x N samples are treated as one comparison set. Each sample's advantage is its reward minus the group mean, divided by the group standard deviation, and set to zero when that deviation is below a threshold. A sample is therefore reinforced only if it beats the item's average across orderings.[^c4]

**Consistency-aware reward.** Responses are first mapped from surface letters back to the original semantic option. For judging, a pair of index-aligned samples gets +1 if they pick the same semantic candidate and -1 otherwise. For MCQ, a response gets +1 only if the group has a unique modal choice and the response equals it; ties are penalized as fragmentation. The total reward is the correctness, length and format terms plus lambda times the consistency term.[^c5]

## What was measured

On Llama-3.1-8B-Instruct, adding the consistency reward alone raised MT-Bench consistency from 80.6% to 83.1% without losing correctness. The group advantage alone improved JudgeBench accuracy from 48.2% to 49.3%. The two together gave the strongest robustness, for example PreferenceBench consistent accuracy rising from 76.3% to 79.8%.[^c6] Lambda = 1.0 was chosen over 0.5 and 2.0. P = 5 beat P = 4, which the authors attribute to the reverse order breaking adjacency bias. The full P = 24 set raised TinyMMLU consistent accuracy from 75.0% to 77.0% at nearly five times the compute.[^c7] The gain also appears under direct decoding with no chain of thought: MT-Bench consistent accuracy was 69.3% for PA-GRPO (Direct) against 58.0% for Base (CoT). The authors read this as the invariance being internalized in the policy.[^c8]

Label and position were also perturbed separately. On PreferenceBench, consistency was 87.2% under the coupled protocol used in training but 62.8% under label-only and 66.9% under order-only perturbation. Residual bias is therefore dataset-dependent and partly untrained.[^c9]

## Limits

The method needs discrete-choice tasks where a permutation group is well defined. The authors say that extending it to open-ended generation is hard because semantic equivalence is hard to quantify there.[^c10] Evaluation is English-only and on open-weight models. Interaction with other artifacts such as verbosity bias is untested.[^c10] Training is on coupled label-plus-position permutations, and the isolated-factor results show gaps remain. Some benchmarks lost a little accuracy. The ablation gains are a point or a few points from single reported runs, with no variance reported in the passages I read. That the cause is "failure to maintain consistency" rather than a stored prior is the authors' framing, not something they tested mechanistically. The cost scales with P, so the uniform-position-coverage design is a compute trade-off rather than a proof of sufficiency.

## Related

- [[mcq-answer-position-bias]] — position skew when a model writes the item rather than answers it
- [[llm-judge-biases]] — position and label effects in pairwise judging, the setting this trains against
- [[pseudo-ensemble]] — aggregating over perturbed views of one input, here used as a training signal instead

[^c1]: arxiv-2603-21016 — "Selection bias is defined as the violation of this"
[^c2]: arxiv-2603-21016 — "permutation-blindness."
[^c3]: arxiv-2603-21016 — "The four cyclic shifts ensure strictly uniform cov-"
[^c4]: arxiv-2603-21016 — "avoid amplifying noise."
[^c5]: arxiv-2603-21016 — "explicitly penalize fragmentation (including ties):"
[^c6]: arxiv-2603-21016 — "Adding rcon to GRPO explicitly encourages within-group agreement, effectively raising"
[^c7]: arxiv-2603-21016 — "marginal gain does not justify the nearly"
[^c8]: arxiv-2603-21016 — "indicating that permutation-aware"
[^c9]: arxiv-2603-21016 — "On PreferenceBench, the standard coupled protocol yields"
[^c10]: arxiv-2603-21016 — "First, our method is primarily tailored for discretechoice tasks (e.g., MCQ and pairwise judgments)"
