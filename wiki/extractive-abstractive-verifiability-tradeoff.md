---
description: "Along a spectrum from extractive to abstractive cited answers, perceived utility rises while citation coverage falls and verification time grows, so the right operating point depends on stakes."
aliases: ["extractive-abstractive spectrum", "verifiability-utility trade-off", "cited generation operating points"]
sources: ["doi-10-48550-arxiv-2411-17375"]
---
# Extractive-abstractive verifiability trade-off

An answer that cites sources can sit at different points on a spectrum defined by how far each sentence departs from the quotes it cites. The work defines five operating points. Extractive output is a set of source snippets. A quoted generation weaves word-for-word quotes inline, marked off from unquoted words. A paraphrased generation rewords the cited quotes without removing or adding information. An entailed generation may reword, remove and logically contract, but adds no claim beyond the cited quotes. An abstractive generation may carry claims that are not cited at all.[^c1]

The answerer's choice of point sets what the asker can check. Quoted text only needs to be checked for context, whereas for more abstractive points the user must also confirm that the sentence was faithfully rewritten from the source.[^c2]

## What was measured

Human evaluation of seven systems over four query distributions found that as generations become more abstractive, fluency and perceived utility rise while verifiability degrades. Perceived utility rose by over 200% and citation coverage fell by over 50% between extractive and a GPT-4 plus search-API abstractive system. Humans took three times longer to verify cited sentences from that system than from quoted generations.[^c3] Rewording a quoted generation into a paraphrased one raised time-to-verify by over 40%.[^c4]

Citation precision stayed at 95%-100% across the reference points but was significantly lower for post-hoc citation systems. The authors attribute the difference to choosing quotes to cite first and then generating from them ("attribute first, then generate").[^c5] The deployed Gemini system was Pareto-dominated by entailed generations: similar fluency and utility, over 80% lower coverage.[^c3] The authors warn that high utility with low coverage may lead users to believe insufficiently supported information.[^c6]

A survey of 200 people found that users prefer search engines for high-stakes questions and LLMs for lower-stakes research tasks.[^c7] The authors draw from this that no single point suits every application. High-stakes settings with dispersed information favor the extractive and quoted points, and low-stakes settings in need of refinement favor abstractive ones.[^c8]

## Limits

Utility is perceived utility rated by annotators, not measured task outcome; the authors note it does not necessarily measure correctness (this is my reading of their caveat). The reference implementations are the authors' own, so the trade-off curve may shift with other systems. The mapping of settings to ideal points is the authors' recommendation, not tested with outcome data. The survey is self-reported preference.

## Related

- [[abstention]] — the paper also reports abstention modes; declining to answer is another way to protect verifiability
- [[question-based-summary-evaluation]] — another way of judging whether generated text is supported by its source
- [[deferred-answer-exposure]] — both concern how an answer's form changes what the asker can do with it

[^c1]: doi-10-48550-arxiv-2411-17375 — "Extractive Output: An extractive output is a set of quotes from the sources themselves."
[^c2]: doi-10-48550-arxiv-2411-17375 — "users only need to ensure the quote is not taken out of context from the source when verifying a cited quote."
[^c3]: doi-10-48550-arxiv-2411-17375 — "perceived utility increases by over 200% and citation coverage decreases by over 50% between"
[^c4]: doi-10-48550-arxiv-2411-17375 — "simply rewording quoted generations to be paraphrased generations increases T2V"
[^c5]: doi-10-48550-arxiv-2411-17375 — "Citation precision is relatively similar (95%-100%) across the reference OP generations"
[^c6]: doi-10-48550-arxiv-2411-17375 — "convincing generations may lead users to"
[^c7]: doi-10-48550-arxiv-2411-17375 — "users prefer search engines to LLMs without citations, like ChatGPT and"
[^c8]: doi-10-48550-arxiv-2411-17375 — "there is no one-size-fits-all operating point"
