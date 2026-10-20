---
description: "A reward that pays for each satisfied criterion favors longer reasoning; a linear length penalty counterweights it, and without one, length either collapses or grows without bound."
aliases: ["overthinking penalty", "reward-driven length inflation", "rubric reward length hacking", "length-counterweighted process reward"]
sources: ["doi-10-48550-arxiv-2608-02831", "doi-10-48550-arxiv-2603-13691"]
---
# Criterion reward length inflation

A reward that scores a response by how many criteria it satisfies has a built-in pull toward length. More criteria can be met by saying more, so a policy trained on such a reward tends to lengthen its reasoning. The audio-reasoning paper states the pressure directly: "satisfying more criteria favors longer reasoning, which risks degenerating into redundant or circular traces".[^c1] It names the exploit as reward hacking "through redundant, circular, or hallucinated reasoning".[^c2]

The counterweight is a length term added to the reward. The authors add "an overthinking penalty that linearly penalizes reasoning length, keeping the trace informative but concise."[^c3] The penalty is one minus the trace's token length divided by a reference length L, and L "normalizes the penalty and sets its scale relative to the other reward terms."[^c4] Taken alone the term favors short traces; combined with the rubric reward it "counterbalances" the pull toward long ones.[^c5]

The two terms are not a tuning detail, because the paper reports what happens when each is missing. With outcome reward only (vanilla GRPO) the response length decays toward near zero, the policy learning to answer tersely. Without the length penalty the length grows without bound and eventually explodes. The full objective holds length in a narrow band, and the authors read the rubric term and the length term as acting in complementary ways: the rubric reward gives "dense credit" to substantive steps, "preventing the degenerate collapse seen under GRPO", while the length term discourages padding.[^c6] The paper says training "converges to a well-calibrated reasoning length", which it reports correlates with the accuracy gains.[^c7]

The mechanism, as I read the paper (my inference, not a result it states), is simple. Any reward that counts satisfied items has a marginal gain from adding items, and a reasoning trace is one of the cheapest places to add them. A judge that checks whether each criterion is met does not by itself charge for the words used to meet it, so the length cost has to be charged somewhere. Read this way, the length term is what keeps a count of satisfied criteria from becoming a measure of how much was written.

The same pull appears when a benchmark, rather than a training reward, scores the answers. QuarkMedBench grades clinical answers with weighted criteria, and its authors report that generative models show Length Bias, which they define as models that "artificially inflate evaluation metrics by generating excessively long texts".[^c8] Unconstrained, Gemini 2.5 Pro averaged 1,935 tokens at 74.57%. Under a length cap of 1,000 (the text says tokens, the figure caption says words) it averaged 943 tokens and scored 62.52%.[^c9] GPT-5.1 moved from 70.90% unconstrained to a score that "maintains a stable score of 69.02% when constrained".[^c10] The authors read the Gemini drop as reliance on "textual expansion, with limited information density per unit of text".[^c11] This is one benchmark and the authors' own ablation over three models. It shows that a score which credits satisfied criteria rewards length differently by model. It does not show how much length costs accuracy in general.

## Limits

- The length curves are shown as a training figure. I did not read whether they are averaged over seeds, so the stability claim rests on one reported run per configuration (my reading).
- The reference length L is a free scale. The paper sets it relative to the other reward terms, and I did not find a sweep over L. The balance point between collapse and explosion is therefore not established here; it presumably depends on L (my inference).
- A linear penalty on token count does not check whether the extra tokens carry information. A longer trace can be honest, so the penalty trades informativeness for brevity by proxy.
- The evidence is one method on three audio reasoning benchmarks (MMAU, MMAR, MMSU), with a single model acting as rubric generator and judge.
- Length is correlated with accuracy in the paper, not shown to cause it.

## Related

- [[rubric-difficulty-evolution]] — the criteria whose satisfaction creates this pull in the first place
- [[judge-then-solve]] — a trajectory-level RL reward that also includes a length term
- [[rubric-complexity-normalized-reward]] — rubric size entering the reward, a different lever from response length

[^c1]: doi-10-48550-arxiv-2608-02831 — "satisfying more criteria favors longer reasoning, which risks degenerating into redundant or circular traces"
[^c2]: doi-10-48550-arxiv-2608-02831 — "which can be exploited to hack the reward through redundant, circular, or hallucinated reasoning"
[^c3]: doi-10-48550-arxiv-2608-02831 — "an overthinking penalty that linearly penalizes reasoning length, keeping the trace informative but concise"
[^c4]: doi-10-48550-arxiv-2608-02831 — "L is a reference length that normalizes the penalty and sets its scale relative to the other reward terms"
[^c5]: doi-10-48550-arxiv-2608-02831 — "Taken in isolation this term favors shorter traces, but in combination it counterbalances the rubric reward, which pushes toward longer traces"
[^c6]: doi-10-48550-arxiv-2608-02831 — "preventing the degenerate collapse seen under GRPO"
[^c7]: doi-10-48550-arxiv-2608-02831 — "converges to a well-calibrated reasoning length"
[^c8]: doi-10-48550-arxiv-2603-13691 — "models artificially inflate evaluation metrics by generating excessively long texts"
[^c9]: doi-10-48550-arxiv-2603-13691 — "Under unconstrained conditions, Gemini 2.5 Pro averages 1,935 tokens per response with an overall score of 74.57%"
[^c10]: doi-10-48550-arxiv-2603-13691 — "maintains a stable score of 69.02% when constrained"
[^c11]: doi-10-48550-arxiv-2603-13691 — "textual expansion, with limited information density per unit of text"
