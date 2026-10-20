---
description: "Human and simulated-AI votes weigh equally in a broad screen and at 7:1 in favour of humans in an expert stage, a staged way to let scarce expert judgment dominate the final list."
aliases: ["staged human-AI voting", "limited voting with weighted voters", "approval-then-limited voting"]
sources: ["arxiv-2602-03849"]
---
# Expert-weighted stage voting

A candidate pool can be narrowed in stages, and the weight of each kind of voter can change from one stage to the next. Zhao et al. run two stages on a 100-candidate pool. The first is a broad screen: "Approval Voting, allowing voters to cast one vote for any candidate they deemed viable without" a cap, cast by 30 human graduate students and 70 simulated agents at the same level.[^c1] Here "human and AI votes" count equally, and the top 30 advance.[^c2]

The second stage is a narrower one. Each voter, human or simulated, "was allocated exactly 10 votes to distribute among the candidates", so every ballot is a fixed budget rather than an unlimited endorsement.[^c3] The weights then change: "each human vote was assigned a weight of 7, whereas each AI vote was assigned a weight of 1." The stated purpose is "to prioritize nuanced expert judgment at this stage".[^c4] The stage is run by 10 human professors and 30 simulated professor-level agents, and the top two candidates from it go to the final list.

Two mechanisms are at work and the paper does not separate them. The first is the vote rule: approval with no cap lets a voter endorse many candidates, so the first stage rewards breadth, while a fixed budget forces each voter to choose, so the second stage rewards a ranking (my reading). The second is the weighting: in the second stage the 10 humans and 30 simulated voters each hold 10 votes, so the human ballots carry 700 of 1,000 weighted votes. The humans are a minority by head-count and a 70% majority by weight. The weighting is a dial on how much a small expert ballot counts against a larger cheap panel. A cross-model step precedes both stages: six LLMs each cast "100 approval votes" over a 600-candidate pool, and the 100 with the most votes go forward.[^c5] That step is an ensemble of models rather than of people, and it has no human weight at all.

What transfers is the parameter, not the number. A staged panel can give a cheap, large voter set the breadth, and a small expert set the final say, and the ratio between them is a choice the designer makes. The paper does not show that 7:1 is the right ratio, only that it is the one used.

## Limits

- No ablation. The text does not compare the 7:1 weighting with equal weights or another ratio, so it cannot say what the weighting changes in the final ten. (my reading)
- The simulated voters are described as built to "match this expertise", and the authors' own check of that match is the JS distance table; no independent validation of the personas is reported.[^c6]
- Pool size and voter weighting change at the same time between the stages, so the text cannot attribute a difference in the outcome to either one.
- Each stage is one run. The text reports no variance across seeds or across the choice of simulated personas, and it does not say whether the same ten would come out again.
- The panel sizes are small (10 professors, 30 graduate students in the human parts) and the human voters are the paper's own panel; the results describe that panel, not a general method for research prioritisation.

## Related

- [[retrospective-prospective-judgment-gap]] — the agreement between these simulated voters and the human panel is lower for open questions than for established breakthroughs.
- [[effective-independent-votes]] — what a pool of correlated voters is worth; the 70 simulated voters here are such a pool, and the paper does not estimate its effective size.
- [[cross-provider-judge-ensemble]] — pooling judges from several providers; the six-LLM approval step is the same cross-model idea applied to proposals rather than to verdicts.

[^c1]: arxiv-2602-03849 — "Approval Voting, allowing voters to cast one vote for any candidate they deemed viable without"
[^c2]: arxiv-2602-03849 — "were weighted equally, and the 30 candidates with the highest total approval votes advanced to the"
[^c3]: arxiv-2602-03849 — "was allocated exactly 10 votes to distribute among the candidates"
[^c4]: arxiv-2602-03849 — "was assigned a weight of 7, whereas each AI vote was assigned a weight of 1."
[^c5]: arxiv-2602-03849 — "with each model casting 100 approval votes"
[^c6]: arxiv-2602-03849 — "agents simulated to match this expertise"
