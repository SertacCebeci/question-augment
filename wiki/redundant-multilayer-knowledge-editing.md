---
description: "Rank-one edits fail multi-hop questions because the edited layer must fit the hop order; copying one edit into several MLP layers lifts 2-hop accuracy but erodes specificity and fluency."
aliases: ["Redundant Editing", "hopping-too-late in model editing", "multi-layer ROME"]
sources: ["arxiv-2601-04600"]
---
# Redundant Multi-Layer Knowledge Editing

A rank-one edit (ROME) writes one fact (subject, relation, new object) into the down-projection of a single MLP layer. It is accurate for the single fact but weak when the edited fact is one step of a chain. He et al. (2026) test GPT-J-6B on MQuAKE 2-hop questions and name three failures: "hopping-too-late", generalization that "deteriorates sharply when editing later layers", and overfitting to the edited hop.[^c1]

## Why depth matters

Prior work they build on finds that models resolve the intermediate entity in early layers and finish the reasoning in later ones, so a chain needs hop-1 knowledge stored earlier than hop-2 knowledge.[^c2] A single-layer edit fixes one depth. The measured single-layer pattern matches: editing hop 1 works best in early layers, editing hop 2 in later ones.[^c3] Single-layer edits also generalize worse to rephrased questions as the layer deepens.[^c4]

## The fix and its measured effect

Redundant Editing runs ROME independently at several layers (5th to 20th) and loads all edited MLPs into the original model, so "any of these copies can be used to build a reasoning chain".[^c5] The best configuration (layers 5, 8, 11, 15, 17, 20) reaches 31.6% average 2-hop accuracy against 16.1% for layer 5 alone.[^c6] The abstract reports a gain of at least 15.5 points, a 96% relative increase.[^c7] The authors attribute it to better rephrase generalization and to more possible internal reasoning chains.[^c8]

## The price

Specificity on COUNTERFACT falls from 76.3 (layer 5) to 17.0 (six layers) and the composite score from 90.9 to 56.6.[^c9] The authors' explanation, offered as a hypothesis, is that edits do not erase the old fact but add a stronger competing signal; the original answer stays in the top-10 tokens in 46% of cases, and hop-1 edits make the model favor the edited intermediate answer over the final one in up to 55.8% of cases against 3.2% for unedited GPT-J.[^c10] More copies strengthen that dominant signal, which they take to explain the specificity loss.[^c11]

## Limits

- One model (GPT-J-6B), one editor (ROME), 2-hop questions with a single edited hop; n>=3 hops and simultaneous multi-hop edits are untested, as the authors state.[^c12]
- COUNTERFACT metrics use only 100 instances and the MQuAKE subsets are 240 and 359 items; absolute 2-hop accuracies stay low (about 30%).
- The signal-interference account is a hypothesis resting on correlation with prior work, not an isolated intervention. The conclusion's phrase "maintaining language quality" conflicts with their own Table 3 trade-off; I trust the tables.
- Whether the lesson transfers to prompting or retrieval is my inference, not shown here.

## Related

- [[parametric-suppression]] — another case where a stored answer is present yet overridden by a stronger signal in later layers
- [[knowledge-injection-mechanism-comparison]] — editing is one of several ways to inject knowledge
- [[hop-depth-difficulty-with-entropy-check]] — difficulty of multi-hop questions as hop count grows

[^c1]: arxiv-2601-04600 — "Second, generalization ability deteriorates sharply when editing later layers."
[^c2]: arxiv-2601-04600 — "Biran et al. (2024) found that LLMs resolve intermediate"
[^c3]: arxiv-2601-04600 — "early layer (e.g., layer 5) excels hop-1 reasoning accuracy at 28.3%, compared to late layers (e.g., layer 20) at"
[^c4]: arxiv-2601-04600 — "Additionally, we observe a decreasing trend for generalization ability in both scenarios (edit hop-1 and hop-2)"
[^c5]: arxiv-2601-04600 — "when tested on multi-hop questions any of these copies can"
[^c6]: arxiv-2601-04600 — "demonstrating significant improvement over configurations"
[^c7]: arxiv-2601-04600 — "Our experiments demonstrate that this approach can improve accuracy on 2hop questions by at least 15.5 percentage points, representing"
[^c8]: arxiv-2601-04600 — "Redundant Editing creates more"
[^c9]: arxiv-2601-04600 — "Specificity decreases significantly from 76.3 (layer 5"
[^c10]: arxiv-2601-04600 — "shows minimal bias (3.2%)."
[^c11]: arxiv-2601-04600 — "copies further strengthens the dominant signal, which explains its observed trade-off of lower specificity for higher"
[^c12]: arxiv-2601-04600 — "single-hop edits, leaving open questions about the scalability"
