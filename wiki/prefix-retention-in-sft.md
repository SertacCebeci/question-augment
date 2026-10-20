---
description: "Keeping short framing sentences at the start of SFT targets, instead of cleaning them out, improved safety and math accuracy in distilled R1 models but not coding or factuality."
aliases: ["prefix-conditioned SFT", "prefix retention", "boilerplate retention", "prefix inclusion ratio"]
sources: ["arxiv-2601-01624"]
---
# Prefix retention in SFT

Most alignment and domain fine-tuning pipelines clean their data first. Introductory boilerplate is removed on the view that it adds style without substance.[^c1] Prefix retention reverses that default: a short framing sentence is kept at the start of each training response, and the share of examples that keep it is the variable being set. The proposed mechanism is that such a sentence acts as a lightweight alignment signal that can guide decoding toward safer and more coherent responses.[^c2]

The design isolates the prefix. Three distilled R1 models (1.5B, 7B, 8B) are fine-tuned with LoRA on targets that were rewritten to a step-by-step format.[^c3] During rewriting the model "is instructed not to include any prefatory boilerplate".[^c4] Each training example then receives a prefix independently with probability α, drawn uniformly from a fixed set of five templates for its capability, with α in {0, 0.25, 0.5, 1.0}.[^c5] Each α is a separate fine-tuning run, and the authors state that prefix prevalence is the only controlled variable across runs.[^c6]

**What was measured.** On safety, prefix conditioning gave consistent gains on Safe@1 for adversarial benchmarks, "with the most pronounced effects on WildJailbreak and StrongReject," up to six points.[^c7] On GSM8K the 7B model moved from 87.67 at α = 0 to 89.00 at 0.25 and 88.00 at 1.0 (Table 3). The authors describe the curve as an inverted V: "GSM8K accuracy peaks at intermediate prefix ratios, forming an".[^c8] Coding and factuality showed marginal or negative effects. The authors attribute the split to task structure: "This divergence arises from differences in task structure."[^c9] Their reading is that safety and math benefit from early framing, while exact-output coding and recall of specific facts are hurt by it.

**The mechanism as proposed.** The paper hypothesizes that prefix tokens are early in the response and semantically loaded, so they are hard to predict and carry higher training loss. Under cross-entropy that would produce larger updates, "allowing a small number of prefix tokens to disproportionately influence model updates".[^c10] The authors also frame the prefix as a policy reminder that narrows the search space before reinforcement learning, so that RL can "rely on simpler reward models for refinement."[^c11] The loss side of this argument is a separate measurement, described in [[framing-token-loss-concentration]]. What survives transfer to other settings is the lever: the first tokens of a training target shape what the model learns to open with. What does not clearly transfer is the magnitude, which was measured on LoRA fine-tuning of small distilled models, not on prompting a deployed model. That last point is my inference.

## Limits

- **Scale.** The authors say "the results may not directly generalize to larger" frontier models or to models trained with full reinforcement learning.[^c12] Among their own models the 1.5B variant was "brittle", with fluctuations on factual and coding benchmarks.[^c13] They read this as smaller models overfitting the prefix as literal content, which is an interpretation, not a probed mechanism.
- **Small math effects.** On GSM8K the 7B differences are about one point against the 0% baseline. The text reports no seed count and no run-to-run variance (my reading; neither term appears), so these gaps are not established as beyond noise.
- **Non-monotone.** The effect is not "more prefix is better". The 100% setting was sometimes below the 25% or 50% settings, so the claim is about a peak, not a direction.
- **Judges.** Safety was scored by GPT-4.1 or by Llama-Guard-3-8B, and "they encode implicit policy assumptions and may" not reflect every deployment's norms.[^c14]
- **Normative content.** The prefixes themselves carry a judgment. "Prefix scaffolds and safety-oriented cues reflect implicit" views of appropriate behaviour, which the authors say may not generalize across contexts.[^c15]
- **One rewriter.** All targets were produced by one model, and "inherent to GPT-4.1 may be reflected in the finetuned models, potentially limiting diversity in reasoning styles."[^c16]
- **Evidence base.** One paper, one set of five templates per capability, and three model sizes of one family. Whether the same split holds for other templates or for prefixes the model generates itself is untested here.

## Related

- [[framing-token-loss-concentration]] — the per-token loss measurement the paper uses to explain why a few prefix tokens matter
- [[lexical-concealment-versus-trajectory-anchoring]] — another visible framing that steers a generated trace, measured by an entropy gap rather than by training loss
- [[non-predictive-cue-training]] — a cue a model learns to lean on through its training signal; here the cue is kept in the data on purpose, and the question is which way it pushes

[^c1]: arxiv-2601-01624 — "Recent alignment studies commonly remove introductory boilerplate phrases from supervised"
[^c2]: arxiv-2601-01624 — "serve as lightweight alignment signals that can"
[^c3]: arxiv-2601-01624 — "We experiment with three unaligned distilled reasoning models from DeepSeek-AI (2025)."
[^c4]: arxiv-2601-01624 — "is instructed not to include any prefatory boilerplate"
[^c5]: arxiv-2601-01624 — "independently with probability α."
[^c6]: arxiv-2601-01624 — "(iii) prefix prevalence is the only controlled variable across runs."
[^c7]: arxiv-2601-01624 — "with the most pronounced effects on WildJailbreak and StrongReject."
[^c8]: arxiv-2601-01624 — "GSM8K accuracy peaks at intermediate prefix ratios, forming an"
[^c9]: arxiv-2601-01624 — "This divergence arises from differences in task structure"
[^c10]: arxiv-2601-01624 — "allowing a small number of prefix tokens to disproportionately influence model updates"
[^c11]: arxiv-2601-01624 — "to rely on simpler reward models for refinement."
[^c12]: arxiv-2601-01624 — "the results may not directly generalize to larger"
[^c13]: arxiv-2601-01624 — "R1-1.5B exhibited brittle behavior, showing fluctuations in factual and coding benchmarks."
[^c14]: arxiv-2601-01624 — "they encode implicit policy assumptions and may"
[^c15]: arxiv-2601-01624 — "Prefix scaffolds and safety-oriented cues reflect implicit"
[^c16]: arxiv-2601-01624 — "inherent to GPT-4.1 may be reflected in the finetuned models, potentially limiting diversity in reasoning styles."
