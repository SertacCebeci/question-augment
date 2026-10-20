---
description: "A defeasible domain lets every position be defeated by better reasoning and has no reference answer; the paper places debate's value there, not in ground-truth tasks."
aliases: ["defeasible question", "defeasible topic", "non-ground-truth domain"]
sources: ["doi-10-48550-arxiv-2605-12718", "arxiv-2511-22832"]
---
# Defeasible domain

A domain is defeasible when a position held in it stays open to revision by a better argument: "where every position can in principle be defeated by better reasoning."[^c1] The status is a property of the question's domain, not of any one answer. An answer in a defeasible domain is held only until it is beaten in argument.

The paper sets this against ground-truth tasks, where a reference answer exists. Its reading of the debate literature is that debate "often fails to outperform simple baselines such as majority voting," and that the answer "lies in defeasible domains, where no ground-truth answer exists and every position."[^c2] The claim is that the genuine value of debate and of dialectic systems "lies not in ground-truth tasks but in defeasible" domains.[^c3]

What changes for asking and answering is the check available. On a ground-truth question an answer can be compared with a reference and stopped when it matches. On a defeasible question no such comparison exists, so the standing of an answer depends on whether it survives challenge under a stated standard. That is the point at which the choice of standard becomes the decisive variable, as [[adjudication-standard-sets-debate-outcome]] reports for one ablation. The consequence for practice is my inference; the paper does not derive it.

The paper's argument for why this matters rests on a second claim: debate alone does not improve expected correctness. It cites the martingale result that "argumentative exchange alone does not improve expected correctness without structural interventions that bias updates toward correction."[^c4] The defeasible framing is offered as the place where argument is the only available test, which makes the absence of a reference a reason to structure the argument, not a reason to skip it.

The paper gives a way to make such domains inspectable. Its belief objects are "auditable belief artifacts," and it expects them to "establish the foundation for dedicated evaluation suites for defeasible argumentation."[^c5] Those suites are described as future work.

A ground-truth task gives one case where a debate-shaped prompt was tried and dropped. An entity-matching study, whose pairs are labelled, compared a single-model pro-and-con prompt (arguments for a match, arguments against, then a moderator who picks the stronger) with other prompts, and found the debate form "significantly worse": "we recognize that it is significantly worse than the other three methods".[^c7] On the DA dataset the debate prompt reached "the debate based prompt only achieves 0.835" zero-shot.[^c8] The authors conclude "Thus we believe it is not a feasible strategy for entity matching" and leave it out of the comparison.[^c9] This is consistent with the paper's placement of debate's value outside ground-truth tasks. It is not a test of that placement: the study uses one model and a single-model prompt, not the multi-agent debate this note is about, and the reported debate numbers are a single example (my reading).

## Limits

- The paper does not evaluate on a defeasible benchmark. Its experiments are ablations on philosophical questions, with simulated agents. Its topic ablation, offered "to assess generalization across philosophical domains," is a single-trajectory demonstration across three topics.[^c6] The "dedicated evaluation suites" are future work.
- The claim that debate's value lies in defeasible domains is the authors' argument. The passages read contain no measured comparison between ground-truth and defeasible tasks under the same method.
- Defeasibility is defined "in principle," which gives no operational test. Nothing in the passages read says how to decide, for a given question, whether a better argument could exist. A question can look ground-truth-free while a reference exists elsewhere, or the reverse.
- The word has a neighbour in the wiki. [[abduction-inference-to-best-explanation]] uses "defeasible" for an inference, a conclusion that new evidence can overturn. Here it names a domain. The two are related, since a defeasible inference is the usual way to work in a defeasible domain, but the note does not treat them as the same object.
- The paper's sense of "ground-truth" is the one it needs for its contrast. Many questions with reference answers still admit contested reasoning, and the note does not settle where that boundary falls.

## Related

- [[abduction-inference-to-best-explanation]] — defeasibility as a property of an inference; here it is a property of a domain
- [[adjudication-standard-sets-debate-outcome]] — in a defeasible domain the scoring standard decides where the exchange converges
- [[dialectic-red-team]] — assigned opposition as a way to test a position when no reference answer exists
- [[confidence-weighted-debate-submartingale]] — the martingale limit of debate, measured against a correct answer where one exists

[^c1]: doi-10-48550-arxiv-2605-12718 — "where every position can in principle be defeated by better reasoning"
[^c2]: doi-10-48550-arxiv-2605-12718 — "that the answer lies in defeasible domains, where no ground-truth answer exists and every position"
[^c3]: doi-10-48550-arxiv-2605-12718 — "lies not in ground-truth tasks but in defeasible"
[^c4]: doi-10-48550-arxiv-2605-12718 — "argumentative exchange alone does not improve expected correctness without structural interventions"
[^c5]: doi-10-48550-arxiv-2605-12718 — "establish the foundation for dedicated evaluation suites for defeasible argumentation"
[^c6]: doi-10-48550-arxiv-2605-12718 — "we provide an singletrajectory demonstration across three topics"
[^c7]: arxiv-2511-22832 — "we recognize that it is significantly worse than the other three methods"
[^c8]: arxiv-2511-22832 — "the debate based prompt only achieves 0.835"
[^c9]: arxiv-2511-22832 — "Thus we believe it is not a feasible strategy for entity matching"
