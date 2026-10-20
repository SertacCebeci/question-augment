---
description: "Building QA from documents newer than every evaluated model's pretraining cutoff makes parametric recall fail, so accuracy gains over no-retrieval prompting measure retrieval and reasoning."
aliases: ["contamination-aware benchmark construction", "time-framed corpus evaluation", "parametric-recall isolation", "clean-room benchmark construction"]
sources: ["arxiv-2602-10210", "arxiv-2601-12632", "arxiv-2601-08611", "doi-10-48550-arxiv-2608-11469", "arxiv-2512-25070", "arxiv-2512-24330", "arxiv-2512-00417", "arxiv-2511-18649", "doi-10-48550-arxiv-2505-10089", "arxiv-2602-00005"]
---
# Post-cutoff corpus benchmark isolation

A question-answering benchmark can reward memory rather than retrieval or reasoning. The work argues that older multi-hop sets (HotpotQA, MetaQA, CWQ, WebQuestions) were built on static sources that sit in LLM pretraining corpora, "making it difficult to isolate the contribution of retrieval and reasoning modules."[^c1]

## The confound, measured

Prompting three models of rising pretraining cutoff on CRAG Movie and Sports questions raised accuracy by up to 102 percent, while a general-reasoning leaderboard moved only 6.7 percent. On fast-changing-fact questions the earliest model scored near zero. The authors read this as pretraining exposure dominating the score.[^c2]

## The isolation mechanism

The construction fixes a document window after the evaluated models' cutoffs. Every document, graph fact and answer is assumed strictly newer than the cutoff, "Consequently, correct answers cannot be recovered via parametric memorization alone."[^c3] Documents come from arXiv within a user-chosen time window, and the window can be regenerated as models change.[^c4] Each question is tied to a knowledge snapshot available up to its issue time, with the needed evidence made explicit as aligned text chunks and a knowledge graph.

## What it showed

Without external knowledge, LLM-only prompting scored 23-40 percent across three domains, even from an 8B model to a 685B one. The authors infer that success is not mainly memorisation or general competence.[^c5] Text RAG added 7-29 absolute points in most model-domain cells. Naive one-hop graph injection could fall below LLM-only prompting because of noise, so the benchmark rewards selective retrieval and not merely more context.[^c6]

The design logic, in my words: the no-retrieval arm becomes a calibrated floor, and the gap above it is attributable to the system rather than the model's memory.

## A second instance: biomedical documents

BioPulse-QA applies the same window idea to clinical text: it kept only drug labels, trial summaries and guidelines "released between January 1, 2024, and February 1, 2025, postdating the December 2023" cutoff of the evaluated models, filtered by publication date, metadata and trial identifiers.[^c7] The authors concede the isolation is partial: "it is not possible to fully eliminate the risk of data contamination, given that" biomedical knowledge is cumulative.[^c8] This supports the limit above that post-cutoff documents can restate older content.

## A third instance: rolling fact-checking claims

VeriTaS applies the isolation to multimodal fact-checking. Static benchmarks draw claims from public sources that LLMs are pretrained on, so "models may implicitly encode both claims and verdicts in their parametric knowledge."[^c9] Its remedy is not a one-time post-cutoff window but quarterly additions through an automated pipeline, so each new split postdates earlier cutoffs. Its Fig. 5 plots error without web search against claim date, with knowledge-cutoff lines. The authors report a performance drop after each model's cutoff; the figure is the only evidence in the extract, and I did not see numbers.[^c10]

## A second route: clean-room construction

Isolation by time is not the only route. A binary-analysis benchmark can instead be written from scratch, so that its targets never existed in public code. The authors take as their premise that "An RE benchmark is valid only if its targets are unknown to the model."[^c11] They argue the bar is stricter there than in other cybersecurity tasks: "In RE, even a coarse degree of leakage is damaging,"[^c12] and in their own results "such data contamination can inflate RE task performance."[^c13] In their ablation, a program derived from public code "can be recovered for roughly $2 in ten minutes."[^c14]

Clean-room provenance removes the shortcut of recall; it does not by itself make a target measure capability. The same ablation shows this, which is why the claim that isolation measures ability also needs target scale (see [[benchmark-target-scale]]).[^c16]

## The window at forecast time

