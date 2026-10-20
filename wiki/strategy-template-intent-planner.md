---
description: "A two-stage plug-in planner picks a response strategy (when to question), then a Socratic template (how), and conditions a generator; it raised questioning but not in domain-tuned models."
aliases: ["Socratic Inquiry Framework", "SIF", "Lightweight Plug-and-play Planner", "strategy anchoring and template retrieval"]
sources: ["arxiv-2602-01598"]
---
# Strategy-template intent planner

A response generator can be steered toward asking by putting a small classifier in front of it. The Socratic Inquiry Framework (SIF) does this for cognitive-behavioural counselling. A Lightweight Plug-and-play Planner (LPP) reads the dialogue context and emits a pair (strategy, template). A separate LoRA-tuned generator then conditions on that pair plus the dialogue history.[^c1]

## Mechanism

**Stage 1, Strategy Anchoring.** An instruct-tuned encoder reads the left-truncated context and the latest seeker utterance. A linear layer and softmax then choose one of ten supportive strategies, such as question, reflection of feelings, information or providing suggestions. This label fixes the turn's role, so that "a turn labeled question indeed initiates an inquiry rather than offering reassurance."[^c2] Choosing the strategy is the "when to ask" decision.

**Stage 2, Template Retrieval.** A second encoder gives a 6-way classification over Socratic methods: definition, counter-questioning, maieutics, dialectics, counterfactual reasoning and other. This fixes "how to formulate the question." It is conditioned on the strategy only implicitly, through the alignment of its training data.[^c3]

**Generation.** The planning pair is concatenated in front of the history, so that "high-level intent is injected before the generative process begins, rather than emerging stochastically from language modeling alone."[^c4] The generator never needs end-to-end retraining. The planner is trained on strategy annotations from a counselling corpus. The generator is trained on Socratic-QA, a filtered set of strategy-aligned question sequences, generated under three criteria: openness, emotional resonance and non-directiveness.[^c5]

## What was measured

- Adding the planner to zero-shot large LLMs raised ROUGE by 0.12 to 0.13 for DeepSeek R1 and V3 in single-turn mode, nearly doubling their baselines.[^c6]
- Proactive Questioning Ability (PQA) rose by 0.46 in single-turn mode for the full SIF system. For Qwen2-7B it rose by 0.87 in multi-turn mode.[^c7]
- Ablation (Table 3, multi-turn, human ratings plus PQA): removing Socratic-QA hurt most (Professionalism 2.40 and PQA 0.85, against 2.79 and 0.97 for the full model). Removing Strategy Anchoring mainly hurt coherence, and removing Template Retrieval had the smallest effect (PQA 0.95).[^c8] The authors read the strategy label as a global constraint on long generation and the template as priming of domain terminology. Those are their interpretations, not tested mechanisms.

## Limits

- Models already specialised for counselling gained little or got worse. The authors attribute this to a conflict between the planner's signal and the model's internal priors; for example, one specialised model's distinct rate dropped by 0.04.[^c9] The conflict is their explanation and was not isolated experimentally.
- The ablation differences are small (PQA 0.94, 0.95 and 0.97), and no variance or significance is reported in the slices read. The largest effect belongs to the data, not the planner stages. My inference is that the "decoupling" claim is therefore only partly separated from the effect of training data.
- Training data was mainly Chinese counselling dialogue, so generality across languages and cultures is untested. The human raters were nine mental-health students and professionals, and they were blinded to whether the planner was present. The case study is a single dialogue.
- PQA measures how often a response initiates directive questions. It does not measure whether those questions helped the client.

## Related

- [[socratic-method]] — the questioning tradition whose categories the template stage encodes.
- [[clarifying-interaction-decomposition]] — the same when/what split, applied to clarification instead of therapy.
- [[intent-based-strategy-selection]] — a fixed-priority intent-to-strategy rule, in contrast to a learned classifier.
- [[think-plan-ask]] — another plan-then-ask architecture.
- [[intent-aware-response-strategy]] — a neighbouring way to condition responses on intent.

[^c1]: arxiv-2602-01598 — "a lightweight, plugand-play therapeutic intent planner that transforms LLMs from passive listeners into active cognitive guides."
[^c2]: arxiv-2602-01598 — "ensuring that a turn labeled question indeed initiates an inquiry rather than offering reassurance."
[^c3]: arxiv-2602-01598 — "While SA decides what kind of support to provide, TR speciﬁes how to formulate the question"
[^c4]: arxiv-2602-01598 — "This design ensures that high-level intent is injected before the generative process begins, rather than emerging stochastically from language modeling alone."
[^c5]: arxiv-2602-01598 — "(1) Openness, to encourage elaboration rather than yes/no"
[^c6]: arxiv-2602-01598 — "Deepseek R1 and Deepseek V3 achieve Rouge improvements of 0.12, 0.13 respectively, nearly doubling their baseline scores."
[^c7]: arxiv-2602-01598 — "0.46 in single-turn settings for SIF"
[^c8]: arxiv-2602-01598 — "Table 3 reveals that removing Socratic QA induces the most severe performance degradation"
[^c9]: arxiv-2602-01598 — "When external planning constraints conﬂict with internal priors, performance may stagnate or degrade."
