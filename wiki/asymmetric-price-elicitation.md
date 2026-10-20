---
description: "An ascending price set from a small random sample removes most bidders after one bit each, so elicitation concentrates on the few contenders near the winning value instead of on every bidder."
aliases: ["asymmetric elicitation", "sample-driven price ascent", "uneven information extraction in ascending auctions"]
sources: ["doi-10-48550-arxiv-2208-11787"]
---
# Asymmetric price elicitation

In a standard English auction every withdrawing bidder reveals roughly her own valuation, because the clock must pass her value before she drops out. Anagnostides, Fotakis and Patsilinakos change who is asked. In each round the mechanism runs a sub-auction on a random sample of agents: "at every round of the auction we simulate a sub-auction on a random sample," and the sub-auction's clearing price is the price announced to everyone, "in the sub-auction as the price of the round."[^c1] Only the sampled agents are consulted in detail; the others are compared against one price.

The consequence is an uneven information pattern. Most bidders are eliminated after the first round, each having revealed a single bit: "agents will be eliminated after the first round, having only revealed a single bit from their."[^c2] The bidders who matter are the ones near the winning value; by the paper's account they will have to disclose a substantial amount of information.[^c3] The paper's contrast with the English auction is that there "every withdrawing bidder approximately reveals her" valuation.[^c4]

The size of the sample is the dial. A larger sample lowers the share of agents who stay active into the next round: "the fraction of the agents that will remain active in the forthcoming round gets gradually smaller" as the sample grows (Lemma 4.5).[^c5] The same sample size also raises the cost of simulating the sub-auction, so the sample "induces a trade-off between two terms."[^c6] The total bits are thus split between a bulk that pays one bit each and a small contested set that pays for the detail.

The paper offers a reason to regard this as a good pattern: "arguably, this property is desirable."[^c7] That is the authors' judgment, not a measured welfare or privacy gain. A related design, for unit-demand multi-unit auctions, applies the same idea with two prices per round: "Our proposed auction announces in every round two separate prices," and recurses on the agents between them.[^c8]

## Limits

- The asymmetry is a property of the bit pattern. The paper does not show that the bits elicited from contenders are the ones that determine welfare, revenue or the outcome; "arguably" is the only support offered for desirability.
- The one-bit-per-bidder pattern holds in expectation over a random sample, with distinct valuations assumed. Ties are not analysed beyond the bound that they can only truncate communication, and the survivor-share result is stated for the sample-based rule, not for arbitrary sampling.
- The sample must have at least two agents for the second-price rule to be defined.[^c9] Below that, the pattern is not defined.
- The multi-unit two-price variant was read only in the introduction's description. I did not check its proofs, so the claim that it has the same asymmetric pattern is my inference from the description, not a result I verified.
- The mechanism's incentive properties depend on the sub-auction type (see [[auction-communication-complexity]]); the asymmetry itself says nothing about truthfulness.

## Related

- [[auction-communication-complexity]] — the cost measure in bits per bidder that this pattern is designed to bring down toward one.
- [[median-cost-sensitivity]] — the sampling step that makes the sub-auction cheap, in facility location.
- [[one-bit-mean-estimation]] — another setting where a one-bit query is the unit and adaptivity's value is the question, here for estimation rather than auctions.

[^c1]: doi-10-48550-arxiv-2208-11787 — "in the sub-auction as the price of the"
[^c2]: doi-10-48550-arxiv-2208-11787 — "agents will be eliminated after the first round, having only revealed a single bit from their"
[^c3]: doi-10-48550-arxiv-2208-11787 — "amount of information"
[^c4]: doi-10-48550-arxiv-2208-11787 — "every withdrawing bidder approximately reveals her"
[^c5]: doi-10-48550-arxiv-2208-11787 — "fraction of the agents that will remain active in the forthcoming round gets gradually smaller"
[^c6]: doi-10-48550-arxiv-2208-11787 — "induces a trade-off between two terms"
[^c7]: doi-10-48550-arxiv-2208-11787 — "arguably, this property is desirable"
[^c8]: doi-10-48550-arxiv-2208-11787 — "Our proposed auction announces in every round two separate prices"
[^c9]: doi-10-48550-arxiv-2208-11787 — "Naturally, we assume that the sample contains at least 2 agents"
