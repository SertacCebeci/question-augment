---
description: "In codebook-style LLM classification, informational detail of the prompt drives accuracy; surface form and added reasoning matter little once detail is present, and model scale moderates both."
aliases: ["prompt brittleness", "informational detail vs prompt engineering", "codebook as prompt"]
sources: ["doi-10-1371-journal-pone-0354757", "arxiv-2602-04297", "arxiv-2512-22742"]
---
# Prompt content over surface form

Çelebi & Penczynski (2026) take three codebooks written for human annotators (one promise task, two strategic-thinking tasks) and split each into components: classification instructions, experiment context, theory, worked examples. They vary the level of detail of each in a factorial design across four models, then at the lowest and highest detail levels vary formatting, framing, wording and reasoning effort.

**Content is the lever.** Transcribed with minimal change, the codebooks reach 82-88% agreement with human-agreed labels.[^c1] On the learning-heavy tasks, cutting the classification instructions to one line drops accuracy from above 80% to below 50%.[^c2] Components partly substitute (context and theory for instructions; examples for content) and partly complement each other.

**Surface form is not.** The authors define surface variations as changes to presentation without change in informational detail, and prompt brittleness as dependence of outcomes on them. At full detail the effect is nil for the largest proprietary model and marginal for its small sibling; open-weight models show some brittleness, but with no consistent direction, so the same change helps in one case and hurts in another.[^c3] The authors read brittleness reported elsewhere as likely an artifact of underspecified prompts or small models.[^c4]

**Reasoning does not replace content.** On a minimal prompt, reasoning can even hurt; given content, reasoning adds about nothing for the frontier model, and small models' zero-shot gains disappear once examples are present.[^c5]

**Model scale moderates.** On the recognition-heavy task model choice explains most variance; on the learning-heavy tasks detail carries comparable weight. Larger models exploit extra detail and tolerate presentation changes; small ones may be hurt by extra detail and are more format-sensitive.[^c6]

**Underspecification as the source of reported sensitivity.** Revisiting prompt sensitivity in text classification (3 tasks, 6 LLaMA variants, 10 prompts per format), comparison of minimal prompts (no instruction, no label set) against instruction prompts finds that minimal prompts show higher accuracy variance and lower logit values for the label tokens; the minimal format often fails to beat random chance because the model emits free text that maps to no label.[^c8] Linear probing indicates the internal representations are only marginally affected, the damage emerging in the final layers and outputs.[^c9] Instruction prompts reduce but do not remove sensitivity: on some model-dataset pairs (for example AG News) they underperform minimal prompts with higher deviation.[^c10]

**Trained models can stay sensitive to wording.** A CTA study fine-tunes instruction-tuned models (FLAN-T5 and Llama 3.1 8B) on one labeling template and tests them on reworded and noisy templates. The authors report that "the sensitivity issue persists even with" full-parameter tuning when no prompt variants are added.[^c11] This is a measured effect on open models trained on one form, not the frontier-model setting of the codebook study, so the two are not directly comparable (my inference).

My reading (inference, not the paper's claim): for asking, what the question tells the answerer about the categories and context is worth more than how it is dressed, and the answerer's capacity decides how much of that content is usable.

## Limits

- Experimental-economics text is, in the authors' words, a best-case setting: constrained vocabulary, known payoffs, full context available.[^c7]
- Codebooks nearer the minimal condition, or concepts intrinsically ambiguous, may make design choices matter again; untested.
- Only four models, three tasks, one agreement metric against human-agreed labels (temperature 0).
- A null on surface form is a null on the tested variations, not on all possible ones.

## Related

- [[task-ambiguity]] — intrinsically ambiguous concepts limit what any codebook can specify
- [[information-need-impact-hierarchy]] — which missing information costs most, in another task domain
- [[capacity-dependent-format-tax]] — format sensitivity that depends on model capacity
- [[llm-judge-biases]] — presentation-driven variance in LLM judgements

[^c1]: doi-10-1371-journal-pone-0354757 — "reaches 82–88% agreement with humans across the four models tested."
[^c2]: doi-10-1371-journal-pone-0354757 — "accuracy on L-tasks falls from above 80% to below 50% when classification instructions are"
[^c3]: doi-10-1371-journal-pone-0354757 — "Surface variations have no significant effect for GPT 5.4 and only marginal effects for GPT 5.4-nano"
[^c4]: doi-10-1371-journal-pone-0354757 — "Our results indicate that prompt brittleness is likely an artifact of classification"
[^c5]: doi-10-1371-journal-pone-0354757 — "Result 4. Reasoning cannot substitute for codebook content and does not improve frontier-model classification."
[^c6]: doi-10-1371-journal-pone-0354757 — "Larger models, GPT 5.4 and Qwen 3.5 397B, make better use of additional detail (full codebook content)"
[^c7]: doi-10-1371-journal-pone-0354757 — "Experimental-economics text is a best-case setting for codebook-based classification"
[^c8]: arxiv-2602-04297 — "underspecified prompts exhibit higher performance variance and lower logit values for relevant tokens"
[^c9]: arxiv-2602-04297 — "emerging in the final layers"
[^c10]: arxiv-2602-04297 — "they are not enough to deal with all"
[^c11]: arxiv-2512-22742 — "the sensitivity issue persists even with"
