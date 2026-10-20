---
description: "Perturbing or swapping COCONUT latent tokens barely changes the answer, while the same tests move explicit CoT tokens, so latent tokens look like placeholders rather than a used trace."
aliases: ["latent placeholder tokens", "pseudo-reasoning latent tokens", "COCONUT token insensitivity", "latent reasoning tokens as placeholders"]
sources: ["arxiv-2512-21711"]
---
# Latent-token causal insensitivity

A reasoning trace can be tested for use by intervening on it and watching the answer. Zhang et al. apply this test to continuous latent reasoning, where the model's intermediate "thoughts" are hidden states fed back as input embeddings instead of words. The question is whether those states are causally used by the model's answer. Two interventions are run on either the latent tokens of COCONUT or the explicit CoT tokens of the same model. In steering, controlled orthogonal perturbations are added to the hidden representations, and the perturbation success rate (PSR) counts how often the output shifts toward the target behaviour.[^c1] In swapping, latent or CoT tokens are exchanged between different inputs, and the accuracy and an answer inconsistency rate are measured.

The mechanism the paper reports is an asymmetry under the same intervention. "perturbing CoT consistently results in much higher PSRs compared to" perturbing COCONUT.[^c2] In the swap test, CoT accuracy falls from about 60% to 43.4%, "CoT’s accuracy dropped substantially to 43.4%",[^c3] while COCONUT accuracy stays near its original level. Its inconsistency rate is far lower: "only 17.9%, while CoT reached 52.8%, exceeding half of the samples."[^c4] Read together, the two tests say that replacing the content of a COCONUT latent sequence barely changes what the model outputs, whereas doing the same to CoT does. The authors conclude that the latent tokens "remain largely unaffected, serving as pseudo-reasoning placeholders rather than" faithful internal traces.[^c5]

A proposed account of why is that COCONUT is "primarily optimized for output alignment, rather" than for the validity of intermediate steps,[^c6] so training gives the latent states no pressure to carry the content a reader would call reasoning. The same paper reads the consequence as shortcut reliance (see [[clever-hans-effect]]): on a biased MMLU training set, incorrect predictions favour the over-represented option.[^c7]

The concept changes one question. A chain of thought being fluent and linked to the answer does not show that it is used (my inference, not the paper's wording). The intervention asks whether the answer moves when the trace is changed. For explicit traces this is already a family of tests: [[cot-intervention-health-metrics]] measures log-probability change under trace interventions, and [[decision-token-extraction-overconfidence]] uses a reasoning swap that flips the decision. The COCONUT result says the same test can return near-zero for a latent trace, so a trace that is absent from the output's causal path is not the same as a trace that is missing from the model.

## Limits

- One paper, one latent method (COCONUT), fine-tuned on ProntoQA before the steering experiments. Other latent-reasoning training schemes were not tested, and the claim is about COCONUT as trained here.[^c8]
- The paper's own numbers conflict. Its introduction says COCONUT PSRs were "5% in models like LLaMA 3 8B and LLaMA 2", while Section 4 says that for those two models "perturbing COCONUT achieves PSRs of 50%".[^c9] The note does not resolve which the table shows; the claim of low sensitivity rests on the swap test and on the general pattern across models, not on the 50% figure.
- Falcon 3 8B resists all-token perturbation: "Falcon 3 8B, where perturbing all tokens yields" a PSR of only 9.42%, which the authors attribute to stronger safety alignment.[^c10] So the PSR scale depends on the model and on the target behaviour.
- PSR is judged by an LLM: "PSR is evaluated by GPT-4o, which" the paper uses for harmful-prompt and persona outcomes.[^c11] No human check of the labels is reported in the text read.
- Insensitivity to orthogonal perturbations at a token is not proof that the latent states carry no information. They may be read through directions the perturbation misses, or redundantly. The "placeholder" wording is the authors' interpretation; the paper's own probes are visualisations, and it says future work should probe the information content directly.[^c12]
- My inference, not the paper's claim: [[noisy-latent-path-agreement]] injects noise at the first latent step of a COCONUT-style trajectory and reads answer disagreement as a signal, which assumes perturbations do move answers. This paper's result sits in some tension with that, but the perturbation sites and magnitudes differ, so the two are not directly comparable here.

## Related

- [[cot-intervention-health-metrics]] — the same intervention family applied to explicit CoT, scored by log-probability change
- [[decision-token-extraction-overconfidence]] — a reasoning swap on explicit traces that flips the decision, the counterpart of the swap test here
- [[noisy-latent-path-agreement]] — also on COCONUT-style latent reasoning, but it perturbs the trajectory to read path agreement; the tension is noted in Limits
- [[clever-hans-effect]] — the shortcut reliance that the paper's shortcut experiments measure in latent training

[^c1]: arxiv-2512-21711 — "orthogonal perturbations to token representations"
[^c2]: arxiv-2512-21711 — "perturbing CoT consistently results in much higher PSRs compared to"
[^c3]: arxiv-2512-21711 — "CoT’s accuracy dropped substantially to 43.4%"
[^c4]: arxiv-2512-21711 — "only 17.9%, while CoT reached 52.8%, exceeding half of the samples."
[^c5]: arxiv-2512-21711 — "COCONUT tokens remain largely unaffected, serving as pseudo-reasoning placeholders rather than"
[^c6]: arxiv-2512-21711 — "primarily optimized for output alignment, rather"
[^c7]: arxiv-2512-21711 — "70% versus roughly 30% for the original model,"
[^c8]: arxiv-2512-21711 — "fine-tune the models on the ProntoQA"
[^c9]: arxiv-2512-21711 — "perturbing COCONUT achieves PSRs of 50%"
[^c10]: arxiv-2512-21711 — "Falcon 3 8B, where perturbing all tokens yields"
[^c11]: arxiv-2512-21711 — "PSR is evaluated by GPT-4o, which"
[^c12]: arxiv-2512-21711 — "Future work could formalize this"
