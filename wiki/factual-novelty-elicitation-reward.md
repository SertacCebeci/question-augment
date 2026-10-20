---
description: "A reward for training an information-eliciting agent from a fixed corpus of real dialogues, scored by the named entities newly introduced in the respondent's reply, not by the agent's own utterance."
aliases: ["factual novelty reward", "entity-based elicitation reward", "YIELD reward signal"]
sources: ["arxiv-2604-10968"]
---
# Factual-novelty elicitation reward

> Reward the elicitor for what the respondent's reply newly contains, not
> for anything about the elicitor's own question: "the elicitor is
> rewarded in proportion to each newly introduced entity."

## Definition / Mechanism

De Lima & Yang train an elicitation policy $\pi_\theta$ offline on YIELD, a
26M-token corpus of real human-to-human elicitation dialogues (academic
interviews, judicial proceedings, journalistic investigations, oral
history), with no live respondent and no LLM judge. Each elicitor turn
$A_t$ is assigned a scalar reward from the respondent's *next* reply
alone: a spaCy NER model extracts entities from every utterance and
maintains a cumulative set $E_{\le t}$ of everything mentioned so far;
after the elicitor's turn, the respondent's reply is scanned for entities
not yet in that set, and $R_{t+1} = E_{t+1} \setminus E_{\le t}$ — the
elicitor is credited only for entities the respondent introduces that
were not already on the table.[^c1]

Two constraints stop the signal from being gamed by the design alone:
entities the elicitor itself utters are added to the cumulative set but
earn no reward, so the elicitor cannot pre-empt and later collect credit
for the respondent merely repeating them; and a repeated entity anywhere
in the dialogue yields no further credit, so an elicitor that lets the
conversation linger on already-covered ground accrues fewer rewards over
time.
[^c2]

Rewards are converted to a return-to-go with a $\gamma = 0.9$
discount over the full dialogue before being used as the offline-RL
target, so a turn's weight reflects its effect on everything that follows
it, not only the immediate reply.

The policy is fit with Advantage-Weighted Regression (AWR): a LoRA-adapted
causal LM produces both the policy and, via a linear value head, a
state-value estimate; the advantage (return-to-go minus predicted value)
reweights each training example's log-likelihood loss, so utterances that
led to higher factual-novelty returns are up-weighted relative to
standard supervised fine-tuning, where every example counts equally.[^c3]

Against a prompted baseline, offline-RL and supervised fine-tuning on the
same reward-annotated corpus both bring model behavior toward the real
elicitor distribution: reported micro-perplexity on held-out human
elicitor turns drops from 46.9 (prompted Llama-3.1-8B, Academic domain) to
12.5 (the offline-RL variant).
[^c4]

Response length drops correspondingly,
from 39.5 tokens to 11.6, matching rather than merely resembling real
elicitors' far shorter turns, and the paper reports dialogue-level offline
optimization as "competitive with" supervised fine-tuning, corroborated by
a separate human evaluation.[^c5]

## Why it matters

[[elicited-response-reward]] scores an elicited-response reward built the
same way — on the *answer* the question pulled out, not the question
itself — but as a weighted sum of goal-relevance (LLM-judged similarity to
a target conclusion), lexical novelty (a lengthnormalized Distinct-N over
tokens) and succinctness, trained online against a simulated respondent in
one adversarial domain. This reward strips that composite down to novelty
alone, measured at the level of named entities rather than tokens, and
trains entirely offline from a fixed corpus of real (not simulated)
dialogues across four different elicitation domains — showing the single
component is enough, on its own, to shift a general-purpose LLM's
elicitation behavior toward the human distribution without any judge
model or live respondent in the loop.

## Limits

Factual novelty is a proxy for informational gain, not informational gain
itself: it counts new named entities, so an elicitor could accrue reward
by fishing for named-entity-dense trivia while missing unnamed but
consequential facts (opinions, causal claims, numeric detail without a
named referent), and the paper's own mitigation against gaming — listing
entities in one utterance — works only because the reward is computed
against curated, real human–human replies, not a live or generated
respondent that could be exploited the same way — a risk the paper
names explicitly: "this risk is mitigated here because rewards are
computed on curated, real human–human dialogues." The result is reported
as pilot-scale (three foundation models, one training run each, no
seed-variance reported), and offline-RL's own micro-perplexity is
slightly higher than supervised fine-tuning's, "consistent with
advantage-weighted training prioritizing longer-horizon behavior over
token-level likelihood" rather than clearly superior to it.[^c6]

## Related

[[elicited-response-reward]] · [[questioning-diversity]] · [[expected-information-gain]] · [[curiosity-value-function]]

[^c1]: arxiv-2604-10968 — "the elicitor is rewarded in proportion to each newly introduced entity."
[^c2]: arxiv-2604-10968 — "Entities produced by the elicitor are also added to the cumulative entity set, but they do not contribute reward, so that entities subsequently repeated by the respondent are not misattributed."
[^c3]: arxiv-2604-10968 — "each w̄i scales the contribution of sample i within the mini-batch B according to its estimated advantage, departing from standard supervised finetuning where all examples contribute equally regardless of their quality."
[^c4]: arxiv-2604-10968 — "the prompted Llama-3.1-8B averaged a micro perplexity of 46.9 in Academic Interviews, while the ORL model averaged 12.5"
[^c5]: arxiv-2604-10968 — "the prompted Llama-3.1-8B averaged 39.5 tokens in Academic Interviews, while the ORL model averaged 11.6 tokens"
[^c6]: arxiv-2604-10968 — "this risk is mitigated here because rewards are computed on curated, real human–human dialogues."
