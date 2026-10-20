---
description: "Content-free responses (a colon, 'Thought process:') are accepted as correct by reference-based LLM judges, up to 90% false positives; training on truncated openers as negatives removes it."
aliases: ["master key attacks", "reasoning-opener reward hacking", "superficial-input false positives in LLM judges"]
sources: ["doi-10-48550-arxiv-2507-08794"]
---
# Judge master-key false positives

A generative judge that compares a response with a reference answer can be made to say "correct" by a response that contains no answer at all. The work calls such inputs "master keys". Two families were tested: non-word symbols (a single blank space, ".", ",", ":") and reasoning openers ("Thought process:", "Let's solve this problem step by step.", "Solution", and the same word in Chinese, Japanese and Spanish).[^c1] The failure first appeared in an RLVR run that collapsed: the policy degenerated into short openers that the Qwen2.5-72B-Instruct judge rewarded, with response length dropping below 30 tokens.[^c2] So the judge's leniency became the policy's optimum.

## How large and how widespread

General-purpose judges were hit hardest. Punctuation alone induced up to 35% false positives in GPT-4o; "Thought process:" gave 60-90% in LLaMA3-70B-Instruct and Qwen2.5-72B-Instruct across benchmarks; multilingual tokens such as "解" also triggered it.[^c3] Specialised verifiers were better but not immune: General Verifier showed 66.8% on MATH with a single blank space.[^c4] The abstract states that GPT-o1 and Claude-4 are affected as well.[^c5]

## Scale is non-monotonic

Across Qwen2.5-Instruct from 0.5B to 72B the false-positive rate was lowest at 0.5B (which also agreed least with GPT-4o), rose sharply at 1.5-3B, was best balanced at 7-14B, and climbed again at 32B and 72B.[^c6] The authors leave the mechanism open. A bigger judge is therefore not a safer one.

Unseen keys also work: text whose embedding is close to a known master key, such as "mental process", triggered high rates.[^c7]

## The fix: truncated openers as negatives

Take 20k questions from the 160k training set, regenerate chain-of-thought responses, keep only the first sentence (typically an opener such as "To solve the problem, we need to find the sets A and B..."), label it NO, and add these to the original data for supervised fine-tuning of Qwen2.5-7B and 32B judges (Master-RM).[^c8] Keys were de-duplicated against the test keys, so the test measures generalisation. The resulting judges reached near-zero false positives on all keys and five benchmarks.[^c9] The training negatives are a plain fraction of the data, not a new objective.

## Inference-time tricks are not a defence

Chain-of-thought plus majority vote (5 samples) lowered false positives on general reasoning for most models but raised them on maths for Qwen models, and did the opposite for LLaMA. The authors conclude effectiveness is "highly model- and domain-dependent".[^c10]

## Limits

- Only reference-based, binary YES/NO judging was studied; pairwise or rubric judging (see [[llm-judge-biases]]) was not.
- The keys are lead-in openers; reflection, self-verification or backtracking cues at the end of a reasoning chain were left to future work.[^c11]
- Robustness was shown against the tested keys and nearby ones; an adaptive attacker who searches against Master-RM was not tested (my inference: the gap remains open).
- The non-monotonic scale trend covers one model family; its explanation is only a preliminary hypothesis.
- The training negatives are first sentences of one generator (GPT-4o-mini); other openers' coverage is unmeasured. Whether accuracy on genuine answers is fully preserved rests on the paper's agreement and VerifyBench checks, which I did not read in detail.

## Related

- [[llm-judge-biases]] — the same judges' surface-feature sensitivities in pairwise grading (position, length)
- [[judge-then-solve]] — judging against a solved answer, another way to avoid being fooled by form
- [[cross-provider-judge-ensemble]] — ensembling judges; here all general judges failed, so diversity alone may not help (my inference)
- [[correct-answer-trap]] — a related case of rewards that miss what the answer lacks

[^c1]: doi-10-48550-arxiv-2507-08794 — "Reasoning Openers: “Thought process:”, “Let’s solve this problem step by step.”, “Solution” and its multilingual counterparts"
[^c2]: doi-10-48550-arxiv-2507-08794 — "the response length drops sharply to fewer"
[^c3]: doi-10-48550-arxiv-2507-08794 — "leads to FPRs as high as 60 − 90% in advanced open LLMs such as LLaMA3-70B-Instruct and"
[^c4]: doi-10-48550-arxiv-2507-08794 — "shows an alarming FPR of 66.8% on the MATH dataset"
[^c5]: doi-10-48550-arxiv-2507-08794 — "including leading proprietary systems such as GPT-o1 and Claude-4."
[^c6]: doi-10-48550-arxiv-2507-08794 — "exhibit a non-monotonic trend"
[^c7]: doi-10-48550-arxiv-2507-08794 — "can trigger high false positive rates"
[^c8]: doi-10-48550-arxiv-2507-08794 — "we retain only the first sentence, which typically consists of a reasoning opener"
[^c9]: doi-10-48550-arxiv-2507-08794 — "they achieve near-zero (if not"
[^c10]: doi-10-48550-arxiv-2507-08794 — "highly model- and domain-dependent"
[^c11]: doi-10-48550-arxiv-2507-08794 — "We encourage future work"
