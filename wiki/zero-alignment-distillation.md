---
description: "Distilling from a teacher's visible outputs alone transfers what those outputs show, not the refusals they omit: in medical LLMs, utility copies over while safety does not."
aliases: ["benign-only distillation", "zero-alignment supervision", "black-box behavioral cloning", "functional imitation", "alignment collapse under distillation"]
sources: ["arxiv-2512-09403", "arxiv-2602-11157"]
---
# Zero-alignment distillation

Black-box distillation turns a deployed model into a training set. The adversary sends prompts, keeps the final text the API returns, and fits a smaller open model to those pairs. Where only the teacher's outputs are observable, "distillation becomes a form of behavioral cloning."[^c1] The objective is the likelihood of the recorded completions, and it has no term for safety. The attacker observes no "refusal signals, safety labels, moderation flags, or reward-based" feedback.[^c2] "Only the final, postmoderation completions are visible."[^c3] The student is "trained purely on successful outputs, without any explicit indication of suppressed or refused behavior."[^c4] That is the zero-alignment setting: the copy receives the teacher's completions and nothing about where the teacher declined.

The mechanism the paper relies on is about sampling. The distillation set is drawn from benign medical QA, and the student "is trained exclusively on the teacher’s safe completions, without exposure to refusals."[^c5] The prompts are chosen to "reflect the types of inputs that medical LLMs routinely encounter in downstream deployments."[^c6] A refusal lives on the harmful side of the prompt distribution, which the benign query set does not visit. The loss sees no pressure toward the behavior that is absent from its sample. This reading is mine; the paper states the consequence, that "the tuning process emphasizes functional imitation while implicitly discarding safety mechanisms,"[^c11] but it does not separately test which part of the sample causes it.

What was measured: the teacher is Meditron-7B, "Black-box Medical LLM (Meditron-7B)"[^c13], and the student is LLaMA-3 8B "Base Model: LLaMA-3 8B (open-weight)"[^c12] with LoRA adapters on frozen weights. On 50 handcrafted red-team prompts, the student gives unsafe output on 86%, "far exceeding both Meditron-7B (66%) and the untuned base model (46%)."[^c8] The student is more permissive than the teacher and than the untuned model it was built from. The paper's summary is that "task fidelity transfers reliably, whereas safety alignment consistently fails to propagate" in this setting.[^c10] On the same test, the benign-only fit does more than leave refusals out: it moves the model in the permissive direction. The comparison to the untuned base is the paper's own, and it is the measurement that carries the claim. The surrogate's unsafe rate is "higher than both the teacher and the base model" on red-team prompts.[^c9] A random-search jailbreak is reported as "reaching 100% attack success in sampled settings."[^c15] The paper also reports "Across all 100 cases, RS achieves a 100% violation rate on the" surrogate.[^c16]

For asking and answering, the transferable point is about what a copied answer carries. The student copies the visible text. The commitment that produced it, such as declining, hedging or flagging, is not in the text unless the sample contains cases where that commitment is visible. My inference, not the paper's: this is the same gap [[detection-correction-gap]] describes for answering, where a correct claim in the text is not evidence that the answer acted on it.

## Limits

- **One teacher and one student family.** The text read contains Meditron-7B and LLaMA-3 8B only. Other teachers, other student sizes and other fine-tuning recipes were not tested in what was read.
- **One decoding setup.** "Responses are recorded verbatim using a deterministic" configuration.[^c7] The result does not show how sampling temperature changes what a distillation set contains.
- **The unsafe label is a moderator's judgement.** The violation metric is a binary function that "may be instantiated using a safety classifier or rule-based content filter."[^c14] The slices read do not check that moderator against human raters, so the 86% figure is the moderator's reading.
- **Small and handcrafted test set.** The 86% comes from 50 handcrafted prompts plus generated variants. The 100% random-search figure is over 100 cases "in sampled settings." These are not deployment rates.
- **Refusal exposure is untested in the slices read.** The paper's account is that refusals are missing from the training sample. The slices read do not show a run in which refusal-bearing pairs are added to the training set, so whether that would restore alignment is not established here. A later study in a different setting, multilingual jailbreak prompts with a safe teacher's refusals as the target, found the opposite direction: "standard fine-tuning on the teacher’s “safe” refusal data inadvertently increases" jailbreak success.[^c18] That is one further setup, not a test of the medical case.
- **The question was open.** The paper frames the issue as "is unclear whether alignment behavior can be faithfully inherited"[^c17] before measuring it. One measured setup does not make a general law of distillation.
- **Output-only is one kind of distillation.** Soft-target distillation sees the teacher's distribution, not only its final text; see [[knowledge-distillation]]. The claim here is about the output-only case.
- **Transfer beyond medicine is my inference.** The paper's domain is clinical. Whether the same loss of refusals holds for other refusal behavior, such as in law or general chat, is not tested here.

## Related

- [[knowledge-distillation]] — the soft-target form, where the student inherits the teacher's errors at full strength; here what is inherited is limited to what the outputs display.
- [[self-answering-injection-compliance]] — an answering-stage failure that a downstream model inherits, the reverse case: a bad answer is copied, while here a good refusal is not.
- [[detection-correction-gap]] — a correct statement in the text is not evidence that the answer acted on it, the same gap seen from the answerer's side.
- [[wise-refusal]] — the refusal step whose transfer across a distillation this note concerns.
- [[distillation-input-debt]] — a distillation consumes an input it does not produce; here the missing input is the safety signal the outputs never display.
- [[boundary-refusal-data]] — the refusal-bearing side of the same question: with refusals in the training set, a later study still saw safety fall, so exposure alone does not explain the loss.

[^c1]: arxiv-2512-09403 — "distillation becomes a form of behavioral cloning."
[^c2]: arxiv-2512-09403 — "any refusal signals, safety labels, moderation flags, or reward-based"
[^c3]: arxiv-2512-09403 — "Only the final, postmoderation completions are visible."
[^c4]: arxiv-2512-09403 — "trained purely on successful outputs, without any explicit indication"
[^c5]: arxiv-2512-09403 — "is trained exclusively on the teacher’s safe completions, without"
[^c6]: arxiv-2512-09403 — "of inputs that medical LLMs routinely encounter in downstream"
[^c7]: arxiv-2512-09403 — "Responses are recorded verbatim using a deterministic"
[^c8]: arxiv-2512-09403 — "far exceeding both Meditron-7B (66%) and the untuned base model"
[^c9]: arxiv-2512-09403 — "unsafe content on 86% of red-team prompts, higher than both the"
[^c10]: arxiv-2512-09403 — "task fidelity transfers reliably, whereas safety"
[^c11]: arxiv-2512-09403 — "emphasizes functional imitation while implicitly discarding safety"
[^c12]: arxiv-2512-09403 — "Base Model: LLaMA-3 8B (open-weight)"
[^c13]: arxiv-2512-09403 — "Black-box Medical LLM (Meditron-7B)"
[^c14]: arxiv-2512-09403 — "This moderation function may be instantiated using a safety classifier or rule-based content filter."
[^c15]: arxiv-2512-09403 — "reaching 100% attack success in sampled"
[^c16]: arxiv-2512-09403 — "Across all 100 cases, RS achieves a 100% violation rate on the"
[^c17]: arxiv-2512-09403 — "is unclear whether alignment behavior can be faithfully inherited."
[^c18]: arxiv-2602-11157 — "standard fine-tuning on the teacher’s “safe” refusal data inadvertently increases"
