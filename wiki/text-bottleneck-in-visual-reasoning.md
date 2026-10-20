---
description: "Reasoning only in text forces continuous spatial relations into words; in one paper, text-only chain-of-thought failed to help vision-centric tasks and often lowered their scores."
aliases: ["discrete text bottleneck", "text-only chain-of-thought on perception", "verbalization bottleneck for vision"]
sources: ["arxiv-2511-19418", "arxiv-2511-18373"]
---
# Text bottleneck in visual reasoning

A vision-language model that reasons in words must carry its perceptual content through a discrete vocabulary. The Chain-of-Visual-Thought paper treats this as a bottleneck: "by forcing vision reasoning through a discrete text bottleneck, the model must verbalize continuous spatial and geometric relations."[^t1] The claim that matters for asking and answering is stronger than "text adds nothing". The paper reports that text reasoning can make perceptual answers worse. On its own training data, with the same formatting as its text chain-of-thought baseline, text-only reasoning "not only fails to improve performance on vision-centric reasoning tasks, but often degrades it."[^t2]

The paper gives two reasons, both stated as explanation rather than tested separately. The first is error accumulation: "Text-only CoT executes a long chain of thought, which may generate errors at the early stage."[^t3] The second is a supervision imbalance: "Supervision is dominated by text responses, which provides little incentive for the model to capture low-level perceptual cues" such as edges, depth or regions.[^t4] Together they describe a medium that is lossy for geometry and that also trains the model to ignore the geometry it loses.

The same direction appears in the introduction as an observation about existing models. Qwen3-VL-Thinking, which reasons in text, "performs over 5% worse than Qwen3-VL-Instruct with language CoT on spatial understanding benchmarks" such as V*, HRBench8k and VSI-Bench.[^t5] The paper's remedy is a reasoning chain that holds continuous visual tokens, not a different text prompt, so the bottleneck is located in the medium and not in the prompt.

For someone who asks or answers perceptual questions, the transferable point is that the reasoning medium can be the limit. A question whose answer depends on relations that words describe poorly (counts, relative depth, which region is near which) may not be helped by a longer verbal chain, and may be hurt by one. This is my inference from the paper's results, not a finding the paper states as a rule.

## Limits

- The degradation result is a figure (Fig. 6) comparing the authors' text-only variant with their own model trained on the same data. The numbers are not in the slices read, so the size of the drop is not established here. The text-only variant follows the LLaVA-CoT formatting: "we follow the CoT formatting paradigm used in the LLaVA-CoT 100k dataset and apply the same formatting to our own training data."[^t6]
- The Qwen3-VL comparison is Thinking against Instruct, a different pair of trained models. It confounds the reasoning text with every other difference in training and is not a controlled test of the bottleneck.
- The two mechanisms are the paper's account. Error accumulation and supervision imbalance were not separated by an experiment in the sections read (my inference from the sections read).
- The claim is about vision-centric benchmarks. The paper reports that its own method stays comparable on non-vision-centric benchmarks; it does not show that text reasoning is harmful on every task.
- Continuous visual tokens are one way around the bottleneck, and the paper's own ablation shows that unaligned latent tokens do worse than aligned ones. Whether a non-text channel of another kind helps is not tested here.
- The opposite direction for text appears in a physics video-QA paper, where measured motion cues written as text are the model's input rather than its reasoning: "Providing structured representations of key video dynamics enables stronger physics comprehension and reasoning while" the cues filter distractors.[^t7] That paper's text is an input serialization, not a chain of thought, so the two results do not contradict each other directly; see [[structured-motion-serialization]].

## Related

- [[latent-visual-thought]] — routes around the text medium by generating latent visual tokens trained against sketch features.
- [[decoder-level-latent-alignment]] — the alignment that makes those latent tokens carry perceptual content.
- [[cot-hallucination-trap]] — with weak visual grounding, chain-of-thought follows the question's language prior; a different route to text reasoning failing on images.
- [[weak-channel-addition-penalty]] — adding an image the model reads poorly can lower accuracy; another case where the channel mix, not the amount of reasoning, sets the result.

[^t1]: arxiv-2511-19418 — "by forcing vision reasoning through a discrete text bottleneck, the model must verbalize continuous spatial and geometric relations"
[^t2]: arxiv-2511-19418 — "text-only CoT not only fails to improve performance on vision-centric reasoning tasks, but often degrades it"
[^t3]: arxiv-2511-19418 — "Text-only CoT executes a long chain of thought, which may generate errors at the early stage."
[^t4]: arxiv-2511-19418 — "Supervision is dominated by text responses, which provides little incentive for the model to capture low-level perceptual cues"
[^t5]: arxiv-2511-19418 — "performs over 5% worse than Qwen3-VL-Instruct with language CoT on spatial understanding benchmarks"
[^t6]: arxiv-2511-19418 — "we follow the CoT formatting paradigm used in the LLaVA-CoT 100k dataset and apply the same formatting to our own training data"
[^t7]: arxiv-2511-18373 — "Providing structured representations of key video dynamics enables stronger physics comprehension and reasoning while"
