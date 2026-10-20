---
description: "A question is asked only when goal uncertainty exceeds an interruption cost that is highest right after the last question and decays to a floor, so repeated asking is priced out."
aliases: ["time-dependent interruption cost", "decaying cost of asking", "question refractory cost"]
sources: ["arxiv-2512-04453"]
---
# Refractory interruption cost

A robot that can ask has to decide whether to interrupt at all, not only what to ask. Ghose et al. turn that decision into a comparison between two numbers. The first is the robot's uncertainty over the human's goal, the entropy H(g) of its belief. The second is the cost of asking at time t, and the paper makes that cost depend on the dialogue's own history: "immediately after asking, the interruption cost is high and then decreases linearly toward a minimum."[^c1]

Write Δt for the time since the last question, T_q for the interval after which the cost reaches its floor, and ΔC = C_max − C_min for the range of costs. The cost is C_min once Δt ≥ T_q, and C_max − ΔC·(Δt/T_q) before that.[^c1] The cost is then multiplied by log(n_goals), the log of the number of plausible goals, and a question is asked when the entropy exceeds the scaled cost, "enough that reducing it is worth the interruption."[^c2] The stated reasons are two. The time dependence exists "to discourage repeated interruptions."[^c3] The log scaling exists because "the value of resolving uncertainty increases with the number of plausible goals."[^c4]

The mechanism is a memory in the asking rule. Right after a question, even a belief that is still very uncertain does not clear the bar, so the robot waits. As time passes the bar falls to a floor, and a sufficiently uncertain belief again licenses a question. The threshold therefore depends on what was asked recently, not only on the belief state. My inference, not a claim the paper makes: a rule that compares belief entropy with a fixed cost would ask again at once whenever an answer left the goal still ambiguous, and this one does not.

The note separates two decisions the paper names together: "The robot must decide when to ask a question, what question to ask and how to use the answer to reduce uncertainty over goals."[^c5] The refractory term settles the *when*. The *what* is settled by expected entropy reduction over candidate questions, which is the subject of [[expected-information-gain]].

What is measured is the question module as a whole. In open-goal cooking runs, BALI made 4.90 mistakes without asking and, "With questions, performance improved further: mistakes dropped substantially to" 4.10 for the small model and 3.12 for the large one, with "On average, the robot asked 1.94" questions per interaction.[^c6] That comparison switches the entire question module on and off. No run reported here varies C_max, C_min or T_q, or turns the time dependence off, so the refractory term has no effect measured on its own.

## Limits

- The refractory term is not isolated. The reported gains belong to asking in general, and the timing rule is one part of that module.
- The slices of the paper I read do not give values for C_max, C_min or T_q, so I cannot say how fast the cost recovers in the runs reported. The paper also does not say what units the costs are in, while it compares them directly with an entropy. My inference: the threshold's meaning depends on that unstated choice.
- The cost depends only on time since the last question (equation 3). It does not vary with what is asked, how long the answer will take, or how hard it is to give. My inference: a one-word question and a long one cost the same to ask.
- The log(n_goals) scaling is justified in words only. It is not compared with an unscaled version.
- The evaluation is simulated plus a proof-of-concept real-world cooking task.[^c7] The paper names "studying human perceptions of clarifying questions in real deployments" as future work.[^c8] Whether people accept a robot's spacing of questions in that way is not tested.
- The rule is a design choice, not a result from theory. The paper says the cost model is inspired by an earlier work; the slices I read do not show that work's evidence.

## Related

- [[expected-information-gain]] — the same paper chooses the question by expected entropy reduction; this note covers only the decision of when to ask
- [[net-expected-value-of-alerting]] — the benefit-versus-interruption rule for notifications; its cost depends on the user's attentional state, not on the dialogue's history, and it has no refractory term
- [[activation-gate]] — a threshold that rises with interruption cost and falls with urgency, the same trade-off in another formalism
- [[tool-call-evpi-question-selection]] — asks only when a belief-scaled threshold is passed; its cost term is per-aspect redundancy, not time since the last question
- [[clarification-timing-decay]] — how the value of asking falls over a trajectory; the refractory cost is a different axis, in which the cost of asking rises right after a question

[^c1]: arxiv-2512-04453 — "immediately after asking, the interruption cost is high and then decreases linearly toward a minimum"
[^c2]: arxiv-2512-04453 — "enough that reducing it is worth the interruption"
[^c3]: arxiv-2512-04453 — "to discourage repeated interruptions"
[^c4]: arxiv-2512-04453 — "Since the value of resolving uncertainty increases with the number of plausible goals"
[^c5]: arxiv-2512-04453 — "The robot must decide when to ask a question, what question to ask and how to use the answer to reduce uncertainty over goals"
[^c6]: arxiv-2512-04453 — "With questions, performance improved further: mistakes dropped substantially to"
[^c7]: arxiv-2512-04453 — "simulated and proof-of-concept real-world collaborative cooking tasks"
[^c8]: arxiv-2512-04453 — "studying human perceptions of clarifying questions in real deployments"
