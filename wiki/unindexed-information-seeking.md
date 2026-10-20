---
description: "Questions whose needed evidence lies beyond search-engine results (in files, dynamic pages, filters) collapse agent accuracy; reachable action space bounds success and the model bounds the rest."
aliases: ["UIS", "UIS-QA", "unindexed information", "deep-web information seeking"]
sources: ["doi-10-48550-arxiv-2603-08117"]
---
# Unindexed information seeking

A question is **unindexed-information-seeking** (UIS) when answering it needs some context that is not in the search engine's snippets or one-step crawls of its results, and the answer cannot be inferred from the indexed part alone.[^c1] Formally, indexed information is the set of snippets plus one-step crawls of the pages a search engine returns; everything else on the web is unindexed. A question Q is UIS if its required context has a non-empty unindexed part and the indexed part alone does not imply the answer.[^c1] In practice an agent only issues a few queries and visits a few top pages, so the practically reachable indexed set is much smaller than the ideal one, which makes the target more likely to sit in the unindexed remainder.[^c2]

## What it does to answering

The authors built UIS-QA, 110 expert-written questions with short deterministic answers. Annotators navigated official sites by multi-round clicks, option selection, filters, in-site search and file downloads, then wrote a question from the page reached, at most two per site.[^c3] Strong search agents fell sharply: scores above 70% on GAIA dropped to 23.6% and 25.5% on UIS-QA for two systems.[^c4] The authors' own agent, with a ~30B backbone trained by supervised then rejection-sampling fine-tuning, reached 27.27%.[^c5]

Two bounds are proposed. The action space sets the upper bound: if search-engine-only agents cannot download files or operate a browser, UIS questions are theoretically unsolvable for them. Model capability sets the lower bound, deciding whether the agent chooses well inside a large action space.[^c6] Larger action spaces also enlarge the search space, so the bottleneck shifts to the underlying LLM; systems of the same framework type and similar action spaces differed by up to about 17-21 points.[^c7]

## Failure modes

Tracking whether an agent retrieves and then visits the root website of the gold source gives a decomposition. Missing retrieval of the root site makes the problem impossible; retrieving it but choosing the wrong source is the second dominant failure; and a substantial share fail even after reaching the right site, because of long multi-step navigation, filter changes and repeated back-and-forth.[^c8] Correct answers without ever touching the gold site were rare, from remembered URLs or third-party mirrors.[^c9]

Training changed behaviour: correct trajectories first used more tools, then fewer as navigation became targeted, while incorrect trajectories showed monotonically more tool calls with no convergence.[^c10]

## Limits

- The benchmark is small (110 items), and 27% remains low; the authors call it far from satisfactory.[^c11]
- The index is approximated with one search engine (Google Serper); "unindexed" is relative to that engine and the queries the agent issued, not an absolute property of the page (this reading is mine, from the definition in eq. 4-6).
- The claim that action space is the upper bound and the model the lower bound is the authors' hypothesis, not an ablation isolating each.
- Questions were written from pages the annotators had reached, so the mix of difficulty may differ from questions real users ask.

## Related

- [[search-effort-accuracy-decoupling]] — more tool calls on failing trajectories did not buy accuracy, as here
- [[retrieval-utilization-gap]] — reaching the source is not the same as using it; the RBB failures echo this
- [[agentic-abstention]] — the figure notes failing agents either refuse or hallucinate when evidence is missing

[^c1]: doi-10-48550-arxiv-2603-08117 — "If the required unindexed information is not empty and the correct answer z cannot be inferred from C (I) , then the Q is a UIS problem."
[^c2]: doi-10-48550-arxiv-2603-08117 — "is much smaller than II, making it more likely that"
[^c3]: doi-10-48550-arxiv-2603-08117 — "For each website, we restrict the annotators to compose a"
[^c4]: doi-10-48550-arxiv-2603-08117 — "drop to"
[^c5]: doi-10-48550-arxiv-2603-08117 — "UIS-Digger achieves the highest score of 27.27% on the UIS-QAbenchmark"
[^c6]: doi-10-48550-arxiv-2603-08117 — "making UIS problems theoretically unsolvable."
[^c7]: doi-10-48550-arxiv-2603-08117 — "The main bottleneck, therefore, shifts to the underlying LLM’s fundamental ability."
[^c8]: doi-10-48550-arxiv-2603-08117 — "Missing retrieval (RRR) and knowledge sourcing (RBR) are two dominant failure modes."
[^c9]: doi-10-48550-arxiv-2603-08117 — "their rarity indicates they do not fundamentally mitigate the UIS"
[^c10]: doi-10-48550-arxiv-2603-08117 — "Incorrect trajectories, however, show a monotonic increase"
[^c11]: doi-10-48550-arxiv-2603-08117 — "remains far from satisfactory"
