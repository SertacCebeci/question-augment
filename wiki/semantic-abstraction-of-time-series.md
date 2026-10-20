---
description: "Rule-based abstraction of a time series into merged phase descriptors (trend, transition, fluctuation) gave LLMs better battery-state reports than raw numbers or plots, without retraining."
aliases: ["time-series-to-text report", "semantic translation of signals", "descriptor-sequence serialization", "TimeSeries2Report prompting"]
sources: ["arxiv-2512-16453", "arxiv-2512-05277"]
---
# Semantic abstraction of time series for LLM reading

A numeric signal can reach a language model as raw numbers, as a rendered plot, or as a text description. This note concerns the third form when the text is produced by a fixed rule pipeline before the model reads anything. The mechanism is a reduction: the signal is cut into short windows, each window is labelled on named attributes, identical neighbours are merged, and the result is written out in plain words. The model then reads a sequence of named phases, not the samples.

The pipeline, as reported for lithium-ion operating data, has four steps. First, the series is partitioned. The authors state that "Assigning a single descriptor to an entire sequence is typically inadequate"[^c1] for signals with several charging, discharging and idle phases, and the window is short and fixed: "the temporal window width is fixed at 10 time stamps, determined through expert knowledge and representative".[^c2]

Second, each window is labelled on attributes. The paper separates "Shape attributes capture temporal dynamics, including trend, transition, fluctuation, and outliers"[^c3] from statistical ones such as temporal mean and standard deviation. The labels are words such as increasing, stable or decreasing, assigned by rules, and the authors say these "are grounded in established principles from standard" practice.[^c4]

Third, adjacent windows with the same labels are merged. The reason given is that "slices with identical semantic descriptors are then merged to reduce redundancy and enhance temporal coherence."[^c5] Fourth, the merged labels are phrased as sentences, for example "1~20th time keeps stable, 20~40th time decrease".

Why this should help a reader is the authors' account of raw input. They attribute the weakness of direct numerical prompting to "the inherent difficulty text-based LLMs face when interpreting raw time-series data, particularly in capturing complex temporal features such as trends, transitions, and outliers."[^c6] On the paper's own description, the abstraction does part of the reader's work in advance: the shape the reader would otherwise have to find in a list of numbers is already named when the reader sees it. The same comparison shows the baseline failing on the same series: "baseline Qwen3-14B fails to capture these patterns reliably."[^c7]

The measured effects are on report quality and on one downstream task. Scored by FactScore against expert reports, the TS2R-augmented prompts beat direct numerical prompting, with "FactScore improvements of 6–57%, most with statistical significance" across four LLM backbones and two cell chemistries (LFP and NCA).[^c8] For state-of-charge prediction on a 28-module deployed system, "the TS2R+Qwen3-14B model reduces RMSE by 20% and 74% compared to its corresponding text-based and" vision-based variants.[^c9] The vision route was worse because "pixel-based representations introduce quantization artifacts" that limit fine-grained reading.[^c10] The authors stress that the gain comes "without retraining"[^c11], which is the practical point: no model is changed, only the input.

The same move appears in a driving benchmark for vision-language models, where the abstraction sits beside the frames rather than replacing them. TCogMap runs a deterministic tool over the ego vehicle's pose sequence and passes the model a structured motion summary.[^c16] The authors report that TCogMap "consistently outperforms the baseline + ego pose" variants, and those variants hand the model the same pose numbers as text.[^c14] Their account of the gap is the one this note started from: "the VLM is unable to digest the raw pose data."[^c15] This is the authors' explanation. Because both variants carry the same pose numbers, the comparison isolates the form of the input; my inference is that the gain lies in what the model can use, not in anything the summary adds to the signal.

The mechanism relates to two neighbouring notes. [[capacity-dependent-evidence-modality]] reports the same burden-shifting claim for figures and tables: converting evidence to text before the reader lowers the reader's load, and a weak reader gains most. Here the conversion is rule-based and deterministic, not an LLM summary. The second neighbour is the information bound. A descriptor sequence is a function of the series, so by [[data-processing-inequality]] it cannot carry anything about the signal that the series did not carry. What it changes is what the reader can use. This is my inference from the design, not a claim the paper makes.

## Limits

