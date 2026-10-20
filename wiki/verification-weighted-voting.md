---
description: "Replacing a plain majority vote with one where tool-verified answers carry weight ω>1 breaks the self-consensus loop that rewards frequent-but-wrong answers; a soft weight beats hard filtering."
aliases: ["T3 RL", "verification-aware voting", "false-popular mode collapse", "tool-verified majority vote"]
sources: ["arxiv-2603-02203", "arxiv-2512-15146"]
---
# Verification-weighted voting

Self-consensus (majority vote over sampled answers) treats frequency as truth. Test-time reinforcement learning (TTRL) uses the majority answer as a pseudo-label and rewards rollouts that agree with it. The paper names the failure: "voting selects popularity rather than truth: incorrect rollouts receive positive reward, correct minority rollouts are suppressed, and test-time RL amplifies the error."[^c1] It calls this false-popular mode collapse.

## Mechanism

The loop is closed: "the model generates candidates, votes on them, and learns from its own vote."[^c2] Once the pseudo-label is a wrong answer, the update raises the chance of sampling it, which raises its vote share, which makes the label more confidently wrong.[^c3] The paper reports that the share of questions with a wrong unverified majority rises sharply with difficulty.[^c4]

The remedy is evidence from outside the model's own distribution. A verifier LLM turns each rollout's reasoning into a small Python program, a code interpreter runs it, and the verifier flags the rollout valid if the tool output equals the rollout's extracted answer.[^c5] Each rollout then gets vote weight w_i = (1 − v_i)·1 + v_i·ω with ω ≥ 1, and the pseudo-label is the answer with the largest total weighted mass.[^c6] The reward stays label-free, but is grounded in tool feedback. In the paper's framing the model asks not only which answer is most frequent but which answers can be verified.[^c7]

## Soft weight, not a filter

ω=1 is plain TTRL; ω→∞ is hard filtering of unverified rollouts. Finite ω>1 improved AIME accuracy on all three backbones tested, with the largest gain for Qwen-2.5-Math-1.5B at ω=5 (AIME +31.6%), and hard filtering was less reliable.[^c8] The stated reason is that the verifier is itself noisy: rollout-to-code translation is stochastic, and verifier accuracy with a Coder-1.5B verifier was only 73.2%, so hard filtering can propagate false positives and discard true positives.[^c9] The weight is a heuristic: the authors say they cannot compute the exact probability of correctness of a verified rollout.[^c10]

A second source of vote weight, with no checker at all, is the model's own confidence: [[step-confidence-weighted-consensus]] weights each response by its average step confidence and, like this note, replaces counting with a weighted sum.[^c11] The two rest on different evidence and were not run on the same tasks, so neither is shown to beat the other.

## Limits

- Tested on math (MATH-500, AMC, AIME 2024) with executable checks; the claim that it extends to other verifiable domains is asserted, not what was measured in the sections read.
- The verifier shares the model family's blind spots in how it writes the check; a rollout and its check can be wrong together. Verifier precision was as low as 25% in one reported configuration (Table 3, as extracted), so the weight corrects only partly.
- ω is a fixed hyperparameter, not derived. My inference: when no tool can check the answer type (open-ended questions), the mechanism has nothing to weigh and reduces to plain majority voting.
- Gains are reported against TTRL, not against a labelled-data upper bound.

## Related

- [[surprisingly-popular-algorithm]] — another rule for escaping a wrong majority, using predicted votes instead of external tools
- [[self-consistency-difficulty-score]] — also uses agreement among samples as a label-free signal
- [[black-box-correctness-ceiling]] — limits of agreement-based correctness signals
- [[verification-aware-stopping]] — verification evidence used as a decision input

[^c1]: arxiv-2603-02203 — "voting selects popularity rather than truth: incorrect rollouts receive positive reward, correct minority rollouts are suppressed, and test-time RL"
[^c2]: arxiv-2603-02203 — "the model generates candidates,"
[^c3]: arxiv-2603-02203 — "The RL update increases the likelihood"
[^c4]: arxiv-2603-02203 — "share rises sharply with difficulty."
[^c5]: arxiv-2603-02203 — "vi = 1[ti = âi ] ."
[^c6]: arxiv-2603-02203 — "wi = (1 − vi ) · 1 + vi · ω,"
[^c7]: arxiv-2603-02203 — "the model should not only ask which answer is most frequent, but which answers can be verified."
[^c8]: arxiv-2603-02203 — "hard filtering is less reliable."
[^c9]: arxiv-2603-02203 — "so hard filtering"
[^c10]: arxiv-2603-02203 — "we cannot"
[^c11]: arxiv-2512-15146 — "Unlike naive majority voting, our method"
