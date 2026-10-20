---
description: "Counting a generated program as correct only when it passes both a functional and a security suite drawn from one specification gives a joint rate far below either marginal pass rate."
aliases: ["joint security-functionality success", "joint pass rate", "conjunctive pass rate over paired suites", "paired-suite joint metric"]
sources: ["arxiv-2511-20709"]
---
# Joint pass rate over paired suites

Give a model one natural-language specification and two test suites built from it: one for functional behaviour, one for security behaviour. A sample then succeeds only if it passes both. DualGauge builds its benchmark this way, pairing each task "with functional and security tests derived" from one shared specification, so that the two suites answer to the same request.[^d1]

The measure is a conjunction, and the arithmetic matters. A sample that counts only when both parts pass can never score above either part alone, and it falls well below both when the parts fail for different reasons. The paper's headline numbers show the size of the gap. The strongest model reaches a "39% functional pass rate on Python," but it "satisfies both constraints on fewer than 15% of" tasks in every language.[^d2][^d3] The authors' reading is that "functional correctness substantially overestimates reliable code generation."[^d4]

The gap is not closed by the usual levers. The paper varies scale, extended thinking, quantization, instruction tuning and code specialization, and finds that each shifts the functional and security metrics differently by model family, while "no factor reliably improves the" joint metric.[^d5] So a rise on the functional suite does not carry over to the joint rate. My inference, not the paper's claim: a marginal rate for each suite does not determine the joint rate, because the two can fail on different samples. The paper reports the joint rate directly rather than deriving it from the marginals, which is why the joint measure has to be taken as its own quantity.

The conjunction makes one failure visible that a single suite cannot show. A program can pass every functional case and still fail the security case, and the functional suite is structurally unable to notice this,[^d8] because it reads only outputs and a secure and a vulnerable program can return the same outputs. That blindness is the subject of [[output-equivalence-blindness]]. The joint measure is the device that turns it into a failure, which is the same job a conjunctive rule does elsewhere. Search can use a conjunction to make a target findable, as in [[conjunctive-masked-criteria]], and here it is used to score success.

## Limits

- The numbers come from one sample per prompt (k = 1), and the paper notes that "so behavior may change under different sampling settings."[^d6] A rate from a single draw is an estimate, and the headline figures are the paper's summaries, not a distribution over samples.
- The security side is judged by an LLM-based evaluator. The authors say "ambiguous traces, complex edge cases, and unfamiliar libraries can still lead to evaluator errors," and that the results are "scalable benchmark estimates, not substitutes for human security review."[^d7]
- The security suites cover the classes the authors chose, derived from OWASP and CERT principles. The text says the benchmark does not exhaustively cover all classes, so a joint rate is a rate over this suite, not over every way code can be insecure.
- The setting is specification-only generation, deliberately without fixed APIs or repository context. The joint rate in a richer setting is not measured here.
- I read the abstract and the audit section, not the full result tables. The per-language and per-model breakdowns beyond the headline figures are not reported in this note.

## Related

- [[correctness-congruence-gap]] — another case where a formal check passes while the goal it stands for is missed; here the second check is a paired suite instead of an intent comparison.
- [[partial-requirement-coverage]] — why a sample can pass one suite and fail the other: a guard that covers only some cases.
- [[output-equivalence-blindness]] — why the functional half of the pair cannot see what the security half measures.
- [[conjunctive-masked-criteria]] — a conjunction used to set a difficulty for search, the same logical device applied to scoring.

[^d1]: arxiv-2511-20709 — "paired with functional and security tests derived"
[^d2]: arxiv-2511-20709 — "39% functional pass rate on Python"
[^d3]: arxiv-2511-20709 — "satisfies both constraints on fewer than 15% of"
[^d4]: arxiv-2511-20709 — "substantially overestimates reliable code generation"
[^d5]: arxiv-2511-20709 — "no factor reliably improves the"
[^d6]: arxiv-2511-20709 — "so behavior may change under different sampling settings"
[^d7]: arxiv-2511-20709 — "benchmark estimates, not substitutes for human"
[^d8]: arxiv-2511-20709 — "structurally blind to this class of failure"
