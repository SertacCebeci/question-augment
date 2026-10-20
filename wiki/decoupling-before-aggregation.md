---
description: "Agent memory is organised by first splitting a similar history into distinct facts, then grouping them, so retrieval keeps the details that summary-first hierarchies blur."
aliases: ["decouple-then-aggregate memory", "revisable hierarchical agent memory"]
sources: ["doi-10-48550-arxiv-2602-02007"]
---
# Decoupling before aggregation

Agent memory is a different retrieval problem from a document corpus. The stored history is one coherent stream in which many spans are near-duplicates, so flat top-k similarity returns context that is relevant but repetitive, and summary-first hierarchies compress the details that separate one candidate from another: "while blurring the subtle details that distinguish one"[^c1] candidate from the next. The proposed remedy is a change of order: "of decoupling before aggregation: the system should first isolate reusable facts"[^c2], updates and distinguishing details, and only then organise them for access.

The construction has three steps. Raw messages are cut into contiguous local segments. Each segment is then decoupled into memory components, each one a reusable fact, constraint, attribute, relation or state update, with a link kept back to its source segment: "each segment is then decoupled into memory components that isolate reusable facts"[^c3]. Only after that are components aggregated into groups. The grouping score adds a sparsity term, which favours balanced group sizes through the inverse of expected within-group scanning cost, and a semantic term, which rewards cosine coherence between components and their group centroids. The objective is one that "balances sparsity and semantic faithfulness"[^c4], because it must avoid two failures the paper names. "If groups are too broad, retrieval becomes less" discriminative, while fragmented groups scatter related evidence across many small units.

The structure is revisable, and this is the part the paper treats as distinct from ordinary incremental memory. A new component joins its nearest group if the similarity clears a threshold, and otherwise opens a new group. "Groups that become too large or internally incoherent are considered for splitting"[^c5], and small or isolated groups are considered for merging, with whichever operation most improves the objective. The paper contrasts this with insertion into existing clusters, which "remains distinct from retroactive reorganisation"[^c6].

Retrieval then runs top-down over the structure. Stage I selects a backbone of groups and components by a greedy trade-off between newly covered neighbours in a kNN graph over groups and query similarity, so the set is "complementary high-level units, rather than repeatedly retrieving near-duplicate evidence by pure"[^c7] similarity ranking. Stage II descends to segments and raw messages only while the reader is still uncertain. "A segment is included only if it yields a positive marginal reduction"[^c8] in the reader's uncertainty, which the implementation measures "via predictive entropy"[^c9]. In my reading, the retrieval has the same two-pass shape as [[coarse-to-fine-evidence-zoom]], but the stopping test is a change in the reader's uncertainty, not a fixed depth.

What the paper measured. On LoCoMo with Qwen3-8B, the ablation starts from flat raw chunks and moves to the decoupled structure. Average BLEU/F1 goes "from 27.95/36.48 for Naive RAG to 31.81/40.77"[^c10] with memory structuring alone, and the paper reads this as retrieval over decoupled units being "more effective than retrieval over flat raw chunks, even with basic similarity matching"[^c11]. Adding both retrieval stages gives the best average and the lowest token use. Freezing the structure by disabling split and merge reduces average F1 "to 38.59"[^c12], against 43.98 for the full system, which reaches "34.48/43.98" on average BLEU/F1 for that backbone.[^c13] The paper's position on cost is that "agent memory should be measured by evidence utility rather than context reduction alone"[^c14].

## Limits

