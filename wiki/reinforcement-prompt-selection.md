---
description: "A reinforcement-learning policy that picks a prompt strategy from a discrete pool each dialogue turn, rewarded by the fraction of the remaining gap to a user's concealed information it closes."
aliases: ["RPS", "Reinforcement Prompt Selection"]
sources: ["arxiv-2604-13817"]
---
# Reinforcement prompt selection

> Which questioning *style* to use next, not which question — turned into
> a discrete action a policy learns to pick from a fixed pool.

## Definition / Mechanism

Reinforcement Prompt Selection (Wang et al. (2026)'s
RPS) formulates the choice of *how to ask*
in open-ended, multi-turn dialogue as a sequential decision problem: the
action space is not a candidate question but a small, predefined pool of
prompt strategies (e.g. direct, precise, adversarial), each one a distinct
elicitation style that is combined with the model's current state to
produce the actual query text. "At each round t, the model selects a
prompt at ∈ A, where A is a predefined pool of prompts that defines the
action space. Each prompt in A corresponds to a distinct information
elicitation strategy (e.g., direct, precise, adversarial). The policy
πθ (at | st ) maps the current state st to a probability distribution over
these prompts."[^c1]

The state is the pair of what the model already knows and the dialogue so
far; the model updates its running estimate of the user's information by
appending whatever a source's response yields, then re-estimates. The
reward is not raw information gain but a *normalized* gain: the fraction
of the remaining distance to the true information that one round closes,
$r_t = \frac{d(\hat I_{t-1}, I) - d(\hat I_t, I)}{d(\hat I_{t-1}, I)}$.
"The reward rt is defined as a normalized information gain, measuring how
much the estimated information Ît moves closer to the ground-truth user
information I relative to the previous round."[^c2]

The normalization is load-bearing, not cosmetic: dividing by the remaining
distance keeps the reward from vanishing as the model's estimate
converges, which a raw (un-normalized) information-gain reward would do —
"it stabilizes reward signals when the information gap is large and
prevents the reward from vanishing as the model's estimate improves,
ensuring continued learning even in later stages."[^c3]

The policy is trained (DDPG in a synthetic Gaussian-mixture testbed with a
continuous query space, DQN in the LLM-dialogue setting with the discrete
prompt pool as the action space) against a random-query baseline and, in
the LLM setting, against fixed single-strategy prompting, an
LLM-regenerated adaptive-prompt baseline, and two prior discrete-prompt
optimizers (RLPrompt, GRIPS) retrofitted with the same reward. On IELegal,
a benchmark the paper builds from real criminal-court case narratives
where facts are labeled positive / neutral / negative by their
implications for the defendant (a proxy for how reluctant a source is to
disclose them), RPS's selected strategy recovers more of the ground-truth
case information than every baseline by the end of the dialogue. "In
IELegal, RPS significantly outperforms static prompt baselines,
demonstrating its effectiveness in uncovering relevant and potentially
concealed information."[^c4]

## Limits

The claimed effect rests on two testbeds the authors themselves built: a
Gaussian-mixture simulation with a hand-specified disclosure model, and
IELegal, a single-domain (Chinese criminal case) benchmark whose
ground-truth reference facts and positive/neutral/negative labels are
themselves LLM-extracted rather than human-annotated. The action space is
a small, hand-authored pool of prompt *styles*, not an open space of
candidate questions or axes — RPS decides which style to use, not what to
ask about, so it does not by itself establish a general question-scoring
or axis-selection mechanism. The paper reports this as a first,
theoretical-grounding study and names extension to other domains
(healthcare) and to time-varying user models as future work rather than
demonstrated results.

## Related

- [[expected-information-gain]]
- [[information-gain-reward]]
- [[amortised-sequential-information-gathering]]

[^c1]: arxiv-2604-13817 — "At each round t, the model selects a prompt at ∈ A, where A is a predefined pool of prompts that defines the action space. Each prompt in A corresponds to a distinct information elicitation strategy (e.g., direct, precise, adversarial). The policy πθ (at | st ) maps the current state st to a probability distribution over these prompts."
[^c2]: arxiv-2604-13817 — "The reward rt is defined as a normalized information gain, measuring how much the estimated information Ît moves closer to the ground-truth user information I relative to the previous round."
[^c3]: arxiv-2604-13817 — "it stabilizes reward signals when the information gap is large and prevents the reward from vanishing as the model’s estimate improves, ensuring continued learning even in later stages."
[^c4]: arxiv-2604-13817 — "In IELegal, RPS significantly outperforms static prompt baselines, demonstrating its effectiveness in uncovering relevant and potentially concealed information."
