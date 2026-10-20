---
description: "Measures an auction by the expected number of bits elicited from bidders rather than by rounds: a sealed bid hears every valuation in full, while a sampled ascent can approach one bit per bidder."
aliases: ["communication complexity of auctions", "bits elicited per bidder", "communication complexity of mechanisms"]
sources: ["doi-10-48550-arxiv-2208-11787"]
---
# Auction communication complexity

Anagnostides, Fotakis and Patsilinakos measure a mechanism by the expected number of bits it reads from its participants: "the expected number of bits elicited from the participants during the interaction process."[^b1] Every valuation is written in k bits, and k is treated as a constant that does not grow with the number of agents n.[^b2] The unit is therefore bits per bidder, not queries and not rounds, and the question becomes how the total grows as n grows.

Under this measure the standard formats separate sharply. A sealed-bid (Vickrey) auction is a direct revelation mechanism that takes "the entire private information from the n agents," so its cost is n times k bits.[^b3] An English auction is the other pole: it is exponential communication of the order n·2^k in the worst case,[^b4] because a standard ascending format "necessitates covering the entire valuation space."[^b9]

The floor is set by a lower bound. Any mechanism that determines the agent with the highest valuation with probability 1 must elicit at least n bits,[^b5] so the trivial floor is one bit per bidder.[^b6] The paper's claim is that Vickrey's rule can be implemented at an expected communication of one bit plus a term that vanishes per bidder, "asymptotically matching the trivial lower bound."[^b7]

The mechanism that achieves this is a sampled ascending auction. In each round a faithful second-price sub-auction runs on a random sample, and the sub-auction's clearing price is announced as the round's price.[^b8] Theorem 4.8 bounds the expected cost by a term of order (1+ε)n plus Q(c;k) log n, where Q is the worst-case communication of the sub-auction and c is the sample size. The sample size "induces a trade-off between two terms": a larger sample removes more bidders per round, while the sub-auction costs more to simulate.[^b10] My reading: since Q(c;k) is fixed once c and k are fixed, the log n term is lower order in n, so the leading constant is 1+ε. The paper states this as its asymptotic result, under the constant-k assumption (Corollary 4.9).[^b12]

The same accounting covers other settings. For m items with additive values, a sequential implementation needs n·m bits, and the paper's simultaneous encoding follows the principle to "encode the more likely events with fewer bits."[^b13] For unit-demand multi-unit auctions the paper reports "leading again to the optimal" bound through a two-price ascending format.[^b14]

## Limits

- The unit is an expected count of bits under the paper's own model. It says nothing about cognitive cost, strategic effort, or the information a bidder keeps back; the paper's introduction motivates the measure by those concerns but does not measure them.
- The results are asymptotic in n with k fixed. The paper says so directly: "We will mainly assume that k is a parameter independent of" the number of agents.[^b2] The sample size analysis is not tight: "We do not claim that our analysis w.r.t. the size of the sample is tight."[^b11]
- Incentives depend on the sub-auction. With an English sub-auction the mechanism is obviously strategy-proof (Proposition 4.3).[^b15] With a sealed-bid sub-auction, dominant-strategy truthfulness holds only if the announced prices are non-decreasing, which the paper guarantees by using the sub-auction's clearing price as a reserve; "Otherwise, truthful reporting is not" necessarily dominant.[^b16]
- Ties are assumed away in the analysis; "as this yields an upper bound on the actual communication complexity," since ties can only truncate communication.[^b17]
- The sampling bound requires the sample to contain at least two agents, so that a second-price rule is defined.[^b18]

## Related

- [[median-cost-sensitivity]] — the same sample-then-decide device, used there for a facility location's social cost rather than for the bits an auction reads.
- [[asymmetric-price-elicitation]] — the pattern of who reveals how much, which is what makes the total bit count near one per bidder.
- [[one-bit-mean-estimation]] — also a one-bit-per-query setting in which adaptivity is the question, but the cost there is samples for estimation, not bits per participant.
- [[separation-oracle-preference-elicitation]] — counts preference queries rather than bits, a different unit for the same question of how much must be asked.
- [[huffman-coding]] — the multi-item encoding applies the same principle, that likely events deserve fewer bits, though the paper does not appeal to Huffman's construction in the parts I read.

[^b1]: doi-10-48550-arxiv-2208-11787 — "the expected number of bits elicited from the participants during the interaction process"
[^b2]: doi-10-48550-arxiv-2208-11787 — "We will mainly assume that k is a parameter independent of"
[^b3]: doi-10-48550-arxiv-2208-11787 — "private information from the n agents"
[^b4]: doi-10-48550-arxiv-2208-11787 — "exponential communication of the order"
[^b5]: doi-10-48550-arxiv-2208-11787 — "Every mechanism that determines the agent with the highest valuation"
[^b6]: doi-10-48550-arxiv-2208-11787 — "trivial lower bound of 1 bit per bidder"
[^b7]: doi-10-48550-arxiv-2208-11787 — "asymptotically matching the trivial lower bound"
[^b8]: doi-10-48550-arxiv-2208-11787 — "algorithm A that faithfully simulates a second-price auction"
[^b9]: doi-10-48550-arxiv-2208-11787 — "a standard ascending format necessitates covering the entire valuation space"
[^b10]: doi-10-48550-arxiv-2208-11787 — "induces a trade-off between two terms"
[^b11]: doi-10-48550-arxiv-2208-11787 — "We do not claim that our analysis w.r.t. the size of the sample is tight"
[^b12]: doi-10-48550-arxiv-2208-11787 — "if k is a constant independent of n"
[^b13]: doi-10-48550-arxiv-2208-11787 — "encode the more likely events with fewer bits"
[^b14]: doi-10-48550-arxiv-2208-11787 — "leading again to the optimal"
[^b15]: doi-10-48550-arxiv-2208-11787 — "If A simulates an English auction, AscendingAuctionViaSampling is"
[^b16]: doi-10-48550-arxiv-2208-11787 — "is dominant strategy incentive compatible if the sequence of announced prices is non-decreasing"
[^b17]: doi-10-48550-arxiv-2208-11787 — "as this yields an upper bound on the actual communication complexity"
[^b18]: doi-10-48550-arxiv-2208-11787 — "the sample contains at least 2 agents, so that the second-price rule is properly"