- The evidence is one domain: battery operating series, with physically meaningful phases (constant-current, constant-voltage, idle). Whether the same abstraction helps on signals without such phase structure is not tested in the text I read.
- The window width and the attribute thresholds were set by expert judgment. The authors give "expert knowledge and representative observations" as the basis for the window. In the parts I read, no ablation varies the window, the thresholds, or removes the merge step, so the contribution of each step is not separated.
- The FactScore judge is itself a language model: an "independent judging LLM (Qwen3-235B-A22B-Instruct-2507) evaluates each sentence pair and assigns a score based on consistency".[^c12] The score measures agreement with expert text as that model reads it, not decision quality.
- The embedding baseline is handicapped by the design of the comparison. The paper says its own embedding model "ChatTS" was weak partly because of its training data, and that "doing so would require substantial computational resources and time" to retrain it on the target data.[^c13] The embedding route was therefore not tried in its tuned form, and the claim that text beats it rests on an untuned baseline.
- The SOC result is one dataset, one horizon (90 minutes of input, prediction at minute 100), and one pair of models for the headline percentages. The abstract's wider claims about decision quality are not established by the parts of the text read here.
- Descriptors are lossy by design. The thresholds decide what counts as a change, so a small trend or a brief transition can disappear in the merge. Whether this loss matters for a given task is a property of that task, and the paper does not map it.
- The video case is a second domain, and it is not a replacement test. The summary is added to the frames, not used in their place. The authors' own blind test still concludes that "visual content remains essential for complete temporal" understanding.[^c17] The summary covers only the ego vehicle, and the authors list "extending temporal cognitive maps to non-ego objects" as future work.[^c18]

## Related

- [[capacity-dependent-evidence-modality]] — the same burden-shifting claim for figures: text before the reader helps a weaker reader, here made by rules rather than an LLM summariser
- [[data-processing-inequality]] — a derived descriptor sequence cannot add information about the signal; the gain is in what the reader can use
- [[perception-context-tradeoff]] — question-agnostic text against raw input, where text can lose detail; here the loss is fixed by the thresholds, not chosen per question
- [[medium-context-sweet-spot-for-numeric-prediction]] — compact, decision-relevant numeric context helps an LLM; a merged descriptor sequence is a compaction of the same kind
- [[symbolic-temporal-representation]] — the same move for dated facts in text: time is rewritten as a fixed symbolic vocabulary before the model reads it; the driving case rewrites motion, not dates

[^c1]: arxiv-2512-16453 — "Assigning a single descriptor to an entire sequence is typically inadequate"
[^c2]: arxiv-2512-16453 — "the temporal window width is fixed at 10 time stamps, determined through expert knowledge and representative"
[^c3]: arxiv-2512-16453 — "Shape attributes capture temporal dynamics, including trend, transition, fluctuation, and outliers"
[^c4]: arxiv-2512-16453 — "These rules are grounded in established principles from standard"
[^c5]: arxiv-2512-16453 — "slices with identical semantic descriptors are then merged to reduce redundancy and enhance temporal coherence"
[^c6]: arxiv-2512-16453 — "particularly in capturing complex temporal features such as trends, transitions, and outliers"
[^c7]: arxiv-2512-16453 — "baseline Qwen3-14B fails to capture these patterns reliably"
[^c8]: arxiv-2512-16453 — "outperforms direct numerical prompting, yielding FactScore improvements of 6–57%, most with statistical significance"
[^c9]: arxiv-2512-16453 — "reduces RMSE by 20% and 74% compared to its corresponding text-based and"
[^c10]: arxiv-2512-16453 — "pixel-based representations introduce quantization artifacts"
[^c11]: arxiv-2512-16453 — "TS2R achieves this performance without any retraining"
[^c12]: arxiv-2512-16453 — "evaluates each sentence pair and assigns a score based on consistency"
[^c13]: arxiv-2512-16453 — "doing so would require substantial computational resources and time"
[^c14]: arxiv-2512-05277 — "consistently outperforms the baseline + ego pose"
[^c15]: arxiv-2512-05277 — "the VLM is unable to digest the raw pose data"
[^c16]: arxiv-2512-05277 — "a deterministic trajectory-analysis tool that produces structured motion summaries that the VLM consumes"
[^c17]: arxiv-2512-05277 — "visual content remains essential for complete temporal"
[^c18]: arxiv-2512-05277 — "extending temporal cognitive maps to non-ego objects"
