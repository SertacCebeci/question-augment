---
description: "A skeptical critic that re-checks each stated fact against the input and guidelines, with one revision cycle, cut hallucination 11.3% to 3.8% and helped most on complex cases."
aliases: ["adversarial self-critique", "critic-revise cycle", "internal adversarial reviewer"]
sources: ["arxiv-2602-13213", "arxiv-2601-09714"]
---
# Skeptical critic fact cross-check

Before an answer reaches a human, a second pass of the same model is given the draft and its reasoning chain and told to act as a skeptical internal reviewer. Its job is to cross-check every stated fact against the input data and the guidelines, list discrepancies, and sometimes inject hypothetical scenarios to test robustness.[^c1] The primary agent then revises once. The design aim is that the agent "must convince an adversarial version of itself before reaching human review".[^c2]

## What was measured

In a commercial-underwriting system tested on 500 expert-validated cases, the agent-only variant produced hallucinated content in 11.3% of cases (for example an alarm system not in the submission, or a nonexistent guideline). With the critic this fell to 3.8%, and no major hallucinations were seen.[^c3] The critic worked by questioning whether stated facts were actually present in the submission.[^c3]

The critic itself was scored: an 87% catch rate on genuine issues and a 12% false-positive rate, so about one flag in eight was a non-issue on human review.[^c4]

The benefit depended on difficulty. On 150 complex cases accuracy rose from 85% to 93%. On 100 simple cases it went from 98% to 99%, so the critic found little to improve there and its overhead was less justified.[^c5] On 30 cases with deliberately inconsistent data, the agent alone missed the inconsistency in 57% of cases, and with the critic it flagged inconsistencies in 90%.[^c6]

## Mechanism (the paper's account, plus my reading)

The critic's questions are about grounding: is this claim in the source? That is a narrower and more checkable question than "is this answer good?". My inference, not tested in the paper, is that this narrowness is why the loop helps: the critic needs no knowledge the primary lacked, only the discipline of re-asking about each claim.

## Limits

- The ablation compares agent-only against agent-plus-critic. It does not separate the critic's role-prompt from the extra pass of compute, so "adversarial" is not isolated as the cause.
- One domain, one model family and one revision cycle. Whether more cycles help was not established here.
- The critic and the primary are the same model family, so shared blind spots are not addressed. This is my inference.
- Evaluation cases are expert-validated by the same organisation that built the system. A false-positive rate of 12% means human review is still needed.
- Grounding is not originality. A critic that re-checks claims against a source does not, by that alone, raise the novelty of what it checks. In a comparison of five agentic ideation workflows, the reflection workflow, a critic that flagged clichés and overlap with the literature followed by a revision, scored lowest on novelty; the paper reads this as self-critique being unable to overcome an unoriginal starting point.[^c7] The reported gap is not tested for significance, and the workflows differ in more than the critic, so the comparison does not isolate the critic's effect.[^c8]

## Related

- [[specific-actionable-self-feedback]] — a self-feedback loop whose quality depends on how specific the critique is
- [[prover-verifier-deliberation]] — another split of generating and checking roles
- [[adversarial-metric-self-review]] — adversarial self-review applied to metrics
- [[llm-red-teaming]] — adversarial probing from outside the model

[^c1]: arxiv-2602-13213 — "who cross-checks every stated fact against input data and"
[^c2]: arxiv-2602-13213 — "adversarial version of itself before reaching human review."
[^c3]: arxiv-2602-13213 — "rate dropped to 3.8%, with no major hallucinations observed"
[^c4]: arxiv-2602-13213 — "an 87% catch rate for genuine issues (95% CI: 83–91%), while"
[^c5]: arxiv-2602-13213 — "was 85%, while adding the critic increased it to 93%, approaching the human benchmark of 98%."
[^c6]: arxiv-2602-13213 — "notice inconsistencies in 57% of cases. While the agent with"
[^c7]: arxiv-2601-09714 — "self-critique cannot overcome fundamentally unoriginal starting points"
[^c8]: arxiv-2601-09714 — "reflection-based approaches score significantly lower (2.33/5)"
