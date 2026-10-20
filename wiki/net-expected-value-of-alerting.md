---
description: "Interrupt a person only when the expected value of telling them now, versus when they would look anyway, exceeds the expected cost of distracting them given their inferred attentional state."
aliases: ["NEVA", "attention-sensitive alerting", "expected cost of interruption", "utility-directed notification"]
sources: ["horvitz-2013"]
---
# Net expected value of alerting

Horvitz, Jacobs and Hovel frame an interruption as a decision under uncertainty about two things: how busy the person is, and how much the message matters. The rule is to alert only when the net value is positive.

## Mechanism

**Cost side.** The system never knows the user's attentional state exactly. It keeps a probability distribution over states of focus, F_j, given evidence, and prices each alert action A_i by the expected cost of alerting, ECA = sum over j of C_a(A_i, F_j) p(F_j | E_a).[^c1] The cost depends on the alert's design as well as on the user's focus. A cognitive distraction cost is separate from the cost of obstructing display content, and an overlay that must be dismissed costs more than one that disappears on its own.[^c2]

**Benefit side.** Deferral is the alternative to interrupting.[^c3] Its cost, the expected cost of delayed action, is the difference between the value of the ideal action taken at arrival and the value of the ideal action taken later. To make this tractable, each message is assigned a probability over criticality classes. Each class has a time-dependent rate of loss with delay, and the probability-weighted rate is the message's expected criticality.[^c4]

**Baseline.** The benefit of an alert is measured against what happens without it. Users still review messages unprompted, and the time between reviews is the inspection interval, which depends on the user's attentional focus and location.[^c5] The expected value of transmitting an alert (EVTA) is the loss avoided by being informed now rather than at the expected inspection time. It is computed from the distribution over inspection intervals and the expected criticality.

**Decision rule.** Relay the message when NEVA = EVTA - ECA is positive.[^c6] An important message does not justify an interruption by itself. A message that the user will see in a minute anyway has low EVTA however critical it is. An unimportant message during deep focus has negative NEVA.

The system also needs a classifier that estimates criticality from message content and headers. The paper's PRIORITIES system does this for email, and it reports discriminatory power at different decision thresholds in a ROC-style figure.

## Why it matters for asking

A question put to a person is an interruption. The rule transfers directly: a clarifying question has a cost that depends on the answerer's state, and a value that depends on how much the answer changes the outcome compared with proceeding without it. This is my inference, not a claim the paper makes. The paper concerns notifications, not questions.

## Limits

- The paper is a 1999-era design and modelling paper. The models are specified, and I did not find an experiment in the slices I read showing that NEVA-guided alerting beats simpler policies.
- The cost functions C_a and the loss rates C_d are assumed to be assessable. How to elicit them is left open.
- The paper notes that treating the value of reading distinct messages as independent can overestimate the value of a multiple-message alert, because messages in a sequence may refer to related content.
- It decomposes interruption cost and obstruction cost but then merges them into one cost for simplicity.
- Nothing here concerns conversational questions, answer quality, or non-human answerers.

## Related

- [[proactivity-taxonomy]] — the situation-aware level is defined by a learned policy of this cost-benefit kind, including staying silent
- [[activation-gate]] — a gate whose threshold rises with interruption cost and falls with urgency, the same trade-off with a different formalism
- [[roc-curve]] — how the criticality classifier's discrimination at different thresholds is displayed

[^c1]: horvitz-2013 — "the expected cost of alerting (ECA) a user with action"
[^c2]: horvitz-2013 — "A design that overlays a graphical notification over"
[^c3]: horvitz-2013 — "A strategy for reducing the cost associated with alerts"
[^c4]: horvitz-2013 — "as the expected criticality (EC) of a message,"
[^c5]: horvitz-2013 — "We refer to the time between periods of reviewing new"
[^c6]: horvitz-2013 — "NEVA= EVTA- ECA"
