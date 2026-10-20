---
description: "A questioner paid the negation of the answerer's score wins by breaking the answerer, e.g. with gibberish; paying it for the wrong category keeps it aiming at a plausible failure."
aliases: ["non-zero-sum attacker", "category-swap attacker reward", "non-cooperative attacker-defender game"]
sources: ["arxiv-2512-20806"]
---
# Non-zero-sum attacker reward

When a questioner and an answerer are trained against each other, the simplest payoff is the negation of the answerer's: whatever the answerer loses, the questioner wins. Paulus et al. reject this for the questioner. Their judge sorts an answer into a good deflection on a harmful prompt or a compliant reply on a benign one. Under negation, the questioner can win with an answer that is neither: "Defender to generate gibberish, it succeeds according to"[^c2] the judge, because "gibberish is neither a good deflection nor a"[^c1] compliant reply. The authors say the negated game "introduces an imbalance by making the task"[^c3] too easy for the questioner, so that "will not find a good approximation of the equilibrium, and"[^c4] the defender stays weak.

The fix does not invert the preferences. "Instead of inverting the preferences, we simply swap the"[^c5] rewards of the two categories. On a benign seed the attacker is paid when the defender deflects, and on a harmful seed when the defender complies. The stated aim is that the attacker tries to fool the defender into placing the query in the other category, rather than producing output that breaks the judge. In the paper's words the attacker "will try to fool the Defender"[^c6], and the reward is still a preference between two attack queries and their responses, so the same pairwise machinery applies (see [[pairwise-judge-over-scalar-reward]]).

**Mechanism, concretely.** For each seed the attacker proposes a rewrite; the defender answers it; a pairwise judge compares two rewrites by the category of the defender's answer. The attacker is paid for the answer that the swapped category rewards. A gibberish answer is therefore worth nothing to the attacker: it is neither the deflection nor the compliance the category needs, so it does not register as a win in either direction.

**What transfers to asking (my inference).** A question generator paid for "any wrong answer" from an answerer can find the same exploit: incoherent or unanswerable questions can make an answerer fail without the failure meaning anything. Paying for a wrong answer within a named category keeps the generator on questions that have a plausible reading. This was not tested in the text; it is the transfer I would check first.

**What does not transfer.** The paper's categories are harmful and benign, a binary split. Most questioning has no such split, and the swap has to be re-derived for whatever categories a question must be classified into. Nash equilibrium is a game-theoretic object, and the paper's existence result is a claim about the same game in its tabular form, not about the trained networks.

## Limits

- The gibberish argument and the claim that the negated game yields a weak defender are the authors' argument. The sections I read contain no run of the negated game, so neither is measured here.
- The equilibrium result is for tabular policies: "strongly concave in the tabular"[^c8] policies have a unique optimum. The trained networks only approximate it: "Unfortunately we do not have access to the equilibrium policies"[^c7].
- The categories are a two-way split of seeds. A questioner over open-ended questions has no such split, and the paper gives no alternative.
- The transfer to question generation is my inference, untested in this work.

## Related

- [[faithfulness-gated-attack-reward]] — the second constraint on the same attacker payoff: a rewrite must keep the seed's meaning.
- [[pairwise-judge-over-scalar-reward]] — the judge whose winner and loser feed this payoff.
- [[llm-red-teaming]] — the wider practice of one model probing another, in which this reward design sits.
- [[co-evolving-rubric-generator]] — another case of a second model trained beside the policy, so that the target moves.

[^c1]: arxiv-2512-20806 — "gibberish is neither a good deflection nor a"
[^c2]: arxiv-2512-20806 — "Defender to generate gibberish, it succeeds according to"
[^c3]: arxiv-2512-20806 — "we argue that this introduces an imbalance by making the task"
[^c4]: arxiv-2512-20806 — "will not find a good approximation of the equilibrium, and"
[^c5]: arxiv-2512-20806 — "Instead of inverting the preferences, we simply swap the"
[^c6]: arxiv-2512-20806 — "the Attacker will try to fool the Defender"
[^c7]: arxiv-2512-20806 — "Unfortunately we do not have access to the equilibrium policies"
[^c8]: arxiv-2512-20806 — "strongly concave in the tabular"
