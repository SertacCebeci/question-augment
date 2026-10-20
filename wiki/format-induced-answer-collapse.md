---
description: "Asking for the reply in JSON or XML, with no decoder constraint, moves a model's choice among equally valid answers toward the field's mode; enforcing the schema adds almost nothing."
aliases: ["structured-output diversity collapse", "register-indexed defaults", "format register effect on answer choice"]
sources: ["doi-10-48550-arxiv-2607-18476"]
---
# Format-induced answer collapse

Where a question has many equally valid answers, the register in which the reply is requested changes which answer a model gives. Parikh re-ran a 31-prompt, 44-model census of one-word answers ("Name a tree") with only one change: the reply was requested as JSON, with no schema enforcement and no constrained decoding. Answer-choice surprisal is the leave-one-out bits of a model's answers under the pooled answers of the other models, and it fell from 1.80 to 1.58 (per-model change -0.22, p = .0002).[^c1] On the unconstrained "Pick a word" prompt the modal answer's share rose from 41% to 64% and distinct answers fell from 52 to 36.[^c2]

## Mechanism as measured

**A sharpener, not a re-indexer.** In 28 of 31 categories the JSON mode equals the plain-chat mode. The three flips fall where the chat mode was weakest (insect: ant to butterfly).[^c3] The format amplifies the prior the model already had.

**Progressive.** Six of 44 models move individually, all toward the mode, led by the most distinctive frontier model (deepseek-v3.2 loses 1.31 bits, half its distinctiveness). The conformist floor barely moves.[^c4] Some positive changes are stranding: a model that holds its answers earns a higher surprisal when the field converges around it. A panel-free self-divergence check separates the two cases.[^c5]

**Not a cooled sampler.** Self-distinctness (distinct answers per sample) is nearly flat across formats (plain 0.42, JSON 0.39) while surprisal drops. The authors read this as a reshaped distribution, not a rescaled one.[^c6]

**Defaults are register-indexed.** At n = 20, a model's stable chat defaults are significantly shifted by JSON in 76 of 144 cases (53%), and 29% revert outright to the field's mode. The format also installs defaults absent from chat: one model answers cerulean for colour 0% of the time in chat and 100% in JSON.[^c7] Two models with the same chat default can diverge under the format (mango stays mango for one, becomes apple for the other). The author's conclusion is a per-register defaults profile, not one personality.[^c8]

**A register gradient.** Compliance-conditioned field changes are JSON -0.22 bits, XML -0.23, YAML -0.09, CSV -0.09 and bracket wrapper +0.13. Only JSON and XML are significant compressions, and the brackets loosening is also significant.[^c9] The author reads this as weighing toward tool-use post-training, the formats models are trained to answer in. The unconstrained prompt still concentrates under every serialization, so a corpus-register component remains.[^c10]

**Enforcement adds little.** On the 36 models whose providers support it, the request gives 1.56 bits, strict response_format gives 1.53, and open chat gives 1.79.[^c11] The effect lies in the model's response to the request, not in the sampler. This places the cost where [[format-restriction-effect]] places it for accuracy: at the prompt, upstream of [[constrained-decoding]].

## What it means for asking

The deployment surface, [[structured-output]], is served by a more homogeneous model than the chat surface where models are compared. The cost bites where many answers are acceptable (surveys, recommendations, brainstorming, tool choice). It does not bite where one correct value is extracted.[^c12]

## Limits

- One snapshot, one gateway (OpenRouter), requested temperature 1.0 not honored uniformly across providers; surprisal is panel-relative, so absolute bits are not portable.[^c13]
- One clause wording per format, so register cannot be separated from phrasing; no paraphrase control.
- Tool-call framing is unmeasured, and enforcement is heterogeneous across providers (native versus gateway coercion), so per-model enforcement reactions are confounded.
- The post-training versus corpus mechanism is an inference from the gradient, not an intervention. The brackets reversal has no settled mechanism.
- Single-word answers only; whether longer free-form answers collapse the same way is not tested. The prompts have no correct answer, so nothing here says the collapse affects accuracy.

## Related

- [[format-restriction-effect]] — the accuracy-side counterpart; both place the cost at the format-requesting prompt
- [[structured-output]] — the umbrella surface whose homogeneity is measured here
- [[constrained-decoding]] — the enforcement arm adds only -0.03 bits beyond the request

[^c1]: doi-10-48550-arxiv-2607-18476 — "mean answer-choice surprisal drops 1.80 to 1.58 bits"
[^c2]: doi-10-48550-arxiv-2607-18476 — "the modal answer’s share rises from 41% to 64% and distinct answers fall from 52 to"
[^c3]: doi-10-48550-arxiv-2607-18476 — "the plain-chat modal answer survives in 28 of 31 categories"
[^c4]: doi-10-48550-arxiv-2607-18476 — "six of 44 models move individually (BH-FDR q = .10), all toward the mode"
[^c5]: doi-10-48550-arxiv-2607-18476 — "A panel-free"
[^c6]: doi-10-48550-arxiv-2607-18476 — "rather than a rescaled one"
[^c7]: doi-10-48550-arxiv-2607-18476 — "JSON shifts 53% of a model’s stable chat defaults, mostly back to the crowd"
[^c8]: doi-10-48550-arxiv-2607-18476 — "a model’s character is indexed to the channel it is"
[^c9]: doi-10-48550-arxiv-2607-18476 — "the field-mean ∆-surprisal is −0.22"
[^c10]: doi-10-48550-arxiv-2607-18476 — "The corpus-register account is not dead"
[^c11]: doi-10-48550-arxiv-2607-18476 — "is 1.56 bits under the"
[^c12]: doi-10-48550-arxiv-2607-18476 — "This bites"
[^c13]: doi-10-48550-arxiv-2607-18476 — "requested temperature 1.0 is not honored uniformly across providers"
