---
description: "In a proposer-solver loop, a sound formal verifier gates both the self-generated problems and the solutions used for training, so no incorrect program enters the loop, unlike unit-test rewards."
aliases: ["verified self-play", "propose-solve-verify", "formal-verification self-play", "PSV"]
sources: ["arxiv-2512-18160"]
---
# Sound-verifier self-play

In a self-play loop, a proposer writes problems, a solver tries them, and the solver is trained on whatever the loop accepts as correct. The weak point is the acceptance test. Propose, Solve, Verify (PSV) makes it a formal check. The proposer writes a problem as a formal specification, the solver writes a program with its proof, and a verifier returns a binary label. The paper's argument is that unit tests cannot fill this role, because "set of cases, so programs can pass them and still be incorrect".[^s1] A verifier that checks the program against the whole specification gives a different guarantee: "formal verification provides a sound reward signal".[^s2] The authors state the consequence directly: "formal verification prevents incorrect solutions from entering the self-play loop".[^s3]

The loop itself is simple. A proposer model generates problems for a solver model to train on,[^s4] and the solver's results steer the next round of proposals. The verifier acts at two points. Solutions are kept for training only if they verify. Specifications are also filtered before any solver compute is spent on them. The paper uses Verus, "a framework that enables formal verification of Rust programs".[^s5]

The two checks have different measured costs. Removing solution verification is the large one: the authors report that "removing solution verification hurts performance significantly", with relative pass@1 drops of 51.5% on Dafny2Verus, 55.2% on MBPP and 52.1% on HumanEval.[^s6] Removing specification verification is an efficiency cost. The authors use the filter "to filter out candidate specs to make sure they are syntactically compilable before attempting inference on them".[^s7] Without it, only 47.7% of unique specs were valid on average.[^s8] The remaining specs are not solvable, and the authors count the cost as "a 2.1x increase in inference" compute for "no resulting performance improvement".[^s9]

A sound verifier also changes the training update. The authors note that the Verus verifier is "sound but not complete", so they train by rejection fine-tuning on verified solutions rather than by an advantage-weighted update, which "could incorrectly punish models for correct solutions that were judged to be incorrect".[^s10][^s11] My inference: a checker that only accepts correct work supports filtering, but it does not by itself license a signed reward that scores every rejection as a failure, because a correct program the checker rejects would be scored as one.

## Limits

- One verifier and one language. The result is for Verus on Rust, with specifications translated from a corpus. The text does not test a second verifier, so whether the same gains follow from another sound checker is open.
- The seed is human-written. The loop starts from a translated corpus that "originates from human-written problems."[^s12] The abstract's phrase "without any human data" describes the loop after seeding, not the seed.
- The verifier checks a solution against a given specification. The only specification check the text reports is compilability. Whether a specification states the problem that was meant is not checked in the text I read; that is my inference, not the paper's claim.
- Incompleteness costs something the paper does not measure: correct programs the verifier rejects are simply lost from training. The authors leave on-policy RL for this setting to future work.
- The "sound" property belongs to the checker. The paper's experiments compare against AlphaVerus, RFT and its own ablations; the unit-test contrast is argued in the introduction and is not measured in the parts I read. The evidence shows that a verified loop outperforms the tested alternatives, not that it cannot err.

## Related

- [[verification-weighted-voting]] — uses tool-verified answers as weighted votes rather than as a training filter
- [[execution-verified-preference-pairs]] — the same idea in SQL: execution match, not a human label, decides which generated answers count
- [[curriculum-collapse]] — the questioner-solver loop whose questioner output sets the solver's whole training distribution
- [[verifier-exploitation-rate]] — measures the reward hacking that a checker weaker than a sound verifier allows

[^s1]: arxiv-2512-18160 — "set of cases, so programs can pass them and still be incorrect"
[^s2]: arxiv-2512-18160 — "formal verification provides a sound reward signal"
[^s3]: arxiv-2512-18160 — "formal verification prevents incorrect solutions"
[^s4]: arxiv-2512-18160 — "a proposer model generates problems for a solver model to train on"
[^s5]: arxiv-2512-18160 — "a framework that enables formal verification of Rust programs"
[^s6]: arxiv-2512-18160 — "removing solution verification hurts performance significantly"
[^s7]: arxiv-2512-18160 — "to filter out candidate specs to make sure they are syntactically compilable before attempting inference on them"
[^s8]: arxiv-2512-18160 — "only 47.7% of unique specs were valid on"
[^s9]: arxiv-2512-18160 — "specs that were not solvable, a 2.1x increase in inference"
[^s10]: arxiv-2512-18160 — "sound but not complete, meaning that advantage-weighted"
[^s11]: arxiv-2512-18160 — "algorithms could incorrectly punish models for correct solutions that were judged to be incorrect"
[^s12]: arxiv-2512-18160 — "which originates from human-written problems"
