---
description: "When a tool makes information cheap to get, the binding limit moves to human verification and synthesis; more inputs then lower forecast accuracy only where processing load is already high."
aliases: ["verification bottleneck", "information overload under AI access", "acquisition-processing shift", "attention bottleneck of AI-assisted research"]
sources: ["arxiv-2512-19705"]
---
# Attention bottleneck under cheap information access

When getting information becomes cheap, the scarce input is no longer the information. It is the human attention that must check and combine it. A study of sell-side analysts makes this concrete. In December 2023 a data platform, FactSet, began offering a generative AI assistant to existing subscribers at no extra cost, and the authors treat that as a plausibly exogenous rise in AI access.[^c1] Reports that cite the platform became richer: "featuring 26% more distinct information sources" and broader in topic and method.[^c2] The authors' summary is that generative AI "relaxes information-acquisition constraints while making human attention a more important bottleneck."[^c3]

The mechanism is the split between acquisition and processing. Richer reports did not uniformly mean better decisions. Relative forecast accuracy "declines when analysts face greater information-processing demands."[^c4] The decline is concentrated where the processing load is high: "The deterioration in accuracy and signal alignment is concentrated among analysts who cover" more complex portfolios, work with smaller teams, or revise several firms on the same day.[^c5]

The test that separates a loss of information from a loss of processing is a machine benchmark. A random forest, fed the same observable report signals, fundamentals and consensus forecasts, does not lose accuracy on those reports: "its forecast accuracy does not deteriorate" in the high-workload subsamples where human accuracy falls.[^c6] With the inputs held fixed and the machine unaffected, the authors read the human decline as "a human processing constraint rather than poorer underlying information."[^c12] This is the data-processing logic of [[data-processing-inequality]] applied to people. Processing cannot add information, so when accuracy falls on unchanged inputs, the loss sits in the processor.

The paper states the shift in one line: "the bottleneck can shift from finding information to verifying, prioritizing, and synthesizing it."[^c7] Its authors add that "More AI-generated information thus entails greater verification effort,"[^c8] because the output still goes through human review. The same tool that helps under routine load "can become a source of distraction when attention is strained."[^c9]

The consequence for asking and answering is a conditional one. Cheap supply of answers, sources or drafts raises the reader's verification load. Where that load is already high, adding material can lower the quality of what the reader does with it. Where it is low, the same material raises richness and timeliness. This is my inference from the analyst setting, not a result the paper tests on questions or answers. It is also the reason the cost of a question is not the same as the cost of an extra answer: [[question-budgets]] prices the user's attention as the scarce budget, and this note says where in the chain that attention is spent.

## Limits

- **The treatment is exposure, not use.** The authors observe FactSet citations, not clicks or prompts in the tool. Their estimates are "the incremental effect of exposure to FACT S ET" rather than an effect of verified use, and placebo platforms "do not by themselves prove direct" usage.[^c10] Some control reports may also use generic AI tools, which would attenuate the contrast.
- **Attention is inferred, not measured.** The high-processing-load subsamples are defined by portfolio complexity, team size and same-day revisions. None of these measures attention itself. The paper does not observe a single analyst's attention at a single moment.
- **The machine null is suggestive.** The authors say the machine result is "difficult to reconcile with a simple deterioration in the underlying information." That is a reasoned exclusion, not a proof that the inputs are equally informative for every decision.
- **One domain.** The sample is U.S. sell-side earnings forecasts from 2022 to 2024. Nothing here covers question-asking, chat, or non-financial users. Transfer to those is my inference.
- **Remedies are untested.** The authors recommend workflow design that protects attention, including "designing interfaces that rank and reconcile signals."[^c11] The paper does not test whether such an interface restores accuracy.

## Related

- [[question-budgets]] — the user's attention as the costly budget; this note locates where that cost is spent once answers are cheap.
- [[data-processing-inequality]] — the machine benchmark is the case in which processing cannot add information, so a human loss on fixed inputs is a processing loss.
- [[metacognitive-laziness]] — a neighbouring case in which an AI tool takes over work the human would otherwise do.
- [[dialogue-complexity-load-amplified-framing-effect]] — another load-amplification effect: prior complexity raises cognitive load and changes how a framing bites.

[^c1]: arxiv-2512-19705 — "the 2023 integration of GenAI into FACT S ET as a plausibly exogenous change in AI access"
[^c2]: arxiv-2512-19705 — "featuring 26% more distinct information sources"
[^c3]: arxiv-2512-19705 — "relaxes information-acquisition constraints while making human attention a more important bottleneck"
[^c4]: arxiv-2512-19705 — "declines when analysts face greater information-processing demands"
[^c5]: arxiv-2512-19705 — "The deterioration in accuracy and signal alignment is concentrated among analysts who cover"
[^c6]: arxiv-2512-19705 — "its forecast accuracy does not deteriorate"
[^c7]: arxiv-2512-19705 — "the bottleneck can shift from finding information to verifying, prioritizing, and synthesizing it"
[^c8]: arxiv-2512-19705 — "More AI-generated information thus entails greater verification effort"
[^c9]: arxiv-2512-19705 — "can become a source of distraction when attention is strained"
[^c10]: arxiv-2512-19705 — "These null effects do not by themselves prove direct"
[^c11]: arxiv-2512-19705 — "designing interfaces that rank and reconcile signals"
[^c12]: arxiv-2512-19705 — "a human processing constraint rather than poorer underlying information"
