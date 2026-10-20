---
description: "In SFT on prefixed answers, a few framing tokens such as 'Certainly' carry per-token cross-entropy several times the corpus average, which the paper reads as concentrated gradient."
aliases: ["token-level loss concentration", "per-token loss as gradient diagnostic", "high-loss prefix tokens"]
sources: ["arxiv-2601-01624"]
---
# Framing-token loss concentration

Average cross-entropy over a fine-tuning corpus is one number, and it hides where the loss sits. Logging the loss at every token position during supervised fine-tuning, the paper finds that a handful of opening framing words carry far more loss than the corpus as a whole. In the mathematics runs, "Certainly" averages "12.6 compared to an overall average of 2.07."[^c1] Across the four domains the pattern repeats: "Across all evaluated settings, prefix tokens consistently exhibit substantially higher average loss" than ordinary tokens.[^c2] Table 7 gives the four-domain picture: all-token averages run from 1.80 (coding) to 3.58 (safety), while "Certainly" runs from 9.18 to 12.60 and "Logically" from 10.55 to 11.38.[^c3]

The measurement is simple. For each run the paper records cross-entropy at every token position, averages the loss of a set of frequent prefix tokens over all their occurrences in prefix-included samples and over training steps, and compares that with the corpus-wide average from the same run.[^c4] It is offered as a diagnostic: the authors call per-token loss "an interpretable diagnostic" for how models internalize alignment signals,[^c10] in line with token-level analyses that read the loss position by position rather than as one global scalar.[^c11]

**Reading the loss as gradient.** The paper's step is from loss to update: "higher loss corresponds to larger gradient magnitudes, indicating that these tokens receive disproportionately strong parameter updates during training."[^c5] Stated in general terms, for softmax cross-entropy the gradient with respect to a token's logits is the predicted distribution minus the one-hot target, so a token the model finds unlikely produces a larger logit gradient. That property of the loss is standard, and it is my inference that it carries over to this setting. Gradient size with respect to the parameters also depends on the hidden states feeding the output, and the paper says so: "our experiments do not directly probe layer-wise" representations.[^c6] The authors do log gradient norms at each step, but the per-token comparison they report is loss.[^c7]

The paper treats the concentration as support for a wider picture in which a few salient tokens dominate gradient flow and therefore downstream generation, a reading it calls "consistent with prior" token-level analyses.[^c8] It also cites work on vocabulary frequency imbalance, where loss reduction concentrated on a subset of tokens accounts for a large part of training gains.[^c9]

## Limits

- **Correlation across conditions, not an intervention.** High loss on framing tokens is observed in runs that include prefixes. The text contains no experiment that reweights, masks or removes those tokens and checks whether the downstream effect follows. "Concentration causes the effect" is the paper's hypothesis, not a result.
- **Loss is not gradient influence.** The per-token numbers are cross-entropy values under teacher forcing on GPT-4.1 rewritten targets. They do not measure how much a token moves the weights in the end.
- **Selected tokens.** The four words in Table 7 were chosen as frequent prefix tokens. "Rewritten" and "Revised" do not follow the same pattern everywhere: in coding, "Revised" and "Rewritten" sit at 7.82 and 6.69, below "Certainly" at 10.82. The claim is about framing tokens generally only loosely.
- **Frequency is not controlled.** A token can have high loss because it is unpredictable from context, which is the authors' argument, or because it is rare in the data. The text does not separate these (my reading).
- **No variance.** The text reports no seed count and no spread across runs for the loss values (my reading; neither term appears in the text).
- **Scale.** The numbers come from three distilled models up to 8B. Whether larger models show the same concentration is not tested.

## Related

- [[prefix-retention-in-sft]] — the intervention whose effect this loss profile is offered to explain
- [[stage-level-hallucination-loss-masking]] — also decides which tokens the SFT loss counts, by masking spans rather than reading the loss off them

[^c1]: arxiv-2601-01624 — "12.6 compared to an overall average of 2.07."
[^c2]: arxiv-2601-01624 — "Across all evaluated settings, prefix tokens consistently exhibit substantially higher average loss"
[^c3]: arxiv-2601-01624 — "Average per-token loss values computed on 100%"
[^c4]: arxiv-2601-01624 — "frequently occurring prefix tokens"
[^c5]: arxiv-2601-01624 — "higher loss corresponds to larger gradient magnitudes, indicating that these tokens receive disproportionately strong parameter updates during training."
[^c6]: arxiv-2601-01624 — "our experiments do not directly probe layer-wise"
[^c7]: arxiv-2601-01624 — "we log the per-token loss"
[^c8]: arxiv-2601-01624 — "supports the interpretation consistent with prior"
[^c9]: arxiv-2601-01624 — "loss reduction concentrated on a subset of tokens can account for a large fraction of training"
[^c10]: arxiv-2601-01624 — "as an interpretable diagnostic for understanding how models internalize alignment signals"
[^c11]: arxiv-2601-01624 — "Rather than treating the loss as a single global scalar"
