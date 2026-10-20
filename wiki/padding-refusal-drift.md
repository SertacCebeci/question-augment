---
description: "Under long-context padding, an agent's refusal rate can rise for one model and fall for another at the same length, so refusal rate alone does not measure safety."
aliases: ["refusal shift under long context", "context-induced refusal change", "refusal rate drift with context length"]
sources: ["arxiv-2512-02445"]
---
# Padding-induced refusal drift

A refusal rate is usually read as a safety signal: the share of harmful requests an agent declines. Long context can move that share, and in the study that measured it, it moved in opposite directions for different models at the same length. The work extends the AgentHarm benchmark with controlled padding of 1K to 200K tokens, placed before or after the task, and tests four padding kinds: random tokens, coherent non-relevant text, coherent relevant text, and other task descriptions.[^c1]

The shift is not one signed effect. For GPT-4.1-nano the refusal rate was lowest with no padding and then rose: it "starts to quickly increase" after 10K tokens and "reaches nearly 40% for 200K" random padding.[^c2] For Grok 4 Fast the starting point was high, an 80% refusal rate, and it fell: the authors write that it "gradually decreases after 5K tokens, becoming half as high" at 200K.[^c4] The paper summarizes the pattern as "GPT-4.1-nano and Grok 4 Fast show opposite behavior with random padding."[^c3] On these four models the effect reads as a property of the model-and-length pair rather than a general tendency of long context to make agents more or less cautious; that reading is mine, since the paper tests too few models to decide it.

The authors do not identify a mechanism. Their reading is that "We think these refusals could be triggered by something other than safety training."[^c5] They draw the consequence for measurement: "This questions the usefulness of refusal rate as a safety metric" when no trigger is identified.[^c6]

Refusal and capability are separate quantities here. GPT-4.1-nano's refusal rate rose, but its benign-task performance also fell, and the authors take this as showing the refusal rise cannot be the whole story: there is a "similar picture for benign tasks, where performance was cut" in half.[^c7] A refusal count also does not say when the refusal happened. The paper separates an immediate refusal, decided from the task description, from a delayed one, which comes "after beginning execution."[^c8][^c9] A delayed refusal can follow information gathering or API calls that already took place, so, on this reading (mine, not a measured result), a low refusal rate could hide actions taken before the agent stopped.

## Limits

The evidence is one benchmark extension: the public AgentHarm test set (176 samples from 44 tasks) restricted to its easiest variant, which the authors say makes their "results represent an upper bound on performance."[^c10] Four models were tested, chosen partly for budget, and they were reached through different API providers, which "may introduce providerlevel safety filters that we cannot fully disentangle from basemodel behavior."[^c11]

Refusals are themselves scored by an LLM judge, which received "small changes" to its prompt and underlying model, so the refusal rate carries a second measurement layer that is not held fixed across models.[^c12] The paper's explanations, such as attention across distant tokens or training on short sequences, are its own hypotheses; no trigger for the refusal change was isolated, and nothing shows that the direction would hold at other lengths, padding kinds or task categories.

## Related

- [[retrieval-induced-safety-degradation]] — retrieved text lowers a refusal threshold in the one direction reported there; here the direction depends on the model.
- [[search-induced-abstention-degradation]] — tool access lowers abstention on unanswerable questions, another way a context change moves refusal-like behavior.
- [[refusal-shortcut-learning]] — a candidate for the unidentified trigger, if refusals bind to surface features of the prompt rather than to intent.
- [[judge-scored-refusal-confidence]] — how a refusal is turned into a score, the layer this study also depends on.
- [[effective-context-length]] — the capacity side: the same long contexts also degrade task performance.

[^c1]: arxiv-2512-02445 — "we experiment with four context padding types"
[^c2]: arxiv-2512-02445 — "starts to quickly increase"
[^c3]: arxiv-2512-02445 — "GPT-4.1-nano and Grok 4 Fast show opposite behavior with random padding."
[^c4]: arxiv-2512-02445 — "gradually decreases after 5K tokens, becoming half as high"
[^c5]: arxiv-2512-02445 — "We think these refusals could be triggered by something other than safety training."
[^c6]: arxiv-2512-02445 — "This questions the usefulness of refusal rate as a safety metric"
[^c7]: arxiv-2512-02445 — "similar picture for benign tasks, where performance was cut"
[^c8]: arxiv-2512-02445 — "distinguish two failure modes"
[^c9]: arxiv-2512-02445 — "delayed (after beginning execution)"
[^c10]: arxiv-2512-02445 — "our results represent an upper bound on performance"
[^c11]: arxiv-2512-02445 — "we cannot fully disentangle from basemodel behavior"
[^c12]: arxiv-2512-02445 — "we provide small changes in the prompt and the underneath"