The same window can be set per question rather than per model. A forecasting system built on a static news corpus retrieves only articles up to one month before each question's resolution date; the paper reports that providing retrieved information raises accuracy by roughly 9 to 18 percent "across model families and sizes."[^c17] The isolation here is set by the question's resolution date, not by a model's cutoff. Whether a month of margin is enough to keep out restated outcomes is not tested in the paper (my inference).

## A fourth instance: a multimodal search benchmark

The same window idea appears for images. HR-MMSearch, a benchmark of 4K-resolution images paired with search-driven visual questions, sources its images so that the vision-language models' pretrained knowledge is not the route to an answer: the stated aim is to prevent leakage, and "all images are sourced exclusively from recent 2025 events."[^c18] This is the isolation of the first instance moved to pictures: the window is set by the image's date, not by the model's cutoff. The sections read do not report the evaluated models' knowledge cutoffs, so whether 2025 postdates every model is not shown; the isolation is asserted by construction rather than measured (my inference).

## A third route: templated refresh

A benchmark can keep its question form fixed and refresh the entities inside it. CryptoBench writes its questions from templates in which the entities are "as variables that can be periodically refreshed": token tickers, wallet addresses, transaction hashes and timeframes.[^c19] The authors claim this gives "strong resistance to contamination, as memorizing past question-answer pairs will offer diminishing returns."[^c20]

The isolation here is set on each question's entities, not on the document window or the model's cutoff, so it does not need a fixed date line. It is an argument from how memorization would behave, not a measured leak rate: the sections read do not test whether refreshed questions score lower for models that saw the earlier versions. The claim should be read as a design rationale until such a test exists (my inference).

## A fifth instance: the release hour

An exam can serve as the window itself. The 2026 Korean CSAT mathematics paper keeps its items secret until release and digitizes them at once, relying on the fact that "because test items remain undisclosed until the exam ends, rapid digitization and evaluation immediately after release" keeps them out of training data.[^c21] The authors claim this removes any chance of exposure: "eliminating any possibility of inclusion in model training data."[^c22]

Here the window is an event rather than a cutoff date. The isolation is set by the exam's secrecy until release, so by the authors' design it holds for any model whose training data closed before that release (my inference). The paper reports accuracy across its models, not a measure of leakage, so it does not show the isolation for each model.

## A sixth instance: cross-lingual news

The XRAG benchmark draws its articles from news "between June 1, 2024, and November 30" and states the reason for the window: the articles are "dated after the knowledge cutoff of LLMs such as" GPT-4 and Claude 3.5.[^c23] Its no-retrieval arm is the floor, as in the first instance: "All LLMs perform poorly without retrieval, with accuracy rates falling below 16%."[^c24] The window is set by the article date, and the paper does not report a check that the evaluated models had not seen the same news; the isolation is asserted by the choice of window (my inference).

## A seventh instance: a post-cutoff query-writing set

AutoBool, a reinforcement-learning system that writes Boolean search queries for medical systematic reviews, builds its test window from the publication date of the review topics. Its primary model, Qwen3, has no officially published cutoff, so the authors "confirmed via direct model queries" that its knowledge runs to October 2024, and they keep only topics published after November 1, 2024.[^c26][^c25] The stated purpose is "out-of-distribution evaluation by ensuring topics were unseen during LLM pretraining."[^c28] The resulting set, PubTemp, is 1,000 sampled topics, kept small partly to limit the cost of evaluating commercial models.[^c27]

The window here is set by a topic's publication date against a cutoff the authors measured by asking the model, not by a document source. What it isolates is the query-writing model's memory of the topic. The retrieval target, PubMed, is not isolated by the window (my inference).

## Limits

- The PubTemp cutoff is measured for one model. The paper evaluates GPT-4o and O3 on the same topics, and the parts read do not give their cutoffs, so the window may not isolate those models (my inference).
- The VeriTaS evidence is a smoothed single-run plot, and claim mix also drifts over time (more AI-generated media, more video), so cutoff and difficulty are confounded (my inference).
- The isolation is an assumption stated in the problem definition, not verified per question. Post-cutoff papers can restate older findings, so some parametric leakage is possible (my inference).
- It rests on public cutoff dates; the paper's own table lists approximate cutoffs, and fine-tuning or search-enabled models would break the premise.
- The domains are arXiv science only (AI, policy, bioinformatics); transfer to everyday questions is untested.
- The clean-room route keeps its isolation by withholding the targets: "To preserve the contamination resistance of SRE-Bench, we do not publicly release the benchmark" binaries or tasks.[^c15] Outside parties can check results only through the authors' evaluation service, not against the targets themselves (my inference).
- Questions are generated automatically with an automated quality filter; the work does not show human-validated answer correctness here.
- The motivating example uses three different model families, so reasoning ability and cutoff are not cleanly separated.
- A release-hour window isolates this year's items, not the mathematics behind them: past exams and their solution methods stay public, so the restatement limit above applies (my inference). The paper does not report its models' training cutoffs (my inference from the text).

