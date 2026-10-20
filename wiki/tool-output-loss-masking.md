---
description: "Tokens an interpreter writes into the context stay as conditioning but drop out of the loss, so training shapes the model's code and reasoning rather than its memory of returned outputs."
aliases: ["selective feedback masking", "interpreter-token masking", "environment-token loss masking", "tool-output masking"]
sources: ["arxiv-2512-20745", "arxiv-2512-08511"]
---
# Tool-output loss masking

When a training trace mixes model-written text with text an environment returns, the loss can be taken over every token or only over the model's own. The AgentMath paper takes the second option in both of its training stages. In supervised fine-tuning, a masking function is introduced "to identify tokens originating from" the interpreter segments, and those tokens are removed from the negative log-likelihood. The stated effect is that "gradient updates originate exclusively from model-generated reasoning and code." The reason given is "avoiding memorization of deterministic interpreter outputs."[^m1]

In reinforcement learning the split is applied to the advantage: "the advantage signal is applied exclusively to tokens within" the think and code segments, and environment-generated tokens are masked out.[^m2]

A self-calling agent applies the same split to a different kind of returned text. Its subagents are the same model answering atomic subtasks, and the policy update leaves out "the textual outputs returned by subagents." The stated reason is not memorization but "to avoid reward leakage": the paper's concern is that the trajectory should not be credited for content a subagent produced.[^m6] See [[self-calling-subagents]]. Whether a reward can leak through returned text that the policy never generated is the paper's claim; the text read gives no ablation that removes the mask.

The mechanism is that the masked tokens are still in the context the model conditions on when it produces the next token. Only the gradient is withheld. So the model can read an error message or a computed value and learn to act on it, without being trained to reproduce that message. The paper's phrase for this is "treating external feedback as non-trainable contextual information."[^m3]

What was measured. The masking appears in the paper's cumulative ablation as the final row, "SFT with selective feedback masking." Before this row the self-correction stage had brought performance to 58.6% on AIME24 and 50.8% on AIME25.[^m5] Adding "fine-tuning using selective feedback masking guided by code execution results" gives 60.5% on AIME24 and 53.3% on AIME25.[^m4] That is the only number for masking in the slices read.

## Limits

The masking number is not isolated. It is the last step of a table in which each row adds a change to the one before, so the 58.6 to 60.5 gain is the masking step together with whatever else changed in that row. No run that differs only in masking appears in the text read.

The RL-side masking is described as a design choice; the slices read contain no ablation for it. Only the supervised side has a number.

The memorization rationale is the authors' and is not tested. It holds most cleanly when the environment's output is deterministic and correct, as with an arithmetic interpreter. When the environment is noisy, partly wrong, or differently phrased at test time, excluding its tokens from the gradient would not, by itself, teach the model how to handle that noise. That point is my inference, not a result of the paper.

The mask stops the model from learning the environment's tokens; it does not stop the model from learning the pattern of what follows an error. The paper's error-correction traces are trained through their model-written parts, so the masked and unmasked signals are not separated in the text.

The same kept-in-context, dropped-from-loss pattern appears for wrong reasoning stages in [[stage-level-hallucination-loss-masking]], but the reason there is that false content should not be reinforced, not that deterministic outputs should not be memorized. The two rationales do not transfer into each other.

## Related

- [[tool-integrated-reasoning]] — the trace structure whose interpreter segments are masked here.
- [[groundedness-gated-tool-routing]] — a tool-using agent trained with loss on decision tokens only and none on tool-returned evidence; the same split, with the reason stated as learning which action to take rather than memorizing retrieved content.
- [[stage-level-hallucination-loss-masking]] — the same pattern for flagged wrong stages, kept in context and removed from the loss, for a different reason.
- [[self-calling-subagents]] — masks the text returned by weight-sharing subagents in GRPO, with reward leakage as the stated reason.

[^m1]: arxiv-2512-20745 — "avoiding memorization of deterministic interpreter outputs"
[^m2]: arxiv-2512-20745 — "the advantage signal is applied exclusively to tokens within"
[^m3]: arxiv-2512-20745 — "treating external feedback as non-trainable contextual information"
[^m4]: arxiv-2512-20745 — "fine-tuning using selective feedback masking guided by code execution results"
[^m5]: arxiv-2512-20745 — "performance substantially improved to 58.6% on AIME24"
[^m6]: arxiv-2512-08511 — "while masking out the textual outputs returned by subagents to avoid reward leakage"
