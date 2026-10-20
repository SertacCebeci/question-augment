---
description: "An agent repairing its output toward a hidden target improves when the sibling solutions already in its repository are shown to it, since they constrain format and workflow."
aliases: ["reference-code prompting", "in-repository reference adaptations"]
sources: ["arxiv-2511-21380"]
---
# Reference-code-guided repair

When a coding agent must produce an artifact that matches a target it cannot see, one constraint is often already in the repository: the other adaptations of the same artifact. The paper on GitHub Copilot's agent mode for dataset adaptation builds its task this way. It takes a repository that holds several dataset adaptations, removes the one under test, and keeps the rest: "files associated with other dataset adaptations will be retained as reference code in each repository."[^r1] Those files go into the prompt. The stated reason is that they "provide hints about function usage, parameter formats, and workflow organization, allowing the agent to align its implementation generated in Step 2 with the existing adaptations."[^r2] What gets repaired is the gap between the agent's edit and its sibling: "the reference code serves as a guiding signal for refining the implementation."[^r3]

The reference is a constraint, not an answer. It fixes the shape the answer must take, such as the argument format a sibling uses or the order in which its scripts call one another, and it leaves open the content that only the missing target supplies. My inference is that this split is what makes the intervention cheap to apply: the agent is not handed the answer, only the form it must fit. The paper does not test the split. It gives the sibling files as hints and reports only the combined effect of its interventions.

Reference-guided repair can also stall. The paper observes that "the agents sometimes fall into a dilemma where Prompt 2 keeps modifying irrelevant parts of the code without fixing the actual issue."[^r4] A sibling shows what consistency looks like, but not where the inconsistency sits. The paper's complement is an expert's fault location, which "helps the agent break out of this loop by explicitly pointing to the exact line that requires modification."[^r5] The two are used in order. Reference code is supplied once the program runs, to correct "logical or structural mistakes."[^r6] The location hint follows when the reference has been applied to the same issue without success: "If Prompt 2 was applied to the same code issue three consecutive times" and the agent has not fixed it, the paper moves to Prompt 3. That threshold is the paper's experimental protocol, not a finding.[^r7]

The location hint also covers what the reference cannot. It "extends the applicability of the overall setup to cases where reference code is unavailable"[^r8], as with a function-name extraction step that has no counterpart in the other datasets. The reference supplies a constraint drawn from siblings; the location supplies a pointer from a person. Each covers the case where the other is missing.

The paper reports its interventions together. "Prompt-level interventions, especially providing execution error messages and reference code, substantially improve structural similarity to ground truth (from 7.25% to 67.14%)."[^r9] The gain is credited to the set of interventions, and the abstract does not assign a share to the reference code alone.

## Limits

- The reference-only effect is not isolated. The abstract reports error messages and reference code as one group, and the parts of the text read give no reference-only figure. The share of the 7.25% to 67.14% change that comes from reference code is not established.
- The evidence is one agent system (Copilot, with two backends) on a small selection of artifacts: "Two projects (i.e., ROCODE [15] and LogHub2.0 [16]) are selected for the following experiments."[^r10] Two repositories do not show how the effect varies across artifacts.
- The reference exists only when the artifact holds several adaptations of the same kind. A method with a single implementation offers no sibling. Whether a sibling that differs in structure misleads the agent is not tested in this text (my inference).
- The dilemma that makes the location hint necessary is described, not counted. The text read gives no frequency with which reference-guided edits stall on irrelevant code.
- The mechanism by which the reference helps is the authors' reading of an aggregate result, supported by citation to prior work rather than by a separate test (my reading of the paper's framing).

## Related

- [[feedback-quality-bottleneck]] — raw error output and reference code are feedback that bypasses a model-written diagnosis, the step that note puts at the centre of self-repair.
- [[stage-disentangled-evaluation]] — the same paper scores its agent stage by stage, so the reference's effect is read at the repair stage, not at the reading or editing stages.
- [[constraint-as-information]] — a sibling's format is a constraint in that note's sense: it removes possibilities without being the answer, whatever its origin.

[^r1]: arxiv-2511-21380 — "files associated with other dataset adaptations will be retained as reference code in each repository"
[^r2]: arxiv-2511-21380 — "These reference files provide hints about function usage, parameter formats, and workflow organization, allowing the agent to align its implementation generated in Step 2 with the existing adaptations."
[^r3]: arxiv-2511-21380 — "the reference code serves as a guiding signal for refining the implementation"
[^r4]: arxiv-2511-21380 — "Prompt 2 keeps modifying irrelevant parts of the code without fixing the actual issue"
[^r5]: arxiv-2511-21380 — "Prompt 3 helps the agent break out of this loop by explicitly pointing to the exact line that requires modification"
[^r6]: arxiv-2511-21380 — "Prompt 2 was employed to provide reference code and guide the multi-agent system in correcting logical or structural mistakes"
[^r7]: arxiv-2511-21380 — "If Prompt 2 was applied to the same code issue three consecutive times"
[^r8]: arxiv-2511-21380 — "it extends the applicability of the overall setup to cases where reference code is unavailable"
[^r9]: arxiv-2511-21380 — "Prompt-level interventions, especially providing execution error messages and reference code, substantially improve structural similarity to ground truth (from 7.25% to 67.14%)"
[^r10]: arxiv-2511-21380 — "Two projects (i.e., ROCODE [15] and LogHub2.0 [16]) are selected for the following experiments."