## Related

- [[parametric-knowledge-gates-retrieval-noise-damage]] — the noise damage from naive graph injection depends on what the model already knows
- [[reference-answer-defect-audit]] — another way benchmark validity is eroded
- [[evidence-chain-question-generation]] — generating questions from explicit evidence chains
- [[hop-depth-difficulty-with-entropy-check]] — hop depth as a difficulty axis
- [[benchmark-target-scale]] — the other requirement for a benchmark that measures capability: targets large enough to separate agents, which isolation from pretraining does not supply

[^c1]: arxiv-2602-10210 — "making it difficult to isolate the contribution of retrieval and reasoning modules."
[^c2]: arxiv-2602-10210 — "These results indicate that benchmark performance can be dominated by pretraining exposure rather than retrieval or reasoning ability, obscuring genuine methodological progress."
[^c3]: arxiv-2602-10210 — "Consequently, correct answers cannot be recovered via parametric memorization alone."
[^c4]: arxiv-2602-10210 — "we select document windows that postdate the"
[^c5]: arxiv-2602-10210 — "This trend indicates that HybridRAG-Bench questions cannot be"
[^c6]: arxiv-2602-10210 — "Notably, naïve KG-based augmentation can degrade performance relative to LLMonly prompting."
[^c7]: arxiv-2601-12632 — "released between January 1, 2024, and February 1, 2025, postdating the December 2023"
[^c8]: arxiv-2601-12632 — "it is not possible to fully eliminate the risk of data contamination, given that"
[^c9]: arxiv-2601-08611 — "models may implicitly encode both claims and verdicts in their parametric knowledge, undermining"
[^c10]: arxiv-2601-08611 — "demonstrating a performance"
[^c11]: doi-10-48550-arxiv-2608-11469 — "An RE benchmark is valid only if its targets are unknown to the model."
[^c12]: doi-10-48550-arxiv-2608-11469 — "In RE, even a coarse degree of leakage is damaging"
[^c13]: doi-10-48550-arxiv-2608-11469 — "such data contamination can inflate RE task performance"
[^c14]: doi-10-48550-arxiv-2608-11469 — "a program derived from public code can be recovered for roughly $2 in ten minutes"
[^c15]: doi-10-48550-arxiv-2608-11469 — "To preserve the contamination resistance of SRE-Bench, we do not publicly release the benchmark"
[^c16]: doi-10-48550-arxiv-2608-11469 — "being clean-room provenance by itself does not make a target hard"
[^c17]: arxiv-2512-25070 — "across model families and sizes"
[^c18]: arxiv-2512-24330 — "all images are sourced exclusively from recent 2025 events"
[^c19]: arxiv-2512-00417 — "as variables that can be periodically refreshed"
[^c20]: arxiv-2512-00417 — "strong resistance to contamination, as memorizing past question-answer pairs will offer diminishing returns"
[^c21]: arxiv-2511-18649 — "because test items remain undisclosed until the exam ends, rapid digitization and evaluation immediately after release"
[^c22]: arxiv-2511-18649 — "eliminating any possibility of inclusion in model training data."
[^c23]: doi-10-48550-arxiv-2505-10089 — "between June 1, 2024, and November 30"
[^c24]: doi-10-48550-arxiv-2505-10089 — "All LLMs perform poorly without retrieval, with accuracy rates falling below 16%."
[^c25]: arxiv-2602-00005 — "we select topics published after November 1, 2024, to minimize overlap"
[^c26]: arxiv-2602-00005 — "we confirmed via direct model queries that its"
[^c27]: arxiv-2602-00005 — "reducing the expense of evaluating commercial models"
[^c28]: arxiv-2602-00005 — "We introduce the PubTemp set to enable fair, out-of-distribution evaluation"
