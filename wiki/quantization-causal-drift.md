---
description: "Weight quantization to INT8 or NF4 moved an 8B model's causal accuracy by under one point on Pearl's ladder, with intervention the most variable rung; the test sat near chance and used one model."
aliases: ["quantization-induced causal drift", "QCD", "compressed causal reasoning", "precision effect on causal reasoning"]
sources: ["arxiv-2512-13725"]
---
# Quantization-induced causal drift

Quantization stores a model's weights at fewer bits. INT8 uses a uniform scale, and NF4 uses a 4-bit NormalFloat code "optimized for transformer weight distributions".[^c1] The work loads the models with BitsAndBytes and keeps computation in BF16, so that the only change is the stored weight precision: "computations retained in BF16 to isolate the effects of weight precision."[^c2]

The quantity the work defines is a drift per rung. For a quantization mode m and rung r, the drift is the BF16 accuracy minus the quantized accuracy, Acc_r(BF16) − Acc_r(m), and the stated purpose is that it "isolates causal-level degradation relative to the full-precision baseline."[^c3] Read this way, a drift is a difference inside one model across precisions, so it separates the effect of compression from the model's general competence on the items.

On 3,000 stratified CLadder queries with zero-shot greedy answers, the work finds that "Across all precision settings, causal accuracy remains stable, with differences below 0.5%."[^c4] Two details complicate a flat reading. Intervention (Rung 2) has the largest spread across precisions, and NF4 is not uniformly worse: "NF4 slightly outperforms BF16 on Rung 2, indicating that aggressive 4-bit quantization does not systematically degrade" intervention-level reasoning at this scale.[^c5] Summed up, the work describes causal reasoning as "largely stable under aggressive compression, with overall degradation below one percentage point."[^c6]

The work reads this stability as preserved internal structure, but it did not measure internal structure. Its analysis "focuses on downstream causal reasoning behavior rather than internal weight distortion."[^c7] So what is established is that answers did not move; that the representations are preserved is the work's interpretation.

## Limits

The accuracy itself sits near chance. Overall zero-shot accuracy is 0.508 to 0.512 at every precision. The text does not give the answer format of the items; if they are yes/no, the stable number is a stable coin flip, and a drop from a floor is hard to see (my inference). The companion benchmark shows the same problem in starker form: CRASS accuracy is constant at 0.267, "with performance remaining near chance even under full-precision inference."[^c8] A drift test cannot register damage to a competence the model does not show at full precision.

Overlapping intervals are the work's test of "statistically unchanged",[^c9] which is a weaker claim than equivalence: intervals that overlap do not show that two values are the same (my inference). The work also reports the drift only at the rung level and for query types, with no interval for the per-type differences in the text read.

The model is one 8B model, Llama-3-8B, and "Larger-scale models may exhibit different robustness or drift characteristics under quantization".[^c10] The study varies only weight precision; activation quantization is not in the design (my reading of the BF16-compute setup). The decoding is greedy with no chain-of-thought, and the work notes that such a choice "may interact differently with quantization and retrieval augmentation."[^c11]

## Related

- [[rung-stratified-causal-accuracy]] — the per-rung breakdown that makes the drift readable; the spread the drift reveals is in Rung 2, not in the mean.
- [[short-form-check-blindness-to-open-ended-bias]] — another quantization study in which a short-form check certifies less than the property it stands in for; the same question about what a closed measurement can see applies here.
- gold-fact-injection-gain — the NF4 model was also tested with benchmark gold answers injected as facts, a separate condition from the drift.

[^c1]: arxiv-2512-13725 — "optimized for transformer weight distributions"
[^c2]: arxiv-2512-13725 — "computations retained in BF16 to isolate the effects of weight precision."
[^c3]: arxiv-2512-13725 — "which isolates causal-level degradation relative to the full-precision baseline."
[^c4]: arxiv-2512-13725 — "Across all precision settings, causal accuracy remains stable, with differences below 0.5%."
[^c5]: arxiv-2512-13725 — "slightly outperforms BF16 on Rung 2, indicating that aggressive 4-bit quantization does not systematically degrade"
[^c6]: arxiv-2512-13725 — "largely stable under aggressive compression, with overall degradation below one percentage point."
[^c7]: arxiv-2512-13725 — "our analysis focuses on downstream causal reasoning behavior rather than internal weight distortion."
[^c8]: arxiv-2512-13725 — "with performance remaining near chance even under full-precision inference."
[^c9]: arxiv-2512-13725 — "This overlap indicates that causal accuracy is statistically unchanged under quantization at the 8B scale."
[^c10]: arxiv-2512-13725 — "Larger-scale models may exhibit different robustness or drift"
[^c11]: arxiv-2512-13725 — "which may interact differently with quantization and retrieval augmentation"
