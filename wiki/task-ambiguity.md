---
description: "Task ambiguity: more than one task fits the instruction and examples, unlike input ambiguity; instructions and decorrelated examples resolve it, and models learn the skill from ambiguous data."
aliases: ["ambiguously-specified tasks", "task underspecification", "AmbiBench"]
sources: ["tamkin-2022"]
---
# Task ambiguity

Task ambiguity arises when more than one task is consistent with the provided instructions or labeled examples.[^c1] It differs from input ambiguity: in "the nurse handed the doctor her phone" the task is clear (resolve the referent) but the input lacks the information to answer it.[^c2] In task ambiguity the input is answerable under each candidate task, and the missing piece is which task the asker meant. The shortcut-learning case is one form: training examples all solvable by a simple feature such as a watermark instead of the intended task.[^c3] This note concerns the asker's side of a request, not the ambiguity in a particular sentence; see [[ambiguity-taxonomy]] for the catalogue of ambiguity sources.

## The measurement device

AmbiBench holds six binary sentence-classification tasks in three feature pairs (for example animal / outdoor location). Every sentence carries one feature from each pair, so a label cannot reveal which feature matters without an instruction or further examples.[^c4] Sentences are built from templates, which lets the authors control and measure how much ambiguity each in-context example carries.[^c5] Because every example fits two tasks, a model cannot succeed from format or label-space cues alone, which earlier work suggested models lean on.[^c6]

## What resolves it

Two resolvers were tested.

- Instruction. Given two examples (one per class) and a full instruction naming the feature, humans were perfect in all but one task, closely followed by text-davinci-003 and -002. All other models, including 175B+ non-feedback models and smaller feedback-trained ones, did relatively poorly.[^c7] With the feature redacted, humans and many models sat near 50 percent. The exception was negation, where humans scored 100 percent, which the authors attribute possibly to an inductive bias making negation salient.[^c8]
- Examples. Labeled examples gradually identify the salient feature provided the features are sufficiently decorrelated.[^c9] A Bayesian oracle is perfect once the examples disambiguate and at chance before. All models underperformed it. The best model, text-davinci-002, significantly outperformed human participants.[^c10]

Scale or human-feedback training alone is not enough: the abstract states that scaling to 175B plus human-feedback training together bring models to or beyond humans, and either alone is insufficient.[^c11] The smaller curie model reliably beat the larger davinci, and feedback training hurt at curie scale but helped dramatically at davinci scale.[^c12]

## A learnable skill

The authors hypothesised that feedback data contained ambiguous few-shot prompts. Finetuning davinci on 272 ambiguous in-context examples from four tasks and testing on two held-out tasks closed the gap to the feedback models. A control finetuned on unambiguous versions gave no improvement, so ambiguity in the training data was the active ingredient.[^c13]

## Limits

- Only two candidate tasks and simple templated linguistic features; real ambiguity may span many or infinitely many tasks, and the authors call for in-the-wild study.[^c14]
- Humans needed extra interface instructions and may have tired over 20 examples, so "superhuman" is cautioned against.[^c15]
- The cause of the feedback-model advantage is a hypothesis supported by the finetuning control, not shown directly; the training data were not released.
- The paper measures resolving ambiguity from given context. It does not test models asking a clarifying question, so nothing here shows when asking beats inferring (my note, not the paper's claim).

## Related

- [[ambiguity-taxonomy]] — taxonomy of ambiguity sources; task ambiguity is the intent-level kind
- [[underspecbench]] — benchmark of underspecified requests, a neighbour measurement
- [[under-specification-severity-asymmetry]] — how costly missing specification is
- [[version-space]] — the set of tasks still consistent with the examples

[^c1]: tamkin-2022 — "Task ambiguity arises when more than one task is consistent with the provided instructions or labeled examples."
[^c2]: tamkin-2022 — "Here, the task is clear (determine who her refers to), but there is not enough information in the input to answer it."
[^c3]: tamkin-2022 — "One form of task ambiguity is shortcut learning (Geirhos et al., 2020), where the training examples can all be solved by identifying a simple feature"
[^c4]: tamkin-2022 — "each sentence has two linguistic features"
[^c5]: tamkin-2022 — "AmbiBench examples are programmatically constructed from a set of templates, allowing precise control over the amount of task ambiguity in each in-context example"
[^c6]: tamkin-2022 — "Thus, models that perform well on AmbiBench must infer the desired task using e.g., the task instruction or other examples."
[^c7]: tamkin-2022 — "Humans are closely followed by the text-davinci-003 and text-davinci-002 HFD models"
[^c8]: tamkin-2022 — "in the case of negation, humans achieve 100% accuracy despite lacking an instruction identifying the salient feature."
[^c9]: tamkin-2022 — "more examples will gradually identify the salient feature provided the features are sufficiently decorrelated."
[^c10]: tamkin-2022 — "the best language model (the HFD-trained text-davinci-002) significantly outperformed the human participants"
[^c11]: tamkin-2022 — "but that either one alone is not sufficient."
[^c12]: tamkin-2022 — "the HFD training hurts at curie scale, but dramatically helps at davinci scale."
[^c13]: tamkin-2022 — "we do not observe any improvement for the control finetuned models"
[^c14]: tamkin-2022 — "task ambiguity may occur between arbitrarily many tasks, or even an infinitely large family of tasks."
[^c15]: tamkin-2022 — "we caution against claims of “superhuman performance”"
