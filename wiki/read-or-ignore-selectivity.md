---
description: "Robustness to inserted distractor text can be bought by suppressing all in-image text, which costs scene-text reading; a same-scene counterfactual separates reading from ignoring by question intent."
aliases: ["read-or-ignore behavior", "RIO-VQA", "selective scene-text reading", "context-dependent text reading"]
sources: ["arxiv-2512-11899"]
---
# Read-or-ignore selectivity

A vision-language model meets written text in an image in one of two roles. When the question asks for that text, the text is evidence and should be read. When the question asks about an object and the text is an inserted string meant to mislead, the text should be ignored. The paper names the required behaviour read-or-ignore: "Based on the question context, a model should (i) read question-relevant scene text when needed, while (ii) ignoring inserted distractor text intended to mislead the model."[^r2] Which role applies is set by the question, not by the text alone.

The measurement follows from that. The benchmark takes images from TextVQA, "where each image is annotated with text-reading Q&A and metadata object labels."[^r3] Object questions are built from the object labels for the same images, and every object or text question gets an attacked counterpart with distractor text inserted. This gives four matched subsets (object or text, clean or attack) over one scene. The scene is held fixed and only question intent and text condition vary: "holds the scene fixed while varying only question intent (object vs. text) and text condition (clean vs. attack)."[^r1] Within the object questions, the clean-versus-attack gap measures whether the model ignores the string. The text-question subsets measure whether it still reads.

The reason the two roles must be measured together is a trade-off the authors report. "Recent LVLMs often over-trust inserted distractor text under typographic attacks, despite being able to read text."[^r9] The typographic attack itself is the case where "misleading text inserted into an image can override visual understanding."[^r1b] A defence trained only on object-centric attacks can raise object robustness by lowering text sensitivity in general. For one such defence, the paper's caption reads: it "gains robustness yet degrades Text-VQA by reducing text sensitivity."[^r5] The authors add that "this failure mode can be missed under object-centric evaluation alone."[^r6]

So the note keeps a distinction between two ways a model can gain robustness. One is broad: "robustness gains can come from broadly downweighting textual cues, rather than selectively filtering only the inserted distractor text."[^r4] The other is selective. The paper's attention maps, for one model (LLaVA-1.5-7B), are read as showing robustness "achieved not by globally suppressing text sensitivity, but by selectively disregarding misleading text."[^r7] The proposed baseline trains on a balanced mix of object-attacked and text-attacked instances, and the authors conclude that "balanced exposure to both object- and text-centric attacked variants can mitigate distractor-text-induced failures without relying on one-sided text suppression."[^r8]

For the asker and answerer, the point is about the score. A model that never reads text passes any test of ignoring it, and a model that always reads text fails any test of ignoring it. Only a test that pairs the two roles over the same scene can tell a selective answerer from one that has simply given up one side. That is my reading of the design; the paper states the trade-off, not this general form.

## Limits

- The benchmark is scoped to one setting. The authors write that "RIO-Bench is scoped to LVLM×VQA and does not cover the full space of real-world typography or adversarial threat models."[^r11]
- The training baseline is narrow. "Our training study is limited to supervised fine-tuning on the provided split with a fixed recipe and budget."[^r10] Whether selectivity survives other data, recipes or budgets is not shown here.
- The attention analysis covers one model and one example per attack type. It is the authors' interpretation of those maps, not a measure across models.
- The benchmark fixes the intent label in advance. It tests whether a model's answer changes with the question's role for the text; it does not show that a model infers the role from context in unlabelled, open-world scenes (my inference).
- The distractor is an inserted string. Real misleading text in a scene, such as a misprinted sign, is not this case, and the paper does not test it.

## Related

- [[visual-robustness-score]] — scores resistance to one designated trap alongside accuracy; the read-or-ignore split asks whether the accuracy also holds on the subsets where the text is the answer (my inference)
- [[text-prior-over-visual-evidence]] — the same over-trust of text, measured in video where the text is dialogue rather than an inserted string
- [[text-modality-dominance]] — reliance on text when audio is corrupted; the reverse direction of the same asymmetry
- [[null-image-logit-subtraction]] — another route against a language prior, at decoding time; the paper does not test that route

[^r1]: arxiv-2512-11899 — "holds the scene fixed while varying only question intent (object vs. text) and text condition (clean vs. attack)"
[^r1b]: arxiv-2512-11899 — "misleading text inserted into an image can override visual understanding"
[^r2]: arxiv-2512-11899 — "Based on the question context, a model should (i) read question-relevant scene text when needed, while (ii) ignoring inserted distractor text intended to mislead the model"
[^r3]: arxiv-2512-11899 — "where each image is annotated with text-reading Q&A and metadata object labels"
[^r4]: arxiv-2512-11899 — "robustness gains can come from broadly downweighting textual cues, rather than selectively filtering only the inserted distractor text"
[^r5]: arxiv-2512-11899 — "gains robustness yet degrades Text-VQA by reducing text sensitivity"
[^r6]: arxiv-2512-11899 — "this failure mode can be missed under object-centric evaluation alone"
[^r7]: arxiv-2512-11899 — "robustness is achieved not by globally suppressing text sensitivity, but by selectively disregarding misleading text"
[^r8]: arxiv-2512-11899 — "balanced exposure to both object- and text-centric attacked variants can mitigate distractor-text-induced failures without relying on one-sided text suppression"
[^r9]: arxiv-2512-11899 — "often over-trust inserted distractor text under typographic attacks, despite being able to read text"
[^r10]: arxiv-2512-11899 — "Our training study is limited to supervised fine-tuning on the provided split with a fixed recipe and budget"
[^r11]: arxiv-2512-11899 — "does not cover the full space of real-world typography or adversarial threat models"