- The benchmarks are LoCoMo and PerLTQA. The authors concede that "they do not exhaust all possible agent-memory settings"[^c15]. Nothing here tests tool-using agents or memory streams of other kinds.
- The ablations are on one backbone: the text reads "LoCoMo with Qwen3-8B. As shown in Figure 3 (a)"[^c16]. The memory-only step changes both the unit (components instead of raw chunks) and the organisation (groups). The text does not separate what decoupling contributes from what grouping contributes. That separation is my inference from the ablation design, not a result of the paper.
- The construction is costly. "xMemory also introduces additional memory-construction cost"[^c17], and the authors add that "simpler retrieval methods may be preferable" when few queries follow construction[^c18]. The efficiency claim is end-to-end, but it depends on how many queries a memory later serves.
- The decoupling is only as good as its extractor. The components are LLM-generated, and "in component extraction may still affect downstream retrieval"[^c19]. The paper does not measure extraction error or its effect on the groups.
- The group-size bound of 12 was chosen by a routing argument and then checked on LoCoMo. "Larger groups weaken discrimination, while smaller groups fragment the hierarchy"[^c20]. A single sweep on one benchmark does not establish the bound as general.
- The reported gains are differences of a few BLEU/F1 points on two datasets, from one preprint. The paper does not report variance across runs in the text I read.

## Related

- [[compressed-memory-versus-raw-retrieval]] — raw records against an agentic memory that compresses them; decoupled components are neither raw spans nor summaries.
- [[retrieval-collision-coverage]] — the same failure, repeated retrieval of near-duplicates under top-k similarity, addressed there by probe ordering rather than by a group graph.
- [[uncertainty-guided-retrieval-triggering]] — gates retrieval on the model's own uncertainty; Stage II here gates expansion on the reader's marginal uncertainty reduction.
- [[incremental-structure-retrieval]] — an externalised, queryable structure; this note adds retroactive split and merge over it.

[^c1]: doi-10-48550-arxiv-2602-02007 — "while blurring the subtle details that distinguish one"
[^c2]: doi-10-48550-arxiv-2602-02007 — "of decoupling before aggregation: the system should first isolate reusable facts"
[^c3]: doi-10-48550-arxiv-2602-02007 — "each segment is then decoupled into memory components that isolate reusable facts"
[^c4]: doi-10-48550-arxiv-2602-02007 — "groups using an objective that balances sparsity and semantic faithfulness"
[^c5]: doi-10-48550-arxiv-2602-02007 — "Groups that become too large or internally incoherent are considered for splitting"
[^c6]: doi-10-48550-arxiv-2602-02007 — "this remains distinct from retroactive reorganisation"
[^c7]: doi-10-48550-arxiv-2602-02007 — "rather than repeatedly retrieving near-duplicate evidence by pure"
[^c8]: doi-10-48550-arxiv-2602-02007 — "A segment is included only if it yields a positive marginal reduction"
[^c9]: doi-10-48550-arxiv-2602-02007 — "implementation via predictive entropy"
[^c10]: doi-10-48550-arxiv-2602-02007 — "27.95/36.48 for Naive RAG to 31.81/40.77"
[^c11]: doi-10-48550-arxiv-2602-02007 — "is more effective than retrieval over flat raw chunks, even with basic similarity matching"
[^c12]: doi-10-48550-arxiv-2602-02007 — "reduces average F1 to 38.59"
[^c13]: doi-10-48550-arxiv-2602-02007 — "improves from 31.44/40.88 for Nemori to 34.48/43.98"
[^c14]: doi-10-48550-arxiv-2602-02007 — "agent memory should be measured by evidence utility rather than context reduction alone"
[^c15]: doi-10-48550-arxiv-2602-02007 — "they do not exhaust all possible agent-memory settings"
[^c16]: doi-10-48550-arxiv-2602-02007 — "LoCoMo with Qwen3-8B. As shown in Figure 3 (a)"
[^c17]: doi-10-48550-arxiv-2602-02007 — "xMemory also introduces additional memory-construction cost"
[^c18]: doi-10-48550-arxiv-2602-02007 — "simpler retrieval methods may be preferable"
[^c19]: doi-10-48550-arxiv-2602-02007 — "in component extraction may still affect downstream retrieval"
[^c20]: doi-10-48550-arxiv-2602-02007 — "Larger groups weaken discrimination, while smaller groups fragment the hierarchy"
