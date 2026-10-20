---
description: "Annotators and LLM judges fail to notice swapped preference labels; reward models tolerate substantial label corruption in accuracy terms while Best-of-N gain vanishes at 50%."
aliases: ["choice blindness in RLHF", "preference injection", "label-corruption insensitivity"]
sources: ["arxiv-2603-08412"]
---
# Choice blindness in preference labels

Choice blindness is the finding that people (and some models) accept a surreptitiously swapped choice as their own and justify it. Wu (2026) transfers it to pairwise preference annotation for RLHF and follows the corrupted signal through three stages.

## Human annotators

In a Prolific study (N=50, 200 swap trials) a justification page showed the response the participant had not chosen, under the heading "You selected this response as the better one". Only 9.0% of swaps were noticed.[^c1] Awareness and behaviour dissociated: participants who later described the swap still failed to detect most swaps, and nine of them had zero detections.[^c2] Participants also agreed with existing HH-RLHF labels at only 56.1%, below the dataset's own researcher agreement, so labels may already be unstable.[^c3]

## LLM judges

Fifteen models were tested in two turns: the model picks a response, then is told calmly that it picked the other one (calm misattribution), or is correctly told its choice under explicit pressure (sycophancy). Nine models almost always caught the misattribution, which the author reads as retrieval from context rather than self-monitoring; six accepted it 4.1% to 33.0% of the time. Models that corrected calm misattribution abandoned their preferences under minimal social pressure (median acceptance 91.4%).[^c4] When the first-turn reasoning was removed so the context held only a bare label, blindness rose significantly in four models (DeepSeek-R1 from 1.5% to 51.7%).[^c5] Susceptibility was higher when the model's original preference was weak, and these close-call pairs are the ones that disproportionately drive the reward model's learning signal.[^c6]

## Reward models and policy

Bradley-Terry reward models were trained on HH-RLHF with chosen/rejected labels randomly swapped from 0% to 50%, on a 86M encoder and a 2B decoder. Pairwise accuracy stayed above 61% up to 30% corruption for the encoder, falling to chance only at 50%, while the reward margin decayed steadily.[^c7] One-sixth to one-third of labels had to be corrupted to halve the reward margin (ED50 16.3% and 32.6%).[^c8] In Best-of-N selection scored by a clean reward model, the gain at 50% swap was effectively zero, i.e. random sampling, although every corrupted proxy still reported scores rising with N.[^c9]

The author's term for the whole pattern is a preference construction problem: the label depends on elicitation context in ways that neither annotators, LLM self-monitoring nor accuracy metrics reveal. (Reading: this is the label-side counterpart of preferences being constructed by dialog, see [[preference-construction]]; that link is my inference, not the paper's claim.)

## Limits

The human result is one platform, a single task type, and short unfamiliar text; some non-detections may be covert awareness, which the paper judges immaterial to the pipeline. The LLM detection result depends on the whole earlier turn staying in context, so it measures retrieval, and a two-turn design is not how production judges are used. Random label swaps are a stand-in for the structured noise real annotators produce. Best-of-N is a simplified proxy for PPO or DPO; the paper cites a proof that corruption weakens GRPO's signal but ran no RL loop. HH-RLHF already carries baseline noise (roughly 10 to 15% by the paper's estimate), so ED50 is relative to total noise. Only two architectures and one dataset were used.[^c10]

## Related

- [[preference-construction]] — preferences as built by the interaction rather than retrieved; same assumption challenged.

[^c1]: arxiv-2603-08412 — "Only 9.0% of swap trials were detected (91.0%"
[^c2]: arxiv-2603-08412 — "demonstrating that metacognitive awareness and"
[^c3]: arxiv-2603-08412 — "participants agreed with"
[^c4]: arxiv-2603-08412 — "Models that reliably corrected calm"
[^c5]: arxiv-2603-08412 — "reasoning significantly increased blindness in four"
[^c6]: arxiv-2603-08412 — "models are more likely"
[^c7]: arxiv-2603-08412 — "pairwise accuracy remains above 61% up to 30%"
[^c8]: arxiv-2603-08412 — "must be corrupted to halve the reward signal."
[^c9]: arxiv-2603-08412 — "at 50% swap, the gold score"
[^c10]: arxiv-2603-08412 — "No full RL loop."
