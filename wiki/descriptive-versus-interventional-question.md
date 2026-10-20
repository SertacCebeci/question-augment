---
description: "Association questions ('what-is') and intervention questions ('what-if') need different tools; a descriptive method answering a what-if can rank the wrong factor for intervention."
aliases: ["what-is versus what-if", "descriptive versus interventional question", "associational versus interventional question"]
sources: ["arxiv-2512-02060"]
---
# Descriptive versus interventional question

A descriptive ("what-is") question asks how observed variables relate in the data that were collected. Correlation, significance testing, PCA, clustering and model-explanation tools such as SHAP answer that kind. An interventional ("what-if") question asks what would happen to an outcome if a variable were changed. The paper's motivating question is how "modifications to certain variables, like increasing the size of the window" would move occupant satisfaction.[^d1] The two kinds of question are not interchangeable. The paper argues that using descriptive tools on interventional questions "often overlooks confounding and colliding variables", and that this leads to bias and to wrong decisions.[^d2]

**The mechanism.** An association is symmetric. A correlation between lighting satisfaction and acoustic satisfaction says that the two move together and nothing about which one to change. An intervention is asymmetric: the answer depends on which variable acts on which, and on which other variables must be held fixed while one is moved. The paper's way of recovering that asymmetry is a causal discovery method: "Causal discovery algorithms exploit conditional independence patterns that reveal directional relationships."[^d3] The graph it returns is a structure over variables, and the intervention question is answered from that structure, not from the correlation matrix. The graph is what the paper uses to carry the asymmetry: causal discovery is "typically represented as a Directed Acyclic Graph (DAG)".[^d15]

**What the split changes in practice.** The two kinds of question can point at different factors. The paper's illustration is that a survey which shows many complaints about noise, and few about lighting, would lead a descriptive reading to "would target acoustics first".[^d4] In its case study the causal reading ranks glare and reflections on screens as the most upstream factor, even though glare "was not the majority source of dissatisfaction in the statistical summary".[^d5] The paper's summary of its own comparison is that the two kinds of tool "can lead to oppositely different suggestions for intervention".[^d6]

The paper also says what it wants from the split as a practice. "We encourage researchers to first categorize their questions as descriptive ('what-is') or interventional ('what-if') before selecting analytical approaches."[^d7] It presents causal discovery as "methodological complementarity rather than replacement" of traditional approaches.[^d8]

**What survives the transfer.** The distinction is the one between conditioning on an observed value and setting a variable to a value. The Pearl-style ladder in [[rung-stratified-causal-accuracy]] draws the same line at finer grain, with association, intervention and counterfactual rungs. The paper's contribution is to apply the line to human-factor survey questions. A second thing the descriptive side cannot do, by the paper's account, is certify independence: a correlation analysis of the same survey found 80 strong associations but "cannot distinguish causal independence from weak associations or provide intervention priorities".[^d9] That independence claim is taken up in causal-skeleton-variable-screening.

The paper's reading is a question-side claim: a question's type should be fixed before the method is picked. The wiki's [[analytical-information-need]] note sorts needs as descriptive, predictive or prescriptive; the what-is/what-if split here is a different cut, and the note's own type list does not contain it. Whether the two cuts coincide was not tested here.

## Limits

- The split is argued from a case study, not proved. The paper says itself that "this was just one case study",[^d10] and that its finding about glare "may reflect building-specific characteristics".[^d16]
- The interventional answers come from observational survey data, so they rest on assumptions the data cannot check. The paper states that "The assumption of no unmeasured confounders is particularly" hard to hold in buildings.[^d11] It calls its structure "testable hypotheses rather than definitive causal claims".[^d12]
- The "intervention" is a high-versus-low contrast in the target variable's satisfaction, which the paper calls "conceptually represented by the do-operator in causal theory".[^d13] This approximates an intervention; it is not an identified one, and this note does not treat it as one.
- Nothing here measures how often a practitioner misclassifies a question, or whether running the descriptive analysis first changes the decision. The paper argues the point with one dataset and one comparison.
- The paper's validation of the causal structure is partial by its own account: the open-ended answers "provides partial support for our causal structural assumptions".[^d14]

## Related

- [[analytical-information-need]] — its descriptive, predictive and prescriptive need types are another cut of the same question; whether the two coincide was not tested.
- [[rung-stratified-causal-accuracy]] — Pearl's ladder, the association-versus-intervention line at finer grain, read per rung for LLM answers.
- [[potential-outcome-counterfactual-semantics]] — what "what if" means once it goes beyond a single intervention.
- causal-skeleton-variable-screening — the graph step that decides which variables an interventional question concerns.
- [[collider-conditioning-bias]] — why a descriptive analysis that conditions on the wrong variable misreads even a plain association.

[^d1]: arxiv-2512-02060 — "aim to understand how modifications to certain variables, like increasing the size of the window"
[^d2]: arxiv-2512-02060 — "often overlooks confounding and colliding variables"
[^d3]: arxiv-2512-02060 — "Causal discovery algorithms exploit conditional independence patterns that reveal directional relationships"
[^d4]: arxiv-2512-02060 — "would target acoustics first"
[^d5]: arxiv-2512-02060 — "Although these factors were not the majority source of dissatisfaction in the statistical summary"
[^d6]: arxiv-2512-02060 — "can lead to oppositely different suggestions for intervention"
[^d7]: arxiv-2512-02060 — "We encourage researchers to first categorize their questions as descriptive"
[^d8]: arxiv-2512-02060 — "methodological complementarity rather than replacement"
[^d9]: arxiv-2512-02060 — "cannot distinguish causal independence from weak associations or provide intervention priorities"
[^d10]: arxiv-2512-02060 — "this was just one case study"
[^d11]: arxiv-2512-02060 — "The assumption of no unmeasured confounders is particularly"
[^d12]: arxiv-2512-02060 — "our causal structure should be interpreted as testable hypotheses rather than"
[^d13]: arxiv-2512-02060 — "conceptually represented by the do-operator in causal theory"
[^d14]: arxiv-2512-02060 — "provides partial support for our causal structural assumptions"
[^d15]: arxiv-2512-02060 — "typically represented as a Directed Acyclic Graph (DAG)"
[^d16]: arxiv-2512-02060 — "may reflect building-specific characteristics rather than universal patterns"
