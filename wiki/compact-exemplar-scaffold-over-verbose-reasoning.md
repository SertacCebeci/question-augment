---
description: "In moral-judgment prompting, short exemplar-guided or lightly structured scaffolds beat long multi-stage reasoning on accuracy, calibration, robustness and token cost."
aliases: ["compact scaffold advantage", "verbosity penalty in moral prompting"]
sources: ["arxiv-2602-13274", "arxiv-2512-22966"]
---
# Compact exemplar scaffold over verbose reasoning

ProMoral-Bench compared 11 prompting paradigms across four model families (GPT-4.1, Claude Sonnet-4, Gemini 2.5 Pro, DeepSeek-3.1) on ETHICS, Scruples, WildJailbreak and a minimal-edit robustness set, ETHICS-Contrast. The headline finding is that the best strategies are compact: few-shot, few-shot with a brief rationale, or a short plan-and-solve step.[^c1]

On ETHICS the same compact runs also had the best calibration. GPT-4.1 with Plan-and-Solve reached 0.960 accuracy with ECE 0.031 at about 642 tokens per example. Verbose pipelines (Thought Experiment, Self-Correct) used thousands of tokens, up to about 13k, and were worse in both accuracy and calibration.[^c2] The authors' reading is that light structure improves "probability quality per token", and that the consistent loser is verbosity.[^c3]

Robustness points the same way. Under minimal edits to the dilemmas, compact structure minimized degradation while verbose introspection was brittle.[^c4]

Models differ in what they need. Claude gains from exemplars, and its generic zero-shot "think step-by-step" slightly trailed plain zero-shot. Gemini needs demonstrations most. GPT-4.1 relies less on exemplars because a role persona already regularizes it.[^c5] For a questioner or answerer, the mechanism is that a short demonstration fixes the label criteria, while extra self-generated reasoning adds noise and cost. This is my inference from the pattern, not something the paper tested.

The paper's summary score, UMSS, is the harmonic mean of min-max normalized moral competence and safety robustness, so a strategy cannot score well by excelling at only one.[^c6]

A clinical benchmark gives a less uniform picture for a heavier package. MedPrompt, which stacks self-generated chain-of-thought, few-shot exemplars and an answer-shuffling ensemble, was tested on sequential clinical decisions for three LLMs. The authors conclude it "does not universally improve model performance," and it lowered one model's differential-diagnosis accuracy sharply.[^c7][^c8] Their account is that long, multi-example prompts consume context and pull attention toward example-consistent patterns. That is a conjecture they did not resolve. For this note the lesson is that the compact-scaffold advantage is a measured ranking in its own tasks; it may not hold wherever structure is added, and the gain depends on the task (see [[task-conditional-prompt-gain]]).

## Limits

- Tasks are short moral classification and jailbreak refusal. Whether the pattern holds for open-ended or multi-hop questions is untested.
- Min-max normalization is across the compared model-strategy pairs, so UMSS values are relative to this set and not absolute.
- The causal account (exemplars fix criteria, extra steps add noise) is my inference. Only the rankings were measured.
- Four model families were used, with no variation in exemplar choice or count reported in the slices I read.

## Related

- [[llm-red-teaming]] — jailbreak resistance is one of the benchmark's axes
- [[principle-guided-critique-revision]] — a multi-stage revision scheme of the kind this benchmark found fragile
- [[explanation-guided-demonstration-elicitation]] — exemplars and demonstrations as the lever

[^c1]: arxiv-2602-13274 — "compact, exemplar-guided scaffolds outperform complex multi-stage reasoning, providing"
[^c2]: arxiv-2602-13274 — "edges out Few-Shot-CoT at 0.960/0.958 (Table 1),"
[^c3]: arxiv-2602-13274 — "Across models, the consistent loser is verbosity: more steps"
[^c4]: arxiv-2602-13274 — "is that compact structure minimizes degradation,"
[^c5]: arxiv-2602-13274 — "Gemini needs demonstrations most, moving from weak zero-shot to competitive accuracy with exemplars plus brief CoT;"
[^c6]: arxiv-2602-13274 — "of a Moral Competence Score (MCS) and a Safety"
[^c7]: arxiv-2512-22966 — "it does not universally improve model performance"
[^c8]: arxiv-2512-22966 — "led to a sharp decline in ChatGPT 4o"
