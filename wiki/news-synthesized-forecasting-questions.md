---
description: "Open-ended forecasting questions can be mass-produced from dated news: one model writes questions about each article's events, another keeps only in-article, forward-looking, resolvable ones."
aliases: ["news-derived forecasting questions", "automated forecasting question generation", "question synthesis from news articles"]
sources: ["arxiv-2512-25070"]
---
# News-synthesized forecasting questions

Forecasting questions for training have mostly come from prediction markets. The paper names three problems with that source: the questions are human-made and so few in number, most have binary outcomes (a 50 percent guessing baseline), and each platform skews toward its own topics.[^c1] The alternative is to write questions from daily news, which "covers a large number of salient events every day".[^c2]

## Mechanism

The pipeline has three stages, each run by a language model.

1. **Sample creation.** For each article, a sample-creator model is asked "to generate up to three diverse forecasting samples." Each sample holds a question, a short background, resolution criteria with a resolution date, a short answer taken from the article, and a link to the source.[^c3] The answer is "usually a name or location", kept short and non-numeric.[^c4] The resolution date is a guess that can be wrong, because "sometimes news articles talk about past events, or report an event late."[^c5]
2. **Selection.** A second model checks that the question-answer pair is "fully based on information in the source article", is forward-looking, and has a definite answer. If several questions survive for one article, it keeps the best one.[^c6]
3. **Leakage editing.** The selector rewrites any span of the title, background or criteria that reveals the answer. A string match then discards what remains. This stage is described in [[answer-string-leakage]].

The scale is what the paper claims as the contribution. From about 248,000 deduplicated articles from five outlets, the sample creator yields roughly 745,000 candidate samples. Most are rejected: 60 percent of candidates are invalid, "because the article does not unambiguously resolve the question to the given answer."[^c7] The result is a training set of "∼ 50,000 open-ended forecasting questions", as the paper's own summary puts it.[^c8] The paper says the recipe "can continually ingest news articles" and so can be rerun as new articles arrive.[^c9]

Filtering matters for the trained model, not just for tidiness. Training Qwen3-8B on unfiltered questions makes it worse, and the leakage edit alone recovers performance. Using all filters "leads to both higher accuracy and Brier score, in one-third the data and training steps."[^c10]

## Limits

- Resolution dates are the weakest link. The paper does not fix them for training data, "due to cost constraints", so some questions resolve on an event already reported.[^c11]
- The source is news only, so the distribution is biased. The paper writes that "we only use news to create forecasting questions, which leads to a distributional bias", and that events reported late, such as scientific breakthroughs, may be easier to "predict".[^c12]
- Many major outlets (Reuters and AP are named) have "disallowed scraping even for CommonCrawl", so the source set is narrower than the news universe.[^c13]
- The question quality of the training recipe is not measured against human judgment. The validation set was made with a stronger model (o4-mini-high) at about ten times the cost and kept about 40 percent of articles; the training set used a cheaper generator and its yield was not compared.
- The filter ablation uses one model family, one run per condition, and a set in which the best condition also uses a different source (Forbes).
- Long-form forecasts and numeric answers are excluded, so the recipe produces only short named answers.

## Related

- [[answer-string-leakage]] — the failure the editing stage exists to remove, and how it was measured
- [[free-form-brier-score]] — the score these questions are graded with
- [[post-cutoff-corpus-benchmark-isolation]] — the same goal of building questions from documents newer than the model's knowledge, applied to QA benchmarks
- [[resolution-time-outcome-supervision-of-forecasts]] — another forecasting source where the resolved outcome is the label, here built from synthetic questions with a frozen resolver

[^c1]: arxiv-2512-25070 — "mostly consist of binary yes or no questions"
[^c2]: arxiv-2512-25070 — "which covers a large number of salient events every day"
[^c3]: arxiv-2512-25070 — "to generate up to three diverse forecasting samples"
[^c4]: arxiv-2512-25070 — "non-numeric (usually a name or location)"
[^c5]: arxiv-2512-25070 — "sometimes news articles talk about past events, or report"
[^c6]: arxiv-2512-25070 — "fully based on information in the source article"
[^c7]: arxiv-2512-25070 — "because the article does not unambiguously resolve the question to the given answer"
[^c8]: arxiv-2512-25070 — "open-ended forecasting questions for training"
[^c9]: arxiv-2512-25070 — "this pipeline can continually ingest news articles"
[^c10]: arxiv-2512-25070 — "in one-third the data and training steps"
[^c11]: arxiv-2512-25070 — "steps to fix resolution dates due to cost constraints"
[^c12]: arxiv-2512-25070 — "we only use news to create forecasting questions, which leads to a distributional"
[^c13]: arxiv-2512-25070 — "have disallowed scraping even for CommonCrawl"
