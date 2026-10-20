---
description: "Topical variation in a user's prompt sequence is counted from a binarized prompt-similarity matrix: exploration is a new topic at the next prompt, exploitation a run of similar prompts."
aliases: ["P(variation)", "topic-switch probability in prompting", "exploration rate in prompt sequences", "prompt-sequence exploration-exploitation"]
sources: ["doi-10-48550-arxiv-2312-00233"]
---
# Prompt-sequence topical variation

A user who submits a series of prompts to an image generator walks through a space of topics. Consecutive prompts that share most of their tokens are exploitation of one concept; consecutive prompts that do not are exploration of a new one. The measure makes this countable. For every pair of a user's prompts the paper takes the Jaccard index over token sets, the intersection over the union of the two token sets.[^c1] The resulting similarity matrix is then binarized: cells above the matrix average become 1, the rest 0. Blocks of 1-valued cells adjacent to the diagonal are runs of mutually similar prompts, and a boundary between two blocks is a pair of consecutive prompts whose binarized similarity is zero.[^c2] The number of topical variations is the number of blocks minus one, which "ranges from one (when all prompts are similar) to the number of prompts minus one (when each prompt is dissimilar from all others)."[^c3] Dividing by the number of transitions gives a per-user probability that the next prompt enters a new topic (my reading of the paper's Equation 3, which is garbled in the text I read).

Read this way, the measure separates two kinds of user. On Stable Diffusion, the paper reports that "the majority tend towards exploration, with 63% changing topics more often than" not, and 16% change topic at every prompt.[^c4] On Pick-a-Pic, "almost all Pick-a-Pic users change topic less than once every five prompts, and 26% of them never do."[^c5] The timing differs too. On Stable Diffusion the exploratory share falls with experience, "from approximately 0.9 at the second prompt to around 0.5 after 15" prompts,[^c6] which the authors read as users gaining confidence in prompt variation within a topic. On Pick-a-Pic the probability of a topic transition stays flat over the observed timeframe. At distance d = 1 the prompt similarity on Pick-a-Pic is "being approximately three times greater than that in Stable Diffusion," so a Pick-a-Pic user needs several more iterations before a topical shift of the size a Stable Diffusion user makes in one step.[^c7]

The paper's working hypothesis links the measure to creativity: "we adopt the working hypothesis that exploration is loosely yet positively associated with" creativity, so that a user who submits more diverse prompts is taken to create a wider range of content.[^c8] The measure itself counts topical change in text. It does not measure creativity, image quality, or what the user wanted.

## Limits

The similarity is token overlap. Two prompts that name the same subject in different words read as a topic change; two that differ only in one noun read as exploitation. The binarization threshold (the matrix mean) is set per user and is a heuristic; the block-counting rule is a heuristic too. The text I read reports no validation of these choices against human judgements of topic change.

The link to creativity is an assumption the paper states, not a result it measures. The exploration result is also observational. Two platforms were compared, and the authors say plainly that they could not control for "the inability to control for external factors such as differing user attitudes towards prompting, art, or technology," and that "it is necessary to extend our study to a broader range of" platforms.[^c9] The samples were matched on prompt count, not on users' goals or experience. The logs come from one launch month per platform, so early adopters dominate.

## Related

- [[prompt-revision-bypass]] — the interface feature under which this measure fell on Pick-a-Pic
- [[exploration-signature-decomposition]] — exploration in the bandit sense, over arms chosen; here exploration is over topics written in text, so the two share a word and little else
- [[questioning-diversity]] — diversity measured over a set of questions, where this note measures change along one user's ordered sequence of prompts

[^c1]: doi-10-48550-arxiv-2312-00233 — "the intersection over the union of the set of tokens composing"
[^c2]: doi-10-48550-arxiv-2312-00233 — "we first binarize the similarity matrix"
[^c3]: doi-10-48550-arxiv-2312-00233 — "from one (when all prompts are similar) to the number of prompts"
[^c4]: doi-10-48550-arxiv-2312-00233 — "with 63% changing topics more often than"
[^c5]: doi-10-48550-arxiv-2312-00233 — "topic less than once every five prompts, and 26% of them never do."
[^c6]: doi-10-48550-arxiv-2312-00233 — "from approximately 0.9 at the second prompt to around 0.5 after 15"
[^c7]: doi-10-48550-arxiv-2312-00233 — "being approximately three times greater than that in Stable Diffusion"
[^c8]: doi-10-48550-arxiv-2312-00233 — "we adopt the working hypothesis that exploration is loosely yet positively associated with"
[^c9]: doi-10-48550-arxiv-2312-00233 — "inability to control for external factors such as differing user attitudes towards prompting, art, or technology"
