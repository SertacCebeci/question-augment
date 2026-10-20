---
description: "Truth-default theory: people presume honesty and suspect deception only on strong triggers, so a confident AI accusation of lying must clear a high bar and is often discounted."
aliases: ["truth-default theory", "TDT", "truth bias", "default honesty assumption"]
sources: ["arxiv-2512-02848"]
---
# Truth-default theory

Truth-default theory (TDT) is an account of why people believe what they are told. As the paper summarises it, "people generally assume honesty in communication because deception is" rare, and "quite rare, and its occurrence is limited to a few prolific liars" is the premise that makes the default reasonable.[^t1] Honesty is a default, not a belief re-checked on every statement. "people become suspicious only in case of strong triggers that disrupt this default truth" such as hidden goals, inconsistencies, or a third-party warning.[^t2]

The observed signature of this default is a truth bias. "humans are truth-biased and tend to judge statements as" truthful more often, and are more accurate on truthful than on deceptive statements.[^t3] The paper treats the bias as the thing TDT explains, not as a separate effect.

The paper uses TDT to account for [[high-confidence-aversion]]: participants discounted confident AI accusations of deception. The authors' reading is that "deception may have lacked sufficient justification to prevail over this truth-default status, thus" favouring a cautious stance.[^t4] They add the social side: this stance is "acknowledging the social costs of falsely accusing someone of lying."[^t5] The abstract states the same pairing, that TDT and "the social costs of accusing someone of lying help explain the" findings.[^t7]

What transfers, in my reading and not as a tested claim here: a default weighs against an accusation in proportion to how strong the trigger is. A confidence score from a classifier is a trigger of a different kind from a visible inconsistency or a warning, since it carries no case-specific evidence a human could inspect. If that holds, a confident machine verdict of deception would be discounted more than a confident verdict of truth, which is the asymmetry the experiment found.

## Limits

- TDT is used here as an explanation after the fact. The experiment did not manipulate the default, the triggers, or the social cost of accusation directly.
- The authors present two explanations, and say the link to self-belief is small: "since these associations are small, other" factors may contribute.[^t8]
- The truth bias did not fully replicate under AI judgments. "we did not replicate a full truth-bias effect that was found in previous studies on hybrid" deception detection, and the authors do not settle whether TDT or distrust of AI accounts for that gap.[^t6]
- No consequences were attached to being accused: "information about possible consequences that the author of the statements would have" experienced was not given.[^t9] The authors suggest that such information could make aversion stronger, which would bear on the social-cost part of the account.
- The sample was English-speaking adults recruited online: "We recruited 493 participants fluent in English from the general population through Prolific"[^t10], and the study was a non-incentivised online task, not a forensic setting.
- The concept of TDT is cited from Levine's (2014) theory and is not re-derived in this paper; its scope beyond the stated premises is not tested.

## Related

- [[high-confidence-aversion]] — the measured pattern that TDT is offered to explain
- [[over-reliance-discrimination-failure]] — the opposite default in a student sample: wrong AI answers were accepted, not accusations rejected
- [[rationale-certainty-framing-trust-shift]] — a certainty cue raised trust in a factual answer; the TDT account predicts that accusations need more than a confident tone to be taken up

[^t1]: arxiv-2512-02848 — "people generally assume honesty in communication because deception is"
[^t2]: arxiv-2512-02848 — "people become suspicious only in case of strong triggers that disrupt this default truth"
[^t3]: arxiv-2512-02848 — "humans are truth-biased and tend to judge statements as"
[^t4]: arxiv-2512-02848 — "deception may have lacked sufficient justification to prevail over this truth-default status, thus"
[^t5]: arxiv-2512-02848 — "acknowledging the social costs of falsely accusing someone of lying."
[^t6]: arxiv-2512-02848 — "we did not replicate a full truth-bias effect that was found in previous studies on hybrid"
[^t7]: arxiv-2512-02848 — "how truth-default theory and the social costs of accusing someone of lying help explain the"
[^t8]: arxiv-2512-02848 — "since these associations are small, other"
[^t9]: arxiv-2512-02848 — "information about possible consequences that the author of the statements would have"
[^t10]: arxiv-2512-02848 — "We recruited 493 participants fluent in English from the general population through Prolific"
